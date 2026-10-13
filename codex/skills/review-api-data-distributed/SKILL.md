---
name: review-api-data-distributed
description: "Review APIs, schemas, storage, queues, retries, replay behavior, and distributed data risks."
---
# Review API, Data, And Distributed Systems

## Focus

- breaking contract changes, weak schema validation, and inconsistent response or error shapes
- missing idempotency, pagination, or versioning; inconsistent serialization; and unclear migration paths
- duplicate sources of truth, unsafe migrations, weak constraints, orphaned records, and data drift
- transaction boundaries, soft-delete correctness, and storage lifecycle behavior
- retries, duplicate delivery, ordering or clock assumptions, retry amplification, and replay-sensitive behavior
- lost updates, double processing, unsafe consumers, deadlocks, and partial failures

## Output

Return:
1. Contract risks
2. Data or storage risks
3. Distributed-system risks
4. Suggested design changes
5. Merge blockers
