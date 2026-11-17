# AWS Data Engineering: Analytics

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Athena scan planning

### Beginner

#### AWS-ANALYTICS-01-B01

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B02

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B03

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B04

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B05

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B06

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B07

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B08

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B09

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B10

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B11

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B12

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B13

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B14

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-ANALYTICS-01-B15

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-ANALYTICS-01-I01

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I02

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I03

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I04

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I05

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I06

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I07

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I08

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I09

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I10

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I11

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I12

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I13

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I14

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-ANALYTICS-01-I15

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-ANALYTICS-01-A01

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A02

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A03

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A04

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A05

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A06

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A07

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A08

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A09

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A10

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A11

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A12

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A13

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A14

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-ANALYTICS-01-A15

**Core:** Given Files(path,partition_day,bytes) values (a,2024-01-01,100),(b,2024-01-02,200),(c,2024-01-03,300), write a query selecting files in [Jan2,Jan3) and calculate bytes scanned in this simplified whole-file model. Do not use live prices.

**Acceptance example / fixture:** Selected [b],model scan 200 bytes.

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
