# AWS Data Engineering mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## AWS-IDENTITY-02-B12 — IAM roles

AWS Data Engineering / Identity / Beginner

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect. Suggested time: 15 minutes.

**Core problem**

Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / baseline**

Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Interview requirement**

Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## AWS-COMPUTE-01-I05 — EC2 capacity planning

AWS Data Engineering / Compute / Intermediate

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect. Suggested time: 30 minutes.

**Core problem**

Given jobs with integer CPU units and instance capacity 4, assign jobs in input order using first-fit bins; reject a job larger than capacity. Return instance assignments and unused units. This is a deterministic bin-packing model, not a claim of optimality.

**Acceptance example / baseline**

Jobs [3,2,1] -> instance1 [3,1], instance2 [2].

**Interview requirement**

Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## AWS-FOUNDATIONS-01-A13 — Cloud versus on premises

AWS Data Engineering / Foundations / Advanced

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect. Suggested time: 45 minutes.

**Core problem**

Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / baseline**

Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Interview requirement**

Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
