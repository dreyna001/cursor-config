#!/usr/bin/env python3
"""Generate legacy skill previews from the released offline UI companion."""
import argparse
import html
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    'skills/development-stack/references/unified-workspace-template.html',
    'codex/skills/development-stack/references/unified-workspace-template.html',
    'codex/skills/investigation-desk-ui/assets/unified-workspace-template.html',
)
PROFILE_LINKS = '''<script>
// Installed packages resolve the same companion through their user-profile root.
(() => {
  const path = location.pathname.replace(/\\\\/g, '/');
  const root = path.includes('/.cursor/skills/')
    ? '../../../../.agents/ui-baseline/'
    : path.includes('/.agents/skills/') ? '../../../ui-baseline/' : null;
  if (root) {
    const base = new URL(root, location.href);
    document.querySelectorAll('[data-suite-reference]').forEach(link => {
      link.href = new URL(link.dataset.suiteReference, base).href;
    });
  }
})();
</script>'''


def render(source, target):
    prefix = '../' * (len(Path(target).parts) - 1) + 'ui-baseline/'

    def link(match):
        href = html.unescape(match[1])
        if not href or href.startswith(('#', 'https:', 'http:', 'mailto:', 'data:')):
            return match[0]
        if ':' in href or href.startswith('/'):
            raise ValueError(f'Nonportable baseline link: {href}')
        value = html.escape(href, quote=True)
        return f'href="{prefix}{value}" data-suite-reference="{value}"'

    content = re.sub(r'href="([^"]*)"', link, source)
    return content.replace('</body>', PROFILE_LINKS + '\n</body>')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    source = (ROOT / 'ui-baseline/visual-reference.html').read_text(encoding='utf-8')
    for relative in TARGETS:
        expected = render(source, relative)
        target = ROOT / relative
        if args.check:
            if target.read_text(encoding='utf-8') != expected:
                raise SystemExit(f'Stale generated UI preview: {relative}')
        else:
            target.write_text(expected, encoding='utf-8')
    print(f'{len(TARGETS)} generated UI companions match the released baseline')


if __name__ == '__main__':
    main()
