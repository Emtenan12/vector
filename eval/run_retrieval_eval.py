#!/usr/bin/env python3
"""
Grounded retrieval evaluation against the built indexes.

Scores ONE axis only -- the "Retrieval hit" axis of the suite's scoring
guide: does the gold paragraph anchor appear in the top-k retrieved chunks?
Faithfulness and Correctness are generation-side axes and need the
generative model, which is not part of this pipeline.

Three retrievers are scored independently, per the request:
  dense  -- ChromaDB cosine over bge-small-en-v1.5 embeddings
  sparse -- BM25Okapi, same tokenizer the index was built with
  fused  -- Reciprocal Rank Fusion over the two

IMPORTANT: the fused scorer here is a STAND-IN. The production fusion lives
in hybrid_retrieval.py on the HF Space, which is not in this repo, so its
weighting/algorithm could not be read. RRF (k=60, unweighted) is the common
default and is used to give the fused column *a* defensible meaning -- treat
fused numbers as "what a standard RRF would do with these two indexes", not
as a measurement of the deployed system.

Gold-chunk resolution: the suite's anchors are paragraph references ("ADP
3-0 (2025), para 2-25"), and the scoring guide notes this "requires
paragraph metadata on chunks". The chunk schema has none. However, the
doctrine's own paragraph numbers survive extraction as line-leading "2-25."
markers in 2,005 of 4,032 chunks, so an anchor is resolved to the chunk(s)
whose text carries that marker. Anchors that resolve to nothing are reported
as UNRESOLVED rather than silently scored as misses.
"""
import argparse
import json
import pickle
import re
import statistics
from pathlib import Path

from pipeline.embed_index import COLLECTION_NAME, _tokenize

BGE_QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
RRF_K = 60

VARIANT_COLS = {
    "primary": 2,
    "paraphrase": 3,
    "casual": 4,
    "typo": 5,
    "trap": 6,
}


def load_suite(xlsx_path: Path) -> list[dict]:
    import openpyxl

    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    ws = wb["Test Suite"]
    rows = list(ws.iter_rows(values_only=True))[1:]
    out = []
    for r in rows:
        if not r[0]:
            continue
        out.append({
            "id": str(r[0]).strip(),
            "category": (r[1] or "").strip(),
            "variants": {k: (r[i] or "").strip() for k, i in VARIANT_COLS.items()},
            "expected": (r[7] or "").strip(),
            "anchor": (r[8] or "").strip(),
        })
    return out


def extract_trap_query(cell: str) -> str:
    """The trap column is prose: "TRAP: 'What are the seven ...?' -> must
    answer six". Pull the quoted question out; that is the query actually
    posed to the retriever.

    Anchored to the trailing arrow rather than to the next quote character,
    because trap questions contain apostrophes ("The principles of war
    aren't in Army doctrine, right?") and a nearest-quote match truncates
    them mid-word -- Q5 was silently being run as "t in Army doctrine,
    right?" before this.
    """
    m = re.search(r"TRAP:\s*['‘\"“](.+?)['’\"”]\s*(?:→|->|-->)", cell, re.S)
    if m:
        return m.group(1).strip()
    m = re.search(r"TRAP:\s*['‘\"“](.+?\?)", cell, re.S)
    return m.group(1).strip() if m else ""


_DOC_RE = re.compile(r"\bAD[PR]\s+(\d+-\d+)\b")

# Paragraph markers are usually line-leading, but not always: an epigraph
# attribution can run into the next paragraph on one line ("...William Joseph
# Slim 1-45. The commander's intent is..."), which is exactly how ADP 6-0
# para 1-45 -- Q8's anchor -- presents. Matching line-start only silently
# loses those. The lookahead for a capital/emphasis opener plus the
# doc/figure scrubbing below keeps this from swallowing citations and
# figure captions.
_PARA_MARKER_RE = re.compile(r"(?<![A-Za-z0-9-])(\d{1,2}-\d{1,3})\.\s+(?=[A-Z_*\"“(])")
_CITATION_RE = re.compile(r"(?:ADP|ATP|ADRP|FM|JP|AR|TC)\s+\d{1,2}-\d{1,3}\.?", re.I)
_CAPTION_RE = re.compile(r"(?:Figure|Fig\.?|Table)\s+\d{1,2}-\d{1,3}\.?", re.I)


def _para_ids_in(text: str) -> set[str]:
    # Substitute a CAPITALIZED placeholder, not a space: a real paragraph can
    # open with a figure callout ("2-6. Figure 2-1 shows the taxonomy..."),
    # and blanking the caption leaves "2-6.  shows", whose lowercase opener
    # fails the marker lookahead and silently drops the paragraph. Cost a
    # real anchor (Q20) before this was caught.
    scrub = _CAPTION_RE.sub(" Ref ", _CITATION_RE.sub(" Ref ", text))
    return set(_PARA_MARKER_RE.findall(scrub))


def parse_anchor(anchor: str) -> list[tuple[str, list[str]]]:
    """Return [(doc_id, [paragraph_id, ...]), ...] for an anchor cell.

    Segmented by document rather than crossed, because an anchor can name
    two publications with different paragraph numbers ("ADP 6-0 (2019), para
    1-14 ... restated in ADP 3-0 (2025), para 2-7"). A cross product would
    make ADP 3-0's para 1-14 -- a completely unrelated 'Levels of Warfare'
    passage that happens to share Q4's number -- count as gold for Q6.
    """
    marks = [(m.start(), "ADP_" + m.group(1)) for m in _DOC_RE.finditer(anchor)]
    if not marks:
        return []
    segments = []
    for i, (pos, doc) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(anchor)
        segments.append((doc, anchor[pos:end]))

    out = []
    for doc, seg in segments:
        scrub = _DOC_RE.sub(" ", seg)
        scrub = re.sub(r"\b(?:Figure|Fig\.?|p\.|pp\.|Table)\s*\d+-\d+", " ", scrub, flags=re.I)
        paras: list[str] = []
        for a, b in re.findall(r"(\d+-\d+)\s*(?:to|through|–|—)\s*(\d+-\d+)", scrub):
            ca, na = a.split("-")
            cb, nb = b.split("-")
            if ca == cb and int(na) <= int(nb):
                paras += [f"{ca}-{n}" for n in range(int(na), int(nb) + 1)]
            else:
                paras += [a, b]
        scrub = re.sub(r"(\d+-\d+)\s*(?:to|through|–|—)\s*(\d+-\d+)", " ", scrub)
        paras += re.findall(r"\b(\d+-\d+)\b", scrub)
        seen, ordered = set(), []
        for p in paras:
            if p not in seen:
                seen.add(p)
                ordered.append(p)
        out.append((doc, ordered))
    return out


def build_para_map(chunks: list[dict]) -> dict[tuple[str, str], list[str]]:
    """(doc_id, para_id) -> [chunk_id, ...]."""
    out: dict[tuple[str, str], list[str]] = {}
    for c in chunks:
        for pid in _para_ids_in(c["text"]):
            out.setdefault((c["doc_id"], pid), []).append(c["chunk_id"])
    return out


# Anchors that name no paragraph at all (Q14 points at an Introduction and a
# logic chart on page 1-1). Resolved by required-substring instead, taken
# from the suite's own Expected Answer wording so the gold set is still
# grounded in the corpus rather than hand-picked by chunk id.
CONTENT_ANCHORS = {
    "14": ("ADP_4-0", ["logistics", "financial management",
                       "personnel services", "health service support"]),
}


def resolve_gold(qid: str, case_anchor: str, para_map, chunks) -> tuple[set[str], list[str]]:
    gold: set[str] = set()
    missing = []
    for doc, paras in parse_anchor(case_anchor):
        for p in paras:
            hit = para_map.get((doc, p))
            if hit:
                gold.update(hit)
            else:
                missing.append(f"{doc}:{p}")

    if not gold and qid in CONTENT_ANCHORS:
        doc, needles = CONTENT_ANCHORS[qid]
        for c in chunks:
            if c["doc_id"] == doc:
                low = c["text"].lower()
                if all(n in low for n in needles):
                    gold.add(c["chunk_id"])
    return gold, missing


class Retrievers:
    def __init__(self, index_dir: Path, model_dir: Path):
        import chromadb
        from sentence_transformers import SentenceTransformer

        self.model = SentenceTransformer(str(model_dir), device="cpu")
        self.col = chromadb.PersistentClient(path=str(index_dir / "chroma_db")).get_collection(
            COLLECTION_NAME
        )
        d = pickle.load((index_dir / "bm25_index.pkl").open("rb"))
        self.bm25, self.bm25_ids = d["bm25"], d["chunk_ids"]

    def dense(self, q: str, k: int) -> list[str]:
        emb = self.model.encode([BGE_QUERY_PREFIX + q]).tolist()
        return self.col.query(query_embeddings=emb, n_results=k)["ids"][0]

    def sparse(self, q: str, k: int) -> list[str]:
        scores = self.bm25.get_scores(_tokenize(q))
        top = sorted(range(len(scores)), key=lambda i: -scores[i])[:k]
        return [self.bm25_ids[i] for i in top]

    def fused(self, q: str, k: int, pool: int = 50) -> list[str]:
        dr = self.dense(q, pool)
        sr = self.sparse(q, pool)
        agg: dict[str, float] = {}
        for ranking in (dr, sr):
            for rank, cid in enumerate(ranking, start=1):
                agg[cid] = agg.get(cid, 0.0) + 1.0 / (RRF_K + rank)
        return [c for c, _ in sorted(agg.items(), key=lambda kv: -kv[1])[:k]]


def rank_of(gold: set[str], ranking: list[str]) -> int | None:
    for i, cid in enumerate(ranking, start=1):
        if cid in gold:
            return i
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("xlsx", type=Path)
    ap.add_argument("--jsonl", type=Path, default=Path("data/stage3_chunks/ADP_Cleaned.jsonl"))
    ap.add_argument("--index-dir", type=Path, default=Path("data/indexes"))
    ap.add_argument("--model-dir", type=Path, default=Path("models/bge-small-en-v1.5"))
    ap.add_argument("--k", type=int, default=10)
    ap.add_argument("--out-json", type=Path, default=None)
    ap.add_argument("--out-md", type=Path, default=None)
    ap.add_argument("--correct", choices=["none", "symspell", "rapidfuzz"], default="none",
                    help="Query-side spell correction applied before ALL retrievers.")
    args = ap.parse_args()

    chunks = [json.loads(l) for l in args.jsonl.open(encoding="utf-8") if l.strip()]
    para_map = build_para_map(chunks)
    suite = load_suite(args.xlsx)
    R = Retrievers(args.index_dir, args.model_dir)

    corrector = None
    if args.correct != "none":
        from pipeline.query_correct import DomainSpellCorrector, build_vocab

        corrector = DomainSpellCorrector(build_vocab(chunks), backend=args.correct)

    results = []
    unresolved = []
    for q in suite:
        gold, missing = resolve_gold(q["id"], q["anchor"], para_map, chunks)
        if not gold:
            unresolved.append({"id": q["id"], "anchor": q["anchor"], "missing": missing})
        for vname, vtext in q["variants"].items():
            if not vtext:
                continue
            query = extract_trap_query(vtext) if vname == "trap" else vtext
            if not query:
                continue
            raw_query = query
            edits: list[tuple[str, str]] = []
            if corrector is not None:
                query, edits = corrector.correct(query)

            row = {
                "id": q["id"], "variant": vname, "query": raw_query,
                "corrected_query": query if edits else None,
                "edits": edits,
                "category": q["category"], "anchor": q["anchor"],
                "gold_n": len(gold), "resolved": bool(gold),
            }
            if gold:
                for name, fn in (("dense", R.dense), ("sparse", R.sparse), ("fused", R.fused)):
                    rk = rank_of(gold, fn(query, args.k))
                    row[f"{name}_rank"] = rk
                    row[f"{name}_hit"] = rk is not None
            results.append(row)

    scored = [r for r in results if r["resolved"]]
    summary = {}
    for name in ("dense", "sparse", "fused"):
        hits = [r for r in scored if r[f"{name}_hit"]]
        ranks = [r[f"{name}_rank"] for r in hits]
        summary[name] = {
            "hit_rate": len(hits) / len(scored) if scored else 0.0,
            "hits": len(hits), "n": len(scored),
            "mrr": (sum(1 / r for r in ranks) / len(scored)) if scored else 0.0,
            "median_rank_when_hit": statistics.median(ranks) if ranks else None,
        }

    payload = {"k": args.k, "cases": len(results), "scored": len(scored),
               "unresolved_questions": unresolved, "summary": summary, "results": results}
    if args.out_json:
        args.out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md = render_md(payload)
    print(md)
    if args.out_md:
        args.out_md.write_text(md, encoding="utf-8")


def render_md(p: dict) -> str:
    L = [f"# Retrieval evaluation (top-k = {p['k']})", ""]
    L.append(f"Cases: {p['cases']}  |  Scored: {p['scored']}  "
             f"|  Unresolved questions: {len(p['unresolved_questions'])}")
    L.append("")
    L.append("Axis scored: **Retrieval hit** only (gold paragraph anchor present in top-k). "
             "Faithfulness/Correctness are generation-side and out of scope here.")
    L.append("")
    L.append("| retriever | hit rate | hits/n | MRR | median rank when hit |")
    L.append("|---|---|---|---|---|")
    for name in ("dense", "sparse", "fused"):
        s = p["summary"][name]
        L.append(f"| {name} | {s['hit_rate']*100:.1f}% | {s['hits']}/{s['n']} | "
                 f"{s['mrr']:.3f} | {s['median_rank_when_hit']} |")
    L.append("")

    L.append("## Hit rate by variant")
    L.append("")
    L.append("| variant | dense | sparse | fused | n |")
    L.append("|---|---|---|---|---|")
    for v in ("primary", "paraphrase", "casual", "typo", "trap"):
        rs = [r for r in p["results"] if r["variant"] == v and r["resolved"]]
        if not rs:
            continue
        cells = []
        for n in ("dense", "sparse", "fused"):
            h = sum(1 for r in rs if r[f"{n}_hit"])
            cells.append(f"{100*h/len(rs):.0f}% ({h}/{len(rs)})")
        L.append(f"| {v} | {cells[0]} | {cells[1]} | {cells[2]} | {len(rs)} |")
    L.append("")

    L.append("## Hit rate vs k")
    L.append("")
    L.append("| k | dense | sparse | fused |")
    L.append("|---|---|---|---|")
    scored = [r for r in p["results"] if r["resolved"]]
    for k in (1, 3, 5, p["k"]):
        row = []
        for n in ("dense", "sparse", "fused"):
            h = sum(1 for r in scored if r[f"{n}_rank"] and r[f"{n}_rank"] <= k)
            row.append(f"{100*h/len(scored):.1f}%")
        L.append(f"| {k} | {row[0]} | {row[1]} | {row[2]} |")
    L.append("")

    if p["unresolved_questions"]:
        L.append("## Unresolved anchors (excluded from scoring, not counted as misses)")
        for u in p["unresolved_questions"]:
            L.append(f"- **Q{u['id']}** — `{u['anchor']}` (no chunk carries: {', '.join(u['missing'][:6])})")
        L.append("")

    L.append("## Per-case results")
    L.append("")
    L.append("| Q | variant | dense | sparse | fused | query |")
    L.append("|---|---|---|---|---|---|")
    def cell(r, n):
        if not r["resolved"]:
            return "n/a"
        return f"PASS ({r[n+'_rank']})" if r[n + "_hit"] else "FAIL"
    for r in p["results"]:
        q = r["query"].replace("|", "\\|")
        q = q if len(q) <= 62 else q[:59] + "..."
        L.append(f"| {r['id']} | {r['variant']} | {cell(r,'dense')} | "
                 f"{cell(r,'sparse')} | {cell(r,'fused')} | {q} |")
    return "\n".join(L)


if __name__ == "__main__":
    main()
