# PostgreSQL: Security

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Roles and row level security

### Beginner

#### PG-SECURITY-01-B01

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B02

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B03

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B04

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B05

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B06

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B07

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B08

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B09

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B10

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B11

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B12

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B13

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B14

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-SECURITY-01-B15

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-SECURITY-01-I01

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I02

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I03

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I04

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I05

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I06

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I07

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I08

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I09

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I10

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I11

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I12

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I13

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I14

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-SECURITY-01-I15

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-SECURITY-01-A01

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A02

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A03

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A04

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A05

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A06

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A07

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A08

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A09

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A10

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A11

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A12

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A13

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A14

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-SECURITY-01-A15

**Core:** For a local model, implement tenant_visible(row_tenant,session_tenant,is_admin). Empty session tenant denies; admin bypass is permitted only for an authenticated session. Then write PostgreSQL RLS policy SQL expressing the same user-facing rule and demonstrate two tenants cannot read each other.

**Acceptance example / fixture:** Authenticated tenant t1 sees t1, not t2; unauthenticated admin flag cannot grant access.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
