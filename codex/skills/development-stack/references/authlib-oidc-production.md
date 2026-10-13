# Authlib OIDC Client Practices

Apply the relevant section when a Python service uses Authlib for either OIDC user login or JOSE/JWT bearer-token verification. These are separate trust flows: follow the configured issuer and token contract, and do not apply browser-login state or nonce requirements to an access-token-only API.

- Use the authorization-code flow, with PKCE `S256` when supported by the provider/client arrangement. Keep the authorization request's state, nonce, and PKCE verifier bound to the initiating server-side session and callback transaction. Do not disable Authlib state checks or accept a callback whose state does not match.
- For OIDC, request `openid`; generate a fresh unpredictable nonce when required by the provider or client profile, retain it with the transaction, and require the ID token nonce to match. Use Authlib's OIDC token parsing/validation path. If application code parses tokens directly, use trusted issuer metadata and the issuer's JWKS, validate signature, issuer, audience, expiry and nonce, and allow only the algorithms configured for that issuer. Do not treat a decoded JWT as validated identity.
- Pin the expected issuer and audience/client ID for each configured provider. Do not let request parameters choose an issuer, discovery URL, JWKS URL, or token endpoint; that creates an SSRF and trust-confusion boundary. Cache discovery/JWKS data through a maintained library, refresh when a signing key rotates, and fail closed when issuer metadata or signature validation cannot be established.
- Use the ID token to establish the login identity and an access token only for its intended API. Store refresh/access tokens server-side, encrypted at rest, associated with the right user/provider, and update the stored token when Authlib refreshes it. Limit requested scopes, expiry, and retention; never put tokens in browser JavaScript, URLs, logs, or analytics.
- Treat the session cookie and OAuth transaction state as security controls: use HTTPS, secure cookie settings, a strong server-side session secret, and an appropriate `SameSite` policy for the IdP callback flow. Protect token persistence with access controls and retention appropriate to the grant.
- Behind a reverse proxy, construct the callback from the configured public origin or trust forwarded headers only from known proxy hops. Do not derive registered redirect URIs from arbitrary `Host` or `X-Forwarded-*` values. Keep callback URIs exact and registered at the provider.
- Verify the actual installed Authlib integration's behavior for state storage, nonce validation, discovery, and JWKS refresh. Test mismatched state/nonce, issuer/audience, expiry, signing-key rotation, refresh-token update, and proxy-host spoofing without live user credentials.

## Bearer-token API verification

- At each protected API boundary, verify the token's signature with a trusted key and an explicit algorithm allowlist, then validate the issuer, this API's audience, required time claims (including `exp`, and `nbf` when issued), and issuer-specific required claims such as subject or tenant. Apply a small, explicit clock-skew allowance only when needed. Authlib's JOSE/JWT decoder does not replace application claim validation; use a claims registry or equivalent explicit checks.
- Obtain signing keys only from a configured, trusted issuer's metadata/JWKS endpoint. Match the token's `kid` to that key set, cache the set with a bounded refresh policy, and refresh on an unknown key to handle rotation. Do not follow a token-supplied `jku`/`jwk` URL or let untrusted token headers select an issuer or key endpoint; fail closed if no trusted key verifies the signature.
- After cryptographic and claim validation, enforce the API's authorization contract (required scopes/roles, tenant policy, subject, and object-level access) on the server. A valid signature alone grants no application permission.
- Do not require an OIDC browser redirect, authorization `state`, or login `nonce` for an API that only accepts bearer access tokens. If the same service also performs OIDC login, keep those callback checks confined to that login flow.
- Test invalid signatures and algorithms, unknown/rotated `kid`, wrong issuer or audience, expired/not-yet-valid tokens, missing required claims, and valid tokens lacking authorization. Use representative local test keys and claims rather than live credentials.

## Official references

- [Authlib Web Clients](https://docs.authlib.org/en/latest/oauth2/client/web/index.html)
- [Authlib Flask OIDC integration](https://docs.authlib.org/en/latest/oauth2/client/web/flask.html)
- [Authlib OAuth2 authorization code, state, PKCE, and OIDC token validation](https://docs.authlib.org/en/stable/oauth2/client/http/index.html)
- [Authlib JOSE/JWT guide](https://jose.authlib.org/en/guide/jwt/)
- [Authlib resource-server guidance](https://docs.authlib.org/en/stable/oauth2/resource-server/index.html)
- [joserfc algorithm allowlists](https://jose.authlib.org/en/guide/algorithms/)
- [Werkzeug `ProxyFix` and trusted proxy counts](https://werkzeug.palletsprojects.com/en/stable/middleware/proxy_fix/)
