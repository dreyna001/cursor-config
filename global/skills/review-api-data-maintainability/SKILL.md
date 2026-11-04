---
name: review-api-data-maintainability
description: "Legacy manual alias for combined API, data, and maintainability reviews; routes explicitly invoked requests to the split review skills."
disable-model-invocation: true
---
# Review API, Data, Maintainability, And Architecture

This compatibility entrypoint is manual-only.

- Use [Review API, Data, And Distributed Systems](../review-api-data-distributed/SKILL.md) for contracts, schemas, storage, queues, retries, replay, and distributed-data risks.
- Use [Review Maintainability And Architecture](../review-maintainability-architecture/SKILL.md) for boundaries, stale code, observability, config hygiene, and documentation gaps.

Do not keep a combined automatic review checklist in this alias.
