---
name: review-api-data-distributed
description: "Review APIs, schemas, storage, queues, retries, replay behavior, and distributed data risks."
---
# Review API, Data, And Distributed Systems

## Focus

- breaking contract changes and weak schema validation
- inconsistent response or error shapes
- missing idempotency, pagination, or versioning
- duplicate sources of truth and inconsistent serialization
- unsafe migrations, weak constraints, orphaned records
- retries, duplicate delivery, ordering assumptions, and clock issues

## Output

Return:
1. Contract risks
2. Data or storage risks
3. Distributed-system risks
4. Suggested design changes
5. Merge blockers
