# Validation and practical limits

Run `python tools.py validate` to regenerate [validation.json](validation.json).

The validator checks unique IDs,exact15/15/15 level counts for every subtopic,nonempty contracts,distinct complete prompts within each subtopic,fixture availability,coverage consistency,all132 original SQL subtopics,local Markdown links and seeded mock determinism. Every saved handout is compared with its complete canonical render and bank hash;stale copies fail validation. It also checks a DDL export does not include its instructor reference answer.

Six independent result assertions execute against the portable fixture using SQLite:filtering,zero-preserving join,conditional counts,anti-join,deterministic ranking and keyset pagination. These validate the small shared fixture's acceptance examples; they are **not** PostgreSQL,SQL Server or Snowflake execution tests.

Questions use a subtopic-specific core with progressively different extensions. Related questions deliberately share scenarios and extension patterns;45 questions should not be read as45 unrelated business domains or45 independently verified reference implementations.

No native cloud deployment,SQL Server/PostgreSQL/Snowflake execution,browser accessibility verification or independent expert review of every generated extension has been performed. Complete solutions and hidden tests for new extensions are not bundled. Before administering any selected question,run it in its intended runtime and prepare independent expected outputs using the instructor guide. Existing legacy core answers do not establish correctness of new extensions.

Proposed coverage for empty/unavailable syllabuses is explicitly labelled. Azure's unavailable OneDrive file has not been read. Structural completeness is relative to the recorded source/proposed scope,not unknown lessons outside that scope.
