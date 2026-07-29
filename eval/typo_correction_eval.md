# Query-side spell correction: backend bake-off and before/after

Fixes the typo-robustness gap found by `eval/run_retrieval_eval.py`: typo
variants hit at 45% (dense) / 40% (sparse) against 80% / 85% on the primary
phrasing.

## Why the fix has to be query-side

The suite's scoring guide predicts that a primary-passes/typo-fails split
means "the failure is lexical (BM25) not semantic". The measured data
contradicts that: **dense degraded as hard as sparse** (-35pp vs -45pp), and
on the 20 typo cases 10 failed *both* retrievers while dense rescued a
sparse miss only twice.

Confirmed cause, by inspecting the embedder's own tokenizer rather than
inferring it:

| correct | tokens | typo | tokens |
|---|---|---|---|
| `dynamics` | `dynamics` | `dynmaics` | `d`+`##yn`+`##ma`+`##ics` |
| `power` | `power` | `pwoer` | `p`+`##wo`+`##er` |
| `warfighting` | `war`+`##fighting` | `warfigthing` | `war`+`##fi`+`##gt`+`##hing` |
| `maneuver` | `maneuver` | `manuever` | `man`+`##ue`+`##ver` |

A single vocabulary token shatters into 3-4 meaningless subwords, so the
query embedding lands nowhere near the passage embedding. Both indexes are
already built from correctly-spelled text, so no index-side change can
repair this — the query is the only place the damage is undoable.

One useful exception found while checking: `defence` is *already* a single
in-vocabulary token, so Q16's failure is caused by `charactristics` alone.

## Backend comparison

Both candidate approaches were built and measured rather than assumed. Both
use a frequency dictionary built **from the corpus**, not general English,
so corrections stay in-domain by construction.

| | baseline | symspell | rapidfuzz |
|---|---|---|---|
| dense, typo | 45% | **80%** | 70% |
| sparse, typo | 40% | **80%** | 60% |
| fused, typo | 50% | **90%** | 75% |
| fused, overall | 75.8% | **84.6%** | 81.3% |
| typo queries corrected | — | 19/20 | 15/20 |

`symspell` wins on recall at equal precision once tie-breaking is fixed
(below). `rapidfuzz` is more conservative — it declines `dynmaics`,
`pwoer`, `missoin`, `intnet`, `moblie`, `froms` and `manuever` — which
costs it 4 typo cases and ~3pp overall. `symspell` is the default.

## Guards, and what each one cost before it existed

A corrector that fires eagerly damages the categories it was not meant to
touch. Every guard below was added in response to an observed misfire, not
defensively:

| guard | misfire it prevents |
|---|---|
| general-English word set | `corpus`→`corps` (Q20 paraphrase), `intel`→`into` (Q13 casual) |
| contractions skipped | `aren't`→`agent` (Q5 trap) |
| chat-filler stoplist | `plz`/`gimme`/`whats` sit within edit distance 2 of real corpus terms |
| ALL-CAPS skipped | protects `MDMP`, `IPOE`, `COA`, `TLP`, `MDO` |
| min length 5 | short tokens are close to everything |

Candidate *ranking* mattered as much as candidate generation, because
several typos have two candidates at the same edit distance. Ranking order
is: edit distance, then first-character preserved, then not-a-retrieval-
stopword, then corpus frequency. Two orderings were tried and rejected:

- **frequency-first** turns `froms` into `from` — a deletion to a common
  function word that is then dropped by the BM25 stopword filter entirely,
  deleting the query's only topical noun — instead of `forms`.
- **length-preservation-first** turns `mision` into `vision` rather than
  `mission`, and `principls` into `principle` rather than `principles`.

The first-character rule is what makes `mision`→`mission` stable; typists
rarely miss the opening letter.

## Before / after, all categories

Fused retrieval, k=10. The non-typo rows are the point of this table: a
spell corrector is only safe if it leaves them alone.

| variant | before | after | delta |
|---|---|---|---|
| primary | 95% | 95% | 0.0 |
| paraphrase | 85% | 85% | 0.0 |
| casual | 85% | 85% | 0.0 |
| **typo** | **50%** | **90%** | **+40.0** |
| trap | 55% | 55% | 0.0 |
| overall | 75.8% | 84.6% | +8.8 |

Verified at case level, not just in aggregate (an aggregate can hide a
swap): **0 cases regressed from pass to fail**, 23 cases went fail to pass,
all 23 in the typo category. Queries the corrector did not modify produced
**bit-identical ranks** across all three retrievers, which is the expected
result and confirms the harness is deterministic.

## What is still broken

Two typo cases still fail, and neither is a spelling problem — both are
corrected exactly right:

- **Q5** `list the principels of war` → `list the principles of war`. The
  gold anchor is para 4-28, *principles of joint operations*; the typo
  variant also rephrases "joint operations" to "war", so this is a
  vocabulary-mismatch failure wearing a typo's clothing.
- **Q6** `what is missoin comand` → `what is mission command`. Q6's
  **primary** variant fails at baseline too, so this is a pre-existing
  retrieval failure for that question, independent of typos.

In other words the typo gap is essentially closed; the residue is a
different problem that the typo category was masking.

## Integration note

`pipeline/query_correct.py` is the prototype and is wired into the eval
harness via `--correct`. Production retrieval runs through
`hybrid_retrieval.py` on the HF Space, which is not in this repo — applying
this there means calling `DomainSpellCorrector.correct()` on the query
string once, before it reaches either retriever, and (recommended) logging
the edit list so corrections stay auditable.

Cost: vocabulary build is ~1s over 4,032 chunks; the SymSpell index is
built once at startup. Correction itself is sub-millisecond per query. Both
are acceptable for the ARM deployment target, but the SymSpell delete-index
carries a memory cost that should be measured on-device before assuming it
fits alongside the model and vector store.
