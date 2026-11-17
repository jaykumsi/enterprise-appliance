# Python: Reliability

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Python; language-level code with injected I/O where needed.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Exceptions and validation

### Beginner

#### PY-RELIABILITY-01-B01

**Core:** Validate rows with nonempty string id and positive integer qty. Booleans are not integers. Return accepted rows and rejected index/reasons sorted by field.

**Acceptance example / fixture:** [{id:a,qty:0}] -> rejected index0,reason qty.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B02

**Core:** Validate a date-range request requiring valid Gregorian start/end and start<=end. Return all field errors; reversed valid dates -> RANGE.

**Acceptance example / fixture:** 2024-02-30..2024-03-01 -> start error.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B03

**Core:** Validate port text as canonical decimal integer1..65535,no sign/whitespace/leading zeros. Return integer or field error.

**Acceptance example / fixture:** "080" -> error; "80" ->80.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B04

**Core:** Validate a batch of unique IDs. Reject all positions whose ID is repeated rather than choosing an arbitrary survivor; return rejected positions ascending.

**Acceptance example / fixture:** [a,b,a] -> rejected[0,2],accepted[b].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B05

**Core:** Validate nested order items: id nonempty,items array,each sku nonempty and qty positive integer. Return JSON-pointer-style paths for all errors sorted.

**Acceptance example / fixture:** {id:a,items:[{sku:"",qty:0}]} -> /items/0/qty,/items/0/sku.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B06

**Core:** Validate an enum transition Open->Paid->Shipped or Open->Cancelled. Illegal event returns INVALID_TRANSITION without changing original state.

**Acceptance example / fixture:** Paid->Cancelled -> rejected,still Paid.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B07

**Core:** Validate CSV-like integer fields without coercing empty/null/boolean to0. Return typed integer or TYPE,FORMAT,RANGE for supplied bounds.

**Acceptance example / fixture:** text"0",bounds0..2 ->0; empty -> FORMAT.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B08

**Core:** Validate percentages as integer0..100 and amounts as nonnegative integer cents; collect independent field errors before calculation.

**Acceptance example / fixture:** pct101,amount-1 -> errors amount,pct.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B09

**Core:** Validate object keys against required[id,qty] and optional[note]. Return missing and unknown keys separately,sorted.

**Acceptance example / fixture:** {id:a,quantity:1} -> missing qty,unknown quantity.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B10

**Core:** Validate a finite dependency graph's referenced nodes before cycle checking. Report all missing references first,otherwise return a cycle witness if present.

**Acceptance example / fixture:** nodes[a],edgea->b -> missing[b].

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B11

**Core:** Validate Unicode display names: after trimming ASCII outer spaces,require1..40 code points and no control characters U+0000..001F. Return normalized name or errors.

**Acceptance example / fixture:** " Ada " -> Ada; newline inside -> control error.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B12

**Core:** Validate checksums as exactly64 lowercase hexadecimal characters; distinguish missing,wrong type and invalid format.

**Acceptance example / fixture:** 64 a characters -> valid; uppercase A -> FORMAT.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B13

**Core:** Validate schema compatibility old/new field type/required maps: optional additions allowed,removal/type change/optional->required rejected.

**Acceptance example / fixture:** Add optional note -> compatible; cents type changed -> incompatible.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B14

**Core:** Implement validate_then_commit(batch,validator,store). Validate every item first; any error means zero store calls. Return all item errors.

**Acceptance example / fixture:** One invalid of3 -> no writes.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-01-B15

**Core:** Implement safe_error(exception) mapping known validation/conflict/not-found types to safe codes; unknown error -> INTERNAL and sanitized message,never stack/secret text.

**Acceptance example / fixture:** Unknown exception containing synthetic password -> INTERNAL with no password.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-RELIABILITY-01-I01

**Core:** Validate rows with nonempty string id and positive integer qty. Booleans are not integers. Return accepted rows and rejected index/reasons sorted by field.

**Acceptance example / fixture:** [{id:a,qty:0}] -> rejected index0,reason qty.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I02

**Core:** Validate a date-range request requiring valid Gregorian start/end and start<=end. Return all field errors; reversed valid dates -> RANGE.

**Acceptance example / fixture:** 2024-02-30..2024-03-01 -> start error.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I03

**Core:** Validate port text as canonical decimal integer1..65535,no sign/whitespace/leading zeros. Return integer or field error.

**Acceptance example / fixture:** "080" -> error; "80" ->80.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I04

**Core:** Validate a batch of unique IDs. Reject all positions whose ID is repeated rather than choosing an arbitrary survivor; return rejected positions ascending.

**Acceptance example / fixture:** [a,b,a] -> rejected[0,2],accepted[b].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I05

**Core:** Validate nested order items: id nonempty,items array,each sku nonempty and qty positive integer. Return JSON-pointer-style paths for all errors sorted.

**Acceptance example / fixture:** {id:a,items:[{sku:"",qty:0}]} -> /items/0/qty,/items/0/sku.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I06

**Core:** Validate an enum transition Open->Paid->Shipped or Open->Cancelled. Illegal event returns INVALID_TRANSITION without changing original state.

**Acceptance example / fixture:** Paid->Cancelled -> rejected,still Paid.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I07

**Core:** Validate CSV-like integer fields without coercing empty/null/boolean to0. Return typed integer or TYPE,FORMAT,RANGE for supplied bounds.

**Acceptance example / fixture:** text"0",bounds0..2 ->0; empty -> FORMAT.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I08

**Core:** Validate percentages as integer0..100 and amounts as nonnegative integer cents; collect independent field errors before calculation.

**Acceptance example / fixture:** pct101,amount-1 -> errors amount,pct.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I09

**Core:** Validate object keys against required[id,qty] and optional[note]. Return missing and unknown keys separately,sorted.

**Acceptance example / fixture:** {id:a,quantity:1} -> missing qty,unknown quantity.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I10

**Core:** Validate a finite dependency graph's referenced nodes before cycle checking. Report all missing references first,otherwise return a cycle witness if present.

**Acceptance example / fixture:** nodes[a],edgea->b -> missing[b].

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I11

**Core:** Validate Unicode display names: after trimming ASCII outer spaces,require1..40 code points and no control characters U+0000..001F. Return normalized name or errors.

**Acceptance example / fixture:** " Ada " -> Ada; newline inside -> control error.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I12

**Core:** Validate checksums as exactly64 lowercase hexadecimal characters; distinguish missing,wrong type and invalid format.

**Acceptance example / fixture:** 64 a characters -> valid; uppercase A -> FORMAT.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I13

**Core:** Validate schema compatibility old/new field type/required maps: optional additions allowed,removal/type change/optional->required rejected.

**Acceptance example / fixture:** Add optional note -> compatible; cents type changed -> incompatible.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I14

**Core:** Implement validate_then_commit(batch,validator,store). Validate every item first; any error means zero store calls. Return all item errors.

**Acceptance example / fixture:** One invalid of3 -> no writes.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-01-I15

**Core:** Implement safe_error(exception) mapping known validation/conflict/not-found types to safe codes; unknown error -> INTERNAL and sanitized message,never stack/secret text.

**Acceptance example / fixture:** Unknown exception containing synthetic password -> INTERNAL with no password.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-RELIABILITY-01-A01

**Core:** Validate rows with nonempty string id and positive integer qty. Booleans are not integers. Return accepted rows and rejected index/reasons sorted by field.

**Acceptance example / fixture:** [{id:a,qty:0}] -> rejected index0,reason qty.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A02

**Core:** Validate a date-range request requiring valid Gregorian start/end and start<=end. Return all field errors; reversed valid dates -> RANGE.

**Acceptance example / fixture:** 2024-02-30..2024-03-01 -> start error.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A03

**Core:** Validate port text as canonical decimal integer1..65535,no sign/whitespace/leading zeros. Return integer or field error.

**Acceptance example / fixture:** "080" -> error; "80" ->80.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A04

**Core:** Validate a batch of unique IDs. Reject all positions whose ID is repeated rather than choosing an arbitrary survivor; return rejected positions ascending.

**Acceptance example / fixture:** [a,b,a] -> rejected[0,2],accepted[b].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A05

**Core:** Validate nested order items: id nonempty,items array,each sku nonempty and qty positive integer. Return JSON-pointer-style paths for all errors sorted.

**Acceptance example / fixture:** {id:a,items:[{sku:"",qty:0}]} -> /items/0/qty,/items/0/sku.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A06

**Core:** Validate an enum transition Open->Paid->Shipped or Open->Cancelled. Illegal event returns INVALID_TRANSITION without changing original state.

**Acceptance example / fixture:** Paid->Cancelled -> rejected,still Paid.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A07

**Core:** Validate CSV-like integer fields without coercing empty/null/boolean to0. Return typed integer or TYPE,FORMAT,RANGE for supplied bounds.

**Acceptance example / fixture:** text"0",bounds0..2 ->0; empty -> FORMAT.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A08

**Core:** Validate percentages as integer0..100 and amounts as nonnegative integer cents; collect independent field errors before calculation.

**Acceptance example / fixture:** pct101,amount-1 -> errors amount,pct.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A09

**Core:** Validate object keys against required[id,qty] and optional[note]. Return missing and unknown keys separately,sorted.

**Acceptance example / fixture:** {id:a,quantity:1} -> missing qty,unknown quantity.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A10

**Core:** Validate a finite dependency graph's referenced nodes before cycle checking. Report all missing references first,otherwise return a cycle witness if present.

**Acceptance example / fixture:** nodes[a],edgea->b -> missing[b].

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A11

**Core:** Validate Unicode display names: after trimming ASCII outer spaces,require1..40 code points and no control characters U+0000..001F. Return normalized name or errors.

**Acceptance example / fixture:** " Ada " -> Ada; newline inside -> control error.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A12

**Core:** Validate checksums as exactly64 lowercase hexadecimal characters; distinguish missing,wrong type and invalid format.

**Acceptance example / fixture:** 64 a characters -> valid; uppercase A -> FORMAT.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A13

**Core:** Validate schema compatibility old/new field type/required maps: optional additions allowed,removal/type change/optional->required rejected.

**Acceptance example / fixture:** Add optional note -> compatible; cents type changed -> incompatible.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A14

**Core:** Implement validate_then_commit(batch,validator,store). Validate every item first; any error means zero store calls. Return all item errors.

**Acceptance example / fixture:** One invalid of3 -> no writes.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-01-A15

**Core:** Implement safe_error(exception) mapping known validation/conflict/not-found types to safe codes; unknown error -> INTERNAL and sanitized message,never stack/secret text.

**Acceptance example / fixture:** Unknown exception containing synthetic password -> INTERNAL with no password.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Files and context managers

### Beginner

#### PY-RELIABILITY-02-B01

**Core:** Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.

**Acceptance example / fixture:** a,2 followed by a,-1 ->a:1.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B02

**Core:** Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.

**Acceptance example / fixture:** lines a,empty,space,b ->total4,blank2,nonblank2.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B03

**Core:** Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.

**Acceptance example / fixture:** bytes010203,chunk2 ->copied3,samebytes.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B04

**Core:** Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.

**Acceptance example / fixture:** a\nb\nc\n,n2 ->a\n,b\n.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B05

**Core:** Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.

**Acceptance example / fixture:** a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B06

**Core:** Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.

**Acceptance example / fixture:** Existingold,newwritefails ->destinationold.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B07

**Core:** Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.

**Acceptance example / fixture:** bytes61FF ->offset1.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B08

**Core:** Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.

**Acceptance example / fixture:** a,b,c,n2 ->b,c.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B09

**Core:** Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.

**Acceptance example / fixture:** fn failsline2 ->line1written,line2error.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B10

**Core:** Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.

**Acceptance example / fixture:** data/a.csv valid;../secret invalid.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B11

**Core:** Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.

**Acceptance example / fixture:** 0102 vs0103 ->offset1.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B12

**Core:** Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.

**Acceptance example / fixture:** valid,bad,valid ->ok,errorline2,ok.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B13

**Core:** Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.

**Acceptance example / fixture:** Permissionfailure ->UNKNOWN rather thanempty.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B14

**Core:** Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.

**Acceptance example / fixture:** Bodythrows ->release1,originalerrorpropagates.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-02-B15

**Core:** Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.

**Acceptance example / fixture:** Failurebeforecommit ->lastoffsetunchanged.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-RELIABILITY-02-I01

**Core:** Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.

**Acceptance example / fixture:** a,2 followed by a,-1 ->a:1.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I02

**Core:** Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.

**Acceptance example / fixture:** lines a,empty,space,b ->total4,blank2,nonblank2.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I03

**Core:** Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.

**Acceptance example / fixture:** bytes010203,chunk2 ->copied3,samebytes.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I04

**Core:** Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.

**Acceptance example / fixture:** a\nb\nc\n,n2 ->a\n,b\n.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I05

**Core:** Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.

**Acceptance example / fixture:** a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I06

**Core:** Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.

**Acceptance example / fixture:** Existingold,newwritefails ->destinationold.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I07

**Core:** Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.

**Acceptance example / fixture:** bytes61FF ->offset1.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I08

**Core:** Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.

**Acceptance example / fixture:** a,b,c,n2 ->b,c.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I09

**Core:** Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.

**Acceptance example / fixture:** fn failsline2 ->line1written,line2error.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I10

**Core:** Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.

**Acceptance example / fixture:** data/a.csv valid;../secret invalid.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I11

**Core:** Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.

**Acceptance example / fixture:** 0102 vs0103 ->offset1.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I12

**Core:** Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.

**Acceptance example / fixture:** valid,bad,valid ->ok,errorline2,ok.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I13

**Core:** Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.

**Acceptance example / fixture:** Permissionfailure ->UNKNOWN rather thanempty.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I14

**Core:** Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.

**Acceptance example / fixture:** Bodythrows ->release1,originalerrorpropagates.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-02-I15

**Core:** Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.

**Acceptance example / fixture:** Failurebeforecommit ->lastoffsetunchanged.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-RELIABILITY-02-A01

**Core:** Parse a text stream of id,integer_cents lines,skip blank lines,sum per id sorted. Malformed nonblank line ->INVALID with one-based number. Close only resources opened inside your function.

**Acceptance example / fixture:** a,2 followed by a,-1 ->a:1.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A02

**Core:** Count nonblank logical lines from a text stream without loading it entirely. Whitespace-only line is blank; report total/blank/nonblank.

**Acceptance example / fixture:** lines a,empty,space,b ->total4,blank2,nonblank2.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A03

**Core:** Copy a binary stream to an injected output in bounded chunks,return bytes copied and propagate write failure. Never close caller-owned streams.

**Acceptance example / fixture:** bytes010203,chunk2 ->copied3,samebytes.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A04

**Core:** Return first n text lines lazily including original newline content,n>=0. n0 reads nothing and does not close caller stream.

**Acceptance example / fixture:** a\nb\nc\n,n2 ->a\n,b\n.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A05

**Core:** Merge two key-sorted ledger streams id,cents,emitting signed totals per id in key order with bounded lookahead. Reject unsorted input.

**Acceptance example / fixture:** a:2,c:3 plusa:-1,b:4 ->a:1,b:4,c:3.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A06

**Core:** Implement atomic_replace(path,content,fs) through injected file APIs:write temp,flush/close,then rename. Failure before rename preserves old destination.

**Acceptance example / fixture:** Existingold,newwritefails ->destinationold.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A07

**Core:** Read UTF-8 bytes strictly and report INVALID_ENCODING at first bad byte offset;do not silently replace malformed bytes.

**Acceptance example / fixture:** bytes61FF ->offset1.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A08

**Core:** Extract the last n text lines using bounded retained lines,n>=0. Preserve original ordering,newlines optional only as stated by caller flag.

**Acceptance example / fixture:** a,b,c,n2 ->b,c.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A09

**Core:** Implement line_transform(input,output,fn). Call fn per logical line,write transformed text;stop on first error with input line number;close owned resources.

**Acceptance example / fixture:** fn failsline2 ->line1written,line2error.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A10

**Core:** Read a manifest of safe relative paths:reject absolute paths,drive prefixes,and any dot-dot component. Do not open a rejected path.

**Acceptance example / fixture:** data/a.csv valid;../secret invalid.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A11

**Core:** Compare two binary streams in bounded chunks,return first differing byte offset or null. A shorter stream differs at its end.

**Acceptance example / fixture:** 0102 vs0103 ->offset1.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A12

**Core:** Parse NDJSON stream,one JSON document per nonblank line. Return per-line valid document/error without losing subsequent valid lines.

**Acceptance example / fixture:** valid,bad,valid ->ok,errorline2,ok.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A13

**Core:** Build a per-file metadata report from injected fs:exists,size,readable. A stat/read failure is UNKNOWN,not a zero-byte file.

**Acceptance example / fixture:** Permissionfailure ->UNKNOWN rather thanempty.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A14

**Core:** Implement a context-manager/resource wrapper releasing an injected handle exactly once on success or exception. Preserve the original application error.

**Acceptance example / fixture:** Bodythrows ->release1,originalerrorpropagates.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-02-A15

**Core:** Implement restartable line processing using byte-safe checkpoints only at complete UTF-8 line boundaries. Return next committed offset after output commit.

**Acceptance example / fixture:** Failurebeforecommit ->lastoffsetunchanged.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## CSV and JSON

### Beginner

#### PY-RELIABILITY-03-B01

**Core:** Parse CSV header id,amount with quoted commas/escaped quotes. Require nonempty id and signed integer amount;return records or logical record errors.

**Acceptance example / fixture:** "a,b",12 ->id a,b,amount12.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B02

**Core:** Flatten JSON orders with items arrays into order_id,sku,qty rows preserving item order. Missing/null items ->empty;nonarray ->rejected.

**Acceptance example / fixture:** o1 itemsA2,B1 ->2rows.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B03

**Core:** Write CSV for records containing comma,quote,newline values using a standards-aware writer,then parse back and prove exact round trip.

**Acceptance example / fixture:** id a,b remains onefield.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B04

**Core:** Compare two JSON objects structurally,ignoring object-field order but retaining array order and distinguishing number,string,boolean,null.

**Acceptance example / fixture:** {a:1,b:2} equals reorderedobject;[1,2] differs[2,1].

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B05

**Core:** Validate NDJSON one document per nonblank line with nonempty id,integer cents;return accepted rows plus line/error paths.

**Acceptance example / fixture:** line2 missingid ->rejectline2 only.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B06

**Core:** Normalize a JSON record schema requiring id:string and qty:positive integer. Extra keys retained in a separate metadata object,not silently assigned to protected fields.

**Acceptance example / fixture:** {id:a,qty:2,admin:true} ->metadata admin,notauthority.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B07

**Core:** Convert a CSV row with named optional columns to JSON,null only for an explicitly supplied NULL marker;empty string stays empty.

**Acceptance example / fixture:** noteempty ->"";noteNULL ->null.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B08

**Core:** Parse a JSON array of versioned records and select highest version per id;equal version/different payload ->CONFLICT.

**Acceptance example / fixture:** a:v1/x,a:v2/y ->a:v2/y.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B09

**Core:** Validate nested JSON depth<=supplied positive limit and total scalar count<=budget before transformation. Return precise limit error.

**Acceptance example / fixture:** depth3,limit2 ->DEPTH_LIMIT.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B10

**Core:** Flatten nested JSON objects into escaped JSON-pointer paths;arrays retain numeric indices,null remains a leaf. Root scalar path is empty.

**Acceptance example / fixture:** {a:[1,null]} ->/a/0:1,/a/1:null.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B11

**Core:** Reconstruct JSON from nonconflicting pointer/leaf pairs. Reject a path that is both a scalar and an ancestor.

**Acceptance example / fixture:** /a:1 and/a/b:2 ->CONFLICT.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B12

**Core:** Parse CSV with required unique headers;return duplicate/missing/unknown header findings before reading data. Required[id,cents],optional[note].

**Acceptance example / fixture:** id,id ->duplicateid,missingcents.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B13

**Core:** Convert exact decimal JSON string fields into integer cents using optional minus/digits/atmost2 fractiondigits. Reject numeric floating inputs instead of guessing original precision.

**Acceptance example / fixture:** "1.25" ->125;numeric1.25 ->TYPE.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B14

**Core:** Implement streaming JSON-array output for an iterator of JSON-compatible records. Correctly place commas/brackets for empty/single/multiple input;never materialize all records.

**Acceptance example / fixture:** []iterator ->"[]".

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-RELIABILITY-03-B15

**Core:** Reconcile CSV and JSON representations of the same unique-ID ledger,comparing exact cents and text values after explicit parsing rules.

**Acceptance example / fixture:** CSVa,2 andJSONa cents3 ->changeda.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-RELIABILITY-03-I01

**Core:** Parse CSV header id,amount with quoted commas/escaped quotes. Require nonempty id and signed integer amount;return records or logical record errors.

**Acceptance example / fixture:** "a,b",12 ->id a,b,amount12.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I02

**Core:** Flatten JSON orders with items arrays into order_id,sku,qty rows preserving item order. Missing/null items ->empty;nonarray ->rejected.

**Acceptance example / fixture:** o1 itemsA2,B1 ->2rows.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I03

**Core:** Write CSV for records containing comma,quote,newline values using a standards-aware writer,then parse back and prove exact round trip.

**Acceptance example / fixture:** id a,b remains onefield.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I04

**Core:** Compare two JSON objects structurally,ignoring object-field order but retaining array order and distinguishing number,string,boolean,null.

**Acceptance example / fixture:** {a:1,b:2} equals reorderedobject;[1,2] differs[2,1].

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I05

**Core:** Validate NDJSON one document per nonblank line with nonempty id,integer cents;return accepted rows plus line/error paths.

**Acceptance example / fixture:** line2 missingid ->rejectline2 only.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I06

**Core:** Normalize a JSON record schema requiring id:string and qty:positive integer. Extra keys retained in a separate metadata object,not silently assigned to protected fields.

**Acceptance example / fixture:** {id:a,qty:2,admin:true} ->metadata admin,notauthority.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I07

**Core:** Convert a CSV row with named optional columns to JSON,null only for an explicitly supplied NULL marker;empty string stays empty.

**Acceptance example / fixture:** noteempty ->"";noteNULL ->null.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I08

**Core:** Parse a JSON array of versioned records and select highest version per id;equal version/different payload ->CONFLICT.

**Acceptance example / fixture:** a:v1/x,a:v2/y ->a:v2/y.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I09

**Core:** Validate nested JSON depth<=supplied positive limit and total scalar count<=budget before transformation. Return precise limit error.

**Acceptance example / fixture:** depth3,limit2 ->DEPTH_LIMIT.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I10

**Core:** Flatten nested JSON objects into escaped JSON-pointer paths;arrays retain numeric indices,null remains a leaf. Root scalar path is empty.

**Acceptance example / fixture:** {a:[1,null]} ->/a/0:1,/a/1:null.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I11

**Core:** Reconstruct JSON from nonconflicting pointer/leaf pairs. Reject a path that is both a scalar and an ancestor.

**Acceptance example / fixture:** /a:1 and/a/b:2 ->CONFLICT.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I12

**Core:** Parse CSV with required unique headers;return duplicate/missing/unknown header findings before reading data. Required[id,cents],optional[note].

**Acceptance example / fixture:** id,id ->duplicateid,missingcents.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I13

**Core:** Convert exact decimal JSON string fields into integer cents using optional minus/digits/atmost2 fractiondigits. Reject numeric floating inputs instead of guessing original precision.

**Acceptance example / fixture:** "1.25" ->125;numeric1.25 ->TYPE.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I14

**Core:** Implement streaming JSON-array output for an iterator of JSON-compatible records. Correctly place commas/brackets for empty/single/multiple input;never materialize all records.

**Acceptance example / fixture:** []iterator ->"[]".

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-RELIABILITY-03-I15

**Core:** Reconcile CSV and JSON representations of the same unique-ID ledger,comparing exact cents and text values after explicit parsing rules.

**Acceptance example / fixture:** CSVa,2 andJSONa cents3 ->changeda.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-RELIABILITY-03-A01

**Core:** Parse CSV header id,amount with quoted commas/escaped quotes. Require nonempty id and signed integer amount;return records or logical record errors.

**Acceptance example / fixture:** "a,b",12 ->id a,b,amount12.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A02

**Core:** Flatten JSON orders with items arrays into order_id,sku,qty rows preserving item order. Missing/null items ->empty;nonarray ->rejected.

**Acceptance example / fixture:** o1 itemsA2,B1 ->2rows.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A03

**Core:** Write CSV for records containing comma,quote,newline values using a standards-aware writer,then parse back and prove exact round trip.

**Acceptance example / fixture:** id a,b remains onefield.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A04

**Core:** Compare two JSON objects structurally,ignoring object-field order but retaining array order and distinguishing number,string,boolean,null.

**Acceptance example / fixture:** {a:1,b:2} equals reorderedobject;[1,2] differs[2,1].

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A05

**Core:** Validate NDJSON one document per nonblank line with nonempty id,integer cents;return accepted rows plus line/error paths.

**Acceptance example / fixture:** line2 missingid ->rejectline2 only.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A06

**Core:** Normalize a JSON record schema requiring id:string and qty:positive integer. Extra keys retained in a separate metadata object,not silently assigned to protected fields.

**Acceptance example / fixture:** {id:a,qty:2,admin:true} ->metadata admin,notauthority.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A07

**Core:** Convert a CSV row with named optional columns to JSON,null only for an explicitly supplied NULL marker;empty string stays empty.

**Acceptance example / fixture:** noteempty ->"";noteNULL ->null.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A08

**Core:** Parse a JSON array of versioned records and select highest version per id;equal version/different payload ->CONFLICT.

**Acceptance example / fixture:** a:v1/x,a:v2/y ->a:v2/y.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A09

**Core:** Validate nested JSON depth<=supplied positive limit and total scalar count<=budget before transformation. Return precise limit error.

**Acceptance example / fixture:** depth3,limit2 ->DEPTH_LIMIT.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A10

**Core:** Flatten nested JSON objects into escaped JSON-pointer paths;arrays retain numeric indices,null remains a leaf. Root scalar path is empty.

**Acceptance example / fixture:** {a:[1,null]} ->/a/0:1,/a/1:null.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A11

**Core:** Reconstruct JSON from nonconflicting pointer/leaf pairs. Reject a path that is both a scalar and an ancestor.

**Acceptance example / fixture:** /a:1 and/a/b:2 ->CONFLICT.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A12

**Core:** Parse CSV with required unique headers;return duplicate/missing/unknown header findings before reading data. Required[id,cents],optional[note].

**Acceptance example / fixture:** id,id ->duplicateid,missingcents.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A13

**Core:** Convert exact decimal JSON string fields into integer cents using optional minus/digits/atmost2 fractiondigits. Reject numeric floating inputs instead of guessing original precision.

**Acceptance example / fixture:** "1.25" ->125;numeric1.25 ->TYPE.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A14

**Core:** Implement streaming JSON-array output for an iterator of JSON-compatible records. Correctly place commas/brackets for empty/single/multiple input;never materialize all records.

**Acceptance example / fixture:** []iterator ->"[]".

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-RELIABILITY-03-A15

**Core:** Reconcile CSV and JSON representations of the same unique-ID ledger,comparing exact cents and text values after explicit parsing rules.

**Acceptance example / fixture:** CSVa,2 andJSONa cents3 ->changeda.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
