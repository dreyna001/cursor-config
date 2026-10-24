# Repository guidance

## Agentic SSP workflow

Use the shared `agentic-security-workflows` skill at
`$HOME/.agents/skills/agentic-security-workflows/SKILL.md` with its SSP-authoring reference for evidence, drafting, contextual-assistant and
review/export changes. The source-backed [review backlog](docs/AGENTIC_WORKFLOW_REVIEW.json)
credits implemented capabilities and preserves current-profile scope, revision
approval and authority/release gates. It does not add an authorization workflow.

Inherit `~/.codex/AGENTS.md` and use applicable global skills under `~/.agents/skills/`. Keep shared instructions there; project-specific validation policy follows.

## Local validation policy

GitHub Actions is disabled for this project, as stated by the user on October 12, 2026. Use local verification and reviewable local diffs. Do not initiate GitHub work, enable Actions, maintain workflows or treat inactive workflow findings as active remediation tasks unless the user explicitly requests it. Existing workflow files are retained as inactive references, not evidence of executed checks. Preserve application security checks and production qualification requirements; run applicable checks locally within the authorized task scope.

## SSP field assignment

For SSP generation, imports and synthetic setup inputs, populate each field with
only information that matches its documented meaning. A component's name identifies
it, its purpose describes its function, and its placement describes its relationship
to the authorization boundary. Do not paste a composite inventory line into purpose
or put personnel, ownership, versions, instance counts or deployment settings there.
Preserve the original source and citation, including accountability information;
use the corresponding supported personnel/inventory fields or relevant control
narrative. Do not invent schema fields or remove legitimate names from component
identities, functional subjects or responsible-actor statements. For the verified
failure and regression boundaries, see [SSP field mapping](docs/PROJECT_CONTEXT.md#ssp-field-mapping).

<!-- BEGIN ato-project-context -->
## Project context for learning

Use [the ATO project context](docs/PROJECT_CONTEXT.md) as a starting point for the inherited contextual-learning workflow. The always-apply stub is `.cursor/rules/contextual-learning.mdc`. Before using a lesson, verify the relevant architecture, environment, versions, diagnostic evidence and exclusions against current source and the intended instance. Explain why it applies; skip or narrow mismatches while preserving ATO's safeguards. Distinguish source implementation, installed behavior, test coverage and live qualification. After a meaningful failure or correction, follow the post-fix checklist in that project context. Keep project commands and exceptions here; do not create a second global policy, skill or lesson store, and do not auto-create skills or rules.
<!-- END ato-project-context -->

## Suite terminology

Before changing user-facing wording, follow the shared
[Suite Vocabulary and Object Model](docs/suite-vocabulary-and-object-model.md).
Use the agreed workspace and assistant names, preserve domain distinctions and
existing API/storage contracts, and run `python3 scripts/check_suite_terminology.py`
after UI copy changes. Shared definitions must retain the same version and content
in all three repositories; record local exceptions in
[the terminology audit](docs/suite-terminology-audit.md).

## Shared workspace UI

Read [the authoritative Suite Workspace UI Standard](docs/suite-ui-standard.md)
before UI work. It defines precedence, adaptation, shared appearance and
verification; the HTML companion is illustrative, not an independent authority.
Keep released copies and shared `suite-workspace.css` identical across the suite.
Run `python3 scripts/check_suite_ui.py` and relevant rendered/workflow checks.
Preserve each app's layouts, accessible primitives, features, intended behavior,
draft/review guards and print/export contracts. Document necessary exceptions.
