# Playwright End-to-End Tests

Read when a React project uses Playwright for browser-level user flows. Keep browser E2E coverage limited to contracts that need a real browser and deployed application wiring.

- Give each test independent browser state and controlled test data. Reuse an authenticated `storageState` only when tests do not mutate shared server-side account state; otherwise isolate accounts or data by worker/test. Treat saved browser state as a credential: store it outside source control, expire it, and use a least-privileged test account.
- Use the configured `webServer` and `baseURL` for a local/test instance when applicable. In CI, avoid silently reusing an unrelated server; make readiness and startup failures visible. Tests should not depend on live third-party pages or uncontrolled production data.
- Make setup and cleanup retry-safe. Playwright may replace a worker after a failure and rerun a test; a retry must not inherit or collide with the failed attempt's data. Prefer unique identifiers and controlled fixtures to serial ordering.
- Capture traces on retry or failure when useful for diagnosis, rather than recording every passing test by default. Traces, screenshots, videos, and reports can include page content, URLs, request data, and auth state: restrict their retention and access, and sanitize artifacts before sharing them outside the trusted team.
- Prefer user-visible locators and retrying assertions. A passing browser test demonstrates the covered user path only; it does not establish API authorization, cloud identity, or service availability beyond what the test environment exercised.
- For material desktop UI or browser-flow changes, run focused checks in Chromium, Firefox, and WebKit using the existing harness; report unavailable engines instead of treating one browser as complete coverage.

## Official references

- [Playwright authentication and storage state](https://playwright.dev/docs/auth)
- [Playwright test isolation](https://playwright.dev/docs/browser-contexts)
- [Playwright best practices and controlled test data](https://playwright.dev/docs/best-practices)
- [Playwright local web server configuration](https://playwright.dev/docs/test-webserver)
- [Playwright test retries](https://playwright.dev/docs/test-retries)
- [Playwright trace configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace)

## UI/UX change workflow

Start with the permanent local UI baseline's **Workflow and popup regression
coverage** section (or the app's released baseline fallback). Use this procedure
for every UI/UX change. A small visual/copy edit needs a focused rendered check;
interaction changes need the relevant workflows and failure paths. Keep the
matrix proportional to the affected surfaces; never silently omit browser verification.

1. Map the changed route, user role, state and intended behavior to existing
   browser tests. Start the isolated local/test app with controlled records.
2. Use Playwright to navigate, click, type and submit as a user would. Check the
   visible result and important state/request outcomes, not just that clicks work.
3. Exercise the relevant keyboard, error/retry, pending-request, repeated-action,
   stale-response and unsaved-edit paths required by the central baseline.
4. For visual/reflow changes, inspect screenshots and actual browser geometry,
   including required desktop zoom levels and every affected popup/action. Follow
   the requested desktop/mobile scope; do not add mobile work implicitly.
5. Run relevant supported browser engines, save concise results and reproductions,
   and identify untested roles/states. API-mocked browser tests are UI integration
   evidence; reserve full-stack E2E claims for real isolated application boundaries.

Use Playwright with Chromium, Firefox and WebKit for the relevant browser checks.
Use screenshots and computed geometry/styles for visual assertions, keyboard
input for focus/navigation, and headed native browser zoom for reflow. Vitest
component tests and TypeScript/build checks supplement browser verification;
they do not replace it. Record unavailable engines or blocked checks as unverified.

The baseline owns shared acceptance rules. This guide owns how to execute them;
do not create a second visual standard or claim complete coverage from one test.
