---
name: cloud-native-platform-architecture
description: "Design or review production cloud architecture across AWS, Azure, GCP, government, and hybrid deployments; use for service selection, parity, portability, security, or reliability."
---
# Cloud-Native Platform Architecture

Preserve product behavior and control outcomes across platforms while allowing each application and cloud to use the architecture that best fits its requirements.

## Load Provider Guidance

- Read [references/aws.md](references/aws.md) for AWS, AWS GovCloud, or AWS-to-other-platform work.
- Read [references/azure.md](references/azure.md) for Azure, Azure Government, or Azure-to-other-platform work.
- Read [references/gcp.md](references/gcp.md) for Google Cloud or GCP-to-other-platform work.
- Read multiple provider references only for parity reviews, migrations, or multi-cloud decisions.

Treat provider references as decision prompts, not prescribed service mappings. Verify current service, region, partition, identity, networking, and feature availability from authoritative sources before making deployment decisions.

## Conditional data protection

When the project uses persistent data, read [conditional backup and recovery decisions](references/data-protection.md) for only the technologies in use. Reuse verified native coverage before proposing additions.

## Architecture Workflow

1. Identify the application, users, workload shape, data sensitivity, deployment boundary, and operational owner.
2. Define the product invariants that must remain true: business behavior, API and data contracts, evidence discipline, security outcomes, tenant isolation, reliability objectives, and operator-visible behavior.
3. Separate application requirements from inherited implementation choices. Do not treat an existing AWS, Azure, or on-prem service choice as a requirement.
4. Classify each decision as one of:
   - product invariant
   - application-specific architecture
   - provider-native implementation
   - customer operational configuration
   - explicitly deferred gap
5. Select the smallest production-ready architecture that satisfies the requirements. Prefer managed, identity-native, observable services where they materially reduce operational burden.
6. Compare alternatives by fit, availability, failure modes, security boundary, scalability, cost shape, operational complexity, and reversibility.
7. Test for forced parity and duct tape before accepting the design.
8. Synchronize code, infrastructure, configuration examples, tests, deployment scripts, diagrams, and operator documentation.
9. Record live-cloud validation that cannot be proven locally.

## Parity Model

Require semantic parity where reasonable:

- equivalent business outcomes
- compatible external contracts
- equivalent security and isolation guarantees
- comparable reliability and audit behavior
- consistent evidence, RAG, and approval semantics
- comparable operator and customer responsibilities

Do not require implementation parity:

- identical service count
- one-to-one managed-service mappings
- identical event topology
- identical identity primitives
- identical storage or search engines
- wrappers that emulate another provider's control plane

When behavior differs, state whether the difference is required by platform constraints, intentionally application-specific, customer-configurable, or an unjustified drift.

## Duct-Tape Test

Flag an implementation when it does one or more of the following without a demonstrated requirement:

- makes a managed service behave like a different provider's service
- introduces a proxy, queue, database, index, or worker only to copy another deployment
- duplicates an authoritative source of truth
- uses static credentials where workload identity is supported
- hides unsupported government-cloud behavior behind compatibility code
- moves workflow or policy logic into transport adapters
- adds broad abstractions before a second real implementation needs them
- keeps an unsuitable service because changing it would reduce superficial parity

Accept an adapter when it protects a stable application boundary, normalizes a real external contract, or isolates provider SDK behavior. Keep it thin and free of workflow policy.

## Minimum Production Review

Evaluate only material, code-supported concerns across:

- correctness and business behavior
- authentication, authorization, tenant isolation, secrets, and least privilege
- data ownership, schemas, concurrency, idempotency, and replay
- retries, backoff, dead-letter handling, partial failure, and recovery
- API and event-contract compatibility
- performance, quotas, scaling, and cost-amplification paths
- observability, deployment safety, configuration validation, and tests
- government-cloud endpoints, regions, identity audiences, DNS, and service availability

Do not recommend a kitchen-sink architecture. Add a component only when a current requirement or credible production failure mode justifies it.

## Customer Configuration Boundary

For Terraform deployment design, apply the [Terraform cloud deployment standard](../terraform-cloud-deployment-standard/SKILL.md). Make create-or-reference-existing choices explicit independently per required deployable dependency, support mixed existing/new infrastructure, and preserve the established stack, ownership, and documented government-cloud exceptions.

Make customer-specific values explicit and documented when they legitimately vary, including retention, resource names, regions, tenant identifiers, endpoints, model deployments, capacity, integration destinations, data mappings, approval policy, and feature enablement.

Do not use customer configuration to conceal unsupported architecture. Define defaults where safe, validate required values at deployment or startup, fail closed for risky capabilities, and keep customer names out of product logic.

Use `$capability-profile-architecture` alongside this skill when optional read-only, writeback, or action-taking capabilities vary by customer.

## LLM And RAG Boundary

For cybersecurity or evidence-sensitive workflows, use `$cybersecurity-workflow-design` alongside this skill.

- Keep direct case evidence separate from retrieved advisory context and model inference.
- Use RAG for environment grounding unless retrieved content is itself the current case record.
- Select vector, lexical, hybrid, or database retrieval from corpus size, query behavior, update rate, filtering, provenance, service availability, and operational burden.
- Do not add a vector database merely because content is called a knowledge base; do add one when semantic retrieval is a demonstrated requirement.

## Required Decision Output

For designs and reviews, produce:

1. application requirements and constraints
2. product invariants
3. selected architecture and why it fits this application
4. provider-native decisions and rejected alternatives
5. justified cross-platform differences
6. suspected duct tape or unjustified drift
7. customer-set values and validation requirements
8. deferred gaps and live-cloud validation
9. smallest safe implementation plan and regression tests

State assumptions and unresolved decisions explicitly. Escalate only choices that materially alter product behavior, security posture, cost model, customer responsibility, or reversibility.
