# Shared Web and Frontend mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## WEB-BROWSER-03-B06 — DOM events and delegation

Shared Web and Frontend / Browser / Beginner

Runtime: Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility. Suggested time: 15 minutes.

**Core problem**

Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / baseline**

Rows A,B; click span inside B remove -> A remains.

**Interview requirement**

Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## WEB-REACT-02-I03 — Effects cleanup and dependencies

Shared Web and Frontend / React / Intermediate

Runtime: Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility. Suggested time: 30 minutes.

**Core problem**

Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / baseline**

Switch A->B then late A event -> B view unchanged.

**Interview requirement**

Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## WEB-BROWSER-01-A04 — Semantic HTML and accessibility

Shared Web and Frontend / Browser / Advanced

Runtime: Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility. Suggested time: 45 minutes.

**Core problem**

Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / baseline**

Empty SKU on submit -> focusable SKU error and no API call.

**Interview requirement**

Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
