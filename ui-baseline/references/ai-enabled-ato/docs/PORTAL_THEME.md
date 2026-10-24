# ATO theme mapping

The [Suite Workspace UI Standard](suite-ui-standard.md) is the authority for
current screen typography, palette, sidebar and equivalent control states.
This file records ATO-specific mappings; it does not define a competing scale.
The [generated visual companion](mockups/ssp-ui-explorations/10-unified-workspace-reference.html)
links to and embeds the current baseline. The older Federal SOC Dark theme,
Investigation Desk release and dated prototypes remain historical evidence.

ATO uses the existing React/Tailwind/Radix/Lucide components. In `portal/src/index.css`,
the app's `--primary` means the primary action fill and `--accent` means a hover
or selection fill; do not copy the HTML companion's token names without mapping
their meanings. The shared `portal/src/suite-workspace.css` supplies the baseline
and equivalent control decorations. The portal remains dark-only.

Preserve the system selector, work/context groups, assistant badge, review notice,
workflow navigation, draft guards, source access, document authoring layout,
approval gates and export contents. Screen typography does not replace authored
document or print/PDF rules. Do not change control sizes or pane arrangements to
imitate a sample. Status color never establishes approval or authorization.

The [conversion plan](SSP_UI_CONVERSION_PLAN.md#unified-template-adaptation--october-19)
records historical source/installed acceptance. Source and mocked browser checks
do not substitute for deployed-stack or customer qualification.
