# Suite Workspace UI Standard

Version: **1.4.0** (2026-10-23). Shared by ATO Workspace, Threat Hunt Workspace,
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
- [Navigation](#navigation), [sidebar states](#sidebar-navigation-states),
  [typography](#typography), [account presentation](#shared-sidebar-account-and-text-roles)
  and [sidebar geometry](#shared-sidebar-geometry-and-interaction): normative shared rules.
- [Preservation and palette](#preservation-boundaries-and-shared-palette): the
  current login, account, typography, color and component boundaries.
- [Visual companion](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/design-previews/20261018/unified/visual-reference.html):
  generated HTML examples, embedded contract and exportable reference assets.
- [Vocabulary and object model](suite-vocabulary-and-object-model.md): shared
  names and the distinctions between app-specific states and domain objects.
- Local exceptions and terminology mappings:
  [Hunt](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/docs/suite-terminology-audit.md),
  [ATO](https://github.com/dreyna001/ai-enabled-ato/blob/main/docs/suite-terminology-audit.md),
  [Incident Response](https://github.com/dreyna001/llm_notable_analysis/blob/main/docs/suite-terminology-audit.md).
- [ATO theme mapping](https://github.com/dreyna001/ai-enabled-ato/blob/main/docs/PORTAL_THEME.md):
  product-specific token meanings and preservation boundaries, not another palette specification.
- [Hunt report guidance](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/docs/threat-hunt-reporting-guidance.md):
  report content and export-specific requirements; do not replace them with screen UI rules.
- [Canonical screen stylesheet](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/frontend/src/suite-workspace.css)
  and [source consistency check](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/scripts/check_suite_ui.py):
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
[Hunt AGENTS.md](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/AGENTS.md),
[ATO AGENTS.md](https://github.com/dreyna001/ai-enabled-ato/blob/main/AGENTS.md), and
[Incident Response AGENTS.md](https://github.com/dreyna001/llm_notable_analysis/blob/main/AGENTS.md). Their implementation/testing advice remains applicable, but they do not
carry a parallel palette, typography scale or sidebar specification. The old
Enterprise Workspace adaptation document is a compatibility pointer here.
Read linked product instructions for the current scope; no UI baseline authorizes
changing security, workflow, storage or deployment contracts.

## Authority and scope

This is the **single authoritative UI/UX baseline** for the suite. Its canonical
source is [this file in ai-enabled-threathunting](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/docs/suite-ui-standard.md).
The identical files in ATO and Incident Response are released mirrors, not
independently maintained standards. Read the checked-out release for the app
being changed; do not mix versions from another branch or a newer template.

Order of precedence:

1. Explicit user/customer requirements and the destination app's intended
   behavior, permissions, accessibility needs and domain meaning.
2. This versioned baseline for shared appearance and approved shared UI roles.
3. The [unified HTML visual companion](https://github.com/dreyna001/ai-enabled-threathunting/blob/main/design-previews/20261018/unified/visual-reference.html)
   in the canonical repository, illustrating the same baseline. Its sample
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
the sample. The [suite vocabulary](suite-vocabulary-and-object-model.md) owns
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
- Section / h2 and card titles: **18px**, weight 600, line-height 1.5.
- Subsection / h3: **16px**, weight 600, line-height 1.5.
- Group / h4–h5: **14px**, weight 600. h6: **13px**.
- Body and assistant answers: **14px**. Primary navigation and form controls:
  **13px**. Dense data and secondary metadata: **12px**. Optional captions and
  overlines: **11px**; keep decisions, errors and essential instructions readable.
- **20px** and **24px** are available for emphasis, metrics or document hierarchy,
  not competing page/section title defaults. Keep semantic heading levels valid.
- Use `workspace-page-title` when a page/empty-state title is semantically h2,
  `workspace-section-title` for non-heading card titles, and
  `workspace-toolbar-title` for the **18px** title in a compact assistant toolbar.
  Existing `folio-overline` is an **11px** metadata-label role, even when h2.
- Body text uses line-height 1.55; longer prose can retain its more generous
  line-height. Code and UI use separate font-family tokens.

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
account, typography, sidebar, color or accessibility work. This release makes
no runtime changes to those implementations; the stylesheet version identifies
the consolidated contract, not a redesign.

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
