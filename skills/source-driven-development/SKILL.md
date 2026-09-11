---
name: source-driven-development
description: Implement code that depends on an external API, library, framework, SDK, or command-line tool using the installed version, authoritative sources, and established project usage instead of model memory.
---

# Source-Driven Development

Use evidence from the actual project and authoritative sources whenever implementation depends on an external API, library, framework, SDK, or command-line tool.

## Required Workflow

1. Check the installed or locked version.
2. Consult authoritative documentation or source for that version.
3. Search the existing codebase for current usage.
4. Follow the existing project pattern when it remains valid.
5. Do not invent APIs, parameters, behaviors, or configuration from model memory.

## Source Priority

Prefer evidence in this order:

1. The project's manifests, lockfiles, configuration, and existing code.
2. Locally installed types, package source, generated schemas, or built-in help.
3. Official versioned documentation.
4. Official source code, release notes, or migration guides.

Use third-party explanations only as supporting context when authoritative sources do not answer the question.

## Version Discipline

- Match the implementation to the version the project actually uses.
- Do not assume documentation for the latest release applies to an older installed version.
- Do not upgrade a dependency merely to match a newer or remembered API unless the task explicitly requires an upgrade.
- When an upgrade is required, check the official migration guidance and keep code, tests, configuration, and lockfiles synchronized.

## Existing Project Patterns

Reuse an existing integration pattern when it is valid for the current version and requirement.

Do not copy an existing pattern blindly when evidence shows that it is deprecated, incorrect, or responsible for the current defect.

## Uncertainty

If authoritative sources conflict or the applicable version cannot be determined:

- Do not guess.
- Inspect the installed implementation or types when available.
- State the uncertainty and the evidence needed to resolve it.
- Avoid committing version-sensitive behavior until it can be verified.

## Completion

Summarize:

- The version used.
- The authoritative source or local evidence consulted.
- The existing project pattern followed or intentionally changed.
- The verification performed.
