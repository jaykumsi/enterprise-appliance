# Full Stack Developer - NodeJs: JavaScript

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Types and exact numeric boundaries

### Beginner

#### NODE-JAVASCRIPT-01-B01

**Core:** Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.

**Acceptance example / fixture:** "12.3" -> 1230; "1.234" -> INVALID.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B02

**Core:** Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.

**Acceptance example / fixture:** -1 -> "-0.01"; 1200 -> "12.00".

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B03

**Core:** Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.

**Acceptance example / fixture:** "01.200" and "1.2" -> true; "-0" and "0" -> true.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B04

**Core:** Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.

**Acceptance example / fixture:** "1.25"+"-0.30" -> "0.95".

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B05

**Core:** Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.

**Acceptance example / fixture:** 2147483647+1 with signed32 bounds -> OVERFLOW.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B06

**Core:** Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.

**Acceptance example / fixture:** (10,3) -> [4,3,3].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B07

**Core:** Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.

**Acceptance example / fixture:** (101,1000) -> 10.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B08

**Core:** Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.

**Acceptance example / fixture:** ("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B09

**Core:** Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.

**Acceptance example / fixture:** (-7,3) -> -3; (7,-3) -> -3.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B10

**Core:** Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.

**Acceptance example / fixture:** (123,2,3) -> 1230; (123,2,1) -> INEXACT.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B11

**Core:** Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.

**Acceptance example / fixture:** (1,3,2,6) -> 0.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B12

**Core:** Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.

**Acceptance example / fixture:** "-000" -> "0"; "+0012" -> "12".

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B13

**Core:** Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / fixture:** ([2,3,-1],-4,4) -> 1.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B14

**Core:** Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.

**Acceptance example / fixture:** (10,[1,1,1]) -> [4,3,3].

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-01-B15

**Core:** Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.

**Acceptance example / fixture:** ("-1A",16) -> -26; ("2",2) -> INVALID.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-JAVASCRIPT-01-I01

**Core:** Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.

**Acceptance example / fixture:** "12.3" -> 1230; "1.234" -> INVALID.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I02

**Core:** Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.

**Acceptance example / fixture:** -1 -> "-0.01"; 1200 -> "12.00".

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I03

**Core:** Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.

**Acceptance example / fixture:** "01.200" and "1.2" -> true; "-0" and "0" -> true.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I04

**Core:** Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.

**Acceptance example / fixture:** "1.25"+"-0.30" -> "0.95".

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I05

**Core:** Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.

**Acceptance example / fixture:** 2147483647+1 with signed32 bounds -> OVERFLOW.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I06

**Core:** Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.

**Acceptance example / fixture:** (10,3) -> [4,3,3].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I07

**Core:** Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.

**Acceptance example / fixture:** (101,1000) -> 10.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I08

**Core:** Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.

**Acceptance example / fixture:** ("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I09

**Core:** Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.

**Acceptance example / fixture:** (-7,3) -> -3; (7,-3) -> -3.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I10

**Core:** Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.

**Acceptance example / fixture:** (123,2,3) -> 1230; (123,2,1) -> INEXACT.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I11

**Core:** Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.

**Acceptance example / fixture:** (1,3,2,6) -> 0.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I12

**Core:** Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.

**Acceptance example / fixture:** "-000" -> "0"; "+0012" -> "12".

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I13

**Core:** Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / fixture:** ([2,3,-1],-4,4) -> 1.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I14

**Core:** Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.

**Acceptance example / fixture:** (10,[1,1,1]) -> [4,3,3].

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-01-I15

**Core:** Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.

**Acceptance example / fixture:** ("-1A",16) -> -26; ("2",2) -> INVALID.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-JAVASCRIPT-01-A01

**Core:** Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.

**Acceptance example / fixture:** "12.3" -> 1230; "1.234" -> INVALID.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A02

**Core:** Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.

**Acceptance example / fixture:** -1 -> "-0.01"; 1200 -> "12.00".

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A03

**Core:** Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.

**Acceptance example / fixture:** "01.200" and "1.2" -> true; "-0" and "0" -> true.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A04

**Core:** Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.

**Acceptance example / fixture:** "1.25"+"-0.30" -> "0.95".

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A05

**Core:** Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.

**Acceptance example / fixture:** 2147483647+1 with signed32 bounds -> OVERFLOW.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A06

**Core:** Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.

**Acceptance example / fixture:** (10,3) -> [4,3,3].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A07

**Core:** Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.

**Acceptance example / fixture:** (101,1000) -> 10.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A08

**Core:** Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.

**Acceptance example / fixture:** ("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A09

**Core:** Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.

**Acceptance example / fixture:** (-7,3) -> -3; (7,-3) -> -3.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A10

**Core:** Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.

**Acceptance example / fixture:** (123,2,3) -> 1230; (123,2,1) -> INEXACT.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A11

**Core:** Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.

**Acceptance example / fixture:** (1,3,2,6) -> 0.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A12

**Core:** Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.

**Acceptance example / fixture:** "-000" -> "0"; "+0012" -> "12".

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A13

**Core:** Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / fixture:** ([2,3,-1],-4,4) -> 1.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A14

**Core:** Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.

**Acceptance example / fixture:** (10,[1,1,1]) -> [4,3,3].

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-01-A15

**Core:** Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.

**Acceptance example / fixture:** ("-1A",16) -> -26; ("2",2) -> INVALID.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Arrays maps and sets

### Beginner

#### NODE-JAVASCRIPT-02-B01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-02-B15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-JAVASCRIPT-02-I01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-02-I15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-JAVASCRIPT-02-A01

**Core:** Implement first_unique(strings),returning first string with frequency1 or null. Preserve input order and case.

**Acceptance example / fixture:** [b,a,b,c] -> a.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A02

**Core:** Implement frequencies(strings),returning [{value,count}] sorted by value and keeping case distinct.

**Acceptance example / fixture:** [b,a,b] -> [{value:a,count:1},{value:b,count:2}].

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A03

**Core:** Implement group_indices(strings),mapping each distinct string to its ascending original positions. Sort output keys.

**Acceptance example / fixture:** [b,a,b] -> {a:[1],b:[0,2]}.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A04

**Core:** Implement invert_unique(mapping). Return value->key only when values are unique; otherwise return sorted duplicate values and no partial inverse.

**Acceptance example / fixture:** {a:x,b:x} -> duplicates[x].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A05

**Core:** Implement left_join_records(left,right) by unique id. Retain left order and attach right payload or null. Reject duplicate IDs in either side.

**Acceptance example / fixture:** left[a,b],right[b:2] -> [a:null,b:2].

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A06

**Core:** Implement set_report(a,b),returning distinct intersection,only_a,only_b,each sorted. Inputs are strings.

**Acceptance example / fixture:** [a,a,b],[b,c] -> intersection[b],only_a[a],only_b[c].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A07

**Core:** Implement dedup_latest(rows),choosing greatest integer version per id. Equal-version different payload -> CONFLICT; return winners sorted by id.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A08

**Core:** Implement group_anagrams(words) for lowercase ASCII strings. Preserve first-group appearance and original word order within each group.

**Acceptance example / fixture:** [eat,tea,bat,ate] -> [[eat,tea,ate],[bat]].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A09

**Core:** Implement bijection(a,b) on equal-length string arrays. Return true only if each distinct source maps to exactly one distinct target and vice versa.

**Acceptance example / fixture:** [a,b,a],[x,y,x] -> true; [a,b],[x,x] -> false.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A10

**Core:** Implement sparse_dot(a,b),where maps contain integer-index->integer-value. Return sum of products over shared indices without expanding dense arrays.

**Acceptance example / fixture:** {1:2,5:3},{1:4,2:7} -> 8.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A11

**Core:** Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / fixture:** a:+5,a:-5,b:+3 -> a:0,b:3.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A12

**Core:** Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / fixture:** [1,1,2,2],3 -> 4.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A13

**Core:** Implement unique_window_counts(values,k) for positive k,returning number of distinct values in every contiguous window of length k. k>length -> [].

**Acceptance example / fixture:** [a,b,a,c],3 -> [2,3].

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A14

**Core:** Implement renames(mapping,requests) atomically. Every old key must exist,new keys must be distinct,and a new key may replace another only if that key is also renamed in the same batch.

**Acceptance example / fixture:** {a:1,b:2},a->b,b->a -> {a:2,b:1}.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-02-A15

**Core:** Implement event_dedup(events) by id and complete payload. Equal repeated payload is ignored; conflicting repeated payload returns CONFLICT with id; retained events preserve first appearance.

**Acceptance example / fixture:** [e:x,e:x,f:y] -> [e:x,f:y].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Closures and scope

### Beginner

#### NODE-JAVASCRIPT-03-B01

**Core:** Implement apply_discount(prices,pct): integer cents>=0,pct0..100. Return new prices floor(price*(100-pct)/100),without input mutation.

**Acceptance example / fixture:** [101,200],10 -> [90,180].

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B02

**Core:** Implement compose(functions) producing a function that applies supplied pure unary functions left to right. Empty list means identity.

**Acceptance example / fixture:** [x+1,x*2] applied3 -> 8.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B03

**Core:** Implement partition(values,predicate) returning accepted and rejected lists in original order. Call predicate exactly once per value.

**Acceptance example / fixture:** [1,2,3],even -> accepted[2],rejected[1,3].

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B04

**Core:** Implement fold_until(values,initial,step,stop). Apply step to each item and stop before the next item once stop(accumulator) is true. Return accumulator and consumed count.

**Acceptance example / fixture:** [2,3,9],initial0,sum,stop>=5 -> value5,consumed2.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B05

**Core:** Implement map_with_index(values,fn),calling fn(value,index) once per value and returning new results. Indices start0.

**Acceptance example / fixture:** [a,b],concatenate value/index -> [a0,b1].

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B06

**Core:** Implement make_counter(initial) with independent add(delta),value() closures. State changes only within that instance.

**Acceptance example / fixture:** Counters0 and10; first.add2 -> first2,second10.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B07

**Core:** Implement apply_if(value,predicate,transform): call transform only when predicate is true; otherwise return original. Return a trace of which callbacks ran.

**Acceptance example / fixture:** -1,is_positive,double -> -1,trace[predicate].

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B08

**Core:** Implement curry3(fn) accepting arguments across three one-argument calls. Each partially applied instance retains only its own arguments.

**Acceptance example / fixture:** add3(1)(2)(3) -> 6; separate partials remain independent.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B09

**Core:** Implement safe_call(fn,arg),returning {ok:value} or {error:type,message}; catch only declared application exceptions,not cancellation/termination signals.

**Acceptance example / fixture:** fn raises ValidationError -> structured error,not false success.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B10

**Core:** Implement memoized_last(fn) caching only the most recent immutable argument/result. Exceptions never populate cache; expose invocation count.

**Acceptance example / fixture:** Calls a,a,b,a -> underlying3 calls.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B11

**Core:** Implement route(value,rules,default) using the first predicate that matches and only its transform. Evaluate predicates in order; no later predicates after a match.

**Acceptance example / fixture:** Rules negative->N,even->E; value-2 -> N.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B12

**Core:** Implement zip_apply(functions,values),requiring equal lengths,calling each function on corresponding value. Reject mismatched lengths before any callback.

**Acceptance example / fixture:** [double,negate],[3,4] -> [6,-4].

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B13

**Core:** Implement repeat_until(value,transform,predicate,limit),checking predicate before each transform. Return value,steps and satisfied; stop after at most limit transforms.

**Acceptance example / fixture:** start1,double,predicate>=5,limit3 -> value8,steps3,true.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B14

**Core:** Implement validate_then(value,validators,action). Run validators in order,collect all returned field errors,and invoke action once only when no errors.

**Acceptance example / fixture:** Two validation errors -> both reported,action calls0.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-03-B15

**Core:** Implement pipeline(stages,input),where each stage returns {ok:value} or {error:code}. Stop at first error and report its stage index; later stages never run.

**Acceptance example / fixture:** success+error+success -> error at1,third calls0.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-JAVASCRIPT-03-I01

**Core:** Implement apply_discount(prices,pct): integer cents>=0,pct0..100. Return new prices floor(price*(100-pct)/100),without input mutation.

**Acceptance example / fixture:** [101,200],10 -> [90,180].

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I02

**Core:** Implement compose(functions) producing a function that applies supplied pure unary functions left to right. Empty list means identity.

**Acceptance example / fixture:** [x+1,x*2] applied3 -> 8.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I03

**Core:** Implement partition(values,predicate) returning accepted and rejected lists in original order. Call predicate exactly once per value.

**Acceptance example / fixture:** [1,2,3],even -> accepted[2],rejected[1,3].

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I04

**Core:** Implement fold_until(values,initial,step,stop). Apply step to each item and stop before the next item once stop(accumulator) is true. Return accumulator and consumed count.

**Acceptance example / fixture:** [2,3,9],initial0,sum,stop>=5 -> value5,consumed2.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I05

**Core:** Implement map_with_index(values,fn),calling fn(value,index) once per value and returning new results. Indices start0.

**Acceptance example / fixture:** [a,b],concatenate value/index -> [a0,b1].

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I06

**Core:** Implement make_counter(initial) with independent add(delta),value() closures. State changes only within that instance.

**Acceptance example / fixture:** Counters0 and10; first.add2 -> first2,second10.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I07

**Core:** Implement apply_if(value,predicate,transform): call transform only when predicate is true; otherwise return original. Return a trace of which callbacks ran.

**Acceptance example / fixture:** -1,is_positive,double -> -1,trace[predicate].

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I08

**Core:** Implement curry3(fn) accepting arguments across three one-argument calls. Each partially applied instance retains only its own arguments.

**Acceptance example / fixture:** add3(1)(2)(3) -> 6; separate partials remain independent.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I09

**Core:** Implement safe_call(fn,arg),returning {ok:value} or {error:type,message}; catch only declared application exceptions,not cancellation/termination signals.

**Acceptance example / fixture:** fn raises ValidationError -> structured error,not false success.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I10

**Core:** Implement memoized_last(fn) caching only the most recent immutable argument/result. Exceptions never populate cache; expose invocation count.

**Acceptance example / fixture:** Calls a,a,b,a -> underlying3 calls.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I11

**Core:** Implement route(value,rules,default) using the first predicate that matches and only its transform. Evaluate predicates in order; no later predicates after a match.

**Acceptance example / fixture:** Rules negative->N,even->E; value-2 -> N.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I12

**Core:** Implement zip_apply(functions,values),requiring equal lengths,calling each function on corresponding value. Reject mismatched lengths before any callback.

**Acceptance example / fixture:** [double,negate],[3,4] -> [6,-4].

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I13

**Core:** Implement repeat_until(value,transform,predicate,limit),checking predicate before each transform. Return value,steps and satisfied; stop after at most limit transforms.

**Acceptance example / fixture:** start1,double,predicate>=5,limit3 -> value8,steps3,true.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I14

**Core:** Implement validate_then(value,validators,action). Run validators in order,collect all returned field errors,and invoke action once only when no errors.

**Acceptance example / fixture:** Two validation errors -> both reported,action calls0.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-03-I15

**Core:** Implement pipeline(stages,input),where each stage returns {ok:value} or {error:code}. Stop at first error and report its stage index; later stages never run.

**Acceptance example / fixture:** success+error+success -> error at1,third calls0.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-JAVASCRIPT-03-A01

**Core:** Implement apply_discount(prices,pct): integer cents>=0,pct0..100. Return new prices floor(price*(100-pct)/100),without input mutation.

**Acceptance example / fixture:** [101,200],10 -> [90,180].

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A02

**Core:** Implement compose(functions) producing a function that applies supplied pure unary functions left to right. Empty list means identity.

**Acceptance example / fixture:** [x+1,x*2] applied3 -> 8.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A03

**Core:** Implement partition(values,predicate) returning accepted and rejected lists in original order. Call predicate exactly once per value.

**Acceptance example / fixture:** [1,2,3],even -> accepted[2],rejected[1,3].

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A04

**Core:** Implement fold_until(values,initial,step,stop). Apply step to each item and stop before the next item once stop(accumulator) is true. Return accumulator and consumed count.

**Acceptance example / fixture:** [2,3,9],initial0,sum,stop>=5 -> value5,consumed2.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A05

**Core:** Implement map_with_index(values,fn),calling fn(value,index) once per value and returning new results. Indices start0.

**Acceptance example / fixture:** [a,b],concatenate value/index -> [a0,b1].

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A06

**Core:** Implement make_counter(initial) with independent add(delta),value() closures. State changes only within that instance.

**Acceptance example / fixture:** Counters0 and10; first.add2 -> first2,second10.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A07

**Core:** Implement apply_if(value,predicate,transform): call transform only when predicate is true; otherwise return original. Return a trace of which callbacks ran.

**Acceptance example / fixture:** -1,is_positive,double -> -1,trace[predicate].

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A08

**Core:** Implement curry3(fn) accepting arguments across three one-argument calls. Each partially applied instance retains only its own arguments.

**Acceptance example / fixture:** add3(1)(2)(3) -> 6; separate partials remain independent.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A09

**Core:** Implement safe_call(fn,arg),returning {ok:value} or {error:type,message}; catch only declared application exceptions,not cancellation/termination signals.

**Acceptance example / fixture:** fn raises ValidationError -> structured error,not false success.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A10

**Core:** Implement memoized_last(fn) caching only the most recent immutable argument/result. Exceptions never populate cache; expose invocation count.

**Acceptance example / fixture:** Calls a,a,b,a -> underlying3 calls.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A11

**Core:** Implement route(value,rules,default) using the first predicate that matches and only its transform. Evaluate predicates in order; no later predicates after a match.

**Acceptance example / fixture:** Rules negative->N,even->E; value-2 -> N.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A12

**Core:** Implement zip_apply(functions,values),requiring equal lengths,calling each function on corresponding value. Reject mismatched lengths before any callback.

**Acceptance example / fixture:** [double,negate],[3,4] -> [6,-4].

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A13

**Core:** Implement repeat_until(value,transform,predicate,limit),checking predicate before each transform. Return value,steps and satisfied; stop after at most limit transforms.

**Acceptance example / fixture:** start1,double,predicate>=5,limit3 -> value8,steps3,true.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A14

**Core:** Implement validate_then(value,validators,action). Run validators in order,collect all returned field errors,and invoke action once only when no errors.

**Acceptance example / fixture:** Two validation errors -> both reported,action calls0.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-03-A15

**Core:** Implement pipeline(stages,input),where each stage returns {ok:value} or {error:code}. Stop at first error and report its stage index; later stages never run.

**Acceptance example / fixture:** success+error+success -> error at1,third calls0.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Objects and immutability

### Beginner

#### NODE-JAVASCRIPT-04-B01

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B02

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B03

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B04

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B05

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B06

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B07

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B08

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B09

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B10

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B11

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B12

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B13

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B14

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-04-B15

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-JAVASCRIPT-04-I01

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I02

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I03

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I04

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I05

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I06

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I07

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I08

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I09

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I10

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I11

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I12

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I13

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I14

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-04-I15

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-JAVASCRIPT-04-A01

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A02

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A03

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A04

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A05

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A06

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A07

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A08

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A09

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A10

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A11

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A12

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A13

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A14

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-04-A15

**Core:** Implement updateQuantity(cart,sku,quantity) returning a new cart with one matching item changed. Cart entries have unique SKU; quantity is a nonnegative integer; zero removes the item. Preserve all input objects.

**Acceptance example / fixture:** [{sku:A,quantity:2}] updated A,0 -> []; original unchanged.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## TypeScript discriminated unions

### Beginner

#### NODE-JAVASCRIPT-05-B01

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B02

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B03

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B04

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B05

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B06

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B07

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B08

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B09

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B10

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B11

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B12

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B13

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B14

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### NODE-JAVASCRIPT-05-B15

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### NODE-JAVASCRIPT-05-I01

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I02

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I03

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I04

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I05

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I06

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I07

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I08

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I09

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I10

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I11

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I12

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I13

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I14

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### NODE-JAVASCRIPT-05-I15

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### NODE-JAVASCRIPT-05-A01

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A02

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A03

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A04

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A05

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A06

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A07

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A08

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A09

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A10

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A11

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A12

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A13

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A14

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### NODE-JAVASCRIPT-05-A15

**Core:** Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / fixture:** Open+Pay -> Paid; Shipped+Pay -> error.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
