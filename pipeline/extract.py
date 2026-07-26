"""
PDF -> structured markdown extraction, using pymupdf4llm -- the tool
justified by eval/extraction_eval.md's evidence (real headings on 3/3 real
ADP PDFs, zero (cid:) artifacts, intact list structure), not by which tool
was discussed in prior conversation.

Documents whose fonts carry a broken/absent ToUnicode map take a repair path
instead (see pipeline/repair_extract.py) -- pymupdf4llm renders those as ~97%
U+FFFD replacement characters, which would otherwise be embedded as garbage.
"""
import logging
from pathlib import Path

import pymupdf4llm

from pipeline.repair_extract import maybe_repair

logger = logging.getLogger(__name__)


def extract_pdf(pdf_path: Path) -> str:
    """Return markdown for a PDF. No page-break cleanup or doc_id
    normalization here -- that's pipeline/clean.py's job, kept separate so
    this stage stays a thin, swappable wrapper around the extraction tool."""
    repaired, _shift = maybe_repair(Path(pdf_path))
    if repaired is not None:
        return repaired
    return pymupdf4llm.to_markdown(str(pdf_path))
