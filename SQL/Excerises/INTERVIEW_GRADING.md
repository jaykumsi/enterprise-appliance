# SQL interview grading

Use canonical IDs from the student topic books. `domain_interview_questions.jsonl` at the curriculum root is the export source,including private references. Never distribute that file or this solutions folder.

Query questions have two result sets. Grade the analysis audit first,then compare the complete report against the independent expected artifact. Never accept only matching row counts or grand totals. The generated preview displays at most five expected rows;the complete expected rows are in DOMAIN_INTERVIEW_EXPECTED.json and native execution evidence is in DOMAIN_INTERVIEW_NATIVE_VALIDATION.json.

Respect the numeric contract:counts,IDs and exact totals must agree;means,medians,percentages and weighted prices allow absolute difference0.000003. The Python oracle's mathematical expected values may contain more fractional digits than the SQL reference's displayed decimals. Do not compare serialized numeric strings as text.

Practical labs use the core SQL/model reference plus a case-specific rubric. These are open native/design demonstrations,not fully enumerated automated solutions. Require concrete inputs,before/after state,precise rejection/acceptance and assertions. Review the chosen case before administering it. A copied core without the new case cannot pass.

| Criterion | Points |
|---|---:|
| Analysis/core contract and business report/case correctness |45|
| Adversarial cases and complete result comparison |25|
| Algorithm,query grain and scaling argument |15|
| Explanation and debugging |10|
| Clear SQL and exact output contract |5|

A wrong monetary total,split cutoff tie,phantom activity row,wrong time boundary,unbounded cycle,tenant/scope leak or lost/duplicated accepted effect blocks a pass until corrected. Accept equivalent SQL;do not require the reference method.

Advanced patterns deliberately recur under different subtopic transformations and domains. Select different patterns for a mixed mock;repeating a memorized pattern with a renamed column is not independent readiness evidence. Include a new independently calculated adversarial fixture and require the candidate to repair one plausible wrong shortcut.

Native validation covers the runnable query references and explicit adversarial populations recorded in the report. It does not mean all open-ended lab extensions have been independently executed or every possible submitted solution is automatically graded.

[Instructor index](solutions/README.md)

[Preserved setup and capstone notes](CONSOLIDATED_INSTRUCTOR_NOTES.md)
