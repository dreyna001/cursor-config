# Frontend deadline, forms/query and bundle review — 1.14.0

2026-10-24. Six independently deployable local frontends; no Python runtime change.

## Decisions and fixed failures

- Transport retains native Fetch and one shared cancellation/error model. The
  deadline now covers optional token preparation, response headers and body
  consumption. Late token completion cannot send a request. Browser-native body
  errors preserve timeout/cancellation classification; 204/205/304 bodyless
  responses remain valid. No automatic mutation retries were added.
- IR's nested default 30-second deadline no longer truncates its explicit
  220-second chat allowance. Reads default to 30 seconds, long mutations/chat to
  220 seconds, signed transfers/downloads to 120 seconds. ATO's generation stream
  retains its explicit heartbeat/idle/caller-cancellation policy.
- Scoped state uses React's subscription API. Restoration-only queue consumers
  do not subscribe to their own draft writes. IR filter changes wait for page
  reset before requesting, preventing a redundant old-cursor request. ATO session
  and Hunt list reads cancel superseded work and reject stale results.
- Forms retain native validation, existing controlled values, shared pending-submit
  protection, server field errors and app-specific draft/revision guards. ATO's
  large draft signature is memoized when unrelated state changes. No form or
  query framework was added: the demonstrated costs were ownership/cancellation
  problems, not missing framework features. React Hook Form and TanStack Query
  remain valid alternatives for a measured dynamic-field or shared-cache need;
  adding either here would require policy and workflow migration without fixing
  these causes by itself.
- ATO defers substantial pages while registering its history guard eagerly.
  Hunt defers substantial rendering modules until first use, retains visited
  panels and keeps eager stylesheet ordering. Shared citation-numbering helpers
  are separate from the report renderer. A browser network regression verifies
  that evidence/report code waits for the relevant view and is not fetched again
  when returning to an already visited panel.
  A failed Hunt panel leaves the surrounding shell and unsaved-work guards mounted.
  The reload action remains explicit. IR generates schemas without an unused
  Zodios/Axios client. Two IR vendor-group configurations were removed because
  their eager dependency graph loaded Markdown before it was needed.
- Existing skills/rules already cover this work. The baseline adds operation
  budgets, source parity and executable bundle budgets instead of another
  overlapping skill. All shared sources remain local copies in each frontend.

## Measured cold-start JavaScript

| Frontend | Before bytes | After bytes | Reduction |
|---|---:|---:|---:|
| ato | 892,111 | 479,514 | 46.2% |
| hunt | 812,718 | 611,956 | 24.7% |
| azure | 459,941 | 399,618 | 13.1% |
| onprem | 707,476 | 390,678 | 44.8% |
| gov | 992,237 | 763,799 | 23.0% |
| commercial | 570,382 | 510,080 | 10.6% |

Three cold Chromium contexts per before/after build, one local HTTP server,
1440×1000 viewport, identical anonymous `/login` inputs. Every requested JS asset
was counted once, including preload and dynamically requested dependencies;
these are not entry-chunk-only numbers. Identity was not supplied: ATO/Hunt/on-prem
render sign-in, Azure renders unconfigured sign-in, and AWS variants render
sign-in-required. Compare each app with its own prior build; these are not equal
cross-app authentication workloads. All six initial-screen before/after PNGs
are pixel-identical at this viewport; this is not an all-route pixel-equality claim.
Gzip figures in JSON are calculated at
level 9, not observed compressed transfer. No end-to-end interaction-latency or
production-network speed claim is made. Full-route JavaScript remains larger
than startup payload; deferred code still downloads when needed.

## Verification and limits

1639 unit checks; six typechecks and production builds;
162 shared component/foundation browser checks;
341 product workflow/UI checks;
48 queue/evidence recovery checks; 5 isolated real ATO API/PostgreSQL
journeys. The shared fixtures cover Chromium, Firefox and WebKit, including
native/schema validation, pending duplicate submissions, retry, keyboard focus,
dialog naming/containment, disabled/readonly states, enlarged content,
Back/Forward guards and session reset. Snapshot-only draft writes do not rerender
the restoration consumer; reactive consumers still update. IR filtered page-two
transitions make one first-page request and no old-cursor request.

An independent HTTP server stalled response bodies in all 18 frontend/browser
combinations. Both timeout and caller cancellation were exercised and server-side
socket close observed (36 cases). This proves browser transport cleanup; it does
not prove that accepted backend computation stops. Late token preparation may
finish inside an identity SDK, but cannot dispatch HTTP after the caller deadline.

Role/route evidence: shared fixtures are identity-neutral test surfaces. ATO's
`/ssp`, agency settings and management routes use synthetic authenticated editors;
the five real-backend journeys use controlled owner identity. Hunt's fixture
analyst exercises `/hunts`, new hunt, plan/evidence/report, Connections and Settings,
including enabled and guarded actions. All four IR variants use synthetic analyst
identity for `/cases`, case detail and assistant states. This is the configured
test-role matrix, not a complete production RBAC certification. Detailed route,
state and browser mappings are in the JSON role/state coverage record.

Real ATO run `run-dxqavg68` used isolated PostgreSQL/API state with controlled identity
and provider fixtures; cleanup is confirmed. Customer IdPs, live cloud/model
providers and actual screen-reader speech remain outside this local qualification.
Hunt remains desktop-only; its existing native-zoom exception is retained.
IR's externally provisioned `portal.spec.ts` is not credited as run.

The pass exposed and corrected bodyless-response handling, native browser error
translation and lazy stylesheet cascade issues. A pending-poll test's simulated
clock now stays below the new request deadline. Per-run trace directories are
separate; qualification is performed with application/fixture sources frozen.
Source equality complements browser evidence, not a substitute for it.

## Reproduction and future decisions

Each frontend: `npm run typecheck`, `npm run build`, `npm test`,
`npm run check:performance`, `npm run test:components`, `npm run test:foundation`.
Each repository: `python3 scripts/check_suite_ui.py` and
`python3 scripts/check_suite_foundation.py`; peers are optional development checks.
Keep separate trace/output directories for concurrent browser runs. Wait for
observable asynchronous completion rather than unrelated text appearing; consume
needed response bodies before navigation. Freeze app, shared-source, fixture and
configuration files during a browser run so hot reload cannot invalidate evidence.

Revisit form/query frameworks when profiles show a concrete need for field-level
subscriptions, multi-consumer cache invalidation or shared pagination ownership.
Revisit budgets using equivalent production routes and state, not a dev-server
comparison. Preserve cancellation, auth lifetime, revisions and uncertain writes.

Authoritative implementation references: [React lazy](https://react.dev/reference/react/lazy),
[React subscription API](https://react.dev/reference/react/useSyncExternalStore),
[OpenAPI generator templates](https://github.com/astahmer/openapi-zod-client).
