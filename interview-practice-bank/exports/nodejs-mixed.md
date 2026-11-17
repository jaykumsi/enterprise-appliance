# Full Stack Developer - NodeJs mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## NODE-JAVASCRIPT-05-B12 — TypeScript discriminated unions

Full Stack Developer - NodeJs / JavaScript / Beginner

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients. Suggested time: 15 minutes.

**Core problem**

Implement reduceOrder(state,event) with typed events Pay,Ship,Cancel. Open may Pay or Cancel; Paid may Ship; all other transitions return {error:INVALID_TRANSITION} without mutation. Make event handling exhaustive at compile time.

**Acceptance example / baseline**

Open+Pay -> Paid; Shipped+Pay -> error.

**Interview requirement**

Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## NODE-BACKEND-01-I05 — HTTP routing and validation

Full Stack Developer - NodeJs / Backend / Intermediate

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients. Suggested time: 30 minutes.

**Core problem**

Implement POST /reservations with {sku,quantity}. Reject invalid JSON or blank SKU/nonpositive integer quantity with 400. Return 201 on reservation and 409 on insufficient stock. Inject inventory; never decrement on invalid input.

**Acceptance example / baseline**

quantity 0 -> 400; A available 1 requested 2 -> 409.

**Interview requirement**

Add pagination to any list result using a stable unique key. For a singleton core,provide a separate batch read adapter preserving request order and per-item outcomes.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## NODE-JAVASCRIPT-01-A13 — Types and exact numeric boundaries

Full Stack Developer - NodeJs / JavaScript / Advanced

Runtime: JavaScript/TypeScript on Node.js; inject databases and HTTP clients. Suggested time: 45 minutes.

**Core problem**

Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / baseline**

([2,3,-1],-4,4) -> 1.

**Interview requirement**

Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
