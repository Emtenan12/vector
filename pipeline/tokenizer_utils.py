"""
Thin wrapper around the chosen embedding model's own tokenizer, so chunk
packing counts tokens the same way the embedder will -- not a word-count
approximation. See eval/embedding_eval.md for why this model was chosen and
what its real max_seq_length is.
"""
from functools import lru_cache

# BAAI/bge-small-en-v1.5, chosen over all-MiniLM-L6-v2 on real 18-query
# retrieval-accuracy testing (see eval/embedding_eval.md addendum): tied for
# best accuracy, no 256-token truncation, faster than gte-small on CPU.
# max_seq_length=512 is load-bearing, not cosmetic -- it's the reason this
# model was reconsidered (256 was silently truncating chunks under the old
# model). Full weights supplied locally at models/bge-small-en-v1.5/ since
# this environment cannot reach huggingface.co to download them itself.
EMBED_MODEL_NAME = "bge-small-en-v1.5"
EMBED_MODEL_MAX_SEQ_LENGTH = 512


@lru_cache(maxsize=1)
def _get_tokenizer():
    from transformers import AutoTokenizer
    import pathlib
    local_path = pathlib.Path(__file__).parent.parent / "models" / EMBED_MODEL_NAME
    if local_path.exists():
        return AutoTokenizer.from_pretrained(str(local_path))
    eval_partial_path = pathlib.Path(__file__).parent.parent / "eval" / "models" / EMBED_MODEL_NAME
    if eval_partial_path.exists():
        return AutoTokenizer.from_pretrained(str(eval_partial_path))
    return AutoTokenizer.from_pretrained(f"BAAI/{EMBED_MODEL_NAME}")


def count_tokens(text: str) -> int:
    tok = _get_tokenizer()
    return len(tok.encode(text, add_special_tokens=True))
