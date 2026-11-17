# AWS Data Engineering: Identity

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## IAM users

### Beginner

#### AWS-IDENTITY-01-B01

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement the core calculation on the supplied local inputs and return exact metric/finding outputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B02

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Run an empty observation period and preserve the core's distinction between zero,missing and unknown.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B03

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement half-open window assignment with injected timestamps. Show an event exactly at start and exactly at end.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B04

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Return a per-input contribution trace so the final counts/totals can be recomputed independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B05

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Validate observation fields and return rejected indices; malformed values must not become zero-valued measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B06

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Sort the report by its declared group/time keys and return deterministic output for reordered input where order has no business meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B07

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Return both numerator and denominator for every ratio in the core. If there is no ratio,return contributing record count alongside each total.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B08

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Create a summary report reconciling group totals/counts to the global result without double-counting rejected records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B09

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Demonstrate the exact equality boundary of the core's threshold. Show why greater-than and greater-than-or-equal yield different decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B10

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Return a finding explanation containing only safe identifiers,rule name and measured value; exclude secret payloads.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B11

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement a one-period-at-a-time evaluator and compare its result with batch evaluation on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B12

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Create a no-side-effect preview of findings/alerts without invoking any notification channel.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B13

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Retain original observation IDs in diagnostics so a reported anomaly can be traced to source evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B14

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Produce an NDJSON report with a schema version and exact integer amounts where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-01-B15

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Build an acceptance table with expected and actual findings for normal,empty and boundary inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-IDENTITY-01-I01

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Deduplicate identical observation IDs and reject conflicting duplicate payloads. Compare counts before and after deduplication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I02

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement incremental state across observation batches and prove concatenated-batch results equal one complete batch under the core's ordering rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I03

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Add hysteresis for alerts: fire using the core rule and resolve after two consecutive known good periods. Missing data cannot count as good.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I04

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Add per-group state so a problem in service/tenant A cannot advance the alarm streak for B.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I05

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Introduce out-of-order observations and a supplied watermark. Recompute open windows; emit corrections rather than silently altering a finalized report.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I06

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Use exact rational comparison for rate thresholds,avoiding an unnecessary floating-point boundary error. Return numerator,denominator and decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I07

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Add a notification deduplication key based on rule,group and transition sequence. Repeated report delivery cannot create a second identical alert intent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I08

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement a configurable threshold with validated type/range and version it in every finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I09

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Compare two observation snapshots and classify new,resolved and unchanged findings by stable identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I10

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Add per-group quality counts for missing and invalid data. Do not hide a missing-data incident behind a zero failure rate.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I11

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Build a baseline/actual comparison for signed integer costs or counts. Reconcile adjustments and flag complete-record differences even when grand totals match.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I12

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Introduce a deterministic notification mock that fails once. Preserve pending alert state and retry without creating a new transition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I13

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Bound retained state by finalized window plus explicitly configured lateness. Demonstrate which observations become TOO_LATE.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I14

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Produce a safe audit report mapping every sent notification to an actual computed transition and its rule version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-01-I15

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Construct an adversarial observation sequence that exposes a threshold,window,duplicate or missing-data shortcut and demonstrate the corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-IDENTITY-01-A01

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement restartable evaluator state and durable alert-intent publication. Inject a crash around both checkpoints and prove transitions are neither lost nor repeatedly published.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A02

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Model two evaluator replicas consuming overlapping data. Use versioned ownership/fencing so only one publishes a transition for each group/window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A03

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Handle late corrections to already published metrics with revisioned reports and explicit corrective notifications rather than rewriting audit history.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A04

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement a bounded-memory merge of large sorted observation streams and compare final findings with the simple batch reference on small fixtures.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A05

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Build differential generated tests for threshold boundaries,missing periods,out-of-order events,duplicate IDs and signed adjustments applicable to the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A06

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Separate data freshness failure from measured-service failure. Demonstrate a stale feed that must not be reported as a healthy zero-error service.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A07

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Add rule-version rollout with historical replay. Show exactly which findings change because of rule changes rather than changed observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A08

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement tenant-isolated state and fair bounded processing so one noisy tenant cannot corrupt or indefinitely block another tenant's reports.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A09

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Reconstruct an incident from raw observation IDs,rule versions,state checkpoints and notification journal. Detect one deliberately missing notification or phantom finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A10

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Model ambiguous notification acknowledgment. Reconcile by durable notification key and retain UNKNOWN if the receiver cannot confirm its effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A11

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Add a conservation checker independent of the metric implementation. Detect a dropped input,double contribution and mismatched allocation bucket.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A12

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Measure actual update work and retained state under skewed groups and late-event bursts. Preserve correctness and provide evidence for a bounded-state design.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A13

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Implement a safe export with irreversible redaction of secret fields and stable pseudonymous identifiers where needed for correlation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A14

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Design a backfill replay that cannot page operators with historical alerts unless explicitly requested. Retain separate replay/run identities in the journal.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-01-A15

**Core:** Implement an access-review function for synthetic IAM user records {name,enabled,last_used_day,keys}. At day 100, flag enabled users not used in more than 30 days and active keys older than 60 days. Return sorted user/reason findings; null last_used means never-used and is flagged.

**Acceptance example / fixture:** User a enabled,last_used 60 -> inactive finding; key created day 39 -> old key.

**Question:** Deliver the evaluator with exact calculations,quality signals,late corrections,durable transitions,notification recovery and an independently checked incident trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## IAM roles

### Beginner

#### AWS-IDENTITY-02-B01

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B02

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B03

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B04

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B05

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B06

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B07

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B08

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B09

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B10

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B11

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B12

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B13

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B14

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-02-B15

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-IDENTITY-02-I01

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I02

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I03

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I04

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I05

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I06

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I07

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I08

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I09

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I10

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I11

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I12

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I13

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I14

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-02-I15

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-IDENTITY-02-A01

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A02

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A03

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A04

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A05

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A06

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A07

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A08

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A09

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A10

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A11

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A12

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A13

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A14

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-02-A15

**Core:** Implement a simplified role-assumption model. A request succeeds only if actor appears in trusted_principals, requested session seconds is positive and <= max_session_seconds, and required MFA is present. Return ALLOW or sorted rejection reasons. This is a local contract, not a full IAM evaluator.

**Acceptance example / fixture:** Trusted a,max=3600,MFA required; a,3601,no MFA -> duration and mfa denied.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## IAM groups

### Beginner

#### AWS-IDENTITY-03-B01

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B02

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B03

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B04

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B05

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B06

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B07

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B08

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B09

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B10

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B11

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B12

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B13

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B14

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-03-B15

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-IDENTITY-03-I01

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I02

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I03

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I04

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I05

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I06

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I07

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I08

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I09

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I10

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I11

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I12

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I13

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I14

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-03-I15

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-IDENTITY-03-A01

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A02

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A03

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A04

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A05

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A06

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A07

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A08

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A09

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A10

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A11

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A12

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A13

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A14

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-03-A15

**Core:** Compute direct-user plus group-granted action sets in a local model. Disabled users have none. Explicit deny actions remove matching allows; action tokens are exact strings, with no wildcards. Return sorted effective actions.

**Acceptance example / fixture:** User allows read,group allows write,group denies read -> [write].

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## KMS encryption grants

### Beginner

#### AWS-IDENTITY-04-B01

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B02

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B03

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B04

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B05

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B06

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B07

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B08

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B09

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B10

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B11

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B12

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B13

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B14

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-04-B15

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-IDENTITY-04-I01

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I02

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I03

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I04

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I05

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I06

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I07

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I08

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I09

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I10

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I11

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I12

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I13

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I14

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-04-I15

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-IDENTITY-04-A01

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A02

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A03

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A04

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A05

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A06

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A07

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A08

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A09

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A10

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A11

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A12

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A13

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A14

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-04-A15

**Core:** Implement a local envelope-decryption decision requiring authenticated principal, an exact Decrypt grant for key ID, and matching expected encryption context tenant. Return ALLOW or sorted failed checks; log no plaintext/key material.

**Acceptance example / fixture:** Key k grant to a,expected tenant t1,request tenant t2 -> context denied.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Secrets Manager rotation

### Beginner

#### AWS-IDENTITY-05-B01

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B02

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B03

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B04

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B05

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B06

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B07

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B08

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B09

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B10

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B11

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B12

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B13

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B14

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-IDENTITY-05-B15

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-IDENTITY-05-I01

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I02

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I03

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I04

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I05

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I06

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I07

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I08

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I09

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I10

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I11

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I12

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I13

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I14

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-IDENTITY-05-I15

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-IDENTITY-05-A01

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A02

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A03

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A04

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A05

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A06

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A07

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A08

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A09

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A10

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A11

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A12

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A13

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A14

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-IDENTITY-05-A15

**Core:** Model secret versions with CURRENT and PREVIOUS labels and a pending rotation. Promote pending only after validation succeeds; previous current becomes PREVIOUS. A failed validation must leave current untouched. Return labels only, never secret values.

**Acceptance example / fixture:** v1 current; v2 pending fails -> current v1; success -> v2 current,v1 previous.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
