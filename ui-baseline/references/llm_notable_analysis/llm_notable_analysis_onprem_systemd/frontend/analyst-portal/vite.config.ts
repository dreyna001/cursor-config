/// <reference types="vitest/config" />
import path from "node:path";
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig, loadEnv } from "vite";

const portalTarget = process.env.VITE_PORTAL_API_TARGET ?? "http://127.0.0.1:8765";
const devUser = process.env.VITE_PORTAL_DEV_USER ?? "dev-preview@local";
const devProxySecret = process.env.PORTAL_DEV_PROXY_SECRET ?? "portal-secret";

export default defineConfig(({ mode }) => {
  // Public VITE_ values can enter browser assets, even when used by the dev proxy.
  const legacyEnv = loadEnv(mode, process.cwd(), "VITE_PORTAL_DEV_PROXY_SECRET");
  if ("VITE_PORTAL_DEV_PROXY_SECRET" in legacyEnv) {
    throw new Error(
      "Use server-only PORTAL_DEV_PROXY_SECRET; VITE_PORTAL_DEV_PROXY_SECRET exposes secrets to browsers.",
    );
  }
  return {
    plugins: [react(), tailwindcss()],
    resolve: {
      alias: {
        "@": path.resolve(__dirname, "./src"),
      },
    },
    // Let route imports determine chunk ownership; vendor grouping eagerly loaded Markdown.
    build: { manifest: true },
    test: {
      environment: "jsdom",
      env: { TZ: "UTC" },
      setupFiles: ["./src/test/setup.ts"],
      exclude: ["**/node_modules/**", "**/e2e/**", "**/e2e-local-workflow/**"],
    },
    server: {
      host: "127.0.0.1",
      port: 5173,
      proxy: {
        "/api": {
          target: portalTarget,
          // Keep the browser Host (5173) so portal same-origin checks match Origin.
          changeOrigin: false,
          configure: (proxy) => {
            proxy.on("proxyReq", (proxyReq) => {
              proxyReq.setHeader("X-Forwarded-User", devUser);
              proxyReq.setHeader("X-Notable-Portal-Proxy-Secret", devProxySecret);
            });
          },
        },
        "/health": { target: portalTarget, changeOrigin: true },
        "/ready": { target: portalTarget, changeOrigin: true },
      },
    },
  };
});
