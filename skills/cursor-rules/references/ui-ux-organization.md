# UI/UX organization

For UI/UX work, start at the permanent local baseline:
`$HOME/.agents/ui-baseline/README.md` (Windows:
`%USERPROFILE%\.agents\ui-baseline\README.md`). On the current workstation,
open [Windows](C:/Users/Daniel.Reyna/.agents/ui-baseline/README.md) or
`$HOME/.agents/ui-baseline/README.md` (WSL).
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

Use this reference for interface layout, navigation, content hierarchy, and editing-state decisions across UI stacks. Adapt it to the user's task, the product's established patterns, and the available screen space; it guides decisions without prescribing an app-specific flow or feature set.

For compact portals with multiple peer workspaces and no distinct home page, use
[small portal routing](small-portal-routing.md) for route, sign-in, and
remembered-destination decisions.

## Organize around the user's task

- Give the primary task a clear place and hierarchy. Keep closely related context, content, status, and actions together, and avoid repeating the same identity or instruction across neighboring regions.
- Give each explanation one place within a view. Do not repeat the same guidance across tooltips, hints, helper text, banners, and descriptions. Keep required instructions visible near the relevant action; put optional background in one contextual help control. Confirmations and validation messages should add information about the current action or state.
- Each input or required step should contribute directly to the user's outcome or a necessary quality decision. Reuse information already available; do not introduce duplicate entry or intermediate confirmations merely to make the interface appear structured.
- When simplifying an existing interface, account for its fields, actions, and prerequisites before moving them. Preserve functionality and validation or approval gates unless the user explicitly requests a behavior change.
- Keep one coherent navigation hierarchy. Use global navigation for app-wide destinations and workspace navigation for sections within the current task. Avoid multiple persistent rails that repeat destinations or compete for the same space.
- Keep persistent context compact: show the current object or system, its relevant status, and the action needed to orient the user. Put detailed profile, version, or update metadata in a suitable overview or detail area rather than repeating it in the persistent header.
- Choose widths for the content. Keep dense lists and detail forms readable instead of stretching them across an unnecessarily wide workspace. At narrow widths, let related regions stack and keep navigation and actions reachable.

## Keep data and hierarchy clear

- Give each editable value one canonical edit location. Other views can summarize it or link to that location, but should not invite duplicate entry of the same data.
- Preserve an established task or workflow order. Where no order is defined, group items by meaning and use natural ascending numeric order for numbered requirements or sections. Keep custom or unknown items stable instead of silently dropping or arbitrarily reshuffling them.
- Use concise summaries and progressive disclosure for detail. Keep blockers, unmet prerequisites, review decisions, validation errors, and required actions visible in the summary or clearly marked on the collapsed item; do not make the only signal depend on opening it.
- Make drill-down and return paths clear, preserve the selected item and pending edits, and use accessible disclosure controls with keyboard operation and an announced expanded state.
- Describe permissions using roles actually supported by the application. Avoid naming a role that users cannot hold; refer to the responsible team when an action belongs outside the application.
- Name metrics for what they measure. Draft-content completeness describes how much content is present; approval or review status describes a decision. Keep those concepts distinct and explain the basis of a metric when users need it to interpret the value.

## Preserve edits and make actions reachable

- Keep unsaved content visible in its canonical location and identify it as a draft or pending change where that helps users recognize its state.
- When an edit surface closes while changes remain dirty, keep the pending content visible and provide a clear Save action in the workspace. Guard navigation or dismissal that would discard edits with the product's established confirmation behavior.
- Show a repeated warning once when it describes the same cause. Keep separate blockers and distinct required actions visible even when they appear in the same region.
- Keep primary actions near the content they affect and outside nested scroll regions when practical. Avoid placing actions over content; if a layout must keep actions persistently available, ensure they do not obscure reading, focus, or pointer targets.

## Use scrolling deliberately

- Prefer one primary workspace scrollbar. Let long or expandable content extend that scroll area; avoid adding a second vertical scrollbar inside cards or sections. When a growing card pushes a directly related section below the visible work area, a bounded card scroll area can keep both reachable together. Keep its title visible, cap its height relative to the viewport, and preserve normal page scrolling.
- When many cards or sections stack vertically, bound the growing list region only when it would push closely related work out of reach; use a compact list cap and leave the rest of the page scrollable.
- For a selection pane that stacks with related work, use the compact card-list cap as a starting point. When it sits side-by-side and the wider layout benefits from showing more choices, it can grow up to the full document or section-browser cap.
- Choose scroll caps by context rather than applying one height everywhere. Use these as starting points, then adjust for content density, viewport height, and the nearby actions that need to stay visible: compact card lists around `min(24rem, 45dvh)`; large work panes around `min(38rem, 65dvh)`; full document or section browsers up to `min(48rem, 70dvh)`; menus and autocomplete results around `min(20rem, 50dvh)`; dialogs within `calc(100dvh - 2rem)`. Avoid fixed `vh` caps that can consume most of a short viewport.

## Shared UI change completion

Approved shared UI changes are not complete until the versioned baseline,
its visual companion, all three apps (six frontends), this configuration
repository's reference bundle, and the permanent local baseline are synchronized.
Follow the baseline's “Keeping one baseline” procedure, record app-specific
exceptions and validation, and preserve newer approved behavior and styling.
If any part cannot be updated or verified, report the remaining drift explicitly.


For shared visual changes, verify computed form roles, semantic colors, keyboard
selection and control geometry against the central baseline. A passing size-scale
check alone does not establish role parity. Preserve the recorded app exceptions.

Equivalent text roles must share the baseline styling across independent apps.
Check placeholder color/opacity and ordinary label emphasis explicitly; browser
defaults are not a design token. Keep helper, status, metadata and action roles distinct.

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
