# Frontend and backend URL routing

Use this reference when adding or changing application routes, browser navigation,
deep links, or the boundary between frontend pages and backend APIs. Preserve the
project's router, API design, auth integration, and deployment layout; this is a
behavior standard, not a mandate to add a routing library or redesign routes.

## Make navigation durable

- Give meaningful screens and addressable records stable, human-readable URLs.
  Treat the URL as the source of truth for navigable state so opening a link,
  refreshing, or using Back/Forward returns to the same view. Use the router or
  History API without full-page reloads where the app is a single-page app.
- Put resource identity and view hierarchy in the path. Put safe, shareable view
  state such as filters, sorting, page/cursor, time range, or a selected record
  in query parameters. Use a fragment for an in-page section or anchor when
  appropriate. Keep ephemeral interaction state local when users would not
  expect a copied link to preserve it.
- Preserve stable citation identity in evidence links. Where the product's
  citation contract requires a record ID and evidence snapshot/version, retain
  those parameters and resolve the referenced source through the authenticated
  backend. Do not silently substitute the currently selected or latest record.

## Keep browser routes and APIs distinct

- Treat frontend routes as navigation and API routes as data/action contracts.
  A page route should load its data through the API; opening a URL should not
  itself perform a consequential write. Use GET for reads and POST, PUT, PATCH,
  or DELETE for explicit writes; never perform state changes through GET. Apply
  server-side validation, authentication, authorization, and tenant/object scope
  checks on every API request. Hiding a link or guarding a frontend route is not
  authorization.
- Configure SPA hosting to serve the application shell for valid frontend
  document routes on direct navigation and refresh. Keep API paths, static
  assets, identity-provider callbacks, health endpoints, and other server-owned
  paths on their intended handlers; unknown API and asset paths should retain
  their normal error responses instead of returning the SPA shell.
- Respect the configured router basename, reverse-proxy prefix, and identity
  provider callback paths. Do not make deployment-specific path assumptions.

## Keep URLs safe and transitions correct

- URLs can appear in browser history, logs, analytics, and referrer data. Never
  put passwords, access/session tokens, secrets, raw evidence, unsaved report
  text, or other sensitive content in paths, queries, or fragments. Include
  record identifiers only when the application already treats them as safe
  references and the server enforces access on retrieval.
- When authentication carries a return destination, accept only a validated
  internal route matching the app's route allowlist. Reject external and
  protocol-relative destinations, strip unnecessary or sensitive parameters,
  and preserve the identity provider's callback and renewal behavior.
- If a route change would discard edits, use the application's established
  save/discard/confirm behavior for links and browser Back/Forward. Keep the
  address bar and rendered view aligned; do not silently lose edits or leave a
  stale URL after canceling navigation.
- Handle direct links, invalid or missing identifiers, signed-out and
  unauthorized access, deleted records, and unavailable data with clear states.
  Recheck access on the server even when a user reaches a deep link. When route
  parameters change during an async request, cancel the old request or ignore
  its stale response so it cannot overwrite the newly selected view.

## Verify the route contract

Check direct loading and refresh for each important route, Back/Forward, query
and fragment restoration, saved citation links to the same record and snapshot,
dirty-edit navigation, invalid IDs, signed-out/forbidden access, and stale async
responses. Verify SPA fallback separately from API, asset, auth-callback, and
health responses. Keep tests desktop or device coverage aligned with project
policy; do not add an unrelated routing library or rewrite to satisfy this
checklist.
