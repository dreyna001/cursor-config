# Suite UI verification — v1.8.0

## Six audited gaps resolved

- All four Incident Response confirmation dialogs contain keyboard focus, expose
  modal semantics, preserve pending-delete guards and restore the opener.
- ATO workspace and IR skeleton waiting states have a live status outside the
  busy region. ATO workspace errors and IR confirmation failures announce errors.
- IR loading-table labels/order match the loaded table.
- All six frontends use the accessible neutral field-boundary token; decorative
  dividers, semantic states, disabled styling, geometry and other colors remain.
- All four IR shells offer Skip to workspace for their existing main regions.
- ATO standalone error/empty states use the current page-title role. The normal
  creation route and card/dialog title hierarchy remain unchanged.

## Validation and limits

The six production builds and relevant unit checks passed. Browser results below
cover Chromium, Firefox and WebKit, including the added modal, busy-state,
loading, error, bypass and contrast cases. Existing navigation/account, typography,
motion/reduced-motion, enlarged-text, scrolling and guarded workflow checks remain.
ATO's empty component branch is verified separately at component level because
the ordinary empty-inventory route intentionally opens the creation form.

See [build results](evidence/accessibility-build-results.json),
[browser results](evidence/accessibility-browser-results.json), and
[scope record](evidence/accessibility-scope.json). Logs and supplemental checks
are in the evidence folder. [The previous motion release](evidence/verification-v1.7.0.md)
remains historical evidence. Current rules, sources and generated HTML agree.

The earlier audit's synthetic-history fixture initially disabled conversation
history, and its empty-state fixture entered the creation route. These fixtures
were corrected without changing application routing. The account Tab regression
now compares with the browser's measured native sequence, which can include
scrollable regions. Only the final corrected runs count as qualification.

All apps keep independent runtime sources and builds. Existing app layouts,
control sizes, authentication, account behavior, workflow guards, request timing,
print/export and domain status meanings remain app-owned.

This is bounded local validation with synthetic APIs/identity. It does not qualify
live cloud/Entra, all possible routes/states, all screen readers, customer themes,
or full WCAG conformance. Root-font enlargement is not proof of browser zoom or
complete reflow qualification. These remain explicit additional checks when
affected by future work; source hashes are never a complete accessibility pass.
