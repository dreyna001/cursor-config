---
name: production-change-safety
description: Apply risk-based safety checks when planning, implementing, reviewing, or releasing changes that can affect a delivered customer product across on-premises, cloud, SaaS, or hybrid deployments.
---

# Production change safety

Keep supported customer installations, data, and integrations working through an update, restart, and recovery. Apply this from design through rollout to features, dependencies, configuration, infrastructure, installers, and release artifacts that can affect a delivered product.

## Scope and verification

Before implementation or review, identify the affected components, customer environments, supported versions, persistent state, and external contracts. Use the product's support matrix, release process, and applicable requirements. Resolve material unknowns before relying on a compatibility or recovery claim. Record why a potentially relevant check does not apply.

- **Compatibility and upgrades.** Against representative existing installs, configuration and data, verify every affected supported upgrade path, including skipped versions if supported. Cover clean installs, interruption, retry and restart where affected. Check supported OS, runtime, database, dependency and API versions. Test mixed client, server, worker and event versions that can coexist during phased rollouts. Preserve settings, credentials, certificates and permissions. Route contract changes through [API, data and distributed systems](../engineering-guidance/references/api-data-and-distributed.md).
- **State and recovery.** Exercise state-changing migrations and verify data and workflow invariants for affected records, files, sessions, transactions and queues. Test recovery from representative failures, including backup restoration and rollback or roll-forward as applicable. For migrations that can affect availability or data, define the single-run or concurrency guard, interruption and resume behavior, lock and downtime limits, and the last safe rollback point. Prove the recovery path beyond it. Verify schema and data compatibility separately from reverting binaries. Use [data protection](../cloud-native-platform-architecture/references/data-protection.md) for the storage in use.
- **Release integrity and operations.** For dependency, build or artifact changes, require evidence for applicable vulnerability scanning, SBOMs, signing, provenance and verification of delivered artifacts. For runtime changes, check affected workflows, integrations, security boundaries, performance and capacity. For infrastructure changes, check drift and affected networking, storage, DNS and IAM through the [Terraform standard](../terraform-cloud-deployment-standard/SKILL.md).
- **Deployment model.** For customer-managed installations, check applicable offline or air-gapped delivery, custom configuration, prerequisites, disk and permission checks, and interrupted installer recovery. For managed rollout, check applicable tenant, region and shared-service isolation. Limit exposure by ring, tenant or region where supported. Use a flag or kill switch when it can safely disable the affected capability. Apply both sets of checks at hybrid boundaries.

## Release gates

Use the existing release record. Bind the decision to the release or artifact, target and phase. Record affected upgrade paths, checks and linked results, recovery evidence, remaining risks and the decision owner. Recheck evidence after changes that invalidate it. Use **PASS** when required evidence passes and **BLOCKED** when required evidence is missing or failed.

**Non-waivable stops.** Block the affected release phase for any of the following:

- Missing authorization or unresolved customer, environment or resource ownership. For Terraform apply, enforce the [Terraform apply stops](../terraform-cloud-deployment-standard/SKILL.md#customer-apply-gate).
- Unresolved data loss or corruption, unauthorized access or tenant exposure, secret disclosure, or an affected security or data-integrity invariant that cannot be verified.
- Failed or missing evidence for an affected supported upgrade path, required recovery for a state-changing update, or the live checks required for promotion. Stop on a breached rollout threshold until recovery or correction is verified. Honor customer, regulatory and product requirements that prohibit an exception.

Use **APPROVED EXCEPTION** only for explicitly waivable checks. Record the authorized approver, release and environment, rationale, verified compensating controls, expiry and follow-up owner before proceeding. Exceptions apply only to the recorded phase and scope.

Before rollout, define health signals, thresholds, observation window, stop or recovery action, and operator. Make automated entry points fail closed on missing or failed checks and invalid exceptions. For checks the delivery path cannot automate, require an operator hold until the check passes or a valid exception applies. Record manual checks and their owner. When changing an entry point, verify that it refuses blocked or unreviewed inputs. Require customer post-upgrade checks or authorized production canary evidence before broader rollout or final sign-off, as appropriate.

For customer-visible changes, prepare [customer release notes](references/customer-release-notes.md) and any required upgrade and support notices before rollout. Release readiness is separate from source merge unless project policy ties them together. Follow existing authorization for deployment, customer access, and publication.
