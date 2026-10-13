# React Rule

When writing React code, make the smallest safe change that preserves the existing architecture, styling, naming, and API contracts. Prioritize readable functional components, typed props, accessible UI, explicit loading/error states, and clean separation between UI, state, and API logic. Add a library only when the current task requires it and existing mechanisms are insufficient. Do not add broad refactors, clever abstractions, unsafe HTML, fake data, or unnecessary hooks.

When changing authentication, API credential forwarding, browser persistence, uploads/previews, or rendering of untrusted content, read [security](security.md) and its matching framework reference. Production response-header and cache policies belong at the actual serving boundary; a layout-only change does not require a security retrofit.
