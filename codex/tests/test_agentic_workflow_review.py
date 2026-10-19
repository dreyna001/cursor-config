from __future__ import annotations

import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "skills/agentic-security-workflows/scripts/validate_review.py"
spec = importlib.util.spec_from_file_location("validate_review", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ReviewValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "product").mkdir()
        (self.root / "product/source.py").write_text("def review_saved_revision(): pass\n")
        self.review = {
            "schema_version": 1, "use_case": "threat_hunting", "review_level": "source_only",
            "review_date": "2026-10-19", "source_revision": "a" * 40,
            "objective": "Review the decision boundary.", "boundaries": ["Human approval."],
            "limits": ["No live qualification."], "variants": [{"id": "native", "root": "product"}],
            "evidence": [{"id": "source", "variant": "native", "kind": "source", "path": "product/source.py", "anchor": "review_saved_revision"}],
            "capabilities": [{"id": "approval", "status": "partial", "assessment": "Reviewed source only.", "evidence_ids": ["source"]}],
            "work_items": [{"id": "version", "priority": "P1", "type": "verification", "status": "verification_required", "capability_id": "approval", "problem": "Concurrent revisions need verification.", "recommendation": "Verify exact version binding.", "acceptance": ["A stale version is rejected."], "evidence_ids": ["source"], "depends_on": []}],
        }

    def test_accepts_each_use_case_without_claiming_runtime_verification(self):
        for use_case in ("threat_hunting", "incident_response", "ssp_authoring"):
            with self.subTest(use_case=use_case):
                self.review["use_case"] = use_case
                self.assertEqual(validator.validate(self.review, self.root), [])

    def test_rejects_missing_source_anchor(self):
        self.review["evidence"][0]["anchor"] = "not_in_current_source"
        self.assertIn("source: anchor not found", validator.validate(self.review, self.root))

    def test_rejects_missing_sources_and_unknown_references(self):
        self.review["evidence"][0]["path"] = "product/missing.py"
        self.review["work_items"][0]["evidence_ids"] = ["unknown"]
        errors = validator.validate(self.review, self.root)
        self.assertIn("source: missing source file", errors)
        self.assertIn("version: unknown evidence 'unknown'", errors)

    def test_rejects_path_escape_and_cross_variant_sources(self):
        self.review["evidence"][0]["path"] = "../outside.py"
        self.assertIn("source path escapes repository", validator.validate(self.review, self.root))
        self.review["evidence"][0]["path"] = "elsewhere.py"
        (self.root / "elsewhere.py").write_text("review_saved_revision")
        self.assertIn("source: source outside variant", validator.validate(self.review, self.root))

    def test_rejects_duplicate_ids_and_cyclic_dependencies(self):
        self.review["evidence"].append(copy.deepcopy(self.review["evidence"][0]))
        self.review["work_items"][0]["depends_on"] = ["version"]
        errors = validator.validate(self.review, self.root)
        self.assertIn("duplicate evidence id: source", errors)
        self.assertIn("dependency cycle at version", errors)

    def test_rejects_missing_acceptance_and_unmeasured_status(self):
        self.review["work_items"][0]["acceptance"] = []
        self.review["work_items"][0]["status"] = "passed"
        errors = validator.validate(self.review, self.root)
        self.assertIn("version: observable acceptance criteria required", errors)
        self.assertIn("version: invalid work status", errors)

    def test_rejects_invalid_top_level(self):
        self.assertEqual(validator.validate([], self.root), ["review must be an object"])

    def test_malformed_field_types_return_errors_without_crashing(self):
        self.review["use_case"] = []
        self.review["review_level"] = {}
        self.review["evidence"][0]["variant"] = []
        self.review["capabilities"][0]["status"] = {}
        self.review["work_items"][0]["capability_id"] = []
        errors = validator.validate(self.review, self.root)
        self.assertIn("invalid use_case", errors)
        self.assertIn("invalid review_level", errors)
        self.assertIn("source: unknown variant", errors)
        self.assertIn("approval: invalid capability status", errors)
        self.assertIn("version: unknown capability", errors)


if __name__ == "__main__":
    unittest.main()
