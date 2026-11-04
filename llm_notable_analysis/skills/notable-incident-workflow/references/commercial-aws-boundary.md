# Commercial AWS product boundary

These instructions apply to all work under `s3_notable_pipeline_commercial/`.

## Scope and safety

- This directory is an independent commercial AWS product for partition `aws` in `us-east-1`.
- Treat `../s3_notable_pipeline/` as an out-of-scope production GovCloud product.
- Never edit, import from, symlink to, deploy, migrate, delete, or clean up resources for `../s3_notable_pipeline/`.
- Do not introduce dual-partition behavior. Deployment code in this project must fail closed outside `aws` and `us-east-1`.
- Do not copy data, secrets, identifiers, endpoints, or runtime state from a GovCloud environment.
- Never run `sam delete`, `aws cloudformation delete-stack`, recursive S3 deletion, or an equivalent destructive AWS command for this work.
- Before any live AWS mutation, verify and report the AWS account ID, partition, region, role/profile, stack name, and intended resources. Obtain explicit user approval for the live deployment step.

## Implementation defaults

- Terraform is the only supported path for new or changed cloud infrastructure.
  Do not extend the legacy SAM/CloudFormation templates. New capabilities must
  compose through `deploy/terraform/customer_default` and its leaf modules.

- Keep planning and task lists local and untracked. Preserve deployment approval and acceptance gates in the maintained operating guides.
- Preserve the copied architecture, behavior, external contracts, and capability-profile system unless a verified commercial-AWS difference requires a change.
- Keep the internal Python package name `s3_notable_pipeline` unless the user explicitly approves a rename.
- Keep changes small and independently testable. Document every intentional difference from the fork baseline.
- Keep customer values such as account IDs, resource names, KMS keys, model IDs, identity settings, endpoints, retention, and capacity in validated deployment configuration.
- Treat dependency remediation as a separate pre-production hardening gate, not as an undocumented part of the AWS partition work.

## Subagents

Follow the user/session-selected model and reasoning settings and the central Codex model and subagent routing guidance. This product defines no separate model or delegation override.
- Keep write-heavy implementation owned by the primary agent unless tasks touch disjoint files and coordination risk is low.
- Subagents must follow the same commercial-only and GovCloud no-touch boundary.
