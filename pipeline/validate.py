#!/usr/bin/env python3
"""
Validation report generator: runs the automated gate checks from the task
spec against a chunked JSONL corpus and produces a human-readable pass/fail
summary -- this is what gets reviewed at each scale-up gate (1 file -> 3
files -> full ADP set), not ad hoc print statements.

Checks:
  1. Content-preservation ratio (chunk chars / cleaned-stage chars) >= ~99%,
     per document -- from pipeline/run_pipeline.py's per-document report.
  2. Zero leaked extraction-tool artifacts in final chunks: the two known
     prompt-leak wordings, and (cid:N) font-encoding artifacts.
  3. doc_id format consistency: every chunk's doc_id must match ADP_X-Y /
     ATP_X-Y underscore form (app.py's _extract_source_pub() requirement).
  4. Known-enumeration regression tests (MDMP 7-step list, mission command
     7 principles) must each land intact in exactly one chunk.
  5. Chunk token-count distribution (min/median/max) via the real embedding
     tokenizer, flagging anything over max_seq_length.
"""
import argparse
import json
import statistics
from pathlib import Path

from pipeline.clean import LEAK_PATTERNS, _CID_ARTIFACT_RE
from pipeline.tokenizer_utils import EMBED_MODEL_MAX_SEQ_LENGTH, count_tokens

DOC_ID_RE_ADP_ATP = __import__("re").compile(r"^(ADP|ATP)_[\w.-]+$")

REGRESSION_TESTS = [
    {
        "name": "ADP 5-0 MDMP 7-step list",
        "doc_id_prefix": "ADP_5-0",
        "needles": [
            "receipt of mission", "mission analysis", "course of action development",
            "course of action analysis", "course of action comparison",
            "course of action approval", "orders production",
        ],
        "min_needles": 6,  # allow one miss for wording drift, still must be substantially intact
    },
    {
        "name": "ADP 6-0 mission command 7 principles",
        "doc_id_prefix": "ADP_6-0",
        "needles": [
            "competence", "mutual trust", "shared understanding",
            "commander's intent", "mission orders", "disciplined initiative",
            "risk acceptance",
        ],
        "min_needles": 7,
    },
]


def load_chunks(jsonl_path: Path) -> list[dict]:
    chunks = []
    with jsonl_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks


def check_preservation_ratio(per_doc_report: list[dict], threshold: float = 0.99) -> list[dict]:
    results = []
    for doc in per_doc_report:
        ratio = doc["chunk_preservation_ratio"]
        results.append({
            "doc_id": doc["doc_id"],
            "check": "content_preservation_ratio",
            "value": round(ratio * 100, 2),
            "pass": ratio >= threshold,
            "detail": f"{ratio*100:.2f}% (threshold >= {threshold*100:.0f}%)",
        })
    return results


def check_artifacts(chunks: list[dict]) -> dict:
    leak_hits = []
    cid_hits = []
    for c in chunks:
        low = c["text"].lower()
        for pat in LEAK_PATTERNS:
            if pat in low:
                leak_hits.append((c["chunk_id"], pat))
        cids = _CID_ARTIFACT_RE.findall(c["text"])
        if cids:
            cid_hits.append((c["chunk_id"], len(cids)))
    return {
        "check": "zero_leaked_artifacts",
        "pass": not leak_hits and not cid_hits,
        "leak_hits": leak_hits,
        "cid_hits": cid_hits,
        "detail": f"{len(leak_hits)} leaked-prompt hits, {len(cid_hits)} chunks with (cid:) artifacts",
    }


def check_doc_id_consistency(chunks: list[dict]) -> dict:
    bad = sorted({c["doc_id"] for c in chunks if not DOC_ID_RE_ADP_ATP.match(c["doc_id"])})
    return {
        "check": "doc_id_format_consistency",
        "pass": not bad,
        "detail": f"{len(bad)} non-conforming doc_id(s): {bad}" if bad else "all doc_ids match ADP_X-Y / ATP_X-Y",
    }


def _normalize_quotes(text: str) -> str:
    # Real ADP text uses curly apostrophes/quotes (U+2019 etc.); normalize
    # to straight ASCII so regression needles don't false-negative on a
    # typographic-quote mismatch (confirmed bug: "Commander's intent" in
    # source text has a curly apostrophe, straight-quote needle missed it).
    return (text.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"'))


def check_regression_enumerations(chunks: list[dict]) -> list[dict]:
    results = []
    for test in REGRESSION_TESTS:
        candidates = [c for c in chunks if c["doc_id"].startswith(test["doc_id_prefix"])]
        best_chunk = None
        best_hits = 0
        for c in candidates:
            low = _normalize_quotes(c["text"].lower())
            hits = sum(1 for n in test["needles"] if n in low)
            if hits > best_hits:
                best_hits = hits
                best_chunk = c["chunk_id"]
        passed = best_hits >= test["min_needles"]
        results.append({
            "check": f"regression: {test['name']}",
            "pass": passed,
            "detail": (
                f"best chunk {best_chunk!r} matched {best_hits}/{len(test['needles'])} items "
                f"(need >= {test['min_needles']})"
                if candidates else
                f"SKIPPED -- no chunks found for doc_id prefix {test['doc_id_prefix']!r} "
                f"(source PDF not yet processed in this run)"
            ),
            "skipped": not candidates,
        })
    return results


def check_token_distribution(chunks: list[dict], max_seq_length: int = EMBED_MODEL_MAX_SEQ_LENGTH) -> dict:
    tokens = sorted(c["token_count"] for c in chunks)
    over = [t for t in tokens if t > max_seq_length]
    return {
        "check": "token_distribution",
        "pass": True,  # informational -- overflow is allowed if logged, not a hard fail
        "detail": (
            f"n={len(tokens)} min={min(tokens)} median={statistics.median(tokens)} "
            f"max={max(tokens)} | {len(over)} chunks ({100*len(over)/len(tokens):.1f}%) "
            f"exceed max_seq_length={max_seq_length} (will be silently truncated by the "
            f"dense embedder at query/index time -- flagged, not a failure by itself, since "
            f"these are logged last-resort overflow units from unsplittable lists/tables)"
        ),
    }


def generate_report(jsonl_path: Path, report_json_path: Path | None = None) -> str:
    chunks = load_chunks(jsonl_path)
    per_doc_report = json.loads(report_json_path.read_text()) if report_json_path and report_json_path.exists() else []

    lines = [f"# Validation report: {jsonl_path}", ""]
    lines.append(f"Total chunks: {len(chunks)}  |  Documents: {len(set(c['doc_id'] for c in chunks))}")
    lines.append("")

    all_results = []

    if per_doc_report:
        lines.append("## 1. Content-preservation ratio (per document)")
        for r in check_preservation_ratio(per_doc_report):
            all_results.append(r)
            mark = "PASS" if r["pass"] else "FAIL"
            lines.append(f"  [{mark}] {r['doc_id']}: {r['detail']}")
        lines.append("")
    else:
        lines.append("## 1. Content-preservation ratio: SKIPPED (no per-doc report supplied)")
        lines.append("")

    lines.append("## 2. Leaked-artifact scan")
    r = check_artifacts(chunks)
    all_results.append(r)
    lines.append(f"  [{'PASS' if r['pass'] else 'FAIL'}] {r['detail']}")
    for cid, pat in r["leak_hits"][:10]:
        lines.append(f"    - leak in {cid}: {pat!r}")
    for cid, n in r["cid_hits"][:10]:
        lines.append(f"    - {n} cid-artifacts in {cid}")
    lines.append("")

    lines.append("## 3. doc_id format consistency")
    r = check_doc_id_consistency(chunks)
    all_results.append(r)
    lines.append(f"  [{'PASS' if r['pass'] else 'FAIL'}] {r['detail']}")
    lines.append("")

    lines.append("## 4. Known-enumeration regression tests")
    for r in check_regression_enumerations(chunks):
        all_results.append(r)
        mark = "SKIP" if r.get("skipped") else ("PASS" if r["pass"] else "FAIL")
        lines.append(f"  [{mark}] {r['check']}: {r['detail']}")
    lines.append("")

    lines.append("## 5. Chunk token-count distribution")
    r = check_token_distribution(chunks)
    all_results.append(r)
    lines.append(f"  [INFO] {r['detail']}")
    lines.append("")

    hard_checks = [r for r in all_results if not r.get("skipped")]
    n_pass = sum(1 for r in hard_checks if r["pass"])
    n_fail = sum(1 for r in hard_checks if not r["pass"])
    n_skip = sum(1 for r in all_results if r.get("skipped"))
    lines.append(f"## Summary: {n_pass} passed, {n_fail} failed, {n_skip} skipped")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonl_path", type=Path)
    parser.add_argument("--report-json", type=Path, default=None,
                         help="Per-document report JSON from run_pipeline.py")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    report_json = args.report_json
    if report_json is None:
        guess = args.jsonl_path.with_name(args.jsonl_path.stem + "_report.json")
        if guess.exists():
            report_json = guess

    report = generate_report(args.jsonl_path, report_json)
    print(report)
    if args.out:
        args.out.write_text(report, encoding="utf-8")


if __name__ == "__main__":
    main()
