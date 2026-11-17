# Full Stack Developer - Java mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## JAVA-COLLECTIONS-01-B12 — Lists and comparators

Full Stack Developer - Java / Collections / Beginner

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model. Suggested time: 15 minutes.

**Core problem**

Implement deduplicate_sorted(values) returning unique ascending integers plus original multiplicities,without mutating input.

**Acceptance example / baseline**

[1,1,2,2,2] -> values[1,2],counts[2,3].

**Interview requirement**

Create a table-driven acceptance runner that prints each input,expected,actual and pass. Include the supplied example and at least two independently derived valid cases.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## JAVA-DESIGN-02-I05 — Interfaces and dependency injection

Full Stack Developer - Java / Design / Intermediate

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model. Suggested time: 30 minutes.

**Core problem**

Implement Checkout with injected PriceRepository and PaymentGateway interfaces. Calculate exact integer cents from SKU quantities; reject unknown SKU and nonpositive quantity before charging. A failed charge must not return a success receipt.

**Acceptance example / baseline**

A price 200,qty 2 -> one charge for 400; unknown SKU -> zero charges.

**Interview requirement**

Write property-based checks for three invariants derived from this core's contract. Generate small inputs and print a concrete counterexample if an invariant fails.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## JAVA-LANGUAGE-01-A13 — Primitives and exact arithmetic

Full Stack Developer - Java / Language / Advanced

Runtime: Java; Spring/JPA tasks need configured dependencies or a framework-free service-boundary model. Suggested time: 45 minutes.

**Core problem**

Implement largest_safe_prefix(values,min,max). Return the first zero-based index whose running sum leaves inclusive bounds,or null. All inputs are signed integers.

**Acceptance example / baseline**

([2,3,-1],-4,4) -> 1.

**Interview requirement**

Implement backpressure between a request producer and slow output consumer. Bound in-flight requests,retain output order and show no unbounded buffer growth under a deterministic slow-sink test.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
