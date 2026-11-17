# AWS Data Engineering: Networking

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## VPC routing

### Beginner

#### AWS-NETWORKING-01-B01

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B02

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B03

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B04

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B05

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B06

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B07

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B08

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B09

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B10

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B11

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B12

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B13

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B14

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-NETWORKING-01-B15

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-NETWORKING-01-I01

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I02

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I03

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I04

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I05

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I06

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I07

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I08

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I09

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I10

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I11

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I12

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I13

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I14

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-NETWORKING-01-I15

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-NETWORKING-01-A01

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A02

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A03

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A04

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A05

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A06

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A07

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A08

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A09

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A10

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A11

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A12

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A13

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A14

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-NETWORKING-01-A15

**Core:** Implement longest-prefix IPv4 route selection from supplied CIDRs. Ignore disabled routes; tie on equal prefix length uses lowest numeric priority then route ID. No route -> UNREACHABLE. Return selected target.

**Acceptance example / fixture:** 10.0.1.5 with /16->A and /24->B -> B.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
