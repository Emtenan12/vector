# Retrieval evaluation (top-k = 10)

Cases: 91  |  Scored: 91  |  Unresolved questions: 0

Axis scored: **Retrieval hit** only (gold paragraph anchor present in top-k). Faithfulness/Correctness are generation-side and out of scope here.

| retriever | hit rate | hits/n | MRR | median rank when hit |
|---|---|---|---|---|
| dense | 72.5% | 66/91 | 0.530 | 1.0 |
| sparse | 81.3% | 74/91 | 0.471 | 2.0 |
| fused | 84.6% | 77/91 | 0.602 | 1 |

## Hit rate by variant

| variant | dense | sparse | fused | n |
|---|---|---|---|---|
| primary | 80% (16/20) | 85% (17/20) | 95% (19/20) | 20 |
| paraphrase | 65% (13/20) | 95% (19/20) | 85% (17/20) | 20 |
| casual | 75% (15/20) | 80% (16/20) | 85% (17/20) | 20 |
| typo | 80% (16/20) | 80% (16/20) | 90% (18/20) | 20 |
| trap | 55% (6/11) | 55% (6/11) | 55% (6/11) | 11 |

## Hit rate vs k

| k | dense | sparse | fused |
|---|---|---|---|
| 1 | 44.0% | 29.7% | 45.1% |
| 3 | 59.3% | 58.2% | 73.6% |
| 5 | 63.7% | 71.4% | 82.4% |
| 10 | 72.5% | 81.3% | 84.6% |

## Per-case results

| Q | variant | dense | sparse | fused | query |
|---|---|---|---|---|---|
| 1 | primary | PASS (1) | PASS (2) | PASS (1) | What are the warfighting functions? |
| 1 | paraphrase | PASS (7) | PASS (6) | PASS (4) | Name the functions that generate combat power. |
| 1 | casual | PASS (1) | PASS (2) | PASS (1) | what r the warfighting functions |
| 1 | typo | PASS (4) | PASS (2) | PASS (2) | list the warfigthing funtions |
| 1 | trap | PASS (1) | PASS (2) | PASS (1) | What are the seven warfighting functions? |
| 2 | primary | FAIL | PASS (2) | PASS (2) | What are the dynamics of combat power? |
| 2 | paraphrase | FAIL | PASS (2) | PASS (3) | Which five variables determine the force of a formation's b... |
| 2 | casual | FAIL | PASS (2) | PASS (3) | combat power dynamics — whats the list |
| 2 | typo | FAIL | PASS (2) | PASS (2) | what are the dynmaics of combat pwoer |
| 2 | trap | FAIL | FAIL | FAIL | What are the eight elements of combat power? |
| 3 | primary | PASS (8) | PASS (4) | PASS (3) | What are the tenets of multidomain operations? |
| 3 | paraphrase | FAIL | PASS (5) | PASS (5) | Which desirable attributes should be incorporated into all ... |
| 3 | casual | FAIL | PASS (8) | PASS (5) | MDO tenets? |
| 3 | typo | PASS (7) | PASS (4) | PASS (3) | tenets of multidoman operations |
| 3 | trap | FAIL | FAIL | FAIL | What are the tenets of unified land operations? |
| 4 | primary | PASS (2) | PASS (5) | PASS (3) | What are the levels of warfare? |
| 4 | paraphrase | PASS (1) | PASS (1) | PASS (1) | How does the Army organize its activities across levels of ... |
| 4 | casual | PASS (1) | PASS (7) | PASS (3) | levels of warfare... how many n what are they |
| 4 | typo | PASS (1) | PASS (5) | PASS (2) | list the lvels of warfare |
| 4 | trap | PASS (3) | PASS (6) | PASS (4) | What are the three levels of warfare? |
| 5 | primary | FAIL | PASS (3) | PASS (4) | What are the principles of joint operations? |
| 5 | paraphrase | FAIL | PASS (3) | FAIL | List the nine principles of war and the three additional jo... |
| 5 | casual | FAIL | PASS (4) | FAIL | principles of war — gimme the list |
| 5 | typo | FAIL | PASS (4) | FAIL | list the principels of war |
| 5 | trap | FAIL | FAIL | FAIL | The principles of war aren't in Army doctrine, right? |
| 6 | primary | FAIL | FAIL | FAIL | What is mission command? |
| 6 | paraphrase | PASS (1) | PASS (4) | PASS (1) | How does Army doctrine define the Army's approach to comman... |
| 6 | casual | FAIL | FAIL | FAIL | define mission command real quick |
| 6 | typo | FAIL | FAIL | FAIL | what is missoin comand |
| 7 | primary | PASS (1) | PASS (6) | PASS (2) | What are the principles of mission command? |
| 7 | paraphrase | PASS (1) | PASS (5) | PASS (2) | Which seven principles enable successful mission command? |
| 7 | casual | PASS (1) | PASS (6) | PASS (2) | mission command principles pls |
| 7 | typo | PASS (1) | PASS (6) | PASS (2) | principls of mision command |
| 7 | trap | PASS (1) | PASS (3) | PASS (1) | Are trust and initiative the only two principles of mission... |
| 8 | primary | PASS (1) | PASS (2) | PASS (1) | What is the commander's intent? |
| 8 | paraphrase | FAIL | PASS (5) | FAIL | What element of planning lets subordinates act to achieve d... |
| 8 | casual | PASS (3) | PASS (2) | PASS (1) | commanders intent — define it |
| 8 | typo | PASS (2) | PASS (2) | PASS (1) | whats the commanders intnet |
| 9 | primary | PASS (1) | PASS (4) | PASS (1) | What is mutual trust? |
| 9 | paraphrase | FAIL | PASS (3) | PASS (3) | How does ADP 6-0 define the shared confidence between comma... |
| 9 | casual | PASS (1) | PASS (3) | PASS (1) | define mutual trust (army doctrine) |
| 9 | typo | PASS (2) | PASS (3) | PASS (2) | what is mutal trust in mission comand |
| 10 | primary | PASS (1) | PASS (1) | PASS (1) | What are the seven steps of the military decision-making pr... |
| 10 | paraphrase | PASS (1) | PASS (1) | PASS (1) | Walk me through the steps a staff uses to develop a plan un... |
| 10 | casual | PASS (1) | PASS (1) | PASS (1) | mdmp steps? |
| 10 | typo | PASS (1) | PASS (7) | PASS (2) | what are teh steps of the MDPM |
| 10 | trap | PASS (1) | PASS (1) | PASS (1) | What are the ten steps of MDMP? |
| 11 | primary | PASS (1) | PASS (1) | PASS (1) | What are the eight steps of troop leading procedures (TLP)? |
| 11 | paraphrase | PASS (5) | PASS (2) | PASS (2) | How do small-unit leaders without a staff plan and prepare ... |
| 11 | casual | PASS (1) | PASS (1) | PASS (1) | TLP steps plz |
| 11 | typo | PASS (3) | PASS (3) | PASS (2) | steps of troop leadng procedures |
| 12 | primary | FAIL | FAIL | PASS (2) | What is the operations process? |
| 12 | paraphrase | FAIL | FAIL | FAIL | What are the major command and control activities performed... |
| 12 | casual | FAIL | FAIL | PASS (3) | ops process — what is it |
| 12 | typo | FAIL | FAIL | PASS (2) | what is the operatoins process |
| 13 | primary | PASS (2) | FAIL | PASS (5) | What are the steps of the Army intelligence process? |
| 13 | paraphrase | PASS (6) | PASS (4) | PASS (1) | Which steps and continuing activities make up the intellige... |
| 13 | casual | PASS (5) | FAIL | FAIL | intel process steps |
| 13 | typo | PASS (7) | FAIL | PASS (7) | steps of the inteligence proccess |
| 13 | trap | FAIL | FAIL | FAIL | Is IPOE the intelligence process? |
| 14 | primary | PASS (1) | PASS (1) | PASS (1) | What are the elements of sustainment? |
| 14 | paraphrase | PASS (1) | PASS (1) | PASS (1) | Which four elements make up the sustainment warfighting fun... |
| 14 | casual | PASS (2) | FAIL | PASS (4) | sustainment WFF — what does it consist of |
| 14 | typo | PASS (3) | PASS (1) | PASS (1) | elements of sustianment |
| 14 | trap | PASS (3) | PASS (3) | PASS (1) | The sustainment function is just logistics, right? |
| 15 | primary | PASS (1) | PASS (1) | PASS (1) | What are the principles of sustainment? |
| 15 | paraphrase | PASS (1) | PASS (1) | PASS (1) | List the principles that are essential to maintaining comba... |
| 15 | casual | PASS (1) | PASS (1) | PASS (1) | sustainment principles? |
| 15 | typo | PASS (1) | PASS (1) | PASS (1) | principles of sustainmnet |
| 16 | primary | PASS (1) | PASS (2) | PASS (1) | What are the characteristics of the defense? |
| 16 | paraphrase | PASS (1) | PASS (1) | PASS (1) | Which characteristics do defending commanders use to regain... |
| 16 | casual | PASS (1) | PASS (2) | PASS (1) | defense characteristics — list em |
| 16 | typo | PASS (1) | FAIL | PASS (4) | charactristics of the defence |
| 16 | trap | PASS (1) | PASS (6) | PASS (2) | What are the five characteristics of the defense? |
| 17 | primary | PASS (1) | PASS (2) | PASS (1) | What are the three types of defensive operations? |
| 17 | paraphrase | PASS (1) | PASS (1) | PASS (1) | Which defensive operation focuses on terrain, which on enem... |
| 17 | casual | PASS (1) | PASS (2) | PASS (1) | types of defensive ops? |
| 17 | typo | PASS (1) | PASS (2) | PASS (1) | 3 types of defensve operations |
| 18 | primary | PASS (2) | PASS (1) | PASS (1) | What are the five forms of maneuver? |
| 18 | paraphrase | FAIL | PASS (2) | PASS (10) | Which distinct tactical combinations of fire and movement d... |
| 18 | casual | PASS (1) | PASS (1) | PASS (1) | forms of maneuver — how many and what |
| 18 | typo | PASS (2) | PASS (1) | PASS (1) | five froms of manuever |
| 19 | primary | PASS (2) | PASS (1) | PASS (1) | What is a mobile defense, and what is the striking force? |
| 19 | paraphrase | PASS (1) | PASS (1) | PASS (1) | In which defensive operation does a striking force deliver ... |
| 19 | casual | PASS (1) | PASS (1) | PASS (1) | explain mobile defense + striking force |
| 19 | typo | PASS (2) | PASS (1) | PASS (1) | what is a moblie defense |
| 20 | primary | PASS (6) | PASS (1) | PASS (2) | Which publication and paragraph list the four elements of d... |
| 20 | paraphrase | PASS (6) | PASS (1) | PASS (2) | Where in the corpus is decisive action broken into its elem... |
| 20 | casual | PASS (4) | PASS (1) | PASS (1) | decisive action elements — which doc says it |
| 20 | typo | PASS (7) | PASS (1) | PASS (2) | four elemnts of decisive action + source |
| 20 | trap | FAIL | FAIL | FAIL | What does ADP 3-0 say about decisive action? |