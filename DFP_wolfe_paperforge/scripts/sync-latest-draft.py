#!/usr/bin/env python3
"""Prepare the PaperForge draft from the publication TeX source.

`DFP_counterexample/main.tex` is the publication-facing source and contains
PDF-only correspondence macros.  The PaperForge converter intentionally does
not execute arbitrary TeX macros, so this adapter removes only those macros
and presentation-only figure/table blocks.  Mathematical text, labels, refs,
and theorem environments are left unchanged.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


INSTANCE = Path(__file__).resolve().parents[1]
ROOT = INSTANCE.parent
SOURCE = ROOT / "DFP_counterexample" / "main.tex"
TARGET = INSTANCE / "inputs" / "draft" / "main.tex"


def remove_environment(text: str, env: str) -> str:
    pattern = re.compile(
        rf"\\begin\{{{re.escape(env)}\}}(?:\[[^]]*\])?.*?\\end\{{{re.escape(env)}\}}\s*",
        re.S,
    )
    return pattern.sub("\n", text)


def prepare(source: str) -> str:
    text = source
    # Remove the publication-only correspondence macro definitions in the
    # preamble, bounded by the marker and the title.
    # Use a callable replacement so the backslash in ``\title`` is not
    # interpreted as ``\t`` by the regular-expression replacement parser.
    text = re.sub(
        r"\n% Lean correspondence follows .*?\\title\{",
        lambda _match: "\n\\title{",
        text,
        flags=re.S,
    )
    # Remove all uses, including the multi-line calls in theorem blocks.
    text = re.sub(r"\\leanClaimTag\s*\{[^{}]*\}\s*\{[^{}]*\}\s*\{[^{}]*\}", "", text)
    text = re.sub(r"\\leanDeclTag(?:Extra)?\s*\{[^{}]*\}\s*\{[^{}]*\}", "", text)
    text = re.sub(r"\\leanDeclTagEnd\b", "", text)
    text = re.sub(r"\\lean(?:FormalizationReadme|DependencyMap)\s*\{\}", "", text)
    # These blocks are useful in the PDF but are not currently represented by
    # the PaperForge converter.  The source figures remain in DFP_counterexample
    # and the interactive site links to the arXiv HTML edition.
    text = remove_environment(text, "figure")
    text = remove_environment(text, "table")
    text = re.sub(r"\\FloatBarrier\b", "", text)
    # The omitted floating blocks still have prose cross-references. Replace
    # those refs with stable plain-language names rather than leaving broken
    # PreTeXt xrefs in the interactive edition.
    omitted_refs = {
        "fig:orbit-comparison": "the orbit-comparison figure",
        "fig:finite-gradient-comparison": "the finite-gradient figure",
        "tab:recurrence-verification": "the recurrence-verification table",
        "tab:finite-comparison": "the finite-comparison table",
    }
    for label, replacement in omitted_refs.items():
        # Remove the authored Figure(s)/Table(s) prefix together with the
        # reference macro; replacing the macro alone would yield prose such as
        # "Figures the orbit-comparison figure".
        def contextual_replacement(match: re.Match[str]) -> str:
            value = replacement
            prefix = match.string[:match.start()].rstrip()
            if not prefix or prefix[-1] in ".?!":
                value = value[:1].upper() + value[1:]
            return value

        text = re.sub(
            rf"(?:Figures?|Tables?)~?\\(?:C|c)ref\{{{re.escape(label)}\}}",
            contextual_replacement,
            text,
        )
        text = re.sub(
            rf"(?:Figures?|Tables?)~?\\ref\{{{re.escape(label)}\}}",
            contextual_replacement,
            text,
        )
        text = re.sub(rf"\\(?:C|c)ref\{{{re.escape(label)}\}}", replacement, text)
        text = re.sub(rf"\\ref\{{{re.escape(label)}\}}", replacement, text)
    text = re.sub(r"\\small\b", "", text)
    # Bibliography URLs are retained as plain text so the converter does not
    # emit an unknown `\\url` macro warning.
    text = re.sub(r"\\url\s*\{([^{}]*)\}", r"\1", text)
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    header = (
        "% Generated from ../DFP_counterexample/main.tex by "
        "scripts/sync-latest-draft.py.\n"
        f"% Publication source SHA-256: {digest}\n"
    )
    return header + text


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(prepare(source), encoding="utf-8")
    print(f"wrote {TARGET} from {SOURCE}")
    print(f"source_sha256={hashlib.sha256(source.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
