# Requirements Confidence

## Requirements and task records

- Identify the repository's authoritative requirements document and task checklist before substantial work. Reuse its existing roadmap, specification, backlog, or issue tracker and state where the current work is recorded. If none exists, choose one suitable repository location and link it from the existing entrypoint.
- Keep requirements and the task checklist together or clearly linked. Update the same records when the user changes direction and when work is completed, recording actual verification and remaining work.
- Keep the record proportional to the task. A small fix can use a short task description and verification result. A substantial feature can use a requirements section and implementation checklist. Apply this to backend, API, data, CLI, model, deployment, export, and UI work as relevant.

## Scope and acceptance

- On non-trivial tasks, get enough clarity on scope, constraints, and success criteria before coding the behavior that depends on them.
- Define pass/fail acceptance criteria for correctness-impacting behavior before implementing that behavior.
- If an unknown could affect correctness, compatibility, security, or safety, ask about that choice and continue work that does not depend on it. Do not guess the blocked decision.
- Add a dependency only when the current task requires it and existing mechanisms are insufficient; explain the need.
- Return only the plan when the user requested planning only. Otherwise proceed once the scope is clear. If a consequential choice blocks part of the work, ask about that choice and continue independent work.
