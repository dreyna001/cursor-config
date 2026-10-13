# Service Defaults

These are starting-point examples, not universal defaults. Inspect the project and
user constraints, then verify current service support, lifecycle, regional
availability, and feature behavior in official AWS documentation before making a
recommendation. Follow an explicit user request unless it conflicts with a real
technical or safety constraint.

## Compute

| App Pattern                                           | Default              | Override Trigger                                                                                      |
| ----------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| Web framework (Django, Rails, Express, FastAPI, etc.) | Fargate + ALB        | "serverless" → Lambda + API Gateway; "managed platform" or "Elastic Beanstalk" → Elastic Beanstalk    |
| Static site / SPA                                     | Amplify Hosting      | "S3" or "more control" → S3 + CloudFront                                                              |
| Background workers                                    | Fargate              | Short tasks (<15min) → Lambda; "managed platform" or "Elastic Beanstalk" → Elastic Beanstalk (Worker) |
| Scheduled jobs                                        | EventBridge + Lambda | Long-running → EventBridge + Fargate                                                                  |
| API-only (no web UI)                                  | Fargate + ALB        | "serverless" → API Gateway + Lambda; "managed platform" or "Elastic Beanstalk" → Elastic Beanstalk    |
| Existing Heroku/Render/Railway app migrating to AWS   | Elastic Beanstalk    | "container orchestration" or "ECS" → Fargate + ALB; "serverless" → Lambda                             |

Service lifecycle and newer deployment options change over time. Verify their
current AWS support status before choosing between them; this reference does not
make a lifecycle claim.

### Why Fargate over Lambda for web frameworks

Most web frameworks (Django, Rails, Flask with WSGI) expect long-running processes.
Lambda's cold starts and request/response model require adapters and introduce latency.
Fargate provides a more natural fit without framework modifications.

### Why Amplify for static sites/SPAs

Amplify Hosting handles CI/CD, HTTPS, custom domains, and CDN automatically.
Less configuration than S3 + CloudFront. Git-based deployments work out of the box.
Use S3 + CloudFront when user needs fine-grained control over caching, edge functions,
or has existing CloudFront infrastructure.

For framework-specific guidance, consult the current official AWS Amplify
documentation and the project's existing framework configuration.

### Why Elastic Beanstalk for managed platform deployments

Elastic Beanstalk is an application management service: the user provides code,
AWS manages deployments, scaling, patching, monitoring, and health response.
Choose when the user wants production-grade reliability with the lowest ongoing
maintenance cost. Choose Fargate when the user wants direct container control.

## Database

| Data Pattern       | Default (Dev)                | Default (Prod)               | Override Trigger                              |
| ------------------ | ---------------------------- | ---------------------------- | --------------------------------------------- |
| PostgreSQL         | Aurora Serverless v2         | Aurora Serverless v2         | "simple RDS" → RDS                            |
| MySQL              | Aurora Serverless v2         | Aurora Serverless v2         | "simple RDS" → RDS                            |
| Document / MongoDB | Amazon DocumentDB Serverless | Amazon DocumentDB Serverless | "provisioned" → Amazon DocumentDB provisioned |
| NoSQL / Key-Value  | DynamoDB                     | DynamoDB                     | -                                             |
| Redis / Caching    | ElastiCache Serverless       | ElastiCache Serverless       | -                                             |
| Full-text search   | OpenSearch Serverless        | OpenSearch Serverless        | -                                             |

### Why Aurora Serverless v2

Scales to near-zero in dev (0.5 ACU minimum), scales up automatically for production.
Single choice works for both environments. Only use provisioned RDS if user has
specific cost constraints or compliance requirements.

### Why Amazon DocumentDB Serverless for MongoDB

Amazon DocumentDB Serverless is the on-demand, auto-scaling configuration of Amazon DocumentDB.
It dynamically adjusts capacity based on application demand so you only pay for what you
use. Ideal for dev/test, variable workloads, and new applications where capacity needs
are unknown. Compatible with MongoDB 3.6, 4.0, 5.0 and 8.0 APIs.
Use provisioned Amazon DocumentDB only when you have predictable, steady-state workloads
or specific compliance requirements that need fixed instance sizing.

## Storage

| Pattern       | Default         |
| ------------- | --------------- |
| Static assets | S3              |
| User uploads  | S3              |
| Secrets       | Secrets Manager |
| Config        | Parameter Store |

## IaC

Use Terraform for every new or changed cloud resource. Use the project's
documented Terraform root. Do not add CDK, CloudFormation, SAM, or another IaC
format. Existing non-Terraform templates are legacy and are not a reason to
extend them. Application builds and artifact publication may keep their
existing tools.

## Sizing (Dev vs Production)

| Component                  | Dev               | Production                     |
| -------------------------- | ----------------- | ------------------------------ |
| Fargate                    | 0.5 vCPU, 1GB     | 1+ vCPU, 2+ GB                 |
| Aurora Serverless          | 0.5-2 ACU         | 2-16+ ACU                      |
| ALB                        | Single AZ OK      | Multi-AZ                       |
| Elastic Beanstalk (web)    | 1x t3.small + ALB | 2-4x t3.medium + ALB, Multi-AZ |
| Elastic Beanstalk (worker) | 1x t3.small       | 2-4x t3.medium                 |

Default to **dev sizing** unless user says "production", "prod", or "production-ready".

## Security

See [security.md](security.md) for encryption, VPC placement, IAM, security group defaults, and pre-deployment security checks.
