---
name: threat-hunt-reporting
description: "Change or review ai-enabled-threathunting browser reports and PDF exports while preserving its saved evidence, analyst edits, chronology and finalization contracts."
---

# Threat-hunt reporting

Use only in `ai-enabled-threathunting`. Read current root `AGENTS.md` and
`docs/threat-hunt-reporting-guidance.md` before changing report content or rendering.
The [full local reporting reference](references/threat-hunt-reporting-guidance.md)
is a versioned snapshot; current app source and approved contracts win.

Use installed global `report-export-parity` for reusable cross-surface review and
`llm-evidence-regression` for changed grounding/output contracts. Shared principles
do not override this app's section order, display exceptions, source inspector,
finalization guards or historical exports.

Preserve these app-specific distinctions:

- Saved answers/findings, analyst edits and evidence/query bindings remain
  canonical. Display suppression/grouping is limited to exact documented cases;
  familiar prose prefixes, similar text and model confidence do not justify loss.
- Event timeline describes environmental observations; Hunt timeline describes
  investigation activity. Point events never prove continuous telemetry or cause.
- Retain approved UTC scope and distinguish executed searches, missing/partial
  coverage and zero matches. Keep every distinct limit with its owner/source/time.
- Stable citation labels resolve to the same immutable records across browser and
  PDF. Missing saved snapshots remain unavailable; current records cannot silently
  replace them. Preserve literal entity values and typed/source distinctions.
- Browser inspection/disclosures retain focus, Escape, hashes/history, complete
  detail and unsaved-edit status. PDF is a complete static saved report with the
  app's section/navigation contract. Never rewrite historical PDFs.

Apply the local paired browser/PDF review gate for either surface. Record both
impacts and justified medium differences. For changed PDFs generate/render actual
files and inspect every page; use desktop Playwright for changed browser behavior.
Respect the user's bounded verification scope and report deferred/unavailable
checks. Presentation never authorizes searches or model calls.

For operations use current `docs/operator-runbook.md`; the
[runbook snapshot](references/operator-runbook.md) and
[full AGENTS snapshot](references/repository-agents.md) preserve local gates.
For production HTTP changes recheck the
[dated security checkpoint](references/production-http-checkpoint.md).
