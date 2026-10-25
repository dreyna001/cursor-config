# Vitest Unit and Component Tests

Read when a React project uses Vitest for unit or component tests. Keep tests deterministic and focused on observable behavior at the seam being changed.

- Use the Node environment for non-DOM code and add `jsdom` or `happy-dom` only for tests that need browser APIs. A simulated DOM does not verify layout, browser navigation, or cross-browser behavior.
- When the behavior under test depends on network responses, time, randomness, browser globals, or an external SDK, control that source of nondeterminism at its boundary. Keep the behavior under test meaningful rather than over-mocking it; ordinary unit/component tests should not depend on live services, real identity providers, or production data.
- Make every test's mutable state explicit. Restore spies/mocks and unstub globals between tests when used; avoid disabling isolation as a speed fix until shared module/global state is known not to leak. Be cautious with automatic global cleanup in concurrent tests.
- Keep test setup proportional to the changed contract: verify a meaningful success case plus the failure or boundary case that could change behavior, then run the repository's existing focused Vitest command.

## Official references

- [Vitest test environments](https://vitest.dev/guide/environment)
- [Vitest mocking](https://vitest.dev/guide/mocking)
- [Vitest global stubs and cleanup](https://vitest.dev/config/unstubglobals)
- [Vitest isolation](https://vitest.dev/config/isolate)

Follow the [shared testing guidance](../../engineering-guidance/references/correctness-and-testing.md) for test-level selection, independent expected results, failure-detection controls, durable outcomes, and honest execution evidence.
