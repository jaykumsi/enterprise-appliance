# AWS Data Engineering: Databases

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## DynamoDB keys and conditional writes

### Beginner

#### AWS-DATABASES-01-B01

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B02

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B03

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B04

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B05

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B06

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B07

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B08

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B09

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B10

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B11

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B12

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B13

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B14

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-01-B15

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-DATABASES-01-I01

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I02

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I03

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I04

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I05

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I06

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I07

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I08

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I09

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I10

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I11

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I12

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I13

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I14

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-01-I15

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-DATABASES-01-A01

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A02

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A03

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A04

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A05

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A06

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A07

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A08

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A09

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A10

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A11

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A12

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A13

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A14

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-01-A15

**Core:** Implement a local key-value table indexed by (pk,sk), with conditional create-if-absent and versioned update. Return CONFLICT on duplicate create or wrong expected version; successful updates increment version exactly once.

**Acceptance example / fixture:** Create (a,1) -> v1; update expecting v0 -> conflict,still v1.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## DynamoDB query and pagination

### Beginner

#### AWS-DATABASES-02-B01

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B02

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B03

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B04

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B05

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B06

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B07

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B08

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B09

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B10

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B11

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B12

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B13

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B14

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-02-B15

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-DATABASES-02-I01

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I02

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I03

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I04

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I05

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I06

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I07

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I08

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I09

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I10

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I11

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I12

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I13

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I14

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-02-I15

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-DATABASES-02-A01

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A02

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A03

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A04

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A05

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A06

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A07

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A08

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A09

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A10

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A11

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A12

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A13

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A14

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-02-A15

**Core:** Implement query(pk,after,limit) over (pk,sk,value). Select only exact partition key and sort by sk ascending; after is exclusive; limit positive. Return continuation cursor only if more matching rows exist.

**Acceptance example / fixture:** a:1,a:2,b:1; query a,null,1 -> a:1,cursor1.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## RDS transactions

### Beginner

#### AWS-DATABASES-03-B01

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B02

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B03

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B04

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B05

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B06

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B07

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B08

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B09

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B10

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B11

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B12

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B13

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B14

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-DATABASES-03-B15

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-DATABASES-03-I01

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I02

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I03

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I04

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I05

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I06

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I07

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I08

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I09

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I10

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I11

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I12

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I13

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I14

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-DATABASES-03-I15

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-DATABASES-03-A01

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A02

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A03

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A04

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A05

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A06

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A07

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A08

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A09

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A10

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A11

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A12

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A13

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A14

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-DATABASES-03-A15

**Core:** Implement atomic fund transfer over a local RDS-backed repository contract. Positive integer cents only; debit and credit must commit together, with consistent row locking. Starting A:100,B:20, transfer 30; inject failure before credit and prove no partial commit.

**Acceptance example / fixture:** Success A:70,B:50; injected failure A:100,B:20.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
