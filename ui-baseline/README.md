# Suite Workspace UI Standard

> **Permanent local edition · v1.7.0 · 2026-10-23**
>
> Start here on Windows: `C:\Users\Daniel.Reyna\.agents\ui-baseline\README.md`.
> WSL opens the same files through `/home/dreyna/.agents/ui-baseline/README.md`.
> This folder is outside project checkouts and temporary worktrees. No GitHub sign-in
> is needed to read this baseline, its visual companion or the linked core references.
>
> [Alignment analysis and verification](verification.md) ·
> [Offline visual companion](visual-reference.html) ·
> [Unmodified published baseline](references/ai-enabled-threathunting/docs/suite-ui-standard.md) ·
> [Release provenance and checksums](manifest.json)
>
> This is the local reading edition of the published standard, with local navigation.
> Shared-rule changes still belong in the versioned suite release. When an app has a
> newer approved release, compare its changes before refreshing this folder; never
> downgrade newer login, account, sidebar, typography, color, layout or workflow work.

Version: **1.7.0** (2026-10-23). Shared by ATO Workspace, Threat Hunt Workspace,
and Incident Response Workspace, including its four deployment variants.

## Start here: the UI/UX index

This page is the central entry point for **all UI/UX work**. UI-related skills,
rules, templates and repository instructions must send readers here first.
The linked supporting material keeps its narrower purpose; it is not a second
source of shared rules.

- [Authority and scope](#authority-and-scope): precedence and preservation of
  each app's intended behavior, layouts, features and newer approved work.
- [Visual adaptation](#visual-adaptation): how to use the common design language
  without importing prototype behavior or replacing an established stack.
- [Motion and reduced motion](#motion-and-reduced-motion): timings, feedback roles, popup scope and validation.
- [Navigation](#navigation), [sidebar states](#sidebar-navigation-states),
  [typography](#typography), [account presentation](#shared-sidebar-account-and-text-roles)
  and [sidebar geometry](#shared-sidebar-geometry-and-interaction): normative shared rules.
- [Preservation and palette](#preservation-boundaries-and-shared-palette): the
  current login, account, typography, color and component boundaries.
- [Visual companion](visual-reference.html):
  generated HTML examples, embedded contract and exportable reference assets.
- [Vocabulary and object model](references/ai-enabled-threathunting/docs/suite-vocabulary-and-object-model.md): shared
  names and the distinctions between app-specific states and domain objects.
- Local exceptions and terminology mappings:
  [Hunt](references/ai-enabled-threathunting/docs/suite-terminology-audit.md),
  [ATO](references/ai-enabled-ato/docs/suite-terminology-audit.md),
  [Incident Response](references/llm_notable_analysis/docs/suite-terminology-audit.md).
- [ATO theme mapping](references/ai-enabled-ato/docs/PORTAL_THEME.md):
  product-specific token meanings and preservation boundaries, not another palette specification.
- [Hunt report guidance](references/ai-enabled-threathunting/docs/threat-hunt-reporting-guidance.md):
  report content and export-specific requirements; do not replace them with screen UI rules.
- [Canonical screen stylesheet](references/ai-enabled-threathunting/frontend/src/suite-workspace.css)
  and [source consistency check](references/ai-enabled-threathunting/scripts/check_suite_ui.py):
  implementation and release checks for this contract.
- [Maintenance and verification](#keeping-one-baseline): release copies,
  generated templates, browser checks and local/CI qualification boundaries.
- [Reconciliation record](#reconciliation-record--2026-10-23): resolved conflicts
  and why older template/theme instructions no longer override this version.

## Skill and rule routing

The installed **React**, **Development Stack**, **Self-explanatory UI**,
**Codex Rules** / **Engineering Guidance** routers, the explicitly invoked
**Investigation Desk UI** workflow, and each app's `AGENTS.md` point here first.
Installed skill entrypoints are `$HOME/.agents/skills/<skill-name>/SKILL.md`;
Windows uses the corresponding `%USERPROFILE%/.agents/skills/` location.
Global entrypoints are `$CODEX_HOME/AGENTS.md` and the installed Cursor
`react` / `ui-ux-organization` rules. Product-specific entrypoints are
[Hunt AGENTS.md](references/ai-enabled-threathunting/AGENTS.md),
[ATO AGENTS.md](references/ai-enabled-ato/AGENTS.md), and
[Incident Response AGENTS.md](references/llm_notable_analysis/AGENTS.md). Their implementation/testing advice remains applicable, but they do not
carry a parallel palette, typography scale or sidebar specification. The old
Enterprise Workspace adaptation document is a compatibility pointer here.
Read linked product instructions for the current scope; no UI baseline authorizes
changing security, workflow, storage or deployment contracts.

## Authority and scope

This is the **single authoritative UI/UX baseline** for the suite, available
here as a permanent local reading edition. Its versioned source is the
[published suite standard](references/ai-enabled-threathunting/docs/suite-ui-standard.md).
The identical files in ATO and Incident Response are released mirrors, not
independently maintained standards. Start here, then compare the app's checked-out
release when implementing changes; do not mix versions or downgrade newer approved work.

Order of precedence:

1. Explicit user/customer requirements and the destination app's intended
   behavior, permissions, accessibility needs and domain meaning.
2. This versioned baseline for shared appearance and approved shared UI roles.
3. The [unified HTML visual companion](visual-reference.html)
   in this local bundle, illustrating the same baseline. Its sample
   layout, synthetic content and prototype interactions are not product features.
4. App theme notes, general skills and older previews. They must link here and
   cannot silently override the current baseline.

The visual companion links back here and embeds this document's current text.
The personal React/Development Stack skills route through the adaptation guide,
which links to this authority. The companion and its current distributed copies
are generated artifacts. Preserve dated historical prototypes and release evidence.

Shared appearance does not require identical pages, navigation structures,
component libraries, control dimensions, table density, dialogs or workflow order.
Keep layouts, available features, event handlers, draft/review guards, identity,
backend contracts and export content unchanged during a visual alignment.
Document necessary exceptions alongside this contract; a visual mismatch alone
does not authorize a functional change or a deployment.

## Visual adaptation

The October 18, 2026 unified Threat Hunting HTML and ATO comparisons established
the suite's visual direction. The selected source-inspector pattern B means
compact source fields, visible citation/context, optional technical detail and
an Open source action. It is one reusable pattern, not a mandatory page layout.
Retain document/PDF/image viewers, long editors, comparison desks, structured
pickers, bulk actions and upload progress wherever the app needs them.

Use the destination's established React, Tailwind, Radix and icon primitives.
Native HTML and Phosphor assets in the companion are examples, not replacement
dependencies. Translate semantic roles: the companion's accent token is a primary
action, while an app's accent token may be a hover fill. Scope screen CSS; do not
paste prototype print rules over application exports. Keep full original evidence,
precise citations, paging, approval boundaries and genuine loading/error states.
Never invent scores, health checks, identities or service capabilities to match
the sample. The [suite vocabulary](references/ai-enabled-threathunting/docs/suite-vocabulary-and-object-model.md) owns
terminology and domain distinctions; wording skills support that contract.

## Navigation

- Expanded primary sidebar: **256px / 16rem**, including padding and border.
- Horizontal sidebar padding: **16px / 1rem per side**. Row padding is separate.
- Use `--workspace-sidebar-width` and `--workspace-sidebar-padding-inline` in
  `src/suite-workspace.css`; keep the sidebar from shrinking and the main region
  able to shrink with `min-width: 0` or `minmax(0, 1fr)`.
- Keep the expanded width consistent across desktop widths. Do not silently
  narrow it at 1250px. Contextual inspectors and document trees are separate.
- Preserve vertical navigation scrolling, reachable footer actions, keyboard
  focus, readable wrapped labels and the full accessible name of truncated items.

## Sidebar navigation states

- Mark primary navigation rows with `workspace-nav-item` and let the existing
  router set `aria-current="page"` on the selected destination. Do not infer the
  current item from its label, DOM position or a separate visual-only flag.
- Selected row: **#1B304B** fill, **#C2D5EF** text and icons, **4px** corners,
  weight **500**, and a transparent border. Do not add a bright border, stripe,
  glow or saturated blue link text. Keep existing row geometry and badges.
- Unselected hover: **#161F2C** fill and **#CBD8E8** text/icons. A selected row
  retains its selected colors on hover. Icons inherit the row color; semantic
  badge/status colors remain independent.
- Keyboard focus is separate from selection: retain a visible **2px #8CBCFF**
  outline with **2px** offset. Never remove focus merely because a row is selected.
- Use `--workspace-nav-selected-*`, `--workspace-nav-hover-*`,
  `--workspace-nav-focus` and `--workspace-nav-radius` from the shared CSS.
  These dark-theme colors follow the verified ATO treatment; customer themes
  or accessibility requirements may override the semantic tokens deliberately.
- Verify selected, selected-hover, unselected-hover and keyboard-focus states,
  including icons, after navigation in Chromium, Firefox and WebKit. Selection
  styling must not change routes, draft guards, approvals or enabled actions.

## Typography

- UI: **Public Sans**, bundled locally at weights **400, 500, 600, 700**, with
  Source Sans Pro and system sans-serif fallbacks. Keep the bundled OFL license.
- Code, queries, raw values and identifiers: **SFMono-Regular, Consolas,
  Liberation Mono, monospace**, in that order. This is one shared platform
  fallback stack, not a promise of the same installed monospace face on every OS.
- Browser UI size scale: **11, 12, 13, 14, 16, 18, 20, 24, 28px** at a 16px root.
  Use the matching `--workspace-font-size-*` rem token. Avoid one-off sizes,
  fractional rem approximations, and a smaller font to force a label to fit.
- Page title / h1: **28px**, weight 600, line-height 1.3.
  ATO’s Create System Workspace title uses this page-title role, even though
  its form is inside a card. Ordinary card and section titles remain 18px.
- Section / h2 and card titles: **18px**, weight 600, line-height 1.5.
- Subsection / h3: **16px**, weight 600, line-height 1.5.
- Group / h4–h5: **14px**, weight 600. h6: **13px**.
- Body, assistant answers and entered form values: **14px**. Primary navigation
  and field labels: **13px**. Compact action text, dense data and secondary
  metadata: **12px**. Optional captions and
  overlines: **11px**; keep decisions, errors and essential instructions readable.
- **20px** and **24px** are available for emphasis, metrics or document hierarchy,
  not competing page/section title defaults. Keep semantic heading levels valid.
- Use `workspace-page-title` when a page/empty-state title is semantically h2,
  `workspace-section-title` for non-heading card titles, and
  `workspace-toolbar-title` for the **18px** title in a compact assistant toolbar.
  Existing `folio-overline` is an **11px** metadata-label role, even when h2.
- Body text uses line-height 1.55; longer prose can retain its more generous
  line-height. Code and UI use separate font-family tokens.

## Shared form text and color roles

Each application owns its local stylesheet, fonts, dependencies and build. Matching
CSS token names and values are a design contract, not a shared runtime library.
No app imports from another app repository or needs another checkout to build or
deploy. The baseline/configuration bundle is documentation and validation material;
it is not a runtime dependency of any app.

- Textual input values, native/custom select values, placeholders and ordinary
  textarea content use **14px** (`--workspace-font-field`). Form labels use
  **13px** (`--workspace-font-label`), weight **500**, color **#BBC6D3**. Entered
  values use weight **400**. Equivalent text roles share family, size, weight and
  color across apps; different wording is appropriate when the domain task differs.
- Placeholder and input-hint text use **#8B949E** at opacity **1** through
  `--workspace-color-placeholder`, including custom combobox placeholders. Do not
  rely on browser defaults or app-local gray values. Disabled controls retain
  their existing component-level dimming; placeholder glyph opacity does not
  override a disabled control’s opacity. The standard dark field
  surfaces provide at least 4.5:1 text contrast; verify the computed colors.
- Compact action text retains **12px** (`--workspace-font-action`) to preserve
  the existing button widths and density. Sidebar navigation/account roles remain
  separately specified. Do not force table-cell links or metadata to form sizes.
- Preserve control height, padding, border radius, layout grids, scroll regions,
  validators, selection, disabled/read-only state and all submit/draft guards.
  Inputs/selects retain a scalable 20px line box; long-editor/composer line heights
  and explicit content/identifier monospace roles remain app-owned.
- Checkboxes, radios, range/color/file pickers and hidden controls retain their
  native geometry. Code/identifier editors marked `.vs-code`, `.font-mono` or
  `data-workspace-text-role="code"` keep their explicit code typography. Metadata
  labels may use `data-workspace-text-role="metadata"` when that is their real role.
  A label acting as an upload/action control uses `data-workspace-text-role="action"`
  and retains its action styling. Do not use either marker to bypass ordinary
  field-label parity. Helper descriptions remain muted and semantic status text
  retains its meaning; they are different roles, not alternate field-label styles.
- Common page/raised surfaces, body/heading/muted text, borders, primary actions
  and links use `--workspace-color-*` from the shared stylesheet. Ordinary titles
  use the heading color. Explicit muted/overline and semantic warning/error/success
  headings retain their meaning; contextual component surfaces are not page backgrounds.
- Keep **Hunts selected on New Hunt** using the existing parsed route. This is a
  current-destination indicator only; callbacks, draft protection and URLs stay intact.

The 14px field role follows the [Fluent web typography scale](https://fluent2.microsoft.design/typography)
as a readable compact-UI choice, not a claim that WCAG mandates a pixel size.
Use relative units and verify [200% text resizing](https://www.w3.org/WAI/WCAG22/Understanding/resize-text)
without losing content or functionality. Avoid shrinking text to force content to fit.

## Motion and reduced motion

Motion is a shared contract, not an implicit framework default. The earlier
parity checks verified appearance and interaction states but did not establish
motion parity. This section closes that gap without changing layouts or workflows.

- Equivalent hover/selection color transitions and disclosure rotations use
  **150ms**, **cubic-bezier(0.4, 0, 0.2, 1)**, and **no delay** through
  `--workspace-motion-duration` and `--workspace-motion-ease`.
- Interpolate only color, background, border, shadow and opacity for ordinary
  controls. Disclosure indicators may rotate; never animate widths, heights,
  spacing, page layout, or workflow completion to manufacture visual parity.
- Keyboard focus indicators appear immediately. Preserve focus rings, outlines,
  final selected/open states and existing accessible names.
- Existing popup enter/exit effects use the same 150ms/easing contract. Mark
  portalled content `workspace-motion-surface workspace-motion-overlay` so its
  transitions are covered outside the main workspace wrapper. Do not introduce
  popup effects or new open/close behavior where none exists.
- Loading spinners use **1s linear**; skeleton/loading pulses use **2s** with
  **cubic-bezier(0.4, 0, 0.6, 1)**. Use the shared spinner/pulse tokens and roles;
  do not add loading animations or loading delays to otherwise static controls.
- IR's existing typing dots retain their distinct **1.2s ease-in-out** cycle and
  **120ms** stagger through `--workspace-motion-typing-duration`. This is a
  documented feedback role, not a different speed for the same ordinary control.
- With `prefers-reduced-motion: reduce`, disable CSS animations, transitions and
  smooth scrolling across the app, including portals and pseudo-elements. Keep
  loading/status content visible and final disclosure/selection states intact;
  typing dots become static. Honor preference changes without a reload. Do not
  change API calls, polling, request cancellation, timers or measurement frames.
- Verify both preference modes in Chromium, Firefox and WebKit. Check actual
  navigation/disclosure roles, keyboard focus, portal scope, loading indicators,
  unchanged geometry, and restoration when the preference changes back. Include
  an explicit motion inventory and results; matching screenshots or source hashes
  alone cannot establish animation parity.

The preference follows [MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)
and [WCAG animation from interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html).
These checks are not a claim of complete accessibility certification.

Parity sign-off must identify which roles were measured: typography, palette,
spacing, hover/selection, keyboard focus, disabled/loading states, overlays,
motion and reduced motion. Record each as verified, an intentional exception,
or unverified. Do not turn a source-hash match or a static screenshot check into
a claim that every interaction and motion state was exercised.

## Scope and maintenance

The versioned `src/suite-workspace.css` is identical across all six frontend
builds; copy deliberate shared changes together. The visual companion and adaptation guide point to this baseline.
Explicit customer branding, accessibility/localization requirements and measured
workflow needs may justify a documented exception. Logo artwork, print/PDF sizing,
and authored document typography have their own contracts; preserve complete
content, citations, approvals, drafts and export behavior.

For a visual change, verify computed sidebar dimensions, padding, loaded fonts,
heading roles, allowed text sizes, focus and contained overflow at **1280, 1440
and 1920px**, plus enlarged text. Use Chromium, Firefox and WebKit when available.
Keep tests on synthetic API/identity fixtures separate from live-stack claims.
Run the relevant frontend unit tests, build/type checks, and existing workflow
regressions. A syntax check alone does not prove rendered consistency.

## Shared sidebar account and text roles

- Use the same sidebar UI family and roles across all six frontend builds:
  Public Sans; navigation 13px/400 (selected 500); group labels 11px/600;
  secondary text 12px/400; text-based brand names 14px/600. Logo artwork is unchanged.
- Keep the account control below scrolling navigation. Use a neutral 32px initials
  avatar, 13px/600 display name, 12px/400 Account label, and upward chevron in one
  56px row. Preserve the full accessible name when the visible name truncates.
- Open account details and Sign out above the row. Escape closes and restores
  trigger focus; outside interaction closes the panel. Keep existing app-specific
  authentication, sign-out and draft-protection callbacks. Do not invent identity,
  email, role or shared sign-on behavior when a session does not provide it.
- The sidebar contract does not authorize changing navigation destinations,
  logos, main-content typography or print/export sizing.

## Shared sidebar geometry and interaction

- Use #10141A sidebar surfaces and #30363D dividers. Primary navigation icons
  use 16px boxes. Domain-specific badges, status markers, logo artwork and
  disclosure controls keep their own meaning and sizing.
- Navigation rows use a 40px minimum height, 8px vertical / 12px horizontal
  padding, a 10px icon gap, 20px line height and 4px spacing in plain row stacks.
  These dimensions scale with the user's root text size; rows may grow for labels.
- Brand slots use an 80px height and 8px internal horizontal inset within the
  existing 16px sidebar gutter. Preserve each logo's artwork and intrinsic size.
  Footers use a divider and 16px vertical padding around existing app content.
- Keep the account control reachable when navigation overflows. Hunt navigation
  scrolls separately from its account footer. Incident Response retains separate
  primary navigation and conversation-history regions; ATO retains its system
  selector, work/context groups, assistant action and human-review notice.
- Account panels share Enter/Space opening, Escape dismissal with trigger focus,
  outside dismissal, and Tab/Shift+Tab continuation from the trigger in document
  order. Show the supplied secondary identifier consistently without changing
  its source or the app's authentication and sign-out behavior.
- Intentional routing exceptions: Hunt keeps callback-based navigation buttons
  and its existing draft guards. ATO workflow-view buttons retain revision/draft
  guards. Incident Response and ATO route links retain normal browser link
  behavior. Do not convert guarded actions into links solely for visual parity.

## Preservation boundaries and shared palette

The latest approved implementation is the preservation baseline for this
reconciliation. An older HTML snapshot must never overwrite newer login,
account, typography, sidebar, color or accessibility work. Version 1.5 aligns the explicitly approved form-text roles and New Hunt
selection while retaining those implementations and their layout/behavior contracts.

- Preserve login routes, local/Entra authentication, identity claims and display
  fallbacks, account controls, session handling, sign-out and draft guards.
- Preserve the sidebar geometry, font family/roles, selection/hover/focus and
  account rules above. All six runtime stylesheets carry the same rules.
- Preserve the current dark screen palette: canvas #0D1117, raised surface
  #161B22, body #BBC6D3, heading #E6EDF3, muted text #8B949E, border #30363D,
  primary action #1F6FEB with white text, and link/focus #8CBCFF. Sidebar roles
  use their dedicated values above; do not replace them with old theme values.
- Map semantic roles, not raw variable names: `accent` can mean primary action
  in the HTML and hover fill in an app. Status colors retain domain meanings.
- Existing button/input dimensions, corner radii, contextual fills and focus
  primitives remain app-owned where a newer shared rule has not been approved.
  For example, ATO's secondary hover and Incident Response's contextual input
  surfaces must not be replaced just to reproduce an earlier template.
- Login pages, editors, tables, dialogs, inspectors and reports retain their
  established layouts and interactions. App/document-specific typography and
  print/PDF rules remain explicit exceptions to ordinary screen text roles.

Further control-level alignment requires evidence from the current rendered
apps and an intentional update to this contract. A difference by itself is not
proof of a bug or permission to copy an older declaration.

## Keeping one baseline

### Approved shared UI changes: completion gate

An approved shared UI change is incomplete until these are synchronized:

1. Update the versioned suite baseline and shared stylesheet together where the
   approved change affects their contract; keep the same released version across
   Threat Hunting, ATO and all four Incident Response frontends.
2. Regenerate the HTML companion and update the three app release copies,
   terminology/theme exceptions and supporting references affected by the change.
   Preserve newer approved login/account flows, spacing, typography, colors,
   layouts, features and application-specific behavior.
3. Refresh `ui-baseline/` in the `cursor-config` repository from those verified
   releases, including this local reading edition, source snapshots, provenance
   hashes and the alignment/validation record. Keep skills and rules pointing here;
   do not create a competing numeric specification in a skill or template.
4. Validate the bundle and all three app releases with
   `python3 scripts/sync_ui_baseline.py check --app-root <hunt> --app-root <ato>
   --app-root <incident> --ref origin/main` from `cursor-config`. Fetch the intended
   approved refs first; use the working-tree default before a release is merged.
   Run each app's existing source consistency checks and the rendered/workflow
   checks required by the changed UI behavior. Record results and any deliberate
   app-specific exception; fixture tests do not prove live identity deployment.
5. Run `python3 scripts/sync_ui_baseline.py install` to refresh the permanent
   user-profile copy, then `check --installed`. On this workstation, the WSL
   path aliases the Windows folder, so update that shared physical copy once.
   When Windows and WSL use separate copies, update and verify both.

Do not declare shared UI work complete while an app, the versioned bundle or an
installed copy still carries stale shared rules. If a release or verification is
blocked, report precisely what remains out of sync. App-only behavior changes do
not require forcing unrelated parity; record an exception when they affect a
shared rule. These instructions do not grant new deployment or merge permission.

Edit this canonical document and canonical `frontend/src/suite-workspace.css`
together when a shared rule changes. Bump both versions, publish identical
released copies to the other five frontends and two repositories, and regenerate
the visual companion with `python3 design-previews/20261018/unified/build-visual-reference.py`.
Copy that generated companion to the current ATO reference and installed personal
template. The adaptation guide and skills contain routing/scope guidance, not
parallel numeric specifications. App theme documents record mappings/exceptions
and link here rather than repeating the palette, font scale or sidebar geometry.

Run `python3 scripts/check_suite_ui.py` in each repo. Add `--peer <repo-root>`
for the other two repos to verify released document/CSS/reference parity. This
check proves source consistency, not usability: also run the existing rendered
suite checks and app workflow regressions described above. Preserve the root
text-size behavior and existing control bounding boxes when aligning decoration.

## Reconciliation record — 2026-10-23

- The HTML embedded an older adaptation text while the installed adaptation
  guide and suite document had advanced independently. The versioned suite
  document now owns the rules; the HTML is generated with its text and backlink.
- Earlier ATO notes specified a 208px sidebar and Roboto Mono. The later approved
  256px sidebar and shared typography above take precedence for screen UI.
  Authored documents and exports retain their separate requirements.
- Old template navigation used 18px icons and different spacing/selection colors.
  The approved v1.3.0 sidebar/account rules above remain unchanged.
- Equivalent action primitives have some app-specific decoration. v1.4.0
  preserves their latest approved implementations instead of restoring older
  template values; future alignment must be supported by rendered evidence.
- Legacy claims that the HTML alone is the source of truth are superseded by
  the authority order above. Historical snapshots describe their original release.

## Form and palette alignment — 2026-10-23

The cross-app visual comparison found 12/13/14px form values and an unselected
New Hunt parent destination. Version 1.5 makes the form-value/label/compact-action
roles explicit, keeps the current layout and action density, and selects the
existing Hunts destination during creation. The already-matching page, surface,
heading and text palette now references the same shared tokens. Existing app
workflows, contextual surfaces, statuses, account and login behavior are preserved.

## Shared text-role alignment — 2026-10-23

Version 1.6 removes browser-default placeholder gray and aligns ordinary label
color/weight across the six independent frontends. It preserves text content,
control geometry, app workflows, identity handling and contextual status colors.
The ATO creation-page title noted in the follow-up audit is a separate unresolved
page-title mapping issue; this release does not silently redefine that role.

## Patch correction — v1.6.1

ATO’s creation page now uses its existing 28px page-title role instead of the
18px card-title role. This corrects the mapping only; no shared color, font,
spacing, layout, form behavior or other app presentation is changed.
