---
name: debug-python-issue
description: Investigates Python failures and implements minimal safe fixes with evidence-driven root cause analysis. Use when handling crashes, incorrect outputs, timeout or retry issues, parsing failures, or regressions in onprem_service, onprem_rag, and onprem-llm-sdk.
---

# Debug Python Issue

## Use This When
- Investigating a failing workflow or regression.
- Diagnosing exceptions, bad output, timeout or retry behavior, or parse failures.
- Tracing and fixing issues in `onprem_service`, `onprem_rag`, or `onprem-llm-sdk`.

## Workflow
1. Capture the exact symptom, expected behavior, and observed behavior.
2. Trace the relevant code path before editing and identify likely failure points.
3. Separate direct evidence from inference; label uncertain items as `unknown`.
4. Reproduce with existing tests, logs, or scripts when possible.
5. Inspect inputs, control flow, config or env usage, parsing, and edge cases.
6. Fix the root cause with the smallest safe targeted change.
7. Add a regression test that fails before and passes after the fix.
8. For external or model calls, verify timeout, retry, backoff, and parse-failure handling.
9. Do not fabricate logs, fields, events, or environment details.

## Output
- Root cause.
- Exact fix made.
- Remaining unknowns or risks.
- Verification steps and results.
