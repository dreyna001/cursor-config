---
description: Reliability, resilience, and performance standards
alwaysApply: false
---

# Reliability And Performance

- Require explicit timeouts on external calls and retries only for transient failures.
- Use bounded backoff with jitter when retrying and avoid duplicate side effects.
- Handle malformed input, partial failures, and degraded dependencies explicitly.
- Make failure paths observable through logs, metrics, or clear surfaced outcomes where relevant.
- Flag crash-on-bad-input behavior, retry storms, and missing recovery strategy.

# Efficiency

- Flag unbounded reads, unbounded concurrency, repeated expensive work, and unnecessary copies.
- Review blocking I/O, batching, pagination, data structure choice, and hot-path logging.
- Consider complexity and scaling behavior for core paths before merging.
