# TASK-01: Global-convergence predicate and negative wrapper

## Objective

Create a compact, mathematically honest global-convergence predicate and prove a
user-facing negation theorem using the existing fixed-constant weak-Wolfe
certificate. This task is the cheapest route to a final theorem of the form
“DFP is not globally convergent.”

## Ownership

Write only this new file:

```text
ReasLib/Optimization/DFP/GlobalConvergence.lean
```

Do not edit `WolfeCounterexample.lean`, either paper theorem, `Theorem_Main_theorem.lean`,
or `DFPWolfe.lean`. Those files belong to later integration.

## Suggested API

Use `DFP.InverseIteration`, `HasHessianBounds`, and
`LineSearch.IsWeakWolfe` rather than duplicating the DFP recurrence. A useful
shape is:

```text
GlobalWeakWolfeConvergence c₁ c₂ : Prop
```

quantifying over finite dimensions `n ≥ 2`, objective/constant data, positive
step lengths, and admissible `InverseIteration`s, with conclusion
`Tendsto (fun k => ‖gradient f (x k)‖) atTop (𝓝 0)`.

For the first deliverable, use the existing global `HasHessianBounds` notion
(bounds at every point), which is stronger than the paper's “relevant level
set” premise and avoids introducing a second level-set abstraction.

Provide one explicitly named theorem whose suffix makes the strength clear, for
example a fixed-parameter theorem at `(1/4,3/4)`. Optionally also prove the
logically weaker wrapper that negates a universal claim over all admissible
Wolfe constants. Do not present either as the paper's all-parameter theorem.

## Proof route

1. Extract `c` from `existsWeakWolfeCounterexample 2 (by omega)` (or use the
   planar theorem directly).
2. Apply the proposed global convergence predicate to `c.iteration` and its
   certificate fields.
3. Combine the resulting limit to `0` with `c.gradientNormTendsto` to
   `c.gradientLimit`.
4. Use uniqueness of limits in `ℝ` and `c.gradientLimitPos` for the contradiction.

The contradiction lemma should be kept generic if it has independent meaning,
for example “a real sequence with a strictly positive limit cannot tend to zero.”
Give every standalone helper its own docstring.

## Acceptance criteria

- `lake lean ReasLib/Optimization/DFP/GlobalConvergence.lean` returns zero.
- No local `sorry`, `admit`, `sorryAx`, or `axiom` in the new file.
- The theorem statement records exactly whether constants are fixed or universally
  quantified.
- A temporary `#print axioms` probe reports only accepted foundations; remove the
  probe before handoff.
- Handoff includes source hash, theorem names, and the exact quantifier scope.

## Non-goals

- Do not add strong Wolfe fields here.
- Do not parameterize the slow-curve/Armijo construction here.
- Do not alter the reusable certificate structure.

## Dependencies and estimate

Reads the existing `WolfeCounterexample` and Theorem 2.4 modules. It is independent
of Tasks 02--04. Estimated human effort: **0.5--1.5 working days**.

## Handoff

Implemented in `ReasLib/Optimization/DFP/GlobalConvergence.lean`.

- Frozen SHA256: `8fd4d4e38487eaf97a53ac3214f23e229d4cc06bbff6385bb9db30c42514620f`.
- Target check: `lake lean ReasLib/Optimization/DFP/GlobalConvergence.lean`, RC0.
- Main declarations: `GlobalWeakWolfeConvergenceAt`,
  `UniversalGlobalWeakWolfeConvergence`,
  `not_globalWeakWolfeConvergenceAt_of_counterexample`, and
  `not_universalGlobalWeakWolfeConvergence_of_counterexample`.
- The witness is fixed at `(c₁,c₂)=(1/4,3/4)`; this refutes a universal
  convergence predicate but is not the paper's all-parameter theorem.
- No local `sorry`, `admit`, `sorryAx`, or project axiom.
