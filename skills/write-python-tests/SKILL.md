---
name: write-python-tests
description: Adds or updates Python tests focused on behavior and regressions. Use when introducing or modifying Python logic, debugging issues, or enforcing runtime contract behavior and failure handling.
---

# Write Python Tests

## Use This When
- Adding tests for new logic.
- Updating tests after behavior changes.
- Adding regression coverage for bug fixes.
- Enforcing runtime contract behavior and failure handling.

## Workflow
1. Define behavior to prove, not implementation details.
2. Cover normal path, edge cases, and failure cases.
3. Use the repository's existing test framework; if absent, prefer `unittest` unless `pytest` is already established.
4. Keep tests deterministic and fast; avoid real network calls, external services, or sleeps unless explicitly required.
5. Mock or stub external APIs and model calls.
6. Add contract tests when environment variables, model names, payload fields, ports, or paths change.
7. Keep assertions specific and behavior-focused.

## Output
- Behaviors covered.
- Important untested areas.
- How to run tests.
