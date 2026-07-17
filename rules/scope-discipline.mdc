---
description: Scope discipline and smallest production-shaped delivery increment
alwaysApply: true
---

# Rule: Scope Discipline and Delivery Shape

Build the smallest production-shaped increment that solves the current block.

Requirements:
- Do not expand scope beyond the current block unless explicitly asked.
- Prefer boring, well-understood implementation choices.
- Keep the implementation simple, readable, and easy to explain.
- Do not add abstractions "for future use" unless a real current need exists.
- Do not introduce shared libraries, shared frameworks, or generic platforms unless duplication has already proven stable.
- Treat future enhancements as future work, not hidden requirements in the current implementation.
- On non-trivial tasks, get enough clarity on scope, constraints, and success criteria before coding.
- If an unknown could affect correctness, compatibility, security, or safety, stop and ask instead of guessing.
- Prefer small, independently testable diffs that touch only the files needed for the current change.
- When a task needs planning first, stop after the plan and wait for approval before implementing.

When starting work:
- State the exact goal of the current block.
- State what is in scope.
- State what is explicitly out of scope.
- Identify the smallest end-to-end slice that can be demoed.

When proposing structure:
- Favor directness over cleverness.
- Match the design to the use case instead of forcing a template.
- Reuse principles, not code shape.
- Default existing apps to the current direct modular style: keep a clear workflow, simple helper modules, and minimal files.
- Keep `main.py` or the entrypoint focused on orchestration: load config, start the loop, call the main processing steps, handle shutdown, and surface top-level errors.
- For frontend served by a backend, keep backend routes/controllers focused on request handling and response shaping; keep frontend routes/pages focused on UI orchestration, data loading, and passing state to simple components.
- Keep detailed work in simple helper modules or functions: input parsing, LLM calls, validation, rendering, file movement, external calls, and tests.
- Keep detailed frontend work in small components or helpers: form handling, display formatting, client API calls, validation, and focused tests.
- Add new files only when they make the current workflow easier to read or test; otherwise add a small function to an existing module.
- Do not introduce profiles, bundles, registries, shared cores, generic adapters, or plugin-style abstractions unless they solve a proven current need.

Avoid:
- speculative extensibility
- enterprise framework thinking for MVP work
- cross-use-case generalization before it is proven necessary
- adding integration points that are not needed for the current block
