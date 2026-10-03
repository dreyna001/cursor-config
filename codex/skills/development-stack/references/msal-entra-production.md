# MSAL and Microsoft Entra Browser/Backend Authentication

Apply when a browser application or backend uses Microsoft Authentication Library (MSAL) with Microsoft Entra ID. Keep browser and server responsibilities distinct, and follow the application's registered platform and customer's tenant/cloud policy.

## Browser application

- For a SPA, use MSAL Browser as a public client with authorization code plus PKCE. Do not place a client secret, certificate, or other confidential credential in browser code, Vite environment variables, source maps, or static build output.
- Register the exact SPA redirect URI and request only the API scopes the feature needs. Use `acquireTokenSilent` first and handle the library's interaction-required result with the application's chosen popup or redirect flow. Let MSAL manage token renewal; do not parse access tokens in the browser to make authorization decisions.
- Choose token-cache persistence to match the threat and UX requirements. Browser cache is accessible to code running in the origin, so prevent XSS, do not export tokens to app state/logging, and do not mistake local storage for a secure secret store.
- A public client ID and authority configuration are not secrets. Any `VITE_*` values are compiled into the client bundle; put confidential credentials and privileged service configuration on the server.

## Backend and API

- A backend web app that signs users in is a confidential client; configure it as registered and keep its client credential server-side, using a certificate or governed secret storage according to the project's supported flow. Managed identity is appropriate for app-only access to Azure resources when the target service and chosen SDK/flow support it; it is not a general replacement for the confidential-client credential in a user sign-in flow. A web API must independently validate incoming access tokens for its configured issuer/tenant, signature, lifetime, and audience, then authorize required delegated scopes (`scp`) or application roles (`roles`) and the requested object/tenant. A successful SPA sign-in does not authorize a backend operation.
- Keep authentication separate from authorization: validate the token and then enforce server-side user, tenant, object ownership, and business permissions. Use on-behalf-of only when a backend needs to call a downstream API on the signed-in user's behalf; use an app-only flow only for genuinely app-owned work.
- Keep the backend's token cache protected and user/account-scoped when delegated tokens are persisted. Use MSAL's silent acquisition/cache APIs and handle reauthentication/consent requirements explicitly; never log or return refresh tokens.

## Authority, endpoint, and evidence

- Treat cloud instance, authority host, resource endpoint, and scope/audience as one deployment configuration. Do not mix commercial Azure with Azure Government or infer an API's token audience from its DNS hostname. For example, Azure AI Search uses `https://search.azure.com/.default` in Azure public and `https://search.azure.us/.default` in Azure Government; Azure Storage service endpoints also differ by cloud. Use the official MSAL national-cloud configuration and each service's endpoint/audience documentation.
- Confirm the tenant/account audience and redirect registration match the target environment. Exercise access-token expiry, silent acquisition failure, required interaction, wrong tenant/issuer/audience, missing scope/role, and denied object access. Use test registrations and identities, not production credentials, in automated tests.

## Official references

- [MSAL authentication flows](https://learn.microsoft.com/en-us/entra/msal/msal-authentication-flows)
- [MSAL Browser token acquisition and caching](https://learn.microsoft.com/en-us/entra/msal/javascript/browser/acquire-token)
- [Public and confidential client applications](https://learn.microsoft.com/en-us/entra/msal/msal-client-applications)
- [Microsoft Entra authorization-code flow and SPA redirect requirements](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow)
- [Validate access tokens at a web API](https://learn.microsoft.com/en-us/entra/identity-platform/access-tokens)
- [MSAL national-cloud configuration](https://learn.microsoft.com/en-us/entra/identity-platform/msal-national-cloud)
- [Azure AI Search keyless connections and cloud endpoints](https://learn.microsoft.com/en-us/azure/search/keyless-connections)
- [Azure Queue Storage authorization and cloud-specific resource IDs](https://learn.microsoft.com/en-us/azure/storage/queues/authorize-access-azure-active-directory)
