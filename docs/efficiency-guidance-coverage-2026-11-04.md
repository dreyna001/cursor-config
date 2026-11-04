# Efficiency guidance coverage — 2026-11-04

The user supplied 17 requested principles, including cancellation/cleanup in
item 14. These are conditional guidance changes, not app implementation or a
requirement to start a new optimization effort.

## Placement

1. Bounded memory caches: new safe-reuse-and-preparation reference; retain approved persistent reuse only with measured need and lifecycle controls.
2. Freshness/access: same reference, routed from security; failed current reads remain failed, retained display content cannot masquerade as fresh evidence.
3. Refresh once: same reference; scope/generation coalescing, fresh mutation/retry reads and late-completion rejection.
4. Prepare once: same reference plus existing API byte-serialization contract; preserve per-workflow limits and citation identity.
5. Preserve analysis: existing llm-efficiency, llm-evidence-regression and agentic safeguards retained; the reuse reference applies them to shared preparation.
6. Chat central: one agentic-security-workflows bullet for existing chat-led products, supporting views and explicit approvals; no universal chat-only redesign.
7. Prove benefit: reuse verification covers before/after work, stale/account/failure/invalidation cases and supported results; existing measured-efficiency guidance retained.
8. Compatible transforms: extraction keys now include content, versions, transform/OCR/layout/output contract, preprocessing, limits and security scope; existing complete embedding contract reused.
9. Upload safety: per-upload admission scanning/validation before extraction reuse; current upload identity and citations remain outside shared transformed content.
10. Check before AI: llm-efficiency now orders deterministic blockers before costly work while valid inputs retain required semantic review.
11. Safe batching: llm-efficiency now defines bounded compatible batching and identified batch-limit fallback without replaying successes or multiplying policy/provider failures.
12. Format meaning: reuse reference defines versioned conversion/projection without rewriting saved material or weakening original integrity.
13. Fair benchmarks: existing benchmark-qualification is reused by link; fixed factors, oracle isolation and all-attempt records are not copied into another policy.
14. Whole result: llm-efficiency compares answer quality, evidence, uncertainty, total workflow cost and end-to-end latency. Reliability now handles late replies and exact-owned, uncommitted/unreferenced staged-upload cleanup.
15. Saved changes: existing boundary testing already requires reload/fresh read; API guidance links that verification to persisted records, file integrity and intended revision.
16. Retry safety: existing idempotency/atomicity preserved; API guidance makes stable logical-operation keys with linked per-attempt trace IDs, conflicting payload reuse, duplicate prevention and recoverable job state explicit.
17. Real boundaries: existing correctness-and-testing remains authoritative for browser/API/authentication/storage coverage, durable readback and labeled mocked dependencies.

## Packaging and boundaries

The native Codex engineering router and Cursor counterpart route into the same
reference contracts. Cursor rules remain small conditional activation stubs.
The scoped checker verifies promoted package mirrors and shared reference links.
App-specific folders, approval gates, source code, runtime state and UI baseline
were not changed. No new standalone skills were needed.

The active WSL profile receives task-owned deltas without replacing its unrelated
local policy edits. Native Windows installation remains outside this task.
Guidance validation is not proof of application savings or whole-stack behavior;
no application, model/provider or performance benchmark was executed for this change.
