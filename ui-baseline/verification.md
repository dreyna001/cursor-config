# Suite UI verification — v1.9.0

## Scope

ATO and the four Incident Response frontends implement desktop zoom reflow,
live conversation feedback, and required-field semantics. Threat Hunt receives
the synchronized shared CSS/documentation, with no new reflow opt-in or runtime
behavior. Its native-zoom/conversation gaps remain outside this authorized scope.

## Verified outcomes

- Ordinary desktop typography, colors, sidebar geometry, account behavior and
  workflow regressions retain the previous baseline.
- Native Chromium page zoom at 100%, 200% and 400% preserves reachable main
  content and focused controls; this uses the browser zoom factor with unchanged
  root font in desktop windows, not mobile or device-scale emulation.
- IR chat waiting status is outside the busy transcript; failures are alerts.
- Both assistants announce a newly completed reply once, without focus transfer
  or token-by-token announcements. Initial/restored history does not announce.
- ATO System Name exposes required state and associated submit instructions;
  existing creation and permission guards remain authoritative.

See [build and focused unit results](evidence/desktop-a11y-build-results.json),
[native zoom and announcement regressions](evidence/desktop-a11y-native-results.json),
and [the existing multi-engine regression results](evidence/desktop-a11y-browser-results.json).
The tests use synthetic API/identity records; no live cloud or identity operation
is qualified. Actual Narrator/NVDA/JAWS speech and native Firefox/WebKit zoom are
unverified. Accessibility-tree and keyboard results do not imply a complete WCAG
conformance audit. No mobile tests or layout changes were performed.

[Previous v1.8 verification](evidence/verification-v1.8.0.md) remains historical.
