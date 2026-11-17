# Python mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## PY-COLLECTIONS-02-B12 — Dictionaries and sets

Python / Collections / Beginner

Runtime: Python; language-level code with injected I/O where needed. Suggested time: 15 minutes.

**Core problem**

Implement count_pairs(values,target) returning count of index pairs i<j summing to target. Duplicate values at distinct positions count separately.

**Acceptance example / baseline**

[1,1,2,2],3 -> 4.

**Interview requirement**

Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## PY-ALGORITHMS-02-I05 — Two pointers and sliding windows

Python / Algorithms / Intermediate

Runtime: Python; language-level code with injected I/O where needed. Suggested time: 30 minutes.

**Core problem**

Return longest substring length with at most k distinct Unicode code points,k>=0.

**Acceptance example / baseline**

eceba,k2 ->3.

**Interview requirement**

Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## PY-FUNDAMENTALS-01-A13 — Numeric types and conversion

Python / Fundamentals / Advanced

Runtime: Python; language-level code with injected I/O where needed. Suggested time: 45 minutes.

**Core problem**

Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / baseline**

([2,3,-1],-4,4) -> 1.

**Interview requirement**

Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
