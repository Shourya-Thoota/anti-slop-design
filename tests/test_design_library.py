import importlib.util
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("design_library", ROOT / "scripts/design_library.py")
lib = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lib)


class LibraryTests(unittest.TestCase):
    def test_integrity(self):
        self.assertEqual(set(lib.load_library()["modules"]),
                         {"frontend-design", "frontend-design-doc", "hallmark", "ui-ux-pro-max"})

    def test_read_entry(self):
        entry = lib.load_library()["modules"]["frontend-design"]["references/source-guide.md"]
        self.assertTrue(entry["text"])

    def test_unsafe_paths(self):
        for name in ["../escape", "/tmp/escape", "a/../../b", "a\\b", ""]:
            with self.assertRaises(ValueError):
                lib.safe_path(name)

    def test_materialize_and_reuse(self):
        data = lib.load_library()
        with tempfile.TemporaryDirectory() as folder:
            first = lib.materialize(data, "frontend-design", folder)
            second = lib.materialize(data, "frontend-design", folder)
            self.assertEqual(first, second)
            self.assertEqual((first / "references/source-guide.md").read_text(),
                             data["modules"]["frontend-design"]["references/source-guide.md"]["text"])

    def test_refuse_changed_output(self):
        with tempfile.TemporaryDirectory() as folder:
            data = lib.load_library()
            root = lib.materialize(data, "frontend-design", folder)
            (root / "SKILL.md").write_text("Local edits")
            with self.assertRaises(ValueError):
                lib.materialize(data, "frontend-design", folder)

    def test_refuse_symlink(self):
        with tempfile.TemporaryDirectory() as folder:
            root = pathlib.Path(folder)
            (root / "frontend-design").symlink_to(root, target_is_directory=True)
            with self.assertRaises(ValueError):
                lib.materialize(lib.load_library(), "frontend-design", root)


if __name__ == "__main__":
    unittest.main()
