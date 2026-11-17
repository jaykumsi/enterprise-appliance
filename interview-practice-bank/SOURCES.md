# Source material and technical references

Local source coverage is recorded per subtopic in `coverage.csv`. SQL Server records originate in `../SQL/Excerises/curriculum.json`;native Retail fixture definitions and rows are copied without executing them. Original files are retained. Existing source IDs are recorded on reused core records; new IDs distinguish the expanded interview requirement from the old core exercise.

The following primary references were checked while preparing runtime/model boundaries. They are references for instructors,not proof that every generated extension has a validated implementation.

- [CoderPad databases](https://coderpad.io/resources/docs/interview/databases/) and [PostgreSQL environment](https://coderpad.io/languages/postgresql/):native database setup.
- [AWS policy evaluation](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html):real authorization is more complex than the deliberately restricted local models.
- [Azure Data Factory copy activity](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-overview):copy activity context.
- [BigQuery introduction](https://docs.cloud.google.com/bigquery/docs/introduction):native analytics context.
- [Snowflake streams](https://docs.snowflake.com/en/user-guide/streams-intro):native change-consumption context.
- [Python data structures](https://docs.python.org/3/tutorial/datastructures.html):language reference.
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html):native relational reference.
- [Node.js event loop](https://nodejs.org/learn/asynchronous-work/event-loop-timers-and-nexttick):async execution context.
- [React state management](https://react.dev/learn/managing-state):frontend state context.
