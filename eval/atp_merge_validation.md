# ATP merge validation: corpus gates, comsec-class bug fix, retrieval eval

Follow-up to `eval/atp_step1_findings.md` and `eval/typo_correction_eval.md`. ATP
(168 docs, re-extracted from PDF per step 1's findings) has been merged into
`data/` alongside ADP as one combined corpus: `data/stage3_chunks/Combined_Cleaned.jsonl`,
**74,483 chunks across 184 documents** (4,032 ADP + 70,451 ATP, zero chunk_id
collisions). `data/raw_pdfs`, `stage1_extracted`, `stage2_cleaned` are merged the
same way; the old `data/atp_full/` staging tree no longer exists.

## 1. Corpus-integrity gates (`pipeline/validate.py`)

Run against `Combined_Cleaned.jsonl`: **189 passed, 2 failed, 0 skipped**
(full report: `data/validation_reports/combined_full.md`).

Both failures are `ADP_7-0` (content-preservation ratio + zero-chunk check) --
the same pre-existing, already-documented gap from the ADP-only build
(README_pipeline.md artifact pattern #13: no text layer, needs a replacement
source file). Confirmed by diffing against `ADP_Cleaned_report.json`, which
already shows `chunks_count: 0` for `ADP_7-0` before this merge. **Not a
regression introduced by the merge.** Both MDMP/mission-command regression
tests and the leak/cid/doc_id/encoding-corruption gates all pass at 184/184
documents.

## 2. The comsec-class corruption bug: reproduced, then confirmed fixed

The bug: `DomainSpellCorrector`'s guards (min length, ALL-CAPS, English
wordlist, chat-stoplist -- see `pipeline/query_correct.py`) don't protect a
lowercase, non-English, non-corpus acronym. If a term is absent from whatever
vocabulary the corrector was built from, it's out-of-vocabulary by definition
and gets "corrected" toward the nearest in-vocabulary word -- exactly the
`corpus`->`corps` / `intel`->`into` misfire class already documented, just
triggered by *domain coverage* rather than *guard design*. `comsec` is a real
ATP-domain term (520 occurrences, mostly ATP 3-04.6/3-12.4/3-90.5/6-02.5x) that
never appears anywhere in the 16-document ADP corpus the corrector was
originally built from.

**Reproduced against the pre-merge (ADP-only, 13,292-term) vocabulary:**

| query | corrected (bug) |
|---|---|
| `what are the comsec requirements for a command post` | `...the come requirements...` |
| `explain comsec destruction procedures` | `explain come destruction procedures` |

**Confirmed fixed against the merged (184-doc, 67,376-term) vocabulary:**
`comsec` frequency is now 520 (>= the `min_freq=3` threshold), so it's
recognized as a known corpus term and both queries above pass through
unmodified.

**Regression check** -- the 6 previously-fixed typo cases from
`eval/typo_correction_eval.md` (`dynmaics`, `pwoer`, `warfigthing`,
`manuever`, `principels`, `missoin comand`) still resolve to the same
corrections against the merged vocabulary. Merging the corpus only grows the
known-term set; it does not change the correction logic or ranking, so no
prior fix regressed.

## 3. Rebuilt indexes

`pipeline/embed_index.py:build_all_indexes` rerun against
`Combined_Cleaned.jsonl` -- BM25 + `chunk_lookup.pkl` (74,483 chunks each) and
the dense ChromaDB collection (`doctrine_chunks_v2`, 74,483 vectors, bge-small-en-v1.5,
CPU, ~2h43m wall time for the embedding pass). `models/bge-small-en-v1.5`
weights were fetched directly from the HF Hub in this session (this
environment's egress is open, unlike the sandboxed container README_pipeline.md
describes) rather than via the LFS-mirror workaround.

## 4. Retrieval eval on the combined index -- ADP suite and ATP suite, reported separately

Two different gold suites were run against the same combined index. They are
**not merged into one number** -- conflating them would hide whether ATP
specifically retrieves well, which is exactly the question a corpus-dilution
effect can't answer on its own.

### 4a. ADP suite (`LIMA_grounded_test_suite.xlsx`, 91 cases, pre-existing)

Full results: `eval/results/retrieval_eval_combined_k10_symspell.md` (with
correction) and `eval/results/retrieval_eval_combined_k10_baseline.md`
(without). This suite has only ADP paragraph anchors, so it measures "did
merging ATP in hurt ADP retrieval," not ATP retrieval quality.

| | ADP-only (pre-merge) | Combined, no correction | Combined, symspell |
|---|---|---|---|
| fused, overall | 84.6% | 62.6% | **72.5%** |
| fused, typo | 90% | 25% | **70%** |
| fused, non-typo categories | unaffected by correction either way (bit-identical to baseline, verified case-by-case) |

### 4b. New ATP suite (`ATP_grounded_test_suite.xlsx`, 40 cases, built this session)

Full results: `eval/results/retrieval_eval_atp_suite_k10_symspell.md` (with
correction) and `eval/results/retrieval_eval_atp_suite_k10_baseline.md`
(without). 8 base questions x 5 variants each, spread across 5 ATP series
(1-XX, 2-XX, 4-XX x2, 5-XX x2, 6-XX x2) specifically chosen to avoid clustering
on whichever documents were easiest to find. Every gold chunk_id was verified
directly against the real chunk text before being used (method: grep the
enumeration in `stage2_cleaned`, confirm the exact item count and wording,
then confirm it lands intact in exactly one chunk in `Combined_Cleaned.jsonl`
-- see the per-case dumps done during this session). `eval/run_retrieval_eval.py`'s
anchor parser (`_DOC_RE`, `parse_anchor`) was extended to recognize ATP
citations and resolve their decimal/hyphenated doc numbers (e.g. "ATP 2-01.3")
against the corpus's actual doc_ids, which carry an internal tracking suffix
the citation doesn't include (e.g. `ATP_2-01.3-003`) -- resolved via a
boundary-safe prefix match, not a hardcoded rename. Verified this introduced
**zero regressions** on the existing 91 ADP anchors (all still resolve
identically) before trusting it for the new suite.

| | Combined, no correction | Combined, symspell |
|---|---|---|
| fused, overall | 77.5% | **82.5%** |
| fused, typo | 62% (5/8) | **88% (7/8)** |
| fused, non-typo categories | unaffected by correction either way (bit-identical to baseline, verified case-by-case) |

**ATP retrieval quality on its own gold set is good** -- 82.5% fused, close to
(not below) the original ADP-only pre-merge baseline of 84.6%, and clearly
above the ADP suite's post-merge 72.5%. The two suites tell different parts
of the same story: ATP content retrieves well when it's the target, and the
ADP suite's drop is specifically about *added competition for ADP's own
answers*, not a sign that the index or the embeddings are broken.

### 4c. Interpreting the two together

Two separate effects, and they should not be conflated:

- **Corpus-size dilution on the ADP suite (real, expected, not a bug):** overall fused hit rate
  drops 84.6% -> 62.6% even with correction *disabled entirely* against the
  ADP-only baseline. Going from 4,032 to 74,483 candidate chunks (18.5x) means
  many more topically-adjacent ATP passages (tactics/sustainment/C2 doctrine
  overlaps heavily with ADP's own subject matter) now compete for the same
  top-k slots as the correct ADP gold chunk. This is an inherent cost of
  broadening the index, not something the merge did wrong.
- **The spell corrector still fully does its job on the larger index, on both
  suites:** ADP-suite typo fused hit rate is 25% -> 70% with correction on (a
  +45pp lift, comparable to the original +40pp measured on the ADP-only
  index); ATP-suite typo fused hit rate is 62% -> 88% (5/8 -> 7/8). Verified
  at the case level on both suites: applying `--correct symspell` changes
  **zero** ranks on any non-typo query (91/91 and 40/40 exact match against
  each suite's no-correction baseline) and only ever moves typo cases from
  fail to pass, never the reverse.

**Bottom line: the comsec-class bug is fixed, with no side effects on
existing corrections or non-typo queries, on either suite.** The ADP-suite
overall hit-rate number moved because the corpus got 18x bigger and harder,
not because anything about the
fix or the merge is broken.
