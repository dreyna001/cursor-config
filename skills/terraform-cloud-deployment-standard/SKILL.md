---
name: terraform-cloud-deployment-standard
description: Design, implement, or review customer-deployable cloud infrastructure with Terraform. Use when a capability adds or changes AWS, Azure, GCP, government-cloud, or hybrid infrastructure; when creating a deployment path; or when checking whether infrastructure is safe, repeatable, and easy for customers to operate.
---

# Terraform Cloud Deployment Standard

Apply this standard to every capability that creates or changes cloud resources. Preserve an established repository's Terraform conventions unless they conflict with a safety requirement below.

## Required design

1. Use Terraform as the only cloud infrastructure owner for the deployment path. Do not split ownership with SAM, CloudFormation, console steps, or application scripts.
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

## Required verification

For every changed Terraform root:

1. Run `terraform fmt -check -recursive`.
2. Run `terraform init -backend=false` unless the test specifically covers the real backend.
3. Run `terraform validate`.
4. Run repository Terraform contract or plan tests.
5. Run the repository-pinned Terraform security scanner.
6. Confirm scanner exceptions are narrow, truthful, inline, and reviewed. Do not use broad global skips to make CI pass.
7. Verify the documented plan and saved-plan apply commands match the implementation.
8. Treat live cloud deployment as a separate acceptance step when credentials or customer infrastructure are required; report when it was not run.

## CI contract

Require pull-request CI for formatting, initialization without the backend, validation, tests, and security scanning. Pin tool versions or use repository lock files. Grant the workflow read-only permissions unless a tested step requires more.

## Handoff

State what changed, the exact checks run, any accepted scanner exceptions, and whether live cloud validation remains outstanding.
