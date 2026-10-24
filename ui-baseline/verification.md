# Three-app UI alignment verification — v1.5.0

## Result

The remaining approved form-text and New Hunt selection changes are implemented
across Threat Hunting, ATO and all four Incident Response frontend variants.
This is evidence for the shared roles and sampled workflows, not a claim that
every page, customer theme, exported document or production identity path is identical.

- Form values use 14px; labels use 13px; compact action text stays 12px.
- New Hunt keeps the Hunts destination selected using the existing parsed route.
- Common page, raised, heading, body, muted, border, action and link colors use
  the same shared tokens. Semantic status colors and contextual surfaces remain intentional.
- Existing grids, widths, control dimensions, navigation, draft/review guards,
  authentication/identity handling and export contracts are preserved.
- The six builds and focused unit tests passed. The browser records below cover
  all six frontends in Chromium, Firefox and WebKit, including exact form roles,
  colors, selection, keyboard account controls and enlarged text.

## Visual evidence

![New Hunt with Hunts selected](evidence/new-hunt.png)
![ATO evidence form](evidence/ato-evidence.png)
![Incident Response filters](evidence/incident-cases.png)

See [the measured styles](evidence/computed-styles.json),
[build results](evidence/form-build-results.json) and
[browser results](evidence/form-browser-results.json).
The log files in `evidence/form-check-*.log` and `evidence/form-build-*.log`
record the executed checks. Earlier v1.4 logs are retained as historical evidence.

## Scope and decisions

The prior comparison found mixed 12/13/14px form text. The baseline now assigns
explicit roles instead of relying on the allowed size scale. This follows the
Fluent 14px body scale while preserving compact enterprise controls; WCAG does
not prescribe a minimum CSS pixel size. Text enlargement is checked separately.

The apps intentionally retain different workflows and content layouts: ATO's
system/work/review groups, Hunt planning, and Incident Response conversation/case
context. Code/identifier editors, native non-text controls, metadata, semantic
warning/error/success headings and contextual surfaces retain documented exceptions.

Visual previews and browser tests use synthetic API/identity fixtures. They do
not qualify live cloud/Entra deployments, execute investigations or approve SSPs.
No production workflows, permissions, backend APIs or live records were changed.

Exact source commits and source/local checksums are in [manifest.json](manifest.json).
