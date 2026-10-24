# Suite UI verification — v1.10.0

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
  baseline 1.10.0. The existing Playwright skill guide documents the workflow.

[Execution record](workflow-gaps-verification.json).

These are controlled frontend tests, not live backend/SSO qualification or complete
accessibility certification. Narrator/screen-reader speech and mobile work were
excluded. WebKit is the Linux test engine, not macOS Safari. Threat Hunt received
documentation and inactive shared CSS roles; its runtime was not retested here.

[Previous baseline verification](verification-v1.9.0.md) remains historical.
