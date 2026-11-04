# Small portal routing

Use this pattern when an app has a small set of peer workspaces and no distinct
home page. Adapt paths and landing behavior to the product; a default destination
is a convenience, not a statement that its workspace is more important.

## Routes and landing

- Give peer workspaces stable, direct routes and equal navigation weight, such
  as `/assistant` and `/cases`.
- Keep sign-in at a dedicated `/login` path when the hosting and identity provider
  allow it. Preserve provider callback routes and existing auth SDK behavior.
- Use `/` as an auth-aware entry: send signed-out users to sign-in; send
  signed-in users to a valid one-time return destination, otherwise their last
  visited workspace, otherwise the product-selected first-login workspace.
- Choose the first-login workspace per product. Do not make `/`, `/cases`, or
  another example a universal default. Keep peer workspaces directly reachable
  from shared navigation.

## Remembering destinations safely

- Save only the workspace pathname as the last-visited preference. Scope it by
  deployment and authenticated user so environments and accounts do not share
  navigation state. Do not store query strings, fragments, record identifiers,
  or credentials in this preference.
- Keep a pre-sign-in deep link as separate, short-lived, one-time return state
  only when needed. Validate it against the app's internal route allowlist;
  omit secrets, sensitive identifiers, and unnecessary query data. If invalid,
  use the remembered or first-login workspace.
- Treat browser storage as optional: handle unavailable, blocked, or malformed
  values and fall back to the product default without blocking sign-in.
- Clear pending return state on logout and account change. Ensure the logout
  transition cannot recreate a cleared return destination from the previous
  authenticated route.
- Preserve the app's existing auth SDK, callback and silent-renew behavior,
  router basename, direct-link refresh behavior, authorization checks, and
  capability boundaries.

## Verify the route lifecycle

Check first-login routing, last-workspace restoration, equal navigation to peer
workspaces, a valid deep link through sign-in, rejection of an unsafe return
destination, logout, account switching, blocked storage, and direct loading or
refreshing of each route. Include the identity provider's callback and router
basename when the app uses them.
