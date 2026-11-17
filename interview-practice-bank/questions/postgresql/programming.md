# PostgreSQL: Programming

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## PLpgSQL and error handling

### Beginner

#### PG-PROGRAMMING-01-B01

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Implement the core in a fresh scratch namespace. Return the before state,each operation's outcome and final state; do not change the shared fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B02

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Implement a preflight query that confirms all core prerequisites before any change. Return the missing objects or columns in sorted order and perform no changes if a prerequisite is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B03

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Apply only the first change from the core, then return all columns of every affected scratch row in primary-key order. Verify unaffected rows separately.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B04

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Repeat the core against an empty scratch fixture with the same schema. Return created objects,accepted changes and rejected changes without suppressing errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B05

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Write a check query for the core's main integrity rule, returning violating keys. Demonstrate it on a scratch copy with one deliberately bad row before adding enforcement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B06

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Capture the exact number of affected rows for each core operation. Distinguish a successful zero-row operation from a rejected operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B07

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Prepare a scratch copy with the core's first primary key duplicated before constraint creation. Return a diagnostic that identifies the duplicate instead of silently deleting it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B08

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Implement a validation-first version of the core. Return the input values that cannot be represented by the requested column types before attempting the mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B09

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Run each core operation as an independently recorded action. Return operation ordinal,status and error category; do not claim later actions succeeded if an earlier prerequisite failed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B10

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Inspect object metadata after the core and return actual column types,nullability and key membership. Compare with the requested definition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B11

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Generate a script that creates only the scratch prerequisites, loads the baseline rows and runs the core. Verify it works in a newly created empty training namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B12

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Apply a no-change request to the core's target. Return whether it is accepted and the resulting state; show that a no-change request is not automatically a rejected request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B13

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Demonstrate the core's behavior when a required input is null. Return the rejected field or database error category and show that no invalid row persists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B14

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Show the dependency order required by the core's object changes using a small object graph. Return a valid execution order and identify an invalid one with a concrete failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PROGRAMMING-01-B15

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Write postcondition assertions for the core and demonstrate one failing assertion by deliberately altering only the scratch result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-PROGRAMMING-01-I01

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Make the core rerunnable with a declared policy for already-existing objects or already-applied changes. Preserve correct existing data; return APPLIED,ALREADY_APPLIED or CONFLICT per action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I02

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Handle a batch containing valid and invalid changes. Use explicit all-or-nothing batch semantics in an instructor-controlled scratch environment and show the state after rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I03

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Provide a dry-run planner returning ordered changes and their preconditions. Verify that dry-run performs no writes and agrees with the eventual execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I04

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Add an audit relation containing action ID,target key,before state and after state. An audit record must correspond to an actual accepted change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I05

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Add an expected-version precondition to mutable target rows. A stale expected version returns CONFLICT without changing the row or writing a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I06

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Implement safe rename/migration logic that retains existing rows and dependent relationships. Supply pre/post queries proving row counts and referenced keys are preserved.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I07

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Add a failure injection between two dependent changes. In the selected engine demonstrate how recovery returns to a consistent,documented state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I08

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Accept a batch with repeated target keys. Collapse identical repeated requests; reject conflicting requests for the same key before any write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I09

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Build a restore script from captured before-state data for the scratch fixture. Demonstrate exact restoration of values and key relationships after the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I10

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Validate that every referenced parent exists before child changes. Return all missing references together; do not disable referential constraints to make the batch pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I11

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Compare declarative database enforcement with application-only validation by showing a direct SQL write that bypasses the application. Keep the database rule authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I12

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Generate a migration verification report including object metadata,invalid-row counts,orphan counts and baseline row preservation. Return actual query results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I13

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Support an explicit allowlist of target scratch objects. Reject a dynamically supplied identifier outside it without constructing executable SQL from raw input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I14

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Implement a bulk version and a row-by-row reference version. Compare final rows,rejections and audit effects,not just elapsed time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PROGRAMMING-01-I15

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Add a schema-version precondition to the script. Wrong version must stop before the first change; correct version must produce the baseline result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-PROGRAMMING-01-A01

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Plan and demonstrate the core while another session writes to the target. Show the locking/isolation strategy and prove that the final integrity rule holds.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A02

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Make the migration restartable using a durable step journal. Inject failure after each step and show that rerun applies no accepted step twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A03

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Implement expand-and-contract migration with old and new application readers. Demonstrate the compatibility window and the checks required before removing the old representation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A04

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Chunk a large data change using a stable key and checkpoint. Show crash recovery at a chunk boundary and prove no row is skipped or processed twice as a business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A05

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Design a compensating recovery for an engine operation that cannot share the desired atomic boundary. Show the durable record of incomplete work and the exact repair action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A06

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Demonstrate concurrent identical requests under one idempotency key. Exactly one may perform the accepted business change; others must receive the same recorded result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A07

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Handle an ambiguous client timeout after the database may have committed. Reconcile by durable action ID before retrying; prove there is no duplicate mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A08

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Detect drift between expected and actual metadata before applying the migration. Reject incompatible drift and produce a targeted diff instead of overwriting it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A09

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Benchmark validation and mutation separately on a reproducible fixture. Report actual work and locking observations,then verify the complete resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A10

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Create adversarial fixtures for overflow,nulls,duplicate keys,orphans and conflicting versions. Show that the core leaves no partially valid state after any rejected case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A11

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Generate a least-privilege execution plan separating setup privileges from runtime mutation privileges. Demonstrate both an allowed operation and a denied unrelated write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A12

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Version the published database contract and provide old/new reader regression tests. Prove a migration cannot silently reinterpret a stored value.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A13

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Model two conflicting migration runners. Use a database-backed ownership mechanism so only one applies changes; show recovery when the owner stops midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A14

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Create an independent reconciliation query from the original business invariants,without reusing the migration's own predicate. Demonstrate a seeded defect it catches.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PROGRAMMING-01-A15

**Core:** Write a PostgreSQL function reserve(sku,qty) over scratch Stock, returning true only when an existing row has at least positive integer qty available. Starting A:3, call reserve(A,2),reserve(A,2),reserve(X,1). Return decisions and final stock.

**Acceptance example / fixture:** [true,false,false]; A:1.

**Question:** Deliver a reproducible migration package with dry run,preconditions,journal,recovery,postconditions and failure-injection evidence. Run it against both a clean and a partially completed scratch state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
