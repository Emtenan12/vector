# Retrieval evaluation (top-k = 10)

Cases: 40  |  Scored: 40  |  Unresolved questions: 0

Axis scored: **Retrieval hit** only (gold paragraph anchor present in top-k). Faithfulness/Correctness are generation-side and out of scope here.

| retriever | hit rate | hits/n | MRR | median rank when hit |
|---|---|---|---|---|
| dense | 67.5% | 27/40 | 0.499 | 1 |
| sparse | 72.5% | 29/40 | 0.413 | 3 |
| fused | 82.5% | 33/40 | 0.489 | 2 |

## Hit rate by variant

| variant | dense | sparse | fused | n |
|---|---|---|---|---|
| primary | 62% (5/8) | 88% (7/8) | 75% (6/8) | 8 |
| paraphrase | 75% (6/8) | 75% (6/8) | 88% (7/8) | 8 |
| casual | 75% (6/8) | 62% (5/8) | 88% (7/8) | 8 |
| typo | 62% (5/8) | 75% (6/8) | 88% (7/8) | 8 |
| trap | 62% (5/8) | 62% (5/8) | 75% (6/8) | 8 |

## Hit rate vs k

| k | dense | sparse | fused |
|---|---|---|---|
| 1 | 40.0% | 32.5% | 35.0% |
| 3 | 57.5% | 42.5% | 52.5% |
| 5 | 62.5% | 55.0% | 67.5% |
| 10 | 67.5% | 72.5% | 82.5% |

## Per-case results

| Q | variant | dense | sparse | fused | query |
|---|---|---|---|---|---|
| 1 | primary | PASS (1) | PASS (1) | PASS (1) | What are the steps of the IPOE process? |
| 1 | paraphrase | FAIL | PASS (5) | PASS (9) | What four steps make up Intelligence Preparation of the Ope... |
| 1 | casual | PASS (1) | PASS (1) | PASS (1) | ipoe steps? |
| 1 | typo | PASS (1) | PASS (1) | PASS (1) | wat are the setps of the ipoe proccess |
| 1 | trap | PASS (1) | PASS (1) | PASS (1) | What are the six steps of the IPOE process? |
| 2 | primary | PASS (1) | PASS (6) | PASS (4) | What are the responsibilities of the corps G-1/AG and divis... |
| 2 | paraphrase | PASS (1) | PASS (4) | PASS (2) | What tasks does the casualty element at a corps or division... |
| 2 | casual | PASS (1) | FAIL | PASS (6) | what does the g1 casualty cell do at corps/div level |
| 2 | typo | PASS (1) | PASS (3) | PASS (1) | resposibilities of the corp g-1 casualty elemnt |
| 2 | trap | PASS (1) | PASS (5) | PASS (3) | List the seven responsibilities of the corps G-1/AG casualt... |
| 3 | primary | PASS (1) | PASS (1) | PASS (1) | What are the tasks of the EOD group S-3 section? |
| 3 | paraphrase | PASS (1) | PASS (3) | PASS (1) | What responsibilities does the S-3 section hold in an EOD g... |
| 3 | casual | PASS (2) | PASS (8) | PASS (1) | eod s3 tasks? |
| 3 | typo | PASS (2) | PASS (1) | PASS (1) | wut are the taks of the eod s-3 secton |
| 3 | trap | PASS (2) | PASS (1) | PASS (2) | The EOD S-3 section consists of seven cells and performs se... |
| 4 | primary | PASS (1) | PASS (1) | PASS (1) | What factors affect cargo-handling capacity in logistics-ov... |
| 4 | paraphrase | PASS (2) | FAIL | FAIL | Which considerations determine how much cargo can be handle... |
| 4 | casual | PASS (1) | PASS (8) | PASS (1) | lots cargo handling factors? |
| 4 | typo | PASS (1) | PASS (1) | PASS (1) | factors affceting cargo handlng capacity |
| 4 | trap | PASS (1) | PASS (1) | PASS (1) | What are the five factors affecting cargo-handling capacity? |
| 5 | primary | FAIL | FAIL | FAIL | What are the steps of risk management? |
| 5 | paraphrase | FAIL | FAIL | PASS (6) | What five-step process do commanders and staffs use to iden... |
| 5 | casual | FAIL | FAIL | FAIL | risk management steps? |
| 5 | typo | FAIL | FAIL | FAIL | wat are teh steps of rsk managment |
| 5 | trap | FAIL | FAIL | FAIL | What are the four steps of risk management? |
| 6 | primary | FAIL | PASS (9) | PASS (5) | What are the substeps of step 2 in the risk management proc... |
| 6 | paraphrase | PASS (3) | PASS (1) | PASS (2) | When applying the risk assessment matrix, what three subste... |
| 6 | casual | FAIL | PASS (2) | PASS (4) | risk assessment substeps step 2? |
| 6 | typo | FAIL | PASS (5) | PASS (2) | substeps of setp 2 risk managment |
| 6 | trap | FAIL | PASS (1) | PASS (2) | What are the two substeps planners apply in step 2 of risk ... |
| 7 | primary | FAIL | PASS (7) | FAIL | What are the tasks of the command and control warfighting f... |
| 7 | paraphrase | PASS (9) | PASS (3) | PASS (6) | Which four tasks make up the C2 warfighting function? |
| 7 | casual | PASS (6) | PASS (7) | PASS (7) | c2 warfighting function tasks? |
| 7 | typo | FAIL | PASS (7) | PASS (8) | taks of the c2 warfigthing functoin |
| 7 | trap | FAIL | FAIL | FAIL | What are the six tasks of the command and control warfighti... |
| 8 | primary | PASS (1) | PASS (5) | PASS (2) | What are the components of DODIN operations on a mission pa... |
| 8 | paraphrase | PASS (2) | PASS (1) | PASS (1) | Which three critical components make up the integrated cons... |
| 8 | casual | PASS (3) | FAIL | PASS (4) | dodin operations components? |
| 8 | typo | PASS (4) | FAIL | PASS (5) | componets of dodin operatons |
| 8 | trap | PASS (4) | FAIL | PASS (5) | What are the five components of DODIN operations? |