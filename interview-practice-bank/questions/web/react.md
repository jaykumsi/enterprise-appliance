# Shared Web and Frontend: React

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## State updates and reducers

### Beginner

#### WEB-REACT-01-B01

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B02

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B03

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B04

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B05

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B06

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B07

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B08

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B09

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B10

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B11

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B12

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B13

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B14

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-01-B15

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-REACT-01-I01

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I02

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I03

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I04

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I05

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I06

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I07

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I08

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I09

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I10

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I11

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I12

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I13

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I14

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-01-I15

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-REACT-01-A01

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A02

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A03

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A04

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A05

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A06

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A07

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A08

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A09

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A10

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A11

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A12

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A13

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A14

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-01-A15

**Core:** Implement a cart reducer with Add,SetQuantity,Remove. Quantities are positive integers; repeated Add sums quantities, invalid input returns a structured error without mutation. Store entries by SKU and render in SKU order.

**Acceptance example / fixture:** Add A:2 then A:3 -> A:5; SetQuantity A:0 -> error.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Effects cleanup and dependencies

### Beginner

#### WEB-REACT-02-B01

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B02

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B03

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B04

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B05

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B06

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B07

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B08

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B09

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B10

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B11

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B12

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B13

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B14

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-02-B15

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-REACT-02-I01

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I02

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I03

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I04

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I05

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I06

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I07

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I08

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I09

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I10

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I11

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I12

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I13

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I14

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-02-I15

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-REACT-02-A01

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A02

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A03

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A04

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A05

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A06

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A07

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A08

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A09

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A10

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A11

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A12

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A13

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A14

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-02-A15

**Core:** Implement a component subscribing to an injected event source for orderId. On ID change unsubscribe old source before subscribing new; on unmount clean up. Old-source events must not change the new order view.

**Acceptance example / fixture:** Switch A->B then late A event -> B view unchanged.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Forms and asynchronous validation

### Beginner

#### WEB-REACT-03-B01

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B02

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B03

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B04

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B05

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B06

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B07

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B08

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B09

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B10

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B11

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B12

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B13

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B14

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-03-B15

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-REACT-03-I01

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I02

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I03

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I04

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I05

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I06

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I07

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I08

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I09

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I10

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I11

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I12

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I13

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I14

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-03-I15

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-REACT-03-A01

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A02

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A03

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A04

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A05

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A06

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A07

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A08

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A09

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A10

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A11

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A12

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A13

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A14

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-03-A15

**Core:** Build username validation: local pattern [a-z][a-z0-9]{2,19}, then injected availability check. Pending or unavailable names cannot submit; late responses cannot validate a changed name.

**Acceptance example / fixture:** abc available response arriving after value becomes abcd cannot enable submit for abcd.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Routing and protected views

### Beginner

#### WEB-REACT-04-B01

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B02

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B03

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B04

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B05

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B06

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B07

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B08

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B09

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B10

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B11

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B12

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B13

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B14

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-REACT-04-B15

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-REACT-04-I01

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I02

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I03

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I04

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I05

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I06

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I07

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I08

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I09

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I10

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I11

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I12

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I13

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I14

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-REACT-04-I15

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-REACT-04-A01

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A02

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A03

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A04

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A05

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A06

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A07

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A08

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A09

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A10

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A11

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A12

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A13

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A14

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-REACT-04-A15

**Core:** Implement a route decision function for /orders/:id. Unauthenticated -> login redirect with safe relative return path; authenticated nonowner -> forbidden; owner or authenticated admin -> order view. Do not expose order data before authorization.

**Acceptance example / fixture:** External return URL -> replaced by /; customer a opening b order -> forbidden.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
