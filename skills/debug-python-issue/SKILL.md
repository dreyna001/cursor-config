---
name: debug-python-issue
description: "Debug Python interpreter, package, crash, timeout, retry, parsing, and regression failures with version-aware minimal fixes; not for non-Python or general recovery work."
---

# Debug Python Issue

Use this skill when diagnosing Python failures or regressions. For non-Python failures or general recovery work, use [debugging and error recovery](../debugging-and-error-recovery/SKILL.md).

## Workflow

1. Capture exact symptom, expected behavior, and observed behavior.
2. Trace relevant code path before editing.
3. Identify likely failure points.
4. Inspect the declared, installed, and deployed interpreter versions and compare them with the failing environment. Do not assume a Python version the project does not use.
5. Separate direct evidence from inference.
6. Mark uncertain items as `unknown`.
7. Reproduce with existing tests, logs, scripts, or minimal fixtures when possible.
8. Inspect inputs, control flow, config/env usage, parsing, and edge cases.
9. Fix the root cause with the smallest safe targeted change.
10. Add a regression test that fails before and passes after the fix.
11. For external or model calls, verify timeout, retry, backoff, and parse-failure handling.
12. Do not fabricate logs, fields, events, or environment details.

## Output

Return:
- root cause
- exact fix made
- remaining unknowns or risks
- verification steps and results