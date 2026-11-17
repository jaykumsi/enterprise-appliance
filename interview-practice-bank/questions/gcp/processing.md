# GCP Data Engineering: Processing

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Dataflow event-time windows

### Beginner

#### GCP-PROCESSING-01-B01

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B02

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B03

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B04

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B05

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B06

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B07

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B08

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B09

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B10

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B11

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B12

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B13

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B14

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-01-B15

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-PROCESSING-01-I01

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I02

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I03

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I04

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I05

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I06

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I07

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I08

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I09

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I10

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I11

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I12

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I13

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I14

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-01-I15

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-PROCESSING-01-A01

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A02

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A03

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A04

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A05

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A06

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A07

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A08

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A09

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A10

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A11

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A12

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A13

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A14

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-01-A15

**Core:** Assign events to fixed half-open 10-second windows by integer event_time. At watermark W accept only events with window_end+allowed_lateness>W; sum signed cents per window and route rejected events to late output.

**Acceptance example / fixture:** time9 -> [0,10); time10 -> [10,20); end10,lateness5,W15 -> late.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Dataproc Spark transformations

### Beginner

#### GCP-PROCESSING-02-B01

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B02

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B03

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B04

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B05

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B06

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B07

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B08

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B09

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B10

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B11

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B12

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B13

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B14

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-PROCESSING-02-B15

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-PROCESSING-02-I01

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I02

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I03

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I04

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I05

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I06

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I07

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I08

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I09

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I10

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I11

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I12

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I13

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I14

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-PROCESSING-02-I15

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-PROCESSING-02-A01

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A02

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A03

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A04

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A05

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A06

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A07

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A08

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A09

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A10

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A11

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A12

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A13

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A14

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-PROCESSING-02-A15

**Core:** Using PySpark, enrich orders with one latest dimension row per customer by version. Retain unknown customers and conserve sum of known cents. Show row counts before/after and prevent a many-version dimension join from duplicating facts.

**Acceptance example / fixture:** One 100-cent order with two dimension versions -> one 100-cent enriched row.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
