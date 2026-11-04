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

Preserve the destination's layout, accessible primitives, component stack,
features, identity, permissions, draft/review guards and exports. For new
enterprise work, use the same visual language with product-specific judgment.
Do not paste prototype CSS or sample behavior into an app as a replacement for
its implementation. Shared-rule changes belong in the canonical standard and
stylesheet, followed by regenerated/released copies and rendered verification.

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

On native Windows, resolve `$HOME/.agents/ui-baseline/` as `%USERPROFILE%\.agents\ui-baseline\`.
