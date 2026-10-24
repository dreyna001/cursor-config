# Frontend hardening qualification — 1.14.0

Local candidate, 2026-10-24. Not committed, merged or deployed.

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
