# React Rule

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

When writing React code, make the smallest safe change that preserves the existing architecture, styling, naming, and API contracts. Prioritize readable functional components, typed props, accessible UI, explicit loading/error states, and clean separation between UI, state, and API logic. Add a library only when the current task requires it and existing mechanisms are insufficient. Do not add broad refactors, clever abstractions, unsafe HTML, fake data, or unnecessary hooks.

When changing authentication, API credential forwarding, browser persistence, uploads/previews, or rendering of untrusted content, read [security](security.md) and its matching framework reference. Production response-header and cache policies belong at the actual serving boundary; a layout-only change does not require a security retrofit.
