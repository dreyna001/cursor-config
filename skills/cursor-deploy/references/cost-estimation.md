# Cost Estimation Patterns

Use current official AWS prices and the AWS Pricing Calculator, or a pricing
integration only if one is actually available in the current session. Do not
assume an `awspricing` MCP server or present unverified prices as current.

## Workflow

1. Identify all AWS services in the architecture
2. Verify each service's current regional rates and billing dimensions
3. Calculate monthly estimates based on expected usage
4. Present total before proceeding

## Service Codes (Reference Only)

Confirm service codes and filter dimensions against current AWS price-list
documentation before using them in a query.

| Service           | Code                | Notes                                            |
| ----------------- | ------------------- | ------------------------------------------------ |
| Fargate           | `AmazonECS`         | Filter by `usagetype` containing "Fargate"       |
| Aurora PostgreSQL | `AmazonRDS`         | Filter: `databaseEngine` = "Aurora PostgreSQL"   |
| Aurora MySQL      | `AmazonRDS`         | Filter: `databaseEngine` = "Aurora MySQL"        |
| RDS PostgreSQL    | `AmazonRDS`         | Filter: `databaseEngine` = "PostgreSQL"          |
| Amazon DocumentDB | `AmazonDocDB`       | MongoDB-compatible managed database              |
| ALB               | `AWSELB`            | Application Load Balancer                        |
| S3                | `AmazonS3`          | Storage and requests                             |
| CloudFront        | `AmazonCloudFront`  | CDN distribution                                 |
| Amplify           | `AWSAmplify`        | Hosting, build minutes                           |
| Lambda            | `AWSLambda`         | Requests and duration                            |
| DynamoDB          | `AmazonDynamoDB`    | On-demand or provisioned                         |
| Secrets Manager   | `AWSSecretsManager` | Per secret per month                             |
| Elastic Beanstalk | N/A (free service)  | No EB charge; query EC2, AWSELB for actual costs |

## Fargate Pricing Dimensions

Fargate commonly charges based on vCPU and memory duration. Verify the current
billing dimensions and regional price list before estimating. Example filter
shapes (not a guaranteed current API contract):

```
usagetype: "USE1-Fargate-vCPU-Hours:perCPU"  # vCPU pricing
usagetype: "USE1-Fargate-GB-Hours"           # Memory pricing
```

These dimensions explain the workload inputs to estimate; do not reuse an old
monthly figure without recalculating it for the target region and usage.

## Aurora Serverless v2 Pricing

Aurora Serverless v2 charges per ACU-hour (Aurora Capacity Unit).

- Minimum: 0.5 ACU
- 1 ACU ≈ 2GB memory

**Dev estimate (0.5-2 ACU range):**

- ~$45-90/month depending on usage patterns

**Production estimate (2-8 ACU range):**

- ~$180-360/month depending on load

## Amazon DocumentDB Serverless Pricing

Amazon DocumentDB Serverless charges per DCU-hour (DocumentDB Capacity Unit),
storage (GB-month), and I/O (standard config only).

- Minimum: 0.5 DCU
- 1 DCU ≈ 2 GiB memory

**Dev estimate (0.5-2 DCU range, 10GB storage):**

- ~$35-120/month depending on usage patterns (scales to 0.5 DCU when idle)

**Production estimate (2-8 DCU range, 100GB storage, multi-AZ):**

- ~$130-400/month depending on load

## Elastic Beanstalk Cost

Elastic Beanstalk itself has no service fee. Cost equals the underlying AWS
resources provisioned for the environment (EC2, ELB, EBS, CloudWatch).
Estimate the actual EC2, load balancer, storage, network, and logging resources
with current regional prices. The ranges below are historical illustrations,
not current quotes:

**Dev web (1x t3.small + ALB):** ~$35-40/month
**Dev worker (1x t3.small, no ALB):** ~$15-20/month
**Production web (4x t3.medium + ALB, Multi-AZ):** ~$150-200/month

Include EBS volume costs (8GB gp3 default: ~$1/month per instance).

## Historical Example Ranges

The following amounts are carried over as rough illustrations only. Recalculate
them using current official pricing and stated workload assumptions before
sharing with a user or using them to choose an architecture.

**Small web app (Fargate + Aurora Serverless v2 + ALB):**

- Dev: ~$70-100/month
- Production: ~$200-400/month

**Small web app (Fargate + Amazon DocumentDB Serverless + ALB):**

- Dev: ~$70-155/month
- Production: ~$200-450/month

**Static site / SPA (Amplify Hosting):**

- Low traffic: ~$0-5/month (free tier covers most small sites)
- High traffic: ~$15-40/month

**Static site (S3 + CloudFront):**

- Low traffic: ~$1-5/month
- High traffic: ~$20-50/month

**Serverless API (Lambda + API Gateway + DynamoDB):**

- Low traffic: ~$5-20/month
- High traffic: scales with requests

**Web app on Elastic Beanstalk:**

- Dev (1x t3.small + ALB): ~$35-40/month
- Production (load-balanced, Multi-AZ): ~$80-200/month

**Web app on EB + Aurora Serverless v2:**

- Dev: ~$80-130/month
- Production: ~$200-400/month

## Presenting Estimates

Always show:

1. Per-service breakdown
2. Monthly total
3. Key assumptions (e.g., "assumes 24/7 uptime", "assumes 1M requests/month")
4. Cost optimization tips if relevant
