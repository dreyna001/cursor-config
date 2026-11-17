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

## Model and embedding efficiency

For model-call and embedding/indexing paths, apply [LLM efficiency with preserved analysis](llm-efficiency.md). Inspect redundant provider work, reuse only compatible results, and measure retained behavior with token/call savings.

## Reuse and completion

For caches, overlapping refreshes and repeated preparation, use
[safe reuse and preparation](safe-reuse-and-preparation.md).
On cancellation or conversation/account/object changes, bind replies to the
originating request, scope and generation. A late reply must not update the
active conversation or new object. Reconcile unknown external completion
through its durable status rather than replaying work.

For overlapping operations on the same object, establish which result may commit or update the view, such as the latest requested read or every serialized mutation. Bind completion to the operation's captured identity and revision. Test reversed completion order, a failed earlier operation after a newer success, and a scope change while work is active. Preserve intentional concurrent work and enforce durable conflict rules at the server boundary.

Clean up abandoned staged uploads using the existing bounded, retry-safe cleanup
path only after verifying exact ownership and that the object is uncommitted and
unreferenced. Preserve attachments already saved, shared or claimed by another
operation. Surface failed cleanup and retain recoverable status; cancellation
does not authorize broad deletion.

## Resource ownership and cleanup

- Identify who creates, owns, shares, and releases subscriptions, timers, sockets, tasks, streams, temporary files, and database sessions in the affected path. Pair acquisition with cleanup on success, error, cancellation, and repeated setup/teardown.
- Release only resources owned by that lifecycle. A departing caller must not cancel work still needed by another subscriber. Keep in-flight work tracked until it settles before releasing the session, transaction, or lock it uses.
- Verify repeated mount/unmount or connect/disconnect cycles and partial initialization failure using observable resource counts or effects where practical. Test idempotent cleanup and late completion without relying on arbitrary sleeps or adding a general resource manager for a local defect.

## Observability and failure isolation

- Preserve a logical operation's correlation across requests, retries, queued work, and completion while distinguishing individual attempts. Use existing logging/tracing facilities to record safe identifiers, outcomes, and failure causes at the boundary that owns recovery; avoid repeated logging of the same failure.
- Verify that normal failure and cancellation paths produce a useful user or operator outcome. Preserve [security guidance](security.md) for sensitive content, credentials, and telemetry. Add infrastructure or broad instrumentation only when needed for a demonstrated diagnostic gap.
- Identify which dependency failures may degrade optional behavior and which must fail the operation. Keep authorization, integrity, and required persistence checks fail-closed. Isolate a failing optional widget or integration without reporting a required operation as successful or losing its failure state.
- Test dependency failure, recovery, and the unaffected required path. Use established timeouts, admission limits, and retry policy. Introduce circuit breakers or bulkheads only when measured failure propagation or resource contention justifies them.
