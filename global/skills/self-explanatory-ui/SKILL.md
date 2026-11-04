---
name: self-explanatory-ui
description: Write and review interface wording so first-time users understand the current view and its actions without knowing internal product terminology.
---

# Self-explanatory UI

For UI/UX work, start at the `$HOME/.agents/ui-baseline/README.md` (permanent local UI/UX baseline)
(if unavailable, use the app's `docs/suite-ui-standard.md` release copy; no GitHub sign-in is required). It is the single
entry point for shared rules, visual examples, product exceptions and verification.
For maintenance, preserve the current approved appearance. For an explicitly
requested redesign or selected visual reference, follow that reference for the
authorized visual scope; existing styles and older examples must not override it.
Preserve functionality, accessibility, permissions and workflow guards separately.
The baseline's **Design authority and redesign scope** section defines this distinction.

Act as a UI clarity reviewer. Read each view as someone encountering
it for the first time.

- Make the current task, relevant content, and next action clear
  within the view itself.
- Use concrete labels. Avoid internal concepts, unexplained product
  personas, and terminology that requires knowledge of another screen.
- Identify AI contributions when their origin matters. Use “AI
  assistant” rather than a product-specific assistant name when that
  makes its role clearer.
- Distinguish saved content, AI suggestions, user edits, and applied
  changes. Do not imply that generated content has been verified.
- Name actions for what they actually do and identify what they affect.
  Preserve distinctions such as applying changes versus approving content.
- Improve existing headings, labels, buttons, and sentences first.
  Remove repetition. Do not compensate for unclear wording by adding
  hints, tooltips, banners, or onboarding text.
- Keep necessary domain terms and precise warnings. Simplification
  must preserve meaning, permissions, and review requirements.

Inspect the rendered view and relevant states when available. Check
whether users can tell what they are seeing, who produced it, what
they should do, and what happens next. Report any inspection limits.

## Shared UI change completion

For a shared production rollout, follow the baseline's **Keeping one baseline**
procedure across the versioned standard, companion, all three apps (six frontends),
reference bundle and permanent local baseline. Report unverified scope or drift.
A scoped mockup or guidance-only change does not authorize a production rollout;
label its scope and retain the production baseline until that rollout is requested.

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

On native Windows, resolve `$HOME/.agents/ui-baseline/` as `%USERPROFILE%\.agents\ui-baseline\`.
