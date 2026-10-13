---
name: debugging-and-error-recovery
description: "Diagnose non-Python or mixed-stack failures, fix the underlying cause with the smallest correct change, and prove the original failure is resolved; use debug-python-issue for Python-only failures."
---
# Debugging and Error Recovery

Use this skill when behavior is failing, tests are broken, errors are occurring, or the cause of a defect is unknown. For Python-only interpreter, package, crash, timeout, retry, parsing, or regression failures, use [debug Python issue](../debug-python-issue/SKILL.md).

## Goal

Find the root cause, make the smallest correct fix, prevent regression, and verify the original failure is resolved.

## Core Loop

`reproduce → isolate → identify root cause → smallest correct fix → regression test → verify original failure`

Do not skip directly from seeing an error to editing code.

## Rules

- Reproduce the failure before attempting a fix when practical.
- Read the relevant implementation before changing it.
- Gather evidence before forming a conclusion.
- Distinguish the symptom from the underlying cause.
- Separate observed facts from hypotheses; mark unavailable details as unknown and do not invent logs, fields, events, or environment facts.
- Change the smallest amount of code necessary.
- Follow existing project patterns.
- Do not refactor unrelated code while debugging.
- Do not redesign architecture unless the root cause genuinely requires it.
- Do not add retries, fallbacks, guards, broader catches, compatibility branches, or defensive behavior until the underlying failure has been identified.
- Do not suppress errors merely to make tests pass.
- Do not weaken assertions or remove failing tests unless the expected behavior itself is proven incorrect.
- Prefer fixing the producer of invalid behavior rather than compensating at every consumer.

## Workflow

### 1. Reproduce

Establish a reliable failing case.

Capture:

- What fails.
- Expected behavior.
- Actual behavior.
- Relevant error output.
- Smallest known reproduction.

If the failure cannot be reproduced, gather additional evidence before modifying code.

### 2. Isolate

Reduce the problem to the smallest relevant area.

Inspect:

- Call path.
- Inputs and outputs.
- State transitions.
- Recent relevant changes.
- Existing tests.
- External boundaries involved in the failure.

Avoid broad speculative edits.

For Python issues, inspect the declared, installed, and deployed interpreter versions and compare them with the failing environment. For external or model calls, inspect timeout, retry, backoff, and parse-failure behavior.

### 3. Identify the Root Cause

Determine why the system produces the incorrect result.

Do not treat:

- an exception
- a null value
- a timeout
- a failed assertion
- an invalid response

as the root cause merely because it is where the problem becomes visible.

Trace backward until the incorrect state or assumption is identified.

### 4. Make the Smallest Correct Fix

Fix the underlying cause.

Prefer:

`root cause → targeted correction`

over:

`symptom → guard → fallback → retry → catch`

Do not introduce unrelated cleanup or architectural changes.

### 5. Add Regression Coverage

Add or update a test that:

1. Reproduces the original defect.
2. Fails without the fix.
3. Passes with the fix.
4. Expresses the intended behavior clearly.

Use the narrowest appropriate test level.

### 6. Verify

Run:

- The regression test.
- Closely related tests.
- Relevant type/lint/static checks.
- Broader tests when the change could affect shared behavior.

Verify the original reproduction no longer fails.

## When the Suspected Fix Does Not Work

Do not stack another speculative fix on top.

Instead:

1. Revert or reconsider the unsupported assumption.
2. Collect new evidence.
3. Re-isolate the failure.
4. Form a new hypothesis based on observed behavior.

Repeated unsuccessful fixes indicate that the root cause has not been identified.

## Completion

Before finishing:

- The original failure was reproduced or otherwise clearly established.
- The root cause is understood.
- The fix addresses that cause rather than masking the symptom.
- Regression coverage exists when appropriate.
- Relevant verification passes.
- No unnecessary retries, fallbacks, guards, or compatibility paths were introduced.

Report the root cause, the correction made, remaining unknowns or risks, and the verification performed.
