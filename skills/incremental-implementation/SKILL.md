---
name: incremental-implementation
description: "Implement non-trivial changes in small, verified increments while minimizing scope, complexity, and unnecessary architectural change."
---
# Incremental Implementation

Use this skill for non-trivial features, refactors, integrations, and changes spanning multiple concerns.

## Goal

Deliver the smallest complete implementation that satisfies the current requirement while keeping the codebase working throughout the change.

## Rules

- Scope is closed unless the task explicitly expands it.
- Read the relevant existing code before editing.
- Follow existing project patterns unless the task requires changing them.
- Prefer modifying or deleting existing code over introducing new concepts.
- Reuse existing functions, modules, patterns, and dependencies before creating new ones.
- Do not create an abstraction for one current use unless it materially simplifies the implementation.
- Do not add speculative configurability, extensibility, fallbacks, compatibility layers, or future-facing architecture.
- Do not make unsolicited architectural improvements.
- Do not refactor or clean up unrelated code.
- Prefer one clear implementation path.
- Each increment must produce user-visible or test-visible value.
- Keep each increment small enough to understand and verify independently.
- Keep the repository in a working state between increments when practical.

## Workflow

### 1. Understand

Before editing:

1. Identify the requested behavior.
2. Locate the existing code responsible for that behavior.
3. Identify existing patterns that can be reused.
4. Determine the smallest end-to-end change that provides meaningful value.

Do not design beyond the current requirement.

### 2. Implement the Smallest Slice

Implement the narrowest complete path first.

Prefer:

`existing code → small modification → verification`

over:

`new abstraction → new framework → migration → implementation`

Do not build infrastructure merely because it might become useful later.

### 3. Verify

After each meaningful increment:

- Run the most relevant focused tests.
- Run relevant type checking, linting, or static analysis when applicable.
- Verify the requested behavior directly when practical.
- Fix failures before expanding the implementation.

Do not claim an increment works without evidence.

### 4. Expand Only When Required

Continue only when another change is necessary to satisfy the original requirement.

Before adding a new:

- module
- service
- interface
- wrapper
- helper
- dependency
- configuration option
- abstraction
- compatibility path

ask:

1. Is this required now?
2. Can existing code handle it?
3. Does adding it reduce total complexity now?
4. Is there more than one concrete current use?

If not, do not add it.

## Scope Escalation

If the implementation becomes substantially larger than expected:

1. Recheck the original requirement.
2. Look for a simpler implementation.
3. Determine whether existing architecture creates a genuine constraint.
4. Do not silently expand scope.

If the requirement genuinely conflicts with the existing architecture, report the conflict and explain what additional work would be required.

## Completion

Before finishing:

- The requested behavior works.
- Relevant tests pass.
- No unrelated behavior was changed.
- No speculative architecture was introduced.
- Every changed file has a direct reason to change.
- The implementation is no larger than necessary.
