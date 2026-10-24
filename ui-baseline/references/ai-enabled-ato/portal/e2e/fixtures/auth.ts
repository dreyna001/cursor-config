import { expect, type Page } from "@playwright/test";
import { setSspFixtureIdentity, type SspFixtureIdentity } from "./stack";

export async function loginViaDevOidc(
  page: Page,
  identity: SspFixtureIdentity = "owner",
): Promise<void> {
  await setSspFixtureIdentity(page.request, identity);
  await page.context().clearCookies();
  await page.goto("/login");
  await expect(page.getByText("ATO Workspace", { exact: true }).first()).toBeVisible();
  await page.getByRole("button", { name: "Sign in", exact: true }).click();
  await page.waitForURL(/\/ssp(?:\?|$)/, { timeout: 30_000 });
  await expect(page.getByRole("navigation", { name: "Primary" })).toBeVisible();
  await expect(page.getByRole("button", { name: /^Account:/ })).toBeVisible();
}

export async function expectAuthenticatedWorkflow(page: Page): Promise<void> {
  await expect(page.getByRole("navigation", { name: "SSP workspace" })).toBeVisible();
}

export async function signOut(page: Page): Promise<void> {
  await page.getByRole("button", { name: /^Account:/ }).click();
  await page.getByRole("button", { name: "Sign out", exact: true }).click();
  await page.waitForURL(/\/login/, { timeout: 15_000 });
}
