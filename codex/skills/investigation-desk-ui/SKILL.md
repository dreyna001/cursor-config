---
name: investigation-desk-ui
description: "Adapt the Enterprise Workspace visual template to an application's actual workflows. Use only when the user explicitly invokes $investigation-desk-ui or names this skill; never auto-select it for ordinary UI work."
---

# Enterprise Workspace UI

For UI/UX work, start at the permanent local baseline:
`$HOME/.agents/ui-baseline/README.md` (Windows:
`%USERPROFILE%\.agents\ui-baseline\README.md`). On the current workstation,
open [Windows](C:/Users/Daniel.Reyna/.agents/ui-baseline/README.md) or
[WSL](/home/dreyna/.agents/ui-baseline/README.md).
If absent, install the versioned `ui-baseline/` bundle from `cursor-config`;
the app's `docs/suite-ui-standard.md` release copy is the fallback. No GitHub
sign-in is required to read the installed reference. This is the single entry
point for shared rules, adaptation, visual examples, exceptions and validation.
Preserve newer approved login/account, sidebar, typography, colors, layouts,
features and intended behavior; older HTML or guidance cannot override them.

Approved shared UI changes are not complete until the versioned baseline,
its visual companion, all three apps (six frontends), this configuration
repository's reference bundle, and the permanent local baseline are synchronized.
Follow the baseline's “Keeping one baseline” procedure, record app-specific
exceptions and validation, and preserve newer approved behavior and styling.
If any part cannot be updated or verified, report the remaining drift explicitly.

This opt-in skill applies the user's preferred visual reference with application-
specific judgment. Read the [visual adaptation contract](references/visual-adaptation.md)
and inspect the [self-contained unified HTML reference](assets/unified-workspace-template.html).
The skill remains explicit-only. Shared UI guidance can express a visual preference
without implicitly invoking this workflow.

## Source of truth

The current reference comes from the October 18, 2026 unified HTML mockup in
`ai-enabled-threathunting`, with cross-application comparisons against ATO.
The user selected source-inspector **B**: compact fields/context and an explicit
Open source action. B is a preferred component pattern, not the name of an entire
application or a prohibition on document viewing.

The central UI/UX baseline owns shared rules; the unified HTML is its generated visual companion. Superseded concept,
refinement and theme templates have been removed. Preserve included font/icon
source notices and licenses when copying assets. Application specifications own
behavior; the visual reference does not grant backend capabilities.

## Adapt, preserve and verify

- Confirm the target repository, scope and requested output. Inspect real screens,
  workflows, shared components, theme and API capabilities before changing them.
- Strongly prefer the reference's visual language for new UI or an authorized
  redesign. Explicit branding/theme decisions take precedence; local fixes stay
  local. Keep one navigation hierarchy, compact context and clear next actions.
- Organize around the destination's tasks. Use readable tables and precise source
  access where they help; retain document viewers, long editors, structured pickers,
  review/diff desks, bulk actions and upload lifecycle when required. The template
  is not a checklist of allowed features or a mandate for one fixed layout.
- Preserve permissions, approvals, canonical content, pending edits, bounded reads,
  exact citations, original files and full exports. Missing data stays unknown.
- Keep the established frontend stack and accessible primitives unless a migration
  is separately requested. Translate tokens and component states; do not blindly
  import global CSS or replace an icon/component library to mimic the HTML runtime.
- Explain material deviations briefly in terms of user benefit. Make routine
  adaptations directly; ask only for unresolved scope/behavior decisions.
- Verify relevant desktop flows: select, inspect, filter/page, follow citations,
  return with context/edits, save/finalize/export and handle errors. Keep heavy raw
  detail lazy. Verify browser/PDF citation parity when applicable; state real limits.

## Domain context

**ATO:** controls, implementation statements, evidence, SSP sections, owners,
review/change decisions and pinned profile/version requirements. Keep essential
system/boundary setup and authoring/approval workflows.

**Incident response:** cases, recorded facts, events/artifacts, ownership,
response decisions and handoff. Preserve action/response approval boundaries.

**Threat hunting/triage:** questions, approved scope, retained results, uncertainty
and source-linked conclusions. Preserve execution and evidence boundaries.

Do not copy domain terminology, sample data, unsupported risk/compliance scores or
fake service behavior merely because the visual example contains it. Use the
[handoff prompt](references/handoff.md) when delegating to another agent.

For shared UI work, complete the central baseline's **Interaction and accessibility**
checks and its role/state coverage record. Exercise keyboard focus and bypass,
modal/popup semantics, disabled/readonly/validation, loading/error announcements,
loading-to-content consistency, field-boundary contrast, and scrolling/enlarged
content in the affected apps. Preserve app-specific guards and layouts. Record
actual browser/route/state evidence and any unverified areas; source parity alone
is not interaction or accessibility sign-off.
