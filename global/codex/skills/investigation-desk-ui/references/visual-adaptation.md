# Enterprise Workspace visual adaptation guide

## Single authority

Read the `$HOME/.agents/ui-baseline/README.md` (permanent local Suite Workspace UI Standard) for the
authoritative rules, current version, adaptation boundaries and reconciliation
record. Start locally; if unavailable, use the app's `docs/suite-ui-standard.md`
release copy. Compare versions and preserve newer approved work. ATO and
Incident Response carry identical released mirrors.

The `$HOME/.agents/ui-baseline/visual-reference.html` (unified HTML visual companion) illustrates
the baseline and links back to it. Its embedded copy is generated, not a second
editable specification. App requirements and intended behavior take precedence
as defined by the standard. Historical previews are not current authority.

Preserve accessible behavior, features, identity, permissions, draft/review guards
and exports. Preserve the existing layout for maintenance; an authorized redesign
may replace layout and styling using the selected reference. For new
enterprise work, use the same visual language with product-specific judgment.
Use the selected reference CSS or an exact token mapping where appropriate;
isolate it from conflicting legacy skins. Never import synthetic behavior as a
replacement for real product functionality. Shared-rule changes belong in the canonical standard and
stylesheet, followed by regenerated/released copies and rendered verification.

## Shared UI change completion

For a shared production rollout, follow the baseline's **Keeping one baseline**
procedure across the versioned standard, companion, all three apps (six frontends),
reference bundle and permanent local baseline. Report unverified scope or drift.
A scoped mockup or guidance-only change does not authorize a production rollout;
label its scope and retain the production baseline until that rollout is requested.


For shared visual changes, verify computed form roles, semantic colors, keyboard
selection and control geometry against the applicable visual authority, including an explicitly selected redesign reference. A passing size-scale
check alone does not establish role parity. Preserve the recorded app exceptions.

Equivalent text roles must share the applicable design styling across independent apps.
Check placeholder color/opacity and ordinary label emphasis explicitly; browser
defaults are not a design token. Keep helper, status, metadata and action roles distinct.

On native Windows, resolve `$HOME/.agents/ui-baseline/` as `%USERPROFILE%\.agents\ui-baseline\`.
