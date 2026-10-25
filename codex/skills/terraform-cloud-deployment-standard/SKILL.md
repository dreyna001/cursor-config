---
name: terraform-cloud-deployment-standard
description: "Design or review customer cloud infrastructure in Terraform, including secure defaults, repeatable operations, and verification."
---
# Terraform Cloud Deployment Standard

Apply this standard to every capability that creates or changes cloud resources. Preserve an established repository's Terraform conventions unless they conflict with a safety requirement below.

Before creating or changing an AWS GovCloud instance, ask whether the FedRAMP authorization is Low, Moderate, or High when that level is not already stated. Do not choose a level. Apply the authorization-ready rule for the stated level.

For production HTTP ingress design, changes, or review, read [authorization-ready applications](../engineering-guidance/references/authorization-ready-apps.md) and [API abuse and exposure](../engineering-guidance/references/api-abuse-and-exposure.md). Verify per-client/per-route quotas at the edge and application; a shared stage throttle is not equivalent. Preserve local developer/test configurations and existing customer-owned resources; the checklist does not authorize deployment or infrastructure migration.

## Conditional data protection

When the project uses persistent data, apply [conditional backup and recovery decisions](../cloud-native-platform-architecture/references/data-protection.md) through its existing deployment roots. This reference governs native coverage, justified additions and evidence; it does not authorize deployment or retention changes.

## Required design

When production ingress serves browser content or authenticated data, also apply [application security](../engineering-guidance/references/security.md) for response-header, cache, and file-serving policies at the owning edge. Treat missing live configuration as unknown; do not infer a deployed vulnerability from an absent template.

1. Use Terraform exclusively for every new or changed cloud resource across all projects and providers. Do not create or extend SAM, CloudFormation, Bicep, ARM, Pulumi, CDK, console provisioning, or infrastructure-creating scripts. Existing alternate IaC is legacy; do not migrate its deployed resources without an explicitly scoped migration. Application builds, artifact publication, and read-only verification are outside this provisioning restriction.
2. Give each customer deployment path one documented root module and one clear entry point.
3. Put reusable resources in focused leaf modules. Keep customer choices and composition in the root.
4. Use encrypted remote state with locking, versioning, restricted access, and a documented bootstrap process. Never store secrets in committed state configuration.
5. Make planning the default action. A normal deploy command must not apply changes automatically.
6. Apply only an explicit saved plan after review. Make the account, region, workspace, and state target visible before apply.
7. Assign every resource to one Terraform owner. Import or reference existing resources explicitly; never silently replace customer-owned policies or resources.
8. Deploy immutable application artifacts, such as digest-pinned container images.
9. Use least-privilege identities, encrypted storage and transport, private networking where supported, and fail-closed security defaults. Document narrow scanner exceptions beside the resource with the check ID and reason.
10. Automate required bootstrap dependencies, such as image repositories and remote-state storage, without creating a second infrastructure path.
11. Validate customer inputs before planning and expose useful non-secret outputs needed for operation and troubleshooting.
12. Keep code, examples, deployment instructions, rollback steps, and tests synchronized.

## Create-or-reference deployment contract

For every required, deployable cloud prerequisite, provide an explicit choice to
create a product-owned resource or reference a compatible existing resource.
Apply this to the dependencies actually needed by the selected application and
capabilities: for example networking, state storage, registries, encryption keys,
databases, model services/deployments, search services/indexes, and source storage.
Allow `disabled` only for optional capabilities. Do not add services or change
the established application/authentication stack merely to implement this rule.

- Keep the project's canonical flags/schema when they already express these
  choices. One documented customer configuration must identify ownership and
  supply either creation settings or existing identifiers, without requiring
  operators to edit module source. Reject conflicting create/existing inputs,
  missing required values, incompatible references, and disabled required
  dependencies. Do not guess ownership from a resource's presence or name.
- In existing mode, reference and validate the resource; do not replace it,
  transfer ownership, rewrite shared policies, or mutate its network/schema
  implicitly. Any permission wiring or mutation must be explicitly scoped.
  Existing application resources can be adopted only through a reviewed import
  or migration, with one owner per resource. This contract does not require a
  reuse flag for every internal resource Terraform already owns.
- Compose the choices through the documented application root and established
  bootstrap/data-plane roots. Order foundation, private connectivity/DNS, state,
  registries, application deployment, and schema configuration so initial setup
  has no circular prerequisite. Feed nonsecret outputs into later stages instead
  of repeatedly asking for IDs of resources just created. Keep state keys/owners
  separate, planning the default, and applies tied to reviewed saved plans.
- Qualify control-plane and data-plane support for the pinned provider, target
  cloud/partition/region, endpoint, identity audience, permissions, and API
  version. A management-plane resource does not prove index/schema support.
  Introduce an additional Terraform provider only for a required unsupported API,
  explain the need, and verify compatibility; preserve established version pins
  unless a scoped change is necessary. If creation is unavailable or ownership
  is externally governed, document that exception and its existing-resource
  contract rather than claiming complete create support or bypassing Terraform.
- Separate Terraform provisioning from release builds, artifact publication,
  corpus loading, external credential issuance, provider approvals/quotas, and
  customer-side network/identity changes. Document remaining prerequisites and
  automate permitted delivery steps with existing tools; wrappers must not
  provision infrastructure outside Terraform or embed provisioning in
  `local-exec`/`remote-exec`. Keep secret bytes out of committed inputs/outputs;
  preserve the established protected secret and state handling.
- Verify create mode's intended resources and wiring, existing mode's compatible
  references and preserved ownership, invalid/missing/conflicting inputs, optional
  disabled mode, and the staged bootstrap path. Use meaningful Terraform contract
  or plan checks; local validation alone does not establish live acceptance.

## Required verification

For every changed Terraform root:

1. Run `terraform fmt -check -recursive`.
2. Run `terraform init -backend=false` unless the test specifically covers the real backend.
3. Run `terraform validate`.
4. Run repository Terraform contract or plan tests.
5. Run the repository-pinned Terraform security scanner. Follow [container and cloud security scans](../engineering-guidance/references/security.md#container-and-cloud-security-scans) for scanner selection, artifact qualification and truthful triage.
6. Confirm scanner exceptions are narrow, truthful, inline, and reviewed. Do not use broad global skips to make CI pass.
7. Verify the documented plan and saved-plan apply commands match the implementation.
8. Treat live cloud deployment as a separate acceptance step when credentials or customer infrastructure are required; report when it was not run.

## CI contract

Require pull-request CI for formatting, initialization without the backend, validation, tests, and security scanning. Pin tool versions or use repository lock files. Grant the workflow read-only permissions unless a tested step requires more.

## Handoff

State what changed, the exact checks run, any accepted scanner exceptions, and whether live cloud validation remains outstanding.
