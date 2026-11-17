# AWS Data Engineering: Foundations

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Cloud versus on premises

### Beginner

#### AWS-FOUNDATIONS-01-B01

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B02

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B03

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B04

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B05

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B06

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B07

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B08

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B09

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B10

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Return the core's dependency/resource graph and validate every referenced node exists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B11

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B12

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Produce a dry-run plan describing observable actions with no external mutation calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B13

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B14

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-01-B15

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-FOUNDATIONS-01-I01

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I02

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I03

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I04

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I05

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I06

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I07

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I08

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I09

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I10

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I11

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I12

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I13

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I14

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-01-I15

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-FOUNDATIONS-01-A01

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A02

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A03

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A04

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A05

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A06

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A07

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A08

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A09

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A10

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A11

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A12

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A13

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A14

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-01-A15

**Core:** Given hourly demand [2,2,8,8], unit cloud cost 3 per unit-hour and fixed on-prem capacity 8 at cost 50 per day, calculate cost and unmet demand for each option. Return a choice based first on zero unmet demand then lowest cost; ignore migration and taxes for this model.

**Acceptance example / fixture:** Cloud cost 60,unmet 0; on-prem cost 50,unmet 0 -> on-prem.

**Question:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Console and account selection

### Beginner

#### AWS-FOUNDATIONS-02-B01

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B02

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B03

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B04

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B05

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B06

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B07

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B08

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B09

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B10

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B11

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B12

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B13

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B14

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-02-B15

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-FOUNDATIONS-02-I01

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I02

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I03

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I04

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I05

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I06

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I07

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I08

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I09

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I10

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I11

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I12

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I13

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I14

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-02-I15

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-FOUNDATIONS-02-A01

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A02

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A03

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A04

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A05

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A06

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A07

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A08

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A09

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A10

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A11

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A12

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A13

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A14

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-02-A15

**Core:** Implement a preflight checker for requested {account,region,environment} against an allowlist. A production environment requires an explicit production flag. Return all mismatch fields sorted; no resource changes are allowed before the checker passes.

**Acceptance example / fixture:** Requested account B with allowlist A -> account mismatch and zero mutation calls.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Local profiles and credentials

### Beginner

#### AWS-FOUNDATIONS-03-B01

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B02

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B03

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B04

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B05

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B06

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B07

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B08

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B09

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B10

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B11

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B12

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B13

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B14

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-FOUNDATIONS-03-B15

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-FOUNDATIONS-03-I01

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I02

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I03

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I04

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I05

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I06

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I07

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I08

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I09

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I10

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I11

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I12

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I13

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I14

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-FOUNDATIONS-03-I15

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-FOUNDATIONS-03-A01

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A02

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A03

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A04

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A05

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A06

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A07

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A08

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A09

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A10

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A11

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A12

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A13

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A14

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-FOUNDATIONS-03-A15

**Core:** Implement profile selection from explicit profile then TRAINING_PROFILE then default. Credentials are supplied by an injected provider; never copy secrets into the result/log. Reject missing credentials or account mismatch before simulated work.

**Acceptance example / fixture:** Explicit student overrides environment instructor; wrong resolved account -> denied.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
