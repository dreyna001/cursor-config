# Vite Build and Runtime Configuration

Read when building, configuring, or deploying a Vite application.

- Treat the browser bundle as public. Vite replaces `import.meta.env` values during build; variables with the configured public prefix (default `VITE_`) are visible to users in the shipped assets. Keep secrets, signing keys, and privileged credentials out of these values. Browser-facing API URLs can be intentional public configuration; `envPrefix` and `define` can also expose values, so review them as public API.
- Separate build-time configuration from runtime configuration. Changing a deployment environment variable after the static bundle has been built does not rewrite values already embedded in it. If one artifact must move between environments, obtain non-secret runtime settings through an explicit runtime config endpoint or server-rendered bootstrap; otherwise build and validate the artifact for each environment.
- Use the correct `base` path and mode for the deployment target. Test the built `dist` output at the actual subpath/hosting shape, including SPA fallback and asset URLs; the dev server is not proof that production static hosting is configured correctly.
- Keep local `.env.*.local` values out of version control. Treat checked-in `.env` values as public defaults, not secrets, and document which names are safe for client exposure.

## Official references

- [Vite environment variables and modes](https://vite.dev/guide/env-and-mode)
- [Vite production builds and base paths](https://vite.dev/guide/build)
- [Vite shared options and `envPrefix`](https://vite.dev/config/shared-options)
