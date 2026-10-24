"""Regression checks for audit rejection paths; no Lean compilation required."""

import unittest

from audit_latest import code_only, parse_axioms


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


if __name__ == "__main__":
    unittest.main()
