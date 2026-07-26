# Embedding model evaluation

## What was planned vs. what could be executed

The plan (see `eval/run_embedding_eval.py`) was to A/B `all-MiniLM-L6-v2` against `bge-small-en-v1.5`,
`gte-small`, and `e5-small-v2` on real doctrine text extracted in the extraction eval — measuring
on-disk footprint, CPU embedding latency, and retrieval quality (does the known-correct real paragraph
rank #1 by cosine similarity for a set of real doctrine queries). The candidate shortlist itself came
from a 2026-era web search (below), not from training-data recall alone.

**The latency and retrieval-quality legs could not be executed in this sandbox.** This is a confirmed
environment constraint, not a skipped step:

1. Direct HTTPS to `huggingface.co` is policy-denied at the network proxy (403 CONNECT rejection,
   logged in the proxy's `recentRelayFailures`) — the same root cause that blocked `docling`'s model
   download in the extraction eval. Every Python path that fetches model weights
   (`sentence_transformers.SentenceTransformer(...)`, `huggingface_hub.hf_hub_download`, `fastembed`)
   hits this identical 403, regardless of library.
2. The sanctioned indirect path, the `hf_fs` MCP connector (used successfully elsewhere in this build
   to fetch PDF text and repo files), has a **hard, deterministic, override-less refusal on binary
   files**: `Refusing to cat non-text file: model.safetensors. The file extension or MIME type is
   known to be binary.` This was confirmed on `.safetensors`, `.onnx` (including the
   ARM64-INT8-quantized `model_qint8_arm64.onnx`, which would otherwise have been directly relevant to
   the iWave board's Cortex-A53 target), `.bin`, and `.h5` variants, across all 4 candidate models, by
   two independent agents plus direct attempts in this session — 100% failure rate, no transient
   success observed (unlike the Google Drive `download_file_content` size-correlated flakiness, which
   *did* eventually succeed on smaller files; this is a flat refusal regardless of size).
3. No Hugging Face Space offering text-embedding/feature-extraction as a remote task was available via
   `dynamic_space` (checked via `discover` — only image/video/OCR/TTS spaces listed), so remote
   inference wasn't an option either.

Per this environment's own proxy guidance ("do not retry organization policy denials — report them"),
this was not routed around (e.g. by hunting for alternate credentials). It's reported here as a real
gap: **CPU latency and retrieval-quality numbers below are not available for `bge-small-en-v1.5`,
`gte-small`, or `e5-small-v2` in this session.** What follows is the architecture/footprint comparison
that *is* verifiable without downloading weights (from each model's official `config.json` /
`sentence_bert_config.json`, fetched as small text files, which `hf_fs` does serve), plus the reasoning
used to make a decision anyway.

## Candidate shortlist (web search, 2026)

Search for current small CPU/edge embedding models surfaced `all-MiniLM-L6-v2` (called out repeatedly
as "the edge deployment workhorse," 22M params), `E5-Small` (~33M params, "pragmatic choice" for
edge/CPU per multiple 2026 sources, competitive MTEB scores), `BGE-small`/`gte-small` (both commonly
recommended CPU-friendly options), and `EmbeddingGemma-300M` (Google's on-device model, 300M params).
EmbeddingGemma was excluded from the shortlist without testing: at 300M parameters it's roughly
3-4.5x the size of the other 4 candidates, working against the "well under 1-2GB including runtime
overhead" constraint shared with the embedder *and* the 1.5B-parameter generative model *and* the OS,
on the same 4GB board.

## What's verifiable without downloading weights

| Model | Params (repo) | Hidden dim | Layers | `max_seq_length` | Weight file size (fp32, from Hub metadata) |
|---|---:|---:|---:|---:|---:|
| all-MiniLM-L6-v2 | 22M | 384 | 6 | **256** | 90,868,376 B (86.7 MB) |
| bge-small-en-v1.5 | ~33M | 384 | 12 | **512** | 133,466,304 B (127.3 MB) |
| gte-small | ~33M | 384 | 12 | **512** | 66,746,168 B (63.7 MB) |
| e5-small-v2 | ~33M | 384 | 12 | **512** | 133,466,304 B (127.3 MB) |

(File sizes via `hf_fs ls`, which returns metadata without transferring content — this part is real
data, not a guess. gte-small's smaller footprint despite 12 layers vs. bge/e5's matching size is
notable and would be worth re-verifying once weights are actually downloadable, since ~half the size
for the same layer count is a meaningful discrepancy that deserves scrutiny before trusting it.)

All four share the same 384-dim output and BERT-family architecture, so index storage cost
(ChromaDB vector size) is identical across candidates — footprint differences are purely in the model
weight file loaded into RAM at inference time.

The one number that matters most for finding #1's silent-truncation bug: **MiniLM is the only
candidate capped at 256 tokens** — bge/gte/e5 all support 512. That's directly relevant, since the
production bug this whole rebuild traces back to was chunks silently truncated at 256 tokens before
dense embedding. A model with a native 512-token ceiling gives the chunker (`pipeline/chunk.py`) more
headroom before hitting the atomic-unit-overflow last resort, independent of any retrieval-quality
delta.

## Decision: keep `all-MiniLM-L6-v2` for this build, with the gap flagged explicitly

This is **not** a "leaderboard citation" decision — it's a decision made under a confirmed inability to
run the intended empirical test, and that should not be dressed up as more rigorous than it is:

- It's the current production model — zero migration risk to the existing `doctrine_chunks_v2` Chroma
  schema, `hybrid_retrieval.py` loading code, and the cross-encoder reranker pairing already validated
  in production.
- `pipeline/chunk.py` and `pipeline/tokenizer_utils.py` are built against its real 256-token
  `max_seq_length` (confirmed from `sentence_bert_config.json`, not assumed), so chunk sizing is
  already correct for it specifically.
- Smallest weight footprint of the four (86.7MB) — directly favorable for the shared 4GB RAM budget.

**This should be revisited before being treated as final.** The 512-token alternatives are architecturally
plausible improvements (fewer forced chunk splits, all with comparable or smaller footprint than
MiniLM's closest competitors), but recommending a switch without the retrieval-quality and CPU-latency
numbers this task explicitly asked for would be exactly the "leaderboard citation" style decision the
task warned against. **Flagging back to the user**: a follow-up eval run in an environment with
unblocked `huggingface.co` egress (or with the weight files supplied another way) is needed to
actually A/B these before switching off the current production model.
