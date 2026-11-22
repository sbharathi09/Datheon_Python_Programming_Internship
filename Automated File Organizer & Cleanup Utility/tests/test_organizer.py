import tempfile
import unittest
from pathlib import Path
from organizer import get_unique_path, EXTENSION_MAP


class OrganizerTests(unittest.TestCase):

    def test_extension_mapping(self):
        self.assertEqual(EXTENSION_MAP[".pdf"], "Documents")
        self.assertEqual(EXTENSION_MAP[".jpg"], "Images")
        self.assertEqual(EXTENSION_MAP[".zip"], "Archives")

    def test_unique_path(self):
        with tempfile.TemporaryDirectory() as temp:
            original = Path(temp) / "report.pdf"
            original.touch()

            result = get_unique_path(original)
            self.assertEqual(result.name, "report_1.pdf")

    def test_unknown_extension(self):
        self.assertEqual(
            EXTENSION_MAP.get(".xyz", "Others"),
            "Others"
        )


if __name__ == "__main__":
    unittest.main()
