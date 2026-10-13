# API Abuse and Exposure

Apply when designing, changing, or reviewing production HTTP APIs, listeners,
reverse proxies, authentication entry points, or health endpoints. Project notes
below apply only to their named repositories. These production controls do not
require retrofitting local developer or disposable test instances unless the user
requests it. Preserve existing protections in every environment. Rules identify
requirements and gaps; they do not authorize deployment, external changes, or
expanding a bounded task into unrelated hardening.

## Quotas and Resource Bounds

- Put per-client, per-route request quotas at the production edge and in the application. Use the configured trusted client address at the edge and authenticated identity in the app; do not trust browser-supplied identity or forwarding headers.
- Key routes by stable route templates so changing path identifiers cannot bypass admission limits.
- Cover every served route, including health, readiness, liveness, metrics, docs, OpenAPI, login/callback, static files, and any permitted test routes. Apply edge quotas to static files served directly by the proxy and app quotas to routes the app actually handles. Do not expose metrics or test routes merely to add a quota.
- Give anonymous callers separate quota buckets so they cannot consume signed-in caller budgets. For app routes without authenticated identity, key anonymous buckets by the trusted client address or verified client identifier supplied by the configured ingress, in a separate namespace from validated signed-in identities.
- Reject quota breaches with 429, log client, route, and time without secrets, and stop before handler execution or expensive authentication/database/model work. A late model-turn budget is not an HTTP admission quota.
- Configure the edge rejection status explicitly where needed; nginx's default request-limit rejection is 503, not 429.
- Cap request body size, request duration, and concurrent connections. Give uploads their own body cap and account for multipart parsing before handler-level file checks. Proxy read/send timeouts do not prove app work stopped; bound execution, cancellation, and outstanding work as appropriate.
- A shared gateway stage/account throttle is not a per-client block. Where such a gateway is used, put a per-client quota in front of it. Verify deployment settings; do not treat configurable defaults as approved production limits.
- AWS stage defaults configure method/route throttles, not necessarily a single cross-route bucket or hard ceiling. Keep client quotas at the approved ingress and preserve private ingress rather than adding a public edge.

## Reusable Starter Profile: `soc-small-team-v1`

This profile is a reusable starting point for a small SOC, not a customer
approval, compliance claim, or automatic production setting. Do not apply it to
local, developer, test, or disposable environments unless requested. Before
production use, the operator must approve the values and verify them against the
service capacity, enabled routes, ingress behavior, and deployment topology.

- Require an operator-supplied public HTTPS origin and trusted proxy CIDRs in
  both the application and the edge configuration. Ignore forwarded identity
  and client-address headers from peers outside those networks.
- Use a 30-minute idle session limit and a 12-hour absolute session limit.
- Limit verified callers to 180 requests/minute per user and stable route;
  anonymous callers to 60/minute per client IP and stable route; login to
  10/minute per client IP with a burst of 20; and health probes to 60/minute per
  client IP and endpoint.
- Provide pre-auth admission headroom of 3,600 requests/minute per client IP
  and route at the edge, sized for up to 20 users behind a shared NAT. Apply an
  app-side aggregate budget of 3,600/minute per client IP before account-store
  or password work, and check that edge route aggregation does not multiply
  the approved shared-NAT headroom.
- Cap JSON request bodies at 4 MiB and uploads at 25 MiB per file, with a
  120-second upload deadline. Set the edge and application wire-body limits
  consistently, allowing for multipart framing where applicable.
- Bound ordinary API work to 30 seconds. Keep readiness free of model calls,
  with a 2-second deadline and 5-second result cache; allow a 60-second startup
  grace. Derive planning deadlines from the existing model-call and repair
  budgets rather than imposing a separate shorter hard cut. Use a 150-second
  PDF deadline for the current 120-second rendering budget plus margin.
- Bound the application to 64 concurrent requests globally and 64 per client
  IP, and configure compatible edge connection limits. Application admission
  counters bound active requests, not the lifetime of TCP sockets.
- Process-local counters assume exactly one Uvicorn worker. If deployment uses
  multiple workers or replicas, require a shared admission mechanism or enforce
  the effective limits at a trusted edge; do not describe in-process counters
  as distributed quotas.

These starter values are not regulatory approval. Keep customer-specific
policies and exceptions explicit, and do not infer approval from the profile's
presence in configuration.

## Public Routes and Health

- Keep an explicit allowlist of routes permitted without authentication. Require server-side authentication and authorization on every other route. Include intended login/callback, health, and static routes in that inventory rather than treating them as undocumented exceptions.
- Liveness does no database, model, or remote work across the entire request path, including authentication/session middleware. Check cookie-bearing calls as well as anonymous calls.
- Keep readiness free of model calls, under an overall execution bound, briefly cached, and quota'd at the edge and in the app. Bound concurrent probe refreshes and choose a short cache interval consistent with operational detection requirements; never turn degraded readiness into success to reduce probe cost.
- Disable or authenticate interactive docs, ReDoc, and raw OpenAPI/schema routes in production. Check both application routes and edge forwarding; absence from a proxy template alone does not establish app-level protection or the live host's exposure.
- Check anonymous static asset packaging and SPA fallback paths for raw schema exposure as well as dedicated documentation endpoints.
- Quota login before account-store or login-state database access. Login lockout does not replace an HTTP quota.

## Authentication, Sessions, and Errors

- Check CSRF and the approved Origin on cookie-authenticated mutations.
- Retain cross-site write protection for ambient browser credentials, including HTTP Basic auth. Assess explicit bearer-token flows separately from cookie or platform-session flows.
- Reject or strip untrusted client-supplied identity/user/group headers. Accept identity only through the configured authentication path.
- Retain verified proxy/platform identity headers behind their enforced trust boundary and existing JWT/IAM, tenant, role and ownership checks.
- Keep CORS disabled when unnecessary; when needed, use an explicit approved origin list.
- End sessions on the approved idle and absolute limits. Verify production configuration rather than inventing new values.
- Enforce authentication-session limits at the responsible identity/session layer; token expiry and chat-history retention do not establish both limits.
- Where passwords are checked, enforce repeated-failure protection by account and client before further password checks. For OIDC/SSO, verify these controls at the identity provider instead of adding a duplicate local password mechanism; the app's login/callback quotas still apply.
- Return safe errors without stack traces, secrets, or internal details. Include a request/correlation ID consistently, including unhandled failures, and retain useful diagnostics in protected logs.

## Project Review Checkpoints

Recheck current code, the enabled routes, and installed production settings before
reporting any observation below as a current deployed gap. Preserve controls that
already exist; distinguish inactive templates from a live production host.

- **ATO (`ai-enabled-ato`, source review October 10, 2026):** Both production Nginx templates proxy `/health/live` and `/health/ready` with timeouts and no request quota. Check server-wide and per-client/per-route coverage on both locations, the API, login, and static paths. Active SSP chat defaults to 30 requests per 60 seconds per signed-in actor, with configurable production values; it limits model-turn attempts after some context work, not anonymous traffic, health, history reads, or all HTTP requests. Readiness probes dependencies on every call without a cache or overall deadline. Liveness's handler is simple, but cookie-bearing session middleware can access the database. Upload caps and proxy timeouts exist; complete admission/resource bounds still need checking. CSRF, ISSO/workspace authorization, identity-header rejection, and session expiry exist and must be retained. Default backend docs/schema routes have no production auth guard; supplied edge templates do not forward them. Verify the actual production IdP, CORS, session limits, and safe-error coverage.
- **Threat hunting (`ai-enabled-threathunting`, source review October 12, 2026; production deployment unverified):** Production-only HTTP admission, sessions and edge configuration are implemented behind an explicit runtime security profile. The single-host, single-Uvicorn-worker application enforces verified-user and separate anonymous quotas by normalized route, early login admission before account-store access, trusted proxy client derivation, bounded bodies/concurrency/deadlines, CSRF plus approved Origin, and persisted idle/absolute expiry. Background polling does not renew idle activity. Liveness avoids authentication/dependency work; readiness is cached and single-flight under a response deadline. Production docs/schema are disabled and raw-schema static paths are denied. The production Nginx selector consumes an export from the same validated runtime file; it covers login, API, health, static and denied paths with 429/logging, connection/body/timeout limits, response headers and request IDs. Preserve existing ownership, password-failure lockout and provider admission; provider admission still does not replace HTTP protection. Reverify the approved HTTPS origin, exact app/edge proxy CIDRs, generated edge environment, migration head and one-worker topology before deployment. MFA is absent. For a FedRAMP Low, Moderate, or High authorization, including AWS GovCloud, that absence is a gap. Outside a FedRAMP authorization it remains a recommendation unless customer policy requires it. Code/tests and native Nginx checks do not establish live ingress configuration or qualification of the pinned production container images.
- **Notable incident response (`llm_notable_analysis`, source review October 10, 2026):**
  - **AWS GovCloud and commercial:** `/health` and `/ready` are unauthenticated. GovCloud access remains restricted by its private API/VPC endpoint and approved agency network. Configurable default method/route throttles are 100 requests/second and burst 50, shared across callers; reviewed Terraform has no per-client/IP quota. Readiness probes DynamoDB, S3 and configured OpenSearch dependencies per request without a short cache. JSON parsing has no explicit application byte cap; signed S3 uploads have separate size/type/expiry bounds.
  - **On-prem:** the application allows `/health` and `/ready` without authentication, while the documented Nginx example inherits site Basic auth on those locations. Its IP-keyed `portal_chat` zone limits chat-prefix and attachment-content routes at 5 requests/minute with burst 2. Probes, other APIs and static routes have no configured request quota. Readiness checks PostgreSQL per request without a short cache. Basic auth does not prevent challenge flooding or provide a normal idle/absolute server-session lifecycle.
  - **Azure Government:** native `/health` and `/ready` require authenticated identity; SPA shell/assets use a broad unauthenticated static fallback. Readiness probes configured dependencies per request with bounded per-probe timeouts but no short cache or overall HTTP quota. The distributed signed-in chat quota does not cover anonymous/static traffic or every API route. Preserve the approved private ingress, Azure OpenAI embeddings and Microsoft semantic ranking.
  - **Across all four:** retain existing verified identity, CORS and upload controls. On-prem middleware protects docs/schema; review cloud static packaging for anonymous raw-schema exposure. Cloud login is delegated; no local password-login feature is implied. Some exception strings and incomplete request-ID correlation remain for qualification.

Provider/configuration semantics: [AWS REST throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html), [AWS HTTP throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-throttling.html), [Nginx request limits](https://nginx.org/en/docs/http/ngx_http_limit_req_module.html), [Nginx Basic auth inheritance](https://nginx.org/en/docs/http/ngx_http_auth_basic_module.html).

## Verification Coverage

Use isolated fixtures to check anonymous and signed-in quota isolation, route
coverage, early 429 rejection/logging with no handler side effects, payload and
upload caps, execution/connection bounds, readiness cache/refresh behavior, and
cookie-bearing liveness without dependency access. Verify public-route and
production docs/schema restrictions, CSRF/origin and identity-header rejection,
session expiry, IdP failure controls, and safe request-ID errors. Local tests and
inactive templates do not prove live production configuration. Do not load-test
or mutate a live production instance without authorization.
