# Conditional backup and recovery decisions

Apply only to technologies the project actually uses and data it owns. This is a
decision reference, not permission to deploy, change retention, or add services.
Honor project-specific limits, including documentation-only scope. Read only the
applicable technology sections.

## Decide from requirements and verified coverage

1. Record authoritative data scope (tables, buckets/prefixes, accounts/containers,
   databases, attachments and associated persistent files), exclusions and why
   excluded data is reproducible or covered elsewhere. Name the data owner,
   backup operator, restore approver and monitoring responder.
2. Document recovery point objective (RPO), recovery time objective (RTO), required
   recovery window, retention and deletion obligations. Identify relevant failure
   scenarios: accidental changes, resource/account deletion, compromised identity,
   or regional loss. Unknown objectives remain unresolved; do not invent values.
3. Inspect existing native settings, central/customer backup policies, selected
   resources, destinations, permissions, encryption, recovery points and restore
   records. Record evidence source and time. Unknown coverage is **unverified**,
   not absent. Reuse verified protection and close only demonstrated gaps.
4. Separate the required recovery outcome from its implementation. Compare native
   protection and existing policies first. Select the smallest, lowest-cost
   supported combination satisfying the documented requirements; avoid overlapping
   coverage. Check supported technology/API, cloud/partition, region, SKU and engine
   version, and the project's pinned Terraform CLI/provider versions and schemas.
   Public-cloud support does not establish government-cloud support.
5. Label each proposed addition **REQUIRED**, **RECOMMENDED**, or **OPTIONAL** with
   its requirement, uncovered failure scenario, coverage evidence and cost reason.
   REQUIRED means necessary for an applicable documented obligation, not merely a
   preferred service or template default. RECOMMENDED addresses a justified risk;
   OPTIONAL is an enhancement. Neither label authorizes implementation. Schedules,
   retention periods, new vaults and additional regions are proposals unless a
   requirement and supported design justify them. Do not alter existing retention
   or protection without authorization.

## DynamoDB, if used

- Inspect each table's native point-in-time recovery (PITR), restorable timestamps
  and configured recovery period, plus existing AWS Backup/organization policies,
  assignments and recovery points. Reuse coverage that meets the objectives.
- Native PITR is continuous protection; it does not need a separate scheduled
  export simply to create recoverable points within its supported window. Add
  scheduled or separately protected recovery points only for uncovered retention,
  isolation, deletion or regional-recovery requirements. An S3 export is a separate
  workflow with its own restore contract, not automatically a substitute backup.
- Verify restoration to a new table and the application's cutover dependencies,
  including indexes, streams, global-table membership and access configuration.
  A shorter PITR window does not necessarily lower its size-based charge.
- For an authorized drill, verify usable recovery points: inspect backup completion
  or the PITR restorable interval, selected timestamp, permissions and key access.
  Prove usability by restoring into separate test tables, waiting for readiness,
  and checking required indexes, representative records and application queries.
  A backup listing or an ACTIVE table alone does not establish application recovery;
  record untested scope and keep production table bindings unchanged.

Sources: [DynamoDB PITR](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html),
[AWS Backup for DynamoDB](https://docs.aws.amazon.com/aws-backup/latest/devguide/advanced-ddb-backup.html),
[restoring test tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html).

## S3, if used

- Identify authoritative objects and attachment metadata. Exclude reproducible
  caches, temporary exports and backup destinations where appropriate; prevent
  recursive copies, overlapping policy selections and duplicate exports.
- Inspect versioning, lifecycle rules, replication and independently retained
  recovery points. Versioning preserves object history in the source bucket;
  replication copies selected changes to another bucket; independent backup adds
  recovery points with a verified separate protection boundary. These mechanisms
  are not interchangeable. Replication alone does not prove independent protection
  from propagated changes or privileged deletion.
- Choose the least combination covering actual failures. Respect bucket-level
  versioning effects on other workloads. Preserve application attachment deletion,
  noncurrent-version expiration, delete-marker and replicated-delete contracts;
  establish approved backup expiry and prevent restores from silently resurrecting
  data that must remain deleted. Check current service selection/exclusion support
  rather than assuming every backup mechanism can filter arbitrary prefixes.
- During authorized verification, restore selected objects to isolated test
  destinations; record source keys/versions, recovery points and restored object
  identities in a protected manifest. Verify expected content, size and metadata,
  including content checksums where available and version/delete-marker behavior.
  Match checksum algorithms and full-object versus composite semantics against
  trusted backup-time evidence. Record unavailable checksums as a coverage limit;
  object presence or a newly computed checksum without a trusted comparison does
  not establish original-content integrity.

Sources: [S3 versioning and lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html),
[replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html),
[AWS Backup for S3](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html),
[S3 content-integrity checks](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html).

## Cosmos DB, if used

- Inspect the account's actual periodic or continuous backup policy, API, retention,
  supported restore scope and existing recovery evidence. Disabled continuous
  backup does **not** establish "no backups": periodic platform protection may
  already apply. Unread or unavailable configuration remains unverified.
- Reuse sufficient periodic protection. If PITR or other objectives require
  continuous mode, choose the smallest supported recovery-window tier meeting
  them, checking API/cloud/region/provider support, migration reversibility and
  pricing. Do not mandate the longest tier or add duplicate export jobs by default.
- Verify what the mode restores and what needs separate recovery, including
  analytical data, account settings, identities and application cutover. Add
  independent protection only for requirements native coverage cannot meet.
- Verify the actual API/mode's supported restore behavior and selection granularity
  in an isolated target. Explicitly restore or configure the necessary identity,
  management/data-plane RBAC, firewall, private endpoints and private DNS through
  the approved Terraform workflow; do not assume the backup recreates them.
  Continuous restores omit RBAC and private-network settings. Verify scoped access
  and representative application queries using the restored target's endpoint;
  service-side restore completion alone does not prove application recovery.

Sources: [Cosmos DB backup modes](https://learn.microsoft.com/en-us/azure/cosmos-db/online-backup-and-restore),
[continuous backup and limitations](https://learn.microsoft.com/en-us/azure/cosmos-db/continuous-backup-restore-introduction).

## Azure Blob Storage, if used

- Inventory existing account-level versioning, blob/container soft delete, change
  feed, point-in-time restore, lifecycle and locks before proposing policy changes.
  Account-level settings can affect unrelated containers, retention and cost;
  container selection does not narrow every account-level capability.
- Operational protection retains recovery data in the source account. Vaulted
  protection retains a separate managed copy. Reuse sufficient existing coverage;
  justify vaulted protection for an uncovered failure boundary or retention need.
  Check current policy/API/provider compatibility: do not promise a standalone
  operational policy if the supported new-policy path requires vaulted protection.
  Native account protection may suffice without a new Backup policy; a policy
  default alone does not justify adding a vault.
- Explicitly choose protected containers and exclusions. Review automatic coverage
  of future containers, supported blob/account types and deleted-container restore
  limits. Preserve attachment deletion and approved expiry across versions, soft
  deletes and vault recovery points; test metadata/object reconciliation on restore.
  Do not assume a blob restore can recover a deleted container or storage account.
- Verify selected restored files: check content/checksums where available, size,
  required metadata/versions and relationships to restored database records.
  Detect missing attachments, wrong versions and orphans. Operational Blob restore
  rolls back data in the source account: never run it against production for a
  drill. Use a supported isolated recovery path; if the existing protection cannot
  supply one, record the live-verification gap rather than changing protection or
  adding a vault automatically. Qualify vaulted restore target restrictions too.

Sources: [Azure Blob backup modes and account effects](https://learn.microsoft.com/en-us/azure/backup/blob-backup-overview),
[support matrix and container scope](https://learn.microsoft.com/en-us/azure/backup/blob-backup-support-matrix),
[Blob restore behavior](https://learn.microsoft.com/en-us/azure/backup/blob-restore).

## PostgreSQL, only if actually used

- Inspect managed-service or existing database backup/PITR coverage and the existing
  approved backup destination before introducing another job or storage target.
- Select logical capture, base backup plus required WAL, or supported consistent
  snapshots from the deployed engine/version and recovery objectives. A live copy
  of database files is not automatically a valid backup. Account for roles,
  extensions, tablespaces and other cluster/configuration dependencies as needed.
- Coordinate database capture with associated persistent files/attachments using
  a documented write-quiesce protocol, atomic coordinated snapshots, or a proven
  immutable/versioned-file manifest tied to the database recovery point. Include
  WAL and all required volumes for physical recovery. A consistent database dump
  alone does not make separately copied files application-consistent.
- Reuse the protected destination; capture checksums, the recovery-point association
  and the restore order. Test database-to-file references and deletion reconciliation
  together. Do not add PostgreSQL to a project merely to follow this section.
- Verify coordinated database and persistent-file recovery in an isolated instance
  and file location using the documented recovery-set manifest and consistency
  method. Check archive/manifest integrity with compatible tools where supported,
  required WAL/replay recovery, schema/data invariants and representative queries,
  then database-to-file references and application behavior. For compatible base
  backups, pg_verifybackup can check backup integrity; it does not replace an
  actual restore or application test. A dump listing or database startup is only
  partial evidence. Keep restored workers and queue consumers disabled.

Sources: [PostgreSQL backup methods](https://www.postgresql.org/docs/current/backup.html),
[logical capture](https://www.postgresql.org/docs/current/backup-dump.html),
[filesystem consistency](https://www.postgresql.org/docs/current/backup-file.html),
[pg_verifybackup scope and limits](https://www.postgresql.org/docs/current/app-pgverifybackup.html).
Use the documentation for the project's deployed PostgreSQL version.

## Terraform, access, monitoring and cost

- For authorized implementation, use the project's existing documented Terraform
  deployment roots and state ownership. Expose explicit **create** or **reference
  existing** choices for necessary policies, destinations/vaults, keys and roles
  where appropriate; allow disabled only for optional coverage. Validate existing
  identifiers and ownership. Reference customer-owned protection without silently
  importing, replacing or changing it. Reuse monitoring destinations and storage.
- Scope backup, restore and monitoring identities to necessary resources/actions.
  Protect backup storage against unauthorized reading/deletion, apply necessary
  at-rest/in-transit encryption and key permissions, and verify keys remain usable
  for the recovery period. Additional customer-managed keys, immutability and
  separate accounts/regions require a documented need and deletion-contract review.
- Route backup failures, missed/stale recovery points and required restore-test
  failures to existing monitoring/alert destinations with named responders. For
  platform-managed backups, verify available health/recovery evidence and signals;
  do not invent scheduled job events or treat a Terraform apply as backup success.
- Estimate incremental cost using data size, object count, change/write/delete rate,
  retained versions/WAL, recovery window and measured restore volume. Identify
  region/currency/date, assumptions and relevant storage, protected-instance,
  request/list/inventory, change-feed/replication, restore/retrieval, transfer,
  compute, logging and key-operation meters. Separate existing costs from additions,
  account for included allowances, and avoid pricing PITR as if all services bill
  per daily full copy. Missing inputs make the estimate incomplete, not zero.

## Integrity and restoration preparation

Apply the same smallest, lowest-cost decision standard to verification. Reuse
existing backups, recovery tooling, monitoring/alert destinations and suitable
execution environments. A retained, relevant successful recovery test may satisfy
a requirement when its scope, versions and recovery objectives still match;
document any uncovered change instead of duplicating sufficient verification.

- **REQUIRED before claiming recovery works:** sufficient successful verification
  for the claimed scope, isolated targets, meaningful integrity and application
  checks, and retained results. Configuration review cannot satisfy this condition.
  Verify documented recovery objectives; do not invent targets or mandatory test
  frequencies. A documentation-only project can prepare a plan/runbook and report
  live recovery as unverified without executing a drill.
- **RECOMMENDED:** read-only backup-health checks for completion, freshness,
  recoverable range, permissions/key availability and failures, using existing
  monitoring. Prepare a reusable on-demand verifier and temporary-resource IaC in
  the application's established repository layout. Keep discovery/health checks,
  authorized restore orchestration and read-only validation as explicit phases;
  running a health check must not create targets or trigger a restore.
- **OPTIONAL unless documented policy requires them:** scheduled restore automation,
  permanent test environments and broader disaster-recovery exercises. Label any
  justified addition with its requirement and incremental cost; do not introduce a
  permanent runner, extra region, new alert destination or testing schedule by
  default. Temporary resources are execution choices, not mandatory standing
  infrastructure.

Repository preparation should define inputs for data scope and exclusions,
recovery-point selection, isolated destinations, consistency/version manifests,
expected checks, permitted identities, cost bounds and cleanup ownership. Use the
existing Terraform conventions and deployment roots for supporting infrastructure;
prepare reviewed plans and create/reference choices rather than another
provisioning path. Qualify provider-native restore operations and Terraform
ownership/state handling for resources they create; if the approved IaC workflow
cannot represent a required operation, record the gap instead of hiding it in
local-exec or bypassing the project's infrastructure policy. Repository preparation
and successful local tests do not authorize infrastructure creation, live restores,
resource deletion or live-setting changes.

## Isolated verification safeguards

- Validate account/subscription, region, resource identifiers and target bindings
  before an authorized run. Refuse production destinations, overwrites and automatic
  cutover. Use separate test targets with scoped identities, protected storage and
  the necessary encryption; restrict recovered-data access before validation.
- Disable outbound business actions and queue/event consumption throughout drills,
  including workers, schedulers, notifications, webhooks and integration writeback.
  Use fixtures/stubs and allow only necessary restoration, verification and
  monitoring traffic. Check these controls before starting the recovered app;
  network isolation alone does not prove its consumers cannot run.
- Before recovered data becomes accessible, reconcile expiry/TTL, deletion records,
  retention obligations and idempotency/in-flight/completed-operation state. Prevent
  resurrection of data that must remain deleted and replay of completed business
  actions. Do not reset production markers or permissions to make a test pass.
- Do not assume independently restored services form a consistent recovery set.
  Use approved transaction boundaries, watermarks or versioned manifests to show
  database/object references align; document any time skew and accepted loss.
  Block recovery claims and data access when required reconciliation is unresolved.
- Compare restored content against trusted expected data using supported checksum
  algorithms and scope. Do not treat ETags or hashes of identifiers as content
  checksums. Validate schemas, key records, relationships, permissions and supported
  application read flows; counts, resource readiness or a health response alone
  do not establish meaningful application recovery.
- Define sample selection, exclusions and checked coverage before reporting results.
  Sampled verification supports only its tested scope, not a claim of full-data or
  full-system recovery. Separate synthetic-fixture validation from recovery of real
  backup data; record untested dependencies and failure scenarios.
- Bound temporary-resource lifetime and cost, identify the owner and prepare scoped
  cleanup through the existing Terraform workflow. Run cleanup only when separately
  authorized, against verified drill-owned targets; preserve source backups and
  retained evidence. Report failed or pending cleanup and remaining resources
  rather than assuming deletion succeeded.

## Map schedules to requirements; keep evidence separate

If a requirement says **daily incremental / weekly full**, record its applicable
control/contract identifier, revision, scope, required outcomes and approved
interpretation. Map each obligation to the actual managed-service recovery model,
available recovery points, retention, failure isolation and restore procedure.
Continuous backups or incremental storage accounting do not, by themselves, prove
equivalence to that wording. Conversely, do not add duplicate daily exports or
weekly full-copy jobs merely to match names. Record unsupported mappings or gaps
for the control owner; do not declare compliance equivalence without evidence.

Report these evidence levels separately:

1. **Backup configuration:** Terraform/configuration inspection, selected scope,
   compatibility, identities/key access, retention and monitoring wiring. Local
   linting, mocked tests and a valid Terraform plan are configuration evidence.
2. **Successful backup completion:** service/job status and usable recovery-point
   identity/range, protected scope, timestamps, completion and freshness evidence.
   A configured policy or successful submission is not a completed backup.
3. **Successful data restoration:** an authorized restore completed into an isolated
   target, with checked content/integrity, recovery-set consistency and documented
   loss/gaps. Service completion is insufficient when required data checks fail.
4. **Successful application recovery:** the isolated application uses the restored
   data with necessary identities/networking, passes meaningful functional/access
   checks and expiry/deletion/idempotency reconciliation, and meets the documented
   recovery objectives for the claimed scope. Data restoration alone does not prove
   application recovery. Production cutover is a separate authorized operation.

Retain protected results using existing result storage and monitoring; prefer a
machine-readable report with a concise operator summary rather than a new reporting
service. Record run/owner identity, source and target
scope, recovery-point identifiers and timestamps, software/provider versions,
sample selection, expected/observed checks, failures/skips, start/end times,
observed recovery-point loss and recovery duration (with measurement boundaries),
comparison with documented RPO/RTO, and cleanup status/remaining resources. Use
explicit passed, failed and not-run/unverified states at each evidence level;
failed or untested required checks block the corresponding success claim. Retain
results for the approved retention period without sensitive payloads, secrets or
unnecessary personal identifiers; use protected manifests or sanitized references.

A plan or successful apply proves neither backup completion nor restorability.
Local integrity tooling and configuration tests are not live recovery evidence.
Documentation-only work leaves execution and live recovery evidence outstanding;
never weaken or extend existing retention just to make a configuration test pass.

## Source verification — 2026-10-24

Documentation review only: no cloud settings changed and no backup or restore ran.
The linked AWS DynamoDB/S3, Azure Cosmos DB/Blob, and PostgreSQL references were
checked for the distinctions above. Recheck current support for the actual cloud,
region, API and pinned provider before implementation; no fixed retention tier,
price, or protection combination is prescribed here.

Cosmos DB periodic backups can provide existing protection; continuous restore
does not restore all networking, RBAC, regions or stored code. Azure Blob's current
new-policy flow requires vaulted backup when adding operational backup; that does
not authorize adding a vault or changing an existing policy. Operational restores
overwrite the source account, so they are unsuitable for a production drill.

For FedRAMP, retrieve the applicable released control baseline, transition rules
and approved system implementation from [FedRAMP requirements](https://www.fedramp.gov/2026/).
The [Rev5 control guidance](https://www.fedramp.gov/2026/reference/rev5-control-guidance/)
must be checked for the governing release. Historical daily-incremental/weekly-full
wording appears in the [optional review-initiation checklist RFC](https://www.fedramp.gov/rfcs/0003/);
the [CP-family update RFC](https://www.fedramp.gov/rfcs/0028/) describes proposed
changes and transition context. An RFC, optional checklist or managed-service
feature is not itself proof of the current binding control or of equivalence.
The consolidated control-guidance page could not be fetched in this review; its
exact current control wording and applicability remain unverified. Escalate that
specific mapping to the control owner instead of declaring compliance or adding
duplicate jobs.

Release disposition: the user deferred FedRAMP control/compliance mapping for
the 2026-10-24 configuration cleanup. It is not a blocker for that release;
revisit the mapping when requested. This disposition makes no compliance claim
and does not change any application's existing protection or control obligations.
