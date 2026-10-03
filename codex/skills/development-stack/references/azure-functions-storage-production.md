# Azure Functions, Blob Storage, and Storage Queues

Apply this reference when a project actually deploys Azure Functions with Azure Blob Storage or Azure Storage Queues. Preserve the repository's language, runtime, binding extensions, and hosting plan; verify their current support before changing a connection or trigger.

## Delivery and execution

- Treat queue and blob-triggered work as replayable. A function can complete a side effect and fail before the host deletes or checkpoints the message, so make writes idempotent using a stable business key plus the source blob identity/version where relevant.
- For Storage Queue triggers, account for the configured visibility timeout, host concurrency, and retry policy. The Functions queue trigger retries a message up to five times by default (including the first attempt), then places it in `<queue>-poison`; configure a deliberate delay, alert on poison growth, and define a safe inspect/replay path. These settings affect a function app's queue-triggered functions, so check blast radius before tuning them.
- Bound work to the plan's configured function timeout and downstream deadlines. Hosting plans differ in execution, scale, networking, startup, and storage behavior; consult the current plan matrix instead of assuming a timeout or scale rule applies everywhere. Split long work into durable, restartable units when it cannot fit the actual execution contract.
- Bound trigger concurrency to the capacity and rate limits of Cosmos DB, Search, and any model/API dependencies. Queue-trigger scaling can multiply concurrent invocations across instances; a per-instance limit is not a global limit.
- Blob uploads, queue publication, and database state changes are separate service operations. Do not assume a transaction spans them: use an existing outbox/reconciliation mechanism or make each partial outcome detectable and recoverable. Queue messages should identify the intended blob/version, and consumers should handle missing, replaced, or already processed blobs.
- Storage Queue does not provide an application-level exactly-once workflow. If ordering matters, encode a sequence/version and enforce it in durable state rather than relying on arrival order.

## Identity and cloud boundaries

- Prefer managed identity for the Functions host, bindings, and SDK clients when the selected extension and hosting plan support it. Grant each identity only the required data-plane roles; distinguish the host's `AzureWebJobsStorage` needs from the function's Blob/Queue data access.
- For identity-based Blob trigger connections, configure the Queue service URI for the same account when required for poison-blob tracking. Check each binding's extension/runtime support and required roles rather than assuming that a working SDK credential also configures the Functions host.
- Resolve service endpoints, Entra authority, and token audience from the chosen Azure cloud and resource configuration. Azure Government and other sovereign clouds use distinct endpoints. In sovereign clouds or custom DNS setups, use explicit service URIs for the Functions storage connection rather than assuming the public-cloud account-name shortcut.
- Before selecting a Functions plan or enabling a service feature, verify its current region, plan, runtime, extension, and cloud support. Emulator success does not establish managed identity, private networking, trigger scaling, or sovereign-cloud behavior.

## Operational evidence

Keep structured logs and metrics sufficient to trace a work item across enqueue, blob access, processing, and durable completion without logging payloads, SAS tokens, or credentials. Monitor failed invocations, queue age/depth, poison messages, function duration/timeouts, and downstream throttling. A retry should be bounded and should not amplify a persistent authorization, validation, or configuration error.

## Official references

- [Azure Queue Storage trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-queue-trigger)
- [Azure Blob Storage trigger for Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob-trigger)
- [Azure Functions hosting and scaling](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale)
- [Configure identity-based connections in Azure Functions](https://learn.microsoft.com/en-us/azure/azure-functions/functions-identity-based-connections-tutorial)
- [Azure Functions connection requirements and plan differences](https://learn.microsoft.com/en-us/azure/azure-functions/manage-connections)
- [Secure Azure Queue Storage](https://learn.microsoft.com/en-us/azure/storage/queues/secure-queues)
- [Azure Storage endpoints in Azure Government](https://learn.microsoft.com/en-us/azure/azure-government/documentation-government-get-started-connect-to-storage)
