# TASK-09: All-dimensional transport of the parameterized certificate

## Objective

Lift the parameterized planar strong-Wolfe certificate to every finite dimension
`n ≥ 2`, preserving the symbolic `(c₁,c₂)` range and the positive gradient tail.

## Sole ownership

Write only this new file:

```text
ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedTransport.lean
```

Do not edit TASK-08's file, Theorem 2.4, or existing transport modules. Use the
orthogonal-sum and linear-isometry equivalences already checked in
`StrongWolfeCounterexample.lean`; keep any finite-index/cast plumbing local.

## Required public result

Provide a theorem of the shape

```lean
theorem existsStrongWolfeCounterexample_of_dimension_ge_two
    (n : ℕ) (hn : 2 ≤ n) {c₁ c₂ : ℝ}
    (hc₁_pos : 0 < c₁) (hc₁_lt_two_thirds : c₁ < 2 / 3)
    (hc₂_ge_two_thirds : 2 / 3 ≤ c₂) (hc₂_lt_one : c₂ < 1) :
    Nonempty (DFP.StrongWolfeCounterexample
      (Fin n) (1 / 2) (3 / 2) c₁ c₂)
```

The exact index-transport representation may differ, but the conclusion must be
definitionally usable by downstream global-convergence negation lemmas. Do not
silently weaken the result to a weak-Wolfe certificate or fixed constants.

## Acceptance criteria

- Target check RC0, no local debt or production probes.
- Explicitly document the `Fin 2 ⊕ Fin (n - 2)` to `Fin n` equivalence (or the
  chosen canonical alternative) and the bound-preservation argument.
- Do not alter any existing source file. If TASK-08 is not green, keep this as a
  read-only prototype and report the dependency blocker.

## Dependencies and estimate

Depends on TASK-08 and the frozen strong transport APIs. Expected effort:
**0.5--1.5 days** once the planar theorem is available.

## Handoff

Completed and frozen. The new
`ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedTransport.lean`
is 2,356 bytes, SHA256
`bf27728d35dca9aa1070fa1a5ffcaa16933581697d5d0698b700caa3e8e69a62`.
Its fresh `lake lean` check on this exact snapshot returned RC0 (dependency
warnings only). The public
`existsStrongWolfeCounterexample_of_dimension_ge_two` theorem preserves the
symbolic range, the strong field, and `(1 / 2, 3 / 2)` bounds. It uses the
identity quadratic block, `m = n - 2`, the explicit `Fin` sum equivalence, and
the existing linear-isometry pullback. Static scans found no local debt or
production probes. TASK-10 may now depend on this file.
