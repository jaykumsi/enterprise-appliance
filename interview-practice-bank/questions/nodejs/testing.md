# Full Stack Developer - NodeJs: Testing

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Tests fakes and deterministic time

### Beginner

#### NODE-TESTING-01-B01

**Core:** Reconcile unique-id integer balances,returning missing,extra and changed entries sorted by id. Duplicate IDs -> INVALID.

**Acceptance example / fixture:** expected a:0,b:2;actual b:3 -> missinga,changedb.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B02

**Core:** Compare multisets of complete rows,including nulls; return each distinct row's expected/actual multiplicity when unequal.

**Acceptance example / fixture:** expected[a,a],actual[a] -> a counts2,1.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B03

**Core:** Compare two ordered sequences and return first differing zero-based index or null; a missing trailing element differs from null value.

**Acceptance example / fixture:** [a,null],[a] -> index1.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B04

**Core:** Reconcile versions per id: missing,extra,stale,newer and same-version-conflicting payloads. Exact match produces no finding.

**Acceptance example / fixture:** a:v2/x vs a:v1/x -> stalea.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B05

**Core:** Verify a total by independently summing signed ledger entries; return computed,claimed and delta. Use exact integers.

**Acceptance example / fixture:** entries[5,-2],claimed4 -> computed3,delta-1.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B06

**Core:** Check a partition's accepted/rejected lineage covers each input position exactly once. Return missing,double-covered and unknown positions.

**Acceptance example / fixture:** input0..2,accepted[0,1],rejected[1] -> missing2,double1.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B07

**Core:** Reconcile a left join's source IDs: each source must appear once,including unmatched rows. Return multiplied and missing source IDs.

**Acceptance example / fixture:** source[a,b],output[a,a] -> multiplieda,missingb.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B08

**Core:** Compare schemas by name,type,nullability and column order; return structural changes separately from reorders.

**Acceptance example / fixture:** [id:int,note:text] vs reversed -> reorder only.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B09

**Core:** Validate a transition trace against allowed edges and increasing sequence numbers. Return first impossible transition or numbering gap.

**Acceptance example / fixture:** Open->Paid->Open -> invalid second transition.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B10

**Core:** Check sorted output with explicit nulls-last,amount-descending,id-ascending rules. Return first adjacent violating pair.

**Acceptance example / fixture:** a:100,b:200 -> violation0,1.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B11

**Core:** Reconcile parent/child references,returning orphan child IDs and unused parent IDs separately,sorted.

**Acceptance example / fixture:** parents[a,b],children[x->a,y->c] -> orphan[y],unused[b].

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B12

**Core:** Compare a cached response to authoritative revision. Return FRESH only if key,tenant and revision all match; else named mismatches.

**Acceptance example / fixture:** same key and revision,wrong tenant -> tenant mismatch.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B13

**Core:** Verify allocation conservation: shares must be integers>=0,sum equal total,and optional weights list length match. Return all invariant failures.

**Acceptance example / fixture:** total10,shares[4,3,2] -> sum failure.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B14

**Core:** Compare source/sink manifests by path and checksum; distinguish missing,extra and changed content despite matching file counts.

**Acceptance example / fixture:** source a/x,b/y;sink a/x,c/y -> missingb,extrac.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-TESTING-01-B15

**Core:** Implement a test-case reducer for a supplied deterministic predicate fails(list). Repeatedly remove one item left-to-right if failure remains until no single removal works; return locally minimal list.

**Acceptance example / fixture:** Failure when both a,b present;[x,a,y,b] -> [a,b].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-TESTING-01-I01

**Core:** Reconcile unique-id integer balances,returning missing,extra and changed entries sorted by id. Duplicate IDs -> INVALID.

**Acceptance example / fixture:** expected a:0,b:2;actual b:3 -> missinga,changedb.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I02

**Core:** Compare multisets of complete rows,including nulls; return each distinct row's expected/actual multiplicity when unequal.

**Acceptance example / fixture:** expected[a,a],actual[a] -> a counts2,1.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I03

**Core:** Compare two ordered sequences and return first differing zero-based index or null; a missing trailing element differs from null value.

**Acceptance example / fixture:** [a,null],[a] -> index1.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I04

**Core:** Reconcile versions per id: missing,extra,stale,newer and same-version-conflicting payloads. Exact match produces no finding.

**Acceptance example / fixture:** a:v2/x vs a:v1/x -> stalea.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I05

**Core:** Verify a total by independently summing signed ledger entries; return computed,claimed and delta. Use exact integers.

**Acceptance example / fixture:** entries[5,-2],claimed4 -> computed3,delta-1.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I06

**Core:** Check a partition's accepted/rejected lineage covers each input position exactly once. Return missing,double-covered and unknown positions.

**Acceptance example / fixture:** input0..2,accepted[0,1],rejected[1] -> missing2,double1.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I07

**Core:** Reconcile a left join's source IDs: each source must appear once,including unmatched rows. Return multiplied and missing source IDs.

**Acceptance example / fixture:** source[a,b],output[a,a] -> multiplieda,missingb.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I08

**Core:** Compare schemas by name,type,nullability and column order; return structural changes separately from reorders.

**Acceptance example / fixture:** [id:int,note:text] vs reversed -> reorder only.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I09

**Core:** Validate a transition trace against allowed edges and increasing sequence numbers. Return first impossible transition or numbering gap.

**Acceptance example / fixture:** Open->Paid->Open -> invalid second transition.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I10

**Core:** Check sorted output with explicit nulls-last,amount-descending,id-ascending rules. Return first adjacent violating pair.

**Acceptance example / fixture:** a:100,b:200 -> violation0,1.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I11

**Core:** Reconcile parent/child references,returning orphan child IDs and unused parent IDs separately,sorted.

**Acceptance example / fixture:** parents[a,b],children[x->a,y->c] -> orphan[y],unused[b].

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I12

**Core:** Compare a cached response to authoritative revision. Return FRESH only if key,tenant and revision all match; else named mismatches.

**Acceptance example / fixture:** same key and revision,wrong tenant -> tenant mismatch.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I13

**Core:** Verify allocation conservation: shares must be integers>=0,sum equal total,and optional weights list length match. Return all invariant failures.

**Acceptance example / fixture:** total10,shares[4,3,2] -> sum failure.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I14

**Core:** Compare source/sink manifests by path and checksum; distinguish missing,extra and changed content despite matching file counts.

**Acceptance example / fixture:** source a/x,b/y;sink a/x,c/y -> missingb,extrac.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-TESTING-01-I15

**Core:** Implement a test-case reducer for a supplied deterministic predicate fails(list). Repeatedly remove one item left-to-right if failure remains until no single removal works; return locally minimal list.

**Acceptance example / fixture:** Failure when both a,b present;[x,a,y,b] -> [a,b].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-TESTING-01-A01

**Core:** Reconcile unique-id integer balances,returning missing,extra and changed entries sorted by id. Duplicate IDs -> INVALID.

**Acceptance example / fixture:** expected a:0,b:2;actual b:3 -> missinga,changedb.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A02

**Core:** Compare multisets of complete rows,including nulls; return each distinct row's expected/actual multiplicity when unequal.

**Acceptance example / fixture:** expected[a,a],actual[a] -> a counts2,1.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A03

**Core:** Compare two ordered sequences and return first differing zero-based index or null; a missing trailing element differs from null value.

**Acceptance example / fixture:** [a,null],[a] -> index1.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A04

**Core:** Reconcile versions per id: missing,extra,stale,newer and same-version-conflicting payloads. Exact match produces no finding.

**Acceptance example / fixture:** a:v2/x vs a:v1/x -> stalea.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A05

**Core:** Verify a total by independently summing signed ledger entries; return computed,claimed and delta. Use exact integers.

**Acceptance example / fixture:** entries[5,-2],claimed4 -> computed3,delta-1.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A06

**Core:** Check a partition's accepted/rejected lineage covers each input position exactly once. Return missing,double-covered and unknown positions.

**Acceptance example / fixture:** input0..2,accepted[0,1],rejected[1] -> missing2,double1.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A07

**Core:** Reconcile a left join's source IDs: each source must appear once,including unmatched rows. Return multiplied and missing source IDs.

**Acceptance example / fixture:** source[a,b],output[a,a] -> multiplieda,missingb.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A08

**Core:** Compare schemas by name,type,nullability and column order; return structural changes separately from reorders.

**Acceptance example / fixture:** [id:int,note:text] vs reversed -> reorder only.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A09

**Core:** Validate a transition trace against allowed edges and increasing sequence numbers. Return first impossible transition or numbering gap.

**Acceptance example / fixture:** Open->Paid->Open -> invalid second transition.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A10

**Core:** Check sorted output with explicit nulls-last,amount-descending,id-ascending rules. Return first adjacent violating pair.

**Acceptance example / fixture:** a:100,b:200 -> violation0,1.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A11

**Core:** Reconcile parent/child references,returning orphan child IDs and unused parent IDs separately,sorted.

**Acceptance example / fixture:** parents[a,b],children[x->a,y->c] -> orphan[y],unused[b].

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A12

**Core:** Compare a cached response to authoritative revision. Return FRESH only if key,tenant and revision all match; else named mismatches.

**Acceptance example / fixture:** same key and revision,wrong tenant -> tenant mismatch.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A13

**Core:** Verify allocation conservation: shares must be integers>=0,sum equal total,and optional weights list length match. Return all invariant failures.

**Acceptance example / fixture:** total10,shares[4,3,2] -> sum failure.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A14

**Core:** Compare source/sink manifests by path and checksum; distinguish missing,extra and changed content despite matching file counts.

**Acceptance example / fixture:** source a/x,b/y;sink a/x,c/y -> missingb,extrac.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-TESTING-01-A15

**Core:** Implement a test-case reducer for a supplied deterministic predicate fails(list). Repeatedly remove one item left-to-right if failure remains until no single removal works; return locally minimal list.

**Acceptance example / fixture:** Failure when both a,b present;[x,a,y,b] -> [a,b].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
