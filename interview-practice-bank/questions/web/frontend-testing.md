# Shared Web and Frontend: Frontend Testing

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Browser/React for UI tasks; a code-only pad can assess the state model but cannot verify rendering/accessibility.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Component and interaction tests

### Beginner

#### WEB-FRONTEND-TESTING-01-B01

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B02

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B03

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B04

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B05

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B06

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B07

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B08

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B09

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B10

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B11

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B12

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B13

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B14

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-01-B15

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-FRONTEND-TESTING-01-I01

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I02

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I03

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I04

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I05

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I06

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I07

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I08

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I09

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I10

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I11

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I12

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I13

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I14

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-01-I15

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-FRONTEND-TESTING-01-A01

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A02

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A03

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A04

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A05

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A06

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A07

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A08

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A09

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A10

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A11

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A12

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A13

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A14

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-01-A15

**Core:** Build an order list with loading,error,empty,success states and retry. Inject the data client. A retry must trigger one fresh request and discard stale results. Supply interaction tests using accessible roles.

**Acceptance example / fixture:** First request fails, retry succeeds with [] -> empty state, no stale error.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Performance and large lists

### Beginner

#### WEB-FRONTEND-TESTING-02-B01

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement the core UI/decision behavior and demonstrate its acceptance example with a reproducible interaction sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B02

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Demonstrate keyboard-only completion of the core's main interaction. Return focus order and visible state changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B03

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Render initial,valid and invalid/empty states applicable to the core. Each must have unambiguous visible text or accessible state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B04

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement input validation so a rejected interaction performs no API/business mutation. Demonstrate with an injected spy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B05

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add semantic labels and an accessible name for every interactive control. Show how a test selects them by role/name rather than CSS position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B06

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Demonstrate the core with two distinct records/instances and prove interacting with one cannot change the other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B07

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Return a pure state-transition function underlying the UI and show a table of input events and resulting state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B08

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Preserve the core's source data without mutation; demonstrate input equality after rendering and interaction.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B09

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Handle a missing optional display value without displaying undefined/null as accidental user text. Use an explicit placeholder and retain the actual data meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B10

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement a deterministic empty state with no phantom selectable/submittable record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B11

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add a safe output boundary that renders user strings as text,not executable markup. Demonstrate with synthetic HTML-like content.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B12

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Create a minimal interaction test for the baseline showing expected and actual rendered state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B13

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Demonstrate the smallest valid/invalid numeric or text boundary in the core. If no input boundary exists,use the first/last visible list item.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B14

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Show the UI at narrow and wide viewports and demonstrate that the main interaction remains reachable without accidental horizontal overflow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### WEB-FRONTEND-TESTING-02-B15

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement a reset/new-instance action restoring initial state and focus without leaking state from the previous record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### WEB-FRONTEND-TESTING-02-I01

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Handle a pending asynchronous action and disable only interactions that would violate the core's state contract. Duplicate activation cannot issue duplicate business requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I02

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Inject a failed request,show an accessible error and support retry without retaining a stale success state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I03

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Handle two asynchronous results arriving out of order. Only the latest relevant request may change the current view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I04

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add cleanup on unmount or route/record change. Late callbacks from the old view must not update the new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I05

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Preserve per-record state by stable ID when rows reorder. Demonstrate why array index keys would attach state to the wrong row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I06

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add a client/server validation adapter that maps field errors by name and preserves user input on rejection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I07

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement a state-machine/reducer version and compare interactions with a simple reference model on a scripted event sequence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I08

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add a debounced asynchronous interaction with an injected clock; schedule only after300ms inactivity and test the exact boundary without real sleeps.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I09

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Handle stale data with an explicit refresh/version rule. A response for an earlier record version must not overwrite a newer accepted edit.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I10

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Build tests for success,error,empty,pending and retry states using accessible queries and controlled promises.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I11

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Support a deterministic URL/query representation of nonsecret view state. Reject invalid URL values and restore defaults visibly.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I12

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement an optimistic update with a saved prior state and request identity. A failure restores only that request's state,not a later successful action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I13

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add a bounded rendered-item window for a large list; retain selection by stable ID even when an item is not mounted.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I14

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Demonstrate focus restoration after a dialog/error/retry interaction and announce asynchronous results through an appropriate status region.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### WEB-FRONTEND-TESTING-02-I15

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Construct an adversarial interaction sequence exposing a stale closure,missing cleanup,mutation or event-target bug applicable to the core; demonstrate the corrected view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### WEB-FRONTEND-TESTING-02-A01

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement a full client/server race simulation with delayed requests,conflicting versions and retries. Preserve user intent and expose unresolved conflicts instead of silently overwriting edits.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A02

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add durable draft restoration with versioned schema and explicit handling of incompatible drafts. Never restore another tenant/user's draft into the current session.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A03

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Demonstrate accessibility under error,pending,virtualized and reordered states. Supply automated interaction evidence and a manual keyboard/focus check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A04

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Bound memory and mounted UI state for100000 records while preserving selection and stable identity. Measure actual mounted node counts and retained per-record state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A05

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement cancellation races before submission,during request and after server commit. Do not label client cancellation proof that the server undid a committed action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A06

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Handle offline/reconnect using durable idempotency IDs for queued business actions. Reconcile accepted/unknown outcomes before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A07

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Migrate the component/public state contract while older callers remain compatible. Write regression tests for both versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A08

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Create model-based generated interaction tests against the pure state reference. Persist a minimal event sequence when rendered state diverges.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A09

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Protect tenant and route boundaries across browser-back navigation,cache hits and late responses. Demonstrate that old authorized data cannot reappear after identity change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A10

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement a safe partial-render/error boundary with retry. A rendering failure in one independent widget cannot corrupt another widget's valid state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A11

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Build an independent telemetry trace connecting user action,request ID,response version and rendered state without logging secret inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A12

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Show a measured rendering bottleneck and optimize it while preserving accessible output and all interaction tests. Do not infer speedup from code structure alone.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A13

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Implement server/client initial-state parity where applicable,or a deterministic pre-render snapshot check for a client-only task. Detect a deliberate initial-state mismatch.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A14

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Add a compatibility test across Unicode text,long IDs,zoomed narrow view and repeated rapid actions. Document actual observations and unresolved browser-specific checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### WEB-FRONTEND-TESTING-02-A15

**Core:** Build a selectable list of 100000 orders with windowed rendering, stable order IDs and persistent selection when rows leave the viewport. State the window contract: render at most visible rows plus ten overscan rows on each side.

**Acceptance example / fixture:** Select A,scroll away,return -> A selected; mounted row count bounded.

**Question:** Deliver the core with state model,accessibility evidence,race tests,cleanup,bounded rendering and one reproducible failure/recovery interaction trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
