# GCP Data Engineering: Analytics

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## BigQuery partition pruning

### Beginner

#### GCP-ANALYTICS-01-B01

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B02

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B03

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B04

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B05

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B06

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B07

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B08

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B09

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B10

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B11

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B12

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B13

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B14

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-01-B15

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-ANALYTICS-01-I01

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I02

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I03

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I04

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I05

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I06

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I07

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I08

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I09

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I10

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I11

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I12

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I13

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I14

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-01-I15

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-ANALYTICS-01-A01

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A02

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A03

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A04

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A05

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A06

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A07

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A08

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A09

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A10

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A11

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A12

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A13

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A14

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-01-A15

**Core:** Given Files(path,partition_day,bytes) (a,Jan1,100),(b,Jan2,200),(c,Jan3,300), select partition days in [Jan2,Jan3) and sum selected bytes under a supplied whole-file scan model. Write SQL and expected IDs.

**Acceptance example / fixture:** [b],200 bytes; do not infer real bill from this toy model.

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## BigQuery nested repeated records

### Beginner

#### GCP-ANALYTICS-02-B01

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B02

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B03

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B04

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B05

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B06

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B07

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B08

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B09

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B10

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B11

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B12

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B13

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B14

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-02-B15

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-ANALYTICS-02-I01

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I02

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I03

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I04

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I05

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I06

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I07

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I08

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I09

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I10

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I11

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I12

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I13

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I14

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-02-I15

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-ANALYTICS-02-A01

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A02

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A03

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A04

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A05

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A06

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A07

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A08

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A09

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A10

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A11

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A12

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A13

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A14

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-02-A15

**Core:** Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / fixture:** [[o1,A,2],[o1,B,1]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## BigQuery deduplication and merge

### Beginner

#### GCP-ANALYTICS-03-B01

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B02

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B03

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B04

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B05

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B06

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B07

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B08

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B09

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B10

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B11

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B12

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B13

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B14

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-ANALYTICS-03-B15

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-ANALYTICS-03-I01

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I02

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I03

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I04

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I05

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I06

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I07

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I08

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I09

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I10

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I11

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I12

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I13

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I14

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-ANALYTICS-03-I15

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-ANALYTICS-03-A01

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A02

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A03

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A04

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A05

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A06

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A07

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A08

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A09

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A10

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A11

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A12

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A13

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A14

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-ANALYTICS-03-A15

**Core:** Choose latest row per business ID by version then ingest_id. Equal version and differing payload is CONFLICT rather than arbitrary selection. Merge only validated winners; repeated committed batch ID has no effect.

**Acceptance example / fixture:** a:v1/x,a:v2/y -> a:v2/y.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
