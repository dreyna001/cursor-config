# Alignment analysis and verification

Recorded 2026-10-23 for Suite Workspace UI Standard **v1.4.0**.

**Yes—the three products were analyzed and aligned to one shared baseline.**
The scope covered six frontends: Threat Hunting, ATO, and the AWS GovCloud,
AWS commercial, Azure and on-premises variants of Incident Response.

## What the analysis resolved

- The older HTML adaptation text disagreed with later approved sidebar/account
  rules. The versioned baseline now owns those rules; HTML is a generated companion.
- Older ATO notes used a 208px sidebar and Roboto Mono. The later approved 256px
  sidebar and shared Public Sans / platform monospace rules take precedence.
- Older template icons, spacing and selected navigation colors were superseded
  by the approved sidebar rules, not restored over the newer apps.
- App-owned controls, login/account flows, identity fallbacks, layouts, features,
  permissions, draft/review guards and exports retain their intended behavior.

See the [baseline reconciliation record](README.md#reconciliation-record--2026-10-23)
and [preservation boundaries](README.md#preservation-boundaries-and-shared-palette).

## Evidence from the completed release

- All six shared stylesheets were checked for parity with the contract.
- All six frontend builds passed. Focused unit tests and **135 browser cases**
  passed: 48 Hunt, 27 ATO and 60 across the four Incident Response variants.
- Browser checks covered Chromium, Firefox and WebKit, including sidebar
  geometry/text, navigation states, account interactions and workflow preservation.
- The consistency checker rejected deliberate CSS divergence and a stale embedded
  baseline. The generated template was also checked in all three browsers.
- Runtime preservation checks confirmed that the v1.4 reconciliation changed no
  application behavior or CSS declarations; the runtime-file change was the shared
  stylesheet's version marker. Earlier approved UI alignment remained in place.

The release merged to remote main in Hunt PR 74, ATO PR 28 and Incident Response
PR 41. Exact release commits and original file hashes are in [manifest.json](manifest.json).
The three temporary worktrees for that completed release were verified and removed.

These were local build/unit/browser checks with synthetic API and identity
fixtures, not a live cloud or Entra deployment qualification. GitHub-hosted CI
could not start because of the account billing/spend limit; a green hosted-CI
result is not claimed.

## This local installation

This change only installs the reference bundle and redirects personal skills and
rules. It does not modify any app checkout or deploy/reconfigure a service.
The Windows and WSL entrypoints open the same physical bundle. Core index links
resolve locally, and the published source baseline is retained byte-for-byte.

## Saved verification records

- [Frontend command results](evidence/baseline-test-results.json)
- [Release change scope](evidence/baseline-change-scope.json)
- [Hunt browser checks](evidence/baseline-check-hunt.log)
- [ATO browser checks](evidence/baseline-check-ato.log)
- [Incident Response GovCloud checks](evidence/baseline-check-s3_notable_pipeline.log)
- [Incident Response commercial checks](evidence/baseline-check-s3_notable_pipeline_commercial.log)
- [Incident Response Azure checks](evidence/baseline-check-azure_notable_pipeline.log)
- [Incident Response on-premises checks](evidence/baseline-check-llm_notable_analysis_onprem_systemd.log)
