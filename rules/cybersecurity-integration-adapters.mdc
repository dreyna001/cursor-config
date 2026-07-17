---
description: General integration-adapter architecture for cybersecurity workflows and external systems
alwaysApply: false
---

# Cybersecurity Integration Adapters

- Keep integrations with external systems behind **thin adapter boundaries**.
- Treat adapters as transport and normalization layers, not places for workflow or policy logic.
- Isolate **auth, config, retries, rate limits, and error translation** inside the adapter.
- Normalize external request and response shapes into stable internal objects before business logic uses them.
- Prefer **one adapter per system or API surface** rather than scattering calls throughout the codebase.
- Keep environment-specific details such as URLs, tenants, field mappings, and credentials out of workflow code.
- Make adapters explicit for systems such as SIEM, SOAR, ticketing, GRC, CMDB, vuln scanners, asset platforms, threat-intel feeds, cloud APIs, and identity platforms.
- Separate **read**, **writeback**, and **action-taking** operations even when they hit the same vendor system.
- Expose clear typed failures so orchestration can distinguish retryable, validation, auth, and policy errors.
- Add adapter tests with fake responses or fixtures; do not rely on live vendor systems for basic contract coverage.
