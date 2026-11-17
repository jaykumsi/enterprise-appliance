# Shared Data Engineering Tools: Local Development

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Python reference model; PySpark/Parquet/Airflow native checks need their respective runtimes.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Docker and service readiness

### Beginner

#### DE-LOCAL-DEVELOPMENT-01-B01

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B02

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B03

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B04

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B05

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B06

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B07

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B08

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B09

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B10

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B11

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B12

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B13

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B14

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-01-B15

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### DE-LOCAL-DEVELOPMENT-01-I01

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I02

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I03

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I04

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I05

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I06

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I07

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I08

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I09

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I10

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I11

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I12

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I13

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I14

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-01-I15

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### DE-LOCAL-DEVELOPMENT-01-A01

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A02

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A03

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A04

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A05

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A06

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A07

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A08

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A09

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A10

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A11

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A12

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A13

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A14

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-01-A15

**Core:** Implement a dependency readiness checker for PostgreSQL and object-store mocks. A service is ready only after a functional probe succeeds, not merely a running container. Use injected probe results and deadline; return failed service names sorted.

**Acceptance example / fixture:** DB container running but query fails -> DB not ready.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## LocalStack and cloud adapters

### Beginner

#### DE-LOCAL-DEVELOPMENT-02-B01

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B02

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B03

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B04

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B05

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B06

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B07

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B08

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B09

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B10

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B11

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B12

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B13

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B14

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-02-B15

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### DE-LOCAL-DEVELOPMENT-02-I01

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I02

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I03

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I04

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I05

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I06

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I07

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I08

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I09

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I10

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I11

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I12

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I13

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I14

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-02-I15

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### DE-LOCAL-DEVELOPMENT-02-A01

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A02

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A03

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A04

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A05

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A06

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A07

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A08

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A09

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A10

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A11

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A12

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A13

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A14

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-02-A15

**Core:** Implement endpoint configuration: local mode requires explicit localhost endpoints for storage/queue and synthetic credentials; cloud mode forbids a localhost override. Produce a validated adapter configuration without network calls.

**Acceptance example / fixture:** local mode with queue endpoint absent -> error queue_endpoint.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## AppFlow transfer reconciliation

### Beginner

#### DE-LOCAL-DEVELOPMENT-03-B01

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B02

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B03

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B04

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B05

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B06

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B07

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B08

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B09

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B10

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B11

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B12

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B13

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B14

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-LOCAL-DEVELOPMENT-03-B15

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### DE-LOCAL-DEVELOPMENT-03-I01

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I02

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I03

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I04

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I05

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I06

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I07

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I08

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I09

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I10

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I11

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I12

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I13

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I14

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-LOCAL-DEVELOPMENT-03-I15

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### DE-LOCAL-DEVELOPMENT-03-A01

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A02

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A03

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A04

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A05

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A06

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A07

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A08

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A09

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A10

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A11

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A12

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A13

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A14

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-LOCAL-DEVELOPMENT-03-A15

**Core:** Reconcile source and sink manifests of {id,version,checksum}. Return missing IDs,stale versions and checksum mismatches sorted by ID; do not consider equal counts proof of equivalence.

**Acceptance example / fixture:** Source a:v2/x,b:v1/y; sink a:v1/x,c:v1/z -> missing b, stale a, extra c.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
