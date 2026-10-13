# Secure-by-Default Infra and Ops

- Do not embed secrets, tokens, or long-lived credentials in images, unit files, compose files, or committed scripts. Use env files, secret managers, or host-only configuration as appropriate.
- Bind sensitive inference or admin APIs to **loopback** unless a documented edge listener is required; document exposure and auth.
- Run services as **dedicated unprivileged users** where supported; use `ProtectSystem`, `ReadWritePaths`, and minimal filesystem permissions consistent with the stack.
- Prefer **explicit restart and health** behavior (`Restart=`, health checks, idempotent installers) over fragile implicit startup.
- For TLS: verify by default; disabling verification is only for documented lab scenarios, never as a silent default in production paths.
- For a production public service, enforce TLS and HTTP admission/resource bounds at the edge and in the application. Read [API abuse and exposure](api-abuse-and-exposure.md) for route and anonymous coverage. Do not retrofit production deployment controls into developer/test instances unless requested; retain existing protections.
