# PostgreSQL: Performance

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Indexes and query plans

### Beginner

#### PG-PERFORMANCE-01-B01

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B02

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B03

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B04

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B05

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B06

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B07

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B08

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B09

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B10

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Return the core's dependency/resource graph and validate every referenced node exists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B11

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B12

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Produce a dry-run plan describing observable actions with no external mutation calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B13

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B14

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-01-B15

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-PERFORMANCE-01-I01

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I02

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I03

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I04

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I05

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I06

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I07

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I08

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I09

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I10

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I11

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I12

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I13

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I14

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-01-I15

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-PERFORMANCE-01-A01

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A02

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A03

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A04

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A05

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A06

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A07

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A08

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A09

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A10

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A11

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A12

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A13

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A14

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-01-A15

**Core:** Orders has 10 million rows. The workload filters CustomerID by equality, filters CreatedAt with an inclusive-start/exclusive-end range and orders by CreatedAt then OrderID. Propose index DDL and a repeatable EXPLAIN ANALYZE experiment comparing estimated and actual rows. Return plan evidence, not an invented speedup.

**Acceptance example / fixture:** A useful proposed key order starts CustomerID,CreatedAt,OrderID; measured plan and cost tradeoff are required.

**Question:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Keyset pagination

### Beginner

#### PG-PERFORMANCE-02-B01

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B02

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B03

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B04

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B05

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B06

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B07

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B08

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B09

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B10

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B11

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B12

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B13

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B14

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-02-B15

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### PG-PERFORMANCE-02-I01

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I02

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I03

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I04

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I05

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I06

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I07

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I08

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I09

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I10

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I11

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I12

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I13

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I14

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-02-I15

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### PG-PERFORMANCE-02-A01

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A02

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A03

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A04

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A05

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A06

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A07

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A08

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A09

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A10

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A11

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A12

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A13

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A14

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-02-A15

**Core:** Using fixture Orders, return the next two rows after cursor (CreatedAt=2024-01-02T00:00:00Z,OrderID=2) ordered by CreatedAt then OrderID. Return OrderID and CreatedAt; use no OFFSET.

**Acceptance example / fixture:** Baseline next IDs [3,4].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## Partitioning and retention

### Beginner

#### PG-PERFORMANCE-03-B01

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Solve the concrete core scenario and return a decision,calculation/schema and observable acceptance check. Do not answer with a definition list.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B02

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Construct the smallest working prototype/model of the proposed core design and show its actual output for the example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B03

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** List the core's explicit inputs and constraints as a machine-readable contract. Reject one invalid input with a precise reason.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B04

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Return a step-by-step calculation or data-flow trace for the baseline,with every intermediate value tied to an input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B05

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Demonstrate an empty/no-demand/no-record case applicable to the core without inventing a phantom workload.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B06

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Give a second design satisfying the same core constraints and compare both against the supplied numbers or fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B07

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Write an independent acceptance assertion for the core's main invariant and evaluate it on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B08

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Create a concrete counterexample to a plausible but incorrect core design. Show the violated requirement and a repair.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B09

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Separate mandatory requirements from optimization preferences in executable validation logic; a cheaper option cannot pass if it violates a mandatory constraint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B10

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Return the core's dependency/resource graph and validate every referenced node exists.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B11

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Identify one exact capacity/type/time boundary and compute both sides using the model's supplied constants rather than live prices.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B12

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Produce a dry-run plan describing observable actions with no external mutation calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B13

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Reconcile all core counts/totals/keys back to the original inputs,including excluded or rejected inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B14

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Build a deterministic report containing assumptions explicitly stated in the core,decision and evidence. Flag missing evidence rather than inventing measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-PERFORMANCE-03-B15

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Write a runnable small acceptance test that distinguishes the chosen design from the incorrect counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-PERFORMANCE-03-I01

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Parameterize the core's supplied constants/constraints and show where the preferred valid design changes. Use exact calculations or measured query evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I02

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Add one explicit failure at the core's main dependency and implement a local simulator showing whether the design fails safely or recovers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I03

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Compare the design with a deliberately simpler reference model over a finite input set. Return every differing decision/output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I04

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Add versioned inputs and repeat the decision after one correction. Return exactly which inputs and outputs changed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I05

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Implement a reconciliation check independent of the primary design,then seed a dropped/duplicated contribution or key to demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I06

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Support a batch of independent scenarios under a shared finite resource budget. State the allocation policy and demonstrate rejected/deferred work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I07

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Introduce a typed configuration validator for the design and return all incompatible options before preparing any action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I08

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Add a dry-run-versus-apply simulator using expected revision checks. A stale plan must not overwrite newer modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I09

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Construct a skewed/adversarial workload and compare actual work in the simple prototype with the proposed improvement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I10

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Write a migration plan from a stated old representation to the proposed design,including observable compatibility checks and preserved business invariants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I11

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Add safe diagnostic logging with input identity,decision and evidence references; do not log raw credentials or sensitive row values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I12

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Demonstrate a retry after an injected transient failure without duplicating any accepted business effect in the model.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I13

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Write a deterministic acceptance matrix across normal,boundary,invalid,empty and failed-dependency cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I14

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Expose uncertainty as UNKNOWN when required measurements/metadata are missing. Show a case where guessing would incorrectly pass a requirement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-PERFORMANCE-03-I15

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Create a review artifact with implemented prototype,actual evidence,tradeoffs and unresolved native-runtime checks. Clearly separate measured facts from predictions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-PERFORMANCE-03-A01

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Model concurrent actors changing the core's input/state between planning and action. Add a commit-time precondition and show safe conflict handling.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A02

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Implement restartable execution of the proposed design with durable step IDs and injected failures around commit boundaries.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A03

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Design a staged rollout keeping old and new consumers compatible. Prove the point at which old representation removal becomes safe.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A04

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Build generated adversarial tests comparing the prototype to the independent reference. Persist a reproducible counterexample instead of only aggregate pass counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A05

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Quantify a resource/performance/cost tradeoff under the core's explicit model and changed demand. Do not replace supplied toy constants with unverified provider claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A06

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Handle an ambiguous external action outcome. Reconcile durable action identity before retry and retain UNKNOWN if evidence remains insufficient.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A07

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Introduce multi-tenant ownership boundaries and demonstrate that a valid operation in one tenant cannot affect another's modeled state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A08

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Implement immutable snapshots for reproducible design decisions. A result must reference the exact input,rule/schema and measurement versions used.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A09

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Add bounded-memory/backpressure behavior for a large workload and measure retained work in the local prototype.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A10

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Create an independent incident reconstruction from state versions,action journal and evidence. Detect an intentionally inconsistent claimed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A11

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Design recovery from one-way/irreversible modeled actions using compensating operations where possible. Record unresolved effects honestly rather than calling compensation a rollback.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A12

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Demonstrate a drifted actual environment relative to the proposed desired state. Produce a targeted plan respecting declared ownership and preserve unmanaged values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A13

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Evaluate a worst-case workload and show whether the mandatory service/capacity/integrity requirements still hold. Supply calculations or actual experiment output.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A14

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Provide a dialect/runtime/provider compatibility adapter and enumerate unsupported features explicitly. Prove behavior on the shared supported subset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-PERFORMANCE-03-A15

**Core:** Design monthly range partitions for UTC Events(at,id) with half-open month boundaries. Route Jan 31 23:59:59Z and Feb 1 00:00:00Z, then write a retention plan that removes January while February remains queryable. Supply DDL and checks.

**Acceptance example / fixture:** First event -> January; second -> February; retained February count unchanged.

**Question:** Deliver a reviewable implementation/model with independent correctness checks,measured evidence,concurrency/failure recovery and explicit limits of the local simulation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
