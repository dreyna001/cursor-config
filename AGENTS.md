# cursor-config

This repository is the canonical source for global Cursor rules/skills and Codex instructions/skills. It is not an application product.

- Cursor loads `rules/*.mdc` from `~/.cursor/rules/` after install. Use the `cursor-rules` skill as the router.
- Codex loads `codex/global-instructions.md` as `~/.codex/AGENTS.md`. Use the `engineering-guidance` skill as the router.
- Install steps and harness details are in [README.md](README.md).
- Keep standing policies aligned in `rules/` and `codex/global-instructions.md` when both harnesses should follow them.

## UI/UX baseline maintenance

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
