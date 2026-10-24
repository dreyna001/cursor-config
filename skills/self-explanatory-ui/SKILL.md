---
name: self-explanatory-ui
description: Write and review interface wording so first-time users understand the current view and its actions without knowing internal product terminology.
---

# Self-explanatory UI

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
