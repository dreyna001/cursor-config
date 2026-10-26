# Flat workspace surfaces — 1.15.0

Qualified locally on 2026-10-24. This is local verification, not a production deployment.

The approved surface update keeps the existing palette and canvas colors. Ordinary
nested workspace sections are transparent with no enclosing card edge; notices use
the existing semantic text and border colors as a left rule; tabs remain transparent
with their existing selection indicator. Dialogs, popups, controls, badges and
independent record cards retain their role-specific treatment.

The generated visual companion was rendered in Chromium at 1440px: the section
resolved to the existing canvas color (`rgb(13, 17, 23)`), the notice background was
transparent with a 2px semantic left rule, and the selected tab was transparent with
the existing underline (`rgb(140, 188, 255)`). This is static-companion render
evidence, not a live application workflow.

ATO focused browser style assertions passed in Chromium, Firefox and WebKit (3/3).
The surface, palette and reflow checks covered desktop widths 1280/1440/1920 at
default and 200% root text size; Enter keyboard activation was checked at both tab
levels.
Additional Chromium checks passed for unsaved-draft guard/focus (2 cases) and
creation/profile retry (1 case). The ATO typecheck, production build,
performance/public-bundle checks and 137 Vitest cases passed. Browser evidence is
scoped to the exercised ATO routes and states; this is not live model/API, SSO,
screen-reader speech or mobile qualification. Native browser zoom was not tested;
the 200% check changed root text size. No live writes or model calls were made.

The Agency document settings route also passed a Chromium render check at 1440 ×
1000: all three ordinary sections were transparent and borderless in the success
state, and the fourth section stayed flat in the HTTP 503 fallback. Existing input
fill/border and editor heading colors were preserved. The ATO route-level details
and capture are recorded in `docs/ui-flat-surfaces-verification-20261024.md`.

All six frontend CSS mirrors, release documents, component/foundation/version
metadata and visual companions passed the v1.15.0 source/link/version checks across
Hunt, ATO and IR. Peer source review found no semantically equivalent nested-section
cards requiring a peer UI edit; standalone record cards remain intentional.

## Closeout verification — 2026-10-25

All four IR frontends passed their shared component suites in Chromium, Firefox
and WebKit (60 cases). ATO passed nine flat-surface/settings/retry cases across
the same engines, including 1280/1440/1920 desktop widths and 200% root text.
Hunt passed 27 component/foundation cases across the three engines. Total: 96
passing synthetic browser cases. The IR report is
`docs/UI_BASELINE_1_15_IR_BROWSER_QUALIFICATION_2026-10-25.md`; ATO reuses
`portal/e2e/security/ssp-workspace-ui.spec.ts`. No native zoom, screen-reader
speech, live identity/service, paid model call or deployment is claimed.

The v1.14 prose and machine-readable publication notes now distinguish original
local qualification from the subsequent merges (IR #52, ATO #39, Hunt #87).
Measured counts and original source identities were not rewritten.

## Previous qualification — 1.14.0

Qualified locally on 2026-10-24; the v1.14 implementation was subsequently committed and merged into all three application repositories. No deployment is implied.

All six frontends passed typecheck, production build and 1639 unit checks.
162 shared browser cases, 341 product cases,
48 queue/recovery cases, 36 real-browser transport
cases, and 5 isolated real ATO API/PostgreSQL journeys passed.

See [the decision, measurement and coverage record](suite-foundation-architecture-review.md)
and `suite-foundation-qualification.json` for per-app counts, exact scenarios,
source state and qualification limits. Per-engine approved component style
assertions passed in every frontend; layouts and domain guards remain app-specific.
The versioned performance contract and production manifest checker prevent
unreviewed eager and total JavaScript growth. Cross-repo code/runtime dependencies
remain prohibited. The disposable ATO stack was cleaned up.


## Previous qualification history

# Suite UI verification — v1.11.0

All six frontend dependency sets now use the shared version contract. Type checks, production builds, 1541 unit tests and 221 scoped synthetic browser cases passed.

[Current qualification and exclusions](evidence/verification-v1.11.0.md). [Machine-readable scenario record](evidence/frontend-stack-1.11.0.json).

This is a local working-tree implementation, not a production deployment. Python runtimes remain separate. Inactive workflow selectors and existing running services are explicitly recorded as operational drift.

---

# Suite UI verification — v1.10.1

Version 1.10.1 explicitly requires scoped Playwright verification for every UI/UX
change. Runtime code is unchanged from the verified 1.10.0 fix, apart from the
stylesheet version marker; source-preservation checks passed in all three apps.

## Fixed and verified

- ATO's three-action unsaved-draft footer wraps within the existing fine-pointer
  desktop reflow scope. All actions are visible; cancellation preserves the draft.
- All four IR capacity popups remain inside the desktop viewport and expose the
  visible title as their accessible dialog name. Their non-modal handlers remain.
- 264 synthetic browser workflow cases pass across Chromium, Firefox and WebKit.
  They cover navigation/drafts, duplicate submissions, delayed responses, retries,
  capability guards, evidence preservation and keyboard/feedback states.
- Five committed native Chromium regressions pass, plus 90 native Firefox/WebKit
  samples across 1280/1440/1920 desktop widths at 100/200/400% zoom. Root font stays
  16px. Focused component tests, builds and applicable TypeScript checks pass.
- Shared CSS, release documents, visual companion and rule entrypoints agree on
  baseline 1.10.1. The existing Playwright skill guide documents the workflow.

[Execution record](evidence/workflow-gaps-verification.json).

These are controlled frontend tests, not live backend/SSO qualification or complete
accessibility certification. Narrator/screen-reader speech and mobile work were
excluded. WebKit is the Linux test engine, not macOS Safari. Threat Hunt received
documentation and inactive shared CSS roles; its runtime was not retested here.

[Previous baseline verification](evidence/verification-v1.10.0.md) remains historical.
