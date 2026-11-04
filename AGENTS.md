# cursor-config

This repository is the canonical source for global Cursor rules/skills and Codex instructions/skills. It is not an application product.

- Cursor loads `global/rules/*.mdc` from `~/.cursor/rules/` after install. Use the `cursor-rules` skill as the router.
- Codex loads `global/codex/global-instructions.md` as `~/.codex/AGENTS.md`. Use the `engineering-guidance` skill as the router.
- Install steps and harness details are in [README.md](README.md).
- Keep standing policies aligned in `global/rules/` and `global/codex/global-instructions.md` when both harnesses should follow them.

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
