"""
Chunking stage: split cleaned markdown into chunks sized for the chosen
embedding model's real max_seq_length, using pymupdf4llm's real headings
(confirmed present in eval/extraction_eval.md) as the primary structural
signal via a narrow LangChain MarkdownHeaderTextSplitter pass, followed by
custom paragraph/list-atomicity packing.

Rules (see task requirements + confirmed findings):
  - A heading's lead-in paragraph is never separated from an immediately
    following list/enumeration -- they are always packed as one atomic unit.
  - Atomic units are packed greedily into a chunk up to the token budget.
  - An atomic unit that alone exceeds the token budget is emitted as its own
    (oversized) chunk and logged -- overflow is a logged last resort, never
    a silent truncation.
  - chunk_id is sequential per document: f"{doc_id}__{NNNNNN}".
"""
import logging
import re
from dataclasses import dataclass, field

from langchain_text_splitters import MarkdownHeaderTextSplitter

from pipeline.tokenizer_utils import count_tokens, EMBED_MODEL_MAX_SEQ_LENGTH

logger = logging.getLogger(__name__)

HEADERS_TO_SPLIT_ON = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
    ("####", "h4"),
    ("#####", "h5"),
    ("######", "h6"),
]

# A markdown list block: consecutive lines starting with '-', '*', '•', or
# "N." / "N)" numbering (allowing indentation for nested items).
_LIST_LINE_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+\S")


@dataclass
class Chunk:
    chunk_id: str
    text: str
    doc_id: str
    source_file: str
    token_count: int


@dataclass
class ChunkResult:
    chunks: list[Chunk] = field(default_factory=list)
    overflow_units: int = 0
    source_chars: int = 0
    chunk_chars: int = 0

    @property
    def preservation_ratio(self) -> float:
        if self.source_chars == 0:
            return 1.0
        return self.chunk_chars / self.source_chars


def _split_paragraphs(text: str) -> list[str]:
    return [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]


def _group_atomic_units(paragraphs: list[str]) -> list[str]:
    """Merge a paragraph with any immediately-following list block(s) into
    one atomic unit, so a heading's lead-in is never separated from its
    enumeration. A run of consecutive list-block paragraphs also merges
    together (a list split across paragraph boundaries by clean.py's
    noise-rejoin stays one unit)."""
    units: list[str] = []
    i = 0
    n = len(paragraphs)
    while i < n:
        current = paragraphs[i]
        j = i + 1
        # Absorb any immediately-following paragraphs that are themselves
        # list blocks (a lead-in paragraph followed by one or more list
        # paragraphs, or a list continuing after a page-break rejoin).
        while j < n and _LIST_LINE_RE.match(paragraphs[j].lstrip().splitlines()[0]):
            current = current + "\n\n" + paragraphs[j]
            j += 1
        units.append(current)
        i = j
    return units


_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'‘’“”(])")


def _contains_list(unit: str) -> bool:
    return any(_LIST_LINE_RE.match(line.lstrip()) for line in unit.splitlines())


def _split_oversized_unit(unit: str, max_tokens: int) -> list[str]:
    """Split a plain-prose unit (no list block) at sentence boundaries into
    pieces that fit the token budget. A unit containing a list is never
    passed here -- see _pack_units -- since splitting a list mid-item would
    violate the list-atomicity requirement; those are kept whole as a
    logged overflow instead. If even a single sentence alone exceeds the
    budget (rare -- a genuine run-on sentence), it is kept whole too."""
    sentences = _SENTENCE_SPLIT_RE.split(unit.strip())
    pieces: list[str] = []
    buf: list[str] = []
    buf_tokens = 0
    for sent in sentences:
        sent_tokens = count_tokens(sent)
        if buf_tokens + sent_tokens > max_tokens and buf:
            pieces.append(" ".join(buf))
            buf, buf_tokens = [], 0
        buf.append(sent)
        buf_tokens += sent_tokens
    if buf:
        pieces.append(" ".join(buf))
    return pieces


def _pack_units(units: list[str], max_tokens: int) -> list[tuple[str, int]]:
    """Greedily pack atomic units into chunks under the token budget.
    Returns list of (chunk_text, token_count). A unit containing a list is
    treated as truly atomic (never split, even if oversized -- logged by the
    caller as a last-resort overflow, per the list-integrity requirement). A
    plain prose unit that alone exceeds max_tokens is instead split at
    sentence boundaries first, since there's no structural reason a long
    paragraph must stay whole -- only lists/enumerations are protected."""
    packed: list[tuple[str, int]] = []
    buf: list[str] = []
    buf_tokens = 0

    def flush():
        nonlocal buf, buf_tokens
        if buf:
            text = "\n\n".join(buf)
            packed.append((text, count_tokens(text)))
            buf = []
            buf_tokens = 0

    for unit in units:
        unit_tokens = count_tokens(unit)
        if unit_tokens > max_tokens:
            flush()
            if _contains_list(unit):
                packed.append((unit, unit_tokens))  # oversized, logged by caller
                continue
            for piece in _split_oversized_unit(unit, max_tokens):
                piece_tokens = count_tokens(piece)
                packed.append((piece, piece_tokens))  # logged by caller if still over
            continue
        if buf_tokens + unit_tokens > max_tokens and buf:
            flush()
        buf.append(unit)
        buf_tokens += unit_tokens

    flush()
    return packed


def chunk_document(
    cleaned_text: str,
    doc_id: str,
    source_file: str,
    max_tokens: int = EMBED_MODEL_MAX_SEQ_LENGTH,
) -> ChunkResult:
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON, strip_headers=False
    )
    sections = splitter.split_text(cleaned_text)

    result = ChunkResult(source_chars=len(cleaned_text))
    seq = 0
    for section in sections:
        section_text = section.page_content.strip()
        if not section_text:
            continue
        # Prepend the innermost heading as a one-line context breadcrumb if
        # the splitter stripped it into metadata rather than leaving it in
        # page_content (behavior differs by langchain version); avoid
        # duplicating it if it's already the first line.
        heading = None
        for level in ("h6", "h5", "h4", "h3", "h2", "h1"):
            if level in section.metadata:
                heading = section.metadata[level]
        if heading and not section_text.lstrip().startswith(heading):
            section_text = f"{heading}\n\n{section_text}"

        paragraphs = _split_paragraphs(section_text)
        units = _group_atomic_units(paragraphs)
        packed = _pack_units(units, max_tokens)

        for text, tokens in packed:
            if tokens > max_tokens:
                logger.warning(
                    "chunk_document: atomic unit exceeds max_tokens (%d > %d) "
                    "in %s, section %r -- kept whole, not truncated",
                    tokens, max_tokens, doc_id, heading,
                )
                result.overflow_units += 1
            seq += 1
            chunk_id = f"{doc_id}__{seq:06d}"
            result.chunks.append(Chunk(
                chunk_id=chunk_id,
                text=text,
                doc_id=doc_id,
                source_file=source_file,
                token_count=tokens,
            ))
            result.chunk_chars += len(text)

    return result
