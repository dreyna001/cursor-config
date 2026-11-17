# Customer release notes

Keep one customer-facing release history per product. Use the existing customer docs, portal or release page. If there is no existing location, keep a separate versioned release-notes document in the product docs and link it from their index. Add one newest-first entry per release with customer impact. Draft from the internal changelog, verified release scope and upgrade instructions. Keep developer detail in the internal changelog.

Lead with action customers must take, who needs to act, and any deadline or maintenance window. Give the release version or identifier and the actual date or availability. Keep each bullet to one customer outcome or requirement. Use only categories that apply. Mention availability by edition, environment or rollout stage when it matters. Link to approved instructions, API migration guides or advisories. Prepare required actions in time for customers to act, and record shipped changes in the history through the authorized publication process.

## Copyable entry

```markdown
# [Product] [version] · [release date or availability]

## Action required

[Who must act, what to do, and by when. Link to instructions. Omit if no action is required.]

## What changed

- **App and workflows** — [What users can now do or what works better.]
- **API and integrations** — [Which clients are affected, what changes, and any compatibility or migration detail.]
- **Administration and upgrades** — [Relevant prerequisites, downtime, configuration, deprecations or end-of-support dates.]
- **Fixes and reliability** — [A customer-visible issue that was resolved.]
- **Security** — [Approved customer impact or action and advisory link, when applicable.]

## Known limitations

[What is affected and a workaround if available. Omit if none apply.]
```
