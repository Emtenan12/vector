"""
Thin wrapper around the chosen embedding model's own tokenizer, so chunk
packing counts tokens the same way the embedder will -- not a word-count
approximation. See eval/embedding_eval.md for why this model was chosen and
what its real max_seq_length is.
"""
from functools import lru_cache

# Set after eval/embedding_eval.md's decision. sentence_bert_config.json in
# the model repo is the source of truth for max_seq_length; this constant is
# duplicated here for use before the model files are staged for import.
EMBED_MODEL_NAME = "all-MiniLM-L6-v2"
EMBED_MODEL_MAX_SEQ_LENGTH = 256


@lru_cache(maxsize=1)
def _get_tokenizer():
    from transformers import AutoTokenizer
    import pathlib
    local_path = pathlib.Path(__file__).parent.parent / "eval" / "models" / EMBED_MODEL_NAME
    if local_path.exists():
        return AutoTokenizer.from_pretrained(str(local_path))
    return AutoTokenizer.from_pretrained(f"sentence-transformers/{EMBED_MODEL_NAME}")


def count_tokens(text: str) -> int:
    tok = _get_tokenizer()
    return len(tok.encode(text, add_special_tokens=True))
