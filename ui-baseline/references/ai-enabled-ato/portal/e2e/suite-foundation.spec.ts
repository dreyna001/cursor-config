import { test, expect } from "@playwright/test";
test.beforeEach(async ({}, info) => { test.skip(info.config.metadata.suiteFoundation !== true, "Dedicated shared-foundation fixture only"); });
test("router preserves guarded Back/Forward and scoped state resets with session", async ({ page }) => {
  await page.goto("/e2e/fixtures/suite-foundation.html#first");
  await page.getByRole("button", { name: "Increment shared count" }).click();
  await page.getByRole("link", { name: "Second page" }).click();
  await expect(page.getByTestId("route")).toHaveText("#second");
  await expect(page.getByRole("status", { name: "Shared count" })).toHaveText("1");
  await page.getByLabel("Title", { exact: true }).fill("Unsaved");
  const dismissed = page.waitForEvent("dialog").then(dialog => dialog.dismiss());
  await page.goBack(); await dismissed;
  await expect(page).toHaveURL(/#second$/);
  await expect(page.getByTestId("route")).toHaveText("#second");
  await expect(page.getByLabel("Title", { exact: true })).toHaveValue("Unsaved");
  await page.getByRole("button", { name: "Keep draft and clear guard" }).click();
  await page.goBack(); await expect(page.getByTestId("route")).toHaveText("#first");
  await page.goForward(); await expect(page.getByTestId("route")).toHaveText("#second");
  await page.getByRole("button", { name: "New session" }).click();
  await expect(page.getByRole("status", { name: "Shared count" })).toHaveText("0");
  await expect(page.getByLabel("Title", { exact: true })).toHaveValue("");
});
test("native and schema validation, pending duplicate submission, failure and retry preserve draft", async ({ page }) => {
  let requests = 0; let release!: () => void;
  const gate = new Promise<void>(resolve => { release = resolve; });
  await page.route("**/foundation-save", async route => { requests++; if (requests === 1) { await gate; await route.fulfill({ status: 503, body: "unavailable" }); } else await route.fulfill({ json: { saved: true } }); });
  await page.goto("/e2e/fixtures/suite-foundation.html");
  await page.getByRole("button", { name: "Save", exact: true }).click();
  await expect(page.getByLabel("Title", { exact: true })).toBeFocused(); expect(requests).toBe(0);
  await page.getByLabel("Title", { exact: true }).fill("x");
  await page.getByRole("button", { name: "Save", exact: true }).click();
  await expect(page.getByRole("alert")).toHaveText("Enter at least two characters."); expect(requests).toBe(0);
  await page.getByLabel("Title", { exact: true }).fill("Valid title");
  await page.getByRole("button", { name: "Save", exact: true }).click();
  await expect(page.getByText("Saving…", { exact: true })).toBeVisible();
  await page.getByRole("form", { name: "Example form" }).evaluate(form => { form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true })); });
  expect(requests).toBe(1); release();
  await expect(page.getByRole("alert")).toHaveText("Save failed. Retry.");
  await expect(page.getByLabel("Title", { exact: true })).toHaveValue("Valid title");
  await page.getByRole("button", { name: "Save", exact: true }).click();
  await expect(page.getByText("Saved.", { exact: true })).toBeVisible(); expect(requests).toBe(2);
});

test("draft persistence updates reactive readers without rerendering snapshot-only forms", async ({ page }) => {
  await page.goto("/e2e/fixtures/suite-foundation.html");
  const renders = await page.getByLabel("Snapshot writer renders").textContent();
  await page.getByRole("button", { name: "Save queue draft", exact: true }).click();
  await page.getByRole("button", { name: "Save queue draft", exact: true }).click();
  await expect(page.getByLabel("Shared count")).toHaveText("2");
  await expect(page.getByLabel("Snapshot writer renders")).toHaveText(renders!);
  await page.getByRole("button", { name: "New session", exact: true }).click();
  await expect(page.getByLabel("Shared count")).toHaveText("0");
});

test("a failed deferred panel preserves its parent draft and navigation guard", async ({ page }) => {
  await page.goto("/e2e/fixtures/suite-foundation.html");
  await page.getByRole("link", { name: "Second page", exact: true }).click();
  await page.getByLabel("Title", { exact: true }).fill("Keep this draft");
  await page.getByRole("button", { name: "Load unavailable panel", exact: true }).click();
  await expect(page.getByRole("alert")).toContainText("could not load");
  await expect(page.getByRole("button", { name: "Reload workspace", exact: true })).toBeVisible();
  page.once("dialog", dialog => dialog.dismiss());
  await page.goBack();
  await expect(page.getByTestId("route")).toHaveText("#second");
  await expect(page.getByLabel("Title", { exact: true })).toHaveValue("Keep this draft");
});
