# Shared Data Engineering Tools mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## DE-FORMATS-03-B06 — Parquet and columnar planning

Shared Data Engineering Tools / Formats / Beginner

Runtime: Python reference model; PySpark/Parquet/Airflow native checks need their respective runtimes. Suggested time: 15 minutes.

**Core problem**

Given file metadata with path,row_count,min_date,max_date,columns, choose files for a projection of id,cents and inclusive-start/exclusive-end date interval. Metadata ranges are inclusive. Unknown statistics must not cause a file to be excluded. Return paths sorted.

**Acceptance example / baseline**

Query [Jan 2,Jan 3), file max Jan 1 -> skip; unknown bounds -> include.

**Interview requirement**

Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## DE-ETL-02-I03 — Incremental loads and watermarks

Shared Data Engineering Tools / ETL / Intermediate

Runtime: Python reference model; PySpark/Parquet/Airflow native checks need their respective runtimes. Suggested time: 30 minutes.

**Core problem**

Given last committed (updated_at,id) cursor, select rows lexicographically greater than it through a captured upper cursor inclusive. Advance watermark only after sink commit. Return selected IDs sorted by cursor.

**Acceptance example / baseline**

Last (10,a), upper (11,b), rows (10,b),(11,b),(12,c) -> first two.

**Interview requirement**

Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## DE-FORMATS-01-A07 — CSV quoting and validation

Shared Data Engineering Tools / Formats / Advanced

Runtime: Python reference model; PySpark/Parquet/Airflow native checks need their respective runtimes. Suggested time: 45 minutes.

**Core problem**

Parse CSV with header id,cents; support quoted commas and escaped quotes. Preserve ID text, require signed integer cents, and return accepted records plus rejected logical record numbers. Do not split lines on commas manually.

**Acceptance example / baseline**

Quoted ID "a,b",12 -> id a,b and cents 12.

**Interview requirement**

Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
