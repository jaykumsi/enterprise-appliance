# Validation status: connected-project revision

## Current domain interview set

The levelled assignments are in [domains/README.md](domains/README.md),not the earlier cross-subject draft. Every one of132 original subtopics has15 Beginner,15 Intermediate and15 Advanced questions in each of nine domains:53,460 levelled questions. Existing foundation IDs remain intact.

- **32,400 runnable query-report references** were executed on native SQL Server LocalDB and compared with an independent Python calculation of complete expected rows and values. All720 domain/subtopic analysis populations were executed natively.
- **1,320 adversarial result comparisons across30 populations** passed,including nulls,zeros,negative/mean-centered scores,same-day ties,30/31-day boundaries,leap/year boundaries,cycles with IDs1/11,missing parents,branched corrections,FIFO partial matches,exact fractional remainders and category-role/text-token separation.
- [Native execution evidence](DOMAIN_INTERVIEW_NATIVE_VALIDATION.json) records source hashes. Reference changes invalidate this evidence until rerun. [Complete expected small-fixture reports](DOMAIN_INTERVIEW_EXPECTED.json) back the instructor previews;large-fixture values differ.
- **21,060 practical lab cases** have a core reference and a case-specific model/rubric. Their open-ended migration,security,type and mutation demonstrations are instructor-reviewed;they are not claimed as fully executed or automatically graded solutions.
- `validate_domain_interviews.py` checks all1,188 domain/subtopic pairs,exact15/15/15 counts,ID matching,real source columns,student-folder links,answer separation and18 exact-prompt mock handouts. `validate_syntax.ps1` also reads the levelled reference bank and checks unique T-SQL statements with SQL Server2017 grammar.

The historical checks below concern the earlier foundation set. Their legacy-runtime limitation does not negate the native execution evidence for the new query set.

## Checks performed

- Verified 5,940 question/answer pairs across 132 subtopics and 16 topic books, with 45 exercises per subtopic and no numbered day labels.
- Verified nine connected domain graphs, exactly five tables each, a primary key on every table and 48 declared foreign-key relationships overall.
- Checked student/instructor ID pairing, unique prompts within each subtopic, all source datatype coverage and local links, including domain briefs.
- Parsed 5,565 SQL blocks with Microsoft's TSql140Parser (SQL Server 2017 grammar): all 5,490 SQL technique answers, 54 domain report answers, three global scripts and eighteen domain schema/seed scripts. [SYNTAX_VALIDATION.json](SYNTAX_VALIDATION.json) records the result and assembly version.
- Loaded the generated seed INSERT statements into 45 constrained in-memory SQLite tables. Checked all foreign-key references, primary-key uniqueness, required values and CHECK constraints during loading.
- Ran 2,052 portable technique queries plus all 54 domain reports. Checked independently specified results for aggregates, NULLs, outer joins, hierarchy traversal, reporting totals and duplicate-join prevention. Sixty-three selected technique queries with SQL Server-specific grammar were skipped.
- Attempted 138 independently constructed invalid writes covering duplicate primary keys, required NULL values and every FK relationship. Also extracted and executed the invalid mutation from each of the 225 constraint answers, including UNIQUE and CHECK cases. The constrained portable models rejected all of them. The exact counts are recorded in [PORTABLE_VALIDATION.json](PORTABLE_VALIDATION.json).

## Limits

**Full native execution of every legacy foundation and every open-ended lab remains unverified.** ScriptDom validates syntax rather than runtime binding,permissions or behavior. SQLite checks translate data types,literals and selected query syntax;they do not prove SQL Server transaction/error,collation,temporal,spatial or permission behavior. See the current-domain section for the new query references that were executed natively.

New independent report assertions cover manufacturing material variance, late deliveries and missing scans, inventory reconciliation/reorder cases.

Before classroom rollout, use a new SQL Server training database, run schema/seed setup and setup/03_verify_fixture.sql, then execute the constraint, ALTER/DROP and representative query answers. Schema-building students should start from the project specification instead of pre-running the complete setup. The old two-table-per-domain database is not compatible with the revised schema.

## Reproduce

```powershell
python .\build_curriculum.py
python .\validate_curriculum.py
.\validate_syntax.ps1 -ScriptDomPath 'C:\path\to\Microsoft.SqlServer.TransactSql.ScriptDom.dll'
```

The Python scripts use only the standard library. ScriptDom comes from the Microsoft.SqlServer.TransactSql.ScriptDom NuGet package; choose a DLL compatible with the PowerShell/.NET runtime. These checks do not connect to or modify any database server.
