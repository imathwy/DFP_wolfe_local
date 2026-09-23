# DFP Wolfe Counterexample

This repository is the Lean 4 and mathlib formalization accompanying the paper
[*A counterexample to global convergence of classical DFP under the standard
strong Wolfe conditions*](https://arxiv.org/html/2608.21708v1).

The paper authors are Benqi Liu, Zichen Wang, Zaiwen Wen, Liwei Zhang, and
Yaxiang Yuan. The formalization author is **Zichen Wang**.

The formalization develops a uniformly convex, globally Hessian-bounded
counterexample for the classical inverse-form Davidon-Fletcher-Powell (DFP)
method. It formalizes the weak-Wolfe global-convergence question, a stronger
strong-Wolfe counterexample in the paper's coefficient range, all-dimensional
transport, level-set semantics, and the identity-initialized matrix
`liminf` corollary.

The repository contains the reusable `ReasLib` infrastructure, the paper-facing
`DFPWolfe` declarations, and the matrix/operator coordinate-change bridges.

## Associated paper

**Title:** *A counterexample to global convergence of classical DFP under the
standard strong Wolfe conditions*

**arXiv:** [2608.21708v1](https://arxiv.org/html/2608.21708v1) (`math.OC`,
22 August 2026)

## Requirements

- Lean 4 `v4.32.0`
- mathlib `v4.32.0`

## Checks

```sh
lake lean DFPWolfe.lean
lake lean DFPWolfe/Paper.lean
lake lean DFPWolfe/Main.lean
```

The [paper correspondence index](DFPWolfe/README.md) maps the current manuscript's
eleven numbered statements to individual files directly in `DFPWolfe/` and to
their Lean proof declarations. The main exports include:

- `DFP.main_not_globalWeakWolfeConvergence_of_parameterRange`
- `DFP.not_PaperRangeGlobalWeakWolfeConvergence`
- `DFP.not_PaperRangeLevelSetGlobalWeakWolfeConvergence`
- `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange`
- `DFP.existsStrongWolfeCounterexampleHolderSharp_of_dimension_ge_two`
- `DFP.existsMatrixIdentityLiminfStrongWolfeHolder`
- `DFP.main_planarWeakWolfeConvergence`
- `DFP.main_planarStrongWolfeConvergence`
- `DFP.SecantIteration.planarDegeneration`

`DFPWolfe/Main.lean` provides the convergence and nonconvergence interfaces;
`DFPWolfe/Paper.lean` also exports the independent results used in the paper,
including the local invariant graph and the complete limiting-circle statement.
Each paper statement has a numbered navigation file with its LaTeX label,
mathematical summary, and `#check` commands for the existing declarations,
including all components of multi-part results. Proofs are organized by
mathematical topic in `ReasLib`. Obsolete numbered wrappers, generic
infrastructure checks, and unused implementation branches remain removed;
the eleven current paper navigation files are intentionally retained.

The September 23, 2026 reorganization passed all three checks above. An ephemeral
`#print axioms` audit of 27 principal declarations, covering all eleven numbered
paper results and the convergence-negation interfaces, found only `propext`,
`Classical.choice`, and `Quot.sound`. Source scans found no proof placeholders
or custom axioms. Navigation `#check` commands are confined to the eleven
paper correspondence files in `DFPWolfe`; no `#check` or `#print` commands
are retained in `ReasLib`. Existing style warnings
remain; these checks do not claim a warning-free tree.

A subsequent source-polishing pass preserved all declaration signatures while
simplifying the matrix identity-initialization bridges and the minimizer-uniqueness
proof. Three inactive proof blocks (692 lines) were removed. Targeted `lake lean`
checks and the root check passed; an expanded audit of 36 declarations, including
the modified interfaces, again found only the three standard axioms above.

A second polishing pass reused the radius limit in the limiting-circle proof and
the existing quadratic coefficients in the truncated Taylor-germ interface. It
removed redundant simplification arguments and inactive tactics, eliminating 66
warning diagnostics in the four modified modules. Their declaration signatures
were preserved. Targeted checks, the root check, and an expanded 85-declaration
axiom audit passed; other modules still have existing style warnings.

The paper navigation pass added eleven correspondence files containing 32
declaration checks. Each file, `Paper.lean`, and the root entry point passed
`lake lean`. A fresh 36-declaration axiom audit covered every navigation target
and the principal convergence-negation interfaces, with only the three standard
axioms above. No proof declarations or signatures changed in this pass.

## Comparator verification

Before the September 2026 source reorganization, two proof interfaces were checked with
[`leanprover/comparator`](https://github.com/leanprover/comparator), using its
`v4.32.0` release to match this project's Lean toolchain. The checks used the
real `landrun` implementation (v0.1.18), so the Challenge build, export, and
Solution build/export ran under Linux Landlock restrictions.
The comparator/landrun command-line delimiter mismatch was handled by a
transparent argument-only adapter; it did not change any source or exported
proof content. The temporary Challenge/Solution wrappers were outside the
tracked tree and were removed after the checks.

| Comparator target | Result |
| --- | --- |
| `DFP.main_not_globalWeakWolfeConvergence_of_parameterRange` | `Your solution is okay!` |
| `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange` | `Your solution is okay!` |

For both targets, comparator found matching Challenge/Solution declarations,
accepted the Solution with the Lean default kernel, and found no axioms beyond
`propext`, `Classical.choice`, and `Quot.sound`. The independent
`lake lean DFPWolfe.lean` check also returned successfully.

Comparator certifies declaration identity, kernel acceptance, and the stated
axiom budget. It does not by itself establish that every formal definition has
the intended correspondence with the paper; that remains the subject of the
separate semantic-fidelity review. A one-shot export of the entire root module
was intentionally not used because it exceeded the practical memory budget;
the two targeted proof-interface checks completed successfully. These are historical
results, not a comparator validation of the reorganized tree or the newer regularity
and convergence theorems.

## Code scale

The figures below are measured from the reorganized Lean source tree (2026-09-23). The
adjacent `DFP_counterexample/` and `DFP_wolfe_paperforge/` directories contain
publication and presentation sidecars; they are excluded from these Lean-code
metrics. Build products, local proof-stage state, generated audits, manuscript
working copies, and temporary probes are excluded by `.gitignore`.

| Metric | Value |
| --- | ---: |
| Lean source files, including the two root modules | 447 |
| Physical Lean lines | 113,931 |
| Non-blank Lean lines | 107,119 |
| Lean source size | 5.11 MiB |
| Declaration heads | 3,707 |
| `ReasLib/` Lean files | 432 |
| `DFPWolfe/` Lean files | 13 |

The declaration-head total counts active source declarations introduced by
`theorem`, `lemma`, `def`, `abbrev`, `structure`, or `instance`. Nested block
comments, line comments, and string literals are excluded; leading attributes
and declaration modifiers are recognized. It is not a count of the full imported
mathlib environment. The breakdown is 2,866 theorems, 290 lemmas, 492 definitions,
3 abbreviations, 51 structures, and 5 instances, including private declarations.
This corrects the earlier line-based count, which included commented-out text
and omitted declarations with attributes on the same line.

Before reorganization the tracked Lean tree had 828 files and 159,815 physical
lines. The cleanup removes generic diagnostic wrappers, unused proof branches,
and the obsolete fixed-parameter compatibility results. Every remaining source
module belongs to the import closure of `DFPWolfe` or the empty `ReasLib` root.
The paper's sixth-order amplitude estimate is retained; its polynomial expansion
reuses the canonical proof instead of a second copy of that calculation.

## License

The formalization code is released under the **Apache License, Version 2.0**.
See [LICENSE](LICENSE) for the complete terms. Copyright 2026 Zichen Wang.
