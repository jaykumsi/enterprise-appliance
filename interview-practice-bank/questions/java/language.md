# Full Stack Developer - Java: Language

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Primitives and exact arithmetic

### Beginner

#### JAVA-LANGUAGE-01-B01

**Core:** Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.

**Acceptance example / fixture:** "12.3" -> 1230; "1.234" -> INVALID.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B02

**Core:** Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.

**Acceptance example / fixture:** -1 -> "-0.01"; 1200 -> "12.00".

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B03

**Core:** Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.

**Acceptance example / fixture:** "01.200" and "1.2" -> true; "-0" and "0" -> true.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B04

**Core:** Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.

**Acceptance example / fixture:** "1.25"+"-0.30" -> "0.95".

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B05

**Core:** Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.

**Acceptance example / fixture:** 2147483647+1 with signed32 bounds -> OVERFLOW.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B06

**Core:** Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.

**Acceptance example / fixture:** (10,3) -> [4,3,3].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B07

**Core:** Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.

**Acceptance example / fixture:** (101,1000) -> 10.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B08

**Core:** Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.

**Acceptance example / fixture:** ("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B09

**Core:** Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.

**Acceptance example / fixture:** (-7,3) -> -3; (7,-3) -> -3.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B10

**Core:** Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.

**Acceptance example / fixture:** (123,2,3) -> 1230; (123,2,1) -> INEXACT.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B11

**Core:** Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.

**Acceptance example / fixture:** (1,3,2,6) -> 0.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B12

**Core:** Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.

**Acceptance example / fixture:** "-000" -> "0"; "+0012" -> "12".

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B13

**Core:** Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / fixture:** ([2,3,-1],-4,4) -> 1.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B14

**Core:** Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.

**Acceptance example / fixture:** (10,[1,1,1]) -> [4,3,3].

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-01-B15

**Core:** Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.

**Acceptance example / fixture:** ("-1A",16) -> -26; ("2",2) -> INVALID.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-LANGUAGE-01-I01

**Core:** Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.

**Acceptance example / fixture:** "12.3" -> 1230; "1.234" -> INVALID.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I02

**Core:** Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.

**Acceptance example / fixture:** -1 -> "-0.01"; 1200 -> "12.00".

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I03

**Core:** Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.

**Acceptance example / fixture:** "01.200" and "1.2" -> true; "-0" and "0" -> true.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I04

**Core:** Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.

**Acceptance example / fixture:** "1.25"+"-0.30" -> "0.95".

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I05

**Core:** Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.

**Acceptance example / fixture:** 2147483647+1 with signed32 bounds -> OVERFLOW.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I06

**Core:** Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.

**Acceptance example / fixture:** (10,3) -> [4,3,3].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I07

**Core:** Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.

**Acceptance example / fixture:** (101,1000) -> 10.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I08

**Core:** Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.

**Acceptance example / fixture:** ("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I09

**Core:** Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.

**Acceptance example / fixture:** (-7,3) -> -3; (7,-3) -> -3.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I10

**Core:** Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.

**Acceptance example / fixture:** (123,2,3) -> 1230; (123,2,1) -> INEXACT.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I11

**Core:** Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.

**Acceptance example / fixture:** (1,3,2,6) -> 0.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I12

**Core:** Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.

**Acceptance example / fixture:** "-000" -> "0"; "+0012" -> "12".

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I13

**Core:** Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / fixture:** ([2,3,-1],-4,4) -> 1.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I14

**Core:** Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.

**Acceptance example / fixture:** (10,[1,1,1]) -> [4,3,3].

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-01-I15

**Core:** Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.

**Acceptance example / fixture:** ("-1A",16) -> -26; ("2",2) -> INVALID.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-LANGUAGE-01-A01

**Core:** Implement parse_cents(text). Accept optional minus,digits and at most two fractional digits. No whitespace/exponents; invalid -> INVALID. Return exact signed integer cents without binary floats.

**Acceptance example / fixture:** "12.3" -> 1230; "1.234" -> INVALID.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A02

**Core:** Implement format_cents(integer). Return signed decimal text with exactly two fractional digits and no leading zeros; zero has no minus sign.

**Acceptance example / fixture:** -1 -> "-0.01"; 1200 -> "12.00".

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A03

**Core:** Implement decimal_equal(a,b) for signed decimal strings with arbitrary digits and optional fractional part. Compare exact values without floats; invalid syntax -> INVALID.

**Acceptance example / fixture:** "01.200" and "1.2" -> true; "-0" and "0" -> true.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A04

**Core:** Implement add_decimal(a,b) on signed decimal strings with at most two fractional digits. Return canonical two-decimal text; reject malformed strings before adding.

**Acceptance example / fixture:** "1.25"+"-0.30" -> "0.95".

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A05

**Core:** Implement checked_add(a,b,min,max) on integers. Return the exact sum only if within inclusive bounds,otherwise OVERFLOW. Reject min>max.

**Acceptance example / fixture:** 2147483647+1 with signed32 bounds -> OVERFLOW.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A06

**Core:** Implement split_bill(cents,n). cents is nonnegative,n positive integer. Return n shares differing by at most one cent; allocate extra cents to earlier positions.

**Acceptance example / fixture:** (10,3) -> [4,3,3].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A07

**Core:** Implement percent_floor(cents,basis_points). Both nonnegative integers,basis_points<=10000. Return floor(cents*basis_points/10000) using exact arithmetic.

**Acceptance example / fixture:** (101,1000) -> 10.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A08

**Core:** Implement round_half_even(text,scale) for a signed decimal string and nonnegative scale. Return exactly scale fractional digits without floating-point conversion.

**Acceptance example / fixture:** ("2.345",2) -> "2.34"; ("2.355",2) -> "2.36".

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A09

**Core:** Implement floor_div(a,b) returning mathematical floor(a/b) for signed integers; zero divisor -> INVALID. Do not assume truncation toward zero.

**Acceptance example / fixture:** (-7,3) -> -3; (7,-3) -> -3.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A10

**Core:** Implement convert_units(value,source_scale,target_scale) where value is a signed integer in 10^-source_scale units. Return exact target integer or INEXACT if digits would be discarded.

**Acceptance example / fixture:** (123,2,3) -> 1230; (123,2,1) -> INEXACT.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A11

**Core:** Implement compare_fractions(a,b,c,d) for signed integer numerators and positive denominators. Return -1,0,1 comparing a/b to c/d without floats.

**Acceptance example / fixture:** (1,3,2,6) -> 0.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A12

**Core:** Implement normalize_integer(text). Accept optional plus/minus and digits only; remove plus/leading zeros and negative zero. Invalid syntax -> INVALID.

**Acceptance example / fixture:** "-000" -> "0"; "+0012" -> "12".

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A13

**Core:** Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / fixture:** ([2,3,-1],-4,4) -> 1.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A14

**Core:** Implement allocate_by_weight(cents,weights) for nonnegative integer cents and positive integer weights. Floor exact proportional shares,then distribute remaining cents by descending fractional remainder,ties by original index.

**Acceptance example / fixture:** (10,[1,1,1]) -> [4,3,3].

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-01-A15

**Core:** Implement parse_base(text,base) with base2..36,optional leading minus,and case-insensitive digits0-9A-Z. Reject a digit outside the base. Return exact integer.

**Acceptance example / fixture:** ("-1A",16) -> -26; ("2",2) -> INVALID.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Control flow and methods

### Beginner

#### JAVA-LANGUAGE-02-B01

**Core:** Implement shipping(grams): positive integer weights through1000 cost500 cents,each started additional1000 costs200. Invalid weight -> INVALID.

**Acceptance example / fixture:** 1001 -> 700; 2000 -> 700.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B02

**Core:** Implement fizz_labels(n) returning labels for1..n: multiples3 -> Fizz,5 -> Buzz,both -> FizzBuzz,otherwise decimal number. Nonnegative integer n required.

**Acceptance example / fixture:** n=5 -> [1,2,Fizz,4,Buzz].

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B03

**Core:** Implement digit_sum(n) for signed integers,ignoring the sign. Do not convert the entire number to floating point.

**Acceptance example / fixture:** -1203 -> 6; 0 -> 0.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B04

**Core:** Implement run_lengths(values),returning [value,count] for each consecutive equal run in original order.

**Acceptance example / fixture:** [a,a,b,a] -> [[a,2],[b,1],[a,1]].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B05

**Core:** Implement longest_positive_streak(values),returning the maximum consecutive count of integers>0.

**Acceptance example / fixture:** [1,2,0,3,-1,4,5,6] -> 3.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B06

**Core:** Implement next_business_day(day,closed_days) using integer day numbers. closed_days is a finite set; return smallest integer>day not in the set.

**Acceptance example / fixture:** day5,closed[6,7] -> 8.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B07

**Core:** Implement tier_cost(units): first100 units at2 cents each,next100 at3,remaining at5. Units is nonnegative integer; return exact total.

**Acceptance example / fixture:** 250 -> 750.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B08

**Core:** Implement multiplicative_steps(start,target) for positive integers: repeatedly double start until >=target. Return steps and final value.

**Acceptance example / fixture:** (3,20) -> {steps:3,value:24}.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B09

**Core:** Implement balance_path(deltas) returning running integer totals from zero and the first negative index or null.

**Acceptance example / fixture:** [2,-3,5] -> totals[2,-1,4],first_negative1.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B10

**Core:** Implement triangle_rows(n) returning rows [1],[1,2],...,[1..n]. Nonnegative integer n; no shared mutable row references.

**Acceptance example / fixture:** 3 -> [[1],[1,2],[1,2,3]].

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B11

**Core:** Implement collatz_step(n) for a positive integer only: even -> n/2,odd ->3n+1. Implement trace until1 with max_steps positive; return LIMIT if not complete.

**Acceptance example / fixture:** n3,max10 -> [3,10,5,16,8,4,2,1].

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B12

**Core:** Implement count_between(values,low,high) with low inclusive,high exclusive. Reject low>high; return count and matching original indices.

**Acceptance example / fixture:** ([1,2,3,2],2,3) -> count2,indices[1,3].

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B13

**Core:** Implement staircase_change(coins,target) for a supplied descending list of positive denominations; repeatedly take largest available denomination<=remaining. Return greedy counts or IMPOSSIBLE; do not claim minimum coins.

**Acceptance example / fixture:** coins[4,3],target6 -> greedy IMPOSSIBLE despite possible3+3.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B14

**Core:** Implement stop_at_sentinel(values,sentinel) returning sum and count before the first sentinel. Do not include or read beyond the sentinel in an iterator.

**Acceptance example / fixture:** [2,3,-1,100],sentinel-1 -> sum5,count2.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-02-B15

**Core:** Implement decimal_digits(n),returning signed integer n as a sign flag and most-significant-first digit array using integer operations.

**Acceptance example / fixture:** -105 -> {negative:true,digits:[1,0,5]}.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-LANGUAGE-02-I01

**Core:** Implement shipping(grams): positive integer weights through1000 cost500 cents,each started additional1000 costs200. Invalid weight -> INVALID.

**Acceptance example / fixture:** 1001 -> 700; 2000 -> 700.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I02

**Core:** Implement fizz_labels(n) returning labels for1..n: multiples3 -> Fizz,5 -> Buzz,both -> FizzBuzz,otherwise decimal number. Nonnegative integer n required.

**Acceptance example / fixture:** n=5 -> [1,2,Fizz,4,Buzz].

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I03

**Core:** Implement digit_sum(n) for signed integers,ignoring the sign. Do not convert the entire number to floating point.

**Acceptance example / fixture:** -1203 -> 6; 0 -> 0.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I04

**Core:** Implement run_lengths(values),returning [value,count] for each consecutive equal run in original order.

**Acceptance example / fixture:** [a,a,b,a] -> [[a,2],[b,1],[a,1]].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I05

**Core:** Implement longest_positive_streak(values),returning the maximum consecutive count of integers>0.

**Acceptance example / fixture:** [1,2,0,3,-1,4,5,6] -> 3.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I06

**Core:** Implement next_business_day(day,closed_days) using integer day numbers. closed_days is a finite set; return smallest integer>day not in the set.

**Acceptance example / fixture:** day5,closed[6,7] -> 8.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I07

**Core:** Implement tier_cost(units): first100 units at2 cents each,next100 at3,remaining at5. Units is nonnegative integer; return exact total.

**Acceptance example / fixture:** 250 -> 750.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I08

**Core:** Implement multiplicative_steps(start,target) for positive integers: repeatedly double start until >=target. Return steps and final value.

**Acceptance example / fixture:** (3,20) -> {steps:3,value:24}.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I09

**Core:** Implement balance_path(deltas) returning running integer totals from zero and the first negative index or null.

**Acceptance example / fixture:** [2,-3,5] -> totals[2,-1,4],first_negative1.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I10

**Core:** Implement triangle_rows(n) returning rows [1],[1,2],...,[1..n]. Nonnegative integer n; no shared mutable row references.

**Acceptance example / fixture:** 3 -> [[1],[1,2],[1,2,3]].

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I11

**Core:** Implement collatz_step(n) for a positive integer only: even -> n/2,odd ->3n+1. Implement trace until1 with max_steps positive; return LIMIT if not complete.

**Acceptance example / fixture:** n3,max10 -> [3,10,5,16,8,4,2,1].

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I12

**Core:** Implement count_between(values,low,high) with low inclusive,high exclusive. Reject low>high; return count and matching original indices.

**Acceptance example / fixture:** ([1,2,3,2],2,3) -> count2,indices[1,3].

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I13

**Core:** Implement staircase_change(coins,target) for a supplied descending list of positive denominations; repeatedly take largest available denomination<=remaining. Return greedy counts or IMPOSSIBLE; do not claim minimum coins.

**Acceptance example / fixture:** coins[4,3],target6 -> greedy IMPOSSIBLE despite possible3+3.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I14

**Core:** Implement stop_at_sentinel(values,sentinel) returning sum and count before the first sentinel. Do not include or read beyond the sentinel in an iterator.

**Acceptance example / fixture:** [2,3,-1,100],sentinel-1 -> sum5,count2.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-02-I15

**Core:** Implement decimal_digits(n),returning signed integer n as a sign flag and most-significant-first digit array using integer operations.

**Acceptance example / fixture:** -105 -> {negative:true,digits:[1,0,5]}.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-LANGUAGE-02-A01

**Core:** Implement shipping(grams): positive integer weights through1000 cost500 cents,each started additional1000 costs200. Invalid weight -> INVALID.

**Acceptance example / fixture:** 1001 -> 700; 2000 -> 700.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A02

**Core:** Implement fizz_labels(n) returning labels for1..n: multiples3 -> Fizz,5 -> Buzz,both -> FizzBuzz,otherwise decimal number. Nonnegative integer n required.

**Acceptance example / fixture:** n=5 -> [1,2,Fizz,4,Buzz].

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A03

**Core:** Implement digit_sum(n) for signed integers,ignoring the sign. Do not convert the entire number to floating point.

**Acceptance example / fixture:** -1203 -> 6; 0 -> 0.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A04

**Core:** Implement run_lengths(values),returning [value,count] for each consecutive equal run in original order.

**Acceptance example / fixture:** [a,a,b,a] -> [[a,2],[b,1],[a,1]].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A05

**Core:** Implement longest_positive_streak(values),returning the maximum consecutive count of integers>0.

**Acceptance example / fixture:** [1,2,0,3,-1,4,5,6] -> 3.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A06

**Core:** Implement next_business_day(day,closed_days) using integer day numbers. closed_days is a finite set; return smallest integer>day not in the set.

**Acceptance example / fixture:** day5,closed[6,7] -> 8.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A07

**Core:** Implement tier_cost(units): first100 units at2 cents each,next100 at3,remaining at5. Units is nonnegative integer; return exact total.

**Acceptance example / fixture:** 250 -> 750.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A08

**Core:** Implement multiplicative_steps(start,target) for positive integers: repeatedly double start until >=target. Return steps and final value.

**Acceptance example / fixture:** (3,20) -> {steps:3,value:24}.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A09

**Core:** Implement balance_path(deltas) returning running integer totals from zero and the first negative index or null.

**Acceptance example / fixture:** [2,-3,5] -> totals[2,-1,4],first_negative1.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A10

**Core:** Implement triangle_rows(n) returning rows [1],[1,2],...,[1..n]. Nonnegative integer n; no shared mutable row references.

**Acceptance example / fixture:** 3 -> [[1],[1,2],[1,2,3]].

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A11

**Core:** Implement collatz_step(n) for a positive integer only: even -> n/2,odd ->3n+1. Implement trace until1 with max_steps positive; return LIMIT if not complete.

**Acceptance example / fixture:** n3,max10 -> [3,10,5,16,8,4,2,1].

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A12

**Core:** Implement count_between(values,low,high) with low inclusive,high exclusive. Reject low>high; return count and matching original indices.

**Acceptance example / fixture:** ([1,2,3,2],2,3) -> count2,indices[1,3].

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A13

**Core:** Implement staircase_change(coins,target) for a supplied descending list of positive denominations; repeatedly take largest available denomination<=remaining. Return greedy counts or IMPOSSIBLE; do not claim minimum coins.

**Acceptance example / fixture:** coins[4,3],target6 -> greedy IMPOSSIBLE despite possible3+3.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A14

**Core:** Implement stop_at_sentinel(values,sentinel) returning sum and count before the first sentinel. Do not include or read beyond the sentinel in an iterator.

**Acceptance example / fixture:** [2,3,-1,100],sentinel-1 -> sum5,count2.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-02-A15

**Core:** Implement decimal_digits(n),returning signed integer n as a sign flag and most-significant-first digit array using integer operations.

**Acceptance example / fixture:** -105 -> {negative:true,digits:[1,0,5]}.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Strings and Unicode

### Beginner

#### JAVA-LANGUAGE-03-B01

**Core:** Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.

**Acceptance example / fixture:** " ab-012 " -> "AB-012".

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B02

**Core:** Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.

**Acceptance example / fixture:** "abba" -> 2; "" -> 0.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B03

**Core:** Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.

**Acceptance example / fixture:** " a  b " -> "b a".

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B04

**Core:** Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.

**Acceptance example / fixture:** "A man, a plan, a canal: Panama" -> true.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B05

**Core:** Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.

**Acceptance example / fixture:** [flower,flow,flight] -> fl.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B06

**Core:** Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.

**Acceptance example / fixture:** "aaabb" -> [{character:a,count:3},{character:b,count:2}].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B07

**Core:** Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.

**Acceptance example / fixture:** "([)]" -> invalid index2; "([])" -> valid.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B08

**Core:** Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.

**Acceptance example / fixture:** "a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B09

**Core:** Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.

**Acceptance example / fixture:** [{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B10

**Core:** Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.

**Acceptance example / fixture:** "swiss" -> 1.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B11

**Core:** Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.

**Acceptance example / fixture:** "ADOBECODEBANC","ABC" -> "BANC".

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B12

**Core:** Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.

**Acceptance example / fixture:** "1.02.0","1.2" -> 0.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B13

**Core:** Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.

**Acceptance example / fixture:** "babad" -> "bab".

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B14

**Core:** Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.

**Acceptance example / fixture:** "3,1-3,5" -> [1,2,3,5].

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-03-B15

**Core:** Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.

**Acceptance example / fixture:** "waterbottle","erbottlewat" -> true.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-LANGUAGE-03-I01

**Core:** Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.

**Acceptance example / fixture:** " ab-012 " -> "AB-012".

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I02

**Core:** Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.

**Acceptance example / fixture:** "abba" -> 2; "" -> 0.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I03

**Core:** Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.

**Acceptance example / fixture:** " a  b " -> "b a".

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I04

**Core:** Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.

**Acceptance example / fixture:** "A man, a plan, a canal: Panama" -> true.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I05

**Core:** Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.

**Acceptance example / fixture:** [flower,flow,flight] -> fl.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I06

**Core:** Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.

**Acceptance example / fixture:** "aaabb" -> [{character:a,count:3},{character:b,count:2}].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I07

**Core:** Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.

**Acceptance example / fixture:** "([)]" -> invalid index2; "([])" -> valid.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I08

**Core:** Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.

**Acceptance example / fixture:** "a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I09

**Core:** Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.

**Acceptance example / fixture:** [{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I10

**Core:** Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.

**Acceptance example / fixture:** "swiss" -> 1.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I11

**Core:** Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.

**Acceptance example / fixture:** "ADOBECODEBANC","ABC" -> "BANC".

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I12

**Core:** Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.

**Acceptance example / fixture:** "1.02.0","1.2" -> 0.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I13

**Core:** Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.

**Acceptance example / fixture:** "babad" -> "bab".

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I14

**Core:** Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.

**Acceptance example / fixture:** "3,1-3,5" -> [1,2,3,5].

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-03-I15

**Core:** Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.

**Acceptance example / fixture:** "waterbottle","erbottlewat" -> true.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-LANGUAGE-03-A01

**Core:** Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.

**Acceptance example / fixture:** " ab-012 " -> "AB-012".

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A02

**Core:** Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.

**Acceptance example / fixture:** "abba" -> 2; "" -> 0.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A03

**Core:** Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.

**Acceptance example / fixture:** " a  b " -> "b a".

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A04

**Core:** Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.

**Acceptance example / fixture:** "A man, a plan, a canal: Panama" -> true.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A05

**Core:** Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.

**Acceptance example / fixture:** [flower,flow,flight] -> fl.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A06

**Core:** Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.

**Acceptance example / fixture:** "aaabb" -> [{character:a,count:3},{character:b,count:2}].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A07

**Core:** Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.

**Acceptance example / fixture:** "([)]" -> invalid index2; "([])" -> valid.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A08

**Core:** Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.

**Acceptance example / fixture:** "a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A09

**Core:** Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.

**Acceptance example / fixture:** [{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A10

**Core:** Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.

**Acceptance example / fixture:** "swiss" -> 1.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A11

**Core:** Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.

**Acceptance example / fixture:** "ADOBECODEBANC","ABC" -> "BANC".

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A12

**Core:** Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.

**Acceptance example / fixture:** "1.02.0","1.2" -> 0.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A13

**Core:** Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.

**Acceptance example / fixture:** "babad" -> "bab".

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A14

**Core:** Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.

**Acceptance example / fixture:** "3,1-3,5" -> [1,2,3,5].

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-03-A15

**Core:** Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.

**Acceptance example / fixture:** "waterbottle","erbottlewat" -> true.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Exceptions and resource handling

### Beginner

#### JAVA-LANGUAGE-04-B01

**Core:** Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.

**Acceptance example / fixture:** a,2 followed by a,-1 ->a:1.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B02

**Core:** Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.

**Acceptance example / fixture:** lines a,empty,space,b ->total4,blank2,nonblank2.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B03

**Core:** Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.

**Acceptance example / fixture:** bytes010203,chunk2 ->copied3,samebytes.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B04

**Core:** Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.

**Acceptance example / fixture:** a\nb\nc\n,n2 ->a\n,b\n.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B05

**Core:** Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.

**Acceptance example / fixture:** a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B06

**Core:** Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.

**Acceptance example / fixture:** Existingold,newwritefails ->destinationold.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B07

**Core:** Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.

**Acceptance example / fixture:** bytes61FF ->offset1.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B08

**Core:** Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.

**Acceptance example / fixture:** a,b,c,n2 ->b,c.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B09

**Core:** Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.

**Acceptance example / fixture:** fn failsline2 ->line1written,line2error.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B10

**Core:** Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.

**Acceptance example / fixture:** data/a.csv valid;../secret invalid.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B11

**Core:** Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.

**Acceptance example / fixture:** 0102 vs0103 ->offset1.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B12

**Core:** Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.

**Acceptance example / fixture:** valid,bad,valid ->ok,errorline2,ok.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B13

**Core:** Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.

**Acceptance example / fixture:** Permissionfailure ->UNKNOWN rather thanempty.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B14

**Core:** Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.

**Acceptance example / fixture:** Bodythrows ->release1,originalerrorpropagates.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### JAVA-LANGUAGE-04-B15

**Core:** Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.

**Acceptance example / fixture:** Failurebeforecommit ->lastoffsetunchanged.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### JAVA-LANGUAGE-04-I01

**Core:** Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.

**Acceptance example / fixture:** a,2 followed by a,-1 ->a:1.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I02

**Core:** Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.

**Acceptance example / fixture:** lines a,empty,space,b ->total4,blank2,nonblank2.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I03

**Core:** Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.

**Acceptance example / fixture:** bytes010203,chunk2 ->copied3,samebytes.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I04

**Core:** Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.

**Acceptance example / fixture:** a\nb\nc\n,n2 ->a\n,b\n.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I05

**Core:** Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.

**Acceptance example / fixture:** a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I06

**Core:** Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.

**Acceptance example / fixture:** Existingold,newwritefails ->destinationold.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I07

**Core:** Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.

**Acceptance example / fixture:** bytes61FF ->offset1.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I08

**Core:** Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.

**Acceptance example / fixture:** a,b,c,n2 ->b,c.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I09

**Core:** Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.

**Acceptance example / fixture:** fn failsline2 ->line1written,line2error.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I10

**Core:** Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.

**Acceptance example / fixture:** data/a.csv valid;../secret invalid.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I11

**Core:** Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.

**Acceptance example / fixture:** 0102 vs0103 ->offset1.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I12

**Core:** Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.

**Acceptance example / fixture:** valid,bad,valid ->ok,errorline2,ok.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I13

**Core:** Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.

**Acceptance example / fixture:** Permissionfailure ->UNKNOWN rather thanempty.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I14

**Core:** Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.

**Acceptance example / fixture:** Bodythrows ->release1,originalerrorpropagates.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### JAVA-LANGUAGE-04-I15

**Core:** Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.

**Acceptance example / fixture:** Failurebeforecommit ->lastoffsetunchanged.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### JAVA-LANGUAGE-04-A01

**Core:** Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.

**Acceptance example / fixture:** a,2 followed by a,-1 ->a:1.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A02

**Core:** Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.

**Acceptance example / fixture:** lines a,empty,space,b ->total4,blank2,nonblank2.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A03

**Core:** Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.

**Acceptance example / fixture:** bytes010203,chunk2 ->copied3,samebytes.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A04

**Core:** Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.

**Acceptance example / fixture:** a\nb\nc\n,n2 ->a\n,b\n.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A05

**Core:** Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.

**Acceptance example / fixture:** a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A06

**Core:** Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.

**Acceptance example / fixture:** Existingold,newwritefails ->destinationold.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A07

**Core:** Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.

**Acceptance example / fixture:** bytes61FF ->offset1.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A08

**Core:** Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.

**Acceptance example / fixture:** a,b,c,n2 ->b,c.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A09

**Core:** Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.

**Acceptance example / fixture:** fn failsline2 ->line1written,line2error.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A10

**Core:** Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.

**Acceptance example / fixture:** data/a.csv valid;../secret invalid.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A11

**Core:** Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.

**Acceptance example / fixture:** 0102 vs0103 ->offset1.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A12

**Core:** Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.

**Acceptance example / fixture:** valid,bad,valid ->ok,errorline2,ok.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A13

**Core:** Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.

**Acceptance example / fixture:** Permissionfailure ->UNKNOWN rather thanempty.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A14

**Core:** Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.

**Acceptance example / fixture:** Bodythrows ->release1,originalerrorpropagates.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### JAVA-LANGUAGE-04-A15

**Core:** Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.

**Acceptance example / fixture:** Failurebeforecommit ->lastoffsetunchanged.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
