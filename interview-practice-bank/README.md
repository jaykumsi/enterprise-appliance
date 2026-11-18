# Interview practice and assessment bank

**SQL location update:** The canonical SQL assignments are now in [SQL/Excerises/domains](../domains/SQL/Excerises/domains/README.md),with all132 subtopics and15 questions per level in each domain. Use those domain folders for SQL classes and tests;the SQL entries in this earlier cross-subject draft remain supplementary.

This is the entry point for the consolidated question bank for all training subjects. Beginner, Intermediate and Advanced each contain 15 questions **per subtopic**. Practice and interview exports read the same question records and retain the same IDs.

Run `python build_bank.py` in this directory to build the topic books,coverage index and machine-readable bank,then `python tools.py samples` to refresh example tests and `python tools.py validate` to check them. Read `STUDENT_GUIDE.md` for practice and `instructor/ASSESSMENT.md` for interview selection and grading.

Original course files remain available as source material. This directory is the canonical entry point for the new practice bank; older question sets are supplementary and are not added to its counts. New IDs deliberately differ from legacy IDs. `coverage.csv` records the source of each subtopic, including proposed coverage where no readable syllabus exists.

Questions are scenario-based exercises: implement, query, trace, repair, or demonstrate a decision with concrete evidence. The three levels increase the reasoning required, rather than changing only names or input values. Each question pairs a subtopic-specific core problem with an extension; both are required. Programming skills use fifteen distinct authored cores where mapped in `problem_variants.py`;SQL typically rotates five existing cores,and service/framework skills retain a focused core with different engineering extensions. Related questions share scenarios and extension patterns. Do not count a core as a separate question.

The cloud exercises use explicit local models and supplied mock inputs. They assess the logic behind engineering work without requiring a cloud account. They do not replace a service deployment lab. Native SQL Server, Snowflake and framework exercises need an appropriate runtime or a manually assessed code pad; see `CODERPAD.md`.

## Generated files

- `questions/<subject>/<topic>.md`: student questions grouped by subtopic and level.
- `catalog.md` and `coverage.csv`: coverage, counts and provenance.
- `bank.json`: all student questions, metadata and core contracts.
- `instructor/legacy_core_references.json`: existing SQL reference answers for the core only; extensions require independent grading.
- `progress.csv`: one row per subtopic and level for student tracking.
- `VALIDATION.md`: checks performed and remaining runtime/content checks.
- [Sample interview handouts](exports/README.md): one mixed mock for every subject/shared track,plus Python examples.

## Export a question or a test

```powershell
python tools.py list --subject python
python tools.py export --ids PY-FUNDAMENTALS-01-B01 --out exports/python-question.md
python tools.py mock --subject python --level Intermediate --seed 21 --out exports/python-mock.md
python tools.py mock --subject python --level Mixed --seed 22 --out exports/python-mixed.md
python tools.py validate
```

Exported handouts include the core contract, fixture and exact extension. Test selection is deterministic for a supplied seed, samples different subtopics and records the selected IDs. Review and run a selected test in its intended runtime before administering it. No material has been uploaded to CoderPad.
