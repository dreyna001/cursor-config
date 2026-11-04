# React Rule

For UI/UX work, start at the permanent local baseline:
`$HOME/.agents/ui-baseline/README.md` (Windows:
`%USERPROFILE%\.agents\ui-baseline\README.md`). On the current workstation,
open [Windows](C:/Users/Daniel.Reyna/.agents/ui-baseline/README.md) or
`$HOME/.agents/ui-baseline/README.md` (WSL).
If absent, install the versioned `ui-baseline/` bundle from `cursor-config`;
the app's `docs/suite-ui-standard.md` release copy is the fallback. No GitHub
sign-in is required to read the installed reference. This is the single entry
point for shared rules, adaptation, visual examples, exceptions and validation.
For maintenance, preserve the current approved appearance. For an explicitly
requested redesign or selected visual reference, follow that reference for the
authorized visual scope; existing styles and older examples must not override it.
Preserve functionality, accessibility, permissions and workflow guards separately.
The baseline's **Design authority and redesign scope** section defines this distinction.

For a shared production rollout, follow the baseline's **Keeping one baseline**
procedure across the versioned standard, companion, all three apps (six frontends),
reference bundle and permanent local baseline. Report unverified scope or drift.
A scoped mockup or guidance-only change does not authorize a production rollout;
label its scope and retain the production baseline until that rollout is requested.

When writing React code, make the smallest coherent change within the requested scope. Preserve API contracts and workflow guards; preserve existing styling and layout during maintenance, but replace them where an authorized redesign calls for it. Prioritize readable functional components, typed props, accessible UI, explicit loading/error states, and clean separation between UI, state, and API logic. Add a library only when the current task requires it and existing mechanisms are insufficient. Do not add broad refactors, clever abstractions, unsafe HTML, fake data, or unnecessary hooks.

When changing authentication, API credential forwarding, browser persistence, uploads/previews, or rendering of untrusted content, read [security](security.md) and its matching framework reference. Production response-header and cache policies belong at the actual serving boundary; a layout-only change does not require a security retrofit.

For frontend performance changes, read [frontend performance](reliability-and-performance.md#frontend-performance), including third-party loading, bundle size, and skeleton states.

## Shared UI change completion


For shared UI work, complete the central baseline's **Interaction and accessibility**
checks and its role/state coverage record. Exercise keyboard focus and bypass,
modal/popup semantics, disabled/readonly/validation, loading/error announcements,
loading-to-content consistency, field-boundary contrast, and scrolling/enlarged
content in the affected apps. Preserve app-specific guards. Preserve layouts outside the authorized redesign scope. Record
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

## Reviewing an existing frontend foundation

When the user requests standardization or architecture review, preservation of
an existing stack is not evidence that it is the best choice. Compare current
implementations with credible alternatives against the actual workflows,
security boundaries, complexity, performance evidence and migration cost.
Record the decision, uncertainty and conditions that would justify revisiting it.
Do not infer quality from one app's incumbent implementation or from popularity.
For the workspace suite, follow the permanent UI/UX baseline's **Foundation
decision review** and shared-foundation contract. Keep apps independently
buildable; cross-repository comparisons are development checks only.
Use the existing source-driven, maintainability, reliability/performance and
testing guidance for relevant concerns; do not create parallel policy skills.
