---
description: API, data, and distributed systems review rules
alwaysApply: false
---

# API, Data, And Distributed Systems

- Require explicit schemas and consistent error or response shapes at boundaries.
- Plan versioning or migration when changes can break clients or stored data.
- Require idempotency for replay-prone writes and consumers.
- Review pagination, filtering, and request growth for list-style surfaces. Check selected database columns and serialized payload size as well as row limits; list endpoints should not load full evidence or report blobs when only summaries are needed.
- Flag duplicate sources of truth, weak constraints, unsafe migrations, and inconsistent serialization.
- Review transaction boundaries, orphaned records, and soft-delete correctness where applicable.
- Trace when related state and queued work become visible to consumers. When both live in one database, commit them together; test consumer claims and duplicate requests across the transition boundary. For external queues, use the existing reliable publication mechanism rather than assuming two writes are atomic.
- Assume retries, duplicate delivery, and imperfect clocks in distributed flows.
- Flag lost updates, double processing, ordering assumptions, deadlocks, and retry amplification.
