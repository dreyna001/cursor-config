# Suite UI verification — v1.7.0

## Motion alignment

All three applications, including all four Incident Response variants, now use
the shared motion contract: 150ms interaction/disclosure/popup transitions,
immediate keyboard focus, 1s linear spinners, 2s loading pulses, and the existing
1.2s staggered IR typing feedback. Reduced motion disables decorative CSS
animation and transitions across the app, including portals and pseudo-elements.
Status content, final open/selected states, request timing and layout are preserved.

The earlier checks established colors and states but missed motion parity. The
baseline now requires a coverage record across typography, palette, spacing,
hover/selection, focus, disabled/loading states, overlays and motion. Matching
source hashes or still screenshots alone cannot establish complete UI parity.

## Fresh verification

- Six production builds and 233 focused/unit tests passed locally.
- 140 browser tests passed across Chromium, Firefox and WebKit. The existing
  shared UI checks now verify normal/reduced preference modes, runtime preference
  changes, actual navigation/disclosure timing, immediate focus, portal-scope
  CSS probes, spinner/pulse/typing roles, stopped animations and stable geometry.
- Existing navigation, account, form, creation and workflow checks still pass.
- ATO E2E TypeScript checking passes; its prior HTML/SVG helper error is fixed.
- Source scope checks preserve existing non-motion CSS, layout, API/identity
  handling, component behavior, dependencies and previous test assertions.
- Shared documents, stylesheets, font assets and the generated companion are
  synchronized. Each application keeps its own independent local implementation.

See [build results](evidence/motion-build-results.json),
[browser results](evidence/motion-browser-results.json), and
[scope checks](evidence/motion-scope.json). Detailed build/browser logs are in
the evidence folder. [Earlier v1.6.1 verification](evidence/verification-v1.6.1.md)
is historical evidence, not a claim that every current screen was requalified.

## Boundaries and intentional differences

Hunt's native disclosure, ATO's profile/provider disclosure and IR's expandable
history keep their existing controls and final states. The IR typing indicator
is an intentional task-specific feedback role. Existing popups retain their
current shape/entry effect; native dialogs do not gain new effects. No workflow
timer, auto-scroll measurement callback, backend operation or live record changed.

Browser checks use synthetic API/identity fixtures. They do not qualify live
cloud/Entra deployments, every customer theme, every possible route/state, all
assistive technology, or full WCAG conformance. Remaining coverage must be
reported explicitly rather than being treated as automatic parity.
