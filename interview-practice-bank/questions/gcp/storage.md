# GCP Data Engineering: Storage

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; BigQuery/Spark native tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Cloud Storage object prefixes

### Beginner

#### GCP-STORAGE-01-B01

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B02

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B03

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B04

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B05

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B06

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B07

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B08

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B09

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B10

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B11

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B12

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B13

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B14

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-01-B15

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-STORAGE-01-I01

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I02

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I03

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I04

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I05

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I06

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I07

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I08

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I09

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I10

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I11

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I12

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I13

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I14

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-01-I15

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-STORAGE-01-A01

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A02

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A03

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A04

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A05

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A06

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A07

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A08

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A09

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A10

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A11

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A12

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A13

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A14

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-01-A15

**Core:** List object names for exact bucket and case-sensitive prefix. Slash is a delimiter,not a real folder; do not normalize ../ segments. Return names sorted.

**Acceptance example / fixture:** raw/a and raw2/a, prefix raw/ -> raw/a only.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Generation preconditions

### Beginner

#### GCP-STORAGE-02-B01

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B02

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B03

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B04

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B05

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B06

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B07

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B08

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B09

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B10

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B11

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B12

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B13

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B14

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### GCP-STORAGE-02-B15

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### GCP-STORAGE-02-I01

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I02

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I03

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I04

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I05

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I06

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I07

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I08

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I09

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I10

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I11

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I12

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I13

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I14

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### GCP-STORAGE-02-I15

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### GCP-STORAGE-02-A01

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A02

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A03

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A04

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A05

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A06

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A07

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A08

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A09

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A10

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A11

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A12

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A13

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A14

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### GCP-STORAGE-02-A15

**Core:** Implement write-if-generation-match for an object. Current generation starts 4; expected 4 replaces content and produces generation5, stale expected4 now conflicts. Create-if-absent uses generation0 and fails for existing objects.

**Acceptance example / fixture:** Two updates expected4 -> one succeeds,other CONFLICT.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
