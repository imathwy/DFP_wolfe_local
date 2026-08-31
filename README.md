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
lake lean DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean
```

The main exported declarations include:

- `DFP.main_not_globalWeakWolfeConvergence_of_parameterRange`
- `DFP.not_PaperRangeGlobalWeakWolfeConvergence`
- `DFP.not_PaperRangeLevelSetGlobalWeakWolfeConvergence`
- `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange`

## Code scale

The figures below are measured from the tracked source tree (2026-08-31). Build
products, local proof-stage state, generated audits, manuscript working copies,
and temporary probes are excluded by `.gitignore`.

| Metric | Value |
| --- | ---: |
| Tracked files | 830 |
| Lean source files | 823 |
| Physical Lean lines | 153,149 |
| Non-blank Lean lines | 142,936 |
| Lean source size | 6.80 MiB |
| Declaration heads | 3,694 |
| `ReasLib` Lean files | 616 |
| `DFPWolfe` Lean files | 205 |

The declaration-head total is a reproducible source-level count of lines whose
declaration keyword is one of `theorem`, `lemma`, `def`, `abbrev`, `structure`,
or `instance`; it is not a count of the full imported mathlib environment.
The breakdown is 2,996 theorems, 185 lemmas, 408 definitions, 13 abbreviations,
86 structures, and 6 instances.

## License

The formalization code is released under the **Apache License, Version 2.0**.
See [LICENSE](LICENSE) for the complete terms. Copyright 2026 Zichen Wang.
