# Authorization-ready applications

Apply when adding, changing, or reviewing a production service, API, or public endpoint. Preserve existing local protections; production deployment controls do not require retrofitting developer/test instances unless requested.

For detailed production HTTP quotas, health behavior, route exposure, and access controls, read [API abuse and exposure](api-abuse-and-exposure.md). Keep named-repository observations in [project HTTP security checkpoints](api-project-checkpoints.md).

- Identify users uniquely. Recommend MFA for privileged and ordinary users. Outside a FedRAMP authorization, treat MFA as mandatory only when explicit customer policy requires it. Do not echo secrets or authenticators.
- Outside a FedRAMP authorization, an absent MFA control is a recommendation or finding. Do not implement MFA or migrate the identity provider unless that change is requested. Confirm the approved identity architecture first.
- Enforce authorization on the server. Keep privileges narrow. Lock out or back off repeated authentication failures.
- End sessions after the approved idle and absolute limits. Do not invent those limits.
- Routes that work without identification are an explicit allowlist. Everything else requires authentication.
- Allow remote access only through the approved path.
- Log authentication, authorization denial, admin action, configuration change, and quota breach with time, actor, source, and outcome. Do not log secrets. Make a logging failure visible. Keep logs for the approved retention period.
- Enforce production HTTP admission and resource bounds using the API abuse and exposure reference; keep quota breaches monitorable.
- Use TLS. Use the platform's approved cryptographic module and at-rest encryption. Do not invent a cipher and treat it as approved. Bind a session to the authenticated caller.

## FedRAMP levels on AWS GovCloud

Before creating or changing a GovCloud instance, ask whether the FedRAMP authorization is Low, Moderate, or High when that level is not already stated. Do not choose a level. Presence in the GovCloud partition is not a level.

Validate the applicable FedRAMP Rev 5 baseline and approved system control implementation before declaring a gap. Missing evidence is unverified coverage, not proof of absence. Do not add an identity provider or a second backup system unless that change is requested.

- MFA for both privileged and non-privileged access, with replay-resistant authentication.
- FIPS-validated or NSA-approved cryptography for required cryptographic functions, including transmission and data at rest.
- For backup controls, use the [shared conditional backup reference](../../cloud-native-platform-architecture/references/data-protection.md#map-schedules-to-requirements-keep-evidence-separate). Document how any applicable daily incremental / weekly full wording maps to native managed-service recovery behavior; do not prescribe duplicate jobs or claim equivalence without evidence.
- Authenticators at NIST SP 800-63 authenticator assurance level 1 for Low.

For Moderate and High backup controls, verify restore-testing and cryptographic-protection obligations against the applicable baseline and approved implementation using that shared reference. An untested restore stays unknown. Moderate and High also require no embedded unencrypted static authenticators, individual authentication when a group authenticator is used, and account access through a separate device. Moderate requires authenticator assurance level 2.

For High backup controls, also verify applicable sampling, separate-storage and alternate-site outcomes; do not infer a mandatory new vault or region from those outcomes alone. High also requires authenticator handling for multiple system accounts and expiration of cached authenticators.

- Validate input. Return errors without internal detail. Do not expose debug or test routes in production.
- Check dependencies for known vulnerabilities in CI. Sign artifacts where the pipeline already signs them. Change cloud infrastructure with Terraform. Do not add an unsupported runtime.
