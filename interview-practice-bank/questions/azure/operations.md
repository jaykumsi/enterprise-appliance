# Azure Data Engineering: Operations

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Azure Monitor alert logic

### Beginner

#### AZ-OPERATIONS-01-B01

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement the core calculation on the supplied local inputs and return exact metric/finding outputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B02

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Run an empty observation period and preserve the core's distinction between zero,missing and unknown.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B03

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement half-open window assignment with injected timestamps. Show an event exactly at start and exactly at end.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B04

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Return a per-input contribution trace so the final counts/totals can be recomputed independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B05

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Validate observation fields and return rejected indices; malformed values must not become zero-valued measurements.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B06

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Sort the report by its declared group/time keys and return deterministic output for reordered input where order has no business meaning.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B07

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Return both numerator and denominator for every ratio in the core. If there is no ratio,return contributing record count alongside each total.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B08

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Create a summary report reconciling group totals/counts to the global result without double-counting rejected records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B09

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Demonstrate the exact equality boundary of the core's threshold. Show why greater-than and greater-than-or-equal yield different decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B10

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Return a finding explanation containing only safe identifiers,rule name and measured value; exclude secret payloads.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B11

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement a one-period-at-a-time evaluator and compare its result with batch evaluation on the baseline.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B12

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Create a no-side-effect preview of findings/alerts without invoking any notification channel.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B13

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Retain original observation IDs in diagnostics so a reported anomaly can be traced to source evidence.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B14

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Produce an NDJSON report with a schema version and exact integer amounts where applicable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-01-B15

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Build an acceptance table with expected and actual findings for normal,empty and boundary inputs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-OPERATIONS-01-I01

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Deduplicate identical observation IDs and reject conflicting duplicate payloads. Compare counts before and after deduplication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I02

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement incremental state across observation batches and prove concatenated-batch results equal one complete batch under the core's ordering rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I03

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Add hysteresis for alerts: fire using the core rule and resolve after two consecutive known good periods. Missing data cannot count as good.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I04

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Add per-group state so a problem in service/tenant A cannot advance the alarm streak for B.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I05

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Introduce out-of-order observations and a supplied watermark. Recompute open windows; emit corrections rather than silently altering a finalized report.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I06

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Use exact rational comparison for rate thresholds,avoiding an unnecessary floating-point boundary error. Return numerator,denominator and decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I07

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Add a notification deduplication key based on rule,group and transition sequence. Repeated report delivery cannot create a second identical alert intent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I08

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement a configurable threshold with validated type/range and version it in every finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I09

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Compare two observation snapshots and classify new,resolved and unchanged findings by stable identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I10

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Add per-group quality counts for missing and invalid data. Do not hide a missing-data incident behind a zero failure rate.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I11

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Build a baseline/actual comparison for signed integer costs or counts. Reconcile adjustments and flag complete-record differences even when grand totals match.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I12

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Introduce a deterministic notification mock that fails once. Preserve pending alert state and retry without creating a new transition.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I13

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Bound retained state by finalized window plus explicitly configured lateness. Demonstrate which observations become TOO_LATE.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I14

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Produce a safe audit report mapping every sent notification to an actual computed transition and its rule version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-01-I15

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Construct an adversarial observation sequence that exposes a threshold,window,duplicate or missing-data shortcut and demonstrate the corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-OPERATIONS-01-A01

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement restartable evaluator state and durable alert-intent publication. Inject a crash around both checkpoints and prove transitions are neither lost nor repeatedly published.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A02

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Model two evaluator replicas consuming overlapping data. Use versioned ownership/fencing so only one publishes a transition for each group/window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A03

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Handle late corrections to already published metrics with revisioned reports and explicit corrective notifications rather than rewriting audit history.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A04

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement a bounded-memory merge of large sorted observation streams and compare final findings with the simple batch reference on small fixtures.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A05

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Build differential generated tests for threshold boundaries,missing periods,out-of-order events,duplicate IDs and signed adjustments applicable to the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A06

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Separate data freshness failure from measured-service failure. Demonstrate a stale feed that must not be reported as a healthy zero-error service.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A07

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Add rule-version rollout with historical replay. Show exactly which findings change because of rule changes rather than changed observations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A08

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement tenant-isolated state and fair bounded processing so one noisy tenant cannot corrupt or indefinitely block another tenant's reports.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A09

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Reconstruct an incident from raw observation IDs,rule versions,state checkpoints and notification journal. Detect one deliberately missing notification or phantom finding.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A10

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Model ambiguous notification acknowledgment. Reconcile by durable notification key and retain UNKNOWN if the receiver cannot confirm its effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A11

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Add a conservation checker independent of the metric implementation. Detect a dropped input,double contribution and mismatched allocation bucket.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A12

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Measure actual update work and retained state under skewed groups and late-event bursts. Preserve correctness and provide evidence for a bounded-state design.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A13

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Implement a safe export with irreversible redaction of secret fields and stable pseudonymous identifiers where needed for correlation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A14

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Design a backfill replay that cannot page operators with historical alerts unless explicitly requested. Retain separate replay/run identities in the journal.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-01-A15

**Core:** Alarm after three consecutive periods where failures/requests>0.05. Zero-request periods reset the streak as missing. Resolve after two consecutive known good periods. Return transition times only.

**Acceptance example / fixture:** bad,bad,bad,good,good -> ALARM at3,RESOLVED at5.

**Question:** Deliver the evaluator with exact calculations,quality signals,late corrections,durable transitions,notification recovery and an independently checked incident trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Network and private endpoint diagnosis

### Beginner

#### AZ-OPERATIONS-02-B01

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B02

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B03

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B04

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B05

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B06

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B07

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B08

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B09

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B10

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B11

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B12

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B13

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B14

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-02-B15

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-OPERATIONS-02-I01

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I02

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I03

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I04

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I05

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I06

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I07

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I08

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I09

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I10

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I11

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I12

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I13

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I14

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-02-I15

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-OPERATIONS-02-A01

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A02

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A03

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A04

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A05

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A06

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A07

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A08

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A09

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A10

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A11

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A12

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A13

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A14

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-02-A15

**Core:** Given DNS answers,route reachability,firewall grants and identity grants, return failed checks in dependency order DNS,ROUTE,FIREWALL,IDENTITY. A successful TCP connection alone does not mean data access succeeds.

**Acceptance example / fixture:** DNS valid,route true,firewall true,identity false -> IDENTITY failure.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Infrastructure plan validation

### Beginner

#### AZ-OPERATIONS-03-B01

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement the core preflight/configuration function and return all findings for the acceptance example without making external changes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B02

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Run one fully valid and one invalid configuration and return exact field-level diagnostics in deterministic order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B03

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Distinguish a missing required field from an explicitly empty field in the diagnostic; both remain invalid when the core requires nonempty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B04

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Enforce the core's numeric/enum boundary,or exact allowlist equality if no numeric boundary exists. Demonstrate an accepted endpoint and its rejected neighbor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B05

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Return a sanitized effective configuration containing nonsecret values and secret-presence flags only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B06

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement a dry-run adapter recording intended calls but invoking none. Prove a failed preflight records no mutation call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B07

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Validate two independent configuration objects in one batch and return findings by original index without merging their settings.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B08

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Reject unknown configuration keys with UNKNOWN_FIELD rather than silently treating a typo as a valid default.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B09

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement a deterministic formatter for diagnostics with path,code and safe message. Do not include raw credential or connection-string contents.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B10

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Return the dependency order of the core's checks and the first blocking check,while retaining a complete finding list where checks are independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B11

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement explicit defaults only for optional fields; return which effective values came from defaults.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B12

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Create an immutable validated configuration object. Demonstrate that later caller mutation cannot change an already validated execution plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B13

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Build a compatibility check between two effective configurations,reporting exactly which nonsecret values differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B14

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement a JSON input/output adapter that rejects malformed documents before any provider/probe call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-OPERATIONS-03-B15

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Write an acceptance runner with input,expected diagnostic paths,actual paths and pass,including a secret-redaction assertion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-OPERATIONS-03-I01

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add configuration sources with explicit precedence: command override,environment,file,default. Return the provenance of every effective nonsecret field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I02

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Resolve references through an injected secret provider only after nonsecret validation succeeds. Return provider failures separately and log no returned secret material.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I03

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add a versioned configuration schema. Reject unsupported versions before execution and implement an explicit v1-to-v2 converter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I04

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement a plan diff classifying changes as no-op,update or replacement using a rule table you state for the core's fields. Do not apply the plan.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I05

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add an expected revision to configuration updates; reject stale writers rather than overwriting a newer valid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I06

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement functional readiness checks with injected outcomes,not merely existence/container-running checks. Return the dependency that actually prevents useful work.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I07

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Introduce bounded probe retries: at most three total attempts at times0,1,3 using an injected clock. Do not retry permanent invalid configuration.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I08

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Separate local/test/cloud execution modes. Reject endpoint/credential combinations forbidden by the core's mode contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I09

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Validate nested configurations and return JSON-pointer-style paths sorted lexicographically,including independent errors in the same object.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I10

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Build a reversible in-memory apply simulator that publishes the validated configuration only after every prerequisite check passes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I11

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add a configuration fingerprint using a declared canonical encoding,excluding secrets but including secret reference/version identifiers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I12

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Construct a path/identifier injection attempt applicable to the core. Reject it using parsing/allowlists rather than attempting shell string escaping.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I13

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement an audit diff exposing changed field names and safe old/new values. Secret changes reveal reference/version only.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I14

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add a maximum plan size/probe count budget and return RESOURCE_LIMIT before partial execution if it would be exceeded.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-OPERATIONS-03-I15

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Compare actual observed configuration metadata with desired state and return targeted drift findings without automatically repairing them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-OPERATIONS-03-A01

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement a two-phase validate/activate rollout with immutable configuration revision. A failed activation leaves the previous revision authoritative.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A02

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Handle competing operators with optimistic revisions and a durable plan journal. Show that a stale approved plan cannot overwrite a newer live revision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A03

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Inject failure after validation,before publication and after publication before acknowledgment. Reconcile by revision and operation ID before retrying.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A04

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Design safe secret rotation using reference versions. Validate new dependencies before switching and prove secrets never appear in logs,diffs or exported plans.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A05

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add continuous readiness monitoring with explicit hysteresis: become unhealthy after three failed probes,healthy after two successful probes. Test with deterministic injected time.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A06

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Model partially available dependencies and return UNKNOWN when evidence is insufficient. Do not treat timeout as proof that the desired state is absent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A07

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement a versioned rollout to two simulated replicas. Return per-replica revision and prevent work requiring a minimum revision from reaching an outdated replica.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A08

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Build differential tests for resolution precedence,schema conversion and redaction. Generate conflicting source values and prove the winning provenance is correct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A09

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Design a bounded dependency-graph validator detecting cycles and missing references before activation. Return a concrete cycle witness,not a recursion error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A10

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Implement drift reconciliation with explicit ownership boundaries. Changes outside the managed field allowlist must be reported but never overwritten.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A11

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Show a time-of-check/time-of-use failure where metadata changes after preflight. Add commit-time preconditions and demonstrate a safe conflict result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A12

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Build a deterministic incident report from sanitized plan,revision history and probe traces. Identify the first failed prerequisite without needing raw credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A13

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Migrate active configurations while old clients remain in service. Demonstrate a compatibility window and a precise condition for retiring v1.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A14

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Add a recovery procedure for a partially applied multi-resource plan. Record per-resource state and distinguish retryable,compensatable and unresolved operations.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-OPERATIONS-03-A15

**Core:** Validate desired resource config before deployment: environment in dev/test/prod,region from allowlist,owner and cost_center nonblank,public_access=false for prod. Return all errors sorted by path; perform no deployment.

**Acceptance example / fixture:** prod with public_access=true -> error public_access.

**Question:** Deliver validated configuration,resolution provenance,redaction tests,revision journal,activation recovery and a reproducible failure trace with no real deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
