# TASK-08: Parameterized planar strong-Wolfe assembly

## Objective

Assemble the checked asymptotic, endpoint, and strong-Wolfe adapters into the
paper-facing planar theorem with symbolic Wolfe constants. The target must state
the paper's quantifiers, not merely repackage `(1 / 4, 3 / 4)`.

## Sole ownership

Write only this new file:

```text
ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedPlanar.lean
```

Do not edit `Theorem_2_3`, `Theorem_Main_theorem`, the existing weak certificate,
or any Wave 1 companion. If a missing interface is found, report it rather than
patching another file.

## Required public result

Prove (or provide the smallest sound certificate immediately below it)

```lean
theorem existsPlanarStrongWolfeCounterexample
    {c₁ c₂ : ℝ} (hc₁_pos : 0 < c₁)
    (hc₁_lt_two_thirds : c₁ < 2 / 3)
    (hc₂_ge_two_thirds : 2 / 3 ≤ c₂) (hc₂_lt_one : c₂ < 1) :
    Nonempty (DFP.StrongWolfeCounterexample
      (Fin 2) (1 / 2) (3 / 2) c₁ c₂)
```

The proof may derive `c₁ < c₂` as a local named fact. Reuse the exact orbit,
realized-objective, Hessian-bound, gradient-limit, and DFP-orbit interfaces from
the fixed planar proof. Choose the initial scale using the margin-dependent
`endpointArmijo_of_lt_two_thirds`; use the exact phase ratios through
`endpointStrongWolfe_of_endpointData` (or an equivalent stable adapter).

## Acceptance criteria

- `lake lean` on this file returns RC0.
- No `sorry`, `admit`, `sorryAx`, project `axiom`, `#check`, or `#print` remains.
- A temporary import probe can construct the theorem for symbolic coefficients.
- The handoff records whether the objective/Hessian bounds remain exactly
  `(1 / 2, 3 / 2)` and gives the first remaining blocker if the full result is
  not reachable.

## Dependencies and estimate

Depends on the frozen `ParameterizedWolfe.lean`, `StrongWolfeCounterexample.lean`,
and the existing Theorem 2.3 infrastructure. Expected effort: **1--3 days**;
most work is factoring the fixed proof's scale-selection block without changing
the source construction.

## Handoff

Completed and frozen. `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedPlanar.lean`
is 15,435 bytes, SHA256
`30ddd393c2f781da9d448c7baedecc7d10bdc031ed97bda98862028a924f5b8c`.
A fresh `lake lean` check returned RC0 with warnings only. The theorem uses
symbolic `c₁,c₂` throughout the Armijo, weak-curvature, and strong-Wolfe
fields; the Hessian bounds remain exactly `(1 / 2, 3 / 2)`. Static scans found
no `sorry`, `admit`, `sorryAx`, project `axiom`, `#check`, or `#print`. The
all-dimensional transport is now frozen separately in TASK-09.
