# DFP PaperForge Instance

This directory is the PaperForge working instance for
*A counterexample to global convergence of classical DFP under the standard
strong Wolfe conditions* (arXiv:2608.21708). The Lean formalization remains in
the parent repository; this instance references it through
`[formalizations.primary]` and keeps generated paper/site artifacts separate.

## Current state

- Publication draft is maintained at `../DFP_counterexample/main.tex`; the
  reproducible adapter `scripts/sync-latest-draft.py` generates the converter-
  compatible `inputs/draft/main.tex` and records the publication SHA-256.
- PaperForge scaffold initialized with the `DFPWolfe` formalization module.
- Five author records and a domain-specific project homepage are present.
- The reviewed declaration map in `crosswalk/lean-decl-map.json` covers all
  nine theorem-like statements in the latest draft; the original candidate is
  retained for provenance.
- The rendered Lean badges resolve through the checked-in source-level index at
  `web-assets/site/formalizations/DFPWolfe/`; each entry links to the pinned
  GitHub file and line. This is a deliberate fallback until a doc-gen4 subset
  is generated.
- The sentence-lock manifest now inventories 584 natural-language sentences,
  including theorem/proof prose and captions. It records 65 Lean-locked
  sentences, 40 inline sentence links, and explicit boundary categories for
  the remaining evidence and editorial text. A further 234 mathematical prose
  records are marked `unmapped-claim` for future declaration-level review.
- `paperforge ingest --bootstrap` completes with a local lxml/XSLT-compatible
  environment and writes the generated PreTeXt tree and numbering snapshot.
- The instance is not release-ready yet. Do not treat `source/` or `output/`
  as a faithful publication build until the gates below are closed.

## Gates before the first published build

1. Add a PaperForge numbering profile for a global theorem counter. The current
   draft numbers the main results globally (Theorem 1, Corollary 2,
   Proposition 3, Lemmas 4--9), while the existing simulator resets theorem
   counters at each section. The source-to-Lean links are independent of this
   display-numbering gate.
2. Extend the converter for the `figure` and outer `table` environments, and
   provide the referenced `Fig1.pdf` and `Fig2.pdf` assets. The current
   interactive edition keeps their captions as empirical boundary records and
   replaces omitted figure/table references with plain text.
3. The declaration map has been manually reviewed against the current Lean
   types and is usable for local badges. Promote it for a release only after
   the global-numbering snapshot is fixed. The Lean source currently preserves
   historical Lemma 3.x--6.x citations, so this requires a matched old
   snapshot rather than a blind renumbering.
4. Add exact paper-facing wrapper declarations where a Lean theorem is only
   logically equivalent to, but not textually the same as, a paper statement.
   In particular, compare the main existential theorem with
   `DFP.existsStrongWolfeCounterexample_of_parameterRange` and the identity
   initialization corollary with
   `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange`.
5. Generate a curated doc-gen4 subset and an `atlas-graph.json` for the
   blueprint. Publish `DFPWolfe` first; the complete ReasLib import closure is
   too large for an initial GitHub Pages deployment.
6. Commit reproducible comparator Challenge/Solution wrappers and a config,
   then add the exact comparator command and source/toolchain hashes to the
   reproducibility page.
7. The section-summary gate is handled by explicit waivers in `paper.toml` for
   divisions whose opening prose is already the summary; revisit those waivers
   if the manuscript structure changes.

The release environment must also provide Python 3.11+, `lxml`, PreTeXt, and
the optional PDF/LaTeX utilities listed by `paperforge doctor`.

## Useful commands

Run these from the PaperForge checkout, with this directory as the instance:

```sh
paperforge doctor DFP_wolfe_paperforge
paperforge ingest --bootstrap DFP_wolfe_paperforge
paperforge build web DFP_wolfe_paperforge --plan
paperforge build site DFP_wolfe_paperforge --plan
```

The latest converter pass over the synchronized draft produces 102 numbered
items, 9 theorem-like statements, 8 proof spans, and 87 prose paragraphs. The
publication-only correspondence macros, figures, tables, and URLs are removed
by `scripts/sync-latest-draft.py` before conversion; the publication source and
its figures remain unchanged in `../DFP_counterexample/`. The pass is
syntactically valid XML and emits only the known omitted-figure/reference
warnings. The validator now passes its objective checks (with the explicit
section-summary waivers above) and reports only that no external plagiarism
sources are configured. The remaining release gates are intentionally recorded
here instead of being hidden by the bootstrap artifacts.

## Licensing

The parent Lean project is Apache-2.0. PaperForge is used as an external build
tool; any PaperForge templates or assets copied into a distributable site must
retain their own license and copyright notices.
