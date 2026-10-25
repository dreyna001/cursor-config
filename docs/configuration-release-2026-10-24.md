# Configuration release verification — 2026-10-24

This release incorporates the previously pending configuration work: shared UI
guidance and current previews, routing, performance/testing standards, conditional
backup decisions, Linux-only contextual learning, and the optional Executive Navy
+ Orange presentation profile. It changes no application code or cloud settings.

The required Codex target is **WSL/Linux**. Native Windows Codex installation is
outside this release scope and is not an outstanding requirement. The user has
explicitly **deferred FedRAMP control/compliance mapping** for this cleanup.

## Verification performed

- `python3 -m unittest discover -s codex/tests`: 28 passed, including platform
  filtering, generated harness drift, conflicting-package preservation, helper
  refusal before store access, and cache-independent source fingerprints.
- `python3 -m unittest discover -s skills/contextual-learning/tests`: 18 passed.
- `python3 -m unittest discover -s codex/skills/contextual-learning/tests`: 18 passed.
  The helpers, synthetic fixtures/tests, lesson template, routing reference and
  backup reference were compared across their applicable distributions.
- Native Windows PowerShell 5.1 exercised the actual Cursor installer in an
  isolated fixture: excluded learning from both skill roots, stripped activation,
  preserved ordinary rules/skills and conflicting local work, and rejected a
  malformed managed section. Execution policy was unchanged. An unsigned UNC
  invocation was refused; the locally authored test harness exercised a local
  fixture without changing policy.
- Native Windows Codex planning selected 57 skills and the generated non-Linux
  harness; both actual helpers refused execution before accessing lesson storage.
  A full isolated Windows Codex link installation was attempted and rolled back
  when the host refused symbolic-link creation (WinError 1314). Full Windows
  Codex installation was not verified; it is **outside the required WSL scope**,
  with no follow-up installation required. No security
  policy, privileges, live learning store or Windows user configuration changed.
- Linux Codex `plan`, `sync --apply`, static verification and runtime discovery
  passed. Runtime discovery found all 58 managed skills with user scope and no
  duplicate managed entries in ATO, Hunt and the canonical Codex source context.
  The check used the existing cached Node 24 runtime; it made no model call.
- `python3 scripts/sync_ui_templates.py --check`: all three HTML companions match
  the released baseline. A Playwright check exercised all three repository
  previews plus installed Cursor/Codex path fixtures in Chromium, Firefox and
  WebKit (15 cases): baseline 1.14.0, keyboard entry, local links, and no script
  errors. A representative Chromium screenshot was visually inspected. These are static
  reference-preview checks, not application workflow or screen-reader sign-off.
- `python3 scripts/sync_ui_baseline.py check --installed` with all three app roots:
  version 1.14.0 and all six frontends verified. This release regenerates skill
  previews from that unchanged baseline; it does not change its visual rules,
  component source, application guards, or existing application qualification.
- Relative Markdown links, generated-source parity and staged whitespace checked.

The 64 Python tests and 15 browser cases above are distinct from the earlier
six-frontend release's application unit/workflow checks. No live cloud backup,
restoration, application recovery or deployment was performed.

## Backup-source review

The shared [conditional reference](../skills/cloud-native-platform-architecture/references/data-protection.md)
records the 2026-10-24 documentation review and its limits. It distinguishes
configuration, backup completion, restored-data integrity and application
recovery; it preserves existing coverage and requires justified additions.

Primary sources checked include [DynamoDB PITR](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html),
[AWS Backup for S3](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html),
[Cosmos DB modes](https://learn.microsoft.com/en-us/azure/cosmos-db/online-backup-and-restore),
[Cosmos DB restore exclusions](https://learn.microsoft.com/en-us/azure/cosmos-db/continuous-backup-restore-introduction),
[Blob backup policy behavior](https://learn.microsoft.com/en-us/azure/backup/blob-backup-overview),
[Blob support limits](https://learn.microsoft.com/en-us/azure/backup/blob-backup-support-matrix),
[Blob restores](https://learn.microsoft.com/en-us/azure/backup/blob-restore),
[PostgreSQL filesystem consistency](https://www.postgresql.org/docs/current/backup-file.html),
and [pg_verifybackup limits](https://www.postgresql.org/docs/current/app-pgverifybackup.html).

The FedRAMP review-initiation checklist and CP-family RFC were read as historical
or proposed context, not binding control text. The consolidated Rev5
control-guidance page could not be retrieved; exact current control wording and
system applicability remain unverified. The guidance requires the governing
released baseline, transition rules, approved implementation and control-owner
mapping before asserting equivalence or compliance. It prescribes no universal
daily export, vault, retention tier, extra region or restore frequency.

## Deferred scope

FedRAMP control-source reconciliation and compliance-equivalence mapping are
deferred at the user's direction. They are not blockers for this configuration
release. Revisit them only when that work is requested; retain the existing
conditional guidance without asserting compliance or altering cloud protection.
