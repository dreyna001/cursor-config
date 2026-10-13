# Splunk SDK, SPL, And Search Jobs

Use this reference when building or reviewing a Splunk platform adapter. The Python SDK is a client for Splunk's REST API; check its current package/API docs and the target deployment's REST docs before relying on an endpoint, authentication parameter, or response behavior. Splunk Cloud and Enterprise can differ, and versioned REST endpoints are not interchangeable by guesswork.

## Bound access and query cost

- Give the integration a dedicated identity with only the capabilities, searchable indexes, and search-resource limits required by its authorized read operations. Avoid admin roles, writeback capabilities, and broad inherited roles. Splunk role permissions are additive, so inspect the effective role set and verify the integration identity against both allowed and denied indexes.
- Prefer trusted templates for fixed operations. If the workflow intentionally accepts generated SPL, treat it as untrusted input and submit it only after deterministic server-side policy validation. Validate the command set and query grammar, indexes, time bounds, resource and result limits, estimated cost, requester authorization, and effective Splunk role permissions; reject unknown or disallowed constructs. Generation alone does not authorize execution, and unvalidated model text must never reach Splunk.
- Require explicit `earliest_time` and `latest_time` for every search. Narrow the index and base predicates early, request only needed fields, and bound the result count, page size, and job concurrency. Do not rely on the REST API's default time range or a client-side row limit to bound server work.
- Keep credentials outside source, query strings, and logs. Use TLS and a supported token or credential flow for the deployed Splunk version; treat bearer tokens and session keys as secrets. Do not log raw events, sensitive query values, or authentication headers.

## Use the documented job lifecycle

- Use the SDK's supported job and result interfaces where they cover the operation. For REST calls, use documented endpoints and parameters; Splunk does not support or document endpoints containing `/admin/` in their URIs. Confirm the documented API version and Cloud limitations for the target.
- For a normal search job, retain its search ID, poll the job's documented state until a terminal outcome or deadline, then read bounded results. Page with server-side offsets/counts where needed and use the SDK's streaming result reader for large result sets. A client timeout does not itself prove that server-side search work stopped; cancel or delete an abandoned job through the documented operation and handle an already-expired job cleanly.
- Use the export endpoint only for one-pass streaming: it starts and streams a search without creating a search ID for later polling or retrieval. Do not treat export and job results as the same lifecycle.
- Record an internal request/template identifier, time bounds, Splunk search ID, result count, elapsed time, and typed failure. Keep event payloads and secrets out of diagnostics.

## Sources

- [Splunk Enterprise SDK for Python](https://github.com/splunk/splunk-sdk-python)
- [Create searches and manage search jobs with the REST API](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-tutorials/10.4/rest-api-tutorials/creating-searches-using-the-rest-api)
- [Splunk search endpoint reference](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-reference/10.2/search-endpoints/search-endpoint-descriptions)
- [Define Splunk roles with capabilities](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.4/manage-splunk-platform-users-and-roles/define-roles-on-the-splunk-platform-with-capabilities)
- [Role-based access and search restrictions](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/9.3/manage-splunk-platform-users-and-roles/about-configuring-role-based-user-access)
- [Splunk authentication tokens](https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/9.2/authenticate-into-the-splunk-platform-with-tokens/set-up-authentication-with-tokens)
- [Time modifiers](https://help.splunk.com/en/splunk-cloud-platform/search/spl2-search-manual/dates-and-time/time-modifiers)
- [Export search results with Splunk SDKs](https://help.splunk.com/en/splunk-cloud-platform/search/search-manual/10.3.2512/export-search-results/export-data-using-the-splunk-sdks)
