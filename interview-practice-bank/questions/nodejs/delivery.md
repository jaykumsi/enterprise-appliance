# Full Stack Developer - NodeJs: Delivery

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Environment configuration

### Beginner

#### NODE-DELIVERY-01-B01

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B02

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B03

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B04

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B05

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B06

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B07

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B08

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B09

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B10

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B11

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B12

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B13

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B14

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-01-B15

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-DELIVERY-01-I01

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I02

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I03

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I04

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I05

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I06

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I07

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I08

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I09

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I10

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I11

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I12

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I13

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I14

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-01-I15

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-DELIVERY-01-A01

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A02

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A03

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A04

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A05

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A06

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A07

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A08

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A09

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A10

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A11

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A12

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A13

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A14

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-01-A15

**Core:** Implement validateConfig(env) requiring PORT integer 1..65535, DATABASE_URL nonempty and LOG_LEVEL INFO,WARN,ERROR. Return all field errors sorted by name; redact secret values.

**Acceptance example / fixture:** PORT=0,DATABASE_URL empty,LOG_LEVEL=DEBUG -> three named errors.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Health checks and graceful shutdown

### Beginner

#### NODE-DELIVERY-02-B01

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B02

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B03

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B04

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B05

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B06

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B07

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B08

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B09

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B10

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B11

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B12

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B13

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B14

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-DELIVERY-02-B15

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-DELIVERY-02-I01

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I02

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I03

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I04

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I05

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I06

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I07

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I08

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I09

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I10

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I11

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I12

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I13

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I14

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-DELIVERY-02-I15

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-DELIVERY-02-A01

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A02

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A03

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A04

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A05

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A06

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A07

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A08

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A09

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A10

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A11

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A12

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A13

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A14

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-DELIVERY-02-A15

**Core:** Implement a lifecycle controller STARTING->READY->DRAINING->STOPPED. Readiness is true only in READY. On shutdown stop accepting work, wait for in-flight requests until injected deadline, then cancel remaining work and close resources exactly once.

**Acceptance example / fixture:** Shutdown with one in-flight request -> readiness false immediately; close after completion or deadline.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
