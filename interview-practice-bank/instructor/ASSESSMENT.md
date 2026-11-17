# Instructor assessment and interview preparation

Question IDs,core contracts and extensions come from `bank.json`. Use the same records for teaching and interview tests. Do not maintain an independently edited test question copy. An exported manifest records question IDs and the exact bank hash.

## Before administering a test

Select questions matching the candidate's taught track and runtime. Read the entire core and extension; advanced extensions may require techniques introduced in other subtopics. Run the selected exercise yourself in the intended environment and record independent expected outputs,including boundaries. The bank contains questions and acceptance examples; it does **not** contain complete validated solutions for every new extension.

`legacy_core_references.json` contains pre-existing SQL reference answers only for the mapped core. Those answers do not solve the additional interview requirement and are not newly runtime-verified here. Some replacement logical cores intentionally have no legacy reference. Keep this directory and generator source out of student distributions. Native fixture setup includes schema answers; do not provide solved setup for a CREATE/INSERT assessment.

Do not treat a structural count check or a candidate's own tests as proof of correctness. For each selected question prepare one ordinary case,one boundary/empty case,one failure case and one counterexample to a plausible shortcut. Compare complete values,multiplicities and required ordering. For open design tasks,write explicit pass/fail evidence before grading candidates.

## Suggested scoring: 100 points per question

| Criterion | Points | Evidence |
|---|---:|---|
| Core correctness | 30 | Correct complete outputs and invariants |
| Extension correctness | 25 | Solves the additional requirement,not just the core |
| Boundaries and failure handling | 20 | Independently checked cases; no lost/duplicated effects |
| Appropriate algorithm/design | 10 | Complexity/capacity argument supported by code or observations |
| Explanation and debugging | 10 | Explains a counterexample and repairs a defect |
| Readability and contract discipline | 5 | Clear interfaces,types,ordering and safe diagnostics |

A missing core or missing extension cannot pass regardless of points elsewhere. A critical tenant leak,corrupted state,double charge or incorrect data total blocks readiness until repaired and independently retested. Accept equivalent implementations with the same contract; do not require reference SQL text.

## Mock formats

| Level | Suggested test | Coding time | Discussion |
|---|---|---:|---:|
| Beginner | 3 different subtopics | 45 minutes | 10 minutes |
| Intermediate | 3 different subtopics | 90 minutes | 15 minutes |
| Advanced | 2 different subtopics | 90 minutes | 20 minutes |
| Mixed interview | 1 B + 1 I + 1 A,distinct subtopics | 90 minutes | 15 minutes |

These are local assessment formats,not claims about employer interview lengths. Reduce question count for a shorter interview. Run setup before the timer. Use exported IDs to attach scores and evidence; calculate a test score as the mean question score after checking mandatory gates.

`tools.py mock` selects distinct subtopics deterministically. Its `--exclude` option excludes exact previously seen question IDs,not all related variants. Because the bank is public practice material,an instructor should verify transfer of reasoning with an independently checked input or follow-up rather than assuming a familiar answer proves readiness.

Recommended readiness evidence: at least12/15 independently correct at each level of each assigned subtopic,at least8 timed correct,and two distinct mixed-topic mocks >=80/100. Assign another attempt to each weak subtopic. Cloud learners also complete a native service lab; full stack learners demonstrate working frontend/backend integration.
