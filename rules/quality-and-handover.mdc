---
description: Quality, validation, and engineer handover for each delivery block
alwaysApply: true
---

# Rule: Quality, Validation, and Handover

Every block should end in something that can be run, reviewed, and explained by another engineer.

Requirements:
- Include representative fixtures or sample inputs.
- Validate the main happy path end to end.
- Test the highest-risk edge cases for the current block.
- Keep configuration explicit and minimal.
- Document how to run the block locally.
- Document key assumptions and known limitations.
- Make logs and errors understandable.

For code changes:
- Prefer small, reviewable increments.
- Avoid silent failure.
- Fail early on malformed required inputs.
- Keep outputs stable and demo-ready.

For reviews:
- Check whether the implementation matches the stated scope.
- Check whether any speculative abstraction was added.
- Check whether the LLM step is bounded and validated.
- Check whether the code can be explained simply.

Avoid:
- demos that only work on one golden input with no guardrails
- hidden configuration
- undocumented assumptions
- handoff that depends on tribal knowledge
