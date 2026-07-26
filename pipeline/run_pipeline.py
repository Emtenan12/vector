#!/usr/bin/env python3
"""
Orchestrates extract -> clean -> chunk across a directory of PDFs, writing
per-stage intermediate output (for dry-run inspection) plus the final
{doc_id}_Cleaned.jsonl chunk file consumed by pipeline/embed_index.py and,
downstream, hybrid_retrieval.py.

Usage:
    python -m pipeline.run_pipeline --pdf-dir data/raw_pdfs --out-dir data --limit 1
"""
import argparse
import json
import logging
from pathlib import Path

from pipeline.chunk import chunk_document
from pipeline.clean import clean_text, normalize_doc_id
from pipeline.extract import extract_pdf

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)


def process_pdf(pdf_path: Path, out_dir: Path) -> dict:
    doc_id = normalize_doc_id(pdf_path.name)

    stage1_dir = out_dir / "stage1_extracted"
    stage2_dir = out_dir / "stage2_cleaned"
    stage1_dir.mkdir(parents=True, exist_ok=True)
    stage2_dir.mkdir(parents=True, exist_ok=True)

    raw_md = extract_pdf(pdf_path)
    (stage1_dir / f"{doc_id}.md").write_text(raw_md, encoding="utf-8")

    clean_result = clean_text(raw_md, doc_id)
    (stage2_dir / f"{doc_id}.md").write_text(clean_result.text, encoding="utf-8")

    chunk_result = chunk_document(clean_result.text, doc_id, pdf_path.name)

    return {
        "doc_id": doc_id,
        "source_file": pdf_path.name,
        "raw_chars": len(raw_md),
        "cleaned_chars": len(clean_result.text),
        "noise_lines_removed": clean_result.noise_lines_removed,
        "rejoins_performed": clean_result.rejoins_performed,
        "leaks_removed": clean_result.leaks_removed,
        "cid_artifacts_found": clean_result.cid_artifacts_found,
        "toc_tables_removed": clean_result.toc_tables_removed,
        "chunks": chunk_result.chunks,
        "overflow_units": chunk_result.overflow_units,
        "chunk_preservation_ratio": chunk_result.preservation_ratio,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf-dir", default="data/raw_pdfs")
    parser.add_argument("--out-dir", default="data")
    parser.add_argument("--limit", type=int, default=None,
                         help="Process only the first N PDFs (for gated scale-up).")
    parser.add_argument("--jsonl-name", default="ADP_Cleaned.jsonl",
                         help="Output filename under <out-dir>/stage3_chunks/")
    args = parser.parse_args()

    pdf_dir = Path(args.pdf_dir)
    out_dir = Path(args.out_dir)
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if args.limit:
        pdfs = pdfs[: args.limit]

    if not pdfs:
        logger.error("No PDFs found in %s", pdf_dir)
        return

    stage3_dir = out_dir / "stage3_chunks"
    stage3_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = stage3_dir / args.jsonl_name

    all_reports = []
    with jsonl_path.open("w", encoding="utf-8") as out_f:
        for pdf_path in pdfs:
            logger.info("Processing %s", pdf_path.name)
            report = process_pdf(pdf_path, out_dir)
            for chunk in report["chunks"]:
                out_f.write(json.dumps({
                    "chunk_id": chunk.chunk_id,
                    "text": chunk.text,
                    "doc_id": chunk.doc_id,
                    "source_file": chunk.source_file,
                    "token_count": chunk.token_count,
                }, ensure_ascii=False) + "\n")
            logger.info(
                "  %s: %d chunks, preservation=%.1f%%, overflow=%d, "
                "noise_removed=%d, rejoins=%d, toc_removed=%d, cid=%d, leaks=%d",
                report["doc_id"], len(report["chunks"]),
                report["chunk_preservation_ratio"] * 100, report["overflow_units"],
                report["noise_lines_removed"], report["rejoins_performed"],
                report["toc_tables_removed"], report["cid_artifacts_found"],
                report["leaks_removed"],
            )
            report.pop("chunks")  # keep the summary report light
            all_reports.append(report)

    summary_path = stage3_dir / (args.jsonl_name.replace(".jsonl", "") + "_report.json")
    summary_path.write_text(json.dumps(all_reports, indent=2), encoding="utf-8")
    logger.info("Wrote %d chunks total to %s", sum(1 for _ in jsonl_path.open()), jsonl_path)
    logger.info("Per-document report: %s", summary_path)


if __name__ == "__main__":
    main()
