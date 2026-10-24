# Threat Hunting terminology audit

Date: 2026-10-19 | Shared vocabulary: 1.0.0

## Applied

- Sidebar branding, sign-in heading, and browser title use **Threat Hunt Workspace**.
- Marketing-facing identity uses **Threat Hunt**.
- Removed Threat Hunt Console and Analyst workspace as alternative app names.
- The logo mark and typography use the approved Compact mark and Public Sans.
- Updated affected browser selectors to the approved sign-in identity.
- Added the shared vocabulary, README/agent entry points, and a local terminology check.

## Dated local identity exception — 2026-10-19

The user approved **Threat Hunt** as the marketing name and **Threat Hunt
Workspace** for the product identity shown inside this app. This intentionally
differs from the shared vocabulary 1.0.0 product name, **Threat Hunting
Workspace**. The shared guide remains unchanged; this local exception applies
only to this app's sidebar, sign-in heading, browser title, and brand-related
checks. The local checker continues to reject retired short aliases such as
**Threat Hunt Console** and the bare ` · Threat Hunt` browser-title suffix.

## Reviewed and retained

- Hunts, Hunt workspace, Hunt plan, hypothesis, Investigation, Evidence, and Report
  identify actual domain records or views. A scoped Hunt workspace remains a
  working environment inside the app.
- Connections and Settings already use the agreed configuration vocabulary.
- Plan approval and report finalization retain their distinct behavior. No run
  states, evidence meaning, confidence scales, permissions, or report content changed.
- No interactive assistant was added just to create naming symmetry. Use Threat
  Hunting Assistant if that capability is exposed later.
- API paths, component names, CSS classes, persisted values, and historical design
  previews retain their technical/original names. Unrelated existing edits remain intact.

## Verification

Run `python3 scripts/check_suite_terminology.py` from the repo root. Frontend
verification uses the existing unit tests, typecheck, build, and desktop browser
checks. The check covers known retired display phrases and identity surfaces;
semantic correctness still requires the shared guide and review.

## Recorded local results — 2026-10-19

- 29 affected frontend unit tests passed.
- TypeScript checks and production build passed.
- Sign-in and authenticated branding/navigation passed in Chromium, Firefox, and WebKit (6 desktop surface checks).
- Terminology check passed, including a separate negative control that rejects a retired product name. Shared guide and checker hashes match across all three repositories.
- Changed-file whitespace review passed. Existing unrelated work was preserved.
- Verification was performed locally before publication; no services or deployments were restarted or updated.
- Browser checks used mocked application APIs in isolated local previews; they do not qualify live integrations or identity providers.

## Main integration boundary

Remote main still uses the earlier Investigation Desk UI. The terminology changes
were ported to that UI independently of the separate uncommitted redesign, routing,
connection monitoring, and deployment changes in the primary checkout. The shared
vocabulary and app name apply to both UI versions. Only the existing sidebar
brand layout was adjusted to fit the full product name.

## Remote-main candidate verification — 2026-10-19

- 118 frontend unit tests passed on the isolated remote-main candidate.
- All applicable frontend TypeScript checks and production builds passed.
- Known terminology checks and changed-file whitespace checks passed.
- Only terminology changes and their documentation/tests are included; unrelated primary-checkout edits remain excluded.
- Earlier-main sign-in and sidebar branding passed six desktop checks across Chromium, Firefox, and WebKit using mocked application APIs.

## Expanded main integration — 2026-10-19

After the initial terminology publication, the user explicitly authorized merging
all remaining primary-checkout work. This follow-up includes the unified desktop
UI, evidence/report/plan views, direct URLs, connection and generation status,
deployment routing, supporting documentation/tests, and retirement of old design
templates. It supersedes the earlier main-integration boundary above: remote main
now contains the unified UI as well as the agreed product language.

Validation on this combined candidate:

- 128 frontend unit tests and all 102 Chromium desktop browser scenarios passed.
- Production frontend build/typecheck passed; mypy passed for 102 backend source files.
- Backend: 1,974 passed, 253 skipped, one pre-existing failure. The identical
  retained-context regression case at the 250,000-character budget fails on both
  the previously published remote-main baseline and this candidate:
  `tests/integration/test_production_composition.py::test_complete_retained_context_is_not_sampled_to_reserve_unneeded_retrieval[250000-stop]`.
  The test was preserved, not weakened or skipped. Its other two parametrizations
  pass in both versions. PostgreSQL-dependent tests and unavailable optional PDF
  renderer checks account for the recorded skips; this is not a PostgreSQL or
  production-readiness qualification.
- Terminology and changed-file whitespace checks passed. No live model, Splunk,
  cloud deployment, runtime-data migration, or credential change was performed.

## Backend failure resolved — 2026-10-19

The retained-context failure recorded above is resolved. Schema growth made the
one-row retrieval request's worst-case bounded repair 250,472 characters, exceeding
the unchanged 250,000-character guard. Compact JSON schema formatting in runtime
requests and minimum-headroom sizing reduces that repair to 249,472 characters.
Evidence values, native schema constraints, repair bounds and budget limits remain
unchanged. Sampled evidence keeps retrieval available; complete evidence still uses
the final-only schema. The original assertions are retained, with additional checks
for full source-value retention, schema equivalence and bounded-repair fit.

Validation: 1,975 backend tests passed, 253 skipped; mypy passed across 102 source
files. The same PostgreSQL and optional PDF-renderer exclusions apply. No live
provider call or runtime deployment was performed.

## Workflow usability follow-up — 2026-10-19

See [context, evidence and recovery fixes](ui-context-evidence-recovery-20261019.md)
for the scoped interaction changes and local verification. The shared vocabulary
and domain-specific review/approval contracts remain unchanged.

## App wording pass — 2026-10-20

Applied the shared `self-explanatory-ui` skill across sign-in, Hunts, intake,
Plan, Investigation, Evidence, Report, hunt activity, Connections and Settings.
Actions name what they affect: Prepare plan, Start approved hunt, Approve plan
and start hunt, and Finalize report. Microsoft Entra labels replace the internal
“native” terminology in collection and analysis controls. Evidence counts name
matching, current-page, shown and saved totals rather than API implementation
terms. Existing copy explains saved settings, pending edits and model-call status.

This is a display wording change. Existing data, identifiers, routes, scope,
approvals, evidence attribution and saved report narratives retain their contracts.
The local Threat Hunt Workspace identity exception remains in effect. No new
hints, tooltips, onboarding or workflow steps are introduced.

Verification uses the installed React 18.3.1 / Vite 6.4.3 / Playwright 1.55.1
environment and synthetic application API fixtures: 158 unit tests, the full
162-case Chromium desktop suite, and 66 focused cases each in Firefox and WebKit
pass. Two final scan-summary/Entra cases also pass again in Firefox and WebKit
after the last copy corrections. The production build/typecheck, terminology
checker and changed-file whitespace check pass. The build retains its existing
large-chunk advisory. Desktop checks cover 1280/1440/1920px, enlarged text,
keyboard focus, draft retention, approval/finalization gates, citations and exports.

Rendered screenshots were reviewed across intake, Plan, Investigation, Evidence,
Report, Connections, Settings and Microsoft Entra analysis. Longer scan-summary
wording initially exceeded its existing 80px height contract (99.78125px at
1280px). Shortening the note restores the original assertion without changing
CSS, font sizes, metrics or coverage caveats. The project-scoped conditional
lesson `threathunt-scan-summary-copy-height` records this verified cause and repair.

No live identity, Splunk, Graph or model calls were used. No customer instance or
database was changed; real-hunt answer quality and customer deployment remain
deferred. Backend behavior, server-generated report exports and historical
report narratives are outside this frontend wording change.
