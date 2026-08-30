# TASK-03: Strong-Wolfe certificate and transport

## Objective

Package the strong-Wolfe part of the construction without breaking the existing
weak-Wolfe certificate. The lower-level exact ratio theorem already proves strong
curvature for ratios `1/3` and `2/3`, but the final `WolfeCounterexample` structure
currently stores only `weakWolfe`.

## Ownership

Write only this new module:

```text
ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean
```

Do not edit `WolfeCounterexample.lean` or its existing `Transport.lean`. Avoid
changing any paper theorem. The integration task may later choose to expose this
module or migrate its declarations.

## Suggested design

Prefer a new wrapper/extension structure around `DFP.WolfeCounterexample`, rather
than adding a field to the existing structure and breaking all current clients.
Choose one canonical strong predicate and document the choice:

- a vector-gradient `IsStrongWolfe` matching `IsWeakWolfe`, or
- an adapter to `LineSearch.Wolfe.IsStrong`/`IsStrongCurvature` using certified
  endpoint line derivatives.

The chosen predicate must include Armijo, endpoint differentiability, and absolute
curvature, not just a scalar ratio lemma.

## Required deliverables

1. A strong certificate type with the same orbit, Hessian, positive-step, and
   positive-limit projections as the weak certificate.
2. A constructor/adapter for the exact two-phase endpoint data, using the existing
   strong ratio facts.
3. Orthogonal-sum and linear-isometry transport for the strong field, or a precise
   blocker showing which map lemma is missing.
4. A theorem that strong curvature implies the corresponding weak curvature under
   the descent sign assumptions, if that bridge is needed for reuse.

## Acceptance criteria

- `lake lean ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean` returns zero.
- Existing weak certificate clients remain untouched and continue to compile.
- No `sorry`, `admit`, `sorryAx`, or project axiom.
- The handoff records the exact strong predicate and whether transport is complete.

## Dependencies and estimate

Reads `AbstractSecantStep/Wolfe/DiscreteRatio.lean`,
`TwoPhaseOrbit/Wolfe.lean`, and the existing weak transport. It can run in parallel
with Tasks 01, 02, and 04, but Task 06 must wait for its API decision. Estimated
human effort: **0.5--1.5 working days**.

## Handoff

Implemented in `ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean`.

- Frozen SHA256: `94b2257e2e0f21891a4153d7b8d5f870d0c3c21f726519db580969d6a66a6d1a`.
- Target check: `lake lean ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean`, RC0,
  warnings only.
- `LineSearch.IsStrongWolfe` contains endpoint differentiability, Armijo, and
  absolute curvature; it has a certified-gradient constructor and a descent-sign
  bridge to weak Wolfe.
- Exact two-phase endpoint adapters and orthogonal-sum/linear-isometry certificate
  transports are present.
- Static debt is clean; accepted axiom dependencies are only
  `propext`, `Classical.choice`, and `Quot.sound`.
