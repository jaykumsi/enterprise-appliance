# AWS Data Engineering: Observability

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## CloudTrail audit trails

### Beginner

#### AWS-OBSERVABILITY-01-B01

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement the core calculation on the supplied local inputs and return exact metric/finding outputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B02

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Run an empty observation period and preserve the core's distinction between zero,missing and unknown.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B03

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement half-open window assignment with injected timestamps. Show an event exactly at start and exactly at end.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B04

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Return a per-input contribution trace so the final counts/totals can be recomputed independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B05

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Validate observation fields and return rejected indices; malformed values must not become zero-valued measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B06

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Sort the report by its declared group/time keys and return deterministic output for reordered input where order has no business meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B07

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Return both numerator and denominator for every ratio in the core. If there is no ratio,return contributing record count alongside each total.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B08

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Create a summary report reconciling group totals/counts to the global result without double-counting rejected records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B09

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Demonstrate the exact equality boundary of the core's threshold. Show why greater-than and greater-than-or-equal yield different decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B10

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Return a finding explanation containing only safe identifiers,rule name and measured value; exclude secret payloads.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B11

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement a one-period-at-a-time evaluator and compare its result with batch evaluation on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B12

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Create a no-side-effect preview of findings/alerts without invoking any notification channel.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B13

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Retain original observation IDs in diagnostics so a reported anomaly can be traced to source evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B14

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Produce an NDJSON report with a schema version and exact integer amounts where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-01-B15

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Build an acceptance table with expected and actual findings for normal,empty and boundary inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-OBSERVABILITY-01-I01

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Deduplicate identical observation IDs and reject conflicting duplicate payloads. Compare counts before and after deduplication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I02

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement incremental state across observation batches and prove concatenated-batch results equal one complete batch under the core's ordering rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I03

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Add hysteresis for alerts: fire using the core rule and resolve after two consecutive known good periods. Missing data cannot count as good.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I04

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Add per-group state so a problem in service/tenant A cannot advance the alarm streak for B.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I05

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Introduce out-of-order observations and a supplied watermark. Recompute open windows; emit corrections rather than silently altering a finalized report.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I06

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Use exact rational comparison for rate thresholds,avoiding an unnecessary floating-point boundary error. Return numerator,denominator and decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I07

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Add a notification deduplication key based on rule,group and transition sequence. Repeated report delivery cannot create a second identical alert intent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I08

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement a configurable threshold with validated type/range and version it in every finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I09

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Compare two observation snapshots and classify new,resolved and unchanged findings by stable identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I10

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Add per-group quality counts for missing and invalid data. Do not hide a missing-data incident behind a zero failure rate.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I11

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Build a baseline/actual comparison for signed integer costs or counts. Reconcile adjustments and flag complete-record differences even when grand totals match.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I12

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Introduce a deterministic notification mock that fails once. Preserve pending alert state and retry without creating a new transition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I13

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Bound retained state by finalized window plus explicitly configured lateness. Demonstrate which observations become TOO_LATE.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I14

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Produce a safe audit report mapping every sent notification to an actual computed transition and its rule version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-01-I15

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Construct an adversarial observation sequence that exposes a threshold,window,duplicate or missing-data shortcut and demonstrate the corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-OBSERVABILITY-01-A01

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement restartable evaluator state and durable alert-intent publication. Inject a crash around both checkpoints and prove transitions are neither lost nor repeatedly published.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A02

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Model two evaluator replicas consuming overlapping data. Use versioned ownership/fencing so only one publishes a transition for each group/window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A03

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Handle late corrections to already published metrics with revisioned reports and explicit corrective notifications rather than rewriting audit history.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A04

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement a bounded-memory merge of large sorted observation streams and compare final findings with the simple batch reference on small fixtures.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A05

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Build differential generated tests for threshold boundaries,missing periods,out-of-order events,duplicate IDs and signed adjustments applicable to the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A06

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Separate data freshness failure from measured-service failure. Demonstrate a stale feed that must not be reported as a healthy zero-error service.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A07

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Add rule-version rollout with historical replay. Show exactly which findings change because of rule changes rather than changed observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A08

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement tenant-isolated state and fair bounded processing so one noisy tenant cannot corrupt or indefinitely block another tenant's reports.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A09

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Reconstruct an incident from raw observation IDs,rule versions,state checkpoints and notification journal. Detect one deliberately missing notification or phantom finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A10

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Model ambiguous notification acknowledgment. Reconcile by durable notification key and retain UNKNOWN if the receiver cannot confirm its effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A11

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Add a conservation checker independent of the metric implementation. Detect a dropped input,double contribution and mismatched allocation bucket.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A12

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Measure actual update work and retained state under skewed groups and late-event bursts. Preserve correctness and provide evidence for a bounded-state design.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A13

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Implement a safe export with irreversible redaction of secret fields and stable pseudonymous identifiers where needed for correlation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A14

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Design a backfill replay that cannot page operators with historical alerts unless explicitly requested. Retain separate replay/run identities in the journal.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-01-A15

**Core:** Given audit events {id,time,actor,action,resource,outcome}, find denied Delete actions in [start,end), deduplicate repeated IDs and order by time,id. Conflicting duplicate IDs are flagged rather than silently discarded.

**Acceptance example / fixture:** Denied Delete at start included; at end excluded.

**Question:** Deliver the evaluator with exact calculations,quality signals,late corrections,durable transitions,notification recovery and an independently checked incident trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## CloudWatch metrics and alarms

### Beginner

#### AWS-OBSERVABILITY-02-B01

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement the core calculation on the supplied local inputs and return exact metric/finding outputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B02

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Run an empty observation period and preserve the core's distinction between zero,missing and unknown.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B03

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement half-open window assignment with injected timestamps. Show an event exactly at start and exactly at end.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B04

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Return a per-input contribution trace so the final counts/totals can be recomputed independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B05

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Validate observation fields and return rejected indices; malformed values must not become zero-valued measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B06

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Sort the report by its declared group/time keys and return deterministic output for reordered input where order has no business meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B07

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Return both numerator and denominator for every ratio in the core. If there is no ratio,return contributing record count alongside each total.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B08

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Create a summary report reconciling group totals/counts to the global result without double-counting rejected records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B09

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Demonstrate the exact equality boundary of the core's threshold. Show why greater-than and greater-than-or-equal yield different decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B10

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Return a finding explanation containing only safe identifiers,rule name and measured value; exclude secret payloads.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B11

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement a one-period-at-a-time evaluator and compare its result with batch evaluation on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B12

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Create a no-side-effect preview of findings/alerts without invoking any notification channel.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B13

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Retain original observation IDs in diagnostics so a reported anomaly can be traced to source evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B14

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Produce an NDJSON report with a schema version and exact integer amounts where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-OBSERVABILITY-02-B15

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Build an acceptance table with expected and actual findings for normal,empty and boundary inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-OBSERVABILITY-02-I01

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Deduplicate identical observation IDs and reject conflicting duplicate payloads. Compare counts before and after deduplication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I02

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement incremental state across observation batches and prove concatenated-batch results equal one complete batch under the core's ordering rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I03

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Add hysteresis for alerts: fire using the core rule and resolve after two consecutive known good periods. Missing data cannot count as good.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I04

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Add per-group state so a problem in service/tenant A cannot advance the alarm streak for B.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I05

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Introduce out-of-order observations and a supplied watermark. Recompute open windows; emit corrections rather than silently altering a finalized report.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I06

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Use exact rational comparison for rate thresholds,avoiding an unnecessary floating-point boundary error. Return numerator,denominator and decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I07

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Add a notification deduplication key based on rule,group and transition sequence. Repeated report delivery cannot create a second identical alert intent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I08

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement a configurable threshold with validated type/range and version it in every finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I09

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Compare two observation snapshots and classify new,resolved and unchanged findings by stable identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I10

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Add per-group quality counts for missing and invalid data. Do not hide a missing-data incident behind a zero failure rate.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I11

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Build a baseline/actual comparison for signed integer costs or counts. Reconcile adjustments and flag complete-record differences even when grand totals match.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I12

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Introduce a deterministic notification mock that fails once. Preserve pending alert state and retry without creating a new transition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I13

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Bound retained state by finalized window plus explicitly configured lateness. Demonstrate which observations become TOO_LATE.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I14

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Produce a safe audit report mapping every sent notification to an actual computed transition and its rule version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-OBSERVABILITY-02-I15

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Construct an adversarial observation sequence that exposes a threshold,window,duplicate or missing-data shortcut and demonstrate the corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-OBSERVABILITY-02-A01

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement restartable evaluator state and durable alert-intent publication. Inject a crash around both checkpoints and prove transitions are neither lost nor repeatedly published.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A02

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Model two evaluator replicas consuming overlapping data. Use versioned ownership/fencing so only one publishes a transition for each group/window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A03

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Handle late corrections to already published metrics with revisioned reports and explicit corrective notifications rather than rewriting audit history.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A04

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement a bounded-memory merge of large sorted observation streams and compare final findings with the simple batch reference on small fixtures.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A05

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Build differential generated tests for threshold boundaries,missing periods,out-of-order events,duplicate IDs and signed adjustments applicable to the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A06

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Separate data freshness failure from measured-service failure. Demonstrate a stale feed that must not be reported as a healthy zero-error service.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A07

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Add rule-version rollout with historical replay. Show exactly which findings change because of rule changes rather than changed observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A08

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement tenant-isolated state and fair bounded processing so one noisy tenant cannot corrupt or indefinitely block another tenant's reports.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A09

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Reconstruct an incident from raw observation IDs,rule versions,state checkpoints and notification journal. Detect one deliberately missing notification or phantom finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A10

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Model ambiguous notification acknowledgment. Reconcile by durable notification key and retain UNKNOWN if the receiver cannot confirm its effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A11

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Add a conservation checker independent of the metric implementation. Detect a dropped input,double contribution and mismatched allocation bucket.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A12

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Measure actual update work and retained state under skewed groups and late-event bursts. Preserve correctness and provide evidence for a bounded-state design.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A13

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Implement a safe export with irreversible redaction of secret fields and stable pseudonymous identifiers where needed for correlation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A14

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Design a backfill replay that cannot page operators with historical alerts unless explicitly requested. Retain separate replay/run identities in the journal.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-OBSERVABILITY-02-A15

**Core:** Evaluate consecutive period error-rate alarm: period rate=errors/requests, zero requests is missing. Alarm after three consecutive known periods with rate>0.05; a missing or good period resets the streak. Return alarm transitions.

**Acceptance example / fixture:** Rates [.1,.1,.1] -> alarm on third; [.1,missing,.1] -> no alarm.

**Question:** Deliver the evaluator with exact calculations,quality signals,late corrections,durable transitions,notification recovery and an independently checked incident trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
