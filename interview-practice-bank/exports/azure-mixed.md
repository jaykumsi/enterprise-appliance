# Azure Data Engineering mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## AZ-OPERATIONS-03-B08 — Infrastructure plan validation

Azure Data Engineering / Operations / Beginner

Runtime: Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime. Suggested time: 15 minutes.

**Core problem**

Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / baseline**

prod with public_access=true -> error public_access.

**Interview requirement**

Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## AZ-IDENTITY-03-I06 — Key Vault secret versions

Azure Data Engineering / Identity / Intermediate

Runtime: Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime. Suggested time: 30 minutes.

**Core problem**

Implement secret-reference resolution by name and optional version. Version pinned reads that enabled version; unpinned reads latest enabled by integer creation sequence. Unknown or disabled reference returns NOT_FOUND. Return version IDs,never secret text.

**Acceptance example / baseline**

v1 enabled,v2 disabled -> unpinned v1.

**Interview requirement**

Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## AZ-INGESTION-01-A03 — Data Factory copy and reconciliation

Azure Data Engineering / Ingestion / Advanced

Runtime: Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime. Suggested time: 45 minutes.

**Core problem**

Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / baseline**

Same row count with different IDs -> fail reconciliation.

**Interview requirement**

Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
