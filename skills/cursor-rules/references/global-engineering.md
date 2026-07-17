---
description: Global engineering rules always loaded for every request
alwaysApply: true
---

# Global Engineering Rules

- Prefer the simplest production-ready implementation.
- Keep changes local, small, reviewable, and easy to roll back.
- Implement only the requested scope; avoid drive-by refactors and speculative abstractions.
- Follow existing codebase conventions before introducing new patterns.
- Preserve backward compatibility unless a breaking change is explicitly requested.
- Prefer explicit contracts at boundaries.
- Keep code, config, tests, docs, examples, and deployment files synchronized when behavior or contracts change.
- Validate external input before persistence, execution, or security-sensitive use.
- Fail closed for risky operations.
- Make failure modes explicit and observable.
- Do not hardcode secrets or log credentials, tokens, session cookies, raw auth headers, or sensitive payloads.
- Separate direct evidence, advisory context, and inference.
- Do not fabricate facts, findings, IDs, IOCs, events, or source evidence.
- Prefer stdlib and existing dependencies; add third-party packages only when clearly justified.
- Do not leave commented-out legacy code behind.
- Remove dead code when proven unused and safe to delete.