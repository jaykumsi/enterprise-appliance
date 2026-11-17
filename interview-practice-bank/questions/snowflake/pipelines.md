# Snowflake: Pipelines

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Streams and change consumption

### Beginner

#### SNOW-PIPELINES-01-B01

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B02

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B03

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B04

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B05

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B06

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B07

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B08

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B09

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B10

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B11

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B12

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B13

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B14

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-01-B15

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-PIPELINES-01-I01

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I02

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I03

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I04

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I05

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I06

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I07

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I08

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I09

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I10

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I11

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I12

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I13

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I14

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-01-I15

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-PIPELINES-01-A01

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A02

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A03

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A04

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A05

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A06

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A07

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A08

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A09

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A10

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A11

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A12

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A13

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A14

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-01-A15

**Core:** Model a change stream with durable offset. Batch reads do not advance the offset; only successful consumer commit does. Apply versioned events once by event_id and store consumer result and offset atomically.

**Acceptance example / fixture:** Read offset0,consumer fails -> offset0; replay and commit -> offset advances once.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Tasks and dependency graphs

### Beginner

#### SNOW-PIPELINES-02-B01

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B02

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B03

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B04

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B05

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B06

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B07

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B08

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B09

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B10

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B11

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B12

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B13

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B14

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-02-B15

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-PIPELINES-02-I01

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I02

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I03

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I04

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I05

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I06

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I07

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I08

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I09

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I10

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I11

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I12

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I13

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I14

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-02-I15

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-PIPELINES-02-A01

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A02

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A03

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A04

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A05

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A06

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A07

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A08

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A09

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A10

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A11

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A12

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A13

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A14

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-02-A15

**Core:** Schedule Validate->Merge->Publish. Failed validation blocks descendants; successful Merge publishes a commit ID consumed by Publish. Retry uses the same batch ID and cannot apply the merge twice.

**Acceptance example / fixture:** Merge commits then Publish retries -> one merge,two publish attempts at most under injected outcomes.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## MERGE and SCD history

### Beginner

#### SNOW-PIPELINES-03-B01

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B02

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B03

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B04

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B05

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B06

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B07

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B08

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B09

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B10

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B11

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B12

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B13

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B14

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-PIPELINES-03-B15

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-PIPELINES-03-I01

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I02

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I03

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I04

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I05

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I06

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I07

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I08

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I09

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I10

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I11

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I12

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I13

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I14

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-PIPELINES-03-I15

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-PIPELINES-03-A01

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A02

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A03

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A04

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A05

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A06

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A07

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A08

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A09

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A10

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A11

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A12

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A13

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A14

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-PIPELINES-03-A15

**Core:** Build per-key half-open validity history from effective times and changed attributes. Ignore repeated identical state; reject same-key same-time different state. Only one current row per key may have null end.

**Acceptance example / fixture:** a at1=X,at3=X,at5=Y -> [1,5)X,[5,null)Y.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
