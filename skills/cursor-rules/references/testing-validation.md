---
description: Testing and validation rules for tests, validators, fixtures, and behavior changes
globs: "**/tests/**,**/*test*.py,**/*spec*.py"
alwaysApply: false
---

# Testing And Validation

- Prefer deterministic, behavior-focused tests.
- Cover happy path, edge cases, negative path, and regressions for non-trivial changes.
- Test malformed input, missing input, empty input, duplicate input, replay behavior, idempotency, and partial failure where relevant.
- Avoid flaky assertions and tests tightly coupled to implementation details.
- Inject clocks, fake HTTP, mock model calls, or use fixtures instead of live network or real models in unit tests.
- Validate schemas, serialization, parsing, and external contract compatibility.
- Add tests for parsers, validators, retries, policy checks, generated output parsing, and runtime contract changes.
- Test names should describe behavior, not only function names.
- Include representative fixtures or sample inputs when useful.
- New features should include a clear verification path: test name, command, or manual validation step.
- Keep examples and operator docs synchronized when env vars, ports, request/response shapes, file layouts, or runtime behavior changes.