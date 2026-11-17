# SQL Server: nine connected domain projects

**Start here: [domain assignments and hard interview practice](domains/README.md).** Each domain now contains all132 subtopics with15 Beginner,15 Intermediate and15 Advanced questions per subtopic:5,940 levelled questions per domain,53,460 in total. The earlier foundation IDs below remain available.

The levelled query set includes32,400 runnable references;the21,060 schema/type/security/change cases use core references and explicit demonstration rubrics. Advanced problems include cycle-safe traversal,rolling medians,FIFO allocation,conserved rounding,cohort retention and five-table reconciliation. These are domain/subtopic-specific compositions of reusable patterns,not53,460 unrelated algorithms. See each domain's hard sampler and mock for the new standard.

Build a complete small database, then use the same tables throughout the assignments. **There are no day labels or daily deadlines.** Students progress when they can demonstrate the required skill.

**New to SQL? Read [Start here: simple SQL practice instructions](BEGINNER_GUIDE.md).** It explains sample rows, table names, NULL and constraints.

## Choose a domain

| Domain | Five related tables | Start here |
|---|---|---|
| Retail | Customers, Products, Orders, OrderItems, Payments | [Retail project](domains/retail/README.md) |
| Banking / Finance | Branches, Customers, Accounts, Transactions, Loans | [Banking project](domains/banking/README.md) |
| Pharma | Suppliers, Products, Warehouses, Batches, Inventory | [Pharma project](domains/pharma/README.md) |
| Healthcare | Patients, Doctors, Medications, Encounters, Prescriptions | [Healthcare project](domains/healthcare/README.md) |
| Oil | Sites, Carriers, Products, Shipments, ShipmentItems | [Oil project](domains/oil/README.md) |
| Retail Manufacturing | Products, Materials, ProductionOrders, BillOfMaterials, MaterialUsage | [Project brief](domains/retail_manufacturing/README.md) |
| Retail Logistics | Customers, Carriers, Shipments, ShipmentPackages, TrackingEvents | [Project brief](domains/retail_logistics/README.md) |
| Retail Inventory | Warehouses, Products, Suppliers, StockMovements, StockBalances | [Project brief](domains/retail_inventory/README.md) |
| Brokerage | Clients, Securities, BrokerageAccounts, TradeOrders, Executions | [Brokerage project](domains/brokerage/README.md) |

Each project includes a relationship diagram, column requirements, real PK/FK dependencies, UNIQUE/CHECK/NOT NULL/default rules, sample rows, assignment navigation, six business reports and a confidence checkpoint. Business identifiers are unique; people or company display names need not be.

## Student handouts

Each domain has a `questions` folder with all 16 topics, reporting questions, table details, sample rows and a beginner guide. Share that folder with students; start with its `README.md`. It contains no instructor solution files.

## Learning sequence

1. **Understand:** identify entities, primary keys, foreign keys and one-to-many relationships from the project brief.
2. **Build:** complete the five DDL CREATE assignments in the stated dependency order. These create permanent training tables, not disconnected #Work tables.
3. **Load:** insert the supplied sample data, parents before children. Keep the same tables and data for later topics.
4. **Protect:** demonstrate rejected duplicates, missing required values, broken CHECK rules and nonexistent parent references.
5. **Change:** practice INSERT, UPDATE, DELETE, ALTER and DROP in a practice database. Ask the instructor to reset the tables between exercises.
6. **Query:** work through filters, joins, grouping, functions, windows and CTEs on the domain tables.
7. **Integrate:** complete six domain reports, reconcile their totals and finish the capstone without copying an answer key.

The 16 topic books contain **5,940 exercises across 132 subtopics**, with 45 assignments per subtopic across nine domains. The **54 domain reports** and **45 advanced query exercises** bring the total to **6,039 assignments**, plus nine capstone checklists. Advanced exercises cover monthly growth with missing months, consecutive-date streaks, rankings with ties, trailing 30-day comparisons and relational division. Existing IDs 01–25 are preserved; new-domain exercises use 26–45. Topic books are grouped by domain; IDs identify exercises and are not a schedule.

## Topic books and separate answers

For a matching solution file for each domain question topic, open the [instructor solution index](solutions/README.md). Each domain’s `solutions` folder uses the same filenames and question IDs as its `questions` folder, including reporting and advanced queries. Answers include reference SQL or model explanations, validation guidance and teaching notes.

| Topic | Students | Instructors |
|---|---|---|
| Introduction | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Database, schema, user | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Data types | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| DDL: CREATE, ALTER, DROP | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Constraints | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| DML | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Data setup | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Queries | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Operators | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Set operations | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Joins | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| String functions | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Dates and time zones | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Aggregates | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Window functions | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| CTEs | [Questions](domains/README.md) | [Solutions](solutions/README.md) |
| Advanced queries | [Questions by domain](domains/README.md) | [Solutions by domain](solutions/README.md) |

Use [COVERAGE.md](COVERAGE.md) for subtopic IDs, [DATA_DICTIONARY.md](DATA_DICTIONARY.md) for conventions and [INSTRUCTOR_GUIDE.md](INSTRUCTOR_GUIDE.md) for assessment.

## Running the projects

Use SQL Server 2017+ in a **new disposable training database**. Do not run the revised setup over the old two-table-per-domain fixture.

- **Build-it-yourself path:** use the project brief and DDL Create questions; after all five tables exist, run that domain's `seed.sql` once or complete its Data Setup inserts. Do not do both.
- **Query-practice path:** an instructor runs [01_create_and_seed.sql](setup/01_create_and_seed.sql), which creates and seeds all 45 tables. Skip CREATE and seed exercises on this already-populated database.
- **Baseline check:** run [03_verify_fixture.sql](setup/03_verify_fixture.sql) before grading.
- **Deliberate reset:** [02_reset_fixture.sql](setup/02_reset_fixture.sql) drops the 45 project tables in reverse dependency order. Use only in the dedicated project database, then recreate and reseed.

**Adding only the four new domains to an existing five-table-project database:** run each new domain's `schema_solution.sql` and `seed.sql` once (or complete its CREATE/INSERT assignments). These use new schemas and preserve existing projects. Do not run the global reset to add a domain. The complete setup is for an empty project database.


DDL Create and initial seeding persist. Other project mutation exercises roll back changes so students can use the same baseline. Individual type/variable demonstrations may still use local temporary tables; those are syntax experiments, not the domain schema.

## Instructor files and maintenance

Keep `solutions/`, `*_SOLUTIONS.md`, `schema_solution.sql`, the generators and JSON answer manifests out of student distributions. Seed files contain data, not assignment answers. Each project reporting answer includes expected results and a capstone grading guide.

Regenerate and check from this directory:

```powershell
python .\build_curriculum.py
python .\validate_curriculum.py
.\validate_syntax.ps1 -ScriptDomPath 'C:\path\to\Microsoft.SqlServer.TransactSql.ScriptDom.dll'
```

`domain_projects.py` defines the connected models, project tasks and reports; `build_curriculum.py` generates the technique books and applies each domain's real column names. No network access is required to regenerate. [VALIDATION.md](VALIDATION.md) records checks and limitations. SQL Server runtime execution remains unverified.

The scope follows the [Tinitiate SQL Server syllabus](https://github.com/tinitiateprime/sqlserver/blob/main/sqlserver-sql/README.md), downloaded October 13, 2026. Curriculum requirements and maintenance steps are in [SKILL.md](SKILL.md). Upstream snapshots remain in `source/` with their original attribution.
