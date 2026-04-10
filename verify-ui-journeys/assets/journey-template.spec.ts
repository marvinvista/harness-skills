// Copy this template into repo-local browser tests and replace the placeholders.

import { test, expect } from "@playwright/test";

test("critical journey", async ({ page }) => {
  await page.goto("http://127.0.0.1:3000");

  // Replace selectors and assertions with repo-specific ones.
  await expect(page).toHaveTitle(/TODO/);
});
