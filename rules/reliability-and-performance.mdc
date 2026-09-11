---
description: Reliability, resilience, and performance standards
alwaysApply: false
---

# Reliability And Performance

- Require explicit timeouts on external calls and distinguish retryable failures from validation, authentication, policy, and other non-retryable failures.
- Use bounded backoff with jitter, honor `Retry-After` when present, and avoid duplicate side effects.
- Handle malformed input, partial failures, and degraded dependencies explicitly.
- Make failure paths observable through structured logs, correlation identifiers, metrics, or clear surfaced outcomes where relevant.
- Flag crash-on-bad-input behavior, retry storms, and missing recovery strategy.

- Distinguish a caller deadline from cancellation of the underlying operation. Verify transport deadlines, SDK retries, cancellation propagation, and cleanup; cancelling a future does not stop an already running thread. When work cannot be interrupted, keep outstanding work bounded until it actually finishes.
- Timeout tests should establish what the underlying operation does after the caller returns, including admission limits and delayed side effects, rather than checking only the raised exception.

# Efficiency

- Flag unbounded reads, concurrency, payloads, context, repeated expensive work, and unnecessary copies.
- Review blocking I/O, batching, pagination, data structure choice, and hot-path logging.
- Consider complexity and scaling behavior for core paths before merging.
