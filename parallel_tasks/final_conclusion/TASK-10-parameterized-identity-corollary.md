# TASK-10: Parameterized identity-initialization corollary

## Objective

State the paper's affine-normalization corollary for symbolic Wolfe constants:
identity initial inverse Hessian, problem-dependent positive Hessian bounds, and
positive gradient liminf. Keep the non-isometric distortion explicit.

## Sole ownership

Write only this new file:

```text
ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedIdentityInitialization.lean
```

Do not edit the existing identity module, planar/all-dimensional theorem files,
or the public facade. Operator-level output is acceptable when a matrix
representation would introduce an unrelated theorem; state that boundary in the
docstring and handoff.

## Required public result

Give a reusable theorem that consumes TASK-08 or TASK-09's strong certificate and
returns an identity-initialized certificate for the same symbolic `(c₁,c₂)` pair,
with explicit lower/upper distortion constants. Also provide a fixed-index
specialization for `Fin 2` if it is cheap and sound.

The conclusion must expose `initialInverseHessian_eq_one` and must not claim that
the original fixed Hessian bounds survive an arbitrary affine pullback.

## Acceptance criteria

- Target check RC0 and static debt/probe scan clean.
- The theorem's hypotheses make every factor/map lower bound explicit; no hidden
  non-isometry assumption is allowed.
- Axiom audit uses only `propext`, `Classical.choice`, and `Quot.sound`.

## Dependencies and estimate

Depends on TASK-08/09 and the frozen `IdentityInitialization.lean`. Expected
effort: **0.5--1 day** for operator-level packaging; **1--2 days** if a concrete
matrix factorization is required.

## Handoff

Completed and frozen. The new
`ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedIdentityInitialization.lean`
is 16,584 bytes, SHA256
`2cf311f589d86f093838194827e5c1a9020252a0bcbf72b8da48ab09db536f03`.
A fresh `lake lean` check returned RC0 with dependency warnings only. The file
defines `IdentityInitializedStrongWolfeOperatorCertificate`, proves strong-Wolfe
transport through an arbitrary continuous linear equivalence, and exposes
`identityInitializedStrongWolfe_of_factorized` plus the dimension-indexed
explicit-witness wrapper. The initial inverse Hessian is exactly identity; the
output Hessian bounds are the explicit `(m * a, M * b)` distortion bounds and
the gradient tail is positive. Static debt/probe scans are clean and the public
axiom audit uses only `propext`, `Classical.choice`, and `Quot.sound`.
Construction of the factor and its matrix spectral constants is now completed
by `AutomaticIdentityFactor.lean` and the matrix-facing
`AutomaticMatrixIdentityLiminf.lean` producer; the explicit-input theorem in
this file remains available for modular use.
