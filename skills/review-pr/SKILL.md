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

## Output

Return sections in this order:
1. Merge blockers
2. High-severity risks
3. Medium-severity issues
4. Dead code or cleanup opportunities
5. Missing tests
6. Suggested refactors
7. Non-blocking observations