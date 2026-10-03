---
description: Core engineering standards for all code changes
alwaysApply: false
---

# Core Engineering

- Preserve backward compatibility unless the task explicitly allows breaking changes.
- Prefer explicit contracts at boundaries; keep code, config, tests, docs, and deployment files aligned when behavior changes.
- Use modern language and framework features judiciously: clear types, cohesive modules, straightforward control flow, and explicit failure modes.
- Add a dependency only when the current task requires it and existing mechanisms are insufficient; explain the need.
- Avoid hidden side effects, global mutable state, and surprising behavior.
- Make failure handling explicit and observable where relevant.
- Remove dead or commented-out code only when its removal is required by the current task.
- Be honest about uncertainty; prefer configurable or documented behavior over guessing.
- Protect secrets, permissions, and sensitive data by default.
