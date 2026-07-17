---
name: review-correctness
description: Review logic, state, boundaries, replay behavior, validation paths, and correctness test gaps.
---

# Review Correctness

Use this skill for correctness-focused review.

## Focus

- logic errors
- boundary conditions
- malformed input
- missing input
- null input
- duplicate input
- state transition validity
- replay and idempotency behavior
- ordering and uniqueness assumptions
- timezone and timestamp correctness
- partial-failure handling
- silent failure paths

## Test Review

Check for:
- happy path
- edge cases
- negative cases
- malformed input paths
- replay behavior
- duplicate behavior
- regression coverage

## Output

Return:
1. Findings by severity
2. Why each matters
3. Concrete fix recommendation
4. Missing tests
5. Residual risk