# Score thresholding (rag-audit W2 / O1): calibrated, and rejected at this layer

**Outcome: not implemented, deliberately.** The calibration data says a
dense-distance threshold cannot do the job it was proposed for, and
production already implements the same guard at a layer where it works.

## What was proposed

Add a distance cutoff to retrieval: if the best chunk doesn't clear it,
return "not found in corpus" instead of k chunks regardless of quality.
Motivation was the measured 55% trap-variant rate — five false-premise
queries (Q2, Q3, Q5, Q13, Q20) returned 10 confident-looking chunks with no
corrective evidence.

## Calibration

Top-1 cosine distance captured for all 91 cases (spell correction applied,
same conditions as the headline eval).

| population | n | min | p25 | median | p75 | max |
|---|---|---|---|---|---|---|
| answerable, gold retrieved | 60 | 0.088 | 0.139 | **0.174** | 0.216 | 0.283 |
| answerable, gold missed | 20 | 0.127 | 0.143 | 0.208 | 0.243 | 0.308 |
| trap, gold retrieved | 6 | 0.156 | 0.174 | 0.195 | 0.245 | 0.276 |
| trap, gold NOT retrieved | 5 | 0.122 | 0.137 | **0.158** | 0.241 | 0.263 |

**The premise fails here.** The five trap failures are not low-confidence
matches — their median distance (0.158) is *lower* (better) than that of
correct answers (0.174). They are confident and wrong, which is precisely
the case a confidence threshold cannot catch.

Individually:

| | top-1 distance | query |
|---|---|---|
| Q3 | **0.1222** | What are the tenets of unified land operations? |
| Q2 | 0.1515 | What are the eight elements of combat power? |
| Q20 | 0.1584 | What does ADP 3-0 say about decisive action? |
| Q5 | 0.2194 | The principles of war aren't in Army doctrine, right? |
| Q13 | 0.2627 | Is IPOE the intelligence process? |

Q3 — a query about a concept the 2025 ADP 3-0 no longer uses — scores
*better* than 25% of the queries that are answered correctly.

## The tradeoff curve

Suppress when top-1 distance > T:

| T | traps caught | correct answers destroyed | cost |
|---|---|---|---|
| 0.10 | 5/5 | 59/60 (98%) | 11.8 good lost per trap |
| 0.12 | 5/5 | 54/60 (90%) | 10.8 |
| 0.14 | 4/5 | 45/60 (75%) | 11.2 |
| 0.16 | 2/5 | 34/60 (57%) | 17.0 |
| 0.18 | 2/5 | 27/60 (45%) | 13.5 |
| 0.20 | 2/5 | 19/60 (32%) | 9.5 |
| 0.22 | 1/5 | 14/60 (23%) | 14.0 |
| 0.24 | 1/5 | 10/60 (17%) | 10.0 |
| 0.26 | 1/5 | 4/60 (7%) | 4.0 |
| 0.28 | 0/5 | 1/60 (2%) | catches nothing |
| 0.30 | 0/5 | 0/60 (0%) | catches nothing |

There is no good operating point. Catching all five traps requires T <
0.122, which destroys **54 of 60 correct answers**. The distributions
overlap almost completely, so this is not a tuning problem — the signal
isn't there.

## Why production's design is already right

`hybrid_retrieval.py` + `app.py` on the HF Space (readable as of this
writing) already implement this guard, and place it correctly:

```python
top_score = chunks[0].get("retrieval_score", 0)
if top_score < 0.2:                      # FIX 1 / FIX 17
    yield "I don't have a reliable passage to answer this." + _suggest_pub(message)
    return
```

The crucial difference is *what is being thresholded*. That score is a
**cross-encoder relevance score** (`ms-marco-MiniLM-L-6-v2`) computed after
RRF merge — a supervised query-document relevance judgement, not a
bi-encoder distance. A cross-encoder sees the query and passage jointly and
can score "tenets of *unified land operations*" against a multidomain-
operations passage as irrelevant, which cosine similarity in bge space
cannot: to the bi-encoder those are near-synonymous phrasings.

Production layers three further guards this eval never exercised:

- `_chunk_answers_question()` — a second reranker pass for topic drift
- a low-confidence caveat at `top_score < 2.5`
- a pre-retrieval router that intercepts several trap classes *before*
  retrieval runs, including `_OBSOLETE_TERMS["unified land operations"]`,
  which is Q3's trap verbatim, and `_expected_count()` (FIX 27), which
  targets enumeration-count traps like Q2's "eight elements"

**Conclusion: no change recommended at the retrieval layer.** Adding a
dense-distance gate would degrade the system while duplicating, worse, a
guard that already exists downstream.

## What this says about the 55% trap number

It measures **raw retrieval only**, and should not be read as the rate at
which users see unguarded wrong answers. Retrieval is one layer of a
multi-layer system; at minimum Q3's trap is fully handled before retrieval
is even called. The end-to-end trap rate has never been measured and is
almost certainly better than 55%.

Measuring it properly requires running the suite through `app.py` on the
Space, not through this harness.
