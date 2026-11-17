# SUBQUERIES

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Retained earlier SQL draft exercises

Unique earlier draft contracts are consolidated here rather than kept in a second SQL bank. They supplement the15/15/15 levelled set;their new extensions were not supplied with complete validated solutions. Use the domain guide for table requirements.

##### SQL-SUBQUERIES-01-B01

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B02

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B03

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B04

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B05

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B06

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B07

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B08

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B09

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B10

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B11

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B12

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B13

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B14

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-B15

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I01

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I02

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I03

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I04

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I05

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I06

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I07

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I08

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I09

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I10

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I11

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I12

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I13

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I14

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-I15

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A01

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A02

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A03

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A04

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A05

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A06

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A07

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A08

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A09

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A10

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A11

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A12

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A13

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A14

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-01-A15

Using retail.Orders,return OrderID,OrderTotal for orders whose known total exceeds the average known total across all orders. Sort by OrderID. Null totals cannot pass.

**Extension:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B01

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B02

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B03

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B04

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B05

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B06

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B07

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B08

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B09

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B10

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B11

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B12

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B13

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B14

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-B15

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I01

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I02

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I03

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I04

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I05

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I06

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I07

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I08

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I09

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I10

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I11

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I12

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I13

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I14

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-I15

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A01

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A02

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A03

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A04

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A05

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A06

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A07

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A08

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A09

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A10

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A11

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A12

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A13

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A14

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-02-A15

Using retail.Orders,return OrderID,CustomerID,OrderTotal for orders whose known total exceeds that customer's average known total. Sort by OrderID; retain ties only if they strictly exceed the average.

**Extension:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B01

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Implement the core query and give its complete baseline result, including duplicate rows and null values. Use the output ordering specified by the core.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B02

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Treat the core result as R. Return a single row ResultRows containing its row count; demonstrate why counting a nullable result column is different.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B03

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Return the core result with a one-based OutputPosition in its specified order. If the core has no total order, add all output columns as tie breakers, null first; identical rows may be indistinguishable.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B04

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Produce a compact profile of R: total rows and number of distinct complete rows. Treat nulls as equal for this distinct-row count.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B05

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Produce one row per output column containing its name, total rows and null count. Include columns even when R is empty.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B06

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Return R as distinct complete rows, preserving the core sort order where possible and then all output columns as tie breakers. State which baseline duplicates were removed.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B07

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Return a tagged result with RowKind=DATA on every row and one SUMMARY row containing total row count in a separate count field. Do not replace null data with summary values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B08

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Write a second query that verifies the baseline result's cardinality without selecting all data rows. Return expected_count,actual_count,pass.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B09

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Materialize R in a scratch relation and query it back with the same columns, nulls, duplicates and ordering. Show that materialization does not itself preserve order.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B10

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Serialize R to a JSON array, retaining null fields and the specified row order. Do not convert numbers into quoted strings merely to format them.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B11

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Produce R and a separate empty-result flag. The flag must be true only when R has zero rows, not when its values are all null.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B12

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Implement the core with named query stages and return a row count per stage. Explain any expansion or reduction using actual fixture rows.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B13

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Return R together with a schema description listing output names and logical types. Demonstrate how the empty result keeps the same schema.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B14

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Create a check query that identifies complete duplicate rows in R and their multiplicities. Return only multiplicities greater than one.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-B15

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Write a baseline regression assertion that compares R to an explicitly written expected table from the fixture, including nulls and multiplicity. Return mismatching rows rather than only a yes/no answer.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I01

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Add a customer-scoped variant. For sources containing CustomerID, evaluate the core separately for each CustomerID; keep that key in the result. For other sources, use the first nonnumeric source key stated in the core. Show why computing globally then filtering may differ.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I02

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Run the core on each half of the input split by ascending source primary-key position, then on the union of both halves. Return the three result counts and demonstrate whether concatenating partial results equals the global result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I03

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I04

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Build a parameterized wrapper around the core with start position and page size over its deterministic output order. Return one page and total rows; reject nonpositive page size. Document how indistinguishable duplicate rows are handled.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I05

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Create a reconciliation report comparing two materialized copies of R: one has its first row removed and another duplicates its last row. Return complete-row expected/actual multiplicities and classify missing versus excess occurrences.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I06

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Materialize R with a unique synthetic output-row identifier. Demonstrate why a source key may not be unique after a join and do not silently discard rows to satisfy the new key.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I07

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Add a typed parameter interface for every literal filter in the core. Return INVALID before executing if a parameter cannot be represented in the declared type; preserve the original default behavior.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I08

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Create a view for the core's relational logic and a consumer query for final ordering. Prove the consumer returns the baseline result; do not rely on ordering inside a view.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I09

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Create two fixture copies: original and one with the first non-key nullable column set to null on every row. Run both and report changed output rows with null-safe comparison.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I10

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Produce a complete-row frequency table for R, then reconstruct R from those frequencies. Verify the reconstructed multiset equals R even when repeated rows contain nulls.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I11

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Create a diagnostic version exposing source-row identifiers alongside each result row or group. For aggregated rows return contributor IDs in ascending order without changing computed values.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I12

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Parameterize the core to run against a temporary fixture with the same schema. Prove it reads no rows from the original fixture by giving the copy disjoint primary keys.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I13

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Add input-quality checks for duplicate primary keys, missing required source values and orphan foreign keys before running the core. Return all violations instead of allowing a misleading result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I14

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** For every aggregate in the core, or a wrapper COUNT if there is none, reconcile totals back to source contributors. Demonstrate that a one-to-many join does not accidentally count a source amount twice.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-I15

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Implement a result-contract validator checking exact column names, compatible types, required ordering and multiplicities. Show one deliberately malformed candidate result that fails each applicable check.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A01

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Design an incremental equivalent of the core for inserted source rows. If the operation cannot be incrementally maintained with only the existing result, identify and implement the additional state needed. Reconcile with full recomputation.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A02

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Extend incremental maintenance to updates and deletes, retaining enough lineage to reverse prior contributions. Show a source correction that changes an earlier output, then reconcile the entire result.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A03

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Run the core over a reproducible large fixture and inspect the actual execution plan. Supply an optimization that preserves the full multiset and report measured evidence; do not invent elapsed times.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A04

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Provide a snapshot-consistent way to compute R and its row count while another session inserts data. Demonstrate the anomaly in an unsafe version and the selected engine's corrected behavior.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A05

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Implement keyset pagination where the core exposes a stable unique key; otherwise materialize an immutable snapshot with row IDs. Show that inserting a source row between pages cannot duplicate or skip rows in the chosen contract.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A06

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Build a differential checker comparing two implementations over generated small fixtures. Include nulls,ties,empty sources and one-to-many relationships; print a minimal counterexample on disagreement.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A07

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Perform a schema migration adding an optional source attribute while preserving the published output contract. Show compatibility checks that detect a column reorder or unexpected SELECT-star expansion.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A08

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Implement restartable result publication: write R under a run ID, validate it, then atomically switch a current-result pointer. A failure before publication must leave the previous result readable.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A09

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Show a counterexample to the claim that matching row counts and grand totals prove equal results. Write SQL that detects your discrepancy using complete-row multiplicities.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A10

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Handle a skewed source where one grouping/join key owns 90 percent of rows. Preserve null and duplicate semantics, examine the plan and propose a measured mitigation without changing business results.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A11

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Translate the core to a second declared SQL dialect. List semantic differences that affect this fixture, and compare normalized results. Unsupported engine-specific types require an explicit alternate representation and a separate native check.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A12

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Implement a deterministic historical comparison between two source snapshots. Return inserted,removed and changed result rows using a declared stable key; if no such key exists, use complete-row multiplicity deltas.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A13

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Give an adversarial source fixture that breaks a plausible shortcut to the core, such as DISTINCT after a bad join or NOT IN with null. Implement the corrected query and show both actual results.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A14

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Place an explicit resource budget on the core using actual source cardinality and width. Choose indexes/materialization or staged processing, then supply a correctness comparison and an experiment for the proposed budget.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.

##### SQL-SUBQUERIES-03-A15

Using retail.Customers,retail.Orders and retail.OrderItems,return customer IDs who ordered every ProductID in required products {1,2}. Multiple purchases do not change eligibility; an empty required set makes every customer eligible. Sort by CustomerID.

**Extension:** Deliver an integrated query review: runnable SQL,independent expected-result checks,deterministic ordering,empty/null/tie cases and actual plan evidence. Introduce one regression and demonstrate that the checks catch it.

**Acceptance example:** Use the canonical small Retail fixture (instructor setup: schema_solution.sql and seed.sql). For an empty required-product set,all five fixture customers qualify.
