# Python intermediate mock - seed 21

These questions use the same IDs,core contracts and extensions as the practice bank.

## PY-COLLECTIONS-03-I11 — Comprehensions and grouping

Python / Collections / Intermediate

Runtime: Python; language-level code with injected I/O where needed. Suggested time: 30 minutes.

**Core problem**

Implement totals_by_customer(rows),summing signed integer cents per customer,keeping zero totals and sorting by customer.

**Acceptance example / baseline**

a:+5,a:-5,b:+3 -> a:0,b:3.

**Interview requirement**

Create an input normalizer that applies only transformations explicitly allowed by the core; reject all other attempted repairs. Return original and normalized inputs for audit without changing valid semantics.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## PY-FUNDAMENTALS-03-I05 — Functions and scope

Python / Fundamentals / Intermediate

Runtime: Python; language-level code with injected I/O where needed. Suggested time: 30 minutes.

**Core problem**

Implement map_with_index(values,fn),calling fn(value,index) once per value and returning new results. Indices start0.

**Acceptance example / baseline**

[a,b],concatenate value/index -> [a0,b1].

**Interview requirement**

Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## PY-STRINGS-02-I08 — Regular expressions

Python / Strings / Intermediate

Runtime: Python; language-level code with injected I/O where needed. Suggested time: 30 minutes.

**Core problem**

Replace standalone ASCII secret assignments token=VALUE with token=[REDACTED],where VALUE is nonempty nonwhitespace text. Do not redact mytoken= text.

**Acceptance example / baseline**

"token=abc mytoken=def" -> "token=[REDACTED] mytoken=def".

**Interview requirement**

Implement a versioned JSON interface with v1 wrapping the original core contract. Unsupported versions fail before processing; add v2 with an explicit metadata envelope while preserving v1 behavior.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
