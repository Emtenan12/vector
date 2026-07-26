"""
Embedding + indexing stage: build the BM25 sparse index, dense ChromaDB
collection, and chunk lookup table that hybrid_retrieval.py already knows
how to load -- same collection name, same file names, same chunk schema, so
this is a drop-in replacement for the existing indexes/ directory, not a
new schema.

No LangChain or other framework here: BM25 (rank_bm25), the embedder
(sentence-transformers), and the vector store (chromadb) are called
directly, since each already does exactly this one job with no abstraction
gap to fill.

Tokenization is copied verbatim from hybrid_retrieval.py rather than
reimplemented, because the on-disk BM25Okapi object only works correctly if
the same token stream is used at both index-build time and query time --
diverging here would silently degrade sparse retrieval.
"""
import json
import logging
import pickle
import re
from pathlib import Path

from pipeline.tokenizer_utils import EMBED_MODEL_NAME

logger = logging.getLogger(__name__)

COLLECTION_NAME = "doctrine_chunks_v2"

# Verbatim from hybrid_retrieval.py -- see module docstring.
_STOPWORDS = {
    "what", "is", "are", "the", "a", "an", "of", "in", "on", "at", "to",
    "for", "how", "does", "do", "did", "was", "were", "be", "been", "being",
    "define", "defined", "definition", "explain", "explained", "describe",
    "described", "list", "give", "tell", "me", "us", "you", "i", "my",
    "and", "or", "but", "if", "then", "that", "this", "it", "its",
    "with", "from", "by", "about", "which", "when", "where", "who", "why",
    "can", "could", "would", "should", "will", "may", "might", "must",
    "not", "no", "yes", "also", "all", "any", "some", "than", "more",
    "according", "based", "per", "as", "into", "up", "out",
}
_PUNCT_STRIP = str.maketrans("", "", '.,?!;:"\'()[]{}')


def _tokenize(text: str) -> list[str]:
    return [
        w for w in (raw.translate(_PUNCT_STRIP) for raw in text.lower().split())
        if w and w not in _STOPWORDS and len(w) >= 2
    ]


def load_chunks_jsonl(path: Path) -> list[dict]:
    chunks = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                chunks.append(json.loads(line))
    return chunks


def build_bm25_index(chunks: list[dict], out_path: Path) -> None:
    from rank_bm25 import BM25Okapi

    chunk_ids = [c["chunk_id"] for c in chunks]
    texts = [c["text"] for c in chunks]
    corpus_tokens = [_tokenize(t) for t in texts]
    bm25 = BM25Okapi(corpus_tokens)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        pickle.dump({"bm25": bm25, "chunk_ids": chunk_ids}, f)
    logger.info("BM25 index (%d chunks) written to %s", len(chunks), out_path)


def build_chunk_lookup(chunks: list[dict], out_path: Path) -> None:
    lookup = {c["chunk_id"]: c for c in chunks}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as f:
        pickle.dump(lookup, f)
    logger.info("Chunk lookup (%d chunks) written to %s", len(chunks), out_path)


class EmbedderUnavailable(RuntimeError):
    """Raised when the embedding model's weights can't be loaded (e.g. the
    HF Hub egress block confirmed in eval/embedding_eval.md). Callers should
    catch this and still keep the BM25 + chunk_lookup outputs, which don't
    depend on the embedder, rather than losing all index-build progress."""


def build_dense_index(chunks: list[dict], chroma_dir: Path, batch_size: int = 256) -> None:
    try:
        from sentence_transformers import SentenceTransformer
        import chromadb
    except Exception as exc:  # pragma: no cover - import-time environment issue
        raise EmbedderUnavailable(f"required package unavailable: {exc}") from exc

    try:
        embedder = SentenceTransformer(EMBED_MODEL_NAME, device="cpu")
    except Exception as exc:
        raise EmbedderUnavailable(
            f"could not load embedding model {EMBED_MODEL_NAME!r}: {exc}"
        ) from exc

    chroma_dir.parent.mkdir(parents=True, exist_ok=True)
    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = client.create_collection(
        COLLECTION_NAME, metadata={"hnsw:space": "cosine"}
    )

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i : i + batch_size]
        batch_texts = [c["text"] for c in batch]
        batch_ids = [c["chunk_id"] for c in batch]
        batch_meta = [
            {
                "doc_id": c.get("doc_id", ""),
                "source_file": c.get("source_file", ""),
                "token_count": c.get("token_count", 0),
            }
            for c in batch
        ]
        embeddings = embedder.encode(batch_texts, show_progress_bar=False).tolist()
        collection.add(
            documents=batch_texts,
            embeddings=embeddings,
            ids=batch_ids,
            metadatas=batch_meta,
        )
        logger.info("Embedded %d / %d chunks", min(i + batch_size, len(chunks)), len(chunks))

    logger.info("Dense index (%d chunks) written to %s", len(chunks), chroma_dir)


def build_all_indexes(jsonl_path: Path, index_dir: Path) -> dict:
    """Build BM25 + chunk_lookup unconditionally, then attempt the dense
    index. Returns a status dict so callers/validate.py can report a
    partial build honestly instead of crashing or silently skipping."""
    chunks = load_chunks_jsonl(jsonl_path)
    build_bm25_index(chunks, index_dir / "bm25_index.pkl")
    build_chunk_lookup(chunks, index_dir / "chunk_lookup.pkl")

    status = {"chunks": len(chunks), "bm25": True, "chunk_lookup": True, "dense": False,
              "dense_error": None}
    try:
        build_dense_index(chunks, index_dir / "chroma_db")
        status["dense"] = True
    except EmbedderUnavailable as exc:
        status["dense_error"] = str(exc)
        logger.warning(
            "Dense index NOT built (embedder unavailable): %s. "
            "BM25 + chunk_lookup were still written -- rerun build_dense_index "
            "once the embedding model can be loaded (e.g. in an environment "
            "with Hugging Face Hub egress, or with weights supplied locally).",
            exc,
        )
    return status
