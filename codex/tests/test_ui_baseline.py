"""Regression checks for bundle installation and preservation boundaries."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("sync_ui_baseline", ROOT / "scripts/sync_ui_baseline.py")
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class BaselineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.source = Path(self.tmp.name) / "source"
        self.destination = Path(self.tmp.name) / "destination"
        shutil.copytree(ROOT / "ui-baseline", self.source)

    def test_valid_release_and_idempotent_install(self):
        sync.install(self.source, self.destination)
        sync.install(self.source, self.destination)
        sync.compare_installed(self.source, self.destination)

    def test_modified_source_is_rejected(self):
        (self.source / "README.md").write_text("changed")
        with self.assertRaisesRegex(ValueError, "Modified baseline"):
            sync.install(self.source, self.destination)
        self.assertFalse(self.destination.exists())

    def test_local_edits_are_preserved(self):
        sync.install(self.source, self.destination)
        (self.destination / "README.md").write_text("local edit")
        with self.assertRaisesRegex(ValueError, "Modified baseline"):
            sync.install(self.source, self.destination)
        self.assertEqual((self.destination / "README.md").read_text(), "local edit")

    def test_unknown_local_files_are_preserved(self):
        sync.install(self.source, self.destination)
        note = self.destination / "personal-notes.txt"
        note.write_text("keep")
        sync.install(self.source, self.destination)
        self.assertEqual(note.read_text(), "keep")

    def test_new_release_file_cannot_overwrite_untracked_local_file(self):
        sync.install(self.source, self.destination)
        note = self.destination / 'new-reference.md'
        note.write_text('personal note')
        added = self.source / 'new-reference.md'
        added.write_text('published reference')
        manifest = json.loads((self.source / 'manifest.json').read_text())
        manifest['files'].append({'path': added.name, 'local_sha256': sync.digest(added)})
        (self.source / 'manifest.json').write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'untracked local file'):
            sync.install(self.source, self.destination)
        self.assertEqual(note.read_text(), 'personal note')

    def test_newer_installed_release_is_not_downgraded(self):
        sync.install(self.source, self.destination)
        manifest = json.loads((self.destination / "manifest.json").read_text())
        readme = self.destination / "README.md"
        readme.write_text(readme.read_text().replace('Version: **1.4.0**', 'Version: **99.0.0**'))
        manifest['version'] = '99.0.0'
        for item in manifest['files']:
            if item['path'] == 'README.md':
                item['local_sha256'] = sync.digest(readme)
        (self.destination / "manifest.json").write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "downgrade"):
            sync.install(self.source, self.destination)

    def test_all_apps_required_and_stylesheet_drift_detected(self):
        roots = []
        baseline = (self.source / "references/ai-enabled-threathunting/docs/suite-ui-standard.md").read_bytes()
        css = (self.source / "references/ai-enabled-threathunting/frontend/src/suite-workspace.css").read_bytes()
        for name, styles in sync.APP_CSS.items():
            root = Path(self.tmp.name) / name
            for path, data in [('docs/suite-ui-standard.md', baseline)] + [(p, css) for p in styles]:
                target = root / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            roots.append(root)
        self.assertEqual(sync.compare_apps(self.source, roots, None), 6)
        with self.assertRaisesRegex(ValueError, "three distinct"):
            sync.compare_apps(self.source, roots[:2], None)
        (roots[0] / sync.APP_CSS[roots[0].name][0]).write_text("drift")
        with self.assertRaisesRegex(ValueError, "Stylesheet drift"):
            sync.compare_apps(self.source, roots, None)


if __name__ == '__main__':
    unittest.main()
