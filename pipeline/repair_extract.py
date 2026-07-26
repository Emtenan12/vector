"""
Repair-path extraction for PDFs whose fonts carry a broken/absent ToUnicode
map, where every glyph code sits at a constant offset from its true ASCII
codepoint.

Why this module exists (confirmed on ADP_2-0.pdf, 88 pages):
pymupdf's default text extraction maps those unmapped glyphs to U+FFFD, and
pymupdf4llm inherits that -- the whole document comes out as 97% replacement
characters and is unusable (179 chunks of pure garbage that would otherwise
be embedded and poison retrieval). The information is NOT lost at the PDF
level, though: extracting with TEXTFLAGS_DICT preserves the raw glyph codes
(e.g. "&KDSWHU\x03\x14" for "Chapter 1"), which decode by adding a constant
offset -- 29 (0x1D) for ADP_2-0. `use_glyphs=True`, pymupdf4llm's documented
escape hatch for exactly this, does not wire through in the installed
version (1.28.0), and patching TextPage.extractDICT/extractRAWDICT doesn't
intercept it either, so the repair is done here against pymupdf directly.

Critically, affected documents are NOT uniformly shifted -- ADP_2-0 mixes
correctly-encoded spans (italic defined-term runs) with shifted ones in the
same line. Decoding blindly corrupts the good spans ("Defense support of
civil authorities" -> "=aefense=support=of=civil=authorities"). So the shift
is applied per span, gated on that span actually containing control
characters, which never occur in legitimate extracted text.

Markdown structure (headings/lists) is reconstructed here from font size and
flags rather than reusing pymupdf4llm, since pymupdf4llm can't see the
repaired text.
"""
import logging
import re
from collections import Counter
from pathlib import Path

import pymupdf

logger = logging.getLogger(__name__)

# Control characters are the tell: legitimate extracted text never contains
# 0x01-0x1F apart from tab/newline/carriage-return.
_CTRL_RE = re.compile(r"[\x01-\x08\x0b\x0c\x0e-\x1f]")

# Candidate shifts to search. 29 (0x1D) is the confirmed ADP_2-0 value; the
# search makes this generalize to other broken-font documents instead of
# hardcoding one publication's quirk.
_SHIFT_CANDIDATES = range(1, 65)

_COMMON_WORDS = (
    " the ", " and ", " of ", " to ", " in ", " is ", " for ", " that ",
    " army ", " commander", " operations", " forces", " support",
)


def _decode(text: str, shift: int) -> str:
    return "".join(
        chr(ord(c) + shift) if 0x01 <= ord(c) <= (0x7E - shift) else c
        for c in text
    )


def _score(text: str) -> float:
    """How English-like is this text? Used to pick the shift empirically
    rather than trusting a hardcoded constant."""
    if not text:
        return 0.0
    low = text.lower()
    word_hits = sum(low.count(w) for w in _COMMON_WORDS)
    printable = sum(1 for c in text if c.isalnum() or c in " .,;:'\"()-\n")
    return word_hits * 10 + printable / len(text)


# A healthy document still shows a trace of control characters (stray glyphs
# in figures, dingbat bullets). Measured across this corpus: every correctly
# encoded ADP sits at <=0.2%, while the broken-font ADP_2-0 sits at 16%. The
# gate is set at 5% -- well clear of both -- because taking the repair path
# on a healthy document is itself harmful: it bypasses pymupdf4llm and so
# loses the page-break noise patterns clean.py depends on (observed as
# noise_removed dropping to 0 on ADP_1-01 when this fired spuriously).
_CORRUPTION_THRESHOLD = 0.05


def detect_shift(doc: pymupdf.Document, sample_pages: int = 12) -> int | None:
    """Return the constant glyph->ASCII offset for this document, or None if
    the document isn't shift-corrupted. Determined empirically by decoding a
    sample and scoring for English-likeness."""
    sample = []
    total_chars = 0
    ctrl_chars = 0
    step = max(1, doc.page_count // sample_pages)
    for pno in range(0, doc.page_count, step):
        raw = doc[pno].get_text("text", flags=pymupdf.TEXTFLAGS_TEXT)
        total_chars += len(raw)
        ctrl_chars += len(_CTRL_RE.findall(raw))
        if _CTRL_RE.search(raw):
            sample.append(raw)
        if len(sample) >= sample_pages:
            break

    if not sample or not total_chars:
        return None
    if ctrl_chars / total_chars < _CORRUPTION_THRESHOLD:
        return None

    blob = "\n".join(sample)
    best_shift, best_score = None, _score(blob)
    for shift in _SHIFT_CANDIDATES:
        s = _score(_decode(blob, shift))
        if s > best_score:
            best_shift, best_score = shift, s
    return best_shift


def _is_shifted_span(text: str) -> bool:
    return bool(_CTRL_RE.search(text))


def extract_repaired(pdf_path: Path, shift: int) -> str:
    """Extract markdown from a shift-corrupted PDF, decoding affected spans
    and reconstructing headings/lists from font metrics."""
    doc = pymupdf.open(str(pdf_path))

    # Body text size = the most common rounded span size across the document.
    sizes: Counter = Counter()
    for page in doc:
        for block in page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT).get("blocks", []):
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if span.get("text", "").strip():
                        sizes[round(span["size"], 1)] += len(span["text"])
    body_size = sizes.most_common(1)[0][0] if sizes else 10.0

    out: list[str] = []
    for page in doc:
        for block in page.get_text("dict", flags=pymupdf.TEXTFLAGS_DICT).get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                parts, max_size, bold = [], 0.0, False
                for span in line.get("spans", []):
                    text = span.get("text", "")
                    if not text:
                        continue
                    if _is_shifted_span(text):
                        text = _decode(text, shift)
                    parts.append(text)
                    max_size = max(max_size, span.get("size", 0.0))
                    # bit 4 of the span flags is the bold indicator
                    if span.get("flags", 0) & 2 ** 4:
                        bold = True

                text = "".join(parts).strip()
                if not text:
                    continue

                # Normalize bullets to markdown list items so chunk.py's
                # list-atomicity logic sees the same structure it sees in
                # pymupdf4llm's output for uncorrupted documents. Two forms
                # occur: a leading non-alphanumeric marker glyph, and a
                # literal "x " -- the latter because these documents draw
                # bullets with a Wingdings-family font, where the bullet
                # glyph sits at the 'x' codepoint and decodes to it.
                if re.match(r"^x\s+\S", text):
                    out.append("- " + text[1:].lstrip())
                    continue
                if re.match(r"^[^\w\s\"'(\[]", text) and len(text) > 2:
                    out.append("- " + text[1:].lstrip())
                    continue

                if max_size >= body_size * 1.45:
                    out.append(f"# {text}")
                elif max_size >= body_size * 1.22:
                    out.append(f"## {text}")
                elif max_size >= body_size * 1.08 and bold:
                    out.append(f"### {text}")
                else:
                    out.append(text)
            out.append("")  # blank line between blocks -> paragraph break

    return "\n".join(out)


def maybe_repair(pdf_path: Path) -> tuple[str | None, int | None]:
    """If this PDF is shift-corrupted, return (repaired_markdown, shift).
    Otherwise return (None, None) so the caller uses the normal
    pymupdf4llm path."""
    doc = pymupdf.open(str(pdf_path))
    shift = detect_shift(doc)
    if shift is None:
        return None, None
    logger.warning(
        "%s: detected broken font encoding (constant glyph offset %d) -- "
        "using repair extraction path instead of pymupdf4llm",
        pdf_path.name, shift,
    )
    return extract_repaired(pdf_path, shift), shift
