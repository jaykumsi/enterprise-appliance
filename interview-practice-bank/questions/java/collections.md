# Full Stack Developer - Java: Collections

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Lists and comparators

### Beginner

#### JAVA-COLLECTIONS-01-B01

**Core:** Implement merge_intervals for half-open integer intervals. Ignore empty intervals,merge overlap/touch,reject start>end,sort ascending.

**Acceptance example / fixture:** [[5,8],[1,3],[3,6]] -> [[1,8]].

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B02

**Core:** Implement rotate_right(values,k) for nonnegative integer k,without mutating input. Empty list remains empty.

**Acceptance example / fixture:** [1,2,3],4 -> [3,1,2].

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B03

**Core:** Implement stable_partition(values,pivot): values<pivot first,then equal,then greater,each group retaining input order.

**Acceptance example / fixture:** [3,1,2,1],2 -> [1,1,2,3].

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B04

**Core:** Implement move_zeros(values),moving numeric zeros to the end and retaining other element order. Return a new integer list.

**Acceptance example / fixture:** [0,2,0,1] -> [2,1,0,0].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B05

**Core:** Implement intersect_multiset(a,b),retaining each integer min(count_a,count_b) times,output ascending.

**Acceptance example / fixture:** [2,1,2],[2,2,3] -> [2,2].

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B06

**Core:** Implement merge_sorted(a,b),retaining all duplicates and ascending order without sorting the concatenation.

**Acceptance example / fixture:** [1,3],[1,2] -> [1,1,2,3].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B07

**Core:** Implement missing_ranges(sorted_distinct,low,high) returning inclusive missing intervals within inclusive bounds.

**Acceptance example / fixture:** [1,3,7],1,8 -> [[2,2],[4,6],[8,8]].

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B08

**Core:** Implement transpose(matrix). Require rectangular rows; [] -> []; ragged input -> INVALID. Output rows must not alias input rows.

**Acceptance example / fixture:** [[1,2],[3,4]] -> [[1,3],[2,4]].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B09

**Core:** Implement flatten_one(values) where each element is either integer or list of integers; flatten exactly one level and reject deeper nesting.

**Acceptance example / fixture:** [1,[2,3],[]] -> [1,2,3].

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B10

**Core:** Implement maximum_subarray(values) returning sum,start,end for nonempty integer input. End exclusive; ties prefer smallest start then smallest end.

**Acceptance example / fixture:** [-2,3,-1,3] -> {sum:5,start:1,end:4}.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B11

**Core:** Implement product_except_self(values) for integers,using no division. Return products of all other positions; empty -> []; one item -> [1].

**Acceptance example / fixture:** [1,2,3] -> [6,3,2]; [0,2,0] -> [0,0,0].

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B12

**Core:** Implement deduplicate_sorted(values) returning unique ascending integers plus original multiplicities,without mutating input.

**Acceptance example / fixture:** [1,1,2,2,2] -> values[1,2],counts[2,3].

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B13

**Core:** Implement pair_indices(values,target) returning lexicographically smallest [i,j],i<j,whose integer values sum to target,or null.

**Acceptance example / fixture:** [3,2,4,3],6 -> [0,3].

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B14

**Core:** Implement k_way_merge(sorted_lists),retaining all integer duplicates,ascending,without flatten-and-sort.

**Acceptance example / fixture:** [[1,4],[],[1,3]] -> [1,1,3,4].

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-01-B15

**Core:** Implement circular_next_greater(values),returning next strictly greater value to the right wrapping once,or null per position.

**Acceptance example / fixture:** [1,2,1] -> [2,null,2].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-COLLECTIONS-01-I01

**Core:** Implement merge_intervals for half-open integer intervals. Ignore empty intervals,merge overlap/touch,reject start>end,sort ascending.

**Acceptance example / fixture:** [[5,8],[1,3],[3,6]] -> [[1,8]].

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I02

**Core:** Implement rotate_right(values,k) for nonnegative integer k,without mutating input. Empty list remains empty.

**Acceptance example / fixture:** [1,2,3],4 -> [3,1,2].

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I03

**Core:** Implement stable_partition(values,pivot): values<pivot first,then equal,then greater,each group retaining input order.

**Acceptance example / fixture:** [3,1,2,1],2 -> [1,1,2,3].

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I04

**Core:** Implement move_zeros(values),moving numeric zeros to the end and retaining other element order. Return a new integer list.

**Acceptance example / fixture:** [0,2,0,1] -> [2,1,0,0].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I05

**Core:** Implement intersect_multiset(a,b),retaining each integer min(count_a,count_b) times,output ascending.

**Acceptance example / fixture:** [2,1,2],[2,2,3] -> [2,2].

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I06

**Core:** Implement merge_sorted(a,b),retaining all duplicates and ascending order without sorting the concatenation.

**Acceptance example / fixture:** [1,3],[1,2] -> [1,1,2,3].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I07

**Core:** Implement missing_ranges(sorted_distinct,low,high) returning inclusive missing intervals within inclusive bounds.

**Acceptance example / fixture:** [1,3,7],1,8 -> [[2,2],[4,6],[8,8]].

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I08

**Core:** Implement transpose(matrix). Require rectangular rows; [] -> []; ragged input -> INVALID. Output rows must not alias input rows.

**Acceptance example / fixture:** [[1,2],[3,4]] -> [[1,3],[2,4]].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I09

**Core:** Implement flatten_one(values) where each element is either integer or list of integers; flatten exactly one level and reject deeper nesting.

**Acceptance example / fixture:** [1,[2,3],[]] -> [1,2,3].

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I10

**Core:** Implement maximum_subarray(values) returning sum,start,end for nonempty integer input. End exclusive; ties prefer smallest start then smallest end.

**Acceptance example / fixture:** [-2,3,-1,3] -> {sum:5,start:1,end:4}.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I11

**Core:** Implement product_except_self(values) for integers,using no division. Return products of all other positions; empty -> []; one item -> [1].

**Acceptance example / fixture:** [1,2,3] -> [6,3,2]; [0,2,0] -> [0,0,0].

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I12

**Core:** Implement deduplicate_sorted(values) returning unique ascending integers plus original multiplicities,without mutating input.

**Acceptance example / fixture:** [1,1,2,2,2] -> values[1,2],counts[2,3].

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I13

**Core:** Implement pair_indices(values,target) returning lexicographically smallest [i,j],i<j,whose integer values sum to target,or null.

**Acceptance example / fixture:** [3,2,4,3],6 -> [0,3].

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I14

**Core:** Implement k_way_merge(sorted_lists),retaining all integer duplicates,ascending,without flatten-and-sort.

**Acceptance example / fixture:** [[1,4],[],[1,3]] -> [1,1,3,4].

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-01-I15

**Core:** Implement circular_next_greater(values),returning next strictly greater value to the right wrapping once,or null per position.

**Acceptance example / fixture:** [1,2,1] -> [2,null,2].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-COLLECTIONS-01-A01

**Core:** Implement merge_intervals for half-open integer intervals. Ignore empty intervals,merge overlap/touch,reject start>end,sort ascending.

**Acceptance example / fixture:** [[5,8],[1,3],[3,6]] -> [[1,8]].

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A02

**Core:** Implement rotate_right(values,k) for nonnegative integer k,without mutating input. Empty list remains empty.

**Acceptance example / fixture:** [1,2,3],4 -> [3,1,2].

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A03

**Core:** Implement stable_partition(values,pivot): values<pivot first,then equal,then greater,each group retaining input order.

**Acceptance example / fixture:** [3,1,2,1],2 -> [1,1,2,3].

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A04

**Core:** Implement move_zeros(values),moving numeric zeros to the end and retaining other element order. Return a new integer list.

**Acceptance example / fixture:** [0,2,0,1] -> [2,1,0,0].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A05

**Core:** Implement intersect_multiset(a,b),retaining each integer min(count_a,count_b) times,output ascending.

**Acceptance example / fixture:** [2,1,2],[2,2,3] -> [2,2].

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A06

**Core:** Implement merge_sorted(a,b),retaining all duplicates and ascending order without sorting the concatenation.

**Acceptance example / fixture:** [1,3],[1,2] -> [1,1,2,3].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A07

**Core:** Implement missing_ranges(sorted_distinct,low,high) returning inclusive missing intervals within inclusive bounds.

**Acceptance example / fixture:** [1,3,7],1,8 -> [[2,2],[4,6],[8,8]].

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A08

**Core:** Implement transpose(matrix). Require rectangular rows; [] -> []; ragged input -> INVALID. Output rows must not alias input rows.

**Acceptance example / fixture:** [[1,2],[3,4]] -> [[1,3],[2,4]].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A09

**Core:** Implement flatten_one(values) where each element is either integer or list of integers; flatten exactly one level and reject deeper nesting.

**Acceptance example / fixture:** [1,[2,3],[]] -> [1,2,3].

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A10

**Core:** Implement maximum_subarray(values) returning sum,start,end for nonempty integer input. End exclusive; ties prefer smallest start then smallest end.

**Acceptance example / fixture:** [-2,3,-1,3] -> {sum:5,start:1,end:4}.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A11

**Core:** Implement product_except_self(values) for integers,using no division. Return products of all other positions; empty -> []; one item -> [1].

**Acceptance example / fixture:** [1,2,3] -> [6,3,2]; [0,2,0] -> [0,0,0].

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A12

**Core:** Implement deduplicate_sorted(values) returning unique ascending integers plus original multiplicities,without mutating input.

**Acceptance example / fixture:** [1,1,2,2,2] -> values[1,2],counts[2,3].

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A13

**Core:** Implement pair_indices(values,target) returning lexicographically smallest [i,j],i<j,whose integer values sum to target,or null.

**Acceptance example / fixture:** [3,2,4,3],6 -> [0,3].

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A14

**Core:** Implement k_way_merge(sorted_lists),retaining all integer duplicates,ascending,without flatten-and-sort.

**Acceptance example / fixture:** [[1,4],[],[1,3]] -> [1,1,3,4].

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-01-A15

**Core:** Implement circular_next_greater(values),returning next strictly greater value to the right wrapping once,or null per position.

**Acceptance example / fixture:** [1,2,1] -> [2,null,2].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Maps sets and equality

### Beginner

#### JAVA-COLLECTIONS-02-B01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-02-B15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-COLLECTIONS-02-I01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-02-I15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-COLLECTIONS-02-A01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-02-A15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Generics and immutable results

### Beginner

#### JAVA-COLLECTIONS-03-B01

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B02

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B03

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B04

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B05

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B06

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B07

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B08

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B09

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B10

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B11

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B12

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B13

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B14

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-03-B15

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-COLLECTIONS-03-I01

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I02

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I03

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I04

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I05

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I06

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I07

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I08

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I09

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I10

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I11

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I12

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I13

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I14

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-03-I15

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-COLLECTIONS-03-A01

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A02

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A03

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A04

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A05

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A06

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A07

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A08

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A09

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A10

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A11

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A12

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A13

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A14

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-03-A15

**Core:** Implement stableDistinct(List<T>) using equality and hashCode. Keep first occurrence order and return an unmodifiable independent result; later changes to the input list cannot change it.

**Acceptance example / fixture:** [a,b,a] -> [a,b]; modifying output must fail.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Streams and collectors

### Beginner

#### JAVA-COLLECTIONS-04-B01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-COLLECTIONS-04-B15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-COLLECTIONS-04-I01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-COLLECTIONS-04-I15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-COLLECTIONS-04-A01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-COLLECTIONS-04-A15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
