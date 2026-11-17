# Full Stack Developer - Java: Backend

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Spring request validation

### Beginner

#### JAVA-BACKEND-01-B01

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B02

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B03

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B04

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B05

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B06

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B07

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B08

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B09

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B10

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B11

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B12

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B13

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B14

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-01-B15

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-BACKEND-01-I01

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I02

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I03

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I04

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I05

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I06

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I07

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I08

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I09

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I10

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I11

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I12

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I13

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I14

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-01-I15

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-BACKEND-01-A01

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A02

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A03

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A04

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A05

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A06

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A07

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A08

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A09

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A10

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A11

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A12

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A13

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A14

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-01-A15

**Core:** Implement POST /reservations with JSON {sku,quantity}; SKU must be nonblank and quantity a positive integer. Return 201 with reservation ID on success, 400 for invalid input, 409 for insufficient stock. Inject inventory; invalid requests must not call it.

**Acceptance example / fixture:** {sku:A,quantity:0} -> 400 and no stock change.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## REST errors and exception mapping

### Beginner

#### JAVA-BACKEND-02-B01

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B02

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B03

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B04

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B05

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B06

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B07

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B08

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B09

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B10

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B11

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B12

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B13

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B14

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-02-B15

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-BACKEND-02-I01

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I02

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I03

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I04

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I05

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I06

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I07

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I08

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I09

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I10

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I11

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I12

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I13

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I14

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-02-I15

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-BACKEND-02-A01

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A02

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A03

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A04

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A05

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A06

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A07

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A08

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A09

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A10

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A11

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A12

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A13

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A14

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-02-A15

**Core:** Implement GET /orders/{id}: 200 with order if found, 404 if absent, 400 for an ID outside [A-Z][0-9]{3}, and 503 for an injected temporary repository failure. Return {code,message} errors without stack traces.

**Acceptance example / fixture:** A001 absent -> 404; bad -> 400.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## JPA fetching and pagination

### Beginner

#### JAVA-BACKEND-03-B01

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B02

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B03

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B04

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B05

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B06

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B07

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B08

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B09

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B10

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Return the core's dependency/resource graph and validate every referenced node exists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B11

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B12

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Produce a dry-run plan describing observable actions with no external mutation calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B13

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B14

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-03-B15

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-BACKEND-03-I01

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I02

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I03

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I04

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I05

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I06

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I07

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I08

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I09

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I10

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I11

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I12

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I13

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I14

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-03-I15

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-BACKEND-03-A01

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A02

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A03

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A04

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A05

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A06

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A07

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A08

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A09

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A10

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A11

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A12

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A13

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A14

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-03-A15

**Core:** Design entities Customer and Order with one customer per order. Implement a page of 20 order summaries including customer name, ordered by createdAt,id. Demonstrate bounded query count with an integration test; avoid one customer query per row.

**Acceptance example / fixture:** For 20 orders, query count must not grow by one per order; return stable IDs on equal timestamps.

**Question:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Transactions and optimistic locking

### Beginner

#### JAVA-BACKEND-04-B01

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B02

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B03

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B04

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B05

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B06

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B07

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B08

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B09

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B10

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B11

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B12

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B13

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B14

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-04-B15

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-BACKEND-04-I01

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I02

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I03

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I04

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I05

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I06

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I07

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I08

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I09

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I10

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I11

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I12

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I13

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I14

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-04-I15

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-BACKEND-04-A01

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A02

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A03

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A04

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A05

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A06

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A07

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A08

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A09

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A10

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A11

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A12

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A13

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A14

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-04-A15

**Core:** Implement updateOrder(id,expectedVersion,newStatus). Allowed transitions are Open->Paid->Shipped; every successful change increments version. Reject stale version with 409 and invalid transition with 422 without mutation.

**Acceptance example / fixture:** Open version 2 -> Paid using version 2 gives version 3; retry version 2 -> 409.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Authentication and authorization

### Beginner

#### JAVA-BACKEND-05-B01

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B02

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B03

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B04

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B05

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B06

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B07

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B08

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B09

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B10

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B11

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B12

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B13

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B14

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-05-B15

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-BACKEND-05-I01

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I02

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I03

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I04

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I05

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I06

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I07

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I08

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I09

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I10

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I11

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I12

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I13

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I14

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-05-I15

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-BACKEND-05-A01

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A02

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A03

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A04

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A05

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A06

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A07

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A08

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A09

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A10

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A11

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A12

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A13

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A14

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-05-A15

**Core:** Implement canReadOrder(actor,order): authenticated admin may read any order; authenticated customer only their own. Missing identity denies. Return decision and reason; enforce at the service boundary as well as HTTP layer.

**Acceptance example / fixture:** customer a reading b -> deny; unauthenticated admin claim -> deny.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Idempotent payment APIs

### Beginner

#### JAVA-BACKEND-06-B01

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B02

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B03

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B04

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B05

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B06

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B07

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B08

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B09

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B10

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B11

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B12

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B13

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B14

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-BACKEND-06-B15

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-BACKEND-06-I01

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I02

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I03

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I04

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I05

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I06

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I07

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I08

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I09

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I10

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I11

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I12

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I13

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I14

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-BACKEND-06-I15

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-BACKEND-06-A01

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A02

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A03

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A04

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A05

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A06

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A07

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A08

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A09

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A10

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A11

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A12

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A13

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A14

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-BACKEND-06-A15

**Core:** Implement POST /payments with Idempotency-Key and {orderId,cents}. First valid request charges once and returns receipt; replay with identical body returns the receipt; same key with a different body gives 409. Inject gateway and store.

**Acceptance example / fixture:** Two identical calls -> one charge and identical receipt.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
