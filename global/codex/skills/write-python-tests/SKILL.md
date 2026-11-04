---
name: write-python-tests
description: "Add Python 3.12 tests for behavior, regressions, runtime contracts, and failure handling."
---
# Write Python Tests

Use this skill when adding or updating Python tests.

## Workflow

1. Define behavior to prove, not implementation details.
2. Cover normal path, edge cases, and failure cases.
3. Target Python 3.12 unless explicitly told otherwise.
4. Use the repository's existing test framework.
5. If no framework exists, prefer pytest.
6. Keep tests deterministic and fast.
7. Keep unit tests isolated from real network calls, external services, model calls, and sleeps.
8. Mock or stub external APIs and model calls in unit tests. Use isolated integration tests against the production database engine when correctness depends on migrations, constraints, locking, or transaction isolation; SQLite and mocks do not prove PostgreSQL behavior. Report unavailable integration infrastructure explicitly. Keep paid model evaluation and live services separately scoped and authorized.
9. Add contract tests when env vars, model names, payload fields, ports, paths, or schemas change.
10. Keep assertions specific and behavior-focused.

## Coverage Bias

Prioritize:
- malformed input
- missing input
- empty input
- duplicate input
- replay behavior
- idempotency
- partial failure
- parse failures
- timeout and retry behavior
- anonymous bursts against health, readiness, and other probe routes are limited
- contract drift

## Output

Return:
- behaviors covered
- important untested areas
- how to run tests

Follow the [shared testing guidance](../engineering-guidance/references/correctness-and-testing.md) for test-level selection, independent expected results, failure-detection controls, durable outcomes, and honest execution evidence.
