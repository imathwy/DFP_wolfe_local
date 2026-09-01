# DFP Wolfe PaperForge Instance

This directory is the PaperForge instance for the Lean formalization of
[*A counterexample to global convergence of classical DFP under the standard
strong Wolfe conditions*](https://arxiv.org/html/2608.21708v1).

The formalization itself lives one directory above in the `DFP_wolfe_local`
Lean project. The instance keeps the editable manuscript, generated PreTeXt,
crosswalk artifacts, and eventual GitHub Pages site separate from that Lean
source tree.

## Layout

- `inputs/draft/main.tex`: converter-compatible snapshot generated from the
  publication source;
- `../DFP_counterexample/main.tex`: publication-facing manuscript with
  sentence/theorem-to-Lean links;
- `scripts/sync-latest-draft.py`: deterministic source synchronizer;
- `scripts/generate-declaration-index.py`: builds the pinned source-level
  resolver used by rendered Lean badges;
- `paper.toml`: PaperForge configuration and the parent `DFPWolfe` module link;
- `crosswalk/`: numbering and paper-to-Lean declaration maps;
- `source/`: generated PreTeXt (never hand-edit after the profile is fixed);
- `web-assets/site/`: the hand-authored project homepage and resource pages;
- `PAPERFORGE_STATUS.md`: release gates and the current conversion audit;
- `formalization.yaml`: machine-readable formalization metadata.

The current files are a bootstrap working state. Run
`python3 scripts/sync-latest-draft.py` after changing the publication source,
then run `python3 scripts/generate-declaration-index.py` after reviewing the
declaration map.
The numbering profile and figure/table conversion still require release review;
the local declaration crosswalk has been checked against the current Lean
statement shapes.
