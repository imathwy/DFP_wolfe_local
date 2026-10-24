"""Regression checks for audit rejection paths; no Lean compilation required."""

import unittest
import hashlib
from pathlib import Path
from unittest.mock import patch

from audit_latest import check_manuscript, code_only, parse_axioms


class AuditTests(unittest.TestCase):
    def test_nested_comments_and_strings(self):
        source = '/- sorry /- axiom -/ admit -/\n"sorry \\" axiom" -- admit\ntheorem t := sorry'
        masked = code_only(source)
        self.assertEqual(len(masked), len(source))
        self.assertEqual(masked.count("sorry"), 1)
        self.assertEqual(masked.count("\n"), source.count("\n"))

    def test_unterminated_comment_rejected(self):
        with self.assertRaises(ValueError):
            code_only("/- unfinished")

    def test_multiline_and_axiom_free_output(self):
        log = ("'A' depends on axioms: [propext,\n Classical.choice, Quot.sound]\n"
               "'B' does not depend on any axioms\n")
        self.assertEqual(parse_axioms(log, ["A", "B"])["B"], [])

    def test_unapproved_axioms_rejected(self):
        for axiom in ("sorryAx", "Project.assumption"):
            with self.subTest(axiom=axiom), self.assertRaises(ValueError):
                parse_axioms(f"'A' depends on axioms: [{axiom}]", ["A"])

    def test_missing_malformed_or_unexpected_output_rejected(self):
        for log in ("", "'A' depends on axioms: broken",
                    "'B' does not depend on any axioms"):
            with self.subTest(log=log), self.assertRaises(ValueError):
                parse_axioms(log, ["A"])

    def test_duplicate_output_rejected(self):
        with self.assertRaises(ValueError):
            parse_axioms("'A' does not depend on any axioms\n" * 2, ["A"])

    def test_omitted_manuscript_is_not_checked(self):
        result = check_manuscript(None, "0" * 64)
        self.assertEqual(result["status"], "not_checked")

    def test_matching_manuscript(self):
        data = b"manuscript"
        expected = hashlib.sha256(data).hexdigest()
        with patch.object(Path, "read_bytes", return_value=data):
            result = check_manuscript(Path("paper.tex"), expected)
        self.assertEqual(result["status"], "matched")
        self.assertEqual(result["sha256"], expected)

    def test_changed_manuscript_rejected(self):
        with patch.object(Path, "read_bytes", return_value=b"changed"):
            with self.assertRaisesRegex(ValueError, "Manuscript SHA256 mismatch"):
                check_manuscript(Path("paper.tex"), "0" * 64)

    def test_missing_manuscript_rejected(self):
        with patch.object(Path, "read_bytes", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                check_manuscript(Path("missing.tex"), "0" * 64)


if __name__ == "__main__":
    unittest.main()
