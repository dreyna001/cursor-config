from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import global_setup


class GlobalSetupTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.source = self.root / "canonical" / "codex"
        self.source.mkdir(parents=True)
        (self.source / "global-instructions.md").write_text("# Global instructions\n", encoding="utf-8")
        self.add_skill("alpha", "Alpha skill description.")
        self.add_skill("beta", "Beta skill description.")
        global_setup.write_source_manifest(self.source, apply=True)
        self.codex_home = self.root / ".codex"
        self.agents_home = self.root / ".agents"

    def tearDown(self) -> None:
        self.temp.cleanup()

    def add_skill(self, name: str, description: str) -> None:
        package = self.source / "skills" / name
        package.mkdir(parents=True, exist_ok=True)
        (package / "SKILL.md").write_text(
            f"---\nname: {name}\ndescription: {description!r}\n---\n\n# {name}\n",
            encoding="utf-8",
        )

    def test_plan_is_read_only_and_lists_expected_links(self) -> None:
        result = global_setup.install(self.source, self.codex_home, self.agents_home, apply=False)
        self.assertFalse(result["applied"])
        self.assertEqual(result["skill_count"], 2)
        self.assertEqual(len(result["changes"]), 3)
        self.assertFalse(self.codex_home.exists())
        self.assertFalse(self.agents_home.exists())

    def test_install_backups_conflicts_and_preserves_unowned_paths(self) -> None:
        self.codex_home.mkdir()
        (self.codex_home / "AGENTS.md").write_text("old global instructions\n", encoding="utf-8")
        (self.codex_home / "skills" / ".system").mkdir(parents=True)
        (self.codex_home / "skills" / ".system" / "sentinel").write_text("keep\n", encoding="utf-8")
        (self.codex_home / "skills" / "alpha").mkdir()
        (self.codex_home / "skills" / "alpha" / "SKILL.md").write_text("old alpha\n", encoding="utf-8")
        (self.agents_home / "skills" / "alpha").mkdir(parents=True)
        (self.agents_home / "skills" / "alpha" / "SKILL.md").write_text("user alpha\n", encoding="utf-8")
        (self.agents_home / "skills" / "unmanaged").mkdir()
        (self.agents_home / "skills" / "unmanaged" / "keep.txt").write_text("keep\n", encoding="utf-8")

        result = global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)

        self.assertTrue(result["applied"])
        self.assertEqual(result["skill_count"], 2)
        agents_link = self.codex_home / "AGENTS.md"
        self.assertTrue(global_setup.is_same_symlink(agents_link, self.source / "global-instructions.md"))
        for name in ("alpha", "beta"):
            self.assertTrue(global_setup.is_same_symlink(self.agents_home / "skills" / name, self.source / "skills" / name))
        self.assertEqual((self.codex_home / "skills" / ".system" / "sentinel").read_text(encoding="utf-8"), "keep\n")
        self.assertEqual((self.agents_home / "skills" / "unmanaged" / "keep.txt").read_text(encoding="utf-8"), "keep\n")

        backup_root = Path(result["backup_directory"])
        backup_manifest = json.loads((backup_root / "manifest.json").read_text(encoding="utf-8"))
        backed_up = {Path(item["original_path"]).name: item for item in backup_manifest["items"]}
        self.assertEqual(len(backup_manifest["items"]), 3)
        self.assertTrue((backup_root / "codex" / "AGENTS.md").is_file())
        self.assertTrue((backup_root / "agents" / "skills" / "alpha" / "SKILL.md").is_file())
        self.assertTrue((backup_root / "legacy-codex-skills" / "alpha" / "SKILL.md").is_file())
        for item in backup_manifest["items"]:
            self.assertEqual(global_setup.item_sha256(Path(item["backup_path"])), item["sha256"])
        self.assertEqual(len(backed_up), 2)  # The two alpha entries share a basename.
        self.assertTrue(global_setup.verify_static(self.source, self.codex_home, self.agents_home)["valid"])

    def test_reinstall_is_idempotent_and_creates_no_second_backup(self) -> None:
        first = global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)
        manifest_path = self.codex_home / global_setup.INSTALLED_MANIFEST
        manifest_before = manifest_path.read_bytes()
        backups_before = sorted((self.codex_home / "backups").iterdir()) if (self.codex_home / "backups").exists() else []

        second = global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)

        self.assertEqual(first["changes"], [
            {"action": "link", "target": str(self.codex_home / "AGENTS.md"), "source": str(self.source / "global-instructions.md")},
            {"action": "link", "target": str(self.agents_home / "skills" / "alpha"), "source": str(self.source / "skills" / "alpha")},
            {"action": "link", "target": str(self.agents_home / "skills" / "beta"), "source": str(self.source / "skills" / "beta")},
        ])
        self.assertEqual(second["changes"], [])
        self.assertEqual(manifest_path.read_bytes(), manifest_before)
        backups_after = sorted((self.codex_home / "backups").iterdir()) if (self.codex_home / "backups").exists() else []
        self.assertEqual(backups_after, backups_before)

    def test_global_override_blocks_install_without_changes(self) -> None:
        self.codex_home.mkdir()
        override = self.codex_home / "AGENTS.override.md"
        override.write_text("user override\n", encoding="utf-8")
        with self.assertRaisesRegex(global_setup.SetupError, "overrides global instructions"):
            global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)
        self.assertEqual(override.read_text(encoding="utf-8"), "user override\n")
        self.assertFalse(self.agents_home.exists())
        self.assertFalse((self.codex_home / "AGENTS.md").exists())

    def test_partial_install_failure_restores_backups_and_removes_new_links(self) -> None:
        self.codex_home.mkdir()
        old_instructions = self.codex_home / "AGENTS.md"
        old_instructions.write_text("old instructions\n", encoding="utf-8")
        legacy_system = self.codex_home / "skills" / ".system" / "sentinel"
        legacy_system.parent.mkdir(parents=True)
        legacy_system.write_text("system skill stays\n", encoding="utf-8")
        old_legacy_skill = self.codex_home / "skills" / "alpha"
        old_legacy_skill.mkdir()
        (old_legacy_skill / "SKILL.md").write_text("old alpha\n", encoding="utf-8")
        unmanaged = self.agents_home / "skills" / "unmanaged" / "keep.txt"
        unmanaged.parent.mkdir(parents=True)
        unmanaged.write_text("unmanaged skill stays\n", encoding="utf-8")

        installed_manifest = self.codex_home / global_setup.INSTALLED_MANIFEST
        prior_manifest_bytes = json.dumps(
            {"schema_version": 1, "owner": global_setup.OWNER, "managed_skills": ["prior-state"]},
            indent=2,
            sort_keys=True,
        ).encode("utf-8") + b"\n"
        installed_manifest.write_bytes(prior_manifest_bytes)

        actual_symlink = global_setup.os.symlink
        symlink_calls = 0

        def fail_after_first_link(source: Path, target: Path, *args: object, **kwargs: object) -> None:
            nonlocal symlink_calls
            symlink_calls += 1
            if symlink_calls == 2:
                raise OSError("injected link failure")
            actual_symlink(source, target, *args, **kwargs)

        with patch.object(global_setup.os, "symlink", side_effect=fail_after_first_link):
            with self.assertRaisesRegex(OSError, "injected link failure"):
                global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)

        self.assertEqual(old_instructions.read_text(encoding="utf-8"), "old instructions\n")
        self.assertEqual((old_legacy_skill / "SKILL.md").read_text(encoding="utf-8"), "old alpha\n")
        self.assertFalse((self.codex_home / "AGENTS.md").is_symlink())
        self.assertFalse((self.agents_home / "skills" / "alpha").exists())
        self.assertEqual(legacy_system.read_text(encoding="utf-8"), "system skill stays\n")
        self.assertEqual(unmanaged.read_text(encoding="utf-8"), "unmanaged skill stays\n")
        self.assertEqual(installed_manifest.read_bytes(), prior_manifest_bytes)

    def test_source_name_must_match_package_name(self) -> None:
        (self.source / "skills" / "alpha" / "SKILL.md").write_text(
            "---\nname: different\ndescription: test\n---\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(global_setup.SetupError, "does not match its directory"):
            global_setup.discover_skills(self.source)


    def learning_fixture(self):
        self.add_skill("contextual-learning", "Linux conditional learning")
        instructions = "# Shared rules\n\n<!-- BEGIN contextual-learning managed section -->\nLinux learning activation\n<!-- END contextual-learning managed section -->\n\n# Other rules\n"
        (self.source / "global-instructions.md").write_text(instructions)
        global_setup.write_source_manifest(self.source, apply=True)

    def test_linux_keeps_learning_and_original_harness(self):
        self.learning_fixture()
        with patch.object(global_setup.sys, "platform", "linux"):
            result = global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)
            self.assertEqual(result["skill_count"], 3)
            self.assertTrue((self.agents_home / "skills/contextual-learning").is_symlink())
            self.assertIn("Linux learning activation", (self.codex_home / "AGENTS.md").read_text())
            self.assertTrue(global_setup.verify_static(self.source, self.codex_home, self.agents_home)["valid"])

    def test_nonlinux_excludes_learning_from_discovery_and_harness(self):
        self.learning_fixture()
        for platform in ("win32", "darwin"):
            with self.subTest(platform=platform), patch.object(global_setup.sys, "platform", platform):
                result = global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)
                self.assertEqual(result["skill_count"], 2)
                self.assertFalse((self.agents_home / "skills/contextual-learning").exists())
                text = (self.codex_home / "AGENTS.md").read_text()
                self.assertNotIn("Linux learning activation", text)
                self.assertIn("# Shared rules", text)
                self.assertIn("# Other rules", text)
                self.assertTrue(global_setup.verify_static(self.source, self.codex_home, self.agents_home)["valid"])

    def test_nonlinux_existing_learning_is_preserved_and_blocks_install(self):
        self.learning_fixture()
        existing = self.agents_home / "skills/contextual-learning/personal.txt"
        existing.parent.mkdir(parents=True)
        existing.write_text("keep existing work")
        with patch.object(global_setup.sys, "platform", "win32"):
            with self.assertRaisesRegex(global_setup.SetupError, "Linux-only"):
                global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)
        self.assertEqual(existing.read_text(), "keep existing work")
        self.assertFalse((self.codex_home / "AGENTS.md").exists())

    def test_stale_generated_nonlinux_harness_is_rejected(self):
        self.learning_fixture()
        (self.source / "global-instructions.nonlinux.md").write_text("incorrect learning activation")
        with self.assertRaisesRegex(global_setup.SetupError, "Non-Linux instructions are stale"):
            global_setup.install(self.source, self.codex_home, self.agents_home, apply=True)
        self.assertFalse(self.codex_home.exists())

    def test_malformed_managed_section_is_rejected(self):
        with self.assertRaisesRegex(global_setup.SetupError, "Malformed"):
            global_setup.without_linux_learning("keep\n<!-- BEGIN contextual-learning managed section -->\n")

    def test_learning_helper_refuses_nonlinux_before_reading_store(self):
        import subprocess
        helper = Path(__file__).resolve().parents[1] / "skills/contextual-learning/scripts/lessons.py"
        result = subprocess.run([sys.executable, "-c", "import sys,runpy; sys.platform='win32'; runpy.run_path(sys.argv[1],run_name='__main__')", str(helper)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Linux-only; no lesson files were read or written", result.stderr)
        self.assertNotIn("ModuleNotFoundError", result.stderr)


    def test_interpreter_caches_do_not_change_source_fingerprint(self):
        before = global_setup.tree_digest(self.source, ["alpha", "beta"])
        cache = self.source / "skills/alpha/__pycache__"
        cache.mkdir()
        (cache / "example.cpython-314.pyc").write_bytes(b"local bytecode")
        self.assertEqual(before, global_setup.tree_digest(self.source, ["alpha", "beta"]))
        (self.source / "skills/alpha/SKILL.md").write_text("real source change")
        self.assertNotEqual(before, global_setup.tree_digest(self.source, ["alpha", "beta"]))


if __name__ == "__main__":
    unittest.main()
