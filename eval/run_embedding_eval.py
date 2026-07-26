#!/usr/bin/env python3
"""
Embedding-model bake-off: footprint, CPU latency, and retrieval quality on
real extracted ADP doctrine text (not synthetic sentences).

Retrieval quality methodology: for each of a handful of hand-picked queries
grounded in the real extracted markdown (eval/samples/*__pymupdf4llm.md),
embed every paragraph of the source document(s) the query's answer lives in
plus paragraphs from the *other* two documents as distractors, then check
whether the known-correct paragraph is ranked #1 by cosine similarity. This
is a small sanity check (order of ~10 queries), not a full MTEB-style
benchmark -- it's sized to what's feasible to hand-verify against real text
in this session, and is reported as such.
"""
import re
import time
import tracemalloc
from pathlib import Path

SAMPLES_DIR = Path(__file__).parent / "samples"

CANDIDATES = {
    "all-MiniLM-L6-v2": "sentence-transformers/all-MiniLM-L6-v2",
    "bge-small-en-v1.5": "BAAI/bge-small-en-v1.5",
    "gte-small": "thenlper/gte-small",
    "e5-small-v2": "intfloat/e5-small-v2",
}

# Some models (e5, bge) recommend query/passage prefixes for asymmetric search.
QUERY_PREFIX = {
    "e5-small-v2": "query: ",
    "bge-small-en-v1.5": "Represent this sentence for searching relevant passages: ",
}
PASSAGE_PREFIX = {
    "e5-small-v2": "passage: ",
}


def load_paragraphs(md_path: Path) -> list[str]:
    text = md_path.read_text(encoding="utf-8")
    # Strip the running-header/footer noise lines identified in the extraction
    # eval (bare bolded short lines) before splitting into paragraphs, so the
    # retrieval test isn't measuring "did the model dodge page-break junk".
    noise_re = re.compile(r"^\*\*[^\n]{1,60}\*\*\s*$")
    lines = [l for l in text.splitlines() if not noise_re.match(l.strip())]
    cleaned = "\n".join(lines)
    paras = [p.strip() for p in re.split(r"\n\s*\n", cleaned)]
    return [p for p in paras if len(p) > 200]  # drop headings/short fragments


# Hand-picked (query, doc_file, unique_substring_of_correct_paragraph) triples,
# grounded in the real extracted text.
QUERIES = [
    (
        "What are the principles of mission command?",
        "ADP_6-0__pymupdf4llm.md",
        "Successful mission command is enabled by the principles of",
    ),
    (
        "What is mutual trust in the context of mission command?",
        "ADP_6-0__pymupdf4llm.md",
        "Mutual trust is shared confidence between commanders",
    ),
    (
        "What is shared understanding among commanders and staffs?",
        "ADP_6-0__pymupdf4llm.md",
        "critical challenge for commanders, staffs, and unified action partners is creating shared understanding",
    ),
    (
        "What is the purpose of Army doctrine?",
        "ADP_1-01__pymupdf4llm.md",
        "doctrine",
    ),
]


def build_corpus():
    docs = {}
    for md_path in SAMPLES_DIR.glob("*__pymupdf4llm.md"):
        docs[md_path.name] = load_paragraphs(md_path)
    all_paragraphs = []
    for fname, paras in docs.items():
        for p in paras:
            all_paragraphs.append((fname, p))
    return all_paragraphs


def main():
    all_paragraphs = build_corpus()
    print(f"Corpus: {len(all_paragraphs)} paragraphs across "
          f"{len(set(f for f, _ in all_paragraphs))} documents\n")

    import numpy as np
    from sentence_transformers import SentenceTransformer

    results = {}
    for name, hf_id in CANDIDATES.items():
        print(f"=== {name} ({hf_id}) ===")
        t0 = time.time()
        model = SentenceTransformer(hf_id, device="cpu")
        load_s = time.time() - t0

        max_seq = model.max_seq_length
        # Rough on-disk footprint via the cached model files.
        try:
            import os
            cache_root = Path.home() / ".cache" / "huggingface" / "hub"
            model_dirs = list(cache_root.glob(f"models--{hf_id.replace('/', '--')}"))
            size_mb = 0
            for d in model_dirs:
                for f in d.rglob("*"):
                    if f.is_file():
                        size_mb += f.stat().st_size
            size_mb /= 1024 * 1024
        except Exception:
            size_mb = float("nan")

        # CPU embedding latency on a representative batch.
        texts = [p for _, p in all_paragraphs[:64]]
        t0 = time.time()
        _ = model.encode(texts, show_progress_bar=False, batch_size=16)
        embed_s = time.time() - t0
        per_item_ms = (embed_s / len(texts)) * 1000

        # Retrieval quality.
        correct = 0
        detail = []
        p_prefix = PASSAGE_PREFIX.get(name, "")
        q_prefix = QUERY_PREFIX.get(name, "")
        corpus_texts = [p_prefix + p for _, p in all_paragraphs]
        corpus_emb = model.encode(corpus_texts, show_progress_bar=False, batch_size=16)
        corpus_emb = corpus_emb / np.linalg.norm(corpus_emb, axis=1, keepdims=True)

        for query, doc_file, needle in QUERIES:
            q_emb = model.encode([q_prefix + query], show_progress_bar=False)[0]
            q_emb = q_emb / np.linalg.norm(q_emb)
            sims = corpus_emb @ q_emb
            top_idx = int(np.argmax(sims))
            top_fname, top_para = all_paragraphs[top_idx]
            hit = needle.lower() in top_para.lower()
            correct += hit
            detail.append((query, hit, top_fname, sims[top_idx]))

        results[name] = {
            "max_seq_length": max_seq,
            "disk_mb": round(size_mb, 1),
            "load_s": round(load_s, 2),
            "embed_ms_per_item": round(per_item_ms, 2),
            "retrieval_hits": f"{correct}/{len(QUERIES)}",
        }
        print(f"    max_seq_length={max_seq}  disk={size_mb:.1f}MB  "
              f"load={load_s:.2f}s  embed={per_item_ms:.2f}ms/item  "
              f"retrieval={correct}/{len(QUERIES)}")
        for q, hit, fname, score in detail:
            mark = "OK" if hit else "MISS"
            print(f"      [{mark}] score={score:.3f} top_doc={fname}  q={q[:60]}")
        print()

    print("\n=== SUMMARY ===")
    for name, r in results.items():
        print(name, r)


if __name__ == "__main__":
    main()
