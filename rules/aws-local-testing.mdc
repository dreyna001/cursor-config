---
description: Local AWS development and test safety with mocked clients or LocalStack
alwaysApply: false
---

# AWS Local Testing

Apply this when creating, modifying, or testing code that uses AWS services, AWS SDK clients, Lambda handlers, infrastructure templates, local development setup, or CI workflows.

- Local development and automated tests must not call real AWS by default.
- Use mocked AWS clients for unit tests, LocalStack for local integration tests, and real AWS only for explicit dev, staging, or production validation.
- Centralize AWS client creation; do not scatter `boto3.client(...)` or AWS SDK client construction through business logic.
- Do not hardcode AWS endpoints, credentials, regions, buckets, queues, topics, or tables.
- Support `AWS_ENDPOINT_URL` for local emulation. When set, default local credentials to `test/test` and local region to `us-east-1`.
- Tests must be safe to run without real AWS credentials.
- Add only the local-support files the repo actually needs, such as `docker-compose.yml`, `.env.local`, `scripts/localstack_bootstrap.sh`, or `tests/integration/`.
- LocalStack bootstrap scripts must be idempotent and create their own local resources.
- Unit tests should mock AWS clients and avoid network calls. Integration tests should create and seed their own LocalStack resources and clean up when practical.
- LocalStack validates local SDK integration and data flow, not IAM correctness, VPC networking, KMS, quotas, CloudWatch behavior, API Gateway edges, cross-account permissions, or deployment correctness.
- Before production, require explicit validation in a real AWS dev or staging account.

Anti-patterns:
- requiring developer AWS credentials for unit tests
- using production AWS accounts for local testing
- hardcoding production resource names
- treating LocalStack as a full replacement for AWS dev or staging validation
