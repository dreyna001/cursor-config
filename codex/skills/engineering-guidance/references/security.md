# Security

- Treat all external input as untrusted and validate at boundaries.
- Never build queries or shell commands from untrusted input.
- Validate and normalize file paths, URLs, identifiers, and model output before use.
- Prevent injection, unsafe deserialization, SSRF, path traversal, and regex DoS where applicable.
- Enforce authentication, authorization, least privilege, and tenant or ownership isolation server-side.
- Treat routes that work without authentication as an explicit allowlist. Every other route requires authentication.
- Never hardcode secrets or log tokens, credentials, or sensitive data.
- Use approved crypto and secure randomness only.
- Require schema validation and request-size limits where payload abuse is plausible.
- Avoid overly permissive exposure, verbose internal errors, and insecure defaults.
- Do not trust LLM output without validation before persistence, execution, or security-sensitive use.

## Scope and framework guidance

Apply these boundaries when the requested change handles authentication, untrusted content, files, external requests, or sensitive data. A layout-only edit does not require a full audit. Preserve existing protections in every environment; production headers and ingress controls do not require retrofitting local developer/test instances unless requested. Guidance does not authorize deployment, new external services, or unrelated remediation.

For installed-framework details, use the matching frontend and backend references in [security-best-practices](../../security-best-practices/SKILL.md); check actual versions and retain the approved authentication architecture. For production HTTP admission, route exposure and sessions, use [API abuse and exposure](api-abuse-and-exposure.md).

For browser-based OAuth/OIDC login, also follow the selected SDK guidance and [OAuth security BCP](https://www.rfc-editor.org/rfc/rfc9700.html#section-2.1.1) for transaction binding to the initiating browser. Keep those login checks separate from bearer-token-only APIs.

## Browser boundaries

- Render API, stored, uploaded and model-generated content as untrusted. Prefer framework-escaped text; disable raw HTML in Markdown unless the product needs it and sanitizes it with a maintained mechanism. Encoding or sanitization must match the actual HTML, URL or script sink.
- Validate navigation, return URLs and cross-window messages against approved destinations/origins and message schemas. Do not automatically load remote images or other active content from evidence or model output; preserve indicators as inert text or an explicit analyst action.
- Keep secrets out of bundles, public configuration and source maps. Review browser token storage through the selected authentication SDK; minimize persistence and clear applicable account caches on logout/account change. Do not prescribe a cookie/BFF migration or assume browser storage encryption defeats XSS. Never forward bearer credentials to unapproved origins.
- Define production CSP for the actual script, style, image, connection and authentication flows, with framing restrictions, MIME sniffing prevention and an approved referrer policy. Verify headers at the final serving layer, including redirects and error responses. Check route-level overrides and inheritance; for example, a Nginx location-level `add_header` can suppress parent headers under the default inheritance rules. Preserve required SSO popup/callback behavior; do not apply cross-origin isolation or HSTS scope/preload blindly.
- Treat sensitive API responses, downloaded evidence and browser persistence separately from public static assets. Use an explicit cache policy, normally `Cache-Control: no-store` for sensitive authenticated responses; keep them out of shared CDN/service-worker caches. Clear app-owned sensitive state on logout/account switch. Public hashed assets can retain their approved caching.
- Isolate active uploaded formats from the authenticated application origin or serve them as downloads with correct MIME type, safe disposition and `nosniff`. Assess sandboxing where previews are required; do not treat an extension or claimed MIME type as proof of safety.

## Backend boundaries

- Derive identity, tenant, role and resource scope from validated server-side context. Authorize every record, attachment, history, job and mutation, including list/search, indirect storage access and generated download URLs. Test cross-user/tenant/case/generation substitution where those scopes exist; preserve explicitly approved shared-case access rather than inventing per-user ownership.
- Allowlist writable and returned fields. Client bodies must not set server-owned identity, role, approval or ownership fields, and serialized responses must not expose internal data merely because it exists in storage. Validate token signature, algorithm, issuer, audience, expiry and required grants through the established verifier; fail closed.
- Constrain outbound destinations, schemes and credentials to approved integration contracts. Revalidate redirects and resolved addresses as appropriate to the fetcher; prevent metadata-service access and unapproved loopback/private destinations while preserving explicitly approved private integrations. Bound download bytes, time, decompression and parser work; page/character counts alone do not establish parser CPU or memory bounds. Verify bounds at the executing operation, including outstanding work after caller cancellation. Retain TLS verification and parameterized database queries.
- Authorize file access before storage lookup or signing; bound upload parsing and processing as well as wire bytes. Validate paths, object keys, actual content and filenames at their trust boundaries. Do not execute uploaded content; use supported parsers and isolation appropriate to enabled formats. Signed URLs require scoped objects, bounded expiry and an intentional cache policy.
- For direct-to-storage uploads, distinguish declared-size validation from a limit enforced on uploaded bytes by the storage service. Verify actual size before parsing; where the provider cannot enforce the declared cap, qualify bounded staged-storage usage and cleanup at the approved upload boundary. A signed URL and short expiry alone do not establish a byte cap.
- Keep tokens, signed URLs, uploaded content and sensitive evidence out of diagnostics and telemetry by default; retain redacted identifiers and protected audit records. Use scoped service credentials and existing secret management; do not add a new vault or rotation service solely to satisfy this rule.

## Qualification

Verify supported behavior alongside rejection: safe Markdown/links and rejected active content, permitted SSO flows, denied foreign redirects, and rejection of login callbacks from a different or missing initiating browser context, authorized resource access and substitution denial, approved private fetches and rejected destinations, safe uploads and rejected active/path inputs, sensitive response/cache/logout handling, and actual serving-layer headers. Use fixed local inputs and existing test boundaries; do not perform unapproved live scans or load tests. Passing local contracts does not establish deployed configuration or complete security.

For production runtime or dependency changes, qualify the deployed backend dependency set and built image as well as frontend packages; an evaluation-only environment or `pip check` does not substitute for vulnerability review of the shipped runtime. Use established scanners and locks without introducing unrequested scanner services or upgrades.

Check that CI actually runs the applicable locked frontend/build-tool and backend dependency audits, bundle secret checks, infrastructure scans and security regressions; a lockfile alone is not a vulnerability check. Compare installed release versions as well as source locks, and flag missing coverage within the review scope. Treat scanner results as evidence to investigate, not proof of exploitability or proof that every boundary is covered.

## Container and cloud security scans

- Use **Trivy** for vulnerability qualification of built container images across AWS, AWS GovCloud, Azure, Azure Government, GCP and other cloud or on-prem targets. Scan the actual release image/digest and platform, including OS and language dependencies; frontend audits or evaluation environments do not substitute for that image.
- Reuse the project's pinned scanner and an installed/cached matching version before downloading tools. Record image identity, scanner version, vulnerability database identity/date, scope and raw results. Offline scans must disclose database age; a timeout or missing results means incomplete qualification. Preserve narrower review-skill limits on installing scanners; missing tooling is a reported qualification gap unless the task authorizes installation.
- For Terraform configuration security checks, retain the established pinned scanner and reviewed exceptions; use Trivy configuration scanning when no scanner is established. Terraform formatting, validation, tests/plan review, IAM/network verification and live service acceptance retain their dedicated checks. Findings do not establish deployment configuration or exploitability.
- Apply the project's severity gate and report scanner completion separately from gate success. In the absence of an approved alternative release policy, unresolved HIGH/CRITICAL findings block production promotion. Separate finding rows from unique advisories and distinguish available fixes, vendor-deferred issues and verified non-applicability/backports. Preserve raw findings; any exception must be narrowly justified, scoped to exact artifacts/conditions, and reviewed under the project's approval policy.
- Use local commands or the authorized existing delivery pipeline. This guidance does not require GitHub Actions, authorize cloud deployment/credential changes, or override the user's selected runtime. Keep platform-specific commands and workarounds in project documentation.

## CI workflows

- Pin third-party GitHub Actions to a commit SHA.
- Set workflow `permissions` to the minimum. Prefer `contents: read`.
- Use cloud OIDC for deploy credentials. Do not put long-lived cloud keys in workflows.
- Do not combine `pull_request_target` with checkout of untrusted pull-request code.
- Keep secrets out of logs and `GITHUB_ENV`.
- Dependency audits, secret checks, infrastructure scans, digest-pinned images, and scanner triage stay in Qualification.

Sources: [Nginx header inheritance](https://nginx.org/en/docs/http/ngx_http_headers_module.html#add_header), [OWASP response headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html), [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html), [MSAL browser caching](https://learn.microsoft.com/en-us/entra/msal/javascript/browser/caching).
