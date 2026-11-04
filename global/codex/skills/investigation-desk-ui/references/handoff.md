# Handoff to another agent

For UI/UX work, start at the `$HOME/.agents/ui-baseline/README.md` (permanent local UI/UX baseline)
(if unavailable, use the app's `docs/suite-ui-standard.md` release copy; no GitHub sign-in is required). It is the single
entry point for shared rules, visual examples, product exceptions and verification.
For maintenance, preserve the current approved appearance. For an explicitly
requested redesign or selected visual reference, follow that reference for the
authorized visual scope; existing styles and older examples must not override it.
Preserve functionality, accessibility, permissions and workflow guards separately.
The baseline's **Design authority and redesign scope** section defines this distinction.

Use **[the user-selected visual reference]** as the visual authority for the
authorized work in **[application/repository]**. Use the released Enterprise
Workspace reference only when the user has not selected another design.
Use the visual reference selected for this task. The historical default does not
override a newer explicit selection.
The released default originated in `ai-enabled-threathunting`, with ATO comparisons; it is not an ATO
workflow specification. Read the accompanying visual adaptation contract.

Match the palette, typography hierarchy, density, spacing and component treatment
within the requested visual scope. Organize the UI around this application's real tasks, roles,
data and existing capabilities. Keep its working framework/accessibility primitives
and map or reuse the selected source styling without legacy theme overrides.

Use compact source-inspector **B** where suitable: concise context/fields,
precise citations, optional technical detail and an explicit Open source action.
Preserve full files/viewing, editors, comparisons, pickers, bulk actions and upload
states when needed. Do not remove functionality just because the sample lacks it.

Preserve permissions, approvals, drafts, canonical records, citations, bounded
paging and full exports. Avoid copying synthetic data, fake statuses or prototype
controls into product behavior. Explain meaningful deviations by their user
benefit; use judgment for routine adaptations without unnecessary approval loops.
Verify the destination's important desktop workflows and report real limits.

## Shared UI change completion

For a shared production rollout, follow the baseline's **Keeping one baseline**
procedure across the versioned standard, companion, all three apps (six frontends),
reference bundle and permanent local baseline. Report unverified scope or drift.
A scoped mockup or guidance-only change does not authorize a production rollout;
label its scope and retain the production baseline until that rollout is requested.


On native Windows, resolve `$HOME/.agents/ui-baseline/` as `%USERPROFILE%\.agents\ui-baseline\`.
