---
name: review-pr
description: Perform broad PR or code reviews covering correctness, security, reliability, maintainability, tests, docs, and deployment.
---

# Review PR

Use this skill for broad review rather than a narrow domain-specific review.

## Review Dimensions

- correctness
- security
- reliability and performance
- API, data, and distributed behavior
- maintainability and architecture
- dead and stale code
- test quality
- observability
- config
- deployment
- documentation

## Review Rules

- Prioritize merge blockers and high-severity issues.
- Separate direct evidence from inference.
- Mark unknowns explicitly.
- Do not overstate exploitability or impact.
- Avoid low-value style comments unless they create real maintainability risk.
- Recommend concrete fixes.

## Targeted Verification

Load only the relevant existing rule references: [API/data](../../rules/api-data-and-distributed.mdc) for state, queues, or list endpoints; [reliability](../../rules/reliability-and-performance.mdc) for external calls and concurrency; [maintainability](../../rules/maintainability-and-architecture.mdc) for responsibility boundaries; [testing](../../rules/correctness-and-testing.mdc) for verification claims. Use the applicable [stack practices](../development-stack/references/stack-boundaries.md) for framework-specific behavior.

- Trace material behavior across the actual API, service, database, worker, and adapter boundaries; inspecting each function in isolation is insufficient for races and lifecycle failures.
- For each consequential finding, distinguish inspected code, reproduced behavior, and unverified assumptions. Check whether existing tests exercise the failure mechanism.
- For production-readiness reviews, report missing evidence for deployed permissions, dependency resolution, CI, and rollback separately from demonstrated defects. Do not turn unknowns into automatic failures.

## Output

Return sections in this order:
1. Merge blockers
2. High-severity risks
3. Medium-severity issues
4. Dead code or cleanup opportunities
5. Missing tests
6. Suggested refactors
7. Non-blocking observations
