# Full Stack Developer - Java: Concurrency

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Executors and futures

### Beginner

#### JAVA-CONCURRENCY-01-B01

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B02

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B03

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B04

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B05

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B06

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B07

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B08

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B09

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B10

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B11

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B12

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B13

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B14

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-01-B15

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-CONCURRENCY-01-I01

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I02

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I03

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I04

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I05

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I06

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I07

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I08

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I09

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I10

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I11

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I12

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I13

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I14

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-01-I15

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-CONCURRENCY-01-A01

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A02

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A03

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A04

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A05

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A06

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A07

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A08

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A09

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A10

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A11

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A12

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A13

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A14

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-01-A15

**Core:** Implement fetchAll(ids,client,limit) using injected asynchronous client calls. At most limit in flight; preserve input order; represent per-id failure without dropping successful results. Caller cancellation must cancel outstanding work.

**Acceptance example / fixture:** [a,b], b completes first -> results ordered a,b.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Synchronization and atomicity

### Beginner

#### JAVA-CONCURRENCY-02-B01

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B02

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B03

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B04

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B05

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B06

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B07

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B08

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B09

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B10

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B11

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B12

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B13

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B14

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-CONCURRENCY-02-B15

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-CONCURRENCY-02-I01

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I02

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I03

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I04

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I05

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I06

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I07

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I08

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I09

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I10

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I11

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I12

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I13

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I14

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-CONCURRENCY-02-I15

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-CONCURRENCY-02-A01

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A02

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A03

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A04

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A05

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A06

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A07

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A08

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A09

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A10

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A11

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A12

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A13

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A14

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-CONCURRENCY-02-A15

**Core:** Implement a thread-safe stock reservation counter starting at 1, with reserveOne() returning boolean. Concurrent callers may succeed only once; stock never becomes negative. Supply a deterministic coordinated test rather than a timing sleep.

**Acceptance example / fixture:** Two callers -> one true, one false, final stock 0.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
