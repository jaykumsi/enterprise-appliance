# AWS Data Engineering: Storage

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native Athena query tasks need Athena or a declared compatible dialect.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## S3 buckets prefixes and keys

### Beginner

#### AWS-STORAGE-01-B01

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B02

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B03

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B04

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B05

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B06

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B07

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B08

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B09

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B10

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B11

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B12

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B13

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B14

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-01-B15

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-STORAGE-01-I01

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I02

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I03

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I04

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I05

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I06

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I07

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I08

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I09

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I10

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I11

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I12

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I13

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I14

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-01-I15

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-STORAGE-01-A01

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A02

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A03

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A04

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A05

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A06

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A07

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A08

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A09

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A10

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A11

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A12

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A13

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A14

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-01-A15

**Core:** Implement an object-prefix listing over records {bucket,key,size}. Keys are case-sensitive exact strings, slash is a delimiter, and no filesystem normalization is allowed. For bucket b and prefix raw/, return matching keys sorted lexicographically.

**Acceptance example / fixture:** b/raw/a,b/raw2/a,b/raw/B -> [raw/B,raw/a].

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## S3 Tables and snapshot commits

### Beginner

#### AWS-STORAGE-02-B01

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B02

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B03

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B04

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B05

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B06

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B07

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B08

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B09

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B10

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B11

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B12

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B13

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B14

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-02-B15

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-STORAGE-02-I01

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I02

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I03

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I04

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I05

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I06

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I07

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I08

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I09

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I10

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I11

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I12

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I13

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I14

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-02-I15

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-STORAGE-02-A01

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A02

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A03

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A04

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A05

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A06

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A07

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A08

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A09

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A10

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A11

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A12

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A13

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A14

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-02-A15

**Core:** Model an immutable table manifest with current snapshot ID. Commit a candidate only if its base snapshot equals current; otherwise return CONFLICT. A successful commit atomically changes the snapshot and preserves old manifests for readers.

**Acceptance example / fixture:** Current s1; commit s2 based s1 succeeds; commit s3 based s1 now conflicts.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Zero ETL reconciliation

### Beginner

#### AWS-STORAGE-03-B01

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B02

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B03

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B04

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B05

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B06

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B07

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B08

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B09

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B10

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B11

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B12

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B13

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B14

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AWS-STORAGE-03-B15

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AWS-STORAGE-03-I01

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I02

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I03

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I04

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I05

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I06

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I07

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I08

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I09

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I10

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I11

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I12

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I13

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I14

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AWS-STORAGE-03-I15

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AWS-STORAGE-03-A01

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A02

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A03

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A04

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A05

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A06

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A07

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A08

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A09

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A10

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A11

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A12

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A13

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A14

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AWS-STORAGE-03-A15

**Core:** Given source and replicated records {id,version,value} plus captured source watermark, report missing/stale/conflicting sink records at or below that watermark. A record above the watermark is not evidence of lost replication.

**Acceptance example / fixture:** Source a:v2,watermark2; sink a:v1 -> stale a.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
