# Full Stack Developer - NodeJs: Backend

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## HTTP routing and validation

### Beginner

#### NODE-BACKEND-01-B01

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B02

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B03

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B04

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B05

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B06

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B07

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B08

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B09

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B10

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B11

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B12

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B13

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B14

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-01-B15

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-01-I01

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I02

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I03

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I04

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I05

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I06

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I07

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I08

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I09

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I10

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I11

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I12

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I13

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I14

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-01-I15

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-01-A01

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A02

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A03

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A04

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A05

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A06

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A07

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A08

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A09

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A10

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A11

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A12

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A13

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A14

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-01-A15

**Core:** Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / fixture:** quantity 0 -> 400; A available 1 requested 2 -> 409.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Express middleware and errors

### Beginner

#### NODE-BACKEND-02-B01

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B02

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B03

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B04

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B05

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B06

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B07

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B08

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B09

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B10

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B11

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B12

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B13

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B14

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-02-B15

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-02-I01

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I02

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I03

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I04

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I05

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I06

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I07

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I08

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I09

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I10

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I11

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I12

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I13

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I14

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-02-I15

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-02-A01

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A02

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A03

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A04

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A05

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A06

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A07

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A08

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A09

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A10

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A11

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A12

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A13

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A14

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-02-A15

**Core:** Implement request ID and error middleware. Accept an incoming X-Request-ID only if it matches [A-Za-z0-9-]{1,64}; otherwise generate one using an injected function. All success/error responses carry it; log one sanitized error record per failed request.

**Acceptance example / fixture:** Bad ID with newline -> generated ID; response and log IDs identical.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## REST filtering and pagination

### Beginner

#### NODE-BACKEND-03-B01

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B02

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B03

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B04

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B05

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B06

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B07

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B08

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B09

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B10

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B11

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B12

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B13

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B14

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-03-B15

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-03-I01

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I02

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I03

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I04

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I05

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I06

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I07

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I08

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I09

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I10

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I11

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I12

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I13

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I14

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-03-I15

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-03-A01

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A02

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A03

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A04

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A05

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A06

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A07

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A08

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A09

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A10

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A11

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A12

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A13

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A14

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-03-A15

**Core:** Implement GET /orders?limit=n&after=id over an injected ID-sorted repository. limit defaults 20 and must be integer 1..100. Return at most n rows with ID strictly greater than after, plus next cursor only if more rows exist.

**Acceptance example / fixture:** IDs a,b,c; limit 2 -> rows a,b and next b.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Database atomicity

### Beginner

#### NODE-BACKEND-04-B01

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B02

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B03

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B04

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B05

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B06

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B07

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B08

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B09

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B10

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B11

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B12

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B13

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B14

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-04-B15

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-04-I01

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I02

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I03

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I04

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I05

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I06

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I07

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I08

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I09

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I10

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I11

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I12

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I13

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I14

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-04-I15

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-04-A01

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A02

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A03

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A04

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A05

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A06

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A07

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A08

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A09

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A10

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A11

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A12

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A13

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A14

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-04-A15

**Core:** Implement reserveOne(sku) with an injected SQL store. Use one conditional update that decrements only positive availability. Starting A:1, two simultaneous requests must yield exactly one success.

**Acceptance example / fixture:** Final availability 0; affected-row counts 1 and 0.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Authentication and access control

### Beginner

#### NODE-BACKEND-05-B01

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B02

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B03

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B04

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B05

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B06

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B07

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B08

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B09

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B10

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B11

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B12

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B13

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B14

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-05-B15

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-05-I01

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I02

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I03

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I04

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I05

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I06

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I07

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I08

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I09

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I10

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I11

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I12

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I13

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I14

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-05-I15

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-05-A01

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A02

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A03

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A04

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A05

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A06

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A07

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A08

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A09

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A10

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A11

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A12

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A13

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A14

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-05-A15

**Core:** Implement canReadOrder(actor,order). Require authenticated identity; admin can read all, customer only their own. Treat client-provided role headers as untrusted. Return reason codes NO_IDENTITY,NOT_OWNER,ALLOW.

**Acceptance example / fixture:** customer a reads b -> NOT_OWNER; no identity with admin header -> NO_IDENTITY.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Idempotency and retries

### Beginner

#### NODE-BACKEND-06-B01

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B02

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B03

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B04

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B05

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B06

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B07

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B08

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B09

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B10

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B11

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B12

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B13

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B14

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-06-B15

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-06-I01

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I02

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I03

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I04

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I05

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I06

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I07

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I08

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I09

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I10

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I11

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I12

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I13

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I14

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-06-I15

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-06-A01

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A02

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A03

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A04

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A05

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A06

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A07

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A08

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A09

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A10

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A11

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A12

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A13

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A14

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-06-A15

**Core:** Implement POST /payments using a durable idempotency store and injected gateway. Identical key/body replays the original receipt; key reused with another body gives 409. Store pending state before side effects and model an ambiguous gateway timeout explicitly.

**Acceptance example / fixture:** Identical successful replay -> one charge; unknown timeout -> PENDING, not an automatic second charge.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Caching and invalidation

### Beginner

#### NODE-BACKEND-07-B01

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B02

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B03

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B04

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B05

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B06

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B07

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B08

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B09

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B10

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B11

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B12

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B13

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B14

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-07-B15

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-07-I01

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I02

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I03

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I04

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I05

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I06

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I07

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I08

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I09

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I10

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I11

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I12

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I13

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I14

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-07-I15

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-07-A01

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A02

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A03

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A04

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A05

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A06

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A07

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A08

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A09

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A10

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A11

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A12

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A13

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A14

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-07-A15

**Core:** Implement a cache-aside order lookup with injected clock and repository. Entries live 60 seconds from load; nulls are not cached. updateOrder invalidates the entry only after successful persistence.

**Acceptance example / fixture:** Load at t=0,read at 59 -> hit; read at 60 -> repository call.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Webhooks and signatures

### Beginner

#### NODE-BACKEND-08-B01

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B02

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B03

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B04

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B05

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B06

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B07

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B08

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B09

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B10

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B11

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B12

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B13

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B14

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-BACKEND-08-B15

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-BACKEND-08-I01

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I02

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I03

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I04

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I05

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I06

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I07

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I08

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I09

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I10

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I11

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I12

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I13

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I14

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-BACKEND-08-I15

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-BACKEND-08-A01

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A02

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A03

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A04

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A05

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A06

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A07

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A08

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A09

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A10

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A11

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A12

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A13

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A14

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-BACKEND-08-A15

**Core:** Implement receiveWebhook(rawBytes,signature,verify,store). Verify exact raw bytes using injected verifier before parsing. Reject invalid signature with 401, malformed payload with 400. Deduplicate by event ID and acknowledge already committed events with 200.

**Acceptance example / fixture:** Two signed deliveries of same event -> one state change, both acknowledged.

**Question:** Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
