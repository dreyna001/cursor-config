---
description: Correctness and test quality requirements
alwaysApply: false
---

# Correctness And Testing

- Verify boundary conditions, malformed input handling, and empty or missing inputs.
- Check duplicate inputs, replay behavior, idempotency, and partial-failure behavior where relevant.
- Review timezone and date correctness anywhere timestamps or ranges matter.
- Check state transition validity, ordering assumptions, and uniqueness assumptions.
- Flag silent failure paths, swallowed exceptions, duplicate side effects, and invalid retry behavior.

# Testing

- Require happy-path, edge-case, negative-path, and regression coverage for non-trivial changes.
- Keep tests deterministic and behavior-focused.
- Avoid flaky assertions and tests tightly coupled to implementation details.
- Test names should describe behavior, not just function names.
- Behavior changes warrant tests for the happy path, representative failure modes, and regressions for parsers, validators, retries, and policy checks.
- Inject clocks, fake HTTP, stubs, or mock model calls instead of live network or real models in unit tests unless explicitly integration-scoped.
- When changing runtime contracts, update examples, operator docs, and runbooks in the same change.
- New features should include a clear verification path when non-obvious.
- Verify that required test, lint, and type checks actually run in the repository's automation when changing its delivery path. Distinguish a locally passing command from configured CI coverage; report missing production-specific validation rather than inferring it from test counts.
