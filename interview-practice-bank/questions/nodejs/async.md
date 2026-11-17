# Full Stack Developer - NodeJs: Async

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Promises and async await

### Beginner

#### NODE-ASYNC-01-B01

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B02

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B03

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B04

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B05

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B06

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B07

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B08

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B09

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B10

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B11

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B12

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B13

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B14

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-01-B15

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-ASYNC-01-I01

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I02

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I03

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I04

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I05

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I06

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I07

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I08

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I09

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I10

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I11

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I12

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I13

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I14

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-01-I15

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-ASYNC-01-A01

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A02

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A03

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A04

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A05

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A06

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A07

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A08

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A09

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A10

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A11

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A12

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A13

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A14

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-01-A15

**Core:** Implement fetchAll(ids,fetch,limit). Keep at most limit promises running; preserve result order and return {ok:value} or {error:message} per item. Synchronous throw from fetch is also an item error.

**Acceptance example / fixture:** ids a,b; b resolves first -> results still a,b.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Event loop and CPU work

### Beginner

#### NODE-ASYNC-02-B01

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B02

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B03

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B04

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B05

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B06

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B07

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B08

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B09

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B10

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B11

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B12

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B13

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B14

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-02-B15

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-ASYNC-02-I01

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I02

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I03

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I04

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I05

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I06

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I07

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I08

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I09

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I10

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I11

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I12

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I13

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I14

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-02-I15

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-ASYNC-02-A01

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A02

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A03

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A04

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A05

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A06

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A07

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A08

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A09

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A10

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A11

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A12

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A13

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A14

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-02-A15

**Core:** Implement chunkedSum(values,chunkSize,schedule), summing safe integers in chunks, yielding through an injected scheduler between chunks. Reject overflow. Show that an unrelated scheduled callback runs before a long computation completes.

**Acceptance example / fixture:** [1,2,3],chunkSize=2 -> sum 6 with one yield between chunks.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Streams and backpressure

### Beginner

#### NODE-ASYNC-03-B01

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B02

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B03

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B04

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B05

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B06

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B07

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B08

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B09

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B10

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B11

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B12

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B13

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B14

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-03-B15

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-ASYNC-03-I01

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I02

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I03

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I04

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I05

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I06

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I07

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I08

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I09

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I10

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I11

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I12

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I13

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I14

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-03-I15

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-ASYNC-03-A01

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A02

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A03

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A04

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A05

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A06

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A07

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A08

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A09

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A10

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A11

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A12

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A13

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A14

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-03-A15

**Core:** Implement an NDJSON transform from readable to writable: parse each nonblank line as {id,cents}, validate, and write one normalized JSON line. Stop on malformed input with line number; respect writable backpressure and do not buffer the full stream.

**Acceptance example / fixture:** {"id":"a","cents":2} followed by blank line -> one output line.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Cancellation and timeouts

### Beginner

#### NODE-ASYNC-04-B01

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B02

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B03

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B04

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B05

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B06

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B07

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B08

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B09

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B10

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B11

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B12

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B13

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B14

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-ASYNC-04-B15

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-ASYNC-04-I01

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I02

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I03

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I04

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I05

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I06

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I07

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I08

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I09

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I10

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I11

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I12

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I13

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I14

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-ASYNC-04-I15

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-ASYNC-04-A01

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A02

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A03

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A04

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A05

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A06

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A07

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A08

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A09

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A10

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A11

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A12

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A13

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A14

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-ASYNC-04-A15

**Core:** Implement withDeadline(operation,deadline,clock,signal). Start operation once; if deadline expires first return TIMEOUT and signal cancellation. If caller aborts first return CANCELLED. Settle once and remove timers/listeners.

**Acceptance example / fixture:** Completion at 5 with deadline 10 -> success; completion at 11 -> TIMEOUT.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
