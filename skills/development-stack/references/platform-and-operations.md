# Platform And Operations Practices

Apply only the sections for technologies the project actually uses. Verify installed versions, provider support, and deployment constraints from authoritative sources before implementation.

## OPA

- Use OPA when policy must be shared, independently audited, or changed separately from application code; keep simple local authorization checks local.
- Define explicit policy inputs and default-deny decisions. Keep data fetching and side effects outside policy evaluation.
- Version policy bundles with the application contract and test allow, deny, missing-input, and malformed-input cases.
- Log the decision, policy version, and non-secret reason needed for audit without exposing sensitive input.

## OpenTelemetry

- Instrument service boundaries and material workflows, not every function.
- Use stable semantic attributes and propagate trace context across HTTP, queues, and workers.
- Keep secrets, document contents, prompts, tokens, and unbounded user values out of attributes and metric labels.
- Bound cardinality and sampling deliberately; make export failure non-fatal unless telemetry is itself a compliance requirement.

## gVisor And Containers

- Use gVisor for untrusted or agent-generated workloads only when the target platform supports it and compatibility has been tested.
- Keep OCI images minimal, non-root, reproducible, and pinned by immutable release identity. Separate build-time credentials from runtime images. Released applications need reproducible direct and transitive dependency resolution consumed by the build, such as a lockfile or equivalent pinned build inputs; do not impose application lock semantics on published library dependency ranges.
- Define CPU, memory, process, filesystem, network, and execution-time limits for untrusted work.

## systemd, vLLM, And LiteLLM

- Use systemd only for customer-controlled hosts. Run under a dedicated identity with explicit environment, restart, resource, and log behavior.
- Use vLLM only for self-hosted inference; pin the model and runtime, bound concurrency and context, and verify readiness and failure behavior.
- Add LiteLLM only when an on-prem deployment currently needs a multi-model or multi-provider routing boundary. Do not add it around one model endpoint.
- Keep model allowlists, credentials, quotas, timeouts, and audit fields explicit at any routing boundary.

## Terraform And Managed Cloud

- Use provider-native managed services and Terraform for cloud deployments; do not recreate on-prem operations on virtual machines.
- Pin provider versions, keep state remote and protected, and separate customer-supplied values from product architecture.
- Plan and validate changes before apply. Treat identity, networking, encryption, retention, quotas, and regional feature availability as deploy-time contracts.
- Keep AWS, Azure, and GCP implementations provider-native while preserving shared application behavior and security outcomes.
