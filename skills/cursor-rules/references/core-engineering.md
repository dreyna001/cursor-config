---
description: Core engineering standards for all code changes
alwaysApply: true
---

# Core Engineering

- Prefer the simplest implementation that is production-ready.
- Keep changes local, reviewable, and easy to roll back.
- Implement the requested scope; avoid drive-by refactors, speculative abstractions, and unrelated cleanup.
- Follow existing conventions before introducing new patterns.
- Preserve backward compatibility unless the task explicitly allows breaking changes.
- Prefer explicit contracts at boundaries and keep code, config, tests, docs, and deployment files aligned when behavior changes.
- Use modern language and framework features judiciously: clear types, cohesive modules, straightforward control flow, and explicit failure modes beat cleverness.
- Do not introduce new dependencies unless clearly justified; prefer stdlib and existing stack choices.
- Avoid hidden side effects, global mutable state, and surprising behavior.
- Make failure handling explicit and observable where relevant.
- Do not leave commented-out code behind; remove dead code when it is proven unused and safe to delete.
- Be honest about uncertainty: if something is unknown or environment-dependent, say so and prefer configurable or documented behavior over guessing.
- Protect secrets, permissions, and sensitive data by default.
