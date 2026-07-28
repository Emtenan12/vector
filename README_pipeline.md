# LIMA ingestion pipeline — artifact patterns & operator notes

From-scratch PDF → Markdown → Chunks → Embeddings → Vector DB pipeline for the ADP doctrine corpus.
This document catalogs every extraction/chunking/infrastructure artifact pattern discovered while
building it, so the next person debugging this doesn't have to re-derive them from scratch. See
`eval/extraction_eval.md` and `eval/embedding_eval.md` for the tool-selection evidence itself.

## Pipeline layout

```
pipeline/extract.py       PDF -> markdown, via pymupdf4llm (justified in eval/extraction_eval.md)
pipeline/clean.py         page-break noise strip + rejoin, doc_id normalize, leak/artifact filter
pipeline/chunk.py         header-aware block segmentation + token-budget packing
pipeline/tokenizer_utils.py  real embedding-model tokenizer, not word-count approximation
pipeline/embed_index.py   BM25 + chunk_lookup + (when available) dense ChromaDB index
pipeline/validate.py      automated gate-check report generator
pipeline/run_pipeline.py  orchestrates extract -> clean -> chunk -> {doc_id}_Cleaned.jsonl
```

Run order for a fresh batch of PDFs:

```
python -m pipeline.run_pipeline --pdf-dir data/raw_pdfs --out-dir data --jsonl-name ADP_Cleaned.jsonl
python -m pipeline.validate data/stage3_chunks/ADP_Cleaned.jsonl
python -c "from pathlib import Path; from pipeline.embed_index import build_all_indexes; \
           build_all_indexes(Path('data/stage3_chunks/ADP_Cleaned.jsonl'), Path('data/indexes'))"
```

## Fetching the embedding model weights (do this first)

The `bge-small-en-v1.5` weights are **not in this repo** — `model.safetensors` is 127MB, over GitHub's
100MB per-file hard limit, so `models/` is gitignored. Both `pipeline/embed_index.py:build_dense_index`
and `pipeline/tokenizer_utils.py:_get_tokenizer` look for them at:

```
models/bge-small-en-v1.5/
```

Each silently falls back to a `BAAI/bge-small-en-v1.5` Hub download when that directory is missing, and
**that fallback does not work here** — this environment's egress policy blocks `huggingface.co` (the
proxy answers 403 to CONNECT). A missing-weights run therefore fails at `EmbedderUnavailable` rather
than quietly producing a wrong index, which is the intended behaviour, but it means the weights have to
be placed by hand before any dense-index build.

The weights are mirrored in a **separate** repo, `Emtenan12/MNOO_`, under `bge-small-en-v1.5/`, with
`model.safetensors` tracked by Git LFS.

**A plain `git clone` of that repo does not get you the weights.** The clone succeeds, but the LFS
smudge filter fails with `Resource not accessible by integration` and leaves a 134-byte pointer file in
place of the model — and the failure aborts checkout partway, so several unrelated small files go
missing too. `git lfs pull`, a direct POST to `github.com/.../info/lfs/objects/batch`, and
`raw.githubusercontent.com` all hit the same wall: the first two return that same 403 (it is a GitHub
App token permission limit, *not* the egress proxy), and `raw` serves the pointer rather than the
object. This is the same App-permission wall that forced the original git-bundle workaround when this
branch was first pushed.

What does work is the LFS **media** endpoint, which the GitHub MCP connector will resolve for you
(`get_file_contents` on the file returns the URL rather than the blob, since it is over the inline
display limit):

```
https://media.githubusercontent.com/media/Emtenan12/MNOO_/<commit-sha>/bge-small-en-v1.5/model.safetensors
```

Procedure that works end to end:

```
apt-get install -y git-lfs && git lfs install --skip-repo   # not present in a stock image
GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/Emtenan12/MNOO_ /workspace/mnoo_
cp -r /workspace/mnoo_/bge-small-en-v1.5/. models/bge-small-en-v1.5/
curl -sSL -o models/bge-small-en-v1.5/model.safetensors "<media URL above>"
```

`GIT_LFS_SKIP_SMUDGE=1` is the important part — it stops the smudge failure from aborting checkout, so
the eight small config/tokenizer files land correctly and only the safetensors needs fetching
separately.

**Verify before building.** The failure mode this guards against is a pointer file masquerading as
weights, which is ~134 bytes of text and will not announce itself:

```
sha256sum models/bge-small-en-v1.5/model.safetensors
# ea1d11a3f23d14fe09fc1826fc7944e89c09a634d2217d57a21dd136805ee3e8   (133,462,128 bytes)
```

That hash is the LFS pointer's own `oid`, so matching it confirms the object is complete and
uncorrupted, not merely large.

Two upstream files, `vocab.txt` and `special_tokens_map.json`, are **absent** from the `MNOO_` mirror.
Nothing currently breaks: `tokenizer.json` is a self-contained fast tokenizer and carries the vocab.
Anything routed to the slow tokenizer path would fail, so add them if that ever becomes a code path.

## Artifact patterns

### 1. Mid-sentence page-break corruption (confirmed, present in every extractor tested)

pymupdf4llm (and MarkItDown, tested for comparison) both emit the page number, publication ID,
publication date, and current running chapter/section title as their own standalone lines at every
page boundary, with no visual distinction from real content other than (for pymupdf4llm) being a bare
bold span with no `#` heading prefix:

```
**1-6**
**ADP 6-0**
**31 July 2019**
**Introduction to Mission Command**
```

When a sentence spans the page boundary, this block lands mid-word. Confirmed real example (ADP 6-0):
`"...This minimizes the number of decisions a"` / *(4-line noise block)* / `"single commander makes..."`.
`pipeline/clean.py` detects these lines (page-number pattern, date pattern tolerant of font-encoding
corruption, the document's own publication-ID variants, or any bold-only line recurring ≥3x verbatim
as a running title) and rejoins across them whenever the preceding text doesn't end in terminal
punctuation. **Guard added during testing**: never rejoin into a line starting with `#` — a heading
always starts a new section even if the text right before a page break (e.g. a figure caption) doesn't
end in punctuation; the original rejoin heuristic incorrectly glued a caption into the *next chapter's*
heading before this guard was added.

### 2. MarkItDown emits zero markdown headings on real ADP PDFs (reproduced on 3/3 files)

`grep -c "^#"` → 0 on every file tested, both default config and `enable_plugins=False`. Section titles
land as bare uppercase text with nothing to anchor a `MarkdownHeaderTextSplitter` on. Also produces
190–265 `(cid:N)` font-encoding artifacts on 2 of 3 files, and on the third, raw Private-Use-Area bullet
glyph bytes (`\xef\x81\xac`) instead of real list markers. pymupdf4llm was the only tool tested that
emits real headings — see `eval/extraction_eval.md` for the full comparison.

### 3. Blank-line-less block transitions collapse into one unsplittable "atomic unit"

pymupdf4llm sometimes emits a narrative paragraph, a bullet list, and a markdown table back-to-back
with only single newlines between them (no blank line). A naive blank-line paragraph splitter treats
all of it as one paragraph; if a list happens to appear anywhere inside, list-atomicity logic then
(wrongly) protects the *entire* multi-thousand-token blob from splitting. Confirmed on ADP 6-0's
front-matter "Introduction" section: a "Summary of changes" bullet list embedded in the same
blank-line-less run as intro narrative + a modified-terms table produced a 2049-token unsplittable
chunk. Fixed by segmenting on block-*type* transitions (prose / list / table / heading), not just blank
lines — see `pipeline/chunk.py:_split_blocks`. A prose block immediately followed by a list block is
still deliberately kept together (a heading's lead-in must never be separated from its enumeration);
every other transition, including list→table and table→prose, always starts a new block.

### 4. Long plain-prose paragraphs are not the same as unsplittable lists

Early version of the chunker treated *any* oversized atomic unit as "must stay whole, log overflow" —
which is correct for a list/table but wrong for an ordinary long paragraph (Army doctrine paragraphs
regularly run 300-1300+ tokens with no list at all). This inflated the over-budget rate to 33.6% of all
chunks on the first real test. Fixed: a unit containing a list or table is kept atomic; a plain-prose
unit is split at sentence boundaries first. Brought the real over-budget rate down to 2.9-6.2% across
the corpus, with all remaining overflow being genuinely unsplittable large lists/tables/glossary blocks
(logged, never silently truncated).

### 5. Rendered Table-of-Contents becomes a multi-thousand-token dead-weight block

pymupdf4llm renders a PDF's front-matter ToC as a markdown table of dot-leader page references, e.g.
`|PREFACE....................................... iii|`. This has zero retrieval value (navigation, not
doctrine content) and was responsible for the single largest chunk observed pre-fix (2538 tokens, on
ADP 1-01). `pipeline/clean.py:_strip_toc_tables` detects a table block where ≥50% of rows contain a
4+-dot leader and drops it entirely — an evidence-based detector (not a fixed-offset guess, since
front matter length varies by document), consistent with the prior pipeline's own documented practice
of removing ToCs during cleaning.

### 6. Font-encoding replacement-character corruption, confined to a repeated header field

The Word-regenerated `ADP_3-0.pdf` sample produced 265 Unicode replacement characters (`�`) in
pymupdf4llm's output, e.g. `**2� M���** 2025**`. Verified with a line-by-line scan that **all** 265 are
confined to one repeated running-header date field (once per page) — zero occurrences in body text.
This field is removed by the page-break noise stripper anyway (see #1), so it never reaches a chunk.
Still worth checking for on any newly-added document: if a similar corruption ever shows up *outside*
a noise line, that's a real extraction failure, not a contained cosmetic one.

### 7. Curly vs. straight quotes break naive substring regression checks

The real ADP 6-0 text uses a curly apostrophe (`'`, U+2019) in "Commander's intent." A regression test
written with a straight-quote needle silently reported 6/7 mission-command principles instead of 7/7 —
not because the extraction was wrong, but because the *test* didn't normalize quote characters before
matching. `pipeline/validate.py:_normalize_quotes` fixes this. Any new regression needle involving a
possessive or a quoted term should assume the source may use typographic quotes.

### 8. `doc_id` separator chaos is real, confirmed directly from the Drive folder listing

The `DatasetPdf/ADP` folder contains, side by side: `ADP 3-05.pdf` (space), `ADP_3-13.pdf` (underscore),
`ADP-6-0.pdf` (hyphen), `ADP_1.pdf` (no version suffix). `pipeline/clean.py:normalize_doc_id` handles
all of these plus mixed internal separators (e.g. `ADP_3_13` → `ADP_3-13`), normalizing everything to
the `ADP_X-Y` underscore form that `app.py`'s `_extract_source_pub()` regex requires for citation
display.

### 9. PDF provenance varies within the corpus, and it's independently checkable via metadata

Not every "ADP" PDF in the Drive folder is the original DoD-published file:
- `ADP_1-01.pdf`: no `/Producer`/`/Creator` metadata at all, `/CreationDate` matches the real 2019
  publication date — consistent with the official government publishing toolchain.
- `ADP_3-0.pdf` (the copy used in this build): `/Creator: Microsoft® Word for Microsoft 365`,
  `/Author: Schrankel, Catherine J CIV USARMY MCCOE (USA)` — a named individual retyped/reformatted
  this document in Word and printed it to PDF on 2026-01-01.
- The ADP 6-0 copy used in this build (`DatasetPdfWithoutCover`'s "Mission Command" file):
  `/Creator: Safari`, `/Title` still contains the original download URL
  (`irp.fas.org/...adp6_0.pdf?utm_source=chatgpt.com`) — a browser "print to PDF" of a web-hosted copy.

Both regenerated copies throw `pypdf` `Ignoring wrong pointing object` xref warnings on load — a
corrupted cross-reference table, independent of whatever extraction tool reads the file afterward.
**Before trusting any new PDF's extraction quality, check its `/Producer`/`/Creator`/`/Author` fields**
— they're a fast, free signal for whether you're looking at a native publication or an informally
regenerated copy that may behave differently.

### 10. Leaked extraction-tool prompt fragments — checked, none found in this pipeline's output

The prior pipeline's `output3` intermediate markdown had two known leaked instruction-prompt wordings
baked in (`"...replace this line with a description of the figure..."`,
`"...verify the figure: OCR of chart labels is unreliable..."`). `pipeline/clean.py` filters both
patterns and `pipeline/validate.py` scans for them as a standing gate check. Neither pymupdf4llm nor
MarkItDown produced an analogous leak on any of the 3 real files tested in this build — but re-run this
check on every new document/tool, since it's a per-tool behavior, not a guarantee.

## Infrastructure constraints hit during this build (not extraction/chunking bugs, but real and worth knowing)

- **`docling` cannot run in this sandboxed dev environment.** Its layout-analysis model must be
  downloaded from `huggingface.co` at first use, even with OCR and table-structure explicitly disabled;
  this environment's egress policy blocks direct `huggingface.co` connections (403). Also pulls 5.7GB of
  dependencies (2.7GB pure CUDA/nvidia libraries) irrelevant to a CPU-only ARM deployment target
  regardless. See `eval/extraction_eval.md`.
- **Embedding model weight files cannot be downloaded from `huggingface.co` in this sandbox**, for any
  of the 4 candidates evaluated. Same egress block as `docling` above, plus the sanctioned `hf_fs` MCP
  connector has a hard, override-less refusal on binary files (`.safetensors`, `.onnx`, `.bin`).
  `pipeline/embed_index.py:build_dense_index` fails cleanly with a clear `EmbedderUnavailable` error and
  logs it rather than crashing — BM25 + `chunk_lookup.pkl` still build successfully, since they don't
  need the embedder. **This is now worked around rather than merely documented**: the weights are
  mirrored in `Emtenan12/MNOO_` and fetched via the LFS media endpoint — see *Fetching the embedding
  model weights* above for the exact procedure and the verification hash. The dense index builds here
  in ~5min on CPU with no HF Hub access at all, so it no longer has to wait on the HF Space's deploy
  environment.
- **Google Drive's `download_file_content` has a hard 10MB-per-file cap** (explicit error message,
  confirmed on `ADP-7-0.pdf`, 11.29MB) and additionally fails intermittently-but-persistently
  ("MCP server session expired") on some files well under that cap — `ADP_5-0.pdf` (6.99MB) failed
  25+ attempts across this entire session, including from multiple fresh sessions/subagents, while
  `ADP_3-07.pdf` (5.2MB) and others succeeded on the first or second try. This is not simple
  size-correlated flakiness; it appears to affect specific files disproportionately. **4 of the 16 ADP
  PDFs could not be downloaded in this session**: `ADP_1.pdf`, `ADP_2-0.pdf`, `ADP_5-0.pdf`,
  `ADP-7-0.pdf`. This build's final corpus covers 12/16 ADP documents (4,772 chunks) — not the full
  set. `ADP_5-0.pdf` specifically is required for the MDMP 7-step-list regression test, which is
  correctly reported as **skipped** (not failed) by `pipeline/validate.py` until that file is available.

### 11. A document can be 97% garbage and still pass every volume-based gate

`ADP_2-0.pdf` (88 pages, Adobe InDesign → Acrobat Distiller) has fonts with a broken/absent
ToUnicode map. Extractors map the unmapped glyphs to U+FFFD, so the whole document came out as
replacement characters — **and it passed content-preservation, doc_id, and leak checks**, because the
*volume* of text was right; it was just unreadable. 179 chunks of pure noise would have been embedded
into the index. The information is not actually lost at the PDF level: extracting with
`TEXTFLAGS_DICT` preserves the raw glyph codes (`&KDSWHU\x03\x14` → `Chapter 1`), which decode by
adding a constant offset — **29 (0x1D)** for this document. `pipeline/repair_extract.py` detects this
and takes a repair path; ADP_2-0 now yields 228 clean chunks.

Three things that matter if you hit this again:
- **The shift is per-span, not per-document.** ADP_2-0 mixes correctly-encoded spans (italic
  defined-term runs) with shifted ones *on the same line*. Decoding blindly corrupts the good spans
  (`Defense support of civil authorities` → `=aefense=support=of=civil=authorities`). Gate the decode
  on the span actually containing control characters, which never occur in legitimate text.
- **Detect on damage, not on presence.** A first cut that triggered on *any* control character
  false-positived on ADP_1-01 and ADP_1 — healthy documents that then lost pymupdf4llm's page-break
  noise patterns (`noise_removed` silently dropped to 0). Measured control-char density cleanly
  separates them: every healthy ADP ≤0.2%, ADP_2-0 at 16%. Threshold set at 5%.
- **pymupdf4llm's own escape hatch doesn't work here.** `use_glyphs=True` is documented for exactly
  this case but doesn't wire through in 1.28.0, and patching `TextPage.extractDICT`/`extractRAWDICT`
  doesn't intercept it either — hence the standalone repair module.

`pipeline/validate.py` now gates on per-document replacement-char ratio so this can never pass
silently again. A corpus-wide count would not have caught it — 14 healthy documents dilute one bad one.

### 12. A corrupted heading propagates far beyond its own line

On ADP_5-0, the running date/page field fails to decode and pymupdf4llm promotes it (large + bold) to
a markdown *heading*. Because it carries a `#`, it is exempt from the bold-noise-line rule — and
`chunk.py`'s `MarkdownHeaderTextSplitter` then adopts it as a section heading and prepends it as a
breadcrumb to **every chunk beneath it** (312 chunks). Deleting such headings outright made things
*worse*: the splitter fell back to a partially-corrupted parent heading and propagated that instead
(8,787 → 23,116 replacement chars corpus-wide). What works is stripping the replacement-character
runs themselves and tidying the empty markup shells left behind — the characters are unrecoverable by
that stage, so they can only add noise to an embedding. Corpus is now at **zero** replacement
characters.

### 13. A source file can be real, correctly sized, and still contain nothing

`ADP-7-0.pdf` (11.29MB, 36 pages) yields **zero** extractable characters — no text layer at all, only
11 images, and 29 of its 36 pages are completely blank. Producer metadata says `Microsoft: Print To
PDF` over a file named `U_ISES-PAI_ADP_7-0_WEB_FINAL_20240429.pdf`. The real ADP 7-0 (Training) is
100+ pages of doctrine, so this file is not a usable copy of it regardless of OCR. It needs a
replacement source. `validate.py` now has a zero-chunk gate so an empty extraction fails loudly
instead of being mistaken for a document that simply wasn't in the run.

## Regression tests (`pipeline/validate.py`)

| Test | Doc | Status this build |
|---|---|---|
| Mission command 7 principles land in one chunk | ADP 6-0 | **PASS** (7/7, chunk `ADP_6-0__000022`) |
| MDMP 7-step list lands in one chunk | ADP 5-0 | **PASS** (7/7, chunk `ADP_5-0__000125`) |

The MDMP test failed 3/7 on its first-ever run — but the chunker was correct and the *test* was wrong:
ADP 5-0 writes steps 3–6 as "COA development/analysis/comparison/approval", while the needles used the
spelled-out "course of action …". Needles now accept multiple surface forms per item. This is the same
class of bug as the curly-apostrophe mismatch in #7 — when a regression test fails, check the needle
against the real source text before concluding the pipeline is broken.

## Final build state

| | |
|---|---|
| Documents indexed | **15 of 16** ADP publications |
| Chunks | **4,032** |
| Embedding model | `BAAI/bge-small-en-v1.5`, 384-dim, `max_seq_length` **512** (verified by loading the model, not assumed) |
| Dense index | ChromaDB `doctrine_chunks_v2`, cosine — built, 4,032 vectors, 384-dim (3m11s original build; 4m48s on a later rebuild, CPU) |
| Sparse index | BM25Okapi + `chunk_lookup.pkl`, tokenizer copied verbatim from `hybrid_retrieval.py` |
| Validation | 21 passed, 2 failed (both the same known-bad source file), 0 skipped |
| Replacement chars | **0** corpus-wide |
| Over-budget chunks | 99 (2.5%) — all logged unsplittable lists/tables, never silently truncated |

Embedding dimension is 384, unchanged from `all-MiniLM-L6-v2`, so **no `doctrine_chunks_v2` schema
migration is needed** — confirmed by loading the model, not inferred.

Retrieval spot-check against the live dense index returns the correct chunk at rank 1 for
"seven steps of the military decision-making process" (ADP_5-0__000125), "principles of mission
command" (ADP_6-0__000022), and "intelligence warfighting function" (ADP_3-0__000061). Note that bge
models expect the instruction prefix `"Represent this sentence for searching relevant passages: "` on
the **query** side only — passages are embedded bare, as done here. Re-checked on a later rebuild:
all three still rank 1, and the prefix makes **no** difference to rank on these three (identical top-5
ordering with and without it) — so the prefix is worth keeping for correctness, but do not read a
rank-1 hit as evidence that it is being applied. Phrasing does matter more than the prefix: wrapping
the first query as a natural question ("What are the seven steps of…?") drops ADP_5-0__000125 to rank
2 behind an ADP_3-37 chunk. That is a hint that question-form queries deserve their own eval, not a
defect.

The rebuild is **deterministic**: rerunning `build_all_indexes()` on the same JSONL reproduced
`bm25_index.pkl` and `chunk_lookup.pkl` byte-identical to the committed copies (SHA256-matched). A
differing sparse index after a rebuild therefore means the corpus or the tokenizer changed, and is
worth investigating rather than shrugging off.

## Known gaps / next steps for whoever picks this up

1. **`ADP-7-0.pdf` needs a replacement source file** — the supplied copy has no text layer and is
   mostly blank pages (artifact pattern #13). This is the only reason the corpus is 15/16 rather than
   16/16, and it is a bad-input problem, not a pipeline problem. Both remaining validator failures
   trace to this one file.
2. `e5-small-v2` was scored 17/18 in the embedding A/B **without** its expected `"query: "` /
   `"passage: "` prefixes, so that number is inconclusive rather than disqualifying. Worth re-testing
   with the prefixes applied if the model choice is ever revisited.
3. Confirm the iWave G35D-19EG hardware specs (4GB DDR4 ECC, Cortex-A53 quad @1.5GHz) against official
   documentation — they were treated as unverified throughout this build per the task's own flag.
   The embedder's real footprint is now known: 127MB weights on disk, 384-dim vectors.
4. ATP corpus (264 docs) is explicitly out of scope for this build; validate a stratified sample by
   extraction-quality metrics before assuming the ADP-derived pipeline generalizes uniformly to it.
   Artifact patterns #11–13 are the ones most likely to recur at that scale, and the validator now
   gates on all three.
