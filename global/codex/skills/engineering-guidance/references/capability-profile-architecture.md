# Capability Profile Architecture

- Treat product features as **named capabilities** with explicit flags, not hidden behavior differences.
- Risky capabilities must be **off by default** and enabled intentionally.
- Apply the risk classes and execution boundaries defined in `cybersecurity-approval-policy-gates` when capabilities can affect external systems.
- Validate **flag dependencies and invalid combinations** at startup; fail fast on unsupported config.
- Treat per-customer config as a **supported capability profile**, not a one-off deployment hack.
- Prefer a small set of documented profiles or bundles over arbitrary config sprawl.
- Follow `deployment-runtime-contract` when capability configuration changes.
- New capabilities should define: purpose, default state, dependencies, approval boundary, and rollback path.
- Use capability flags for coarse enablement; use policy rules and approvals for risk control inside the capability.
- Name flags and profiles clearly enough that operators can understand what is enabled without reading code.
