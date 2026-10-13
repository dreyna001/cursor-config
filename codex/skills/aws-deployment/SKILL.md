---
name: aws-deployment
description: "Plan or implement AWS application deployment infrastructure; use for hosting requests that need service selection, cost, security, and operations guidance."
---
# AWS Deployment

Use this skill when the user asks to design or implement an AWS deployment. Preserve an existing repository's framework, infrastructure owner, and deployment conventions. Do not turn an architecture request into a live deployment.

## Workflow

1. Inspect the application, manifests, existing IaC, runtime, data stores, and operational requirements. If the target is AWS GovCloud and the FedRAMP level is not already stated, ask whether it is Low, Moderate, or High before recommending or generating that infrastructure. Apply the authorization-ready rule for the answer. Do not choose the level.
2. Recommend a small service set with the reasons, tradeoffs, and any assumptions. Treat the service matrix in [defaults](references/defaults.md) as a starting point, not current provider truth.
3. Verify service availability, lifecycle, feature support, and version-sensitive configuration in current official AWS documentation for the target region/partition.
4. Estimate costs with current prices and explicit usage assumptions before generating infrastructure. Use the AWS Pricing Calculator or a pricing integration only if it is actually available. If current prices cannot be verified, say so and provide an assumption-based estimate rather than inventing precision.
5. Generate Terraform for new or changed cloud resources, using the project's documented root. Apply the [Terraform cloud deployment standard](../terraform-cloud-deployment-standard/SKILL.md), including explicit create-or-reference choices for required deployable prerequisites. Do not add another IaC format. Apply the security principles in [security defaults](references/security.md) and follow the source links in the relevant reference.
6. Run the repository's tests, formatters, and available IaC/security checks. Distinguish unrun checks and provider behavior.
7. Prepare a plan for review. Applying infrastructure, changing accounts, or making external deployment changes requires the user's explicit authorization immediately before that action.

## Decision Principles

- Keep user constraints and existing architecture ahead of these defaults. When a service choice materially affects cost, availability, data residency, or operations and the preference is not stated, explain the options and ask only for the decision needed.
- Use dev-sized, low-cost configurations for development when appropriate; do not apply them to production without checking reliability requirements.
- Show cost assumptions and excluded costs; include traffic, compute, storage, network transfer, logs, backups, and managed services where applicable.
- Keep secrets out of source and images. Use least-privilege identities, encryption, private networking where supported, and explicit rollback or recovery guidance.
- Do not assume any AWS-specific MCP server, pricing connector, shell command, or SDK is present. Check available tools, repository dependencies, and local documentation before using them.

## References

- [Service selection starting points](references/defaults.md)
- [Cost estimation](references/cost-estimation.md)
- [Security defaults](references/security.md)
- [Elastic Beanstalk details](../aws-elastic-beanstalk/SKILL.md)
