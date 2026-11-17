# Course sequences and shared prerequisites

One canonical question ID appears in one subject bank. Tracks can reuse those IDs; reuse does not increase the total question count.

| Training track | Practice sequence |
|---|---|
| SQL Server | Introduction;database/schema/user;types;DDL;constraints;data setup;DML;DQL;operators;joins;sets;aggregates;strings;dates;subqueries;windows;CTEs |
| Python | Fundamentals;collections;strings;algorithms;reliability;design;concurrency;testing |
| PostgreSQL | Shared relational concepts from SQL Server without T-SQL-specific syntax,then PostgreSQL queries;types;integrity;performance;programming;security |
| Java full stack | Java language;collections;design;shared Web/Frontend;Java concurrency;backend;testing;delivery;integrated UI/API lab |
| Node.js full stack | JavaScript;async;shared Web/Frontend;Node backend;testing;delivery;integrated UI/API lab |
| AWS DE | Python + relational SQL prerequisites;shared formats/ETL;AWS foundations;identity;networking;storage;databases;compute;orchestration;analytics;messaging;observability;native service lab |
| Azure DE | Python + relational SQL;shared formats/ETL/Spark;Azure identity;storage;ingestion;orchestration;compute;analytics;streaming;governance;operations;native service lab |
| GCP DE | Python + relational SQL;shared formats/ETL/Spark;GCP identity;storage;analytics;compute;messaging;processing;orchestration;operations;native service lab |
| Snowflake | Relational SQL;shared formats/ETL;Snowflake security;compute;loading;queries;pipelines;recovery;performance;native warehouse lab |

AWS syllabus headings PySpark,PostgreSQL,Airflow,AppFlow,LocalStack and data formats map to the shared Data Engineering/PostgreSQL banks. Python and SQL prerequisites map to their canonical banks. IAM Users/Roles/Groups,S3 Tables and Zero ETL have separate coverage. Student onboarding is an administrative activity and is not counted as an interview subtopic.

## Source boundaries

- SQL Server retains all132 source subtopics and adds three explicit subquery subtopics. The nine original domain repetitions are consolidated around the Retail fixture; domain names are not treated as separate skills. Existing healthcare materials remain supplementary domain practice.
- SQL Server logical introduction/security cores replace definition-only prompts. New IDs are namespaced and preserve legacy source mappings where an original core is reused.
- Python,PostgreSQL,Java,Node.js and shared frontend coverage is proposed because their folders contain no readable lesson files.
- Azure coverage is proposed because its syllabus file is an unavailable OneDrive placeholder. It has not been silently assumed to match the original syllabus.
- GCP and Snowflake Terraform files establish infrastructure context,not a complete curriculum; additional coverage is proposed.
- Cloud simulation contracts state a limited model explicitly. Real platform behavior needs a native follow-up; proposed coverage should be reconciled with the instructor's full syllabus when available.

The bank is a consolidated practice set,not an assertion that unreadable or absent syllabuses were recovered.
