# Azure Data Engineering: Ingestion

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Data Factory copy and reconciliation

### Beginner

#### AZ-INGESTION-01-B01

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B02

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B03

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B04

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B05

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B06

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B07

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B08

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B09

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B10

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B11

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B12

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B13

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B14

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-01-B15

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-INGESTION-01-I01

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I02

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I03

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I04

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I05

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I06

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I07

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I08

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I09

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I10

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I11

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I12

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I13

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I14

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-01-I15

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-INGESTION-01-A01

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A02

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A03

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A04

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A05

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A06

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A07

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A08

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A09

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A10

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A11

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A12

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A13

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A14

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-01-A15

**Core:** Given source manifest {id,version,checksum} and copied sink rows, report missing,stale,extra and conflicting IDs sorted. Commit the batch only if every source row matches its sink row and no unexpected sink IDs exist.

**Acceptance example / fixture:** Same row count with different IDs -> fail reconciliation.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## ADF incremental watermarking

### Beginner

#### AZ-INGESTION-02-B01

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B02

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B03

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B04

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B05

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B06

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B07

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B08

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B09

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B10

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B11

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B12

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B13

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B14

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-INGESTION-02-B15

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-INGESTION-02-I01

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I02

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I03

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I04

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I05

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I06

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I07

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I08

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I09

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I10

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I11

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I12

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I13

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I14

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-INGESTION-02-I15

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-INGESTION-02-A01

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A02

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A03

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A04

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A05

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A06

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A07

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A08

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A09

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A10

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A11

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A12

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A13

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A14

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-INGESTION-02-A15

**Core:** Select rows after committed (modified_at,id) through captured upper cursor inclusive. Do not update watermark if copy/validation/commit fails. Return selected IDs and proposed watermark separately from committed watermark.

**Acceptance example / fixture:** Cursor (10,a),rows (10,b),(11,a),upper(10,z) -> select (10,b) only.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
