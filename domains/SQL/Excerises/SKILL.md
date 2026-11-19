---
name: sql-student-assignments
description: Create and update beginner-friendly SQL Server assignments with connected business tables, self-contained questions, per-domain instructor solutions, large practice data and domain-specific student handout folders. Use when continuing or adapting this training curriculum.
---

# SQL student assignments

Apply these agreed requirements when editing or extending the SQL training assignments. Later user instructions can change the scope or teaching level.

Last updated: 2026-11-16.

## Consolidation overrides

The user subsequently requested one retained copy of duplicate files. These instructions override the older requirements to retain shared topic books and to copy common guides into every standalone student folder.

- Publish assignments once in `domains/<company>/sql/questions/<TOPIC>.md` (folder per slug in `company_paths.py`);publish matching answers once in `solutions/<TOPIC>.md`. Answer pages link to questions instead of repeating their full text.
- Common beginner,interview and grading guides live once at the curriculum root. Domain folders may link to these shared guides;they are no longer completely independent copies.
- Mock files select canonical IDs and link to the original contracts. Generate full standalone handouts only when explicitly requested.
- Earlier unique healthcare and cross-subject SQL material is retained as clearly labelled supplements in the canonical Healthcare/Retail topic files. `consolidated_supplements.json` is a private regeneration input,not a second distributed workbook.
- The latest Healthcare/AmeriMed quality-selection request overrides publishing every historical healthcare record. `healthcare_exercise_review.py` selects applied cases and maps retired IDs to preferred live assessments; `HEALTHCARE_EXERCISE_REVIEW.json` records all480 decisions. Preserve the private source and all5,940 current levelled questions. AmeriMed's README links to the same canonical files rather than publishing another workbook. Historical tier letters are not current Advanced ratings.
- `consolidate_sql_materials.py` runs after levelled generation. `CONSOLIDATION_REPORT.json` records removed paths and retained destinations. Keep input datasets and build/validation metadata with distinct functions.
- NEVER enumerate or remove Git/other hidden metadata as part of assignment cleanup. Only explicitly mapped public handout paths are eligible;resolve every target inside the workspace. Remove empty directories individually rather than recursively deleting a computed directory.

## Current domain interview requirement

The user explicitly confirmed **15 Beginner,15 Intermediate and15 Advanced questions for every one of the132 existing subtopics in every domain**. The canonical SQL entry is `DOMAIN_ASSIGNMENTS.md`;each domain's `questions/README.md` links its levelled topic books. The earlier cross-subject draft under `interview-practice-bank` is not the canonical SQL assignment set.

- Preserve all original foundation IDs. New levelled IDs are domain-prefixed,for example `RETAIL-CTE-03-A06`.
- `domain_interview_generate.py` runs at the end of `build_curriculum.py` so regeneration retains the new question/solution sections and navigation.
- Levelled total:53,460 questions (5,940 per domain),including32,400 runnable relational-query references and21,060 practical labs with a core reference and case-specific grading model. These are reusable problem-pattern compositions,not53,460 unrelated algorithms.
- Query questions require an analysis audit plus the business report. Fixed A/B/C roles use the original category code,not a transformed text segment. Declare exact output columns,ordering,boundaries,tie rules and actual source columns.
- Advanced means concrete multi-stage SQL or practical migration/failure reasoning. Do not fill the quota with “profile the result,”generic test-writing,renamed constants or unsubstantiated benchmark requests.
- Keep matched solution files private. Practical lab extensions are instructor-reviewed demonstrations;do not call them fully executed automatic tests.
- `validate_domain_interview_native.py --full` executes runnable reports on the explicitly marked disposable LocalDB database and compares them with an independent Python oracle and adversarial populations. It refuses to reuse an unmarked existing database. No existing user database is reset or overwritten.
- `validate_domain_interviews.py` verifies the full counts,source-column validity,handout separation,canonical mock prompts and native source hashes. Reference logic changes invalidate native evidence and require rerunning affected native checks.
- `export_domain_interview.py` uses the exact canonical prompt for both practice and mock/CoderPad handouts. Exports contain input schemas/rows and never instructor answer SQL. No automatic CoderPad upload is implied.

## Project location and source

The existing project is `SQL/Excerises` under the Tinitaite Training workspace. Preserve the spelling `Excerises` in existing paths. If this file is attached in another chat, locate that project before modifying files; do not assume its files are attached with this skill.

The syllabus reference is https://github.com/tinitiateprime/sqlserver/blob/main/sqlserver-sql/README.md and its linked lessons. Consult it when changing syllabus coverage. Existing local curriculum files are the starting point for ordinary edits. The existing materials target SQL Server 2017 or later.

## Student question style

- Use simple, direct English and short tasks. Students should understand what to create or query without deciphering a long project brief.
- For CREATE TABLE questions, put the exact table name, every column name, data type, nullability, primary key, UNIQUE rule and default directly in the question. List exact CHECK expressions and foreign key targets alongside the column table.
- State which columns form a composite key together. Identify actual parent-table dependencies, including self-references, accurately. Do not imply that an unrelated earlier table is a dependency.
- Do not say only “use the columns and constraints in the guide.” The guide is supplementary; the question must include the required table definition.
- Query-topic questions (DQL, OPERATORS, JOINS, SET_OPERATIONS, STRING_FUNCTIONS, DATE_FUNCTIONS, AGGREGATES, ANALYTICAL_FUNCTIONS, CTE) must name the domain's real table and real column names, the exact output columns and the final ORDER BY. State tie-breakers for ranking (for example “Break ties by OrderID ascending”). End with a `Source columns:` list naming the columns the answer reads. Generic placeholders such as Category, Amount or PartyID must never appear in a student question; `domain_question_wording.py` maps them to each domain's columns.
- The question text must match the reference answer: if the answer partitions by `WorkflowStatus`, the question says WorkflowStatus, and the listed output columns match the answer's SELECT list.
- Avoid repetitive explanation, submission and validation paragraphs. Use numbered steps only when the task needs several actions. Preserve accurate SQL identifiers.
- Keep the actual connected business schema and existing question IDs. Simplify wording without silently changing data requirements or reducing topic coverage.
- No daily labels or daily deadlines. Topic order and assignment IDs are not dates.

Example question format:

Create `[retail].[Customers]` with these columns:

| Column | Data type | Constraints |
|---|---|---|
| CustomerID | int | PRIMARY KEY; NOT NULL |
| CustomerName | nvarchar(80) | NOT NULL |
| CustomerCode | varchar(20) | UNIQUE; NOT NULL |
| Region | varchar(10) | NOT NULL |

Add CHECK (`LEN(LTRIM(RTRIM(CustomerName))) > 0`) so the customer name cannot be blank.

Example query question:

Use ROW_NUMBER() over each RoutingCategory by decreasing EstimatedValue in `[brokerage].[TradeOrders]`. Break ties by OrderID ascending. Return OrderID, RoutingCategory, EstimatedValue and Position, in OrderID order. Source columns: `RoutingCategory`, `EstimatedValue`.

These examples illustrate the format; derive each actual question from its domain model.

## Concepts not yet taught

The user has not taught BEGIN TRANSACTION or ROLLBACK TRANSACTION.

- Do not require those commands, starting a transaction, rolling back, or transaction-based undo in student questions, beginner guides, domain guides or capstones.
- Remove dependent instructions such as checking that a dropped table has returned after rollback. Renumber remaining steps.
- Explain briefly that changes are kept when run. Use a practice database and ask the instructor to reset the original tables and sample rows between exercises that change them. DROP exercises need a separate practice copy.
- Do not assume the next exercise still has the original data after INSERT, UPDATE, DELETE or ALTER. Make the reset requirement clear without teaching transactions.
- Keep foreign key rules enabled unless changing a constraint is the explicit exercise.
- Instructor-only solutions and setup scripts may retain transaction handling. Do not copy those implementations into student handouts.
- Business uses of “transaction,” such as banking transaction rows, are valid and must not be removed by a blanket text replacement.

## Curriculum and domains

Each domain uses connected business tables (five per domain; E-commerce has six and Retail Supply Chain nine, as the user requested on 2026-11-18) with appropriate primary keys, foreign keys, UNIQUE, CHECK, NOT NULL and default rules. CREATE questions build those actual tables cumulatively. Subsequent data setup, constraints, DML, queries, joins, functions and reports use the same domain model and sample data.

Current domains:

- Retail: `retail`
- Banking / Finance: `banking`
- Pharma: `pharma`
- Healthcare: `healthcare`
- Oil: `oil`
- Retail Supply Chain: `retail_supply_chain` (Maple & Main Supply Chain; replaced Retail Inventory and Retail Manufacturing on 2026-11-18)
- Retail Logistics: `retail_logistics`
- E-commerce: `ecommerce` (Everyday Bazaar, a fictional high-volume marketplace; never use a real company name such as Amazon)
- Brokerage: `brokerage`

Domains with more than five tables keep five questions per subtopic: DDL Create and Data Setup split all tables into five dependency-ordered steps (`build_steps` in `domain_projects.py`), and per-table drills (Alter, Drop, DML, Constraints) use the model's five `focus` tables. Their large practice data comes from `large_data_extra.py` (E-commerce has about 32,000 orders).

Use neutral Brokerage naming and synthetic data without company branding. Brokerage orders are all Buy; RoutingCategory A=market, B=limit, C=scheduled.

Current baseline (recalculate if the scope changes; these are not a reason to add unrelated work):

- 16 topic books, 132 subtopics, five questions per domain per subtopic: 45 per subtopic, 5,940 topic questions.
- Six reporting assignments per domain (54).
- Five advanced queries per domain (45): monthly growth with missing months, gaps and islands / consecutive-date streaks, tie-aware ranking, trailing 30-day comparisons and relational division.
- Total 6,039 assignments, plus nine capstone checklists.
- Twelve extra SUBSTRING practice exercises per domain, with worked examples.
- Existing IDs 01–25 are preserved; newer-domain exercises use 26–45.

Current topic files: `DDL`, `DATA_SETUP`, `CONSTRAINTS`, `DML`, `DQL`, `OPERATORS`, `JOINS`, `SET_OPERATIONS`, `STRING_FUNCTIONS`, `DATE_FUNCTIONS`, `AGGREGATES`, `ANALYTICAL_FUNCTIONS`, `CTE`, `DATATYPES`, `DATABASE_SCHEMA_USER`, `INTRODUCTION`. Extra files: `REPORTING_ASSIGNMENTS`, `ADVANCED_QUERIES`, `SUBSTRING_PRACTICE`.

## Student handout folders

Every `domains/<company>/sql/questions/` folder must be independently shareable with students. Include:

- `README.md`: a short topic index with question counts, linking to the domain's files.
- One Markdown file per topic, containing only that domain's questions.
- `DOMAIN_GUIDE.md`: table details, relationships and sample rows.
- `BEGINNER_GUIDE.md`: simple prerequisite instructions and terms, without transaction steps.
- `REPORTING_ASSIGNMENTS.md`: that domain's six reporting questions.
- `ADVANCED_QUERIES.md`: that domain's five advanced queries.
- `SUBSTRING_PRACTICE.md`: the 12 extra SUBSTRING exercises with a one-based position guide.
- `PRACTICE_DATA.md`: large practice data row counts and loading instructions.

Keep all local links inside the student folder so copying that folder alone preserves navigation. Include no instructor solution files or links to answer keys. Do not require students to filter their domain's IDs out of a shared topic book. Domain-level navigation should point to its local questions.

Keep shared topic books available outside these handout folders. Preserve useful table guides, sample data, reports and competency checkpoints. Do not hand students the entire parent domain directory when it also contains instructor answers; share its `questions` folder.

## Instructor solution folders

Every `domains/<company>/sql/solutions/` folder mirrors its `questions` folder: same filenames and question IDs, including reporting, advanced queries and SUBSTRING practice. `solutions/README.md` links each student file to its solution file with answer counts.

Each answer shows the question, a reference answer (SQL or model explanation), expected results where fixed, and a short “Check and explain” teaching note for diagnosing common mistakes. Topic-level teaching notes live in `TEACHING_NOTES` in `instructor_solutions.py`. Fixed counts and totals assume the small original sample, not the large practice data; say so in the solution index.

The older shared `solutions/*_SOLUTIONS.md` books and the root `solutions/README.md` index remain for instructors.

## Large practice data

`large_data_setup.py` with `realistic_data.py` generates a larger fixture per domain: `domains/<company>/sql/DATA_SETUP.md`, `data_setup.sql` and the student `PRACTICE_DATA.md`. Each master table has at least 50 rows and each transaction/detail table at least 100. Data is deterministic, fictional and plausible (no real people, companies or market quotes), and is validated against the modeled constraints in SQLite. Use it in a separate practice database. It does not change the small `seed.sql` fixture that answer-key totals depend on. `LARGE_DATA_SETUP.md` lists row counts per domain.

## Maintaining generated materials

Generator layout:

- `domain_projects.py`: connected models, project briefs, reports, handout folders; calls `domain_question_wording.clarify_question`, `advanced_queries.generate` and `instructor_solutions.generate`.
- `build_curriculum.py`: technique books for every topic; calls `large_data_setup.generate`.
- `instructor_solutions.py`: per-domain solution folders; calls `substring_practice.generate`.
- `curriculum.json` holds generated question records; `domain_models.json` holds generated models; `advanced_queries.json` holds the advanced set.

Steps:

1. Inspect the relevant generator and existing files before editing. Update the generator so regeneration retains the requested improvements. Do not hand-edit generated Markdown only.
2. Update manually maintained guides or requirement notes (README, INSTRUCTOR_GUIDE, VALIDATION, this file) when the same change applies there.
3. Run `python build_curriculum.py` from the project folder, or invoke it by its full path.
4. Run the validators: `python validate_curriculum.py`, `python validate_question_wording.py` (question text vs schema and answers), `python validate_advanced_queries.py` (SQLite checks) and `.\validate_syntax.ps1 -ScriptDomPath <ScriptDom DLL>` (T-SQL grammar).
5. Check that every domain handout contains exactly its expected assignment IDs, all intended topics, six reports and five advanced queries. Check for missing or duplicate questions and other-domain content.
6. Verify relative Markdown links resolve inside each independently shareable student folder, and no answer files or transaction steps appear there. Exclude SQL code spans when parsing Markdown links.
7. Review representative CREATE, ALTER, DROP, DML, constraint and query questions for readable instructions, correct dependencies and wording that matches the reference answer.
8. Where possible, run representative answers on a real SQL Server (LocalDB `(localdb)\MSSQLLocalDB` is available on the user's machine) in a disposable database.
9. Report what changed and link the relevant student index. Distinguish file/content validation from SQL Server execution; never claim runtime testing unless it was performed.

## Carrying this into another chat

Attach this SKILL.md or ask the assistant to read its local path, then state the requested assignment change. This file records the reusable requirements; it does not itself install a globally discoverable skill or include the curriculum files.
