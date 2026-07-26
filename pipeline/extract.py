"""
PDF -> structured markdown extraction, using pymupdf4llm -- the tool
justified by eval/extraction_eval.md's evidence (real headings on 3/3 real
ADP PDFs, zero (cid:) artifacts, intact list structure), not by which tool
was discussed in prior conversation.
"""
from pathlib import Path

import pymupdf4llm


def extract_pdf(pdf_path: Path) -> str:
    """Return pymupdf4llm's markdown extraction of a PDF. No page-break
    cleanup or doc_id normalization here -- that's pipeline/clean.py's job,
    kept separate so this stage stays a thin, swappable wrapper around the
    extraction tool itself."""
    return pymupdf4llm.to_markdown(str(pdf_path))
