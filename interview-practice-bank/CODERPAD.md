# Use the same bank in CoderPad

The exporter prepares Markdown handouts for manual use in CoderPad or another interview editor. It does not create CoderPad questions,upload a database or connect to an account.

1. Select exact IDs from [catalog.md](catalog.md) or `python tools.py list --subject python`.
2. Run `python tools.py export --ids ID1,ID2 --out exports/test.md`,or use the seeded `mock` command in [README.md](README.md).
3. Review the handout and run the selected tasks in the intended runtime. Keep independently checked expected results and grading notes private.
4. Create a pad with the needed language/dependencies. Preload a query fixture before the timer; omit solved CREATE/INSERT setup when those skills are assessed.
5. Paste the complete question,including its core,example and extension. Keep IDs unchanged and retain the adjacent manifest.
6. Grade core and extension with [the instructor rubric](instructor/ASSESSMENT.md). Save evidence against IDs.

## Runtime boundaries

CoderPad documents PostgreSQL database environments and custom database setup. Check the selected environment and account capabilities before administering a native database exercise. [CoderPad databases](https://coderpad.io/resources/docs/interview/databases/),[PostgreSQL environment](https://coderpad.io/languages/postgresql/).

T-SQL types such as hierarchyid,rowversion and geography,and Snowflake features such as VARIANT/QUALIFY/streams,need their native engine or an explicitly adapted exercise. The runtime label in each record is part of its contract. A code-only pad can assess a stated local state-machine model; it cannot establish that engine-specific SQL was executed correctly.

Cloud questions deliberately use local models with exact stated rules. A simplified IAM/RBAC evaluator is not a complete implementation of the real provider's authorization engine. Framework/UI questions need their dependencies and browser for native integration/accessibility checks; a pure model assesses only the relevant logic.

No complete hidden-test suite is bundled for the generated extensions. Prepare and execute independent tests for selected questions before using a timed assessment. Do not advertise them as automatically graded CoderPad tests until a native integration and expected-result suite have been added and verified.
