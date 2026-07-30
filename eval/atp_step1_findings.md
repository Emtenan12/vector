# ATP rebuild — step 1: does the ADP-era cleaning logic apply?

Sample-based check before committing to a 170-document run.

## Drive access

**Reachable from this session.** Folder `1VV1eHki…` lists fine, and both a
185 KB PDF and a 3.4 MB PDF downloaded successfully. The 10 MB
`download_file_content` cap and the intermittent failures recorded in
README_pipeline.md still apply and will matter at scale — several ATP PDFs
in the listing exceed 10 MB (`ATP_3-21.11-000.pdf` is 30.9 MB,
`ATP_3-21.8-001.pdf` 27.1 MB, `ATP_3-24.2-000.pdf` 25.0 MB), so those cannot
come through this connector at all and need another transfer route.

## Document count: 170 is correct, 264 is not supported

`A| Data description.pdf` reports **170 documents / 23,695 pages**, and its
own series breakdown sums exactly to 170:

| series | docs | | series | docs |
|---|---|---|---|---|
| ATP 1-XX | 8 | | ATP 5-XX | 4 |
| ATP 2-XX | 3 | | ATP 6-XX | 13 |
| ATP 3-XX | 90 | | ATP 7-XX | 4 |
| ATP 4-XX | 48 | | **total** | **170** |

The report labels this section "CORRECTED COUNTS", which implies it
supersedes an earlier figure — 264 is most likely that superseded number.
Nothing in the folder supports 264.

Caveat: I did not exhaustively enumerate every file in Drive (that needs
many paginated calls). I verified the report's internal arithmetic and
sampled both the root folder and the `ATP-3` subfolder, which are
consistent with it.

## Scope flag that was never resolved

The report marks **ATP 4-XX (Sustainment, 48 docs, 5,987 pages)** as
"⚠ DECISION Under consideration — may skip or extract selectively".

That decision was never recorded — but the Drive folder **does** contain
ATP 4-XX PDFs (4-02.x series, 4-10 through 4-13, 4-31, 4-32.1, 4-33, 4-41,
4-42, 4-44, 4-48, 4-70, 4-71, 4-90.5 and more). So they were collected
regardless. Including them is 48 docs / ~6,000 pages — roughly a quarter of
the corpus. **This needs an explicit yes/no before the full run**, not a
default.

## The finding: do NOT build on the upstream cleaned corpus

There are two candidate inputs, and they are not equivalent.

1. **Raw PDFs** — `1VV1eHki…` (+ `ATP-3` subfolder)
2. **An already-cleaned markdown corpus** — a *separate* folder
   (`1K9V3V1y…`) holding `.md` files plus the `.cleaning.json` sidecars

Compared head-to-head on `ATP_3-90.20-000` (64 pages), extracting the PDF
myself with pymupdf4llm versus the upstream `.md`:

| | my extraction | upstream cleaned |
|---|---|---|
| size | 135,765 chars | 130,523 chars (96.1%) |
| **leaked prompt fragments** | **0** | **12** |
| `(cid:N)` artifacts | 0 | 0 |
| U+FFFD | 0 | 0 |
| bare-bold page furniture | 208 | 0 |
| HTML page markers | 0 | 64 |
| heading levels used | h1–h6 | h1–h3 only |
| sections after splitting | 113 | 110 |

**The upstream corpus contains unfilled LLM figure-description
placeholders**, 12 in this one document:

```
> **[FIGURE — page 11]** replace this line with a description of the figure
> plus a Markdown transcription of any table.
```

That string is one of the two `LEAK_PATTERNS` in `pipeline/clean.py`
verbatim. A vision/LLM pass was supposed to replace each of these with a
figure transcription and never ran, so every figure in the document is
represented by an instruction to the model that was meant to describe it.
It is absent from my own extraction because pymupdf4llm never inserts such
placeholders.

At ~1% of document text and 12 per 64 pages, extrapolating naively across
23,695 pages suggests on the order of **4,000+ such placeholders** corpus-
wide. This is almost certainly related to the 529 ATP chunks production's
`_is_garbled` filter already discards.

**Conclusion: re-extract from the PDFs.** The upstream cleaned corpus is not
a shortcut — it carries a defect class this pipeline explicitly gates on,
and `pipeline/validate.py` would fail it on the leaked-artifact check.

## Does the ADP-era cleaning logic apply? Yes, unchanged

Against a fresh pymupdf4llm extraction, ATP presents the **same** artifact
profile ADP did: 208 bare-bold page-break furniture lines, the exact pattern
`_preclean()` was written for, and a full h1–h6 heading hierarchy for
`MarkdownHeaderTextSplitter` to work with. Median section size (443 chars)
is in the same range as ADP.

So the concern that upstream cleaning might conflict with `_preclean()`
resolves cleanly: it would have, but only if we consumed upstream output.
Extracting from PDF ourselves means there is no upstream pass to conflict
with, and no logic here is redundant.

One thing the upstream sidecars are still useful for: `word_retention` and
`stray_char_ratio` per document make a ready-made stratification signal for
sample-based validation. The sampled sidecar reports `word_retention
0.9917`, `stray_char_ratio 0.0221`, and warns "possible broken word
boundaries or glyph mapping; spot-check" — worth using to pick the
validation sample rather than choosing files by convenience.

## Scale

170 docs / 23,695 pages against ADP's 15 docs. Dense indexing alone ran
4m48s for 4,032 chunks; a ~14x corpus implies roughly 55,000–60,000 chunks
and about an hour of CPU embedding, before extraction time. The >10 MB
transfer ceiling is the more likely bottleneck than compute.
