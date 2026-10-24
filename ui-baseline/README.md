# Suite Workspace UI Standard

> **Permanent local edition · v1.14.0 · 2026-10-24**
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

Version: **1.14.0** (2026-10-24). Shared by ATO Workspace, Threat Hunt Workspace,
and Incident Response Workspace, including its four deployment variants.

## Start here: the UI/UX index

This page is the central entry point for **all UI/UX work**. UI-related skills,
rules, templates and repository instructions must send readers here first.
The linked supporting material keeps its narrower purpose; it is not a second
source of shared rules.

- [Authority and scope](#authority-and-scope): precedence and preservation of
  each app's intended behavior, layouts, features and newer approved work.
- [Shared components and drift prevention](#shared-components-and-drift-prevention): canonical source, approved variants and automated parity gates.
- [Shared frontend foundations](#shared-frontend-foundations-and-independent-deployment): routing, transport, state, forms, validation and standalone builds.
- [Frontend stack and Python compatibility](#frontend-stack-and-python-compatibility): current pins, toolchain alignment and documented holds.
- [Visual adaptation](#visual-adaptation): how to use the common design language
  without importing prototype behavior or replacing an established stack.
- [Interaction and accessibility](#interaction-and-accessibility): keyboard,
  dialogs, feedback states, control contrast and scrolling checks.
- [Workflow and popup regression coverage](#workflow-and-popup-regression-coverage): failure paths, dialog names and constrained desktop actions.
- [Desktop zoom and conversational feedback](#desktop-zoom-and-conversational-feedback): native zoom, reflow, reply announcements and required states.
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

This is the **single authoritative UI/UX baseline** for the suite. Its canonical
source is [this file in ai-enabled-threathunting](README.md).
The identical files in ATO and Incident Response are released mirrors, not
independently maintained standards. Read the checked-out release for the app
being changed; do not mix versions from another branch or a newer template.

Order of precedence:

1. Explicit user/customer requirements and the destination app's intended
   behavior, permissions, accessibility needs and domain meaning.
2. This versioned baseline for shared appearance and approved shared UI roles.
3. The [unified HTML visual companion](visual-reference.html)
   in the canonical repository, illustrating the same baseline. Its sample
   layout, synthetic content and prototype interactions are not product features.
4. App theme notes, general skills and older previews. They must link here and
   cannot silently override the current baseline.

The visual companion links back here and embeds this document's current text.
The personal React/Development Stack skills route through the adaptation guide,
which links to this authority. The companion and its current distributed copies
are generated artifacts. Preserve dated historical prototypes and release evidence.

Shared appearance does not require identical pages, navigation structures,
component compositions, table density, specialized inspectors or workflow order.
Equivalent ordinary controls use the shared component contract below.
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

Use the shared suite React/Radix component source and the destination's established
Tailwind and icon integration.
Native HTML and Phosphor assets in the companion are examples, not replacement
dependencies. Translate semantic roles: the companion's accent token is a primary
action, while an app's accent token may be a hover fill. Scope screen CSS; do not
paste prototype print rules over application exports. Keep full original evidence,
precise citations, paging, approval boundaries and genuine loading/error states.
Never invent scores, health checks, identities or service capabilities to match
the sample. The [suite vocabulary](references/ai-enabled-threathunting/docs/suite-vocabulary-and-object-model.md) owns
terminology and domain distinctions; wording skills support that contract.

## Shared components and drift prevention

Version 1.12 adopts the approved component choices across **all six frontends**.
The canonical source is Hunt's `frontend/src/components/ui/`; the same files and
`src/lib/utils.ts` are mirrored byte-for-byte into ATO and all four IR builds.
The checked [component contract](references/ai-enabled-threathunting/docs/suite-component-contract.json) records the file
hashes. These files are one suite release, not six independently evolving forks.

- **Buttons:** IR's 37px default height and 6px radius, ATO's blue-tinted secondary
  hover, soft red destructive treatment, consistent visible keyboard focus.
- **Fields:** ATO's 36px default height, 6px radius, opaque page background and
  common high-contrast border; ordinary values are 14px. Native-select and popup
  select triggers use the same field geometry. Keep native input semantics.
- **Badges:** ATO's 12px tinted/bordered family with semantic status variants.
  Hunt's optional status dot carries the same meaning; never rely on color alone.
- **Confirmation dialogs:** IR's 520px maximum width and 8px radius, shared Radix
  focus containment/restoration, accessible title/description, Cancel-first focus,
  busy dismissal/duplicate-submit protection and inline actionable failures.
  Existing larger inspectors keep their documented wide layout and callbacks.
- These dimensions describe the default at a 16px root. Text and primary field/
  button heights scale with enlarged text. Explicit compact/icon/composer and
  wrapping layouts use the same shared implementation; they are not permission
  to create an app-specific visual fork.

The shared source set also includes the existing card, label, separator,
skeleton, tabs, select and account primitives. Product layouts may supply width,
placement and wrapping. Normal component appearance belongs to the shared CSS.
`suite-components.css` makes equivalent controls render consistently under the
ordinary Tailwind setup and Hunt's prefixed Tailwind/legacy CSS context.

Use the shared primitives for new ordinary controls. The reviewed native-control
inventory in each app's `suite-component-exceptions.json` preserves specialized
navigation/record selectors, anchored non-modal context popups, native file and
checkbox inputs, code editors, single-border assistant composers and app-specific login presentation. These are
explicit scope exceptions, not six alternative implementations of generic fields.
Do not mass-convert specialized controls or change their guards to satisfy a hash.

**Required edit procedure:** change the canonical component, copy the exact bytes
to all six builds, update the versioned contract and affected exception records,
then run `scripts/check_suite_components.py` with both peer repositories.
`scripts/check_suite_ui.py` includes that gate. New or changed native controls
and app-local `.suite-button`/field/badge/dialog overrides fail the gate.
Do not update expected hashes merely to accept a divergent app implementation.
The shared-file Git attributes enforce LF line endings on Windows and Linux, so
checkout conversion cannot silently create different source bytes.

Run `npm run test:components` in each frontend. The identical
`playwright.components.config.ts` starts a dedicated Vite fixture server to load
`/e2e/fixtures/suite-components.html` in its actual CSS context. The component
tests are explicitly enabled by this configuration and stay skipped in ordinary
product journeys, whose server may serve only compiled assets. Compare
the computed-style attachments within each browser engine across all six builds.
The approved per-engine computed styles are also checked inside every frontend's
component test, so an app-local generic CSS rule cannot quietly change a control
while its shared source still matches. Update these expectations only after an
approved visual change is verified across the suite.
The fixture verifies hover/focus, disabled/readonly/invalid/required fields,
dialog naming/focus/restoration, delayed failure/retry, duplicate submissions,
constrained desktop fit, popup keyboard behavior, tabs and reduced motion.
It uses simulated requests; also run the actual app workflow/role coverage below.
Fixtures are test assets, not product routes or a production component explorer.
The current [verification record](suite-foundation-verification.md) identifies
actual browser/role/state coverage and the synthetic versus live boundaries.

Shared component source parity does **not** prove every product screen looks or behaves identically. The shared foundation contract below now owns routing, transport, state, form and validation parity, with domain-specific adapters preserving each product's semantics.

## Shared frontend foundations and independent deployment

Version 1.14 hardens the standardized routing, HTTP transport, state conventions, forms and
validation across all six frontends. The canonical source is Hunt's
`frontend/src/lib/suite/`; each other frontend contains the **same source bytes**
inside its own repository. The [foundation contract](references/ai-enabled-threathunting/docs/suite-foundation-contract.json)
records their hashes and the shared verification assets.

**Each app builds and deploys independently.** There are no cross-repository
imports, linked packages, shared runtime servers, or sibling-checkout build
requirements. ATO needs only the ATO repository; Hunt needs only Hunt; each IR
variant remains a standalone build within the IR repository. Peer checkouts are
optional inputs to development-time drift checks, never application dependencies.

- **Routing:** React Router 8.5.0 through the shared `routing.tsx` entrypoint and
  BrowserRouter in all six apps. Route tables, allowlists, authentication redirects,
  draft/review permission decisions and recovery destinations remain app-owned.
  Hunt's event-driven navigation adapter now feeds this same browser engine and
  preserves citation history state. Its pre-router Back/Forward guard restores
  rejected history before a dirty editor can unmount. ATO's earlier capture guard
  and save/continue logic remain intact. Back, Forward, deep links and rejected
  navigation require real-browser tests; matching route source alone is inadequate.
- **HTTP:** native Fetch through shared `fetchResponse`, `requestScope`, `ApiError`
  and `readJson`. One cancellation/error model, deadline cleanup, validated JSON
  decoding and **no automatic mutation retry**. App adapters supply endpoints,
  identity headers, CSRF, error-body interpretation and domain response parsers.
  The default deadline is 30 seconds across preparation, headers and response body.
  IR chat and long mutations explicitly allow 220 seconds; signed uploads and
  downloads allow 120 seconds. Hunt reads now use 30 seconds and mutations use
  220 seconds. ATO SSP non-streaming reads use 30 seconds and mutations 220 seconds.
  Only ATO generation streaming opts out, retaining its explicit heartbeat/idle
  timeout and caller cancellation. No nested default may shorten an override.
  Abort cancels browser transport/body reads; it does not prove server work stopped.
  Preserve uncertain-write reconciliation and never automatically replay a mutation. Signed object
  storage requests must never receive portal bearer tokens or CSRF headers.
- **State:** React local state for component/route ownership and React Context for
  state shared by descendants. Shared `createStateScope` provides memory-only
  provider state with reactive subscriptions and an explicit restoration-only
  snapshot accessor. IR queue draft persistence uses the snapshot accessor so
  typing does not broadcast updates through the authenticated tree.
  `useFormState` is the controlled
  draft-state entrypoint. Derived values remain derived. Server data stays owned by
  its existing request/polling controller; there is no suite-wide persisted server
  cache. No Redux, Zustand, or query-cache package is required. Do not move private
  case data into global storage. Existing authenticated lifetimes, polling,
  cancellation, stale-response checks and Hunt's explicitly scoped tab drafts stay
  app-owned. The shared latest-read controller cancels superseded ATO session
  reads and Hunt queue reads; stale responses cannot overwrite newer state.
  IR filter changes reset pagination before requesting data, so an old cursor
  cannot trigger a redundant request. Contexts representing workflow callbacks are domain adapters, not
  alternative global-state frameworks.
- **Forms:** all native form surfaces render the same `SuiteForm`, retaining their
  exact DOM, classes, labels, focus order and browser validation. It suppresses
  duplicate pending async submissions and respects `aria-busy`. Existing handlers
  still own field values, save/reconcile behavior, busy/error announcements and
  reset decisions. Return async work to the form and handle failures visibly; a
  timeout must not discard the draft or automatically repeat an accepted write.
- **Validation:** Zod 3.25.76 in every frontend through the shared validation
  entrypoint, with `parseWithSchema` and `validateFields`. Native required/type/
  length constraints remain. Domain schemas and generated API contracts differ
  because the products have different data; retain their meanings, refinements,
  evidence preservation and rejection paths. Backend validation remains
  authoritative. Generated browser modules contain schemas only, excluding unused Zodios/Axios
  clients. Keep the checked-in schemas-only template in `generate:api`.
  Zod stays on 3 while the installed generator requires it; Python 3.12 versus 3.14 does not create this hold.

`suite-foundation-adapters.json` in each repository records the intentional product
boundaries. Equivalent generic mechanisms must not fork. Change the canonical
source, copy it to all six frontends, update the shared contract and run
`scripts/check_suite_foundation.py` locally, optionally with both `--peer` paths.
`check_suite_ui.py` includes this gate. It rejects changed shared bytes, direct
Fetch/form/router/validation bypasses and file-linked deployment dependencies.
Adding a state, form, query or HTTP framework requires a recorded decision and
an update to the reviewed-package contract; it is not a silent app-local choice.
Run `npm run test:foundation` in each frontend for its own standalone fixture;
then run the product workflow and component checks. Record actual browser, role,
route and state coverage in [the foundation verification record](suite-foundation-verification.md).


### Fast feedback and release qualification

During implementation, run the local source gate and focused unit/browser tests
for the changed boundary. Use the installed Node/browser caches and the dedicated
`test:foundation` / `test:components` commands; freeze application files during a
browser qualification run so hot reload does not contaminate the result. Run the
complete affected six-frontend matrix once the shared candidate is stable, and
repeat affected checks only after a relevant change or unresolved failure. Do
not shorten the final release matrix by hiding failures or dropping required
roles/states.

Responsiveness comparisons require the same compiled production serving mode,
browser/viewport, data, workload and stated cold/warm cache conditions. A Vite
source fixture is appropriate for component behavior; its startup or test runtime
is not a production responsiveness benchmark. Report build time, harness time,
network/server latency and interaction/render latency separately. The current qualification reports anonymous cold-start JavaScript payloads
separately from behavior, request counts and render counts. It does not equate
smaller assets with lower end-to-end workflow latency.

### Production bundle budgets

Run `npm run build` then `npm run check:performance` in each frontend. The local
checker reads Vite's production manifest, counts each eager JavaScript asset once
(including preloaded dependencies), excludes truly dynamic imports from that
eager count, and separately bounds total JavaScript across all routes. Limits in
`suite-performance-contract.json` use the measured 1.14 candidate with explicit
headroom; they are payload limits, not latency guarantees. Update limits only
with reviewed before/after network and bundle evidence, never merely to silence
a failure. Also inspect actual browser requests: authentication or initial route
logic can load dynamic chunks before the first usable screen.

ATO page splitting must retain the eagerly registered agency-settings history
guard. Hunt lazy renderer boundaries must leave the shell, drafts and workflow
guards mounted. Delay a hidden panel until its first use, then retain it when
visited so drafts survive. Keep shared data helpers separate from renderer
modules so a static helper import cannot defeat the intended code split. New asynchronous screens need accessible loading and recoverable
errors. Keep per-app identity, permissions, revisions and deploy independence.

## Foundation decision review

See the [current decision review and follow-up limits](references/ai-enabled-threathunting/docs/suite-foundation-architecture-review.md) for the 1.14 candidate.

An aligned implementation is a reviewed default, not proof of optimality. When
asked to standardize, review or materially replace a foundation, compare the
current implementations with a credible alternative before selecting a winner.
Routine fixes do not reopen the whole stack.

Record the requirement, concrete failure or cost, considered alternatives,
security/workflow constraints, migration cost, measured evidence and reversal
condition. Name evidence that is missing. Prefer a narrow experiment when the
choice depends on performance or operator behavior. Do not assume the newest
package, smallest dependency count, most popular library, or one app's existing
implementation is inherently better.

For these frontends, use the following questions:

- Would React Router data APIs remove duplicated loading/navigation machinery,
  and can they preserve every dirty-draft and authentication transition? Keep
  the current declarative engine until those benefits justify a tested migration.
- Does a query library reduce duplicated server-state lifecycle code enough to
  justify explicit authenticated cache keys, logout invalidation, refresh policy,
  cancellation and mutation-reconciliation rules? Never introduce a global cache
  merely to make all apps list the same dependency.
- Do complex forms need field arrays, granular subscriptions or extensive shared
  validation that a form library demonstrably simplifies? Compare equivalent
  typing/rendering and error/focus behavior before replacing working native forms.
- Does the HTTP layer bound the actual operation being discussed: connection,
  headers, body, stream idle time or server-side work? Cancelling a browser request
  does not establish that a mutation was cancelled. Preserve uncertain-write
  reconciliation and signed-upload credential boundaries.
- Does a wrapper own useful common behavior or a stable boundary? Avoid adding
  aliases, settings or indirection solely to make different business flows look
  identical in source. Product schemas, permissions and workflows are allowed to
  differ; equivalent generic behavior needs parity tests.

Use the existing React, Development Stack, Source-Driven Development,
Maintainability/Architecture, Reliability/Performance and Correctness/Testing
guidance together. These cover the work; a new suite-specific skill for each
library would duplicate policy. Keep selections and exact versions here, method
guidance in the existing skills, and mechanical enforcement in executable gates.
If a future repeated workflow is genuinely missing, add a focused skill only for
that gap and link it from this entry point.


## Frontend stack and Python compatibility

Version 1.11 standardizes the implementation toolchain across ATO, Threat Hunt,
and all four Incident Response frontends. The exact, offline-checkable pins are
in [the frontend stack contract](references/ai-enabled-threathunting/docs/suite-frontend-stack.json). The contract and
the package manifests/lockfiles are released together. A newest-version lookup
does not by itself qualify a release; upgrades must pass the checks below.

The stable target verified against publisher metadata on **2026-10-24** is:

- Node.js **24.22.1 LTS**, npm **11.19.1**; Node 26 is Current, not the selected LTS.
- React and React DOM **19.3.1**, with matching React 19 type packages.
- TypeScript **7.0.2**, Vite **8.3.5**, React Vite plugin **6.1.2**.
- Tailwind CSS and its Vite plugin **4.3.3**; Radix primitives at the exact
  component-specific versions in the contract; Lucide React **1.61.0**.
- React Router **8.5.0**, imported from `react-router` (or `react-router/dom`
  for DOM-specific APIs). The old `react-router-dom` compatibility package is
  not the current major and must not be used as the latest-version indicator.
- Vitest **5.0.5** and Playwright Test **1.64.1**. Where used, jsdom is **30.1.3**,
  Testing Library React **16.3.3**, and jest-dom **7.0.1**.

Use exact direct dependency pins, committed npm lockfiles, the same Node major,
and the existing independently deployable builds. Do not create cross-repository
runtime imports or install product-specific libraries where they have no use.
All common packages that are present must match the contract. Run
`python3 scripts/check_frontend_stack.py --installed` in each repository;
`check_suite_ui.py` also checks declared and locked versions.

Stack alignment preserves product behavior, security and layout. Tailwind may
coexist with the approved custom CSS; Hunt excludes Tailwind Preflight and prefixes
its utility layer to prevent new global resets. All six frontends mount the same React Router browser engine through the shared foundation entrypoint. Hunt retains its event-driven navigation adapter, route allowlist and workflow callbacks around that engine.
Use Radix primitives for equivalent interactions while keeping the documented
native dialogs, layout density, exports and customer identity providers intact.

### Python is a separate compatibility axis

The suite's intended backend direction is **Python 3.14**. A backend may remain
on its declared, verified Python 3.12 runtime while its frontend is upgraded.
Browser libraries execute in JavaScript, and Vite/TypeScript execute under Node;
Python 3.12 alone is not a reason to lower React, Router, Tailwind or Vite versions.
Node build stages and Python service stages remain separate. Do not change a
backend runtime or cloud deployment merely to satisfy a frontend version target.

A real coupling can exist in API/schema generation, Python browser-test bindings,
offline installers, build scripts, native wheels, or hosting packages. Record the
exact package, affected app/variant, tested version, concrete failing boundary,
temporary pin, and removal condition. If Python 3.14 resolves that boundary,
make the frontend recheck a named acceptance item of that app's Python migration.
Recheck required SDKs, schema/client generation, browser tests and packaged static
assets when either runtime changes. Use the target runtime's actual dependency
declarations and qualification evidence rather than inferring status from a label.

### Current compatibility hold

**Zod 3.25.76** is retained in ATO and the Incident Response clients using
`openapi-zod-client` / `@zodios/core`. The latest Zod is **4.6.7**, but the installed
Zodios client declares `zod: ^3.x` and the generated schemas use that contract.
This hold is independent of Python. Remove it when the client generation/runtime
chain supports Zod 4 and schema, authorization/error, and generated-client tests
pass. Do not use forced or legacy peer-dependency resolution to hide the mismatch.
MSAL is product-specific; its selected common version is **5.26.0** wherever used.

### Upgrade and evaluation acceptance

- Verify stable publisher releases and their Node/browser/peer requirements;
  inspect installed packages and caches before downloading. Do not select canary,
  beta, RC or experimental APIs simply to obtain a larger version number.
- Update manifests, locks, Node selectors, build images, generated clients where
  applicable, the contract, release mirrors, companion and permanent baseline.
  Record exceptions with an objective exit condition; do not silently fork pins.
- Require type checks, production builds and relevant unit tests for all six
  frontends. Browser checks must include the central interaction/accessibility,
  popup/workflow, desktop zoom and reduced-motion requirements. Keep tests that
  detect real regressions; update only stale API usage, ambiguous locators and
  invalid timing assumptions. Preserve assertions of actual user outcomes.
- Compare frontend performance using equivalent production builds, data volumes,
  browser engines, viewport and cache policy. Record visible-content and paint
  timing separately from automation dispatch/waiting and backend/model latency.
- Isolated synthetic browser tests may use two workers after state independence
  is verified. Keep real shared-state/provider workflows serialized until isolated.
  Run a focused feedback lane and a broader release lane; never drop required
  browser, zoom or guarded-flow coverage to make the result faster.
- Record actual engine versions, routes, roles, states, skips and unavailable
  checks. Native browser zoom is not font resizing; accessibility-tree assertions
  are not screen-reader speech. Source/lock parity is not runtime qualification.

Publisher references: [Node releases](https://nodejs.org/en/about/previous-releases),
[React versions](https://react.dev/versions), [Vite releases](https://vite.dev/releases),
[Router v8 migration](https://reactrouter.com/upgrading/v7),
[npm registry package metadata](https://registry.npmjs.org/).


## Navigation

- Expanded primary sidebar in ordinary desktop views: **256px / 16rem**, including padding and border. The desktop zoom exception below takes precedence when that width would obstruct reflow.
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

## Interaction and accessibility

These are shared outcomes for equivalent roles, not a requirement to use one
component library or change app layouts. Preserve native controls, authentication,
domain-specific permissions and busy/draft/review guards. The six gaps reproduced
in the October 24 audit are regression cases for this contract.

- **Keyboard focus and bypass:** every action must be keyboard reachable, with
  visible immediate focus and a logical order. Keep focus visible when containers
  scroll. Provide a keyboard-visible **Skip to workspace** link before repeated
  navigation, targeting the active main region with programmatic focus support.
- **Modal dialogs:** give the dialog a name and an appropriate description; move
  focus inside, contain Tab/Shift+Tab, make background content inert, and restore
  focus to the connected opener on close. Preserve existing Escape/outside-click
  and pending-operation guards. Native `showModal()` is suitable where already
  compatible with the app; Radix dialogs remain suitable. Account panels and
  non-modal help popups keep their separate existing behavior, never a modal trap.
- **Loading and error feedback:** expose a concise live status for waiting states
  and `aria-busy` on the affected region. Keep the status outside a busy subtree
  so busy suppression cannot swallow it. Announce actionable errors without
  forcing focus unless the flow needs it. Preserve retries, timers, data and
  existing request guards; do not announce every token or polling refresh.
- **Loading-to-content consistency:** skeletons must use the current loaded view's
  column order and exact labels for equivalent meanings. Preserve geometry and
  status meaning; avoid exposing placeholder rows as real data to assistive tech.
- **Disabled, readonly and validation:** use accurate native/ARIA state, keep
  duplicate-action protection and approval guards, and make reasons for unavailable
  actions discoverable. Keep associated labels/help/errors and existing native
  validation; verify invalid-field focus and error recovery. Component-specific
  dimming, sizes and readonly behavior remain app-owned.
- **Essential control boundaries:** use `--workspace-color-control-border`
  (**#6E7B8D**) for enabled neutral textual fields, selects and marked composite
  field boundaries. Verify at least **3:1** against adjacent surfaces where the
  boundary identifies the control. Keep decorative dividers at #30363D. Preserve
  semantic invalid/warning states, which require their own contrast check, and
  disabled component dimming. Native controls keep their geometry. Forced-color
  modes use system colors rather than suppressing the user's contrast settings.
- **Page-state headings:** a standalone loading/error/empty screen must retain
  its correct page hierarchy. Error/empty titles use the existing 28px page-title
  role, including semantic h2 via `workspace-page-title`; card/dialog titles stay
  at their existing section role.
- **Scrolling and enlarged content:** check desktop widths **1280, 1440 and
  1920px**, enlarged text to **200%**, short desktop heights, and the affected
  panes/popups. Verify keyboard access, visible focus, reachable footer/actions,
  contained intended table/editor overflow, and no accidental page clipping.
  Record full zoom/reflow and assistive-technology qualification separately when
  not exercised; a root-font test does not prove browser zoom or screen-reader use.

For every affected app/frontend, record the route and actual state checked,
browser/viewport, expected outcome and result for the above roles, plus motion,
color and typography. Run focused regressions in Chromium, Firefox and WebKit
when available. Distinguish **verified**, **intentional exception** and
**unverified**; do not claim complete WCAG 2.2 AA conformance from this finite suite.
Customer requirements and app-specific exceptions remain explicit.

References: [WAI modal dialog pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/),
[status messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html),
[non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html),
and [bypass blocks](https://www.w3.org/WAI/WCAG22/Understanding/bypass-blocks.html).

## Workflow and popup regression coverage

Every UI/UX change must include Playwright verification of the affected surface.
For a small visual or copy edit, a focused rendered-browser check is sufficient;
for an interaction change, exercise the relevant workflow and failure paths.
Use screenshots, computed styles/geometry, keyboard input and native desktop zoom
as appropriate. Vitest, TypeScript and build checks supplement browser testing.
Record unavailable engines or blocked checks explicitly; do not silently skip
browser verification or claim source-only checks as UI sign-off.

UI parity includes usable workflows and failure recovery, not only matching styles.
For changed surfaces, record the app, role, route, state, browser and real-versus-
synthetic API boundary. Reuse existing Playwright fixtures and local browser caches.

- Every `dialog` and `alertdialog`, including non-modal information popups, has
  a programmatic name connected to its visible title (prefer `aria-labelledby`).
  Verify the computed accessible name in a browser. Keep non-modal popups non-modal;
  do not add a focus trap or change their existing dismissal behavior.
- At 100%, 200% and 400% native desktop zoom from 1280, 1440 and 1920px windows,
  open affected popups both before and after zooming. Check every confirmation
  action, including three-action unsaved-draft footers. All focused actions and
  ordinary popup text must fit horizontally. Allow the action row to wrap only
  within the existing fine-pointer desktop reflow scope; never shrink its text.
- Constrain an affected popup's width and horizontal position to the viewport
  while preserving its anchor, vertical placement, scrolling, open/close handlers,
  focus policy and ordinary desktop appearance. Respect the existing desktop-only
  reflow media query; this does not authorize mobile layout work.
- Exercise relevant user journeys with controlled delayed/failed requests,
  repeated submission, retries, out-of-order replies, navigation during pending
  requests and unsaved edits. Assert preserved input, selection, source content,
  request counts and intended guards. Do not treat an unavailable capability as
  a bug when the app intentionally disables it.
- Keep test locators aligned with the current user-facing wording. Fix stale
  selectors in the test; never revert approved UI copy to make a test pass.
- A green style check, synthetic workflow suite or accessibility tree is not
  proof of live backend persistence, authorization, real identity, spoken screen-
  reader feedback or full product coverage. Record excluded/unavailable checks.

Regression entrypoints: ATO and each IR frontend's
`e2e/desktop-accessibility.spec.ts` cover the affected three-action dialog or
capacity popup at native Chromium zoom. IR's `ContextUsageIndicator.test.tsx`
checks its accessible name, and `e2e/queue-evidence-recovery.spec.ts` uses current
evidence wording. Recheck native Firefox/WebKit zoom and the affected interactions
when those engines are available; do not substitute root-font resizing.

Release 1.10 scope: the ATO unsaved-draft footer and the four IR capacity popups.
Threat Hunt receives the synchronized baseline/rules and inactive shared CSS roles;
its runtime and workflows are outside this fix. Existing app exceptions, newer
styles and mobile behavior remain authoritative.

## Desktop zoom and conversational feedback

Version 1.9 makes these existing interaction outcomes testable beyond root-font
resizing. Preserve the normal desktop composition, typography, colors, routing,
drafts, permissions, request timing and cancellation behavior.

- Test **actual full-page browser zoom at 100%, 200% and 400%**, starting from
  desktop windows of 1280, 1440 and 1920px. Verify the browser's zoom factor and
  layout viewport, keep the root font unchanged, and identify the tested engine.
  Pinch magnification, device scale emulation and changing the root font are not
  substitutes. A 320 CSS-pixel layout reached by zooming a desktop window is a
  desktop reflow check, not authorization to test or redesign mobile interfaces.
- In the opt-in `.workspace-desktop-reflow` shell, a fine-pointer, hover-capable
  desktop with an effective viewport at most 48rem reflows the sidebar before
  full-width content. Do not gate reflow on device pixel ratio: page zoom can
  change the layout viewport without a matching resolution change. This is the accessible alternative
  to pinning 256px of navigation beside a narrow workspace. Keep all navigation and
  account actions available, preserve Skip to workspace, and allow vertical page
  scrolling. Retain local horizontal scrolling for genuine tables/code/documents;
  ordinary headings, controls and prose must not require sideways page scrolling.
  These rules do not alter coarse-pointer/touch/mobile presentation.
- Verify focused controls remain fully reachable after scrolling at zoom, including
  filters, required fields, submit actions, assistant composers and modal buttons.
  Preserve modal focus/guard behavior and existing app-specific pane semantics.
- Keep chat waiting status outside its busy transcript and announce failures as
  actionable alerts. Time counters and typing dots must not repeat announcements
  on every tick. Preserve visible feedback and cancellation/request behavior.
- After a **newly completed** assistant response, announce **“Assistant response
  ready.”** once without moving focus or reading a long answer automatically.
  Do not announce initial/restored history, pagination, refreshes, failed/cancelled
  requests or responses belonging to a previous workspace. This is an equivalent
  feedback role across independently implemented assistants, not shared runtime code.
- Expose truly required fields through native `required` or appropriate ARIA, with
  associated instructions when an unavailable submit action needs explanation.
  Keep existing validators and submit guards authoritative; labels alone do not
  communicate a field's required state to assistive technology.
- Record native zoom/reflow, accessibility-tree semantics, keyboard behavior and
  actual assistive-technology speech separately. A passing DOM/AX assertion is not
  a claim that Narrator, NVDA or JAWS speech was tested. Report unavailable engines
  or speech capture honestly. No GitHub Actions or additional runtime dependency
  is required by this validation contract.

Run each in-scope frontend's `e2e/desktop-accessibility.spec.ts` in its existing
Playwright harness using Chromium and a headed desktop session (`xvfb-run` is
suitable for Linux). Reuse the installed browser; `SUITE_UI_CHROMIUM_EXECUTABLE_PATH`
can select an existing compatible binary. The harness creates only an isolated,
temporary browser profile and extension for native zoom. Keep the usual multi-engine
interaction suite as a separate check; explicitly skipped native zoom is unverified.

Version 1.9 remediation scope: ATO and all four Incident Response frontends implemented these fixes.
Threat Hunt received the synchronized standard and stylesheet only in version 1.9; its runtime
was explicitly excluded from that remediation. The reflow selector is opt-in and
does not change Threat Hunt. Its native-zoom and conversational-feedback alignment
is unverified for this release and must not be described as complete suite coverage.
Existing shared typography, palette, account, sidebar and motion rules remain intact.

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
- Version 1.12 supersedes prior app-owned ordinary button/input/badge/dialog
  decoration with the approved shared component contract. Specialized layouts
  and the explicitly recorded native controls retain their documented scope.
- Login pages, editors, tables, dialogs, inspectors and reports retain their
  established layouts and interactions. App/document-specific typography and
  print/PDF rules remain explicit exceptions to ordinary screen text roles.

Further alignment outside the version 1.12 component scope requires rendered
evidence and an intentional contract update. Preserve specialized product roles.

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

Edit this canonical document, the shared component source/manifest and canonical `frontend/src/suite-workspace.css`
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
suite checks and app workflow regressions described above. Preserve root text-size behavior and specialized layout constraints. Default
component geometry follows the approved shared component contract.

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

## Interaction parity correction — v1.8.0

The October 24 broader audit reproduced IR dialog focus escape, incomplete
loading/error announcements, stale IR skeleton column labels/order, insufficient
neutral field-boundary contrast, missing IR bypass links and ATO standalone
page-state title mappings. Version 1.8 corrects those six gaps and adds the
interaction/accessibility check contract above. Existing layouts, authentication,
workflow guards, decorative palette and motion standards remain in place.

## Desktop accessibility correction — v1.9.0

The desktop-only follow-up reproduced obstructed 400% reflow, IR chat waiting/error
announcement gaps, missing reply-completion cues and ATO required-field semantics.
This release corrects them in the five in-scope frontends and makes their validation
explicit. Normal desktop layouts and all workflow/domain guards are preserved.
