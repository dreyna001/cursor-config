---
description: Tests and docs when behavior or contracts change
alwaysApply: false
globs: "**/README.md,**/docs/**/*.md,**/tests/**/test_documentation_contract.py"
---

# Testing and Documentation Standards

Follow `correctness-and-testing` for general testing and runtime-contract requirements.

# Operator documentation contracts

- Every deploy path must end at a validation doc or section with real commands and expected outcomes.
- When root README paths, runbook ownership, or journey links change, update or add `test_documentation_contract.py` in the same change.
- Preserve approval gates, supported environment bounds, commands, and rollback-vs-teardown distinction when simplifying docs.
- Full journey refactors: use skill `operator-documentation-journey`.
