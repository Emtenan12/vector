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
built once at startup. Correction itself is sub-millisecond per query.

## Measured memory footprint

Measured as RSS deltas in an isolated process (`/proc/self/status` VmRSS,
`gc.collect()` between stages), not estimated from the vocabulary file size.

| stage | RSS | delta |
|---|---|---|
| interpreter + imports | 9.9 MiB | — |
| + corpus chunks (build-time only) | 21.8 MiB | +11.8 |
| + vocabulary Counter (13,292 terms) | 23.4 MiB | +1.5 |
| + English guard set (82,834 terms) | 30.1 MiB | +6.8 |
| + SymSpell corrector (prefix 5) | 36.0 MiB | +5.9 |
| peak RSS (`ru_maxrss`) | **36.0 MiB** | |

The concern that prompted this was correct: the delete-index is far larger
than its source dictionary. At the original `prefix_length=7` the index
measured **14.4 MiB from a vocabulary occupying 1.5 MiB — roughly 14x**,
and process peak was 51.3 MiB.

### prefix_length is the dominant term, and reducing it is free here

| max_edit | prefix_length | index size | build | delete entries |
|---|---|---|---|---|
| 1 | 7 | 2.8 MiB | 0.04s | 32,903 |
| 2 | 7 | 14.4 MiB | 0.16s | 87,435 |
| **2** | **5** | **0.6 MiB** | **0.07s** | **20,163** |
| 3 | 7 | 21.2 MiB | 0.33s | 123,776 |

`prefix_length=5` is a **24x** reduction over `prefix_length=7`, and it is
not a quality trade on this corpus: all three of the configurations above
produce **byte-identical corrections** on all 26 corrections the suite
exercises, and a full 91-case re-run at prefix 5 differs from prefix 7 by
**0 rank changes across all three retrievers**. The default is therefore 5.

Caveat on that: the suite has 20 typo queries. They all happen to be
recoverable within a 5-character prefix. A typo distribution with errors
concentrated later in longer words could behave differently, so the
parameter is exposed rather than hard-coded.

Two consequences worth noting:

- **The English guard set is now the largest component** at 6.8 MiB, over
  10x the delete-index. If memory ever needs trimming, that list is the
  place to look, not SymSpell.
- **The 11.8 MiB of corpus chunks is build-time only.** A deployment would
  ship a precomputed vocabulary rather than re-derive it from the JSONL,
  removing that from the runtime footprint entirely.

### What this does and does not tell us about the target

Measured on **x86_64, 4 cores, CPython 3.11** — not on the target board.

Transfers reasonably: Cortex-A53 in the ARMv8-A/AArch64 configuration is
also 64-bit, so CPython's per-object and per-dict-entry overhead — which is
essentially all of this footprint, since these are Python dicts and sets —
should be within a few percent. The structures are pointer-heavy, and
pointer width is the thing that matters most.

Does **not** transfer, and must be checked on-device:

- **32-bit userland.** If the board runs armhf rather than AArch64, pointer
  size halves and these numbers drop substantially — the measurement would
  be conservative rather than wrong.
- **Page size.** AArch64 kernels may use 16 KiB or 64 KiB pages against
  x86_64's 4 KiB, which inflates RSS by rounding.
- **Allocator.** glibc vs musl differ in arena behaviour and in how
  aggressively freed memory is returned.
- **Contention.** This measures the corrector alone in a clean process. It
  says nothing about behaviour alongside the ~1.2 GB Qwen2.5-1.5B GGUF, the
  embedder, and the vector store competing for the same DDR4.

For scale: ~26 MiB of feature footprint against a claimed 4 GB PS DDR4 is
well under 1%, and ~2% of the generative model alone. That margin is wide
enough that the ordering of the caveats above is unlikely to change the
decision — but the 4 GB figure is itself listed as unverified in the
project's reference notes, so this remains a rough sizing rather than a
fit-check.
