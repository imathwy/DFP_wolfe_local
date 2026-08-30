# TASK-11: Parameterized Main theorem and public facade

## Objective

After TASK-08--10 freeze their theorem names, add a paper-faithful Main API and
expose only the stable theorem-facing imports. Keep the fixed-parameter negative
theorems as compatibility aliases or clearly named corollaries.

## Sole ownership

Only these existing files may be edited:

```text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean
DFPWolfe.lean
```

Do not edit any ReasLib source or theorem producer. Never reintroduce the old
giant infrastructure import list or `MetricTopSectionCertificateAdapter`.

## Required API

Expose a theorem whose quantifiers visibly match
`0 < c₁ < 2 / 3`, `2 / 3 ≤ c₂ < 1`, plus the all-dimensional and
identity-initialized corollaries when their producers are green. Names must make
the quantifier scope clear; fixed-constant names remain marked
`fixedParameters`.

## Acceptance criteria

- Fresh `lake lean` RC0 on Main and facade.
- External import probe resolves the parameterized theorem and its negation of
  `GlobalWeakWolfeConvergenceAt` (and, if stated, the universal wrapper).
- No production probes or debt tokens; record exact hashes and axioms.

## Dependencies and estimate

Depends on TASK-08--10. Expected effort: **0.5--1 day**.

## Handoff

Completed and frozen. `Theorem_Main_theorem.lean` now exports
`existsStrongWolfeCounterexample_of_parameterRange`,
`main_not_globalWeakWolfeConvergence_of_parameterRange`, its explicit
`forall_parameterRange` wrapper, level-set negative variants, literal
paper-range negation predicates, and the automatic matrix identity-liminf
theorem. `DFPWolfe.lean` publicly imports all semantic and matrix producers
while retaining the fixed-parameter aliases. Fresh serial `lake lean` checks of
Main and the facade both returned RC0 (dependency/header warnings only).

Current source hashes:

- Main SHA256 `7d6cc3d0ca5c1910a719659078bb35fbc0609547a83334f35c9bd04ff3d71037`.
- Facade SHA256 `6f12fc459a67ef681da77a57b11cbe28858747e0ef39b7af78f8c5180c99cc99`.

Static scans found no production probes or debt tokens (the word “admits” in a
module docstring is prose). Strong certificates project directly to the existing
weak global-negation adapter. The identity alias remains available as a
conditional operator interface, while the automatic matrix theorem supplies the
unconditional paper-facing certificate with generated bounds and `liminf`.
