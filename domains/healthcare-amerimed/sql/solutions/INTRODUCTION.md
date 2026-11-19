# Healthcare: INTRODUCTION — instructor solutions

[Instructor index](README.md) · [Student questions](../questions/INTRODUCTION.md)

## Teaching and troubleshooting

Ask the student to explain the concept using this domain’s tables and a concrete example. Accept equivalent explanations that address the stated risk and limitations.

Expected counts refer to the small original fixture. Run each answer independently; reset the fixture before independent mutation exercises. Equivalent SQL is acceptable when values, duplicates, NULL handling and required ordering agree.

### INTRODUCTION-01-04 — Relational database fundamentals

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of duplicate master details in every transaction, and proposes: separate the master entity and transaction entity and reference a stable master key. Relevant concepts: primary key, foreign key and one-to-many relationship.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-01-09 — Relational database fundamentals

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: separate the master entity and transaction entity and reference a stable master key. State the rule being enforced and what still requires application/operational validation. Discuss primary key, foreign key and one-to-many relationship.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-01-14 — Relational database fundamentals

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, separate the master entity and transaction entity and reference a stable master key. Discuss primary key, foreign key and one-to-many relationship; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-01-19 — Relational database fundamentals

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce duplicate master details in every transaction in a disposable environment, then apply the proposed control. Pass condition: a master name change is made once and all related facts still reference the same key. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-01-24 — Relational database fundamentals

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: duplicate master details in every transaction. Recommendation: separate the master entity and transaction entity and reference a stable master key. Success measure: a master name change is made once and all related facts still reference the same key. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include primary key, foreign key and one-to-many relationship in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-02-04 — Structured Data Storage and Control

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of negative quantities and untyped date strings entering the system, and proposes: use typed columns plus NOT NULL, CHECK and key constraints. Relevant concepts: schema validation and a rejected invalid insert.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-02-09 — Structured Data Storage and Control

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: use typed columns plus NOT NULL, CHECK and key constraints. State the rule being enforced and what still requires application/operational validation. Discuss schema validation and a rejected invalid insert.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-02-14 — Structured Data Storage and Control

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, use typed columns plus NOT NULL, CHECK and key constraints. Discuss schema validation and a rejected invalid insert; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-02-19 — Structured Data Storage and Control

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce negative quantities and untyped date strings entering the system in a disposable environment, then apply the proposed control. Pass condition: a negative quantity is rejected while zero is accepted if the business rule permits it. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-02-24 — Structured Data Storage and Control

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: negative quantities and untyped date strings entering the system. Recommendation: use typed columns plus NOT NULL, CHECK and key constraints. Success measure: a negative quantity is rejected while zero is accepted if the business rule permits it. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include schema validation and a rejected invalid insert in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-03-04 — Advanced Querying and Data Operations

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of operators editing all records because a WHERE predicate is missing, and proposes: preview the intended rows, apply a specific predicate and inspect affected rows inside a transaction. Relevant concepts: SELECT, INSERT, UPDATE and DELETE responsibilities.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-03-09 — Advanced Querying and Data Operations

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: preview the intended rows, apply a specific predicate and inspect affected rows inside a transaction. State the rule being enforced and what still requires application/operational validation. Discuss SELECT, INSERT, UPDATE and DELETE responsibilities.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-03-14 — Advanced Querying and Data Operations

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, preview the intended rows, apply a specific predicate and inspect affected rows inside a transaction. Discuss SELECT, INSERT, UPDATE and DELETE responsibilities; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-03-19 — Advanced Querying and Data Operations

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce operators editing all records because a WHERE predicate is missing in a disposable environment, then apply the proposed control. Pass condition: only the target rows change and a rollback restores the original values. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-03-24 — Advanced Querying and Data Operations

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: operators editing all records because a WHERE predicate is missing. Recommendation: preview the intended rows, apply a specific predicate and inspect affected rows inside a transaction. Success measure: only the target rows change and a rollback restores the original values. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include SELECT, INSERT, UPDATE and DELETE responsibilities in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-04-04 — Security and Regulatory Support

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of reporting users receiving modification rights, and proposes: grant a reporting role only required SELECT access; review grants, auditing and sensitive-data handling. Relevant concepts: least privilege, roles, auditing and a separate compliance review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-04-09 — Security and Regulatory Support

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: grant a reporting role only required SELECT access; review grants, auditing and sensitive-data handling. State the rule being enforced and what still requires application/operational validation. Discuss least privilege, roles, auditing and a separate compliance review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-04-14 — Security and Regulatory Support

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, grant a reporting role only required SELECT access; review grants, auditing and sensitive-data handling. Discuss least privilege, roles, auditing and a separate compliance review; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-04-19 — Security and Regulatory Support

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce reporting users receiving modification rights in a disposable environment, then apply the proposed control. Pass condition: the reader can query authorized objects and cannot modify them; this alone does not establish regulatory compliance. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-04-24 — Security and Regulatory Support

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: reporting users receiving modification rights. Recommendation: grant a reporting role only required SELECT access; review grants, auditing and sensitive-data handling. Success measure: the reader can query authorized objects and cannot modify them; this alone does not establish regulatory compliance. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include least privilege, roles, auditing and a separate compliance review in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-05-04 — Performance and Scalability

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of a growing report scanning far more rows than it returns, and proposes: inspect the actual plan and measured I/O before evaluating an index on selective filter/join columns. Relevant concepts: actual execution plan, logical reads, representative workload and write cost.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-05-09 — Performance and Scalability

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: inspect the actual plan and measured I/O before evaluating an index on selective filter/join columns. State the rule being enforced and what still requires application/operational validation. Discuss actual execution plan, logical reads, representative workload and write cost.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-05-14 — Performance and Scalability

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, inspect the actual plan and measured I/O before evaluating an index on selective filter/join columns. Discuss actual execution plan, logical reads, representative workload and write cost; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-05-19 — Performance and Scalability

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce a growing report scanning far more rows than it returns in a disposable environment, then apply the proposed control. Pass condition: compare elapsed time and logical reads before and after, with identical results and acceptable write overhead. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-05-24 — Performance and Scalability

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: a growing report scanning far more rows than it returns. Recommendation: inspect the actual plan and measured I/O before evaluating an index on selective filter/join columns. Success measure: compare elapsed time and logical reads before and after, with identical results and acceptable write overhead. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include actual execution plan, logical reads, representative workload and write cost in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-06-04 — Analytics and Business Intelligence

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of a dashboard double-counting master records after joining to details, and proposes: define the metric grain, aggregate detail at the required grain and reconcile totals. Relevant concepts: grain, dimensions, measures and aggregate reconciliation.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-06-09 — Analytics and Business Intelligence

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: define the metric grain, aggregate detail at the required grain and reconcile totals. State the rule being enforced and what still requires application/operational validation. Discuss grain, dimensions, measures and aggregate reconciliation.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-06-14 — Analytics and Business Intelligence

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, define the metric grain, aggregate detail at the required grain and reconcile totals. Discuss grain, dimensions, measures and aggregate reconciliation; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-06-19 — Analytics and Business Intelligence

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce a dashboard double-counting master records after joining to details in a disposable environment, then apply the proposed control. Pass condition: the dashboard total equals an independent detail-level control total. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-06-24 — Analytics and Business Intelligence

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: a dashboard double-counting master records after joining to details. Recommendation: define the metric grain, aggregate detail at the required grain and reconcile totals. Success measure: the dashboard total equals an independent detail-level control total. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include grain, dimensions, measures and aggregate reconciliation in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-07-04 — Transactional Workloads

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of a multi-step business operation succeeding only halfway, and proposes: enclose the related writes in one transaction with rollback on failure. Relevant concepts: atomicity, consistency, isolation and durability.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-07-09 — Transactional Workloads

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: enclose the related writes in one transaction with rollback on failure. State the rule being enforced and what still requires application/operational validation. Discuss atomicity, consistency, isolation and durability.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-07-14 — Transactional Workloads

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, enclose the related writes in one transaction with rollback on failure. Discuss atomicity, consistency, isolation and durability; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-07-19 — Transactional Workloads

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce a multi-step business operation succeeding only halfway in a disposable environment, then apply the proposed control. Pass condition: an injected failure leaves neither a partial debit/charge nor its unmatched counterpart. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-07-24 — Transactional Workloads

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: a multi-step business operation succeeding only halfway. Recommendation: enclose the related writes in one transaction with rollback on failure. Success measure: an injected failure leaves neither a partial debit/charge nor its unmatched counterpart. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include atomicity, consistency, isolation and durability in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-08-04 — Data Warehousing and BI

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of daily reporting conflicting with live operational processing, and proposes: define a separate reporting model and load schedule, recording source cutoffs and reconciliation totals. Relevant concepts: fact grain, dimensions, refresh latency and reconciliation.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-08-09 — Data Warehousing and BI

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: define a separate reporting model and load schedule, recording source cutoffs and reconciliation totals. State the rule being enforced and what still requires application/operational validation. Discuss fact grain, dimensions, refresh latency and reconciliation.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-08-14 — Data Warehousing and BI

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, define a separate reporting model and load schedule, recording source cutoffs and reconciliation totals. Discuss fact grain, dimensions, refresh latency and reconciliation; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-08-19 — Data Warehousing and BI

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce daily reporting conflicting with live operational processing in a disposable environment, then apply the proposed control. Pass condition: a repeated load does not duplicate facts and a published report states its data cutoff. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-08-24 — Data Warehousing and BI

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: daily reporting conflicting with live operational processing. Recommendation: define a separate reporting model and load schedule, recording source cutoffs and reconciliation totals. Success measure: a repeated load does not duplicate facts and a published report states its data cutoff. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include fact grain, dimensions, refresh latency and reconciliation in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-09-04 — Digital Content Management

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of unversioned document metadata overwriting earlier editorial changes, and proposes: store content metadata with a stable key and version/concurrency token; define where large content bytes live. Relevant concepts: metadata schema, content location and concurrency check.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-09-09 — Digital Content Management

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: store content metadata with a stable key and version/concurrency token; define where large content bytes live. State the rule being enforced and what still requires application/operational validation. Discuss metadata schema, content location and concurrency check.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-09-14 — Digital Content Management

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, store content metadata with a stable key and version/concurrency token; define where large content bytes live. Discuss metadata schema, content location and concurrency check; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-09-19 — Digital Content Management

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce unversioned document metadata overwriting earlier editorial changes in a disposable environment, then apply the proposed control. Pass condition: an update using a stale version is rejected rather than overwriting a newer edit. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-09-24 — Digital Content Management

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: unversioned document metadata overwriting earlier editorial changes. Recommendation: store content metadata with a stable key and version/concurrency token; define where large content bytes live. Success measure: an update using a stale version is rejected rather than overwriting a newer edit. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include metadata schema, content location and concurrency check in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-10-04 — Enterprise Applications

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

A strong answer uses Encounters and Patients as its example, explains the risk of separate application modules maintaining inconsistent master IDs, and proposes: share governed master keys, enforce references and define module-specific schema permissions. Relevant concepts: master-data ownership, foreign keys and application role boundaries.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-10-09 — Enterprise Applications

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Construct a concrete pair of related Encounters and Patients records and a failure case. Response: share governed master keys, enforce references and define module-specific schema permissions. State the rule being enforced and what still requires application/operational validation. Discuss master-data ownership, foreign keys and application role boundaries.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-10-14 — Enterprise Applications

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Application validation can improve feedback, but every write/read path must respect the same business contract. For this case, share governed master keys, enforce references and define module-specific schema permissions. Discuss master-data ownership, foreign keys and application role boundaries; do not claim a feature alone solves all operational concerns.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-10-19 — Enterprise Applications

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Setup: create a small valid Encounters and Patients baseline. Action: deliberately reproduce separate application modules maintaining inconsistent master IDs in a disposable environment, then apply the proposed control. Pass condition: both modules resolve the same master ID and an unknown reference is rejected. Preserve before/after evidence.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

### INTRODUCTION-10-24 — Enterprise Applications

**Question**

[Canonical questions](../questions/INTRODUCTION.md)

**Reference answer**

Risk: separate application modules maintaining inconsistent master IDs. Recommendation: share governed master keys, enforce references and define module-specific schema permissions. Success measure: both modules resolve the same master ID and an unknown reference is rejected. Ask the owner to confirm the workload, rule boundaries and responsibility for failures. Include master-data ownership, foreign keys and application role boundaries in the review.

**Check and explain:** Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

<!-- DOMAIN_LEVELLED_INTERVIEW_START -->

## Levelled interview answers

Keep answers private. For query tasks,grade both analysis audit and report. Expected small-fixture rows are stored in `DOMAIN_INTERVIEW_EXPECTED.json`;large-data outputs differ. For practical labs,the reference core alone does not solve the new case:require the listed case-specific evidence and rubric.

### Relational database fundamentals: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-01-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-01-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-01-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-01-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-01-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-01-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Structured Data Storage and Control: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-02-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-02-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-02-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-02-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-02-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-02-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Advanced Querying and Data Operations: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-03-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-03-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-03-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-03-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-03-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-03-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Security and Regulatory Support: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-04-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-04-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-04-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-04-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-04-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-04-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Performance and Scalability: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-05-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-05-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-05-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-05-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-05-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-05-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Analytics and Business Intelligence: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-06-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-06-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-06-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-06-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-06-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-06-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Transactional Workloads: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-07-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-07-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-07-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-07-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-07-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-07-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Data Warehousing and BI: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-08-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-08-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-08-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-08-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-08-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-08-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Digital Content Management: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-09-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-09-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-09-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-09-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-09-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-09-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

### Enterprise Applications: progression

**Beginner:15 questions**

#### HEALTHCARE-INTRODUCTION-10-B01

**Valid baseline**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b01)

**Assessment model:** The baseline satisfies every stated column/type/key rule;the observed result matches the core reference. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B02

**Missing input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b02)

**Assessment model:** Required and optional are distinguished from metadata;unsupported optionality is rejected,not invented. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B03

**Exact boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b03)

**Assessment model:** The chosen boundary is documented by the actual type/object contract and a native observable result. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B04

**Two independent rows**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b04)

**Assessment model:** Different business keys/variables do not share unintended state;all requested outcomes are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B05

**Duplicate proposal**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b05)

**Assessment model:** Behavior follows actual key/object/construct semantics;repeat does not automatically mean idempotency. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B06

**Metadata evidence**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b06)

**Assessment model:** Metadata agrees with the object/value actually created and distinguishes runtime values from object definitions. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B07

**Unknown versus zero**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b07)

**Assessment model:** Null,zero and absence are not conflated;no invented persistent representation is claimed for CURSOR/ROWVERSION. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B08

**Wrong type input**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b08)

**Assessment model:** The result is established by native execution;implicit conversion is not assumed lossless. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B09

**Dependency order**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b09)

**Assessment model:** Only actual PK/FK,scope or object dependencies are asserted;an unrelated earlier lesson is not a prerequisite. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B10

**Rejected request preserves state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b10)

**Assessment model:** Rejected state is absent;independent earlier valid work is not falsely reported as undone. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B11

**Deterministic presentation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b11)

**Assessment model:** Final ordering is explicit;native types and required values are retained rather than flattened to misleading text. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B12

**Least sufficient permission**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b12)

**Assessment model:** The scope of the grant is explicit;permission on a similarly named object does not count. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B13

**Name and scope collision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b13)

**Assessment model:** Display labels are not assumed unique;qualification and stable keys determine identity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B14

**Empty state**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b14)

**Assessment model:** Empty is handled according to the construct;no fabricated row or successful mutation is reported. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-B15

**Independent acceptance check**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-b15)

**Assessment model:** The assertion does not merely rerun the implementation predicate;the seeded defect produces a visible failure. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Intermediate:15 questions**

#### HEALTHCARE-INTRODUCTION-10-I01

**Batch with mixed validity**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i01)

**Assessment model:** Every input has one disposition;invalid requests never become default-valued successes;changes persist and instructor resets between attempts. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I02

**Lossless round trip**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i02)

**Assessment model:** The chosen second representation is explicit;byte length alone is not proof of semantic equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I03

**All conflicting keys**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i03)

**Assessment model:** Conflicts are identified with actual comparison semantics,including trailing spaces/case where applicable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I04

**Drift before change**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i04)

**Assessment model:** Preflight checks actual state and runs before writes;it does not blindly recreate the object. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I05

**Application bypass**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i05)

**Assessment model:** Every write path is considered;an application-only check is not mistaken for database integrity. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I06

**Partial input correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i06)

**Assessment model:** Corrections are explicit and targeted;good state is unchanged and bad state is traceable. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I07

**Idempotency decision**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i07)

**Assessment model:** Business identity is distinct from row display name;the journal cannot claim an unexecuted action succeeded. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I08

**Reference membership**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i08)

**Assessment model:** Real dependencies are checked in their correct direction;unsupported references are explicitly rejected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I09

**Schema version precondition**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i09)

**Assessment model:** The accepted plan names the version it validated;stale assumptions cannot overwrite a newer definition. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I10

**Before-image restoration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i10)

**Assessment model:** Before images contain keys and exact values/definitions;restore order respects real dependencies. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I11

**Representation-aware reconciliation**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i11)

**Assessment model:** A matching count/checksum/grand total is not accepted as a proof of equality. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I12

**Safe dynamic identifier**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i12)

**Assessment model:** Identifiers and values are handled separately;raw interpolation is not accepted as parameterization. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I13

**Precision and aggregate boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i13)

**Assessment model:** Intermediate and final types are both considered;unsupported operations are rejected instead of coerced. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I14

**Two independent implementations**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i14)

**Assessment model:** Both strategies enforce the same contract and expose disagreements as concrete counterexamples. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-I15

**Auditable decision table**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-i15)

**Assessment model:** Expected outcomes are declared before execution;the interaction changes a real decision and is not just another constant. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

**Advanced:15 questions**

#### HEALTHCARE-INTRODUCTION-10-A01

**Zero-loss representation migration**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a01)

**Assessment model:** A lossless representation/explicit rejection policy exists;old consumers are supported until the declared cutover;no silent rounding/truncation/key loss. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A02

**Conflicting concurrent actors**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a02)

**Assessment model:** There is an observable race and a guarded resolution;checking only before computation is insufficient. Do not invent transaction syntax in student prerequisites. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A03

**Crash after accepted effect**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a03)

**Assessment model:** Accepted effects are not duplicated;unknown remains distinct from failed;replay payload conflict is detected. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A04

**Dependency graph rebuild**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a04)

**Assessment model:** Actual keys/types/scopes are preserved;deferred data loading or staged nullable links are justified without permanently disabling constraints. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A05

**Collation and canonicalization trap**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a05)

**Assessment model:** All colliding originals are reported;canonicalization is not allowed to silently discard one;where the native type has no collation,use an applicable representation collision instead. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A06

**Intermediate overflow or precision loss**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a06)

**Assessment model:** Casting only the final result is not accepted when overflow/loss occurs earlier;the proof includes the actual problematic intermediate step. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A07

**Restartable chunked repair**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a07)

**Assessment model:** Chunk boundaries and action identities are durable;the plan does not use unstable offset paging over changing data. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A08

**Stale authorization at execution**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a08)

**Assessment model:** The proof distinguishes missing identity,stale policy and wrong object scope;an earlier allow is not sufficient. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A09

**Mixed-version import with tombstones**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a09)

**Assessment model:** Tombstone/version metadata is retained;null data is not used as an ambiguous delete marker;conflicts are visible. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A10

**Atomic publication boundary**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a10)

**Assessment model:** Prepared and published states are distinct;readers cannot observe a mix;post-publication response failure is reconciled by version. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A11

**Type or scope spoofing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a11)

**Assessment model:** Logical identity and actual native representation are checked;sanitizing display text alone is not accepted. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-04` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A12

**Nonunique history correction**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a12)

**Assessment model:** There is no arbitrary TOP1/DISTINCT survivor;history boundaries and conflict lineage remain explicit. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-09` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A13

**Owner failure and fencing**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a13)

**Assessment model:** Lease expiry alone is insufficient;the actual write checks the token and returns a visible stale-owner conflict. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-14` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A14

**Independent corruption detector**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a14)

**Assessment model:** The scanner is not a copy of the mutation predicate;all applicable seeded defects are detected and unsupported states are explicitly identified. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-19` in this topic's earlier foundation answers. Also require the case-specific evidence above.

#### HEALTHCARE-INTRODUCTION-10-A15

**Adversarial native case study**

[Canonical question](../questions/INTRODUCTION.md#healthcare-introduction-10-a15)

**Assessment model:** All three hazards interact in a concrete case;correctness evidence,not vague recommendations or a benchmark request,is required. Core checkpoint: Grade the domain example, technical accuracy, explicit limitations and observable validation; accept equivalent justified designs.

**Core reference:** Find `INTRODUCTION-10-24` in this topic's earlier foundation answers. Also require the case-specific evidence above.

<!-- CONSOLIDATED_UNIQUE_MATERIAL -->

## Selected AmeriMed applied answer key

Historical references require instructor review on the large fixture. These are not newly validated levelled references. [Selection audit](EXERCISE_SELECTION.md).

##### INTRODUCTION-I05: Logical query processing order

[Question](../questions/INTRODUCTION.md)

```sql
SELECT EncounterID, Charge * 2 AS DoubleCharge
FROM healthcare.Encounters
WHERE Charge * 2 > 400        -- the alias DoubleCharge is not visible here
ORDER BY DoubleCharge DESC;  -- but it is visible here
```

**How it works:** FROM → ON → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → TOP/OFFSET. Aliases are created in SELECT, so only ORDER BY (which comes after) can use them.

**Expected result:** 57 rows, first 6 shown

| EncounterID | DoubleCharge |
|---|---|
| 124 | 500 |
| 171 | 500 |
| 180 | 500 |
| 204 | 500 |
| 86 | 496 |
| 77 | 494 |

##### INTRODUCTION-I06: Clustered vs nonclustered index

[Question](../questions/INTRODUCTION.md)

```sql
SELECT i.name, i.type_desc, i.is_primary_key, i.is_unique
FROM sys.indexes AS i
WHERE i.object_id = OBJECT_ID('healthcare.Encounters')
  AND i.type > 0;
```

**How it works:** A clustered index sorts and stores the table's rows by its key; there can be only one (here, the primary key). A nonclustered index is a separate sorted structure that points back to the rows; a table can have many. The UNIQUE constraint created one.

**Expected result:** 2 rows

| name | type_desc | is_primary_key | is_unique |
|---|---|---|---|
| PK\_Encounters | CLUSTERED | 1 | 1 |
| UQ\_Encounters\_1 | NONCLUSTERED | 0 | 1 |

##### INTRODUCTION-A01: Execution plan basics

[Question](../questions/INTRODUCTION.md)

```sql
SET SHOWPLAN_TEXT ON;
GO
SELECT EncounterID, EncounterDate FROM healthcare.Encounters WHERE PatientID = 1;
GO
SET SHOWPLAN_TEXT OFF;
```

**How it works:** The optimizer turns SQL into a plan of physical operators (scan, seek, join type). Here there is no index on PatientID, so it scans the clustered index. An index on PatientID would turn it into a seek. In SSMS, press Ctrl+L to see the graphical plan.

**Expected result:** run it in your own practice database; this statement changes server-level settings, so it was not run here.
