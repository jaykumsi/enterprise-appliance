# Shared Web and Frontend: Browser

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Semantic HTML and accessibility

### Beginner

#### WEB-BROWSER-01-B01

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B02

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B03

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B04

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B05

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B06

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B07

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B08

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B09

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B10

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B11

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B12

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B13

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B14

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-01-B15

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-BROWSER-01-I01

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I02

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I03

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I04

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I05

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I06

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I07

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I08

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I09

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I10

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I11

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I12

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I13

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I14

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-01-I15

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-BROWSER-01-A01

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A02

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A03

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A04

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A05

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A06

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A07

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A08

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A09

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A10

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A11

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A12

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A13

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A14

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-01-A15

**Core:** Build a reservation form with labelled SKU and quantity controls, a submit button and a status region. Invalid input must identify the field in text, remain keyboard reachable and never rely only on color. Submit only nonblank SKU and positive integer quantity.

**Acceptance example / fixture:** Empty SKU on submit -> focusable SKU error and no API call.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## CSS layout and responsiveness

### Beginner

#### WEB-BROWSER-02-B01

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B02

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B03

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B04

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B05

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B06

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B07

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B08

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B09

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B10

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B11

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B12

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B13

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B14

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-02-B15

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-BROWSER-02-I01

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I02

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I03

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I04

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I05

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I06

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I07

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I08

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I09

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I10

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I11

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I12

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I13

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I14

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-02-I15

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-BROWSER-02-A01

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A02

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A03

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A04

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A05

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A06

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A07

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A08

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A09

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A10

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A11

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A12

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A13

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A14

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-02-A15

**Core:** Build an order-card layout that uses one column below 600 CSS px and three equal columns at or above 600 px, with 16px gaps. Long unbroken IDs must wrap without horizontal page overflow. Each card includes a labelled Select button; activating it marks only that card selected and announces its ID. Supply markup,CSS and viewport evidence.

**Acceptance example / fixture:** 599px -> one column; 600px -> three columns.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## DOM events and delegation

### Beginner

#### WEB-BROWSER-03-B01

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B02

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B03

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B04

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B05

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B06

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B07

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B08

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B09

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B10

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B11

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B12

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B13

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B14

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-03-B15

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-BROWSER-03-I01

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I02

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I03

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I04

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I05

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I06

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I07

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I08

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I09

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I10

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I11

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I12

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I13

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I14

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-03-I15

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-BROWSER-03-A01

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A02

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A03

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A04

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A05

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A06

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A07

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A08

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A09

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A10

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A11

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A12

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A13

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A14

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-03-A15

**Core:** Build a cart list with delegated remove buttons. Each click removes only its own SKU; clicking nested button text must still work. Handle newly appended rows without adding per-row handlers.

**Acceptance example / fixture:** Rows A,B; click span inside B remove -> A remains.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Fetch errors and cancellation

### Beginner

#### WEB-BROWSER-04-B01

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B02

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B03

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B04

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B05

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B06

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B07

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B08

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B09

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B10

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B11

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B12

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B13

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B14

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-BROWSER-04-B15

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-BROWSER-04-I01

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I02

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I03

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I04

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I05

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I06

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I07

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I08

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I09

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I10

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I11

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I12

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I13

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I14

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-BROWSER-04-I15

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-BROWSER-04-A01

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A02

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A03

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A04

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A05

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A06

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A07

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A08

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A09

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A10

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A11

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A12

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A13

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A14

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-BROWSER-04-A15

**Core:** Implement an order search box calling injected search(query,signal). Ignore responses from older queries, show pending/error/empty/results states, and cancel obsolete work. Trim only the outer ASCII spaces of the query.

**Acceptance example / fixture:** Query a then ab; a resolves last -> only ab results displayed.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
