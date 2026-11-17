# Snowflake: Loading

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Native Snowflake for SQL; Python/Java/JavaScript for explicitly described local models.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## Stages and file manifests

### Beginner

#### SNOW-LOADING-01-B01

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B02

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B03

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B04

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B05

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B06

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B07

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B08

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B09

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B10

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B11

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B12

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B13

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B14

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-01-B15

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-LOADING-01-I01

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I02

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I03

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I04

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I05

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I06

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I07

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I08

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I09

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I10

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I11

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I12

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I13

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I14

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-01-I15

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-LOADING-01-A01

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A02

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A03

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A04

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A05

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A06

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A07

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A08

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A09

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A10

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A11

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A12

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A13

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A14

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-01-A15

**Core:** Build a load manifest from staged files {path,checksum}. Skip identical previously committed path/checksum pairs. Changed content at an old path is CONFLICT pending operator resolution,not silently skipped.

**Acceptance example / fixture:** Committed a/x; staged a/x,b/y -> load b only.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## COPY validation and rejected rows

### Beginner

#### SNOW-LOADING-02-B01

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement the core transformation and return accepted output plus rejected/error output exactly as specified by the acceptance example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B02

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Create a row-level trace from each input record to its output/rejection. Preserve original source index or source ID for lineage.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B03

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Run the core on an empty input with the same schema. Return typed empty outputs and zero counters,not an absent/unknown result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B04

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Validate required fields and return all rejected source positions. Demonstrate the difference between a missing field,null and a valid zero where the core permits zero.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B05

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Produce a reconciliation summary input_count,accepted_input_count,rejected_input_count. For one-to-many outputs also return output_count; do not equate output rows with accepted input records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B06

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement a strict output schema check for names,types and nullability. Give one incorrectly typed candidate row and its exact failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B07

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Return accepted records in the core's prescribed order and a separate deterministic reject report sorted by source position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B08

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Write a batch adapter preserving source-file ID and logical record number throughout parsing and transformation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B09

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement a dry-run validation pass that emits diagnostics but writes no sink data or checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B10

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Produce per-error-reason counts and reconcile their unique rejected-record count separately when one row has multiple reasons.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B11

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Serialize accepted output to NDJSON with one complete record per line. Preserve exact integers,nulls and escaped delimiter characters.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B12

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Demonstrate a repeated identical input record according to the core's explicit duplicate rules. If the core has no deduplication rule,preserve both occurrences and report their multiplicity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B13

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Separate parse errors from business-validation errors. A malformed record must retain its source location without being treated as a zero-valued valid row.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B14

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement a small independent reference transformation and compare full output records with the main implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-02-B15

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Create an executable acceptance table with source,expected disposition,expected output and actual output. Include an empty case and a boundary case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-LOADING-02-I01

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Process input as a stream with bounded batches. Do not collect all records in memory; preserve global grouping/dedup semantics using explicit retained state where required.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I02

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add deterministic batch IDs and committed-batch deduplication. Repeating an already committed batch cannot duplicate sink effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I03

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Split input into two partitions and combine partial outputs correctly. Show which operations require a merge stage rather than naive concatenation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I04

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add a source-to-sink reconciliation by business key and complete payload. Matching row counts alone must not pass an unequal dataset.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I05

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement a schema-evolution gate: optional added fields compatible,removed/type-changed/newly required fields breaking. Return sorted schema differences before loading.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I06

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Write accepted rows and reject rows under one batch manifest. Publish the manifest only after both outputs are durable.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I07

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Inject a sink failure after some tentative writes. Recover without marking the batch/checkpoint committed or duplicating accepted records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I08

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Use exact integer arithmetic for counts/amounts and detect overflow at the declared output boundary. Do not silently convert to binary floats.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I09

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add source cursor tracking and commit the cursor only with output publication. Demonstrate a retry from the last committed cursor.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I10

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Handle late-arriving corrections with versions/effective times supplied as additional input metadata. Recompute affected outputs and retain a trace of superseded results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I11

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Build per-partition quality thresholds with explicit rule: quarantine batch if rejected/input>0.05; empty input is valid with ratio0. Return actual ratios and dispositions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I12

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement a deterministic content manifest with schema version,input identities,output counts and checksums. Confirm complete records when using the manifest to prove equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I13

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Compare a native framework implementation with the local reference on the same fixture,normalizing only documented representation differences.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I14

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add privacy-preserving reject output: include record ID,field and reason but no raw secret-bearing values. Demonstrate with a synthetic credential field.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-02-I15

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Construct an adversarial fixture that exposes a join multiplication,wrong watermark boundary or duplicate-version bug applicable to this core. Show the failed shortcut and corrected result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-LOADING-02-A01

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Build restartable end-to-end processing with immutable input manifest,versioned output and atomic current-manifest publication. Inject failure before each publication boundary.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A02

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement out-of-order corrections and tombstones without stale resurrection. Reconcile final state with a full source replay in version order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A03

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Scale to a highly skewed partition while retaining correctness. Measure actual partition work and propose bounded splitting/combining rather than changing business keys arbitrarily.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A04

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Demonstrate two simultaneous writers for the same batch/partition. Use ownership with a fencing token so only the current owner can publish.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A05

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add schema migration while old and new consumers coexist. Publish explicit versioned contracts and reject consumers unable to represent new required semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A06

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement a bounded-memory merge reconciliation of sorted source and sink manifests. Detect missing,extra and changed payloads with duplicate-key diagnostics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A07

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Create differential generated tests for empty input,nulls,ties,late updates,repeated IDs and malformed nested data applicable to the core. Persist a reproducible counterexample.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A08

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Design event-time versus processing-time behavior for delayed inputs. Supply explicit watermarks and allowed lateness,then show accepted,corrected and too-late outcomes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A09

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Model an ambiguous sink commit timeout. Discover commit status using durable batch ID before retrying; unresolved status remains UNKNOWN rather than assumed failure.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A10

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add auditable lineage from each published output to contributing source versions and transformation version. Verify one output independently from those contributors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A11

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Implement safe backfill overlapping live incremental loads. Assign partition/version ownership and prove the final view has no duplicate or lost business keys.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A12

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Add end-to-end backpressure with bounded parser,transform and sink queues. Demonstrate bounded retained records under a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A13

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Reconcile exact totals and complete records across a type/format conversion. Seed a precision/truncation/Unicode defect applicable to the core and demonstrate detection.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A14

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Write an independent quality monitor using published manifests and source identities. Detect a missing batch even when the remaining batches have individually valid row counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-02-A15

**Core:** Validate staged CSV rows id,cents before a load. Integer cents required; duplicate IDs within batch reject all occurrences of that ID. Return accepted rows and rejected source record numbers; commit only accepted rows under a unique batch ID.

**Acceptance example / fixture:** a:1,a:2,b:3 -> accept b; reject both a rows.

**Question:** Deliver a runnable local pipeline with schema checks,lineage,replay,backfill and failure-injection evidence. List native service/framework integration checks still needed for deployment.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## Snowpipe event deduplication

### Beginner

#### SNOW-LOADING-03-B01

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement the core using injected inputs/outcomes and return a deterministic ordered state-transition trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B02

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Run the happy path and return each step's input,output and final status. No step may run before its prerequisites.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B03

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Inject failure in the first core step. Return failed and blocked work separately and prove no dependent side effect occurs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B04

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Validate all node/event/job identifiers before scheduling. Missing references return INVALID with sorted identifiers and no work started.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B05

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Construct an empty-work case and return the documented terminal state with no phantom task execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B06

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add a state-transition guard rejecting an event that is not legal from the current state. Return INVALID_TRANSITION without mutation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B07

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Return a dependency adjacency list and a topological order where the core has a DAG; for a state machine,return its allowed transition table and a valid path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B08

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Record attempt number starting at one for every invoked step. Demonstrate that a skipped/blocked step has zero attempts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B09

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add a dry-run planner listing intended work and dependency order without calling injected workers/providers.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B10

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Return an event log with sequence numbers increasing by one. Do not use wall-clock time to determine causal order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B11

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Demonstrate that replaying a read-only trace produces the same final status and attempt counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B12

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Build a batch of independent workflows returning one terminal summary per input workflow ID in input order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B13

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Validate one numeric/time/attempt boundary from the core. If none exists,add max_steps as a positive integer and reject before execution when invalid.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B14

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add a final invariant check that completed work has every required predecessor completed. Return violating step IDs on a deliberately corrupted trace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### SNOW-LOADING-03-B15

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Create an acceptance runner comparing the full transition trace against an explicitly written expected trace for the core example.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### SNOW-LOADING-03-I01

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add bounded concurrent scheduling of independent ready work. Use lexicographic ID tie breaking and return the maximum observed in-flight count.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I02

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement the core's retry rule with injected clock and deterministic backoff; if absent,use at most two retries after first attempt at delays 1 and 2 units. Permanent errors never retry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I03

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add a workflow-level deadline. Stop starting new work at deadline,request cancellation of active work and distinguish completed,failed and cancelled tasks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I04

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Use durable idempotency keys for accepted business effects. Repeated delivery after commit returns the recorded outcome without reapplying the effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I05

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Handle a cycle in dependencies or a repeated invalid transition loop. Detect it before unbounded work and return a concrete cycle/path witness.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I06

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add checkpointing after each committed step. Restart from a checkpoint without rerunning already committed effects.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I07

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement partition/batch ownership with an expected ownership version. A stale owner must not publish output even if its computation completes.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I08

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Run two workflow instances sharing a worker capacity. Enforce a global bound and deterministic fairness by queued sequence number.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I09

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Separate transient,permanent and unknown outcomes. Unknown side effects enter NEEDS_RECONCILIATION and cannot automatically be retried as if no effect occurred.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I10

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add a manual retry command for a failed step after its cause is repaired. Reuse the workflow and effect IDs; do not duplicate completed predecessors.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I11

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Build a transition-log validator rejecting duplicate sequence numbers,missing prerequisites and impossible terminal-state reversals.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I12

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement a plan diff between two dependency/state-machine definitions. Identify newly blocked work and invalidated checkpoints before adopting a new version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I13

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add per-step input/output contracts. A worker reporting success with malformed output is FAILED_VALIDATION and cannot unblock descendants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I14

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Produce operational metrics from the trace: attempts,retries,blocked steps,in-flight peak and terminal counts. Reconcile them with actual worker calls.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### SNOW-LOADING-03-I15

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement deterministic schedule simulation with supplied durations/outcomes. Return start/end times and a counterexample to scheduling everything in input order despite unmet dependencies.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### SNOW-LOADING-03-A01

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Demonstrate crash recovery at every boundary around worker completion and checkpoint commit. Prevent duplicate business effects with durable effect IDs and reconciliation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A02

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement leased ownership with monotonically increasing fencing tokens. Show an expired worker finishing late cannot overwrite a newer worker's publication.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A03

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Model at-least-once delivery,out-of-order arrival and deduplication together. Preserve the core's per-key/state ordering without assuming global event order.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A04

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement a compensating workflow for a multi-step accepted effect. Do not label compensation a database rollback; record which effects were compensated and which need manual resolution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A05

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add backpressure across producer,worker and result sink. Bound every queue and demonstrate progress with a deliberately slow sink.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A06

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Support a versioned workflow definition while older instances remain active. Pin each instance's definition version and demonstrate a safe explicit migration of one checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A07

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Handle a provider timeout after it may have completed an effect. Reconcile by effect ID before deciding retry,success or unresolved status.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A08

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement a replay simulator that explores alternative valid concurrent interleavings on a small fixture. Assert dependency,capacity and idempotency invariants on every explored path.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A09

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Add a dead-letter/reconciliation queue with structured failure reason and original correlation ID. Replay after correction must reuse the original idempotency identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A10

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Process a large dependency graph with bounded recursion and indexed ready queues. Detect cycles and compare the schedule's correctness with a small reference implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A11

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Demonstrate tenant isolation under shared capacity: one tenant cannot execute another's tasks or consume all scheduling opportunities indefinitely. Use an explicit round-robin tenant policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A12

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Design an audit query over the transition journal that reconstructs the exact accepted effects for one workflow. Detect a missing or duplicated effect record independently.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A13

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Implement safe cancellation races: cancellation before start,during work,and after commit. Return distinguishable outcomes and never claim cancellation undid a committed effect.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A14

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Inject failures in the journal,worker,sink and ownership store separately. Show which failures permit retry and which require reconciliation without inventing an exactly-once guarantee.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### SNOW-LOADING-03-A15

**Core:** Model file-arrival events by (path,checksum). A completed pair is a no-op; another checksum at the same path is quarantined. Mark complete only after load commit. Retry before commit must not produce duplicate rows.

**Acceptance example / fixture:** Repeated completed a/x -> one load.

**Question:** Deliver the core with durable state,deterministic simulation,race tests,capacity evidence and a complete recovery trace from one interrupted execution.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
