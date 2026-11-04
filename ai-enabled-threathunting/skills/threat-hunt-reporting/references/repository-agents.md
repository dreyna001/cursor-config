# Repository guidance

## Agentic threat-hunting workflow

Use the installed `agentic-security-workflows` skill at
`${HOME}/.agents/skills/agentic-security-workflows/SKILL.md` and its
`references/threat-hunting.md` for agentic capability, evidence, approval and
analyst-workflow changes. Use the [project README](README.md#current-status) for current status and the
[operator runbook](docs/operator-runbook.md) for operational gates. Documentation
does not change the active engine, execution scope, limits or approval requirements.

## Codex model and subagent routing

Follow the user/session-selected model and reasoning settings and the central Codex model and subagent routing guidance. This repository defines no separate model or delegation override.

## Project context and conditional learning

Use the global contextual-learning workflow only when relevant, checking current
source, environment, versions and exclusions before applying a lesson. Current
operational instructions belong in [the runbook](docs/operator-runbook.md);
current implementation status belongs in [the README](README.md#current-status).
This grants no application, deployment, access or external-action authority.

## Threat-hunt reporting

- When creating or changing hunt report content or presentation, follow
  [threat-hunt reporting guidance](docs/threat-hunt-reporting-guidance.md).
- Use the `threat-hunt-reporting` skill when installed. Keep factual assessments,
  approved scope, evidence provenance and event timelines distinct from model
  confidence, investigation operations and presentation conventions.
- For changes to either the browser Report or PDF export, apply the
  [paired browser/PDF review gate](docs/threat-hunt-reporting-guidance.md#paired-browserpdf-review-gate).
  Explicitly assess the other surface in the PR, update it when needed, and
  verify generated PDFs before merging export changes. Record justified
  medium-specific differences and any deferred parity work in the project queue.

## UI verification

- Test this application at desktop viewport sizes only. Do not run mobile viewport checks, device emulation, mobile screenshot capture, or mobile-specific development unless the user explicitly requests it.
- Keep browser regression tests and ad hoc verification desktop-only. Preserve historical mobile artifacts as evidence; do not rerun them.

## Suite terminology

Before changing user-facing wording, follow the shared
[Suite Vocabulary and Object Model](docs/suite-vocabulary-and-object-model.md).
Use the agreed workspace and assistant names, preserve domain distinctions and
existing API/storage contracts, and run `python3 scripts/check_suite_terminology.py`
after UI copy changes. Shared definitions must retain the same version and content
in all three repositories; record local exceptions in
[the documentation index](docs/README.md).

## Shared workspace UI

Read [the authoritative Suite Workspace UI Standard](docs/suite-ui-standard.md)
before UI work. It defines precedence, adaptation, shared appearance and
verification; the shared stylesheet and actual application provide the maintained visual implementation.
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

For every UI/UX change, use Playwright to verify the affected surface and follow the central baseline's **Workflow and popup regression coverage**.
Verify every dialog's accessible name, all constrained desktop confirmation actions,
popup viewport fit, and relevant delayed/failed-request, retry, duplicate-submit and
unsaved-navigation paths. Preserve each app's guards and desktop/mobile scope;
record actual browser/role/state evidence and synthetic-versus-live test boundaries.

For shared frontend architecture changes, follow the baseline's **Shared frontend
foundations and independent deployment** and **Foundation decision review**.
Run `scripts/check_suite_foundation.py` as well as the UI/workflow checks.
Treat the current implementation as a reviewed default, not proof of optimality;
record evidence, alternatives and intentional domain adapters. Each app must
remain buildable and deployable without another application's checkout.
