---
name: mvp-hardening-review
description: "Review MVP blocks for demo, pilot, or handoff readiness without adding unnecessary complexity."
---
# MVP Hardening Review

Use this skill when a current block needs demo, pilot, or handoff readiness.

## Objective

Find the highest-value fixes needed to make the current block runnable, testable, and explainable without turning the review into a rewrite.

## Workflow

1. Restate intended scope.
2. Confirm implementation matches scope.
3. Check required inputs and validation behavior.
4. Check error handling and logging.
5. Check whether any LLM step is bounded and validated.
6. Check output stability and usefulness.
7. Check config and run instructions.
8. Identify top gaps only.
9. Recommend smallest hardening changes with best ROI.

## Constraints

- Focus on the current block only.
- Do not add speculative architecture improvements.
- Do not recommend broad refactors unless a critical defect justifies them.
- Prioritize fixes that reduce operational or demo risk quickly.

## Output

Return:
- scope match
- main risks
- top hardening fixes
- test or fixture gaps
- documentation gaps
- demo readiness