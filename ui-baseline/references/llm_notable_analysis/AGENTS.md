# Repository guidance

## Agentic incident-investigation workflow

Use the shared [agentic-security-workflows skill](.agents/skills/agentic-security-workflows/SKILL.md)
with its incident-response reference for case evidence, investigation, Q&A and
handoff changes. The source-backed [review backlog](AGENTIC_WORKFLOW_REVIEW.json)
separates all four native products and proposed scope extensions. Preserve
retrieval-bound read-only chat, retired automatic-query boundaries and action gates;
the review does not authorize response execution or deployment.

## Cloud infrastructure policy

Use Terraform exclusively for all new or changed cloud infrastructure. Do not add
or extend SAM, CloudFormation, Bicep, ARM, Pulumi, CDK, console-based provisioning,
or cloud-resource creation scripts. Existing alternate templates are legacy
references; new capabilities and deployment instructions must use the documented
Terraform root. Application builds, artifact publication, and read-only cloud
verification are not infrastructure provisioning. Do not migrate or delete
existing deployed resources without an explicitly scoped migration.

## Generalizable analysis fixes

Analysis, grounding, prompt, skill and reasoning fixes must address a reusable
principle or contract across scenarios and all four products. Treat a failing case
as evidence of a broader failure class, not as a reason to add a special exception
for its hostname, indicator, filename, wording or fixture ID.

Express constraints through the supplied evidence, schema and relationships.
Distinguish observations, inferences, hypotheses and proposed investigations;
missing evidence does not establish a negative fact, and an entity's name does
not establish its properties. Preserve evidence through structured-output handling.
Exact schema and source checks are appropriate when driven by the actual inputs;
do not hardcode the values from an evaluation case into reasoning behavior.

Use specific cases as regression examples. Validate the underlying principle with
varied scenarios and supported/unsupported controls, including supported facts
that must survive. Record the limits of deterministic checks rather than claiming
general reasoning correctness from a finite passing corpus.

## Codex model and subagent routing

Follow the user/session-selected model and reasoning settings and the central Codex model and subagent routing guidance. This repository defines no separate model or delegation override.

## Context-aware learning

Use [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) as a product-specific starting point
for the global contextual-learning workflow, not as authority over current code.
Before reusing a lesson, explain the measured product, architecture, environment,
version and condition matches; verify its diagnostics and exclusions. Skip or
narrow mismatches while preserving this repository's safeguards. Keep local
commands and exceptions in that reference; use the existing global skill/store
and its automatic-saving and review boundaries rather than adding a local skill,
lesson collection or copied global policy.
On repeat integration, update the existing reference and entrypoint in place;
reuse existing lesson IDs rather than creating duplicates.

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

For shared UI work, complete the central baseline's **Interaction and accessibility**
checks and its role/state coverage record. Exercise keyboard focus and bypass,
modal/popup semantics, disabled/readonly/validation, loading/error announcements,
loading-to-content consistency, field-boundary contrast, and scrolling/enlarged
content in the affected apps. Preserve app-specific guards and layouts. Record
actual browser/route/state evidence and any unverified areas; source parity alone
is not interaction or accessibility sign-off.

For desktop zoom and assistant-feedback work, follow the central baseline's
**Desktop zoom and conversational feedback** section. Verify actual browser zoom
separately from root-font resizing, preserve the requested desktop/mobile scope,
and test waiting/error/completion announcements, required states and guarded flows.
Distinguish accessibility-tree evidence from actual screen-reader speech; record
excluded apps and unavailable checks rather than claiming whole-suite coverage.

For UI changes, follow the central baseline's **Workflow and popup regression coverage**.
Verify every dialog's accessible name, all constrained desktop confirmation actions,
popup viewport fit, and relevant delayed/failed-request, retry, duplicate-submit and
unsaved-navigation paths. Preserve each app's guards and desktop/mobile scope;
record actual browser/role/state evidence and synthetic-versus-live test boundaries.
