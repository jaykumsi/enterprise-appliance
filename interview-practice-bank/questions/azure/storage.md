# Azure Data Engineering: Storage

[Master index](../../catalog.md)

Every subtopic: 15 Beginner + 15 Intermediate + 15 Advanced. Each numbered question consists of its core,acceptance example and extension. Implement all three parts; the core is not an additional question.

Extension additions preserve the core unless they explicitly introduce a new input/contract. For any design choice left open,declare it and give a testable rationale; an unspecified assumption cannot replace an explicit requirement.

Runtime: Local Python/Java/JavaScript model; native SQL/Spark tasks need their respective runtime.

For generic additional failure tests use injected dependency results. No live credentials,provider calls or deployment are required by local-model questions. Native exercises must run in their stated runtime.

## ADLS paths and partition listing

### Beginner

#### AZ-STORAGE-01-B01

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement the core against an in-memory store and return the supplied example's complete result/state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B02

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add a strict request validator. Distinguish unknown key from invalid key syntax; preserve case sensitivity and the core's exact naming rules.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B03

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Expose a read-only snapshot operation returning records in deterministic key order. Prove reading does not mutate stored state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B04

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Apply one accepted core operation followed by one rejected operation. Return state after both and show rejection leaves the first accepted result intact.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B05

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement an empty-store case. Return the contract's explicit empty/not-found result instead of throwing an unrelated host-language error.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B06

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Build a batch read preserving input key order and repeated keys. Return an explicit found/not-found status for each requested position.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B07

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement exact-match filtering over the core's key/metadata fields. Demonstrate that a similarly named key is not included accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B08

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Produce a state summary with record count and count per status/version category present in the core. Totals must reconcile to the snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B09

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Return a structured operation record with operation ID,key,result category and state version. Do not include secret values in storage examples involving credentials.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B10

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Write a complete state comparison between expected and actual snapshots,including missing keys,extra keys and changed values.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B11

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Demonstrate the first/last boundary of a core prefix,version or expiry rule. Include an excluded neighbor and show the actual results.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B12

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Return a dry-run result for a core mutation without applying it; for a read-only core,return a query plan listing examined keys. Verify original state unchanged.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B13

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Construct two independent stores with identical initial states. Mutate only the first where supported,or query it with a different filter; prove the second remains independent.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B14

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement serialization and reload of the store's nonsecret metadata. Compare the reloaded snapshot and all core decisions with the original.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-01-B15

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Build a baseline acceptance runner reporting expected/actual state and operation outcomes,not only success counts.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-STORAGE-01-I01

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add optimistic concurrency with an expected store revision on writes. Two writers using the same revision must not both overwrite each other.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I02

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement stable cursor pagination over an immutable snapshot. Return next cursor only when more results exist; reject a cursor from another snapshot.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I03

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add idempotency records for mutations. Identical operation ID/payload replays the result; different payload under the same ID is CONFLICT.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I04

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement a bulk operation with validation-before-write and all-or-nothing local state semantics. Show one invalid request prevents every mutation in that bulk call.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I05

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Create a reconciliation report between source and replica snapshots,distinguishing missing,extra,stale and equal-version-conflicting records.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I06

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add an injected failure before commit. Ensure no partially visible metadata/current-pointer update and return a retryable failure record.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I07

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement an LRU read cache keyed by full namespace,key and revision. Demonstrate isolation between identical key names in two namespaces.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I08

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Preserve historical metadata versions and support read-at-revision. Do not fabricate a version that never existed; return VERSION_NOT_FOUND.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I09

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add retention selection using an injected current day and explicit keep-until exclusive boundary. Select eligible metadata without deleting current or pinned revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I10

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement exact metadata checksums using a declared deterministic encoding. Use them as a diagnostic shortcut only; confirm content on checksum match when proving equality.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I11

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Build a transaction journal recording prepare and commit for each state change. A read must never see prepared-but-uncommitted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I12

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add size limits to keys,metadata and batch length before any work. Return precise TOO_LARGE paths and prove no partial write.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I13

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Migrate serialized metadata from schema v1 to v2 with an explicit converter. Keep old snapshots readable and reject unknown versions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I14

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** For prefix/list cores,implement an ordered index; for point-update cores,implement an exact-key index. Compare result parity and actual inspected-key counts with a scan reference.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-01-I15

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement deterministic replay of operation logs. Detect conflicting operation IDs and compare the replayed final state to a stored checkpoint.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-STORAGE-01-A01

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Model two concurrent clients and prove successful conditional mutations are linearizable. Provide a coordinated interleaving that would lose an update in an unconditional implementation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A02

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement crash recovery after prepare,after state persistence and after commit-record persistence. Reopen the store and reconcile incomplete operations without applying committed effects twice.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A03

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Publish immutable multi-object snapshots using one current-pointer update. Demonstrate readers see either the old or new complete snapshot,never a mixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A04

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Introduce replica lag as an explicit model parameter. Support minimum-revision reads returning NOT_CAUGHT_UP when needed rather than a misleading not-found result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A05

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement bounded-memory external reconciliation of two sorted million-record manifests. Compare complete records and retain only a bounded merge window.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A06

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Handle an ambiguous response after a successful commit using durable operation IDs. A retry must discover and return the original committed result.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A07

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Demonstrate stale-cache risk after revocation/deletion or metadata update. Add revision-aware invalidation and a test proving stale sensitive state is not returned.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A08

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement safe garbage-collection planning with snapshot pins. A pinned historical reader must retain every referenced object until its pin expires or is released.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A09

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Design tombstones for versioned deletion so a delayed replica update cannot resurrect removed metadata. Show behavior for older,equal and newer revisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A10

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Build a differential fuzzer against the simple state-machine reference. Generate conflicting writers,duplicate requests,reordered retries and empty/list-boundary cases.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A11

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Add namespace ownership checks at every key resolution boundary. Demonstrate that a key crafted with separators cannot escape into another namespace.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A12

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Implement a migration rollout with dual readers and a single authoritative writer. Show rollback to old readers without losing already accepted state.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A13

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Measure index/cache behavior with a skewed key distribution and a bounded-memory workload. Preserve semantic parity and report actual observations,not provider performance claims.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A14

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Write an independent integrity scanner for dangling current pointers,missing versions,duplicate revisions and journal/state disagreement. Seed and detect each corruption.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-01-A15

**Core:** Implement listing for a lake container and exact case-sensitive prefix; slash is a delimiter, no dot-segment normalization. Return file paths sorted and reject attempts to use another container.

**Acceptance example / fixture:** raw/a and raw2/a under prefix raw/ -> raw/a only.

**Question:** Deliver the store model with concurrency,crash recovery,history,retention and reconciliation evidence. State which guarantees require a real provider-specific integration test.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

## ADLS access-control model

### Beginner

#### AZ-STORAGE-02-B01

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement the core decision function with no network calls. Return a decision and machine-readable reasons for the supplied case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B02

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Evaluate one request that satisfies every grant/precondition and one that lacks the final required grant. Return the exact differing checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B03

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Evaluate a request with no authenticated identity. Show the denial and prove caller-supplied role text cannot create an identity.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B04

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement a batch review returning one decision per request in original order,including repeated requests.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B05

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Return all failed core checks rather than only the first. Sort reasons by their documented names and show a request failing two checks.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B06

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Produce an explanation trace naming only the grants/attributes that influenced the decision. Do not include secret material or raw tokens.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B07

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Evaluate the exact boundary of the core's time/scope/quantity check; where there is no numeric bound,use an exact-match grant and a one-character-different action. Return both decisions.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B08

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add strict schema validation for policy and request objects. Missing mandatory fields are INVALID_INPUT,not ALLOW or an implicit default grant.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B09

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Reject unknown action tokens before matching grants. Supply the list of valid tokens explicitly from the core and return UNKNOWN_ACTION for a new one.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B10

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Canonicalize the decision output so duplicate reasons/grants appear once in sorted order. Demonstrate that input grant order does not affect the decision.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B11

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement a read-only review that does not mutate policy,actor or resource objects. Demonstrate their equality before and after a denied request.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B12

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Return a coverage matrix for two actors and two resources you construct from the core example. Give one allowed and one denied cell.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B13

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Construct the smallest input change that flips the supplied example's decision,and show before/after decisions without changing unrelated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B14

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Build a decision assertion table with request,expected decision,actual decision and reasons. Include missing identity and a wrong-resource case.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

#### AZ-STORAGE-02-B15

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Serialize a review report exposing actor identifier,resource identifier,decision and reason codes only. Demonstrate redaction with a synthetic secret-bearing input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 15 minutes.

### Intermediate

#### AZ-STORAGE-02-I01

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add policy version to each decision. Evaluate the same requests before and after revoking one grant and report exactly which decisions change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I02

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Compare two supplied policy versions over a finite explicit actor/action/resource universe. Return newly allowed and newly denied triples sorted lexicographically.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I03

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement least-privilege reduction for that finite universe: remove grants one at a time only if all required allowed cases remain allowed and all required denied cases remain denied. Do not claim a globally optimal policy.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I04

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add role/group inheritance only where supported by the core model. For other cores,add an explicit dependency graph of required grants. Detect cycles/missing references before evaluation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I05

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement request-context caching keyed by policy version,identity,resource,action and every context value read. Show why omitting one context field creates an incorrect reuse.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I06

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add a dry-run revocation report showing affected allowed requests without changing the live policy object. Apply only the selected revision in a separate operation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I07

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement expiry using an injected integer clock; a grant valid_until is exclusive. Show that a cached allow cannot survive expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I08

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add an audit sink that records the decision after evaluation. Define audit failure as REVIEW_UNRECORDED,never as an allowed business action; demonstrate the fail-closed adapter.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I09

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** For hierarchical scopes,verify slash-segment matching; for exact-key scopes,verify exact equality. Construct a similarly named resource that must not inherit access accidentally.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I10

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Evaluate conflicting allow and deny inputs using the core's stated model. If the model has no deny feature,reject such a field as unsupported rather than inventing provider semantics.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I11

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Generate exhaustive tests for all combinations of the core's boolean preconditions. Return the truth table and identify the minimal requirements for ALLOW.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I12

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add an optimistic policy update requiring expected_version. Reject concurrent stale updates without losing a previously accepted revocation.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I13

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement a review diff that separates actual policy change from reordered or duplicate grants. Prove a cosmetic reorder yields no authorization change.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I14

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Construct an escalation attempt combining missing identity,forged context and overly broad resource selection. Return each denied step with the failed core check.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

#### AZ-STORAGE-02-I15

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Build an adapter from a provider-shaped sample to the explicit local model. Reject unsupported policy features and label the report as a partial simulation,not full provider authorization.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 30 minutes.

### Advanced

#### AZ-STORAGE-02-A01

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Demonstrate time-of-check/time-of-use risk when policy is revoked between decision and action. Add a policy-version precondition at action commit and prove stale authorization cannot complete the action.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A02

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement snapshot-consistent batch evaluation while policy updates occur. Every decision in a report must reference one immutable policy version.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A03

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Design a bounded permission-diff evaluator for a large finite universe. Preserve complete newly allowed/newly denied results and compare with exhaustive enumeration on a small fixture.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A04

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement durable audit with action/decision correlation IDs. Inject a crash between authorization and attempted action; reconcile accepted,rejected and unknown action states.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A05

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Model delayed policy propagation explicitly with versioned evaluator replicas. Return INDETERMINATE when the requested minimum version is unavailable instead of inventing an up-to-date allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A06

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Build differential property tests comparing a slow reference evaluator to an optimized one. Generate exact/similar resource names,expiry boundaries,disabled identities and repeated grants.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A07

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Demonstrate an attacker-controlled cache key collision caused by naive string concatenation. Replace it with typed canonical encoding and prove the two contexts remain distinct.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A08

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Migrate a policy schema while keeping old evaluator clients compatible. Reject unsupported new features in old clients instead of silently broadening access.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A09

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement a revocation-first rollout: new deny decisions must be enforced before introducing any new grant. Show intermediate policy versions and their finite-universe decision diffs.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A10

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Create a reproducible incident reconstruction from policy versions,request context and decision logs. Identify the exact minimal fact that changed an allow into a deny.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A11

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Add tenant isolation and demonstrate that a valid grant in tenant A cannot authorize a similarly named resource in B. Include a cross-tenant administrator claim from untrusted input.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A12

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Bound evaluation work for an adversarially large inheritance/dependency graph. Return a documented RESOURCE_LIMIT outcome without a partial allow.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A13

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Design a break-glass path as a separate authenticated,expiring,audited grant in the local model. Prove it does not bypass missing identity or its own expiry.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A14

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Implement an independent invariant checker asserting every ALLOW has all required core checks and no prohibited context. Seed an overly broad grant defect and show it is detected.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.

#### AZ-STORAGE-02-A15

**Core:** Implement a simplified hierarchical access check: authenticated user needs execute on every ancestor directory and read on the target file. Grants are exact user/action pairs; no groups/default ACL semantics in this model. Return missing path/action pairs.

**Acceptance example / fixture:** Read on file without execute on parent -> denied at parent.

**Question:** Deliver a review package with decision function,reference truth table,policy diff,revocation race test and explicit unsupported-provider-feature list. Do not claim this model replaces live authorization verification.

Fixture: `inline: construct the exact data specified in the core and acceptance example; use injected fakes for external I/O`. Suggested time: 45 minutes.
