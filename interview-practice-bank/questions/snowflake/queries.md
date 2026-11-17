# Snowflake: Queries

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## QUALIFY and window ranking

### Beginner

#### SNOW-QUERIES-01-B01

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B02

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B03

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B04

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B05

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B06

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B07

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B08

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B09

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B10

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B11

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B12

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B13

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B14

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### SNOW-QUERIES-01-B15

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-QUERIES-01-I01

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I02

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I03

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I04

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I05

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I06

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I07

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I08

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I09

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I10

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I11

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I12

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I13

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I14

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### SNOW-QUERIES-01-I15

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### SNOW-QUERIES-01-A01

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A02

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A03

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A04

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A05

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A06

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A07

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A08

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A09

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A10

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A11

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A12

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A13

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A14

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### SNOW-QUERIES-01-A15

**Core:** Using fixture Orders, select top known-amount order per customer, amount descending with OrderID ascending for ties. Return CustomerID,OrderID sorted by CustomerID; use a window and QUALIFY in Snowflake.

**Acceptance example / fixture:** Baseline [[1,1],[2,3],[3,5]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## VARIANT and FLATTEN

### Beginner

#### SNOW-QUERIES-02-B01

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B02

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B03

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B04

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B05

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B06

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B07

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B08

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B09

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B10

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B11

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B12

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B13

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B14

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-02-B15

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-QUERIES-02-I01

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I02

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I03

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I04

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I05

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I06

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I07

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I08

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I09

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I10

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I11

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I12

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I13

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I14

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-02-I15

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-QUERIES-02-A01

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A02

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A03

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A04

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A05

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A06

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A07

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A08

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A09

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A10

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A11

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A12

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A13

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A14

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-02-A15

**Core:** Given Payloads(id,body VARIANT) with id1 items[A qty2,B qty3],id2 items[], flatten valid item objects to id,sku,qty in array-index order. Reject noninteger/nonpositive qty into an errors result.

**Acceptance example / fixture:** Valid baseline [[1,A,2],[1,B,3]],no errors.

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Date and timestamp semantics

### Beginner

#### SNOW-QUERIES-03-B01

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B02

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B03

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B04

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B05

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B06

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B07

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B08

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B09

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B10

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B11

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B12

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B13

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B14

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-QUERIES-03-B15

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-QUERIES-03-I01

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I02

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I03

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I04

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I05

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I06

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I07

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I08

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I09

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I10

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I11

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I12

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I13

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I14

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-QUERIES-03-I15

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-QUERIES-03-A01

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A02

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A03

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A04

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A05

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A06

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A07

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A08

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A09

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A10

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A11

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A12

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A13

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A14

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-QUERIES-03-A15

**Core:** Given two UTC instants 2024-01-01T00:30Z and 2024-01-01T05:30Z, calculate America/New_York local dates using explicit time-zone conversion. Supply input type declarations so session time zone cannot change results.

**Acceptance example / fixture:** First -> 2023-12-31; second -> 2024-01-01.

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
