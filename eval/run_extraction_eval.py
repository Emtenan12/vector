#!/usr/bin/env python3
"""
Extraction-tool bake-off: run MarkItDown, pymupdf4llm, and docling against
real ADP PDFs and collect the evidence needed to pick one.

This is throwaway evaluation tooling (deliverable 1), not part of the
production pipeline (pipeline/extract.py) -- kept separate on purpose so the
production module only contains the tool that actually won.
"""
import re
import sys
import time
import traceback
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw_pdfs"
OUT_DIR = Path(__file__).parent / "samples"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Known leaked-prompt-fragment wordings from the old pipeline (finding #4) --
# check whether any new tool's own output has an analogous instruction-leak.
LEAK_PATTERNS = [
    "replace this line with a description of the figure",
    "verify the figure: ocr of chart labels is unreliable",
]

CID_ARTIFACT_RE = re.compile(r"\(cid:\d+\)")
HEADING_RE = re.compile(r"^#{1,6}\s", re.MULTILINE)


def count_headings(text: str) -> int:
    return len(HEADING_RE.findall(text))


def count_cid_artifacts(text: str) -> int:
    return len(CID_ARTIFACT_RE.findall(text))


def find_leaks(text: str) -> list[str]:
    low = text.lower()
    return [p for p in LEAK_PATTERNS if p in low]


def run_markitdown(pdf_path: Path) -> str:
    from markitdown import MarkItDown
    md = MarkItDown()
    result = md.convert(str(pdf_path))
    return result.text_content


def run_markitdown_no_plugins(pdf_path: Path) -> str:
    # MarkItDown exposes few PDF-specific knobs; this checks whether the
    # default conversion path differs when plugins are disabled explicitly.
    from markitdown import MarkItDown
    md = MarkItDown(enable_plugins=False)
    result = md.convert(str(pdf_path))
    return result.text_content


def run_pymupdf4llm(pdf_path: Path) -> str:
    import pymupdf4llm
    return pymupdf4llm.to_markdown(str(pdf_path))


def run_docling(pdf_path: Path) -> str:
    from docling.document_converter import DocumentConverter
    converter = DocumentConverter()
    result = converter.convert(str(pdf_path))
    return result.document.export_to_markdown()


TOOLS = {
    "markitdown_default": run_markitdown,
    "markitdown_no_plugins": run_markitdown_no_plugins,
    "pymupdf4llm": run_pymupdf4llm,
    "docling": run_docling,
}


def main():
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    pdfs = sorted(RAW_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {RAW_DIR}")
        sys.exit(1)

    rows = []
    for pdf_path in pdfs:
        for tool_name, fn in TOOLS.items():
            if only and tool_name not in only:
                continue
            print(f"=== {pdf_path.name} :: {tool_name} ===", flush=True)
            t0 = time.time()
            try:
                text = fn(pdf_path)
                elapsed = time.time() - t0
                out_path = OUT_DIR / f"{pdf_path.stem}__{tool_name}.md"
                out_path.write_text(text, encoding="utf-8")
                headings = count_headings(text)
                cids = count_cid_artifacts(text)
                leaks = find_leaks(text)
                chars = len(text)
                rows.append({
                    "pdf": pdf_path.name,
                    "tool": tool_name,
                    "status": "ok",
                    "elapsed_s": round(elapsed, 1),
                    "chars": chars,
                    "headings": headings,
                    "cid_artifacts": cids,
                    "leaks": leaks,
                    "out_path": str(out_path),
                })
                print(f"    ok: {chars} chars, {headings} headings, "
                      f"{cids} cid-artifacts, {elapsed:.1f}s -> {out_path}")
            except Exception as exc:
                elapsed = time.time() - t0
                rows.append({
                    "pdf": pdf_path.name,
                    "tool": tool_name,
                    "status": "error",
                    "elapsed_s": round(elapsed, 1),
                    "error": f"{type(exc).__name__}: {exc}",
                })
                print(f"    ERROR after {elapsed:.1f}s: {exc}")
                traceback.print_exc()

    print("\n\n=== SUMMARY ===")
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
