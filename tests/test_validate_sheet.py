import unittest

from scripts.validate_sheet import slug_filename, validate_rows


FIELDS = [
    "sku_name",
    "description",
    "format",
    "garnish_left",
    "garnish_right",
    "garnish_back",
    "garnish_notes",
    "output_filename",
]


class ValidatorTests(unittest.TestCase):
    def test_slug_filename(self):
        self.assertEqual(slug_filename(" Cocoa Protein 30! "), "cocoa-protein-30.png")

    def test_valid_row_is_normalized(self):
        errors, rows = validate_rows(
            FIELDS,
            [{"sku_name": "Iced Americano", "description": "Coffee over ice", "format": "ICED"}],
        )
        self.assertEqual(errors, [])
        self.assertEqual(rows[0]["format"], "iced")
        self.assertEqual(rows[0]["garnish_left"], "none")
        self.assertEqual(rows[0]["output_filename"], "iced-americano.png")

    def test_duplicate_garnish_requires_repeat_note(self):
        errors, _ = validate_rows(
            FIELDS,
            [{
                "sku_name": "Lime Slush",
                "description": "Frozen lime cooler",
                "format": "slush",
                "garnish_left": "lime halves",
                "garnish_right": "lime halves",
            }],
        )
        self.assertTrue(any("multiple zones" in error for error in errors))

    def test_unsupported_format_fails(self):
        errors, _ = validate_rows(
            FIELDS,
            [{"sku_name": "Cola", "description": "Cola", "format": "bottle"}],
        )
        self.assertTrue(any("unsupported format" in error for error in errors))


if __name__ == "__main__":
    unittest.main()

