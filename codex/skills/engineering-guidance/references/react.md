---
description: React frontend conventions for functional components, state, and API boundaries
globs: "**/*.{tsx,jsx}"
alwaysApply: false
---

# React Rule

When writing React code, make the smallest safe change that preserves the existing architecture, styling, naming, and API contracts. Prioritize readable functional components, typed props, accessible UI, explicit loading/error states, and clean separation between UI, state, and API logic. Add a library only when the current task requires it and existing mechanisms are insufficient. Do not add broad refactors, clever abstractions, unsafe HTML, fake data, or unnecessary hooks.
