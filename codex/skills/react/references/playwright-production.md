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
