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
