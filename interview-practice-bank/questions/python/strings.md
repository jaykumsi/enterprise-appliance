# Python: Strings

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Python; language-level code with injected I/O where needed.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Parsing and normalization

### Beginner

#### PY-STRINGS-01-B01

**Core:** Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.

**Acceptance example / fixture:** " ab-012 " -> "AB-012".

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B02

**Core:** Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.

**Acceptance example / fixture:** "abba" -> 2; "" -> 0.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B03

**Core:** Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.

**Acceptance example / fixture:** " a  b " -> "b a".

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B04

**Core:** Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.

**Acceptance example / fixture:** "A man, a plan, a canal: Panama" -> true.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B05

**Core:** Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.

**Acceptance example / fixture:** [flower,flow,flight] -> fl.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B06

**Core:** Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.

**Acceptance example / fixture:** "aaabb" -> [{character:a,count:3},{character:b,count:2}].

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B07

**Core:** Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.

**Acceptance example / fixture:** "([)]" -> invalid index2; "([])" -> valid.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B08

**Core:** Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.

**Acceptance example / fixture:** "a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B09

**Core:** Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.

**Acceptance example / fixture:** [{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B10

**Core:** Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.

**Acceptance example / fixture:** "swiss" -> 1.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B11

**Core:** Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.

**Acceptance example / fixture:** "ADOBECODEBANC","ABC" -> "BANC".

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B12

**Core:** Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.

**Acceptance example / fixture:** "1.02.0","1.2" -> 0.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B13

**Core:** Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.

**Acceptance example / fixture:** "babad" -> "bab".

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B14

**Core:** Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.

**Acceptance example / fixture:** "3,1-3,5" -> [1,2,3,5].

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-01-B15

**Core:** Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.

**Acceptance example / fixture:** "waterbottle","erbottlewat" -> true.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-STRINGS-01-I01

**Core:** Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.

**Acceptance example / fixture:** " ab-012 " -> "AB-012".

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I02

**Core:** Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.

**Acceptance example / fixture:** "abba" -> 2; "" -> 0.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I03

**Core:** Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.

**Acceptance example / fixture:** " a  b " -> "b a".

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I04

**Core:** Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.

**Acceptance example / fixture:** "A man, a plan, a canal: Panama" -> true.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I05

**Core:** Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.

**Acceptance example / fixture:** [flower,flow,flight] -> fl.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I06

**Core:** Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.

**Acceptance example / fixture:** "aaabb" -> [{character:a,count:3},{character:b,count:2}].

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I07

**Core:** Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.

**Acceptance example / fixture:** "([)]" -> invalid index2; "([])" -> valid.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I08

**Core:** Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.

**Acceptance example / fixture:** "a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I09

**Core:** Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.

**Acceptance example / fixture:** [{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I10

**Core:** Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.

**Acceptance example / fixture:** "swiss" -> 1.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I11

**Core:** Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.

**Acceptance example / fixture:** "ADOBECODEBANC","ABC" -> "BANC".

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I12

**Core:** Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.

**Acceptance example / fixture:** "1.02.0","1.2" -> 0.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I13

**Core:** Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.

**Acceptance example / fixture:** "babad" -> "bab".

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I14

**Core:** Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.

**Acceptance example / fixture:** "3,1-3,5" -> [1,2,3,5].

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-01-I15

**Core:** Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.

**Acceptance example / fixture:** "waterbottle","erbottlewat" -> true.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-STRINGS-01-A01

**Core:** Implement normalize_code(text): trim outer ASCII spaces,uppercase ASCII letters,and require two letters,hyphen,three digits. Other forms -> INVALID.

**Acceptance example / fixture:** " ab-012 " -> "AB-012".

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A02

**Core:** Implement longest_distinct(text),returning longest contiguous substring length in Unicode code points with no repeat.

**Acceptance example / fixture:** "abba" -> 2; "" -> 0.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A03

**Core:** Implement reverse_words(text),splitting on one or more ASCII spaces and joining reversed words with one space; other characters unchanged.

**Acceptance example / fixture:** " a  b " -> "b a".

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A04

**Core:** Implement palindrome(text),considering ASCII letters/digits only and ignoring ASCII letter case. Empty filtered text is true.

**Acceptance example / fixture:** "A man, a plan, a canal: Panama" -> true.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A05

**Core:** Implement common_prefix(strings) using Unicode code points; empty input -> empty string. Do not split supplementary characters into half units.

**Acceptance example / fixture:** [flower,flow,flight] -> fl.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A06

**Core:** Implement compress_runs(text),returning an array of {character,count} for consecutive Unicode code points. No lossy text encoding.

**Acceptance example / fixture:** "aaabb" -> [{character:a,count:3},{character:b,count:2}].

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A07

**Core:** Implement balanced_brackets(text) for characters()[]{} only. Return valid or first invalid zero-based code-point index; unclosed opener reports its index.

**Acceptance example / fixture:** "([)]" -> invalid index2; "([])" -> valid.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A08

**Core:** Implement escaped_split(text),splitting on unescaped commas. Backslash escapes comma or backslash only; dangling/unknown escape -> INVALID; retain empty fields.

**Acceptance example / fixture:** "a\\,b,c" interpreted with one escape before comma -> ["a,b","c"].

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A09

**Core:** Implement decode_runs(pairs) for {character,count},one Unicode code point and nonnegative integer count. Return concatenated text; enforce supplied max_output length before allocating.

**Acceptance example / fixture:** [{a,2},{b,1}],max3 -> aab; max2 -> TOO_LARGE.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A10

**Core:** Implement first_nonrepeating_position(text) in Unicode code points,returning index or null; comparison is case-sensitive.

**Acceptance example / fixture:** "swiss" -> 1.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A11

**Core:** Implement minimum_window(text,required) returning shortest substring containing every required code-point multiplicity. Ties prefer earliest start; no match -> null; empty required -> empty string.

**Acceptance example / fixture:** "ADOBECODEBANC","ABC" -> "BANC".

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A12

**Core:** Implement compare_versions(a,b) for dot-separated nonnegative integer components. Ignore leading component zeros and trailing zero components; reject empty components.

**Acceptance example / fixture:** "1.02.0","1.2" -> 0.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A13

**Core:** Implement longest_palindrome(text),returning longest contiguous code-point palindrome,ties earliest start.

**Acceptance example / fixture:** "babad" -> "bab".

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A14

**Core:** Implement expand_ranges(text) for comma-separated nonnegative integers or inclusive a-b ranges. Reject reversed ranges; return distinct integers ascending.

**Acceptance example / fixture:** "3,1-3,5" -> [1,2,3,5].

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-01-A15

**Core:** Implement is_rotation(a,b) on Unicode code-point strings. Require same length; empty strings are rotations. Do not sort characters.

**Acceptance example / fixture:** "waterbottle","erbottlewat" -> true.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Regular expressions

### Beginner

#### PY-STRINGS-02-B01

**Core:** Extract distinct standalone codes matching two uppercase ASCII letters,hyphen,three digits. Adjacent ASCII letter/digit invalidates a boundary. Preserve first occurrence.

**Acceptance example / fixture:** "AB-123 xAB-124 AB-125!" -> [AB-123,AB-125].

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B02

**Core:** Validate usernames: lowercase ASCII letter then2..19 lowercase letters/digits. Return VALID or INVALID with no partial match.

**Acceptance example / fixture:** abc -> VALID; 1abc -> INVALID.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B03

**Core:** Parse YYYY-MM-DD text and validate actual Gregorian calendar dates,not only the regex shape. Return canonical date or INVALID.

**Acceptance example / fixture:** 2024-02-29 valid; 2023-02-29 invalid.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B04

**Core:** Parse signed decimal text with optional minus and at most2 fractional digits,requiring digits before decimal. Return integer cents; no exponent/whitespace.

**Acceptance example / fixture:** -1.2 -> -120; .5 -> INVALID.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B05

**Core:** Extract key=value tokens with ASCII identifier keys and double-quoted values supporting escaped quote/backslash. Reject malformed nonspace text and duplicate keys.

**Acceptance example / fixture:** a="x y" b="z" -> {a:"x y",b:"z"}.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B06

**Core:** Validate IPv4 dotted decimal: exactly4 components0..255,no leading zeros except0. Return four integers or INVALID.

**Acceptance example / fixture:** 192.168.0.1 valid; 01.2.3.4 invalid.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B07

**Core:** Parse a log line LEVEL timestamp message,LEVEL in INFO,WARN,ERROR and timestamp integer>=0. Preserve the entire message after the second separator.

**Acceptance example / fixture:** "INFO 10 hello world" -> {level:INFO,time:10,message:"hello world"}.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B08

**Core:** Replace standalone ASCII secret assignments token=VALUE with token=[REDACTED],where VALUE is nonempty nonwhitespace text. Do not redact mytoken= text.

**Acceptance example / fixture:** "token=abc mytoken=def" -> "token=[REDACTED] mytoken=def".

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B09

**Core:** Extract @mentions from text with name[A-Za-z][A-Za-z0-9_]{0,19}; mention must not be preceded by an ASCII word character. Return occurrences with code-point offsets.

**Acceptance example / fixture:** "Hi @Ada and x@Bob" -> Ada only,offset3.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B10

**Core:** Validate order references ORD-YYYY-NNNN with year2000..2099 and exactly4 digits suffix. Return parsed year/sequence or INVALID.

**Acceptance example / fixture:** ORD-2024-0007 -> {year:2024,sequence:7}.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B11

**Core:** Parse ISO-like durations PT followed by optional hours then minutes then seconds,integer quantities,at least one field. Return total seconds; reject repeated/out-of-order fields.

**Acceptance example / fixture:** PT1H2M3S -> 3723; PT1M1H -> INVALID.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B12

**Core:** Extract decimal integer tokens bounded by non-word characters,allowing a leading minus. Return exact integers and original positions; do not capture digits embedded in IDs.

**Acceptance example / fixture:** "x12 -3 +4" -> -3 and4,not12.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B13

**Core:** Validate semantic versions major.minor.patch with nonnegative integer components,no leading zeros,optional hyphen prerelease[A-Za-z0-9.-]+. Return components and prerelease or INVALID.

**Acceptance example / fixture:** 1.2.3-beta -> parsed; 01.2.3 -> INVALID.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B14

**Core:** Implement wildcard_match(text,pattern) where ? matches one code point and * any sequence; backslash has no special meaning. Match the entire string without translating untrusted text into executable code.

**Acceptance example / fixture:** abc,a*c -> true; abc,a? -> false.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-STRINGS-02-B15

**Core:** Validate a password policy without logging the value: length12..64 code points,at least one ASCII uppercase,lowercase,digit,and one of!@#$; no whitespace. Return missing requirement names sorted.

**Acceptance example / fixture:** "Abcdefghij1!" -> no failures.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-STRINGS-02-I01

**Core:** Extract distinct standalone codes matching two uppercase ASCII letters,hyphen,three digits. Adjacent ASCII letter/digit invalidates a boundary. Preserve first occurrence.

**Acceptance example / fixture:** "AB-123 xAB-124 AB-125!" -> [AB-123,AB-125].

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I02

**Core:** Validate usernames: lowercase ASCII letter then2..19 lowercase letters/digits. Return VALID or INVALID with no partial match.

**Acceptance example / fixture:** abc -> VALID; 1abc -> INVALID.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I03

**Core:** Parse YYYY-MM-DD text and validate actual Gregorian calendar dates,not only the regex shape. Return canonical date or INVALID.

**Acceptance example / fixture:** 2024-02-29 valid; 2023-02-29 invalid.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I04

**Core:** Parse signed decimal text with optional minus and at most2 fractional digits,requiring digits before decimal. Return integer cents; no exponent/whitespace.

**Acceptance example / fixture:** -1.2 -> -120; .5 -> INVALID.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I05

**Core:** Extract key=value tokens with ASCII identifier keys and double-quoted values supporting escaped quote/backslash. Reject malformed nonspace text and duplicate keys.

**Acceptance example / fixture:** a="x y" b="z" -> {a:"x y",b:"z"}.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I06

**Core:** Validate IPv4 dotted decimal: exactly4 components0..255,no leading zeros except0. Return four integers or INVALID.

**Acceptance example / fixture:** 192.168.0.1 valid; 01.2.3.4 invalid.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I07

**Core:** Parse a log line LEVEL timestamp message,LEVEL in INFO,WARN,ERROR and timestamp integer>=0. Preserve the entire message after the second separator.

**Acceptance example / fixture:** "INFO 10 hello world" -> {level:INFO,time:10,message:"hello world"}.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I08

**Core:** Replace standalone ASCII secret assignments token=VALUE with token=[REDACTED],where VALUE is nonempty nonwhitespace text. Do not redact mytoken= text.

**Acceptance example / fixture:** "token=abc mytoken=def" -> "token=[REDACTED] mytoken=def".

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I09

**Core:** Extract @mentions from text with name[A-Za-z][A-Za-z0-9_]{0,19}; mention must not be preceded by an ASCII word character. Return occurrences with code-point offsets.

**Acceptance example / fixture:** "Hi @Ada and x@Bob" -> Ada only,offset3.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I10

**Core:** Validate order references ORD-YYYY-NNNN with year2000..2099 and exactly4 digits suffix. Return parsed year/sequence or INVALID.

**Acceptance example / fixture:** ORD-2024-0007 -> {year:2024,sequence:7}.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I11

**Core:** Parse ISO-like durations PT followed by optional hours then minutes then seconds,integer quantities,at least one field. Return total seconds; reject repeated/out-of-order fields.

**Acceptance example / fixture:** PT1H2M3S -> 3723; PT1M1H -> INVALID.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I12

**Core:** Extract decimal integer tokens bounded by non-word characters,allowing a leading minus. Return exact integers and original positions; do not capture digits embedded in IDs.

**Acceptance example / fixture:** "x12 -3 +4" -> -3 and4,not12.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I13

**Core:** Validate semantic versions major.minor.patch with nonnegative integer components,no leading zeros,optional hyphen prerelease[A-Za-z0-9.-]+. Return components and prerelease or INVALID.

**Acceptance example / fixture:** 1.2.3-beta -> parsed; 01.2.3 -> INVALID.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I14

**Core:** Implement wildcard_match(text,pattern) where ? matches one code point and * any sequence; backslash has no special meaning. Match the entire string without translating untrusted text into executable code.

**Acceptance example / fixture:** abc,a*c -> true; abc,a? -> false.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-STRINGS-02-I15

**Core:** Validate a password policy without logging the value: length12..64 code points,at least one ASCII uppercase,lowercase,digit,and one of!@#$; no whitespace. Return missing requirement names sorted.

**Acceptance example / fixture:** "Abcdefghij1!" -> no failures.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-STRINGS-02-A01

**Core:** Extract distinct standalone codes matching two uppercase ASCII letters,hyphen,three digits. Adjacent ASCII letter/digit invalidates a boundary. Preserve first occurrence.

**Acceptance example / fixture:** "AB-123 xAB-124 AB-125!" -> [AB-123,AB-125].

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A02

**Core:** Validate usernames: lowercase ASCII letter then2..19 lowercase letters/digits. Return VALID or INVALID with no partial match.

**Acceptance example / fixture:** abc -> VALID; 1abc -> INVALID.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A03

**Core:** Parse YYYY-MM-DD text and validate actual Gregorian calendar dates,not only the regex shape. Return canonical date or INVALID.

**Acceptance example / fixture:** 2024-02-29 valid; 2023-02-29 invalid.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A04

**Core:** Parse signed decimal text with optional minus and at most2 fractional digits,requiring digits before decimal. Return integer cents; no exponent/whitespace.

**Acceptance example / fixture:** -1.2 -> -120; .5 -> INVALID.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A05

**Core:** Extract key=value tokens with ASCII identifier keys and double-quoted values supporting escaped quote/backslash. Reject malformed nonspace text and duplicate keys.

**Acceptance example / fixture:** a="x y" b="z" -> {a:"x y",b:"z"}.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A06

**Core:** Validate IPv4 dotted decimal: exactly4 components0..255,no leading zeros except0. Return four integers or INVALID.

**Acceptance example / fixture:** 192.168.0.1 valid; 01.2.3.4 invalid.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A07

**Core:** Parse a log line LEVEL timestamp message,LEVEL in INFO,WARN,ERROR and timestamp integer>=0. Preserve the entire message after the second separator.

**Acceptance example / fixture:** "INFO 10 hello world" -> {level:INFO,time:10,message:"hello world"}.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A08

**Core:** Replace standalone ASCII secret assignments token=VALUE with token=[REDACTED],where VALUE is nonempty nonwhitespace text. Do not redact mytoken= text.

**Acceptance example / fixture:** "token=abc mytoken=def" -> "token=[REDACTED] mytoken=def".

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A09

**Core:** Extract @mentions from text with name[A-Za-z][A-Za-z0-9_]{0,19}; mention must not be preceded by an ASCII word character. Return occurrences with code-point offsets.

**Acceptance example / fixture:** "Hi @Ada and x@Bob" -> Ada only,offset3.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A10

**Core:** Validate order references ORD-YYYY-NNNN with year2000..2099 and exactly4 digits suffix. Return parsed year/sequence or INVALID.

**Acceptance example / fixture:** ORD-2024-0007 -> {year:2024,sequence:7}.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A11

**Core:** Parse ISO-like durations PT followed by optional hours then minutes then seconds,integer quantities,at least one field. Return total seconds; reject repeated/out-of-order fields.

**Acceptance example / fixture:** PT1H2M3S -> 3723; PT1M1H -> INVALID.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A12

**Core:** Extract decimal integer tokens bounded by non-word characters,allowing a leading minus. Return exact integers and original positions; do not capture digits embedded in IDs.

**Acceptance example / fixture:** "x12 -3 +4" -> -3 and4,not12.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A13

**Core:** Validate semantic versions major.minor.patch with nonnegative integer components,no leading zeros,optional hyphen prerelease[A-Za-z0-9.-]+. Return components and prerelease or INVALID.

**Acceptance example / fixture:** 1.2.3-beta -> parsed; 01.2.3 -> INVALID.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A14

**Core:** Implement wildcard_match(text,pattern) where ? matches one code point and * any sequence; backslash has no special meaning. Match the entire string without translating untrusted text into executable code.

**Acceptance example / fixture:** abc,a*c -> true; abc,a? -> false.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-STRINGS-02-A15

**Core:** Validate a password policy without logging the value: length12..64 code points,at least one ASCII uppercase,lowercase,digit,and one of!@#$; no whitespace. Return missing requirement names sorted.

**Acceptance example / fixture:** "Abcdefghij1!" -> no failures.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
