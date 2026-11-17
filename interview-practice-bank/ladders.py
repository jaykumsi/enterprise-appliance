"""Distinct extensions for each core problem, 15 at each difficulty.

An extension changes the deliverable, algorithm, or failure model. It is never
just another customer name or another set of constants. Core + extension is
the complete question; a core alone is not separately counted.
"""

LADDERS = {}


def ladder(name, beginner, intermediate, advanced):
    LADDERS[name] = {level: [x.strip() for x in text.strip().splitlines() if x.strip()]
                     for level, text in [('Beginner', beginner), ('Intermediate', intermediate), ('Advanced', advanced)]}
    assert all(len(v) == 15 for v in LADDERS[name].values()), name


ladder('query', r'''
Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.
Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.
Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.
Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.
Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.
Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.
Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.
Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.
Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.
Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.
Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.
Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.
Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.
Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.
Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.
''', r'''
Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.
Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.
Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.
Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.
Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.
Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.
Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.
Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.
Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.
Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.
Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.
Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.
Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.
For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.
Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.
''', r'''
Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.
Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.
Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.
Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.
Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.
Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.
Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.
Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.
Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.
Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.
Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.
Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.
Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.
Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.
Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.
''')

ladder('mutation', r'''
Implement the core in a fresh scratch namespace. Return the before state,each operation's outcome and final state; do not change the shared fixture.
Implement a preflight query that confirms all core prerequisites before any change. Return the missing objects or columns in sorted order and perform no changes if a prerequisite is absent.
Apply only the first change from the core, then return all columns of every affected scratch row in primary-key order. Verify unaffected rows separately.
Repeat the core against an empty scratch fixture with the same schema. Return created objects,accepted changes and rejected changes without suppressing errors.
Write a check query for the core's main integrity rule, returning violating keys. Demonstrate it on a scratch copy with one deliberately bad row before adding enforcement.
Capture the exact number of affected rows for each core operation. Distinguish a successful zero-row operation from a rejected operation.
Prepare a scratch copy with the core's first primary key duplicated before constraint creation. Return a diagnostic that identifies the duplicate instead of silently deleting it.
Implement a validation-first version of the core. Return the input values that cannot be represented by the requested column types before attempting the mutation.
Run each core operation as an independently recorded action. Return operation ordinal,status and error category; do not claim later actions succeeded if an earlier prerequisite failed.
Inspect object metadata after the core and return actual column types,nullability and key membership. Compare with the requested definition.
Generate a script that creates only the scratch prerequisites, loads the baseline rows and runs the core. Verify it works in a newly created empty training namespace.
Apply a no-change request to the core's target. Return whether it is accepted and the resulting state; show that a no-change request is not automatically a rejected request.
Demonstrate the core's behavior when a required input is null. Return the rejected field or database error category and show that no invalid row persists.
Show the dependency order required by the core's object changes using a small object graph. Return a valid execution order and identify an invalid one with a concrete failure.
Write postcondition assertions for the core and demonstrate one failing assertion by deliberately altering only the scratch result.
''', r'''
Make the core rerunnable with a declared policy for already-existing objects or already-applied changes. Preserve correct existing data; return APPLIED,ALREADY_APPLIED or CONFLICT per action.
Handle a batch containing valid and invalid changes. Use explicit all-or-nothing batch semantics in an instructor-controlled scratch environment and show the state after rejection.
Provide a dry-run planner returning ordered changes and their preconditions. Verify that dry-run performs no writes and agrees with the eventual execution plan.
Add an audit relation containing action ID,target key,before state and after state. An audit record must correspond to an actual accepted change.
Add an expected-version precondition to mutable target rows. A stale expected version returns CONFLICT without changing the row or writing a success audit.
Implement safe rename/migration logic that retains existing rows and dependent relationships. Supply pre/post queries proving row counts and referenced keys are preserved.
Add a failure injection between two dependent changes. In the selected engine demonstrate how recovery returns to a consistent,documented state.
Accept a batch with repeated target keys. Collapse identical repeated requests; reject conflicting requests for the same key before any write.
Build a restore script from captured before-state data for the scratch fixture. Demonstrate exact restoration of values and key relationships after the core.
Validate that every referenced parent exists before child changes. Return all missing references together; do not disable referential constraints to make the batch pass.
Compare declarative database enforcement with application-only validation by showing a direct SQL write that bypasses the application. Keep the database rule authoritative.
Generate a migration verification report including object metadata,invalid-row counts,orphan counts and baseline row preservation. Return actual query results.
Support an explicit allowlist of target scratch objects. Reject a dynamically supplied identifier outside it without constructing executable SQL from raw input.
Implement a bulk version and a row-by-row reference version. Compare final rows,rejections and audit effects,not just elapsed time.
Add a schema-version precondition to the script. Wrong version must stop before the first change; correct version must produce the baseline result.
''', r'''
Plan and demonstrate the core while another session writes to the target. Show the locking/isolation strategy and prove that the final integrity rule holds.
Make the migration restartable using a durable step journal. Inject failure after each step and show that rerun applies no accepted step twice.
Implement expand-and-contract migration with old and new application readers. Demonstrate the compatibility window and the checks required before removing the old representation.
Chunk a large data change using a stable key and checkpoint. Show crash recovery at a chunk boundary and prove no row is skipped or processed twice as a business effect.
Design a compensating recovery for an engine operation that cannot share the desired atomic boundary. Show the durable record of incomplete work and the exact repair action.
Demonstrate concurrent identical requests under one idempotency key. Exactly one may perform the accepted business change; others must receive the same recorded result.
Handle an ambiguous client timeout after the database may have committed. Reconcile by durable action ID before retrying; prove there is no duplicate mutation.
Detect drift between expected and actual metadata before applying the migration. Reject incompatible drift and produce a targeted diff instead of overwriting it.
Benchmark validation and mutation separately on a reproducible fixture. Report actual work and locking observations,then verify the complete resulting state.
Create adversarial fixtures for overflow,nulls,duplicate keys,orphans and conflicting versions. Show that the core leaves no partially valid state after any rejected case.
Generate a least-privilege execution plan separating setup privileges from runtime mutation privileges. Demonstrate both an allowed operation and a denied unrelated write.
Version the published database contract and provide old/new reader regression tests. Prove a migration cannot silently reinterpret a stored value.
Model two conflicting migration runners. Use a database-backed ownership mechanism so only one applies changes; show recovery when the owner stops midway.
Create an independent reconciliation query from the original business invariants,without reusing the migration's own predicate. Demonstrate a seeded defect it catches.
Deliver a reproducible migration package with dry run,preconditions,journal,recovery,postconditions and failure-injection evidence. Run it against both a clean and a partially completed scratch state.
''')

ladder('code', r'''
Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.
Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.
Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.
Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.
Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.
Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.
Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.
Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.
Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.
Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.
Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.
Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.
Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.
Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.
Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.
''', r'''
Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.
Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.
Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.
Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.
Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.
Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.
Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.
Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.
Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.
Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.
Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.
Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.
Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.
Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.
Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.
''', r'''
Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.
Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.
Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.
Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.
Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.
Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.
Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.
Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.
Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.
Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.
Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.
Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.
Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.
Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.
Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.
''')

ladder('policy', r'''
Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.
Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.
Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.
Implement a batch review returning one decision per request in original order,including repeated requests.
Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.
Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.
Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.
Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.
Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.
Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.
Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.
Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.
Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.
Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.
Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.
''', r'''
Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.
Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.
Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.
Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.
Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.
Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.
Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.
Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.
For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.
Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.
Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.
Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.
Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.
Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.
Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.
''', r'''
Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.
Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.
Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.
Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.
Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.
Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.
Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.
Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.
Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.
Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.
Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.
Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.
Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.
Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.
Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.
''')

ladder('storage', r'''
Implement the core against an in-memory store and return the supplied example's complete result/state.
Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.
Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.
Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.
Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.
Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.
Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.
Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.
Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.
Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.
Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.
Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.
Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.
Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.
Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.
''', r'''
Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.
Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.
Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.
Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.
Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.
Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.
Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.
Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.
Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.
Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.
Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.
Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.
Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.
For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.
Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.
''', r'''
Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.
Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.
Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.
Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.
Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.
Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.
Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.
Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.
Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.
Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.
Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.
Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.
Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.
Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.
Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.
''')

ladder('workflow', r'''
Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.
Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.
Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.
Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.
Construct an empty-work case and return the documented terminal state with no phantom task execution.
Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.
Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.
Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.
Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.
Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.
Demonstrate that replaying a read-only trace produces the same final status and attempt counts.
Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.
Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.
Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.
Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.
''', r'''
Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.
Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.
Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.
Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.
Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.
Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.
Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.
Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.
Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.
Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.
Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.
Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.
Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.
Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.
Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.
''', r'''
Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.
Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.
Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.
Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.
Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.
Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.
Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.
Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.
Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.
Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.
Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.
Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.
Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.
Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.
Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.
''')

# Async functions use the same scheduling/failure ladder but keep their
# language-specific core and concurrency/cancellation contract.
LADDERS['async'] = LADDERS['workflow']

ladder('api', r'''
Implement the core endpoint/service boundary with injected dependencies and demonstrate the acceptance example's exact status,headers and body.
Handle malformed JSON before business processing. Return400 with code INVALID_JSON and show that no dependency mutation was called.
Validate missing required fields separately from wrong-type fields. Return400 with field paths sorted; preserve the core's valid response contract.
Demonstrate one accepted and one rejected request at the core's exact boundary,including dependency call counts and final state.
Implement a framework-free request-to-response function and show that it produces the same core response as the HTTP adapter.
Return a deterministic structured error body with code,message and request_id. Do not expose stack traces,connection strings or secret request fields.
Add an injected request ID generator used when no valid request ID is supplied. All response/log records for one request must share the same ID.
Handle an unsupported method with405 and an Allow header listing the core's supported method. No business function may run.
Handle an unknown path with404 without accidentally calling a similar-prefix route. Demonstrate a valid and a neighboring invalid route.
Implement a response-contract validator checking status,required headers and body shape. Show one deliberately invalid response it rejects.
Prove rejected requests leave caller input and repository state unchanged. Return snapshots and exact mutation call count.
Add Content-Type validation for a body-bearing endpoint: unsupported types return415 before parsing. For a bodyless endpoint,reject an unexpected body with400 under this explicit adapter contract.
Create table-driven tests for success,validation failure and missing/conflicting resource where applicable. Include exact expected outputs,not only status classes.
Add an in-memory dependency fake retaining invocation order. Return the trace for the acceptance example and verify only necessary calls were made.
Serialize the successful response deterministically,retaining nulls and exact integer representations from the core. Demonstrate that a string amount is not silently accepted as a numeric amount.
''', r'''
Add authenticated tenant context at the service boundary. Reject absent identity with401 and cross-tenant resource access with403 before returning protected data.
Use an explicit idempotency key for state-changing requests. Identical key/body replays the original result; changed body with the same key returns409. For a read-only core,use a versioned conditional-read key instead.
Add an optimistic expected-version precondition to updates or a conditional version header to reads. Stale updates must not overwrite; unchanged conditional reads return304 without a body.
Inject a repository/provider failure and map known transient failures to503 with a safe code. Do not convert a validation error or missing resource into a server failure.
Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.
Enforce an explicit positive request-size/item-count bound before expensive work. Return413 without partial effects at the first disallowed boundary.
Add a unit-of-work adapter for the core's state changes so all required persistent changes commit together. For a read-only endpoint,read related fields from one consistent snapshot.
Create a sanitized audit record correlating request ID,actor,resource,action and outcome. Show failed authorization cannot produce a success audit.
Implement a per-client token bucket in an injected-clock local model: capacity2,refill1 per second. Return429 when empty; a rejected request invokes no business effect.
Add timeout handling distinguishing dependency-known-failure from unknown-effect timeout. A state-changing unknown outcome returns a pending/reconciliation identity instead of blindly retrying.
Build independent HTTP adapter tests and service tests. Demonstrate an adapter-only parsing defect and a service-only invariant defect caught by different tests.
Add API versioning with an unchanged v1 contract and v2 metadata envelope. Reject unsupported versions before touching the repository.
Implement retry guidance only for explicitly retryable outcomes. Replays of accepted state changes must reuse the original idempotency identity.
Add a schema allowlist rejecting unknown write fields such as client-supplied owner/admin/version overrides. Show no mass-assignment change occurs.
Construct a race-prone pair of requests applicable to the core and write a coordinated local test exposing an unsafe implementation without timing sleeps.
''', r'''
Implement concurrent identical idempotent requests so exactly one owns the business effect and others receive the same durable result or a precise pending response.
Handle a crash after an external effect but before response persistence. Reconcile using durable action identity and demonstrate no duplicate charge/change on retry.
Demonstrate authorization revocation between request validation and commit. Enforce a commit-time policy/version precondition so stale authorization cannot finalize protected mutation.
Implement an outbox model committing domain change and event intent together. Repeated event delivery must not duplicate downstream business effects.
Add graceful shutdown: stop accepting new mutations,drain accepted work to an injected deadline and preserve unresolved operation IDs for recovery.
Build generated differential request tests against a simple service reference,including malformed values,tenant boundaries,repeated keys and concurrent versions.
Support a rolling API/schema migration with old and new clients. Demonstrate compatibility before removing an old field or interpretation.
Introduce an explicit circuit-breaker model around a failing dependency. Separate rejected/open/half-open decisions from actual provider calls and test recovery with injected time.
Bound concurrent in-flight dependency work and pending queue length. Reject overload explicitly rather than allowing an unbounded request backlog.
Reconstruct one request's actual effect from ingress log,idempotency record,repository version and event journal. Detect a deliberately inconsistent claimed success.
Demonstrate that matching HTTP status alone does not prove correctness. Seed a wrong amount,wrong tenant or duplicate side effect and catch it with independent postcondition tests.
Add secure cursor/idempotency context binding so a token from tenant A cannot address tenant B's resources. Reject altered or stale context without leaking protected state.
Design a partial-failure batch API with per-item durable identities and explicit atomicity semantics. Show recovery after response delivery fails midway.
Measure actual call counts,queue depth and retained state under slow dependencies. Preserve the contract while adding a tested overload/retry policy.
Deliver the endpoint with exact request/response contract,independent expected outputs,authorization,idempotency,concurrency and one full crash/reconciliation trace.
''')

ladder('data', r'''
Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.
Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.
Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.
Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.
Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.
Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.
Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.
Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.
Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.
Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.
Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.
Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.
Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.
Implement a small independent reference transformation and compare full output records with the main implementation.
Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.
''', r'''
Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.
Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.
Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.
Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.
Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.
Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.
Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.
Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.
Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.
Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.
Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.
Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.
Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.
Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.
Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.
''', r'''
Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.
Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.
Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.
Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.
Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.
Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.
Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.
Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.
Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.
Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.
Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.
Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.
Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.
Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.
Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.
''')

ladder('config', r'''
Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.
Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.
Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.
Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.
Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.
Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.
Validate two independent configuration objects in one batch and return findings by original index without merging their settings.
Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.
Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.
Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.
Implement explicit defaults only for optional fields; return which effective values came from defaults.
Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.
Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.
Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.
Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.
''', r'''
Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.
Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.
Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.
Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.
Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.
Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.
Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.
Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.
Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.
Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.
Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.
Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.
Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.
Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.
Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.
''', r'''
Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.
Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.
Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.
Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.
Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.
Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.
Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.
Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.
Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.
Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.
Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.
Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.
Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.
Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.
Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.
''')

ladder('monitoring', r'''
Implement the core calculation on the supplied local inputs and return exact metric/finding outputs.
Run an empty observation period and preserve the core's distinction between zero,missing and unknown.
Implement half-open window assignment with injected timestamps. Show an event exactly at start and exactly at end.
Return a per-input contribution trace so the final counts/totals can be recomputed independently.
Validate observation fields and return rejected indices; malformed values must not become zero-valued measurements.
Sort the report by its declared group/time keys and return deterministic output for reordered input where order has no business meaning.
Return both numerator and denominator for every ratio in the core. If there is no ratio,return contributing record count alongside each total.
Create a summary report reconciling group totals/counts to the global result without double-counting rejected records.
Demonstrate the exact equality boundary of the core's threshold. Show why greater-than and greater-than-or-equal yield different decisions.
Return a finding explanation containing only safe identifiers,rule name and measured value; exclude secret payloads.
Implement a one-period-at-a-time evaluator and compare its result with batch evaluation on the baseline.
Create a no-side-effect preview of findings/alerts without invoking any notification channel.
Retain original observation IDs in diagnostics so a reported anomaly can be traced to source evidence.
Produce an NDJSON report with a schema version and exact integer amounts where applicable.
Build an acceptance table with expected and actual findings for normal,empty and boundary inputs.
''', r'''
Deduplicate identical observation IDs and reject conflicting duplicate payloads. Compare counts before and after deduplication.
Implement incremental state across observation batches and prove concatenated-batch results equal one complete batch under the core's ordering rules.
Add hysteresis for alerts: fire using the core rule and resolve after two consecutive known good periods. Missing data cannot count as good.
Add per-group state so a problem in service/tenant A cannot advance the alarm streak for B.
Introduce out-of-order observations and a supplied watermark. Recompute open windows; emit corrections rather than silently altering a finalized report.
Use exact rational comparison for rate thresholds,avoiding an unnecessary floating-point boundary error. Return numerator,denominator and decision.
Add a notification deduplication key based on rule,group and transition sequence. Repeated report delivery cannot create a second identical alert intent.
Implement a configurable threshold with validated type/range and version it in every finding.
Compare two observation snapshots and classify new,resolved and unchanged findings by stable identity.
Add per-group quality counts for missing and invalid data. Do not hide a missing-data incident behind a zero failure rate.
Build a baseline/actual comparison for signed integer costs or counts. Reconcile adjustments and flag complete-record differences even when grand totals match.
Introduce a deterministic notification mock that fails once. Preserve pending alert state and retry without creating a new transition.
Bound retained state by finalized window plus explicitly configured lateness. Demonstrate which observations become TOO_LATE.
Produce a safe audit report mapping every sent notification to an actual computed transition and its rule version.
Construct an adversarial observation sequence that exposes a threshold,window,duplicate or missing-data shortcut and demonstrate the corrected result.
''', r'''
Implement restartable evaluator state and durable alert-intent publication. Inject a crash around both checkpoints and prove transitions are neither lost nor repeatedly published.
Model two evaluator replicas consuming overlapping data. Use versioned ownership/fencing so only one publishes a transition for each group/window.
Handle late corrections to already published metrics with revisioned reports and explicit corrective notifications rather than rewriting audit history.
Implement a bounded-memory merge of large sorted observation streams and compare final findings with the simple batch reference on small fixtures.
Build differential generated tests for threshold boundaries,missing periods,out-of-order events,duplicate IDs and signed adjustments applicable to the core.
Separate data freshness failure from measured-service failure. Demonstrate a stale feed that must not be reported as a healthy zero-error service.
Add rule-version rollout with historical replay. Show exactly which findings change because of rule changes rather than changed observations.
Implement tenant-isolated state and fair bounded processing so one noisy tenant cannot corrupt or indefinitely block another tenant's reports.
Reconstruct an incident from raw observation IDs,rule versions,state checkpoints and notification journal. Detect one deliberately missing notification or phantom finding.
Model ambiguous notification acknowledgment. Reconcile by durable notification key and retain UNKNOWN if the receiver cannot confirm its effect.
Add a conservation checker independent of the metric implementation. Detect a dropped input,double contribution and mismatched allocation bucket.
Measure actual update work and retained state under skewed groups and late-event bursts. Preserve correctness and provide evidence for a bounded-state design.
Implement a safe export with irreversible redaction of secret fields and stable pseudonymous identifiers where needed for correlation.
Design a backfill replay that cannot page operators with historical alerts unless explicitly requested. Retain separate replay/run identities in the journal.
Deliver the evaluator with exact calculations,quality signals,late corrections,durable transitions,notification recovery and an independently checked incident trace.
''')

ladder('frontend', r'''
Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.
Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.
Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.
Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.
Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.
Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.
Return a pure state-transition function underlying the UI and show a table of input events and resulting state.
Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.
Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.
Implement a deterministic empty state with no phantom selectable/submittable record.
Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.
Create a minimal interaction test for the baseline showing expected and actual rendered state.
Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.
Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.
Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.
''', r'''
Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.
Inject a failed request,show an accessible error and support retry without retaining a stale success state.
Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.
Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.
Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.
Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.
Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.
Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.
Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.
Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.
Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.
Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.
Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.
Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.
Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.
''', r'''
Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.
Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.
Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.
Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.
Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.
Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.
Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.
Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.
Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.
Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.
Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.
Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.
Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.
Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.
Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.
''')

ladder('design', r'''
Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.
Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.
List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.
Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.
Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.
Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.
Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.
Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.
Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.
Return the core's dependency/resource graph and validate every referenced node exists.
Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.
Produce a dry-run plan describing observable actions with no external mutation calls.
Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.
Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.
Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.
''', r'''
Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.
Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.
Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.
Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.
Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.
Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.
Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.
Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.
Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.
Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.
Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.
Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.
Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.
Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.
Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.
''', r'''
Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.
Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.
Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.
Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.
Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.
Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.
Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.
Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.
Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.
Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.
Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.
Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.
Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.
Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.
Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.
''')
