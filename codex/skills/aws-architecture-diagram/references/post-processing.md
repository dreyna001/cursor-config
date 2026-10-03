# Manual XML and Layout Validation

The source Cursor plugin used a PostToolUse hook and fixer scripts. Those hooks
and scripts are not included in this Codex skill, so no automatic validation,
layout correction, or preview generation occurs after a file write.

Before handing off a diagram:

1. Parse the `.drawio` file as XML with an available XML parser or draw.io CLI.
2. Check for unique `mxCell` IDs and ensure every edge source/target points to an
   existing cell.
3. Confirm shape names against `aws4-shapes-services.md` and
   `aws4-shapes-resources.md`.
4. Review that icon colors, container parentage, step badges, external actors,
   and legend placement follow the relevant style and layout references.
5. If an optional export was requested, export only when the draw.io desktop CLI
   is already available; preserve the editable source file.

If the needed parser or renderer is unavailable, state which checks could not be
run. Do not claim that a hook, fixer, or preview URL ran when it did not.
