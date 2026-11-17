# Snowflake: Recovery

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Time Travel and recovery planning

### Beginner

#### SNOW-RECOVERY-01-B01

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B02

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B03

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B04

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B05

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B06

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B07

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B08

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B09

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B10

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Return the core's dependency/resource graph and validate every referenced node exists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B11

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B12

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Produce a dry-run plan describing observable actions with no external mutation calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B13

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B14

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-RECOVERY-01-B15

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-RECOVERY-01-I01

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I02

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I03

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I04

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I05

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I06

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I07

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I08

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I09

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I10

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I11

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I12

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I13

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I14

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-RECOVERY-01-I15

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-RECOVERY-01-A01

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A02

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A03

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A04

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A05

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A06

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A07

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A08

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A09

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A10

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A11

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A12

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A13

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A14

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-RECOVERY-01-A15

**Core:** Using versioned snapshots s1:{a:1,b:2},s2:{a:3,b:2},s3:{a:3}, prepare SQL to inspect the state at a supplied historical statement/time and recover deleted b into a scratch table without overwriting current a. Retention is supplied by the interviewer,not assumed.

**Acceptance example / fixture:** Recovered b:2; current a remains3.

**Question:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
