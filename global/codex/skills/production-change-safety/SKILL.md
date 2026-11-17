---
name: production-change-safety
description: Apply risk-based safety checks when planning, implementing, reviewing, or releasing changes that can affect a delivered customer product across on-premises, cloud, SaaS, or hybrid deployments.
---

# Production change safety

Keep supported customer installations, data, and integrations working through an update, restart, and recovery. Apply this from design through rollout to features, dependencies, configuration, infrastructure, installers, and release artifacts that can affect a delivered product.

## Scope and verification

Before implementation or review, identify the affected components, customer environments, supported versions, persistent state, and external contracts. Use the product's support matrix, release process, and applicable requirements. Resolve material unknowns before relying on a compatibility or recovery claim. Record why a potentially relevant check does not apply.

- **Compatibility and upgrades.** Against representative existing installs, configuration and data, verify every affected supported upgrade path, including skipped versions if supported. Cover clean installs, interruption, retry and restart where affected. Check supported OS, runtime, database, dependency and API versions. Test mixed client, server, worker and event versions that can coexist during phased rollouts. Preserve settings, credentials, certificates and permissions. Route contract changes through [API, data and distributed systems](../engineering-guidance/references/api-data-and-distributed.md).
- **State and recovery.** Exercise state-changing migrations and verify data and workflow invariants for affected records, files, sessions, transactions and queues. Test recovery from representative failures, including backup restoration and rollback or roll-forward as applicable. Establish when rollback stops being safe. Verify schema and data compatibility separately from reverting binaries. Use [data protection](../cloud-native-platform-architecture/references/data-protection.md) for the storage in use.
- **Release integrity and operations.** For dependency, build or artifact changes, require evidence for applicable vulnerability scanning, SBOMs, signing, provenance and verification of delivered artifacts. For runtime changes, check affected workflows, integrations, security boundaries, performance and capacity. For infrastructure changes, check drift and affected networking, storage, DNS and IAM through the [Terraform standard](../terraform-cloud-deployment-standard/SKILL.md).
- **Deployment model.** For customer-managed installations, check applicable offline or air-gapped delivery, custom configuration, prerequisites, disk and permission checks, and interrupted installer recovery. For managed rollout, check applicable tenant, region and shared-service isolation. Limit exposure by ring, tenant or region where supported. Use a flag or kill switch when it can safely disable the affected capability. Apply both sets of checks at hybrid boundaries.

## Release evidence

Use the existing release record with the release or artifact ID, affected support matrix and transitions, executed checks and linked results, recovery evidence, remaining risks and the decision for each applicable phase. Record **PASS** only for a phase whose required evidence is present, **BLOCKED** when evidence is missing or failed, and **APPROVED EXCEPTION** only with documented approval from the product's authorized owner, scope, expiry and compensating controls. Track deferred checks explicitly. Reuse existing automated gates within the authorized scope.

Before rollout, specify the health signals, thresholds, observation window, stop or recovery action, and operator. Automate stopping where the platform supports it. Use customer post-upgrade checks or authorized production canary results before broader rollout or final release sign-off, according to the deployment model. Update applicable release notes, upgrade and recovery instructions, support ownership, support windows, and breaking-change or end-of-support notices. Release readiness is separate from source merge unless project policy ties them together. Follow existing authorization for deployment, customer access, communications and exceptions.
