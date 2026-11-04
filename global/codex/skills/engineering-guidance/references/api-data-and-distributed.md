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
