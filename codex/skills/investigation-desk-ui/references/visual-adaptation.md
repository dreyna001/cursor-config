# Enterprise Workspace visual adaptation guide

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

The baseline owns numeric rules and precedence. Use its linked HTML companion
for examples; app theme documents record mappings and deliberate exceptions.
Preserve the destination's layout, accessible primitives, component stack,
features, identity, permissions, draft/review guards and exports. Do not paste
prototype CSS or sample behavior over the approved application implementation.

For shared visual changes, verify computed form roles, semantic colors, keyboard
selection and control geometry against the central baseline. A passing size-scale
check alone does not establish role parity. Preserve the recorded app exceptions.

Equivalent text roles must share the baseline styling across independent apps.
Check placeholder color/opacity and ordinary label emphasis explicitly; browser
defaults are not a design token. Keep helper, status, metadata and action roles distinct.
