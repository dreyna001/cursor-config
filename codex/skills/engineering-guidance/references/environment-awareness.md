# Rule: Environment Awareness Without Lock-In

Design for the current deployment target while avoiding unnecessary coupling to provider-specific infrastructure in the core logic.

Requirements:
- It is acceptable to implement for one environment first.
- Do not pretend the app is environment-neutral if core logic depends on provider-specific primitives.
- Keep business logic understandable without reading cloud trigger code or local runtime wiring.
- Isolate environment-specific concerns near the edges of the app.
- Keep storage, job triggering, model backend calls, and secrets/config handling understandable as deployment concerns.

When working on AWS or on-prem:
- Be explicit about what is deployment-specific.
- Be explicit about what is application logic.
- Do not bury business rules inside Lambda handlers, shell wrappers, cron glue, or infrastructure callbacks.
- Keep input/output shapes clear and stable.

Do not force a universal adapter template.
Do not introduce generic interfaces solely for portability theater.
Portability should come from clean separation of concerns and simple code, not from premature abstraction.

Avoid:
- provider-specific assumptions leaking across the codebase
- overengineering portability before it is needed
- abstract factories, plugin systems, or generic adapter layers without demonstrated need
