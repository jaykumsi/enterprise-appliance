# Instructor guide

## Domain interview progression

Use [the domain assignment index](domains/README.md). Every domain retains all132 subtopics and has15 Beginner,15 Intermediate and15 Advanced questions per subtopic. Topic files retain earlier foundation IDs and append the new domain-prefixed IDs. The shared technique books below are the earlier foundations,not the new levelled count.

Each domain has a hard sampler,a120-minute hard mock and a105-minute mixed mock. They reuse canonical practice IDs and exact prompts. Select different underlying challenge patterns and supply an independently checked adversarial fixture so memorizing a pattern does not count as transfer of reasoning.

Match every new student ID in that domain's solutions folder. Grade both the analysis audit and business report for query tasks. For schema/type/security/DML labs,require the concrete implementation and observed evidence against the case-specific rubric;these extensions are not claimed as fully automated native tests. The native report identifies the scope of query execution and independent comparisons.

Regenerate with `python build_curriculum.py`. Run `python validate_domain_interviews.py`;after changing reference logic,run `python validate_domain_interview_native.py --full` in the explicitly owned disposable LocalDB database and regenerate the handouts to refresh expected-result previews. `export_domain_interview.py` prepares exact-ID handouts with complete input schemas and baseline rows.

Students choose one domain and build five connected tables before doing isolated syntax practice. Teach relationships and data integrity first; progress by evidence, not a daily label. [README.md](README.md) links all projects and topic books.

## Teaching sequence and checkpoints

| Stage | Required evidence |
|---|---|
| Model | Student explains all five entities, keys, mandatory/optional references and one-to-many relationships |
| CREATE | All five tables exist in dependency order, with correct columns, PKs, trusted FKs, UNIQUE/CHECK/default/NOT NULL rules |
| Seed | Counts and sample values match; all child references resolve |
| Constraints | Duplicate PK, duplicate business key, missing required value, invalid CHECK and invalid FK are each rejected |
| DML | INSERT/UPDATE/DELETE affect only intended rows;instructor restores original samples between independent cases |
| ALTER/DROP | Student identifies dependencies, demonstrates changes and restores the schema |
| Reporting | All six business reports reconcile, including missing activity and repeated-detail cases |
| Advanced queries | Complete the15 Advanced questions per assigned subtopic;use the hard sampler for cycle-safe traversal,FIFO allocation,rolling medians,exact proportional allocation,cohort retention and five-table reconciliation. Earlier five-query IDs remain as bridge practice |
| Capstone | Student rebuilds independently, explains results, and fixes a deliberately incorrect join |

Do not count completion of copied SQL as confidence. Ask the student to predict results, explain a failure and adapt the solution to a new valid record. Passing requires all integrity tests and reports to reconcile. A student who cannot explain why an aggregate doubled after a join should revisit grain and pre-aggregation.

## Assessment

Use ten points per task: four for correct schema/result, two for keys/NULLs/duplicates/boundaries, two for correct method and rollback discipline, two for an explanation with reproducible evidence. Accept equivalent correct SQL. Compare complete values and duplicate counts; row count alone is insufficient. For written tasks, grade technical accuracy, domain example, limitations and an observable test.

Each domain brief links assignment IDs for all topics. The topic books are grouped by domain, with no calendar labels. The 5,940 technique exercises retain the syllabus coverage across nine domains; 54 additional reports, 45 advanced query exercises and nine capstones integrate the connected models. Original assignment IDs remain stable. Instructor solutions are separate from student questions. [Advanced solution index](solutions/README.md).

## Lab execution

Start in a fresh SQL Server 2017+ database. The previous two-table fixture is incompatible with this revision. Use a new database instead of layering the new schema over it.

For schema practice, students execute DDL CREATE one table at a time and then use either the domain seed.sql or its Data Setup INSERT tasks. For query-only sessions, use setup/01_create_and_seed.sql. Never seed twice. Foreign keys use NO ACTION and are checked; never disable constraints to load bad data.

Project INSERT/UPDATE/DELETE, ALTER/DROP and constraint demonstrations wrap changes in a transaction and ROLLBACK. Use a fresh session with no ambient transaction. Expected constraint failures are caught with XACT_ABORT OFF so the demonstration can inspect the unchanged row and roll back. If interrupted, inspect @@TRANCOUNT and roll back the lab transaction before continuing.

DROP exercises intentionally remove incoming FKs inside a transaction before dropping the target table, then roll back to restore both schema and data. CREATE exercises persist because later tables depend on them. Individual data-type examples may use #Work; the domain schema does not.

Database creation and principal-management lessons need instructor-authorized permissions. WITHOUT LOGIN users require no passwords or instance configuration change. Run SQL blocks individually; variable names may repeat across blocks. GO in the database-creation example is a client batch delimiter.

## SQL accuracy notes

DECIMAL(5,2) ranges from -999.99 to 999.99; NUMERIC is its fixed-precision synonym. DATEPART weekday depends on DATEFIRST, explicitly set to 1 in these exercises. DATEDIFF counts boundaries rather than completed ages. DATETIMEOFFSET stores an offset rather than a named time zone; named-zone conversions use event-date rules. TEXT is legacy and finite; ROWVERSION is not clock time. LAST_VALUE needs the requested window frame, and RANK/DENSE_RANK should not break ties with a unique ID when equal business values must share a rank.

## Validation

Run python validate_curriculum.py for book integrity, connected-model checks, constrained portable-data checks and domain reports. validate_syntax.ps1 checks Microsoft T-SQL grammar. setup/03_verify_fixture.sql checks baseline counts, amount totals, orphan references and trusted FK state on an actual SQL Server. [VALIDATION.md](VALIDATION.md) states the completed checks and the outstanding SQL Server runtime limit.

## Additional project checkpoints

Manufacturing students must reconcile recipe requirements with actual consumption. Logistics students must distinguish scan counts, package counts and shipment-level charges. Inventory students must reconcile signed movements to opening and closing balances using the full warehouse/product key. A successful FK test alone does not enforce aggregate limits such as inventory snapshot reconciliation.

To add the new domains without rebuilding existing projects, use their individual schema_solution.sql and seed.sql files in the existing training database. All four use separate new schemas. The global setup/reset/check scripts cover all nine domains; the full baseline check expects all nine to be installed.

Brokerage students must reconcile requested and executed quantities, identify overfills, and calculate quantity-weighted prices. Executed notional is not account cash, profit or portfolio value.
