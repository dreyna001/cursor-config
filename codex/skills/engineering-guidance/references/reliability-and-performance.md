# Reliability And Performance

- Require explicit timeouts on external calls and distinguish retryable failures from validation, authentication, policy, and other non-retryable failures.
- Use bounded backoff with jitter, honor `Retry-After` when present, and avoid duplicate side effects.
- Handle malformed input, partial failures, and degraded dependencies explicitly.
- Make failure paths observable through structured logs, correlation identifiers, metrics, or clear surfaced outcomes where relevant.
- Flag crash-on-bad-input behavior, retry storms, and missing recovery strategy.
- Give production listeners request quotas, body size limits, timeouts, and connection caps. For production HTTP route coverage, anonymous quotas, and bounded/cached health checks, read [API abuse and exposure](api-abuse-and-exposure.md). Preserve local protections without retrofitting production deployment controls unless requested.

- Distinguish a caller deadline from cancellation of the underlying operation. Verify transport deadlines, SDK retries, cancellation propagation, and cleanup; cancelling a future does not stop an already running thread. When work cannot be interrupted, keep outstanding work bounded until it actually finishes.
- Timeout tests should establish what the underlying operation does after the caller returns, including admission limits and delayed side effects, rather than checking only the raised exception.

# Efficiency

- Flag unbounded reads, concurrency, payloads, context, repeated expensive work, and unnecessary copies.
- Review blocking I/O, batching, pagination, data structure choice, and hot-path logging.
- Consider complexity and scaling behavior for core paths before merging.

## Frontend performance

Apply when implementing or reviewing relevant frontend paths. Preserve project scope, existing architecture, security, and behavior; do not turn unrelated changes into a performance audit.

- Remove third-party scripts confirmed unnecessary, including their unused integrations. Check conditional use and product requirements first.
- Load nonessential analytics and chat widgets outside the critical rendering path, using the framework's supported loading strategy. Prefer loading after initial page load or on interaction where appropriate. Preserve consent, required event capture, and widget availability; avoid duplicate initialization. A deferred script does not by itself guarantee execution after page load.
- For bundle performance work, use the existing build's bundle analyzer or equivalent tooling to identify the largest shipped dependencies and chunks. Inspect production output before changing imports. Prefer supported selective imports, tree shaking, or lazy loading when they reduce shipped code; avoid unsupported deep imports and unnecessary dependency replacements.
- Inspect generated HTML, `modulepreload` links, and the eager import graph when splitting bundles. Count each asset loaded for the initial route once, including preloaded vendor chunks and their eager dependencies; a separate chunk is not necessarily deferred. Compare the same startup scenario and build configuration with a consistent raw/gzip/Brotli size method. Use browser network evidence when available; label calculated compressed sizes separately from observed transfer.
- When substantial screens or expensive content renderers are unnecessary at startup, use the framework's supported route/screen lazy loading and defer renderers such as Markdown until their content is shown. Keep required startup/authentication behavior, deep links, and accessible loading/error states working; do not split every small component by default.
- For long transcripts or rich lists, avoid reparsing or rendering unchanged rich content during timers, streaming updates to other items, and unrelated state changes. Reuse work for unchanged rendering inputs and invalidate it when content or rendering-relevant options change; preserve sanitization and output behavior. Profile representative interactions before adding caching machinery or virtualization.
- Auto-follow chat or transcript updates only while the reader is near the end or explicitly requests the latest content. Preserve their visual anchor and scroll position while they read older content, including when history is prepended; unrelated updates must not force them to the bottom.
- Use existing skeleton components for perceptible initial loading of structured content. Reserve layout space, provide accessible loading status, and respect reduced motion. Preserve usable content during refresh when appropriate, and distinguish loading from empty and error states.
- Use representative builds and interactions to verify the change. Report relevant before/after measurements and checks proportionate to the change. Distinguish expected improvements from measured results; if measurement cannot run, state what remains unverified.
