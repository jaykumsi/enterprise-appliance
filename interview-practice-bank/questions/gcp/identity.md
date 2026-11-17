# GCP Data Engineering: Identity

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Service accounts and impersonation

### Beginner

#### GCP-IDENTITY-01-B01

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B02

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B03

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B04

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B05

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B06

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B07

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B08

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B09

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B10

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B11

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B12

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B13

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B14

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-01-B15

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-IDENTITY-01-I01

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I02

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I03

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I04

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I05

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I06

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I07

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I08

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I09

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I10

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I11

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I12

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I13

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I14

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-01-I15

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-IDENTITY-01-A01

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A02

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A03

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A04

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A05

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A06

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A07

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A08

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A09

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A10

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A11

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A12

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A13

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A14

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-01-A15

**Core:** Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / fixture:** Caller a lacking grant on b -> denied even if a has a similarly named account.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## IAM project and dataset scopes

### Beginner

#### GCP-IDENTITY-02-B01

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B02

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B03

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B04

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B05

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B06

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B07

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B08

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B09

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B10

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B11

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B12

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B13

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B14

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-IDENTITY-02-B15

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-IDENTITY-02-I01

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I02

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I03

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I04

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I05

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I06

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I07

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I08

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I09

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I10

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I11

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I12

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I13

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I14

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-IDENTITY-02-I15

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-IDENTITY-02-A01

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A02

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A03

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A04

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A05

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A06

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A07

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A08

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A09

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A10

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A11

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A12

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A13

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A14

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-IDENTITY-02-A15

**Core:** Compute exact allowed actions inherited from ancestor slash-segment scopes. A query requires both project run_job and dataset read. This is a simplified local model with no conditions/deny policies.

**Acceptance example / fixture:** Dataset read without project run_job -> query denied.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
