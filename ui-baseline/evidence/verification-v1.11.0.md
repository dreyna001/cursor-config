# Frontend stack qualification — baseline 1.11.0

Date: 2026-10-24. Scope: local working-tree candidate in all three repositories / six frontends. Not committed, merged or deployed.

## Result

All six frontends passed TypeScript checking, production builds, and 1541 unit tests in total. 221 selected Playwright cases passed with zero skips, flakes or failures in the accepted runs. Chromium 156.0.8078.4, Firefox 157.0 and Linux WebKit 27.2 were used with Playwright 1.64.1 and Node 24.22.1 / npm 11.19.1.

| Frontend | Unit tests | Browser cases | Browser serving mode |
| --- | ---: | ---: | --- |
| ATO | 404 | 36 | Vite development server |
| Threat Hunt | 196 | 65 | production preview |
| IR / Azure Government | 231 | 30 | Vite development server |
| IR / on-premises | 230 | 30 | Vite development server |
| IR / AWS GovCloud | 222 | 30 | Vite development server |
| IR / AWS commercial | 258 | 30 | Vite development server |

The version contract is [suite-frontend-stack.json](../suite-frontend-stack.json). [Machine-readable qualification](frontend-stack-1.11.0.json) includes exact scenario titles, source locations, engines, counts and timings. [Publisher metadata](frontend-publisher-metadata-20261024.json) records the stable package versions and peer/engine requirements returned on this date.

## Routes, roles, states and boundary coverage

- ATO /ssp and assistant/workspace dialogs
- Hunt /hunts, /hunts/new, /hunts/:id/{plan,investigation,evidence,report,activity,advanced}, settings/login/history
- All four IR /cases, /cases/:id, /assistant and conversation/capacity dialogs
- Roles: Synthetic analyst/workspace-owner fixtures, not every production authorization role.
- States: default, empty and populated, keyboard skip/focus and modal containment, disabled, pending, error, retry and completion, delayed responses, duplicate submissions and unsaved-navigation cancellation, 1280/1440/1920 desktop widths and enlarged text, native Chromium 100/200/400% zoom in ATO and all four IR variants.
- Dialogs retain accessible names and cancellation/focus behavior; ATO's Radix tab mouse activation was adjusted to prevent duplicate unsaved-draft guard prompts. Existing automatic keyboard activation remains.
- Neutral-field boundary contrast and shared heading/sidebar checks execute in the suite helpers. Loading/error/completion live-region checks inspect the accessibility tree, not spoken output.

## Additional checks

- Hunt Node 24.22.1 Alpine frontend Docker builder completed successfully
- IR on-prem, GovCloud, commercial and Azure server-only secret probes passed; retired public shell/dotenv names rejected
- Stack contract rejects a deliberately mismatched React version
- Six installed dependency sets, exact manifests/locks and shared CSS/release documents match the stack contract
- IR bootstrap scripts passed Bash and PowerShell syntax validation

## Harness corrections and implementation differences

- Hunt's broad `/api/` wildcard could intercept Vite source modules under `/src/api/`. API mocks now match the URL pathname beginning `/api/`. No workflow assertions were weakened.
- An initial Hunt source/dev run caused StrictMode duplicate-effect assertions to fail. The accepted run uses the application's existing production-preview convention; all 65 cases passed.
- An initial Azure run had no synthetic tenant build configuration and correctly stopped at “Sign-in is not configured.” The accepted run supplies synthetic Azure Government identifiers and replaces only the identity SDK. The app guard was preserved.
- The Playwright upgrade uses its matching browser binaries; older cached browser revisions were not used for qualification.
- Hunt shares the current React/Router/Tailwind toolchain while retaining its guarded history adapter, approved custom CSS and prefixed Tailwind utilities without Preflight. Product-specific authentication and layouts remain distinct.
- Python 3.12 does not require an older frontend version. Python 3.14 is a separate backend migration. The documented Zod 3 hold is caused by the generated client chain, not Python.

## Exclusions and remaining operational drift

- Synthetic local API and identity fixtures; real SSO, production backends, provider/model calls and durable deployment behavior not qualified
- Hunt native browser zoom not covered by this run; enlarged root text is covered separately
- Native Firefox/WebKit zoom not rerun; ordinary desktop layout/keyboard/state checks passed in all three engines
- WebKit is the Linux Playwright engine, not macOS Safari
- Mobile and actual screen-reader speech were excluded
- Production builds passed for all six; browser regression harnesses used source/dev for ATO/IR and compiled preview for Hunt. These timings are not a cross-app performance ranking
- No complete backend Python 3.14 qualification or full production container deployment was performed
- Inactive GitHub Actions files retain historical Node 22 selectors (and Azure Node 24 major). Repository policy excludes workflow maintenance without an explicit request. Update those selectors and requalify before any future reactivation.
- Existing running app services and globally installed Node executables were not replaced. Restart/rebuild each app with its checked-in .nvmrc and new assets when applying the candidate.

For reproduction, use the repository `.nvmrc`, `npm ci`, `npm run typecheck`, `npm run build`, `npm test`, and `python3 scripts/check_frontend_stack.py --installed`; use `check_suite_ui.py` with all peer roots for release parity. Preserve each product's documented Playwright configuration, authentication fixtures and required state coverage. Performance comparisons require equivalent compiled assets and data/cache policies across apps.
