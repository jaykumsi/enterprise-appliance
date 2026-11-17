# How to practice for interviews

Start with your course in [the master index](catalog.md) and follow its [track sequence](TRACKS.md). Each subtopic contains **15 Beginner,15 Intermediate and 15 Advanced questions**. A question includes its core problem,acceptance example and extension; solve the complete question.

Beginner establishes correct behavior on small concrete cases. Intermediate combines it with boundaries,other components or failure handling. Advanced adds scale,concurrency,recovery or independent correctness evidence. Difficulty is relative to the subtopic: a beginner graph exercise still assumes basic programming.

Use a fresh practice namespace for changes to data or schema. Changes persist when you run them; ask your instructor to reset original tables/data between mutation exercises. Native SQL Server build questions need their stated objects created in dependency order. Do not preload solved CREATE/INSERT scripts when the question is assessing those skills.

## A useful practice attempt

1. Read the input/output contract aloud. State any open design choices and identify edge cases.
2. Work independently,without opening legacy answers or a completed earlier attempt.
3. Implement the core and the exact extension. Use injected clocks/providers for local-model cloud questions.
4. Run the acceptance example,an empty/boundary case and a case you derive independently. Preserve actual outputs.
5. Explain correctness,ordering,null/duplicate behavior and relevant complexity. State what your implementation does after failure.
6. Save `QUESTION_ID_yourname` with implementation,tests/output and a short explanation. Keep the ID unchanged.

The suggested time boxes are practice targets,not course deadlines. First reach correctness; then repeat unfamiliar questions under time limits. Native runtime setup and fixture loading happen before the timer.

## Evidence of readiness

Track progress in [progress.csv](progress.csv). A suggested progression gate is at least12/15 independently correct questions at a level,with at least8 solved under the suggested time and no unresolved critical correctness issue. Progress by subtopic rather than compensating for weak joins with strong string exercises.

After covering the track,complete two different timed mixed-topic mocks on separate attempts and score at least80/100 on each using the instructor rubric. Explain a failed case and repair it without copying a solution. If you memorized a question,request another ID or a new independently checked fixture.

These thresholds are training gates,not a guarantee of an interview outcome. Cloud tracks also need a native service lab; full stack tracks need an actual UI/API integration exercise. A mock local model cannot establish deployment competence or browser accessibility on its own.
