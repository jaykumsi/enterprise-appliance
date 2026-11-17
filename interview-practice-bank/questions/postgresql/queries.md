# PostgreSQL: Queries

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: PostgreSQL; native database exercises need a PostgreSQL runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Filtering and null semantics

### Beginner

#### PG-QUERIES-01-B01

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B02

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B03

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B04

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B05

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B06

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B07

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B08

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B09

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B10

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B11

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B12

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B13

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B14

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-01-B15

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### PG-QUERIES-01-I01

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I02

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I03

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I04

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I05

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I06

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I07

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I08

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I09

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I10

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I11

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I12

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I13

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I14

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-01-I15

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### PG-QUERIES-01-A01

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A02

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A03

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A04

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A05

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A06

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A07

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A08

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A09

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A10

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A11

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A12

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A13

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A14

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-01-A15

**Core:** Using fixture Orders, return OrderID and AmountCents where AmountCents is at least 200 and Status is Open. Unknown amounts must not pass. Sort by OrderID.

**Acceptance example / fixture:** Baseline expected: [[3,200]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## Joins and cardinality

### Beginner

#### PG-QUERIES-02-B01

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B02

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B03

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B04

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B05

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B06

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B07

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B08

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B09

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B10

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B11

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B12

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B13

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B14

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-02-B15

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### PG-QUERIES-02-I01

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I02

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I03

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I04

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I05

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I06

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I07

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I08

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I09

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I10

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I11

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I12

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I13

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I14

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-02-I15

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### PG-QUERIES-02-A01

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A02

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A03

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A04

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A05

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A06

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A07

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A08

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A09

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A10

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A11

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A12

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A13

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A14

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-02-A15

**Core:** Using fixture Customers and Orders, return every customer ID and number of orders, including zero, sorted by customer ID. Count orders, not joined placeholder rows.

**Acceptance example / fixture:** Baseline expected: [[1,2],[2,2],[3,1],[4,0]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## Grouping and conditional aggregates

### Beginner

#### PG-QUERIES-03-B01

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B02

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B03

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B04

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B05

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B06

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B07

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B08

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B09

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B10

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B11

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B12

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B13

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B14

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-03-B15

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### PG-QUERIES-03-I01

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I02

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I03

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I04

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I05

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I06

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I07

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I08

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I09

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I10

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I11

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I12

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I13

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I14

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-03-I15

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### PG-QUERIES-03-A01

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A02

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A03

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A04

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A05

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A06

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A07

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A08

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A09

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A10

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A11

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A12

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A13

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A14

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-03-A15

**Core:** Using fixture Orders, return CustomerID, count of all orders and count of Open orders per customer present in Orders. Sort by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,2,1],[2,2,1],[3,1,1]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## Subqueries and anti joins

### Beginner

#### PG-QUERIES-04-B01

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B02

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B03

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B04

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B05

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B06

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B07

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B08

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B09

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B10

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B11

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B12

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B13

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B14

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-04-B15

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### PG-QUERIES-04-I01

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I02

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I03

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I04

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I05

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I06

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I07

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I08

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I09

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I10

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I11

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I12

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I13

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I14

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-04-I15

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### PG-QUERIES-04-A01

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A02

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A03

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A04

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A05

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A06

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A07

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A08

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A09

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A10

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A11

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A12

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A13

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A14

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-04-A15

**Core:** Return customers with no Open order from fixture Customers and Orders. Return CustomerID only, sorted ascending; duplicate orders must not duplicate customers.

**Acceptance example / fixture:** Baseline expected: [[4]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## Windows and deterministic ties

### Beginner

#### PG-QUERIES-05-B01

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B02

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B03

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B04

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B05

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B06

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B07

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B08

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B09

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B10

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B11

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B12

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B13

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B14

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

#### PG-QUERIES-05-B15

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `fixtures/portable.sql`. Suggested time: 15 minutes.

### Intermediate

#### PG-QUERIES-05-I01

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I02

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I03

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I04

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I05

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I06

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I07

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I08

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I09

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I10

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I11

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I12

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I13

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I14

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

#### PG-QUERIES-05-I15

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `fixtures/portable.sql`. Suggested time: 30 minutes.

### Advanced

#### PG-QUERIES-05-A01

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A02

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A03

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A04

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A05

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A06

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A07

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A08

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A09

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A10

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A11

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A12

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A13

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A14

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

#### PG-QUERIES-05-A15

**Core:** Return the highest known-amount order per customer from fixture Orders. Break amount ties by OrderID ascending. Return CustomerID and OrderID sorted by CustomerID.

**Acceptance example / fixture:** Baseline expected: [[1,1],[2,3],[3,5]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `fixtures/portable.sql`. Suggested time: 45 minutes.

## Recursive CTEs

### Beginner

#### PG-QUERIES-06-B01

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B02

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B03

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B04

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B05

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B06

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B07

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B08

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B09

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B10

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B11

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B12

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B13

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B14

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### PG-QUERIES-06-B15

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### PG-QUERIES-06-I01

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I02

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I03

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I04

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I05

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I06

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I07

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I08

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I09

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I10

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I11

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I12

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I13

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I14

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### PG-QUERIES-06-I15

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### PG-QUERIES-06-A01

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A02

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A03

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A04

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A05

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A06

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A07

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A08

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A09

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A10

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A11

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A12

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A13

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A14

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### PG-QUERIES-06-A15

**Core:** Using Nodes(id,parent_id) values (a,null),(b,a),(c,a),(d,b), return each node and its depth from root a, root depth zero. Sort by depth then id. Detect a repeated node on the path and return CYCLE rather than looping.

**Acceptance example / fixture:** Baseline: [[a,0],[b,1],[c,1],[d,2]].

**Question:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
