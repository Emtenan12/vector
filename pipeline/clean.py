"""
Cleaning stage: strip page-break noise (running headers/footers, page numbers,
publication dates) emitted by pymupdf4llm and rejoin paragraphs that were
split mid-sentence by a page boundary, then normalize doc_id and filter known
leaked-extraction-artifact patterns.

Evidence this is built against (see eval/extraction_eval.md): pymupdf4llm
does not emit a literal form-feed at page boundaries. Instead it emits the
page number, publication ID, publication date, and the current running
chapter/section title as separate standalone bold lines with no leading '#'
-- e.g.

    **1-6**

    **ADP 6-0**

    **31 July 2019**

    **Introduction to Mission Command**

Real headings always carry a markdown '#' prefix in pymupdf4llm's output;
these noise lines never do, which is the primary structural signal used
below. Confirmed to split sentences mid-word ("a single commander" -> "a" /
noise / "single commander") when the text before the break does not end in
terminal punctuation -- the trigger condition for the rejoin logic.
"""
import re
from dataclasses import dataclass, field

# A pymupdf4llm noise line is an entire line consisting of a single bold
# span, standing alone between blank lines, never prefixed with '#'.
_BOLD_LINE_RE = re.compile(r"^\*\*(.+?)\*\*\s*$")

# Page numbers: roman numerals (front matter: i, ii, iii, ...) or arabic,
# optionally chapter-prefixed (1-6, 4-12, A-3).
_PAGE_NUM_RE = re.compile(r"^(?:[ivxlcdm]{1,6}|[a-zA-Z]?-?\d{1,4}(?:-\d{1,3})?)$", re.I)

# Publication dates as they appear in ADP running footers, e.g. "31 July
# 2019". Tolerates the replacement-char font-encoding corruption confirmed
# on the Word-regenerated ADP_3-0.pdf sample ("2� M���� 2025").
_MONTHS = ("January|February|March|April|May|June|July|August|September"
           "|October|November|December")
_DATE_RE = re.compile(
    rf"^[\d�]{{1,2}}\s+(?:{_MONTHS}|[A-Za-z�]{{3,10}})\s+\d{{4}}$"
)

# Terminal punctuation that means "this is a real paragraph/sentence/list-item
# boundary, don't rejoin across it even if noise follows."
_TERMINAL_PUNCT_RE = re.compile(r'[.!?:;"\')’”]\s*$')

# Known leaked prompt-fragment wordings (finding #4). Both are checked
# case-insensitively as substrings.
LEAK_PATTERNS = [
    "replace this line with a description of the figure",
    "verify the figure: ocr of chart labels is unreliable",
]

_CID_ARTIFACT_RE = re.compile(r"\(cid:\d+\)")

# Table-of-contents / front-matter navigation rows: pymupdf4llm renders a
# PDF's ToC as a markdown table whose cells are dot-leader page references,
# e.g. "PREFACE.................................................... iii".
# Confirmed on ADP_1-01.pdf: this becomes one ~2500-token table block with
# zero retrieval value (it's page navigation, not doctrine content) that
# would otherwise dominate a chunk as a forced atomic-unit overflow. The
# prior pipeline's own documented cleaning step explicitly dropped ToCs;
# this reproduces that with an evidence-based detector rather than a
# position-based guess (front matter isn't always at a fixed offset).
_TABLE_ROW_RE = re.compile(r"^\s*\|")
_DOT_LEADER_RE = re.compile(r"\.{4,}")


def _strip_toc_tables(text: str) -> tuple[str, int]:
    lines = text.split("\n")
    out: list[str] = []
    removed = 0
    i = 0
    n = len(lines)
    while i < n:
        if _TABLE_ROW_RE.match(lines[i]):
            j = i
            table_lines = []
            while j < n and (_TABLE_ROW_RE.match(lines[j]) or lines[j].strip() == ""):
                if _TABLE_ROW_RE.match(lines[j]):
                    table_lines.append(lines[j])
                j += 1
            dot_leader_rows = sum(1 for l in table_lines if _DOT_LEADER_RE.search(l))
            if table_lines and dot_leader_rows / len(table_lines) >= 0.5:
                removed += 1
                i = j
                continue
            out.extend(lines[i:j])
            i = j
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), removed


def _pub_id_variants(doc_id: str) -> list[str]:
    """Generate regex-escaped variants of a doc's own publication ID as it
    might appear in a running header, e.g. doc_id 'ADP_6-0' -> 'ADP 6-0',
    'ADP-6-0', 'ADP6-0'."""
    base = doc_id.replace("_", " ").replace("-", " ", 1)  # "ADP 6-0" style
    kind, rest = doc_id.split("_", 1) if "_" in doc_id else (doc_id, "")
    variants = {doc_id, doc_id.replace("_", " "), doc_id.replace("_", "-")}
    if rest:
        variants.add(f"{kind} {rest}")
        variants.add(f"{kind}-{rest}")
        variants.add(f"{kind}{rest}")
    return sorted(variants, key=len, reverse=True)


@dataclass
class CleanResult:
    text: str
    noise_lines_removed: int = 0
    rejoins_performed: int = 0
    leaks_removed: int = 0
    cid_artifacts_found: int = 0
    toc_tables_removed: int = 0


# Runs of replacement characters, left by a font whose ToUnicode map failed
# on part of a line (confirmed on ADP_5-0's running header/date field, which
# pymupdf4llm promotes to a markdown heading -- so it survives the bold-noise
# rule, carries no readable text, and gets adopted as a section heading whose
# breadcrumb is then prepended to every chunk beneath it). Deleting these
# runs outright is safe: the characters are already unrecoverable at this
# stage, so they can only add noise to an embedding.
#
# Deliberately NOT handled by dropping such headings entirely -- tried that,
# and it was worse: the splitter then fell back to a partially-corrupted
# parent heading and propagated it to more chunks (8,787 -> 23,116
# replacement chars corpus-wide).
_REPL_RUN_RE = re.compile(r"�+")


def _is_noise_line(stripped: str, pub_id_patterns: list[re.Pattern],
                    running_title_counts: dict[str, int]) -> bool:
    m = _BOLD_LINE_RE.match(stripped)
    if not m:
        return False
    content = m.group(1).strip()
    if _PAGE_NUM_RE.match(content):
        return True
    if _DATE_RE.match(content):
        return True
    # A bold line that is nothing but replacement characters is a running
    # header whose font failed to decode (confirmed on ADP_5-0: the date
    # field renders as "**??????? 2019**" and the page-id field as pure
    # replacement chars). It carries no content, and left in place it
    # becomes the opening line of the chunk that follows it.
    if content and all(c == "�" or c.isspace() for c in content):
        return True
    for pat in pub_id_patterns:
        if pat.match(content):
            return True
    # Running chapter/section title: recurs verbatim >= 3x across the
    # document. This check runs on a pre-computed frequency table (see
    # clean_text) so a one-off bold line (unusual, since real headings use
    # '#') is not misclassified as noise.
    if running_title_counts.get(content, 0) >= 3:
        return True
    return False


def _find_running_titles(lines: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in lines:
        m = _BOLD_LINE_RE.match(line.strip())
        if not m:
            continue
        content = m.group(1).strip()
        if _PAGE_NUM_RE.match(content) or _DATE_RE.match(content):
            continue
        counts[content] = counts.get(content, 0) + 1
    return counts


def clean_text(raw_text: str, doc_id: str) -> CleanResult:
    """Strip page-break noise and rejoin mid-sentence splits, then filter
    known leaked-artifact patterns. Operates on pymupdf4llm markdown output."""
    pub_id_patterns = [re.compile(re.escape(v) + r"$", re.I)
                        for v in _pub_id_variants(doc_id)]

    lines = raw_text.split("\n")
    running_title_counts = _find_running_titles(lines)

    out_lines: list[str] = []
    noise_removed = 0
    rejoins = 0

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if stripped and _is_noise_line(stripped, pub_id_patterns, running_title_counts):
            # Consume this noise line and any immediately-blank lines around
            # it (pymupdf4llm surrounds each noise line with blank lines).
            noise_removed += 1
            i += 1
            while i < n and lines[i].strip() == "":
                i += 1
            # Consume a contiguous run of further noise lines (page number,
            # pub id, date, running title typically appear back-to-back).
            while i < n:
                nxt = lines[i].strip()
                if nxt and _is_noise_line(nxt, pub_id_patterns, running_title_counts):
                    noise_removed += 1
                    i += 1
                    while i < n and lines[i].strip() == "":
                        i += 1
                    continue
                break

            # Decide whether to rejoin: look at the last non-blank emitted
            # line. If it doesn't end in terminal punctuation, this was a
            # mid-sentence/mid-list-item split -- splice the next non-blank
            # content directly onto it instead of leaving a paragraph break.
            last_idx = len(out_lines) - 1
            while last_idx >= 0 and out_lines[last_idx].strip() == "":
                last_idx -= 1
            if last_idx >= 0 and not _TERMINAL_PUNCT_RE.search(out_lines[last_idx].rstrip()):
                # Find the next non-blank content line to splice in. Never
                # rejoin into a heading -- a '#' line always starts a new
                # structural unit regardless of what preceded it (e.g. a
                # figure caption ending without punctuation, immediately
                # followed by noise then the next chapter's heading, is a
                # real section boundary, not a mid-sentence split).
                j = i
                while j < n and lines[j].strip() == "":
                    j += 1
                if j < n and lines[j].lstrip().startswith("#"):
                    continue
                if j < n:
                    prev = out_lines[last_idx].rstrip()
                    cont = lines[j].strip()
                    out_lines[last_idx] = prev + " " + cont
                    rejoins += 1
                    i = j + 1
                    continue
            continue
        out_lines.append(line)
        i += 1

    text = "\n".join(out_lines)

    # Collapse the blank-line runs left behind by noise removal down to a
    # single paragraph break, and strip the noise/rejoin comment artifacts.
    text = re.sub(r"\n{3,}", "\n\n", text)

    leaks_removed = 0
    low = text.lower()
    for pat in LEAK_PATTERNS:
        if pat in low:
            # Remove the sentence/line containing the leak, case-insensitively.
            text = re.sub(
                r"[^\n]*" + re.escape(pat) + r"[^\n]*\n?", "", text,
                flags=re.IGNORECASE,
            )
            leaks_removed += 1

    text, toc_removed = _strip_toc_tables(text)

    # Drop unrecoverable replacement-character runs, then tidy the empty
    # markup shells they leave behind (e.g. "## **** " -> removed entirely).
    text = _REPL_RUN_RE.sub("", text)
    text = re.sub(r"^#+\s*(?:\*\*\s*\*\*)?\s*$", "", text, flags=re.M)
    text = re.sub(r"\*\*\s*\*\*", "", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    cid_count = len(_CID_ARTIFACT_RE.findall(text))

    return CleanResult(
        text=text.strip() + "\n",
        noise_lines_removed=noise_removed,
        rejoins_performed=rejoins,
        leaks_removed=leaks_removed,
        cid_artifacts_found=cid_count,
        toc_tables_removed=toc_removed,
    )


def normalize_doc_id(raw_name: str) -> str:
    """Normalize any doc_id/filename separator style to 'ADP_X-Y' /
    'ATP_X-Y' underscore form, per finding #3 -- app.py's
    _extract_source_pub() regex requires this exact form to display
    citations correctly.

    Handles all confirmed real-corpus variants: 'ADP 3-05', 'ADP_3-13',
    'ADP-6-0', 'ADP_1', 'adp5_0' etc.
    """
    stem = re.sub(r"\.(pdf|md|txt)$", "", raw_name.strip(), flags=re.I)
    m = re.match(r"^\s*(ADP|ATP)[\s_-]*(.+?)\s*$", stem, re.I)
    if not m:
        raise ValueError(f"doc_id does not match ADP/ATP pattern: {raw_name!r}")
    kind = m.group(1).upper()
    rest = m.group(2).strip()
    # Normalize internal separators in the number part to '-' (e.g. a
    # filename using underscores throughout, "ADP_3_13" -> "3-13").
    rest = re.sub(r"[\s_]+", "-", rest)
    rest = re.sub(r"-{2,}", "-", rest).strip("-")
    return f"{kind}_{rest}"
