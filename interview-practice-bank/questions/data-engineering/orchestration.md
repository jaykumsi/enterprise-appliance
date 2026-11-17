# Shared Data Engineering Tools: Orchestration

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Python reference model; PySpark/Parquet/Airflow native checks need their respective runtimes.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Airflow dependencies and retries

### Beginner

#### DE-ORCHESTRATION-01-B01

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B02

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B03

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B04

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B05

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B06

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B07

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B08

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B09

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B10

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B11

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B12

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B13

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B14

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-01-B15

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### DE-ORCHESTRATION-01-I01

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I02

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I03

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I04

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I05

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I06

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I07

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I08

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I09

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I10

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I11

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I12

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I13

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I14

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-01-I15

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### DE-ORCHESTRATION-01-A01

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A02

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A03

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A04

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A05

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A06

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A07

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A08

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A09

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A10

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A11

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A12

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A13

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A14

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-01-A15

**Core:** Model tasks extract->validate->load->publish. validate failure blocks load and publish; extract may retry twice after its first attempt. Publish must reference a committed load ID. Produce task-state traces from injected outcomes.

**Acceptance example / fixture:** extract fails then succeeds,validate fails -> load and publish blocked.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Backfills and partition ownership

### Beginner

#### DE-ORCHESTRATION-02-B01

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B02

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B03

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B04

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B05

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B06

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B07

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B08

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B09

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B10

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B11

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B12

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B13

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B14

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### DE-ORCHESTRATION-02-B15

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### DE-ORCHESTRATION-02-I01

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I02

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I03

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I04

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I05

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I06

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I07

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I08

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I09

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I10

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I11

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I12

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I13

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I14

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### DE-ORCHESTRATION-02-I15

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### DE-ORCHESTRATION-02-A01

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A02

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A03

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A04

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A05

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A06

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A07

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A08

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A09

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A10

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A11

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A12

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A13

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A14

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### DE-ORCHESTRATION-02-A15

**Core:** Plan daily jobs for half-open UTC days in [start,end). Successful existing partitions are skipped unless force=true. At most one owner may publish a partition; retry must use the same partition idempotency key.

**Acceptance example / fixture:** [Jan1,Jan3), Jan1 already committed -> only Jan2 scheduled.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
