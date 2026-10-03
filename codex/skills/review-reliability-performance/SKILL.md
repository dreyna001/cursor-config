---
name: review-reliability-performance
description: "Review resilience, failure handling, efficiency, scaling, retries, integrations, and hot paths."
---
# Review Reliability And Performance

Use this skill for resilience, scaling, and performance-focused review.

## Reliability Checks

- missing timeouts
- bad retries
- missing backoff
- weak partial-failure handling
- crash-on-malformed-input behavior
- missing degradation or recovery behavior
- poor failure observability
- retry amplification
- non-idempotent replay-prone operations

## Performance Checks

- unbounded reads
- unbounded concurrency
- repeated expensive work
- excessive copies or allocations
- blocking I/O on hot paths
- chatty network behavior
- missing batching
- missing pagination
- inefficient serialization
- avoidable memory growth

## Output

Return:
1. Reliability findings
2. Performance findings
3. Expected failure or scaling symptom
4. Concrete remediation
5. Priority order