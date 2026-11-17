# GCP Data Engineering: Operations

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Logging and alerting

### Beginner

#### GCP-OPERATIONS-01-B01

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement the core calculation on the supplied local inputs and return exact metric/finding outputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B02

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Run an empty observation period and preserve the core's distinction between zero,missing and unknown.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B03

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement half-open window assignment with injected timestamps. Show an event exactly at start and exactly at end.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B04

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Return a per-input contribution trace so the final counts/totals can be recomputed independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B05

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Validate observation fields and return rejected indices; malformed values must not become zero-valued measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B06

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Sort the report by its declared group/time keys and return deterministic output for reordered input where order has no business meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B07

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Return both numerator and denominator for every ratio in the core. If there is no ratio,return contributing record count alongside each total.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B08

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Create a summary report reconciling group totals/counts to the global result without double-counting rejected records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B09

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Demonstrate the exact equality boundary of the core's threshold. Show why greater-than and greater-than-or-equal yield different decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B10

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Return a finding explanation containing only safe identifiers,rule name and measured value; exclude secret payloads.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B11

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement a one-period-at-a-time evaluator and compare its result with batch evaluation on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B12

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Create a no-side-effect preview of findings/alerts without invoking any notification channel.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B13

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Retain original observation IDs in diagnostics so a reported anomaly can be traced to source evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B14

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Produce an NDJSON report with a schema version and exact integer amounts where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-01-B15

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Build an acceptance table with expected and actual findings for normal,empty and boundary inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-OPERATIONS-01-I01

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Deduplicate identical observation IDs and reject conflicting duplicate payloads. Compare counts before and after deduplication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I02

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement incremental state across observation batches and prove concatenated-batch results equal one complete batch under the core's ordering rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I03

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Add hysteresis for alerts: fire using the core rule and resolve after two consecutive known good periods. Missing data cannot count as good.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I04

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Add per-group state so a problem in service/tenant A cannot advance the alarm streak for B.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I05

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Introduce out-of-order observations and a supplied watermark. Recompute open windows; emit corrections rather than silently altering a finalized report.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I06

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Use exact rational comparison for rate thresholds,avoiding an unnecessary floating-point boundary error. Return numerator,denominator and decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I07

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Add a notification deduplication key based on rule,group and transition sequence. Repeated report delivery cannot create a second identical alert intent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I08

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement a configurable threshold with validated type/range and version it in every finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I09

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Compare two observation snapshots and classify new,resolved and unchanged findings by stable identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I10

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Add per-group quality counts for missing and invalid data. Do not hide a missing-data incident behind a zero failure rate.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I11

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Build a baseline/actual comparison for signed integer costs or counts. Reconcile adjustments and flag complete-record differences even when grand totals match.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I12

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Introduce a deterministic notification mock that fails once. Preserve pending alert state and retry without creating a new transition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I13

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Bound retained state by finalized window plus explicitly configured lateness. Demonstrate which observations become TOO_LATE.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I14

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Produce a safe audit report mapping every sent notification to an actual computed transition and its rule version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-01-I15

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Construct an adversarial observation sequence that exposes a threshold,window,duplicate or missing-data shortcut and demonstrate the corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-OPERATIONS-01-A01

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement restartable evaluator state and durable alert-intent publication. Inject a crash around both checkpoints and prove transitions are neither lost nor repeatedly published.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A02

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Model two evaluator replicas consuming overlapping data. Use versioned ownership/fencing so only one publishes a transition for each group/window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A03

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Handle late corrections to already published metrics with revisioned reports and explicit corrective notifications rather than rewriting audit history.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A04

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement a bounded-memory merge of large sorted observation streams and compare final findings with the simple batch reference on small fixtures.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A05

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Build differential generated tests for threshold boundaries,missing periods,out-of-order events,duplicate IDs and signed adjustments applicable to the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A06

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Separate data freshness failure from measured-service failure. Demonstrate a stale feed that must not be reported as a healthy zero-error service.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A07

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Add rule-version rollout with historical replay. Show exactly which findings change because of rule changes rather than changed observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A08

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement tenant-isolated state and fair bounded processing so one noisy tenant cannot corrupt or indefinitely block another tenant's reports.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A09

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Reconstruct an incident from raw observation IDs,rule versions,state checkpoints and notification journal. Detect one deliberately missing notification or phantom finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A10

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Model ambiguous notification acknowledgment. Reconcile by durable notification key and retain UNKNOWN if the receiver cannot confirm its effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A11

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Add a conservation checker independent of the metric implementation. Detect a dropped input,double contribution and mismatched allocation bucket.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A12

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Measure actual update work and retained state under skewed groups and late-event bursts. Preserve correctness and provide evidence for a bounded-state design.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A13

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Implement a safe export with irreversible redaction of secret fields and stable pseudonymous identifiers where needed for correlation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A14

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Design a backfill replay that cannot page operators with historical alerts unless explicitly requested. Retain separate replay/run identities in the journal.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-01-A15

**Core:** From deduplicated logs {id,service,time,outcome}, calculate failure rate per service in supplied half-open windows. Zero requests -> null rate. Return service/time sorted rows and flag rate>0.05.

**Acceptance example / fixture:** 19 success,1 failure -> .05 and no flag; no requests -> null.

**Question:** Deliver the evaluator with exact calculations,quality signals,late corrections,durable transitions,notification recovery and an independently checked incident trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Terraform resource dependencies

### Beginner

#### GCP-OPERATIONS-02-B01

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B02

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B03

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B04

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B05

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B06

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B07

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B08

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B09

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B10

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B11

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B12

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B13

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B14

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-OPERATIONS-02-B15

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-OPERATIONS-02-I01

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I02

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I03

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I04

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I05

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I06

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I07

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I08

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I09

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I10

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I11

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I12

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I13

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I14

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-OPERATIONS-02-I15

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-OPERATIONS-02-A01

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A02

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A03

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A04

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A05

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A06

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A07

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A08

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A09

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A10

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A11

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A12

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A13

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A14

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-OPERATIONS-02-A15

**Core:** Topologically order resource operations from a supplied dependency graph; lexicographic tie breaking. Detect missing dependency references and cycles before any apply operation. Do not run Terraform against real accounts.

**Acceptance example / fixture:** bucket->dataset and service_account->dataset -> bucket,service_account,dataset.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
