# API, Data, And Distributed Systems

For frontend route and backend API boundaries, including deep-link access and
SPA hosting fallback, also read [frontend and backend URL routing](url-routing.md).

- Require explicit schemas and consistent error or response shapes at boundaries.
- Plan versioning or migration when changes can break clients or stored data.
- Require idempotency for replay-prone writes and consumers.
- Review pagination, filtering, and request growth for list-style surfaces. Check selected database columns and serialized payload size as well as row limits; list endpoints should not load full evidence or report blobs when only summaries are needed.
- Flag duplicate sources of truth, weak constraints, unsafe migrations, and inconsistent serialization.
- Review transaction boundaries, orphaned records, and soft-delete correctness where applicable.
- Trace when related state and queued work become visible to consumers. When both live in one database, commit them together; test consumer claims and duplicate requests across the transition boundary. For external queues, use the existing reliable publication mechanism rather than assuming two writes are atomic.
- Assume retries, duplicate delivery, and imperfect clocks in distributed flows.
- Flag lost updates, double processing, ordering assumptions, deadlocks, and retry amplification.

## Query performance and bounded lists

Apply when implementing or reviewing relevant database or list paths. Preserve project scope, existing architecture, security, and behavior; do not turn unrelated changes into a performance audit.

- Paginate potentially large lists at the data source with bounded page sizes and deterministic ordering. Prefer cursor/keyset pagination when scale and access patterns justify it; retain simpler approaches where sufficient. Virtualization can complement pagination but does not bound data fetching.
- Inspect query patterns, existing indexes, and representative query plans before adding indexes. Consider filters, joins, ordering, and row-level security (RLS) predicates together. Choose useful composite, partial, or other supported indexes where justified; avoid automatically indexing every referenced column. Account for write cost, storage, and migration impact.
- Detect N+1 access patterns using query logs, traces, or query-count checks. Replace per-record fetching with an appropriate join, eager loading, or bounded batch query. Prefer a small, bounded number of efficient queries over forcing everything into one oversized join.
- Preserve authorization, tenant isolation, ordering, pagination, and required consistency during query optimization. Validate RLS using the actual application role; never bypass security policies to improve performance.
- Use representative data, roles, and interactions to verify the change. Report relevant before/after measurements and checks proportionate to the change. Distinguish expected improvements from measured results; if measurement cannot run, state what remains unverified.

## Byte-bounded serialization and backing reads

- When constructing byte-bounded projections, inspect loops that copy and serialize each growing prefix. Avoid that repeated work; incremental exact-byte accounting is suitable when the actual serializer and admissible input contract permit compositional accounting. Otherwise use another verified equivalent approach rather than applying a delimiter formula to an incompatible encoder.
- Preserve the serializer-specific encoding, Unicode/escaping behavior, separators, key conversion and ordering, nested/custom-value handling, and object framing. Count encoded bytes rather than characters. Retain the existing byte limit, field selection/order, and truncation behavior; do not weaken limits or security controls to gain speed.
- Verify output equivalence and byte boundaries below, at, and above the limit, including empty input, non-ASCII and escaped content, nested values, and an oversized entry. Measure representative field counts and value sizes; report a synthetic CPU benchmark as local evidence rather than a production request speedup.
- Distinguish response pagination/projection from backend read bounds: a small returned page can still fetch and parse a complete archive object. Trace and measure storage requests, bytes read, parsing, and projection CPU separately. If full-object reads remain, record that remaining cost and any unmeasured deployed latency; consider a storage-layout change only when requirements, measurements, cost, and migration impact justify it.

## Retry and save identity

Reuse the same logical-operation/idempotency key for retries of the same logical
operation, binding it to the authorized scope and payload. Keep per-attempt
request/trace IDs linked to that operation so retry diagnostics remain distinct. A changed operation requires a
new identity; reject conflicting reuse. Prevent duplicate side effects with the
existing atomic claim/deduplication boundary and retain recoverable job status.
Resolve an unknown outcome by reading that status, not by silently starting over.

After a material saved change, reload through a fresh authorized read and confirm
stored records and associated files match the intended revision/content, including
required integrity and provenance. A success notification is not persistence proof.
Use [the existing boundary testing guidance](correctness-and-testing.md#test-selection-and-trustworthy-evidence)
for browser/API/authentication/storage journeys and explicit real-versus-mocked
dependencies. For shared parsing or byte accounting, also read
[safe preparation](safe-reuse-and-preparation.md).

## Invariants and concurrent updates

- State the relationship that must remain true across the affected records and side effects. Enforce it in the existing authoritative transaction, constraint, or conditional write, including concurrent requests. A read-then-check in application code alone does not prevent a competing write.
- Define conflict behavior for edits to the same revision. Preserve deliberate merge or last-write semantics where required. Use the existing version/precondition mechanism where conflict detection is required. Test independent callers against the real storage boundary when locking or isolation matters.
- For partial failure across services, inspect the existing durable status, reconciliation, or compensation path. Compensation is a new fallible operation, so preserve ownership and retry identity. Add distributed coordination only for a demonstrated invariant that existing boundaries cannot protect.

## Optimistic updates and reconciliation

- Identify the authoritative saved result and the pending local mutation. Reconcile affected detail, list, and cache views on success, and represent rejection or uncertain completion explicitly. Roll back only the failed mutation's contribution so a late failure cannot erase a newer edit.
- Keep displayed stale content distinguishable from confirmed current state. Reuse the established cache and invalidation mechanisms. Verify overlapping saves, failure followed by a newer success, and reload through a fresh authorized read. For scope and late-result ownership, use [reliability guidance](reliability-and-performance.md#reuse-and-completion).

## Contract evolution

- Identify the producers, consumers, stored records, and supported versions affected by a contract change. Include older browser sessions, queued messages, and mixed application versions only where the deployment supports them.
- Use the existing compatibility and migration strategy. Sequence schema expansion, backfill, reader/writer changes, and removal of old fields according to the actual rollout and rollback window. Preserve the meaning of omitted fields, defaults, nulls, enum values, and error shapes that supported callers rely on.
- Exercise representative old and new payloads and records through the real decoder and write/read paths. Include replayed work and rollback compatibility when required. Report an unsupported transition rather than silently discarding data or inventing an indefinite compatibility layer.
