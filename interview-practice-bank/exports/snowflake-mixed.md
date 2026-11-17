# Snowflake mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## SNOW-PERFORMANCE-02-B06 — Query profile diagnosis

Snowflake / Performance / Beginner

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models. Suggested time: 15 minutes.

**Core problem**

Given measured stages scan:8s,join:40s,aggregate:2s and counts scan1M,join20M, diagnose row multiplication from a nonunique dimension key. Provide deduplicating SQL,assertion queries and a comparison plan before choosing a larger warehouse.

**Acceptance example / baseline**

Deduplicated dimension must have one row per key; joined fact count should return to1M for one-to-one enrichment.

**Interview requirement**

Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## SNOW-PERFORMANCE-01-I08 — Micro partition pruning

Snowflake / Performance / Intermediate

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models. Suggested time: 30 minutes.

**Core problem**

Given partition metadata id,min_cents,max_cents with p1:[0,99],p2:[100,200],p3:unknown, select candidates for cents>=150. Unknown statistics require inclusion. Write SQL against the metadata and return IDs sorted.

**Acceptance example / baseline**

Candidates [p2,p3].

**Interview requirement**

Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## SNOW-SECURITY-03-A06 — Masking and row access logic

Snowflake / Security / Advanced

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models. Suggested time: 45 minutes.

**Core problem**

Implement displaySalary(actor,row). Unauthenticated or wrong tenant -> HIDDEN_ROW; authenticated payroll for same tenant -> integer salary; other same-tenant role -> MASKED. Do not return raw salary in error/debug fields.

**Acceptance example / baseline**

Same tenant analyst -> MASKED; other tenant payroll -> HIDDEN_ROW.

**Interview requirement**

Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
