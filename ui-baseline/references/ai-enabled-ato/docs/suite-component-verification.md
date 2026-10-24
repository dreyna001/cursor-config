# Shared component verification — v1.12.0

Verified on 2026-10-24 as a local working-tree candidate. No commit, merge or deployment is implied.
All six frontends carry the same 21 component/utility/fixture/configuration files from the canonical Hunt release. Source hashes, recorded native-control exceptions, app-local override checks and peer comparisons passed.

## Verification results

- 1541 frontend unit tests passed; all six type checks and production builds passed.
- 90 component interaction checks passed: five scenarios per frontend in Chromium, Firefox and WebKit.
- 340 product-workflow checks passed across the six frontends, including the explicitly recorded ATO stable-server repeat.
- Five ATO journeys passed using the real isolated PostgreSQL/API/OIDC stack and deterministic provider fixture: agency document settings, agency template upload/download, save-and-continue, rejected-middle-file upload retry, and lost-response upload reconciliation. The runner confirmed cleanup of its disposable database, storage and credentials.
- 18 rendered comparisons (six frontends × three engines) matched all measured component properties, including the dialog. This is equality for equivalent shared controls, not pixel identity of different product pages.
- The dedicated `npm run test:components -- --project=chromium` entry point was exercised successfully. Component fixtures are not sent to Hunt's compiled-asset product server.
- Negative controls proved rejection of a changed shared source, new native control, duplicate primitive under the UI folder, and an app-local variant override.

## Frontend and state coverage

- **ATO:** 404 unit tests; 15 component checks; 36 product-workflow checks.
- **Hunt:** 196 unit tests; 15 component checks; 184 product-workflow checks.
- **IR Azure:** 231 unit tests; 15 component checks; 30 product-workflow checks.
- **IR on-premises:** 230 unit tests; 15 component checks; 30 product-workflow checks.
- **IR GovCloud:** 222 unit tests; 15 component checks; 30 product-workflow checks.
- **IR commercial:** 258 unit tests; 15 component checks; 30 product-workflow checks.

All six component fixtures exercised normal/hover/focus, disabled, readonly, invalid and required field states; semantic badges; named modal title/description; Cancel-first focus; Tab/Shift+Tab containment; busy modal focus when actions are disabled; Escape/outside dismissal rules; failed request/retry; duplicate-submit suppression; focus restoration; select and tab keyboard behavior; constrained 640×480 desktop fit; enlarged text; and reduced motion.

Product journeys exercised the existing routes and synthetic identities rather than replacing their adapters. ATO retained revision/draft guards, System Setup tabs, source selection, assistant drafts, account/sign-out, review and export gates. Hunt covered its complete product E2E suite, including routes/history guards, plan approvals, retained evidence, source inspectors, report sections, settings, connections, programs, recovery and cancellation. All four IR variants covered cases and assistant routes, skip links, account controls, loading/failed state announcements, required inputs, guarded deletion, capacity popup fit and desktop zoom.

The ATO browser identity used a synthetic authenticated user; the isolated API journeys used the test owner identity. IR used each deployment's existing mock identity/capabilities. Hunt used its deterministic mock API session. These are not production SSO, an exhaustive role matrix or provider attestations.

## Preservation exceptions and limits

The approved exception inventory preserves compound navigation/record selectors, anchored non-modal context popups, native checkbox/file controls, monospaced editors, one-border assistant composers and existing login presentation. Ordinary actions, fields, badges and confirmation dialogs share the canonical primitives. Width, placement, wrapping and documented compact variants remain layout inputs, not separate component forks.

Native browser zoom at 100/200/400% was exercised by the existing Chromium desktop tests for ATO and four IR builds. Hunt's previously documented native-zoom exception remains; it retains desktop-width and enlarged-root-text checks. Browser semantics and keyboard evidence do not claim actual Narrator/NVDA/JAWS speech. Full production identity integration, external model services and the long all-controls ATO generation benchmark were not qualified here. Export endpoints/content contracts were preserved; no backend code was changed.

One ATO WebKit viewport check was repeated after an in-flight development-server restart removed its injected motion probe. The repeat passed with the server stable. A first mixed run sent Hunt's source-only component fixture to a compiled SPA server; the dedicated component configuration corrected that evaluation setup, and all six fixtures passed in all three engines. Neither incident was counted as a passing product check without separate evidence.

Routing implementation, HTTP client conventions, global/server state ownership, form orchestration and schema validation remain separate parity decisions. Shared dependency versions do not imply those implementations are already identical.

## Reproduce and maintain

Run `python3 scripts/check_suite_ui.py --peer <peer-one> --peer <peer-two>` from the canonical checkout, each frontend's build/unit suite, and `npm run test:components` in all six frontends. Run the affected existing product E2E suites and ATO's disposable runner for real-backend paths; keep fixture-only and deployed-stack claims distinct. The compact case record for this qualification is `suite-component-qualification.json`. Follow the baseline's “Keeping one baseline” procedure before publishing changes.
