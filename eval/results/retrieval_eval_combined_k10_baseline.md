# Retrieval evaluation (top-k = 10)

Cases: 91  |  Scored: 91  |  Unresolved questions: 0

Axis scored: **Retrieval hit** only (gold paragraph anchor present in top-k). Faithfulness/Correctness are generation-side and out of scope here.

| retriever | hit rate | hits/n | MRR | median rank when hit |
|---|---|---|---|---|
| dense | 50.5% | 46/91 | 0.313 | 2.0 |
| sparse | 48.4% | 44/91 | 0.184 | 4.0 |
| fused | 62.6% | 57/91 | 0.309 | 3 |

## Hit rate by variant

| variant | dense | sparse | fused | n |
|---|---|---|---|---|
| primary | 65% (13/20) | 65% (13/20) | 85% (17/20) | 20 |
| paraphrase | 40% (8/20) | 70% (14/20) | 75% (15/20) | 20 |
| casual | 65% (13/20) | 50% (10/20) | 70% (14/20) | 20 |
| typo | 30% (6/20) | 15% (3/20) | 25% (5/20) | 20 |
| trap | 55% (6/11) | 36% (4/11) | 55% (6/11) | 11 |

## Hit rate vs k

| k | dense | sparse | fused |
|---|---|---|---|
| 1 | 23.1% | 8.8% | 18.7% |
| 3 | 36.3% | 20.9% | 35.2% |
| 5 | 44.0% | 29.7% | 48.4% |
| 10 | 50.5% | 48.4% | 62.6% |

## Per-case results

| Q | variant | dense | sparse | fused | query |
|---|---|---|---|---|---|
| 1 | primary | PASS (1) | PASS (5) | PASS (1) | What are the warfighting functions? |
| 1 | paraphrase | FAIL | FAIL | PASS (6) | Name the functions that generate combat power. |
| 1 | casual | PASS (1) | PASS (5) | PASS (1) | what r the warfighting functions |
| 1 | typo | FAIL | FAIL | FAIL | list the warfigthing funtions |
| 1 | trap | PASS (1) | PASS (8) | PASS (1) | What are the seven warfighting functions? |
| 2 | primary | FAIL | PASS (6) | PASS (6) | What are the dynamics of combat power? |
| 2 | paraphrase | FAIL | PASS (3) | FAIL | Which five variables determine the force of a formation's b... |
| 2 | casual | FAIL | PASS (6) | FAIL | combat power dynamics — whats the list |
| 2 | typo | FAIL | FAIL | FAIL | what are the dynmaics of combat pwoer |
| 2 | trap | FAIL | FAIL | FAIL | What are the eight elements of combat power? |
| 3 | primary | FAIL | PASS (4) | PASS (3) | What are the tenets of multidomain operations? |
| 3 | paraphrase | FAIL | PASS (7) | PASS (7) | Which desirable attributes should be incorporated into all ... |
| 3 | casual | FAIL | FAIL | FAIL | MDO tenets? |
| 3 | typo | PASS (3) | FAIL | PASS (6) | tenets of multidoman operations |
| 3 | trap | FAIL | FAIL | FAIL | What are the tenets of unified land operations? |
| 4 | primary | PASS (2) | FAIL | PASS (4) | What are the levels of warfare? |
| 4 | paraphrase | PASS (1) | PASS (1) | PASS (1) | How does the Army organize its activities across levels of ... |
| 4 | casual | PASS (1) | FAIL | PASS (4) | levels of warfare... how many n what are they |
| 4 | typo | PASS (7) | FAIL | PASS (1) | list the lvels of warfare |
| 4 | trap | PASS (3) | FAIL | PASS (5) | What are the three levels of warfare? |
| 5 | primary | FAIL | PASS (4) | PASS (6) | What are the principles of joint operations? |
| 5 | paraphrase | FAIL | PASS (3) | FAIL | List the nine principles of war and the three additional jo... |
| 5 | casual | FAIL | FAIL | FAIL | principles of war — gimme the list |
| 5 | typo | FAIL | FAIL | FAIL | list the principels of war |
| 5 | trap | FAIL | FAIL | FAIL | The principles of war aren't in Army doctrine, right? |
| 6 | primary | FAIL | FAIL | FAIL | What is mission command? |
| 6 | paraphrase | PASS (1) | PASS (8) | PASS (1) | How does Army doctrine define the Army's approach to comman... |
| 6 | casual | FAIL | FAIL | FAIL | define mission command real quick |
| 6 | typo | FAIL | FAIL | FAIL | what is missoin comand |
| 7 | primary | PASS (1) | FAIL | PASS (6) | What are the principles of mission command? |
| 7 | paraphrase | PASS (1) | FAIL | PASS (4) | Which seven principles enable successful mission command? |
| 7 | casual | PASS (1) | FAIL | PASS (8) | mission command principles pls |
| 7 | typo | FAIL | FAIL | FAIL | principls of mision command |
| 7 | trap | PASS (2) | PASS (9) | PASS (2) | Are trust and initiative the only two principles of mission... |
| 8 | primary | PASS (2) | PASS (6) | PASS (3) | What is the commander's intent? |
| 8 | paraphrase | FAIL | FAIL | FAIL | What element of planning lets subordinates act to achieve d... |
| 8 | casual | PASS (5) | PASS (6) | PASS (3) | commanders intent — define it |
| 8 | typo | FAIL | FAIL | FAIL | whats the commanders intnet |
| 9 | primary | PASS (1) | PASS (8) | PASS (3) | What is mutual trust? |
| 9 | paraphrase | FAIL | PASS (3) | PASS (2) | How does ADP 6-0 define the shared confidence between comma... |
| 9 | casual | PASS (1) | PASS (5) | PASS (2) | define mutual trust (army doctrine) |
| 9 | typo | PASS (4) | PASS (2) | PASS (2) | what is mutal trust in mission comand |
| 10 | primary | PASS (3) | PASS (6) | PASS (4) | What are the seven steps of the military decision-making pr... |
| 10 | paraphrase | FAIL | PASS (6) | PASS (4) | Walk me through the steps a staff uses to develop a plan un... |
| 10 | casual | PASS (9) | PASS (8) | PASS (4) | mdmp steps? |
| 10 | typo | PASS (7) | FAIL | FAIL | what are teh steps of the MDPM |
| 10 | trap | PASS (5) | PASS (8) | PASS (2) | What are the ten steps of MDMP? |
| 11 | primary | FAIL | FAIL | FAIL | What are the eight steps of troop leading procedures (TLP)? |
| 11 | paraphrase | FAIL | FAIL | PASS (7) | How do small-unit leaders without a staff plan and prepare ... |
| 11 | casual | FAIL | PASS (3) | PASS (8) | TLP steps plz |
| 11 | typo | FAIL | FAIL | FAIL | steps of troop leadng procedures |
| 12 | primary | FAIL | FAIL | FAIL | What is the operations process? |
| 12 | paraphrase | FAIL | FAIL | FAIL | What are the major command and control activities performed... |
| 12 | casual | FAIL | FAIL | FAIL | ops process — what is it |
| 12 | typo | FAIL | FAIL | FAIL | what is the operatoins process |
| 13 | primary | PASS (3) | FAIL | PASS (5) | What are the steps of the Army intelligence process? |
| 13 | paraphrase | FAIL | PASS (10) | PASS (6) | Which steps and continuing activities make up the intellige... |
| 13 | casual | PASS (9) | FAIL | FAIL | intel process steps |
| 13 | typo | FAIL | FAIL | FAIL | steps of the inteligence proccess |
| 13 | trap | FAIL | FAIL | FAIL | Is IPOE the intelligence process? |
| 14 | primary | PASS (1) | PASS (3) | PASS (1) | What are the elements of sustainment? |
| 14 | paraphrase | PASS (1) | PASS (2) | PASS (1) | Which four elements make up the sustainment warfighting fun... |
| 14 | casual | PASS (3) | FAIL | PASS (7) | sustainment WFF — what does it consist of |
| 14 | typo | FAIL | FAIL | FAIL | elements of sustianment |
| 14 | trap | PASS (5) | PASS (6) | PASS (3) | The sustainment function is just logistics, right? |
| 15 | primary | PASS (1) | PASS (1) | PASS (1) | What are the principles of sustainment? |
| 15 | paraphrase | PASS (1) | PASS (1) | PASS (1) | List the principles that are essential to maintaining comba... |
| 15 | casual | PASS (1) | PASS (1) | PASS (1) | sustainment principles? |
| 15 | typo | PASS (1) | PASS (2) | PASS (1) | principles of sustainmnet |
| 16 | primary | PASS (2) | FAIL | PASS (3) | What are the characteristics of the defense? |
| 16 | paraphrase | PASS (1) | PASS (1) | PASS (1) | Which characteristics do defending commanders use to regain... |
| 16 | casual | PASS (6) | FAIL | PASS (6) | defense characteristics — list em |
| 16 | typo | FAIL | FAIL | FAIL | charactristics of the defence |
| 16 | trap | PASS (2) | FAIL | PASS (5) | What are the five characteristics of the defense? |
| 17 | primary | PASS (2) | PASS (9) | PASS (4) | What are the three types of defensive operations? |
| 17 | paraphrase | PASS (1) | PASS (1) | PASS (1) | Which defensive operation focuses on terrain, which on enem... |
| 17 | casual | PASS (1) | FAIL | PASS (4) | types of defensive ops? |
| 17 | typo | PASS (5) | FAIL | PASS (10) | 3 types of defensve operations |
| 18 | primary | PASS (6) | PASS (4) | PASS (5) | What are the five forms of maneuver? |
| 18 | paraphrase | FAIL | FAIL | FAIL | Which distinct tactical combinations of fire and movement d... |
| 18 | casual | PASS (5) | PASS (2) | PASS (1) | forms of maneuver — how many and what |
| 18 | typo | FAIL | FAIL | FAIL | five froms of manuever |
| 19 | primary | PASS (4) | PASS (4) | PASS (1) | What is a mobile defense, and what is the striking force? |
| 19 | paraphrase | PASS (1) | PASS (9) | PASS (2) | In which defensive operation does a striking force deliver ... |
| 19 | casual | PASS (2) | PASS (4) | PASS (1) | explain mobile defense + striking force |
| 19 | typo | FAIL | FAIL | FAIL | what is a moblie defense |
| 20 | primary | FAIL | PASS (1) | PASS (2) | Which publication and paragraph list the four elements of d... |
| 20 | paraphrase | FAIL | PASS (3) | PASS (3) | Where in the corpus is decisive action broken into its elem... |
| 20 | casual | FAIL | PASS (1) | PASS (2) | decisive action elements — which doc says it |
| 20 | typo | FAIL | PASS (2) | FAIL | four elemnts of decisive action + source |
| 20 | trap | FAIL | FAIL | FAIL | What does ADP 3-0 say about decisive action? |