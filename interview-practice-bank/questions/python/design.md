# Python: Design

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Python; language-level code with injected I/O where needed.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Classes and invariants

### Beginner

#### PY-DESIGN-01-B01

**Core:** Implement Inventory reserve/release on initial A5. Invalid qty/unknown SKU returns false; release cannot exceed reservations. Preserve available+reserved.

**Acceptance example / fixture:** reserveA3 true,releaseA4 false -> available2,reserved3.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B02

**Core:** Implement BankAccount deposit/withdraw in integer cents. Positive amounts only; no overdraft; failed withdrawal leaves balance unchanged.

**Acceptance example / fixture:** initial10,withdraw11 ->false,balance10.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B03

**Core:** Implement immutable Money(currency,cents),three uppercase currency letters; add only identical currency,with explicit overflow policy.

**Acceptance example / fixture:** USD100+USD-20 ->USD80; USD+EUR ->INVALID.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B04

**Core:** Implement bounded FIFO Queue(capacity) with put/get,return FULL/EMPTY without mutation on rejection. Capacity positive.

**Acceptance example / fixture:** cap2,put a,b,c ->thirdFULL;get ->a.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B05

**Core:** Implement Stack with push,pop,peek and snapshot independent of future mutation. Empty pop/peek ->EMPTY.

**Acceptance example / fixture:** push a,b;pop ->b;snapshot[a].

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B06

**Core:** Implement Reservation state Open->Confirmed->Completed or Open->Cancelled. Rejected transitions preserve state and version.

**Acceptance example / fixture:** Confirmed->Cancelled ->INVALID,stillConfirmed.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B07

**Core:** Implement immutable DateRange(start,end) using integer half-open bounds,start<=end. intersect returns overlap or an empty range at max(start).

**Acceptance example / fixture:** [1,5) intersect[3,7) ->[3,5).

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B08

**Core:** Implement ShoppingCart keyed SKU with positive integer quantities and exact cents. Set quantity0 removes; invalid update changes nothing.

**Acceptance example / fixture:** Aprice2,qty3 ->total6;setA0 ->empty.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B09

**Core:** Implement Counter instances with atomic-by-contract add and snapshot but no shared state between instances. Detect declared integer overflow.

**Acceptance example / fixture:** instances1,1;first.add2 ->3,second1.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B10

**Core:** Implement Task with pending,running,succeeded,failed. Only pending->running and running->terminal allowed; result only for succeeded,error only for failed.

**Acceptance example / fixture:** pending->succeeded ->INVALID.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B11

**Core:** Implement RateLimiter capacity2,refill1 per integer second using injected monotonic clock. Accepted acquire consumes1; invalid backward clock ->INVALID.

**Acceptance example / fixture:** t0 two accepted,thirdrejected;t1 one accepted.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B12

**Core:** Implement versioned Document.update(expected_version,text). Initial version1; success increments; stale expected rejects without changing text.

**Acceptance example / fixture:** update1,x ->v2;update1,y ->CONFLICT.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B13

**Core:** Implement SeatMap reserve(seat,owner),release(seat,owner). Only owner may release; reserving same seat/owner again is idempotent; other owner conflicts.

**Acceptance example / fixture:** A byu thenA byv ->CONFLICT;releaseA byv denied.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B14

**Core:** Implement a dependency-injected Checkout using SKU price lookup and payment gateway. Validate every quantity/SKU before charging exactly once.

**Acceptance example / fixture:** A200,qty2 ->charge400;unknownSKU ->zerocharges.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-01-B15

**Core:** Implement ExpiringValue with injected clock,put(value,ttl),get(). ttl positive; value expires when now>=inserted+ttl. Do not reset expiry on read.

**Acceptance example / fixture:** putx at0,ttl5;get4 ->x;get5 ->NOT_FOUND.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-DESIGN-01-I01

**Core:** Implement Inventory reserve/release on initial A5. Invalid qty/unknown SKU returns false; release cannot exceed reservations. Preserve available+reserved.

**Acceptance example / fixture:** reserveA3 true,releaseA4 false -> available2,reserved3.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I02

**Core:** Implement BankAccount deposit/withdraw in integer cents. Positive amounts only; no overdraft; failed withdrawal leaves balance unchanged.

**Acceptance example / fixture:** initial10,withdraw11 ->false,balance10.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I03

**Core:** Implement immutable Money(currency,cents),three uppercase currency letters; add only identical currency,with explicit overflow policy.

**Acceptance example / fixture:** USD100+USD-20 ->USD80; USD+EUR ->INVALID.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I04

**Core:** Implement bounded FIFO Queue(capacity) with put/get,return FULL/EMPTY without mutation on rejection. Capacity positive.

**Acceptance example / fixture:** cap2,put a,b,c ->thirdFULL;get ->a.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I05

**Core:** Implement Stack with push,pop,peek and snapshot independent of future mutation. Empty pop/peek ->EMPTY.

**Acceptance example / fixture:** push a,b;pop ->b;snapshot[a].

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I06

**Core:** Implement Reservation state Open->Confirmed->Completed or Open->Cancelled. Rejected transitions preserve state and version.

**Acceptance example / fixture:** Confirmed->Cancelled ->INVALID,stillConfirmed.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I07

**Core:** Implement immutable DateRange(start,end) using integer half-open bounds,start<=end. intersect returns overlap or an empty range at max(start).

**Acceptance example / fixture:** [1,5) intersect[3,7) ->[3,5).

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I08

**Core:** Implement ShoppingCart keyed SKU with positive integer quantities and exact cents. Set quantity0 removes; invalid update changes nothing.

**Acceptance example / fixture:** Aprice2,qty3 ->total6;setA0 ->empty.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I09

**Core:** Implement Counter instances with atomic-by-contract add and snapshot but no shared state between instances. Detect declared integer overflow.

**Acceptance example / fixture:** instances1,1;first.add2 ->3,second1.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I10

**Core:** Implement Task with pending,running,succeeded,failed. Only pending->running and running->terminal allowed; result only for succeeded,error only for failed.

**Acceptance example / fixture:** pending->succeeded ->INVALID.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I11

**Core:** Implement RateLimiter capacity2,refill1 per integer second using injected monotonic clock. Accepted acquire consumes1; invalid backward clock ->INVALID.

**Acceptance example / fixture:** t0 two accepted,thirdrejected;t1 one accepted.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I12

**Core:** Implement versioned Document.update(expected_version,text). Initial version1; success increments; stale expected rejects without changing text.

**Acceptance example / fixture:** update1,x ->v2;update1,y ->CONFLICT.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I13

**Core:** Implement SeatMap reserve(seat,owner),release(seat,owner). Only owner may release; reserving same seat/owner again is idempotent; other owner conflicts.

**Acceptance example / fixture:** A byu thenA byv ->CONFLICT;releaseA byv denied.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I14

**Core:** Implement a dependency-injected Checkout using SKU price lookup and payment gateway. Validate every quantity/SKU before charging exactly once.

**Acceptance example / fixture:** A200,qty2 ->charge400;unknownSKU ->zerocharges.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-01-I15

**Core:** Implement ExpiringValue with injected clock,put(value,ttl),get(). ttl positive; value expires when now>=inserted+ttl. Do not reset expiry on read.

**Acceptance example / fixture:** putx at0,ttl5;get4 ->x;get5 ->NOT_FOUND.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-DESIGN-01-A01

**Core:** Implement Inventory reserve/release on initial A5. Invalid qty/unknown SKU returns false; release cannot exceed reservations. Preserve available+reserved.

**Acceptance example / fixture:** reserveA3 true,releaseA4 false -> available2,reserved3.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A02

**Core:** Implement BankAccount deposit/withdraw in integer cents. Positive amounts only; no overdraft; failed withdrawal leaves balance unchanged.

**Acceptance example / fixture:** initial10,withdraw11 ->false,balance10.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A03

**Core:** Implement immutable Money(currency,cents),three uppercase currency letters; add only identical currency,with explicit overflow policy.

**Acceptance example / fixture:** USD100+USD-20 ->USD80; USD+EUR ->INVALID.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A04

**Core:** Implement bounded FIFO Queue(capacity) with put/get,return FULL/EMPTY without mutation on rejection. Capacity positive.

**Acceptance example / fixture:** cap2,put a,b,c ->thirdFULL;get ->a.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A05

**Core:** Implement Stack with push,pop,peek and snapshot independent of future mutation. Empty pop/peek ->EMPTY.

**Acceptance example / fixture:** push a,b;pop ->b;snapshot[a].

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A06

**Core:** Implement Reservation state Open->Confirmed->Completed or Open->Cancelled. Rejected transitions preserve state and version.

**Acceptance example / fixture:** Confirmed->Cancelled ->INVALID,stillConfirmed.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A07

**Core:** Implement immutable DateRange(start,end) using integer half-open bounds,start<=end. intersect returns overlap or an empty range at max(start).

**Acceptance example / fixture:** [1,5) intersect[3,7) ->[3,5).

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A08

**Core:** Implement ShoppingCart keyed SKU with positive integer quantities and exact cents. Set quantity0 removes; invalid update changes nothing.

**Acceptance example / fixture:** Aprice2,qty3 ->total6;setA0 ->empty.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A09

**Core:** Implement Counter instances with atomic-by-contract add and snapshot but no shared state between instances. Detect declared integer overflow.

**Acceptance example / fixture:** instances1,1;first.add2 ->3,second1.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A10

**Core:** Implement Task with pending,running,succeeded,failed. Only pending->running and running->terminal allowed; result only for succeeded,error only for failed.

**Acceptance example / fixture:** pending->succeeded ->INVALID.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A11

**Core:** Implement RateLimiter capacity2,refill1 per integer second using injected monotonic clock. Accepted acquire consumes1; invalid backward clock ->INVALID.

**Acceptance example / fixture:** t0 two accepted,thirdrejected;t1 one accepted.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A12

**Core:** Implement versioned Document.update(expected_version,text). Initial version1; success increments; stale expected rejects without changing text.

**Acceptance example / fixture:** update1,x ->v2;update1,y ->CONFLICT.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A13

**Core:** Implement SeatMap reserve(seat,owner),release(seat,owner). Only owner may release; reserving same seat/owner again is idempotent; other owner conflicts.

**Acceptance example / fixture:** A byu thenA byv ->CONFLICT;releaseA byv denied.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A14

**Core:** Implement a dependency-injected Checkout using SKU price lookup and payment gateway. Validate every quantity/SKU before charging exactly once.

**Acceptance example / fixture:** A200,qty2 ->charge400;unknownSKU ->zerocharges.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-01-A15

**Core:** Implement ExpiringValue with injected clock,put(value,ttl),get(). ttl positive; value expires when now>=inserted+ttl. Do not reset expiry on read.

**Acceptance example / fixture:** putx at0,ttl5;get4 ->x;get5 ->NOT_FOUND.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Iterators and generators

### Beginner

#### PY-DESIGN-02-B01

**Core:** Implement lazy batches(iterator,size),yielding at most size items; size positive. Emit no empty final batch and do not preconsume the next batch.

**Acceptance example / fixture:** [1,2,3],2 -> [1,2],[3].

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B02

**Core:** Implement lazy take(iterator,n),consuming at most n items,n>=0. n0 must not request even one source item.

**Acceptance example / fixture:** source1,2,3;n2 ->1,2.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B03

**Core:** Implement lazy drop_while(iterator,predicate). Stop invoking predicate after first false and yield that item plus all remaining.

**Acceptance example / fixture:** [1,2,0,3],positive ->0,3.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B04

**Core:** Implement lazy pairwise(iterator),yielding consecutive overlapping pairs with constant retained state.

**Acceptance example / fixture:** [1,2,3] ->(1,2),(2,3).

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B05

**Core:** Implement lazy running_sum(iterator) for signed integers,emitting each prefix sum.

**Acceptance example / fixture:** [2,-1,4] ->2,1,5.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B06

**Core:** Implement lazy unique_first(iterator) retaining seen immutable keys and yielding first occurrence in input order.

**Acceptance example / fixture:** a,b,a,c ->a,b,c.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B07

**Core:** Implement lazy merge_sorted(a,b),retaining duplicates and at most one lookahead per input.

**Acceptance example / fixture:** [1,3],[1,2] ->1,1,2,3.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B08

**Core:** Implement lazy interleave(iterators) round-robin,skipping exhausted sources,without buffering full sources.

**Acceptance example / fixture:** [1,2],[a],[x,y] ->1,a,x,2,y.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B09

**Core:** Implement lazy flatten(iterables),exhausting one child at a time and closing an opened child on cancellation where its interface supports close.

**Acceptance example / fixture:** [[],[1,2],[3]] ->1,2,3.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B10

**Core:** Implement lazy sliding_windows(iterator,k),yielding independent lists of exactly k items; k positive.

**Acceptance example / fixture:** [1,2,3,4],3 ->[1,2,3],[2,3,4].

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B11

**Core:** Implement lazy enumerate_from(iterator,start),yielding exact integer index/item pairs without reading ahead.

**Acceptance example / fixture:** [a,b],start5 ->(5,a),(6,b).

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B12

**Core:** Implement lazy chunks_by_key(iterator,key_fn) for adjacent equal keys. One lookahead allowed; return key/group pairs preserving order.

**Acceptance example / fixture:** a1,a2,b1,a3 keyed firstletter ->a:[a1,a2],b:[b1],a:[a3].

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B13

**Core:** Implement lazy limit_until(iterator,predicate),yielding items strictly before first matching sentinel and consuming that sentinel only once.

**Acceptance example / fixture:** [1,2,0,9],iszero ->1,2;9 remains unread.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B14

**Core:** Implement two-consumer tee with an explicit max_lag bound. If one advances too far,return LAG_LIMIT rather than buffering unbounded input.

**Acceptance example / fixture:** maxlag1;consumerA reads2 items beforeB -> second read LAG_LIMIT.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-02-B15

**Core:** Implement lazy map_errors(iterator,fn),yielding per-item ok/error and continuing after declared application errors. Cancellation must propagate.

**Acceptance example / fixture:** [1,0,2],integer reciprocal validation ->ok,error,ok.

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-DESIGN-02-I01

**Core:** Implement lazy batches(iterator,size),yielding at most size items; size positive. Emit no empty final batch and do not preconsume the next batch.

**Acceptance example / fixture:** [1,2,3],2 -> [1,2],[3].

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I02

**Core:** Implement lazy take(iterator,n),consuming at most n items,n>=0. n0 must not request even one source item.

**Acceptance example / fixture:** source1,2,3;n2 ->1,2.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I03

**Core:** Implement lazy drop_while(iterator,predicate). Stop invoking predicate after first false and yield that item plus all remaining.

**Acceptance example / fixture:** [1,2,0,3],positive ->0,3.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I04

**Core:** Implement lazy pairwise(iterator),yielding consecutive overlapping pairs with constant retained state.

**Acceptance example / fixture:** [1,2,3] ->(1,2),(2,3).

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I05

**Core:** Implement lazy running_sum(iterator) for signed integers,emitting each prefix sum.

**Acceptance example / fixture:** [2,-1,4] ->2,1,5.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I06

**Core:** Implement lazy unique_first(iterator) retaining seen immutable keys and yielding first occurrence in input order.

**Acceptance example / fixture:** a,b,a,c ->a,b,c.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I07

**Core:** Implement lazy merge_sorted(a,b),retaining duplicates and at most one lookahead per input.

**Acceptance example / fixture:** [1,3],[1,2] ->1,1,2,3.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I08

**Core:** Implement lazy interleave(iterators) round-robin,skipping exhausted sources,without buffering full sources.

**Acceptance example / fixture:** [1,2],[a],[x,y] ->1,a,x,2,y.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I09

**Core:** Implement lazy flatten(iterables),exhausting one child at a time and closing an opened child on cancellation where its interface supports close.

**Acceptance example / fixture:** [[],[1,2],[3]] ->1,2,3.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I10

**Core:** Implement lazy sliding_windows(iterator,k),yielding independent lists of exactly k items; k positive.

**Acceptance example / fixture:** [1,2,3,4],3 ->[1,2,3],[2,3,4].

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I11

**Core:** Implement lazy enumerate_from(iterator,start),yielding exact integer index/item pairs without reading ahead.

**Acceptance example / fixture:** [a,b],start5 ->(5,a),(6,b).

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I12

**Core:** Implement lazy chunks_by_key(iterator,key_fn) for adjacent equal keys. One lookahead allowed; return key/group pairs preserving order.

**Acceptance example / fixture:** a1,a2,b1,a3 keyed firstletter ->a:[a1,a2],b:[b1],a:[a3].

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I13

**Core:** Implement lazy limit_until(iterator,predicate),yielding items strictly before first matching sentinel and consuming that sentinel only once.

**Acceptance example / fixture:** [1,2,0,9],iszero ->1,2;9 remains unread.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I14

**Core:** Implement two-consumer tee with an explicit max_lag bound. If one advances too far,return LAG_LIMIT rather than buffering unbounded input.

**Acceptance example / fixture:** maxlag1;consumerA reads2 items beforeB -> second read LAG_LIMIT.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-02-I15

**Core:** Implement lazy map_errors(iterator,fn),yielding per-item ok/error and continuing after declared application errors. Cancellation must propagate.

**Acceptance example / fixture:** [1,0,2],integer reciprocal validation ->ok,error,ok.

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-DESIGN-02-A01

**Core:** Implement lazy batches(iterator,size),yielding at most size items; size positive. Emit no empty final batch and do not preconsume the next batch.

**Acceptance example / fixture:** [1,2,3],2 -> [1,2],[3].

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A02

**Core:** Implement lazy take(iterator,n),consuming at most n items,n>=0. n0 must not request even one source item.

**Acceptance example / fixture:** source1,2,3;n2 ->1,2.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A03

**Core:** Implement lazy drop_while(iterator,predicate). Stop invoking predicate after first false and yield that item plus all remaining.

**Acceptance example / fixture:** [1,2,0,3],positive ->0,3.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A04

**Core:** Implement lazy pairwise(iterator),yielding consecutive overlapping pairs with constant retained state.

**Acceptance example / fixture:** [1,2,3] ->(1,2),(2,3).

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A05

**Core:** Implement lazy running_sum(iterator) for signed integers,emitting each prefix sum.

**Acceptance example / fixture:** [2,-1,4] ->2,1,5.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A06

**Core:** Implement lazy unique_first(iterator) retaining seen immutable keys and yielding first occurrence in input order.

**Acceptance example / fixture:** a,b,a,c ->a,b,c.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A07

**Core:** Implement lazy merge_sorted(a,b),retaining duplicates and at most one lookahead per input.

**Acceptance example / fixture:** [1,3],[1,2] ->1,1,2,3.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A08

**Core:** Implement lazy interleave(iterators) round-robin,skipping exhausted sources,without buffering full sources.

**Acceptance example / fixture:** [1,2],[a],[x,y] ->1,a,x,2,y.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A09

**Core:** Implement lazy flatten(iterables),exhausting one child at a time and closing an opened child on cancellation where its interface supports close.

**Acceptance example / fixture:** [[],[1,2],[3]] ->1,2,3.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A10

**Core:** Implement lazy sliding_windows(iterator,k),yielding independent lists of exactly k items; k positive.

**Acceptance example / fixture:** [1,2,3,4],3 ->[1,2,3],[2,3,4].

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A11

**Core:** Implement lazy enumerate_from(iterator,start),yielding exact integer index/item pairs without reading ahead.

**Acceptance example / fixture:** [a,b],start5 ->(5,a),(6,b).

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A12

**Core:** Implement lazy chunks_by_key(iterator,key_fn) for adjacent equal keys. One lookahead allowed; return key/group pairs preserving order.

**Acceptance example / fixture:** a1,a2,b1,a3 keyed firstletter ->a:[a1,a2],b:[b1],a:[a3].

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A13

**Core:** Implement lazy limit_until(iterator,predicate),yielding items strictly before first matching sentinel and consuming that sentinel only once.

**Acceptance example / fixture:** [1,2,0,9],iszero ->1,2;9 remains unread.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A14

**Core:** Implement two-consumer tee with an explicit max_lag bound. If one advances too far,return LAG_LIMIT rather than buffering unbounded input.

**Acceptance example / fixture:** maxlag1;consumerA reads2 items beforeB -> second read LAG_LIMIT.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-02-A15

**Core:** Implement lazy map_errors(iterator,fn),yielding per-item ok/error and continuing after declared application errors. Cancellation must propagate.

**Acceptance example / fixture:** [1,0,2],integer reciprocal validation ->ok,error,ok.

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Decorators and caching

### Beginner

#### PY-DESIGN-03-B01

**Core:** Implement bounded LRU memoizer for pure string-key function. Hits update recency; exceptions not cached; expose hit/miss counts.

**Acceptance example / fixture:** cap2,calls a,b,a,c,b ->hits1,misses4.

**Question:** Implement the core and demonstrate the supplied acceptance example. Return exactly the specified result shape; do not print a prose answer instead of a result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B02

**Core:** Implement FIFO cache where hits do not affect eviction order. Return evicted key on insertion past capacity.

**Acceptance example / fixture:** cap2,put a,b,geta,putc ->evicta.

**Question:** Add an input-validation boundary that distinguishes malformed input from a valid empty result. Demonstrate one example of each under the core's rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B03

**Core:** Implement TTL cache using injected clock; expire exactly at now>=created+ttl,reads do not renew expiry.

**Acceptance example / fixture:** putaat0,ttl5;get5 ->MISS.

**Question:** Write a trace version of the core that returns the decisions/intermediate state needed to explain the acceptance example. Keep the ordinary return contract unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B04

**Core:** Implement single-last-result memoizer. Only immediately repeated equal immutable argument is a hit; exceptions never cached.

**Acceptance example / fixture:** a,a,b,a ->onehit.

**Question:** Implement a batch entry point receiving a list of independent core requests. Return one result per request in original order; a rejected request must not erase successful results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B05

**Core:** Implement per-tenant cache keys so identical resource IDs in different tenants remain independent.

**Acceptance example / fixture:** t1/a:x,t2/a:y ->two distinct values.

**Question:** Wrap the core in a newline-delimited JSON interface. Emit exactly one structured result or error per input line,including the one-based line number on errors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B06

**Core:** Implement version-aware cache lookup requiring exact resource and requested revision; stale entry must be a miss.

**Acceptance example / fixture:** stored a:v2;requesta:v3 ->MISS.

**Question:** Demonstrate all explicitly specified equality/threshold boundaries of the core with executable cases. Return the case inputs and actual results,not just a test checklist.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B07

**Core:** Implement cache-aside lookup with injected repository; cache only nonnull successes. Failure and not-found are not cached.

**Acceptance example / fixture:** missing key requested twice ->two repo calls.

**Question:** Implement a side-effect-free variant: caller-owned inputs must compare deeply equal before and after every success or rejection. Return independent mutable outputs where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B08

**Core:** Implement explicit negative caching with distinct NOT_FOUND marker and shorter ttl2 versus positive ttl10. Never confuse null payload with absence.

**Acceptance example / fixture:** notfoundat0 read1 ->negativehit,read2 ->miss.

**Question:** Add a result formatter that produces deterministic JSON with sorted object keys and preserves array order,nulls and exact integers. Follow the core's documented representation for integers beyond the host JSON numeric range.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B09

**Core:** Implement batch cache lookup preserving input order/repeats and fetching each unique missing key once.

**Acceptance example / fixture:** keys[a,b,a],cacheb ->fetchaonce,threeoutputs.

**Question:** Make two independent instances/calls using different inputs and show that no result leaks into the other. Demonstrate with executable interleaved calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B10

**Core:** Implement invalidate_prefix over exact case-sensitive key strings with no path normalization. Return removed keys sorted.

**Acceptance example / fixture:** raw/a,raw2/a;prefixraw/ ->remove raw/a only.

**Question:** Build a command dispatcher accepting {operation:"solve",input:...}. Reject unknown operations with UNKNOWN_OPERATION before invoking the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B11

**Core:** Implement write-through cache: persist before updating cache; repository failure leaves prior cache value/revision intact.

**Acceptance example / fixture:** cachedx,persisty fails ->stillx.

**Question:** Return a structured validation error with path and reason for the first invalid field,using input-field order. Keep the core's valid outputs unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B12

**Core:** Implement cached pure result cloning so a caller cannot mutate a cached collection through a returned reference.

**Acceptance example / fixture:** get list,append ->laterget unaffected.

**Question:** Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B13

**Core:** Implement capacity-by-weight LRU with positive integer entry weights. Oversized entry rejected before evicting any valid entry.

**Acceptance example / fixture:** budget3,existinga weight2,newb weight4 ->reject,keepa.

**Question:** Implement an adapter from JSON-compatible objects to the core's native types. Reject missing required fields and report extra fields without silently changing their meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B14

**Core:** Implement a cache statistics snapshot with hits,misses,evictions,expired removals. Snapshot must not reset counters or expose mutable internals.

**Acceptance example / fixture:** onehit,twomisses ->exact counters preserved after read.

**Question:** Implement a result-contract checker. Give it one valid result and one deliberately wrong type/shape; it must distinguish them without rerunning the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PY-DESIGN-03-B15

**Core:** Implement canonical typed keys distinguishing integer1,string"1",booleantrue and null. Structured input objects ignore field order but retain array order.

**Acceptance example / fixture:** {a:1,b:2} equals reordered object key;[1,2] differs[2,1].

**Question:** Provide a minimal independent reference implementation for small inputs. Compare it to the main implementation on the supplied example and a different valid input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PY-DESIGN-03-I01

**Core:** Implement bounded LRU memoizer for pure string-key function. Hits update recency; exceptions not cached; expose hit/miss counts.

**Acceptance example / fixture:** cap2,calls a,b,a,c,b ->hits1,misses4.

**Question:** Extend the batch entry point with fail-fast=false collecting per-item errors,and fail-fast=true stopping at the first error. Return how many requests were actually executed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I02

**Core:** Implement FIFO cache where hits do not affect eviction order. Return evicted key on insertion past capacity.

**Acceptance example / fixture:** cap2,put a,b,geta,putc ->evicta.

**Question:** Add bounded LRU caching for pure requests keyed by canonical input; include exact numeric types in the key. Stateful cores must instead cache only a read-only snapshot and invalidate on mutation. Demonstrate eviction and no stale result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I03

**Core:** Implement TTL cache using injected clock; expire exactly at now>=created+ttl,reads do not renew expiry.

**Acceptance example / fixture:** putaat0,ttl5;get5 ->MISS.

**Question:** Implement a streaming batch adapter that consumes a request iterator and yields one result at a time. It must not materialize all requests or read more than one request ahead.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I04

**Core:** Implement single-last-result memoizer. Only immediately repeated equal immutable argument is a hit; exceptions never cached.

**Acceptance example / fixture:** a,a,b,a ->onehit.

**Question:** Add a stable request_id to every batch request. Identical repeated request IDs with equal inputs return the recorded result; different inputs under the same ID produce CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I05

**Core:** Implement per-tenant cache keys so identical resource IDs in different tenants remain independent.

**Acceptance example / fixture:** t1/a:x,t2/a:y ->two distinct values.

**Question:** Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I06

**Core:** Implement version-aware cache lookup requiring exact resource and requested revision; stale entry must be a miss.

**Acceptance example / fixture:** stored a:v2;requesta:v3 ->MISS.

**Question:** Implement two distinct algorithms for the core and compare full results over exhaustive small inputs. Show one case where comparing only result lengths would miss a defect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I07

**Core:** Implement cache-aside lookup with injected repository; cache only nonnull successes. Failure and not-found are not cached.

**Acceptance example / fixture:** missing key requested twice ->two repo calls.

**Question:** Add an optional maximum input-size limit enforced before expensive processing. Return TOO_LARGE without partial output; demonstrate the exact accepted/rejected boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I08

**Core:** Implement explicit negative caching with distinct NOT_FOUND marker and shorter ttl2 versus positive ttl10. Never confuse null payload with absence.

**Acceptance example / fixture:** notfoundat0 read1 ->negativehit,read2 ->miss.

**Question:** Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I09

**Core:** Implement batch cache lookup preserving input order/repeats and fetching each unique missing key once.

**Acceptance example / fixture:** keys[a,b,a],cacheb ->fetchaonce,threeoutputs.

**Question:** Add an operation-count instrument for the algorithm's dominant work. Demonstrate counts over increasing input sizes and justify the complexity using those observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I10

**Core:** Implement invalidate_prefix over exact case-sensitive key strings with no path normalization. Return removed keys sorted.

**Acceptance example / fixture:** raw/a,raw2/a;prefixraw/ ->remove raw/a only.

**Question:** Implement batch deduplication that executes identical pure requests once while retaining every original output position. For a stateful core,deduplicate only requests sharing an explicit idempotency ID.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I11

**Core:** Implement write-through cache: persist before updating cache; repository failure leaves prior cache value/revision intact.

**Acceptance example / fixture:** cachedx,persisty fails ->stillx.

**Question:** Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I12

**Core:** Implement cached pure result cloning so a caller cannot mutate a cached collection through a returned reference.

**Acceptance example / fixture:** get list,append ->laterget unaffected.

**Question:** Inject an optional diagnostic logger. It must receive bounded structured events without exposing caller input secrets or changing returned values. Show behavior with a logger that throws.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I13

**Core:** Implement capacity-by-weight LRU with positive integer entry weights. Oversized entry rejected before evicting any valid entry.

**Acceptance example / fixture:** budget3,existinga weight2,newb weight4 ->reject,keepa.

**Question:** Implement replay from a recorded input/result transcript and detect the first inconsistent output with its request index. Do not assume equal grand totals imply equal results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I14

**Core:** Implement a cache statistics snapshot with hits,misses,evictions,expired removals. Snapshot must not reset counters or expose mutable internals.

**Acceptance example / fixture:** onehit,twomisses ->exact counters preserved after read.

**Question:** Accept a deterministic clock/random source wherever an extension needs time or generated IDs. Prove the same injected sequence produces byte-identical output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PY-DESIGN-03-I15

**Core:** Implement canonical typed keys distinguishing integer1,string"1",booleantrue and null. Structured input objects ignore field order but retain array order.

**Acceptance example / fixture:** {a:1,b:2} equals reordered object key;[1,2] differs[2,1].

**Question:** Build a test mutation that changes one meaningful core comparison or state transition. Demonstrate an independently derived acceptance test that fails against that mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PY-DESIGN-03-A01

**Core:** Implement bounded LRU memoizer for pure string-key function. Hits update recency; exceptions not cached; expose hit/miss counts.

**Acceptance example / fixture:** cap2,calls a,b,a,c,b ->hits1,misses4.

**Question:** Analyze the core's input-reading lower bound and optimize a demonstrably inefficient operation if one exists. If the implementation already meets the lower bound,justify that instead of inventing a speedup. Compare complete results with a simple reference and measure actual operation counts over scaled inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A02

**Core:** Implement FIFO cache where hits do not affect eviction order. Return evicted key on insertion past capacity.

**Acceptance example / fixture:** cap2,put a,b,geta,putc ->evicta.

**Question:** Run bounded concurrent requests against the implementation. Pure calls must remain isolated; stateful calls need an explicit linearizable ordering. Produce a deterministic race test,not a sleep-based demonstration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A03

**Core:** Implement TTL cache using injected clock; expire exactly at now>=created+ttl,reads do not renew expiry.

**Acceptance example / fixture:** putaat0,ttl5;get5 ->MISS.

**Question:** Process a batch of one million logical requests under a bounded-memory contract. Stream inputs and outputs,measure retained state and specify how errors are emitted without losing ordering.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A04

**Core:** Implement single-last-result memoizer. Only immediately repeated equal immutable argument is a hit; exceptions never cached.

**Acceptance example / fixture:** a,a,b,a ->onehit.

**Question:** Implement durable checkpoint/restart for a long batch. A crash after producing a result but before advancing a cursor must not duplicate a committed output on restart.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A05

**Core:** Implement per-tenant cache keys so identical resource IDs in different tenants remain independent.

**Acceptance example / fixture:** t1/a:x,t2/a:y ->two distinct values.

**Question:** Version and migrate durable state used by the core or its adapter. Support reading v1 during migration,write v2 only after validation and demonstrate recovery from an interrupted migration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A06

**Core:** Implement version-aware cache lookup requiring exact resource and requested revision; stale entry must be a miss.

**Acceptance example / fixture:** stored a:v2;requesta:v3 ->MISS.

**Question:** Build a differential fuzzer against the independent reference with boundary values,nulls and repeated keys where permitted. Persist a minimal failing input and replay it deterministically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A07

**Core:** Implement cache-aside lookup with injected repository; cache only nonnull successes. Failure and not-found are not cached.

**Acceptance example / fixture:** missing key requested twice ->two repo calls.

**Question:** Implement cancelable batched execution. After cancellation,stop starting work; return explicit completed/cancelled positions and leave stateful invariants intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A08

**Core:** Implement explicit negative caching with distinct NOT_FOUND marker and shorter ttl2 versus positive ttl10. Never confuse null payload with absence.

**Acceptance example / fixture:** notfoundat0 read1 ->negativehit,read2 ->miss.

**Question:** Handle a downstream output-sink failure after computation. Record which results are durably committed and resume without recomputing stateful side effects or silently dropping a request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A09

**Core:** Implement batch cache lookup preserving input order/repeats and fetching each unique missing key once.

**Acceptance example / fixture:** keys[a,b,a],cacheb ->fetchaonce,threeoutputs.

**Question:** Design a security boundary for untrusted JSON requests with bounded depth,size and work. Demonstrate rejected adversarial input and an ordinary valid request with unchanged semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A10

**Core:** Implement invalidate_prefix over exact case-sensitive key strings with no path normalization. Return removed keys sorted.

**Acceptance example / fixture:** raw/a,raw2/a;prefixraw/ ->remove raw/a only.

**Question:** Implement cross-language parity: provide a second-language version or a precise interchange test suite. Detect integer,Unicode,null and ordering differences applicable to this core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A11

**Core:** Implement write-through cache: persist before updating cache; repository failure leaves prior cache value/revision intact.

**Acceptance example / fixture:** cachedx,persisty fails ->stillx.

**Question:** Prove a selected optimization preserves the core's semantics by writing a counterexample to a tempting incorrect shortcut and regression tests for the corrected approach.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A12

**Core:** Implement cached pure result cloning so a caller cannot mutate a cached collection through a returned reference.

**Acceptance example / fixture:** get list,append ->laterget unaffected.

**Question:** Add an audit trail for stateful operations or a reproducibility manifest for pure operations. Demonstrate that a result can be traced to its exact input,algorithm version and deterministic dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A13

**Core:** Implement capacity-by-weight LRU with positive integer entry weights. Oversized entry rejected before evicting any valid entry.

**Acceptance example / fixture:** budget3,existinga weight2,newb weight4 ->reject,keepa.

**Question:** Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A14

**Core:** Implement a cache statistics snapshot with hits,misses,evictions,expired removals. Snapshot must not reset counters or expose mutable internals.

**Acceptance example / fixture:** onehit,twomisses ->exact counters preserved after read.

**Question:** Publish the implementation behind a compatibility adapter. Show that clients using v1 still receive the original result/error contract while v2 clients can request new metadata.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PY-DESIGN-03-A15

**Core:** Implement canonical typed keys distinguishing integer1,string"1",booleantrue and null. Structured input objects ignore field order but retain array order.

**Acceptance example / fixture:** {a:1,b:2} equals reordered object key;[1,2] differs[2,1].

**Question:** Deliver the core with independent correctness checks,complexity evidence,adversarial cases and one injected failure. Demonstrate which observable test would reject an incorrect interview solution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
