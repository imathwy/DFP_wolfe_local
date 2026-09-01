# Crosswalk artifacts

`numbering-current.json` is the bootstrap output for the synchronized latest
manuscript.
It is not yet the release snapshot: the manuscript uses a global theorem
counter, while the current PaperForge simulator uses section-reset theorem
numbers.

`lean-decl-map.json` is the reviewed local map for all nine theorem-like
statements. Its records point to the exact declaration wrappers and source
lines in the audited Lean snapshot. It can be used for local PaperForge badges;
the global theorem-numbering gate still controls publication. The older
`lean-decl-map.candidate.json` is retained as provenance for the initial
two-entry bootstrap proposal.

The sentence-level manifest lives beside the publication source in
`../DFP_counterexample/sentence-locks.json`. It is intentionally separate from
the theorem crosswalk: inline claim tags can cite reusable `ReasLib` interfaces,
while the accepted PaperForge badge map remains the nine statement-level
crosswalk.
