---
description: API, data, and distributed systems review rules
alwaysApply: false
---

# API, Data, And Distributed Systems

- Require explicit schemas and consistent error or response shapes at boundaries.
- Plan versioning or migration when changes can break clients or stored data.
- Require idempotency for replay-prone writes and consumers.
- Review pagination, filtering, and request growth for list-style surfaces.
- Flag duplicate sources of truth, weak constraints, unsafe migrations, and inconsistent serialization.
- Review transaction boundaries, orphaned records, and soft-delete correctness where applicable.
- Assume retries, duplicate delivery, and imperfect clocks in distributed flows.
- Flag lost updates, double processing, ordering assumptions, deadlocks, and retry amplification.
