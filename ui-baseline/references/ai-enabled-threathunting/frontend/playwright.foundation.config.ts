import { defineConfig } from "@playwright/test";

// Isolated foundation fixtures need source-serving Vite, not a production SPA fallback.
// Product journeys remain in the application's existing Playwright configuration.
export default defineConfig({
  testDir: "./e2e",
  testMatch: "suite-foundation.spec.ts",
  metadata: { suiteFoundation: true },
  workers: 2,
  retries: 0,
  timeout: 30_000,
  use: { baseURL: "http://127.0.0.1:5781", viewport: { width: 1440, height: 1000 }, trace: "retain-on-failure" },
  outputDir: "test-results/foundation",
  webServer: {
    command: "npm run dev -- --host 127.0.0.1 --port 5781 --strictPort",
    url: "http://127.0.0.1:5781/e2e/fixtures/suite-foundation.html",
    reuseExistingServer: false,
    timeout: 30_000,
  },
  projects: [
    { name: "chromium", use: { browserName: "chromium", launchOptions: process.env.SUITE_UI_CHROMIUM_EXECUTABLE_PATH ? { executablePath: process.env.SUITE_UI_CHROMIUM_EXECUTABLE_PATH } : undefined } },
    { name: "firefox", use: { browserName: "firefox" } },
    { name: "webkit", use: { browserName: "webkit" } },
  ],
});
