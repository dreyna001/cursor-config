---
name: review-api-data-maintainability
description: Reviews API contracts, data/storage behavior, distributed-system risks, maintainability, architecture boundaries, dead code, observability, config hygiene, and documentation gaps. Use when reviewing endpoints, schemas, storage, queues, consumers, retries, replay-sensitive flows, or long-term engineering quality.
---

# Review API, Data, Maintainability, And Architecture

Use this skill for API/data/distributed review or maintainability/architecture review.

## API And Contract Focus

- breaking contract changes
- weak schema validation
- inconsistent response shapes
- inconsistent error shapes
- missing versioning
- missing pagination
- inconsistent serialization
- unclear migration path

## Data And Storage Focus

- duplicate sources of truth
- unsafe migrations
- weak constraints
- orphaned records
- soft-delete correctness
- transaction boundary issues
- data drift
- poor storage lifecycle behavior

## Distributed-System Focus

- missing idempotency
- duplicate delivery issues
- retry amplification
- ordering assumptions
- clock assumptions
- replay-sensitive bugs
- unsafe consumer behavior
- deadlocks or lost updates

## Maintainability Focus

- poor boundaries
- hidden dependencies
- duplicated logic
- fragile utilities
- god functions
- deep nesting
- magic values
- leaky abstractions
- hard-to-replace bottlenecks

## Cleanup Focus

- dead code
- stale flags
- zombie tests
- deprecated wrappers
- obsolete docs
- unsafe defaults
- missing operational docs

## Output

Return:
1. Contract risks
2. Data or storage risks
3. Distributed-system risks
4. Maintainability and architecture concerns
5. Dead or stale code to delete
6. Missing docs or operational needs
7. Suggested design changes
8. Merge blockers
9. What to fix now vs later