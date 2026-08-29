import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from src.file_list import list_files


class FileListTests(unittest.TestCase):
    def test_list_files_sorts_file_names(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "b.txt").write_text("b")
            (root / "a.txt").write_text("a")
            (root / "subdir").mkdir()
            (root / "subdir" / "ignore.txt").write_text("ignored")

            stdout = io.StringIO()
            with redirect_stdout(stdout):
                list_files(root)

            self.assertEqual(stdout.getvalue().splitlines(), ["a.txt", "b.txt"])

    def test_list_files_reports_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                list_files(Path(tmpdir))

            self.assertIn("No files found", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
