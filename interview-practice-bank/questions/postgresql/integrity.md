# PostgreSQL: Integrity

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Keys and check constraints

### Beginner

#### PG-INTEGRITY-01-B01

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Implement the core in a fresh scratch namespace. Return the before state,each operation's outcome and final state; do not change the shared fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B02

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Implement a preflight query that confirms all core prerequisites before any change. Return the missing objects or columns in sorted order and perform no changes if a prerequisite is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B03

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Apply only the first change from the core, then return all columns of every affected scratch row in primary-key order. Verify unaffected rows separately.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B04

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Repeat the core against an empty scratch fixture with the same schema. Return created objects,accepted changes and rejected changes without suppressing errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B05

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Write a check query for the core's main integrity rule, returning violating keys. Demonstrate it on a scratch copy with one deliberately bad row before adding enforcement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B06

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Capture the exact number of affected rows for each core operation. Distinguish a successful zero-row operation from a rejected operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B07

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Prepare a scratch copy with the core's first primary key duplicated before constraint creation. Return a diagnostic that identifies the duplicate instead of silently deleting it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B08

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Implement a validation-first version of the core. Return the input values that cannot be represented by the requested column types before attempting the mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B09

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Run each core operation as an independently recorded action. Return operation ordinal,status and error category; do not claim later actions succeeded if an earlier prerequisite failed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B10

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Inspect object metadata after the core and return actual column types,nullability and key membership. Compare with the requested definition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B11

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Generate a script that creates only the scratch prerequisites, loads the baseline rows and runs the core. Verify it works in a newly created empty training namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B12

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Apply a no-change request to the core's target. Return whether it is accepted and the resulting state; show that a no-change request is not automatically a rejected request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B13

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Demonstrate the core's behavior when a required input is null. Return the rejected field or database error category and show that no invalid row persists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B14

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Show the dependency order required by the core's object changes using a small object graph. Return a valid execution order and identify an invalid one with a concrete failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-01-B15

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Write postcondition assertions for the core and demonstrate one failing assertion by deliberately altering only the scratch result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-INTEGRITY-01-I01

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Make the core rerunnable with a declared policy for already-existing objects or already-applied changes. Preserve correct existing data; return APPLIED,ALREADY_APPLIED or CONFLICT per action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I02

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Handle a batch containing valid and invalid changes. Use explicit all-or-nothing batch semantics in an instructor-controlled scratch environment and show the state after rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I03

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Provide a dry-run planner returning ordered changes and their preconditions. Verify that dry-run performs no writes and agrees with the eventual execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I04

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Add an audit relation containing action ID,target key,before state and after state. An audit record must correspond to an actual accepted change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I05

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Add an expected-version precondition to mutable target rows. A stale expected version returns CONFLICT without changing the row or writing a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I06

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Implement safe rename/migration logic that retains existing rows and dependent relationships. Supply pre/post queries proving row counts and referenced keys are preserved.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I07

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Add a failure injection between two dependent changes. In the selected engine demonstrate how recovery returns to a consistent,documented state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I08

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Accept a batch with repeated target keys. Collapse identical repeated requests; reject conflicting requests for the same key before any write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I09

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Build a restore script from captured before-state data for the scratch fixture. Demonstrate exact restoration of values and key relationships after the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I10

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Validate that every referenced parent exists before child changes. Return all missing references together; do not disable referential constraints to make the batch pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I11

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Compare declarative database enforcement with application-only validation by showing a direct SQL write that bypasses the application. Keep the database rule authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I12

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Generate a migration verification report including object metadata,invalid-row counts,orphan counts and baseline row preservation. Return actual query results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I13

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Support an explicit allowlist of target scratch objects. Reject a dynamically supplied identifier outside it without constructing executable SQL from raw input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I14

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Implement a bulk version and a row-by-row reference version. Compare final rows,rejections and audit effects,not just elapsed time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-01-I15

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Add a schema-version precondition to the script. Wrong version must stop before the first change; correct version must produce the baseline result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-INTEGRITY-01-A01

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Plan and demonstrate the core while another session writes to the target. Show the locking/isolation strategy and prove that the final integrity rule holds.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A02

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Make the migration restartable using a durable step journal. Inject failure after each step and show that rerun applies no accepted step twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A03

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Implement expand-and-contract migration with old and new application readers. Demonstrate the compatibility window and the checks required before removing the old representation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A04

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Chunk a large data change using a stable key and checkpoint. Show crash recovery at a chunk boundary and prove no row is skipped or processed twice as a business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A05

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Design a compensating recovery for an engine operation that cannot share the desired atomic boundary. Show the durable record of incomplete work and the exact repair action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A06

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Demonstrate concurrent identical requests under one idempotency key. Exactly one may perform the accepted business change; others must receive the same recorded result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A07

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Handle an ambiguous client timeout after the database may have committed. Reconcile by durable action ID before retrying; prove there is no duplicate mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A08

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Detect drift between expected and actual metadata before applying the migration. Reject incompatible drift and produce a targeted diff instead of overwriting it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A09

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Benchmark validation and mutation separately on a reproducible fixture. Report actual work and locking observations,then verify the complete resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A10

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Create adversarial fixtures for overflow,nulls,duplicate keys,orphans and conflicting versions. Show that the core leaves no partially valid state after any rejected case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A11

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Generate a least-privilege execution plan separating setup privileges from runtime mutation privileges. Demonstrate both an allowed operation and a denied unrelated write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A12

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Version the published database contract and provide old/new reader regression tests. Prove a migration cannot silently reinterpret a stored value.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A13

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Model two conflicting migration runners. Use a database-backed ownership mechanism so only one applies changes; show recovery when the owner stops midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A14

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Create an independent reconciliation query from the original business invariants,without reusing the migration's own predicate. Demonstrate a seeded defect it catches.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-01-A15

**Core:** Create a scratch Stock(sku text primary key,quantity integer not null check quantity>=0). Apply inserts (A,2),(B,0),(C,-1) separately; capture accepted rows and rejection reason categories. Leave A and B present.

**Acceptance example / fixture:** Final rows [[A,2],[B,0]]; C rejected CHECK.

**Question:** Deliver a reproducible migration package with dry run,preconditions,journal,recovery,postconditions and failure-injection evidence. Run it against both a clean and a partially completed scratch state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Upserts and conflict targets

### Beginner

#### PG-INTEGRITY-02-B01

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Implement the core in a fresh scratch namespace. Return the before state,each operation's outcome and final state; do not change the shared fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B02

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Implement a preflight query that confirms all core prerequisites before any change. Return the missing objects or columns in sorted order and perform no changes if a prerequisite is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B03

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Apply only the first change from the core, then return all columns of every affected scratch row in primary-key order. Verify unaffected rows separately.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B04

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Repeat the core against an empty scratch fixture with the same schema. Return created objects,accepted changes and rejected changes without suppressing errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B05

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Write a check query for the core's main integrity rule, returning violating keys. Demonstrate it on a scratch copy with one deliberately bad row before adding enforcement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B06

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Capture the exact number of affected rows for each core operation. Distinguish a successful zero-row operation from a rejected operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B07

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Prepare a scratch copy with the core's first primary key duplicated before constraint creation. Return a diagnostic that identifies the duplicate instead of silently deleting it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B08

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Implement a validation-first version of the core. Return the input values that cannot be represented by the requested column types before attempting the mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B09

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Run each core operation as an independently recorded action. Return operation ordinal,status and error category; do not claim later actions succeeded if an earlier prerequisite failed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B10

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Inspect object metadata after the core and return actual column types,nullability and key membership. Compare with the requested definition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B11

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Generate a script that creates only the scratch prerequisites, loads the baseline rows and runs the core. Verify it works in a newly created empty training namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B12

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Apply a no-change request to the core's target. Return whether it is accepted and the resulting state; show that a no-change request is not automatically a rejected request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B13

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Demonstrate the core's behavior when a required input is null. Return the rejected field or database error category and show that no invalid row persists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B14

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Show the dependency order required by the core's object changes using a small object graph. Return a valid execution order and identify an invalid one with a concrete failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-02-B15

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Write postcondition assertions for the core and demonstrate one failing assertion by deliberately altering only the scratch result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-INTEGRITY-02-I01

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Make the core rerunnable with a declared policy for already-existing objects or already-applied changes. Preserve correct existing data; return APPLIED,ALREADY_APPLIED or CONFLICT per action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I02

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Handle a batch containing valid and invalid changes. Use explicit all-or-nothing batch semantics in an instructor-controlled scratch environment and show the state after rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I03

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Provide a dry-run planner returning ordered changes and their preconditions. Verify that dry-run performs no writes and agrees with the eventual execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I04

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Add an audit relation containing action ID,target key,before state and after state. An audit record must correspond to an actual accepted change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I05

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Add an expected-version precondition to mutable target rows. A stale expected version returns CONFLICT without changing the row or writing a success audit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I06

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Implement safe rename/migration logic that retains existing rows and dependent relationships. Supply pre/post queries proving row counts and referenced keys are preserved.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I07

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Add a failure injection between two dependent changes. In the selected engine demonstrate how recovery returns to a consistent,documented state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I08

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Accept a batch with repeated target keys. Collapse identical repeated requests; reject conflicting requests for the same key before any write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I09

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Build a restore script from captured before-state data for the scratch fixture. Demonstrate exact restoration of values and key relationships after the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I10

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Validate that every referenced parent exists before child changes. Return all missing references together; do not disable referential constraints to make the batch pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I11

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Compare declarative database enforcement with application-only validation by showing a direct SQL write that bypasses the application. Keep the database rule authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I12

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Generate a migration verification report including object metadata,invalid-row counts,orphan counts and baseline row preservation. Return actual query results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I13

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Support an explicit allowlist of target scratch objects. Reject a dynamically supplied identifier outside it without constructing executable SQL from raw input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I14

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Implement a bulk version and a row-by-row reference version. Compare final rows,rejections and audit effects,not just elapsed time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-02-I15

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Add a schema-version precondition to the script. Wrong version must stop before the first change; correct version must produce the baseline result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-INTEGRITY-02-A01

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Plan and demonstrate the core while another session writes to the target. Show the locking/isolation strategy and prove that the final integrity rule holds.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A02

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Make the migration restartable using a durable step journal. Inject failure after each step and show that rerun applies no accepted step twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A03

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Implement expand-and-contract migration with old and new application readers. Demonstrate the compatibility window and the checks required before removing the old representation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A04

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Chunk a large data change using a stable key and checkpoint. Show crash recovery at a chunk boundary and prove no row is skipped or processed twice as a business effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A05

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Design a compensating recovery for an engine operation that cannot share the desired atomic boundary. Show the durable record of incomplete work and the exact repair action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A06

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Demonstrate concurrent identical requests under one idempotency key. Exactly one may perform the accepted business change; others must receive the same recorded result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A07

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Handle an ambiguous client timeout after the database may have committed. Reconcile by durable action ID before retrying; prove there is no duplicate mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A08

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Detect drift between expected and actual metadata before applying the migration. Reject incompatible drift and produce a targeted diff instead of overwriting it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A09

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Benchmark validation and mutation separately on a reproducible fixture. Report actual work and locking observations,then verify the complete resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A10

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Create adversarial fixtures for overflow,nulls,duplicate keys,orphans and conflicting versions. Show that the core leaves no partially valid state after any rejected case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A11

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Generate a least-privilege execution plan separating setup privileges from runtime mutation privileges. Demonstrate both an allowed operation and a denied unrelated write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A12

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Version the published database contract and provide old/new reader regression tests. Prove a migration cannot silently reinterpret a stored value.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A13

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Model two conflicting migration runners. Use a database-backed ownership mechanism so only one applies changes; show recovery when the owner stops midway.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A14

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Create an independent reconciliation query from the original business invariants,without reusing the migration's own predicate. Demonstrate a seeded defect it catches.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-02-A15

**Core:** Create scratch Balances(id text primary key,cents bigint not null). Starting a:10, process a:+5,b:+3,a:-2 as deltas. Use a single atomic upsert per delta; return final balances sorted by id.

**Acceptance example / fixture:** Final [[a,13],[b,3]].

**Question:** Deliver a reproducible migration package with dry run,preconditions,journal,recovery,postconditions and failure-injection evidence. Run it against both a clean and a partially completed scratch state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Transactions and isolation

### Beginner

#### PG-INTEGRITY-03-B01

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B02

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B03

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B04

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B05

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B06

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B07

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B08

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B09

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B10

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B11

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B12

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B13

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B14

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-03-B15

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-INTEGRITY-03-I01

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I02

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I03

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I04

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I05

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I06

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I07

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I08

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I09

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I10

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I11

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I12

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I13

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I14

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-03-I15

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-INTEGRITY-03-A01

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A02

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A03

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A04

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A05

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A06

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A07

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A08

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A09

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A10

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A11

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A12

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A13

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A14

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-03-A15

**Core:** With Stock(sku,quantity) initially A:1, implement a reservation operation in PostgreSQL which atomically decrements only if stock is positive. Give two-session SQL and an interleaving showing only one reservation succeeds and final stock is zero.

**Acceptance example / fixture:** Two concurrent reservations -> one success, one failure, quantity 0.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Locks and deadlock recovery

### Beginner

#### PG-INTEGRITY-04-B01

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B02

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B03

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B04

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B05

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B06

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B07

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B08

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B09

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B10

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B11

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B12

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B13

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B14

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-INTEGRITY-04-B15

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-INTEGRITY-04-I01

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I02

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I03

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I04

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I05

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I06

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I07

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I08

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I09

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I10

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I11

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I12

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I13

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I14

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-INTEGRITY-04-I15

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-INTEGRITY-04-A01

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A02

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A03

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A04

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A05

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A06

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A07

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A08

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A09

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A10

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A11

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A12

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A13

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A14

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-INTEGRITY-04-A15

**Core:** Two transfers need accounts A and B. Implement consistent account-lock ordering by account ID, check sufficient funds, and move integer cents atomically. Starting A:100,B:100, transfer A->B 30. Prove funds are conserved; failed transfer changes neither balance.

**Acceptance example / fixture:** After successful transfer A:70,B:130; sum 200.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
