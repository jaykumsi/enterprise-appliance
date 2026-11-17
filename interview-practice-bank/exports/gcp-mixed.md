# GCP Data Engineering mixed mock - seed 22

These questions use the same IDs,core contracts and extensions as the practice bank.

## GCP-STORAGE-01-B06 — Cloud Storage object prefixes

GCP Data Engineering / Storage / Beginner

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime. Suggested time: 15 minutes.

**Core problem**

List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / baseline**

raw/a and raw2/a, prefix raw/ -> raw/a only.

**Interview requirement**

Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## GCP-ANALYTICS-02-I03 — BigQuery nested repeated records

GCP Data Engineering / Analytics / Intermediate

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime. Suggested time: 30 minutes.

**Core problem**

Given Orders(id,items ARRAY<STRUCT<sku STRING,qty INT64>>) with o1:[A2,B1],o2:[], flatten into id,sku,qty using original item offset for ordering. State whether empty orders appear: they must not in this contract.

**Acceptance example / baseline**

[[o1,A,2],[o1,B,1]].

**Interview requirement**

Write an independent equivalent query using a different relational strategy. Compare complete result multisets in both directions; do not use a checksum as proof.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.


## GCP-IDENTITY-01-A07 — Service accounts and impersonation

GCP Data Engineering / Identity / Advanced

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime. Suggested time: 45 minutes.

**Core problem**

Implement a local impersonation decision requiring authenticated caller, exact tokenCreator grant on target service account, and positive requested duration no greater than supplied maximum. Return sorted failed checks.

**Acceptance example / baseline**

Caller a lacking grant on b -> denied even if a has a similarly named account.

**Interview requirement**

Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Submit implementation plus actual outputs/checks. Preserve the core contract except where the extension explicitly changes it. Explain any open design choice with testable evidence.

**Fixture:** Construct the exact inline example. Inject all external I/O; no cloud credentials or real deployment is required for a local-model question.
