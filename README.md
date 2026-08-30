# DFP Wolfe Counterexample

Lean 4 and mathlib formalization of a uniformly convex counterexample to
global convergence of the classical inverse-form DFP method under weak Wolfe
line search.

The repository contains the reusable `ReasLib` infrastructure, the paper-facing
`DFPWolfe` declarations, and the current semantic and matrix identity-
initialization bridges.

## Requirements

- Lean 4 `v4.32.0`
- mathlib `v4.32.0`

## Checks

```text
lake lean DFPWolfe.lean
lake lean DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean
```

The main exported declarations include:

- `DFP.main_not_globalWeakWolfeConvergence_of_parameterRange`
- `DFP.not_PaperRangeGlobalWeakWolfeConvergence`
- `DFP.not_PaperRangeLevelSetGlobalWeakWolfeConvergence`
- `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange`

Build products, local proof-stage state, generated audits, and temporary probes
are intentionally excluded by `.gitignore`.
