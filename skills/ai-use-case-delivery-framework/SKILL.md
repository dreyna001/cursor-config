---
name: ai-use-case-delivery-framework
description: Guides stakeholder-to-MVP delivery of AI and LLM use cases across AWS, on-prem, or hybrid environments. Use when discovering a new AI use case, assessing readiness, defining governance gates, planning a pilot, or deciding whether to iterate, scale, or stop.
---

# AI Use Case Delivery Framework

Use this skill when shaping an AI or LLM use case from stakeholder discussion through MVP, pilot, and scale decision.

## Workflow

1. Discover the operator pain, workflow steps, desired outcome, and definition of done.
2. Confirm deployment path: AWS, on-prem, hybrid, or minimum remediation first.
3. Pick one high-value, feasible use case.
4. Map workflow, data sources, systems of record, and current process.
5. Check data sufficiency and classify hard vs soft gaps.
6. Lock the destination contract: output shape, idempotency, retention, retries, and writeback path.
7. Define assurance controls: security, guardrails, deterministic vs assistive boundary, observability, and approval gates.
8. Build the smallest operational MVP.
9. Pilot and measure quality, speed, correction rate, invalid output rate, adoption, and cost.
10. Decide: iterate, scale, or stop.

## Gates

- Gate A: pain is real and definition of done is clear.
- Gate B: MVP can be built quickly with contracts, evaluation data, operational edges, and acceptable risk.
- Gate C: pilot meets agreed KPI thresholds.
- Gate D: scale, iterate, or stop.

## Output

Return:
- use case summary
- deployment path
- data readiness
- delivery contract
- governance and assurance controls
- MVP scope
- pilot metrics
- scale, iterate, or stop recommendation

## Preferred Outcome

Operational MVPs with measurable value, not open-ended proofs of concept.