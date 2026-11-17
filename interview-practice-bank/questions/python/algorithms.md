# Python: Algorithms

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Python; language-level code with injected I/O where needed.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Sorting and binary search

### Beginner

#### PY-ALGORITHMS-01-B01

**Core:** Implement lower_bound(sorted,target): first index value>=target,or length. Integers ascending; logarithmic comparisons.

**Acceptance example / fixture:** [1,2,2,5],2 -> 1.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B02

**Core:** Implement upper_bound(sorted,target): first index value>target,or length. Integers ascending; logarithmic comparisons.

**Acceptance example / fixture:** [1,2,2,5],2 -> 3.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B03

**Core:** Return first/last target positions in an ascending integer list,or null if absent,using logarithmic search.

**Acceptance example / fixture:** [1,2,2,5],2 -> [1,2].

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B04

**Core:** Implement insertion_index for descending integers: first index value<=target. Preserve earlier strictly larger values.

**Acceptance example / fixture:** [9,7,7,2],7 -> 1.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B05

**Core:** Search a rotated ascending distinct integer list,return original index or null. Do not reconstruct/sort the list.

**Acceptance example / fixture:** [4,5,1,2,3],2 -> 3.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B06

**Core:** Find the minimum in a nonempty rotated ascending distinct integer list using logarithmic comparisons.

**Acceptance example / fixture:** [4,5,1,2,3] -> 1.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B07

**Core:** Find kth smallest integer in two ascending lists,one-based k,without sorting the combined lists. Invalid k -> INVALID.

**Acceptance example / fixture:** [1,3],[2,4],3 -> 3.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B08

**Core:** Implement stable order sort: amount descending,null last,id ascending; IDs unique. Do not mutate input.

**Acceptance example / fixture:** b:200,a:200,c:null -> [a,b,c].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B09

**Core:** Return the three smallest distinct values with their full multiplicities from unsorted integers; fewer than3 distinct means all distinct.

**Acceptance example / fixture:** [5,1,2,1,4] -> [(1,2),(2,1),(4,1)].

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B10

**Core:** Implement integer_sqrt(n) for nonnegative integers: largest x with x*x<=n. Use no floating sqrt and reject negative input.

**Acceptance example / fixture:** 15 -> 3; 16 -> 4.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B11

**Core:** Given sorted nonoverlapping inclusive intervals,find the interval containing point or null using logarithmic search.

**Acceptance example / fixture:** [[1,3],[5,8]],5 -> [5,8].

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B12

**Core:** Given monotone predicate false then true over indices0..n-1,find first true or null with bounded predicate calls. Do not call outside range.

**Acceptance example / fixture:** [false,false,true,true] -> 2.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B13

**Core:** Find the smallest positive capacity allowing ordered positive jobs to be split into at most d contiguous groups,each sum<=capacity.

**Acceptance example / fixture:** jobs[3,2,2],d2 -> 4.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B14

**Core:** Return count of sorted integers in half-open [low,high) using two bounds; low>high -> INVALID.

**Acceptance example / fixture:** [1,2,2,3],2,3 -> 2.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-01-B15

**Core:** Merge k ascending streams using a heap,retaining duplicates and returning ascending output. Never materialize all streams before the first output.

**Acceptance example / fixture:** [1,4],[1,3],[] -> [1,1,3,4].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-ALGORITHMS-01-I01

**Core:** Implement lower_bound(sorted,target): first index value>=target,or length. Integers ascending; logarithmic comparisons.

**Acceptance example / fixture:** [1,2,2,5],2 -> 1.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I02

**Core:** Implement upper_bound(sorted,target): first index value>target,or length. Integers ascending; logarithmic comparisons.

**Acceptance example / fixture:** [1,2,2,5],2 -> 3.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I03

**Core:** Return first/last target positions in an ascending integer list,or null if absent,using logarithmic search.

**Acceptance example / fixture:** [1,2,2,5],2 -> [1,2].

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I04

**Core:** Implement insertion_index for descending integers: first index value<=target. Preserve earlier strictly larger values.

**Acceptance example / fixture:** [9,7,7,2],7 -> 1.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I05

**Core:** Search a rotated ascending distinct integer list,return original index or null. Do not reconstruct/sort the list.

**Acceptance example / fixture:** [4,5,1,2,3],2 -> 3.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I06

**Core:** Find the minimum in a nonempty rotated ascending distinct integer list using logarithmic comparisons.

**Acceptance example / fixture:** [4,5,1,2,3] -> 1.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I07

**Core:** Find kth smallest integer in two ascending lists,one-based k,without sorting the combined lists. Invalid k -> INVALID.

**Acceptance example / fixture:** [1,3],[2,4],3 -> 3.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I08

**Core:** Implement stable order sort: amount descending,null last,id ascending; IDs unique. Do not mutate input.

**Acceptance example / fixture:** b:200,a:200,c:null -> [a,b,c].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I09

**Core:** Return the three smallest distinct values with their full multiplicities from unsorted integers; fewer than3 distinct means all distinct.

**Acceptance example / fixture:** [5,1,2,1,4] -> [(1,2),(2,1),(4,1)].

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I10

**Core:** Implement integer_sqrt(n) for nonnegative integers: largest x with x*x<=n. Use no floating sqrt and reject negative input.

**Acceptance example / fixture:** 15 -> 3; 16 -> 4.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I11

**Core:** Given sorted nonoverlapping inclusive intervals,find the interval containing point or null using logarithmic search.

**Acceptance example / fixture:** [[1,3],[5,8]],5 -> [5,8].

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I12

**Core:** Given monotone predicate false then true over indices0..n-1,find first true or null with bounded predicate calls. Do not call outside range.

**Acceptance example / fixture:** [false,false,true,true] -> 2.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I13

**Core:** Find the smallest positive capacity allowing ordered positive jobs to be split into at most d contiguous groups,each sum<=capacity.

**Acceptance example / fixture:** jobs[3,2,2],d2 -> 4.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I14

**Core:** Return count of sorted integers in half-open [low,high) using two bounds; low>high -> INVALID.

**Acceptance example / fixture:** [1,2,2,3],2,3 -> 2.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-01-I15

**Core:** Merge k ascending streams using a heap,retaining duplicates and returning ascending output. Never materialize all streams before the first output.

**Acceptance example / fixture:** [1,4],[1,3],[] -> [1,1,3,4].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-ALGORITHMS-01-A01

**Core:** Implement lower_bound(sorted,target): first index value>=target,or length. Integers ascending; logarithmic comparisons.

**Acceptance example / fixture:** [1,2,2,5],2 -> 1.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A02

**Core:** Implement upper_bound(sorted,target): first index value>target,or length. Integers ascending; logarithmic comparisons.

**Acceptance example / fixture:** [1,2,2,5],2 -> 3.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A03

**Core:** Return first/last target positions in an ascending integer list,or null if absent,using logarithmic search.

**Acceptance example / fixture:** [1,2,2,5],2 -> [1,2].

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A04

**Core:** Implement insertion_index for descending integers: first index value<=target. Preserve earlier strictly larger values.

**Acceptance example / fixture:** [9,7,7,2],7 -> 1.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A05

**Core:** Search a rotated ascending distinct integer list,return original index or null. Do not reconstruct/sort the list.

**Acceptance example / fixture:** [4,5,1,2,3],2 -> 3.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A06

**Core:** Find the minimum in a nonempty rotated ascending distinct integer list using logarithmic comparisons.

**Acceptance example / fixture:** [4,5,1,2,3] -> 1.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A07

**Core:** Find kth smallest integer in two ascending lists,one-based k,without sorting the combined lists. Invalid k -> INVALID.

**Acceptance example / fixture:** [1,3],[2,4],3 -> 3.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A08

**Core:** Implement stable order sort: amount descending,null last,id ascending; IDs unique. Do not mutate input.

**Acceptance example / fixture:** b:200,a:200,c:null -> [a,b,c].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A09

**Core:** Return the three smallest distinct values with their full multiplicities from unsorted integers; fewer than3 distinct means all distinct.

**Acceptance example / fixture:** [5,1,2,1,4] -> [(1,2),(2,1),(4,1)].

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A10

**Core:** Implement integer_sqrt(n) for nonnegative integers: largest x with x*x<=n. Use no floating sqrt and reject negative input.

**Acceptance example / fixture:** 15 -> 3; 16 -> 4.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A11

**Core:** Given sorted nonoverlapping inclusive intervals,find the interval containing point or null using logarithmic search.

**Acceptance example / fixture:** [[1,3],[5,8]],5 -> [5,8].

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A12

**Core:** Given monotone predicate false then true over indices0..n-1,find first true or null with bounded predicate calls. Do not call outside range.

**Acceptance example / fixture:** [false,false,true,true] -> 2.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A13

**Core:** Find the smallest positive capacity allowing ordered positive jobs to be split into at most d contiguous groups,each sum<=capacity.

**Acceptance example / fixture:** jobs[3,2,2],d2 -> 4.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A14

**Core:** Return count of sorted integers in half-open [low,high) using two bounds; low>high -> INVALID.

**Acceptance example / fixture:** [1,2,2,3],2,3 -> 2.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-01-A15

**Core:** Merge k ascending streams using a heap,retaining duplicates and returning ascending output. Never materialize all streams before the first output.

**Acceptance example / fixture:** [1,4],[1,3],[] -> [1,1,3,4].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Two pointers and sliding windows

### Beginner

#### PY-ALGORITHMS-02-B01

**Core:** Return length of longest substring with no repeated Unicode code point; empty text ->0.

**Acceptance example / fixture:** abba ->2.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B02

**Core:** Return largest sum of any exactly k consecutive integers,k positive and<=length. Ties return earliest start with sum.

**Acceptance example / fixture:** [1,4,-1,3],k2 ->sum5,start0.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B03

**Core:** For positive integers and positive target,return shortest contiguous length with sum>=target or0 if absent.

**Acceptance example / fixture:** [2,3,1,2,4,3],7 ->2.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B04

**Core:** Return number of distinct values in every contiguous window of positive length k;k>length ->[].

**Acceptance example / fixture:** [a,b,a,c],3 ->[2,3].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B05

**Core:** Return longest substring length with at most k distinct Unicode code points,k>=0.

**Acceptance example / fixture:** eceba,k2 ->3.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B06

**Core:** Return longest contiguous integer-array length containing at most k zeros; every value must be0 or1.

**Acceptance example / fixture:** [1,0,1,0,1],k1 ->3.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B07

**Core:** Return whether sorted integer input contains a distinct-index pair summing to target using two pointers.

**Acceptance example / fixture:** [1,2,4,5],6 ->true.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B08

**Core:** Remove duplicates from a sorted integer array into a new array,allowing each value at most2 times. Preserve order.

**Acceptance example / fixture:** [1,1,1,2,2,3] ->[1,1,2,2,3].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B09

**Core:** Return all unique value triplets summing to0,each triplet ascending,triplets lexicographically sorted. Use distinct original positions.

**Acceptance example / fixture:** [-1,0,1,2,-1,-4] ->[[-1,-1,2],[-1,0,1]].

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B10

**Core:** Return maximum water area for nonnegative integer heights: area=(j-i)*min(height_i,height_j);<2 bars ->0.

**Acceptance example / fixture:** [1,8,6,2,5,4,8,3,7] ->49.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B11

**Core:** Return sorted squares from an ascending signed-integer array without sorting all output afterward.

**Acceptance example / fixture:** [-4,-1,0,3] ->[0,1,9,16].

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B12

**Core:** Return shortest substring covering all required code-point multiplicities,ties earliest;no match ->null,empty required ->empty.

**Acceptance example / fixture:** ADOBECODEBANC,ABC ->BANC.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B13

**Core:** Return all zero-based start indices where an anagram of a nonempty pattern occurs in lowercase ASCII text.

**Acceptance example / fixture:** cbaebabacd,abc ->[0,6].

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B14

**Core:** Return length of longest substring that can become one repeated uppercase ASCII letter by replacing at most k characters.

**Acceptance example / fixture:** AABABBA,k1 ->4.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-02-B15

**Core:** Return count of contiguous subarrays of positive integers with product<positive target. Target<=1 yields0; use exact arithmetic.

**Acceptance example / fixture:** [10,5,2,6],100 ->8.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-ALGORITHMS-02-I01

**Core:** Return length of longest substring with no repeated Unicode code point; empty text ->0.

**Acceptance example / fixture:** abba ->2.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I02

**Core:** Return largest sum of any exactly k consecutive integers,k positive and<=length. Ties return earliest start with sum.

**Acceptance example / fixture:** [1,4,-1,3],k2 ->sum5,start0.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I03

**Core:** For positive integers and positive target,return shortest contiguous length with sum>=target or0 if absent.

**Acceptance example / fixture:** [2,3,1,2,4,3],7 ->2.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I04

**Core:** Return number of distinct values in every contiguous window of positive length k;k>length ->[].

**Acceptance example / fixture:** [a,b,a,c],3 ->[2,3].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I05

**Core:** Return longest substring length with at most k distinct Unicode code points,k>=0.

**Acceptance example / fixture:** eceba,k2 ->3.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I06

**Core:** Return longest contiguous integer-array length containing at most k zeros; every value must be0 or1.

**Acceptance example / fixture:** [1,0,1,0,1],k1 ->3.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I07

**Core:** Return whether sorted integer input contains a distinct-index pair summing to target using two pointers.

**Acceptance example / fixture:** [1,2,4,5],6 ->true.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I08

**Core:** Remove duplicates from a sorted integer array into a new array,allowing each value at most2 times. Preserve order.

**Acceptance example / fixture:** [1,1,1,2,2,3] ->[1,1,2,2,3].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I09

**Core:** Return all unique value triplets summing to0,each triplet ascending,triplets lexicographically sorted. Use distinct original positions.

**Acceptance example / fixture:** [-1,0,1,2,-1,-4] ->[[-1,-1,2],[-1,0,1]].

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I10

**Core:** Return maximum water area for nonnegative integer heights: area=(j-i)*min(height_i,height_j);<2 bars ->0.

**Acceptance example / fixture:** [1,8,6,2,5,4,8,3,7] ->49.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I11

**Core:** Return sorted squares from an ascending signed-integer array without sorting all output afterward.

**Acceptance example / fixture:** [-4,-1,0,3] ->[0,1,9,16].

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I12

**Core:** Return shortest substring covering all required code-point multiplicities,ties earliest;no match ->null,empty required ->empty.

**Acceptance example / fixture:** ADOBECODEBANC,ABC ->BANC.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I13

**Core:** Return all zero-based start indices where an anagram of a nonempty pattern occurs in lowercase ASCII text.

**Acceptance example / fixture:** cbaebabacd,abc ->[0,6].

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I14

**Core:** Return length of longest substring that can become one repeated uppercase ASCII letter by replacing at most k characters.

**Acceptance example / fixture:** AABABBA,k1 ->4.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-02-I15

**Core:** Return count of contiguous subarrays of positive integers with product<positive target. Target<=1 yields0; use exact arithmetic.

**Acceptance example / fixture:** [10,5,2,6],100 ->8.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-ALGORITHMS-02-A01

**Core:** Return length of longest substring with no repeated Unicode code point; empty text ->0.

**Acceptance example / fixture:** abba ->2.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A02

**Core:** Return largest sum of any exactly k consecutive integers,k positive and<=length. Ties return earliest start with sum.

**Acceptance example / fixture:** [1,4,-1,3],k2 ->sum5,start0.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A03

**Core:** For positive integers and positive target,return shortest contiguous length with sum>=target or0 if absent.

**Acceptance example / fixture:** [2,3,1,2,4,3],7 ->2.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A04

**Core:** Return number of distinct values in every contiguous window of positive length k;k>length ->[].

**Acceptance example / fixture:** [a,b,a,c],3 ->[2,3].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A05

**Core:** Return longest substring length with at most k distinct Unicode code points,k>=0.

**Acceptance example / fixture:** eceba,k2 ->3.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A06

**Core:** Return longest contiguous integer-array length containing at most k zeros; every value must be0 or1.

**Acceptance example / fixture:** [1,0,1,0,1],k1 ->3.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A07

**Core:** Return whether sorted integer input contains a distinct-index pair summing to target using two pointers.

**Acceptance example / fixture:** [1,2,4,5],6 ->true.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A08

**Core:** Remove duplicates from a sorted integer array into a new array,allowing each value at most2 times. Preserve order.

**Acceptance example / fixture:** [1,1,1,2,2,3] ->[1,1,2,2,3].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A09

**Core:** Return all unique value triplets summing to0,each triplet ascending,triplets lexicographically sorted. Use distinct original positions.

**Acceptance example / fixture:** [-1,0,1,2,-1,-4] ->[[-1,-1,2],[-1,0,1]].

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A10

**Core:** Return maximum water area for nonnegative integer heights: area=(j-i)*min(height_i,height_j);<2 bars ->0.

**Acceptance example / fixture:** [1,8,6,2,5,4,8,3,7] ->49.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A11

**Core:** Return sorted squares from an ascending signed-integer array without sorting all output afterward.

**Acceptance example / fixture:** [-4,-1,0,3] ->[0,1,9,16].

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A12

**Core:** Return shortest substring covering all required code-point multiplicities,ties earliest;no match ->null,empty required ->empty.

**Acceptance example / fixture:** ADOBECODEBANC,ABC ->BANC.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A13

**Core:** Return all zero-based start indices where an anagram of a nonempty pattern occurs in lowercase ASCII text.

**Acceptance example / fixture:** cbaebabacd,abc ->[0,6].

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A14

**Core:** Return length of longest substring that can become one repeated uppercase ASCII letter by replacing at most k characters.

**Acceptance example / fixture:** AABABBA,k1 ->4.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-02-A15

**Core:** Return count of contiguous subarrays of positive integers with product<positive target. Target<=1 yields0; use exact arithmetic.

**Acceptance example / fixture:** [10,5,2,6],100 ->8.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Recursion and graphs

### Beginner

#### PY-ALGORITHMS-03-B01

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B02

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B03

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B04

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B05

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B06

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B07

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B08

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B09

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B10

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B11

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B12

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B13

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B14

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-ALGORITHMS-03-B15

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-ALGORITHMS-03-I01

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I02

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I03

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I04

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I05

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I06

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I07

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I08

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I09

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I10

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I11

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I12

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I13

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I14

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-ALGORITHMS-03-I15

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-ALGORITHMS-03-A01

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A02

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A03

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A04

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A05

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A06

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A07

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A08

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A09

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A10

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A11

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A12

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A13

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A14

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-ALGORITHMS-03-A15

**Core:** Implement dependency_order(nodes,edges), where [a,b] means a must finish before b. Return the lexicographically smallest valid topological ordering, or CYCLE. Reject edges referencing absent nodes as INVALID.

**Acceptance example / fixture:** nodes=[a,b,c], edges=[[a,c],[b,c]] -> [a,b,c].

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
