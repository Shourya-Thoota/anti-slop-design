import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "design_audit", Path(__file__).resolve().parents[1] / "scripts/design_audit.py")
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)


class DesignAuditTests(unittest.TestCase):
    def test_black_white_contrast(self):
        self.assertAlmostEqual(AUDIT.contrast_ratio("#000000", "#ffffff"), 21)

    def test_identical_contrast(self):
        self.assertEqual(AUDIT.contrast_ratio("#123456", "#123456"), 1)

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            AUDIT.contrast_ratio("#fff", "#000000")

    def test_placeholder_and_focus_are_review_not_verdict(self):
        result = AUDIT.inspect_source('<a href="#">go</a>\n<style>a{outline:none}</style>', "a.html")
        self.assertEqual({v["rule_id"] for v in result}, {"placeholder-link", "focus-removal"})
        self.assertTrue(all(v["status"] == "needs_review" for v in result))
        self.assertEqual(result[1]["line"], 2)

    def test_empty_alt_is_not_missing(self):
        self.assertEqual(AUDIT.inspect_source('<img src="a" alt="">', "a.html"), [])

    def test_image_without_alt(self):
        result = AUDIT.inspect_source('<img src="a">', "a.html")
        self.assertEqual(result[0]["rule_id"], "image-alt-source-review")

    def test_repo_exclusions_and_clean_not_conformant(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "node_modules").mkdir()
            (root / "node_modules" / "x.html").write_text('<a href="#">x</a>')
            (root / "index.html").write_text('<main><h1>Records</h1></main>')
            result = AUDIT.audit(root)
            self.assertEqual(result["files_scanned"], 1)
            self.assertEqual(result["findings_count"], 0)
            self.assertIn("No findings does not mean the quality gate passed.", result["limitations"])

    def test_invalid_root(self):
        with self.assertRaises(ValueError):
            AUDIT.audit("/this-is-not-a-project-1234")

    def test_symlink_not_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "copy.html").symlink_to("/etc/hosts")
            result = AUDIT.audit(root)
            self.assertEqual(result["files_scanned"], 0)
            self.assertEqual(result["skipped"][0]["reason"], "symlink_or_outside_root")


if __name__ == "__main__":
    unittest.main()
