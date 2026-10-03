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


if __name__ == "__main__":
    unittest.main()
