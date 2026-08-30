# TASK-04: Identity-initialized counterexample corollary

## Objective

Assemble the paper's affine-normalization corollary: a counterexample whose initial
inverse Hessian is exactly the identity, with problem-dependent positive Hessian
bounds and a positive limiting (or liminf) gradient norm.

The generic pullback machinery already exists, but no final certificate-level
corollary currently packages it.

## Ownership

Write only this new reusable module:

```text
ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean
```

Do not edit `Operator/Orbit.lean`, `Gradient/Hessian.lean`,
`WolfeCounterexample/Transport.lean`, or the paper-facing theorem files.

## Required deliverables

1. A theorem that factors the initial positive-definite inverse Hessian through a
   continuous linear equivalence and applies `IsOrbit.pullback_of_initialFactor`.
2. A certificate-level result with an explicit identity initial inverse Hessian.
3. Transported objective smoothness, Hessian bounds, Wolfe conditions, and positive
   gradient-limit data.
4. A clear statement of the bound change: do not claim that identity initialization
   preserves the fixed `[1/2,3/2]` bounds unless it is actually proved.

Start with the current fixed-constant weak-Wolfe certificate. If Task 03 supplies a
stable strong wrapper, add a separate strong corollary rather than changing the weak
one in place.

## Proof guidance

- Reuse `DFP.Operator.IsOrbit.pullback_of_initialFactor` and the Hessian coordinate-
  change lemmas.
- Keep the square-root/factorization interface behind named local or standalone
  lemmas; do not unfold matrix constructors throughout the main proof.
- Preserve the positive limit when transporting the gradient by an invertible map;
  `liminf > 0` is acceptable only if the theorem statement deliberately chooses it.

## Acceptance criteria

- `lake lean ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean`
  returns zero.
- The theorem visibly states `H 0 = 1` (or the equivalent identity operator).
- No placeholders or project axioms.
- No edits outside the owned new module.

## Dependencies and estimate

Independent of the parameterization task; it reads the current weak certificate and
the pullback infrastructure. Estimated human effort: **1--2 working days**.

## Handoff

Implemented in `ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean`.

- Final frozen SHA256: `5a6b522b6ce6f3006518dbd2cd3f4d8ad1957c529e971c313db0e20885be4817`.
- Target check: `lake lean ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean`,
  RC0; only unused `ha`/`hb` warnings remain.
- `factorInitialInverseHessian_and_pullback` exposes the normalized operator orbit.
- `identityInitialized_of_factorized` returns an identity-initialized certificate
  with transformed bounds `(m*a, M*b)`, transported weak Wolfe data, and a positive
  eventual gradient lower bound.
- The certificate is intentionally operator-level. It does not claim that the
  original `[1/2,3/2]` Hessian bounds survive a non-isometric pullback unchanged.
- No placeholders, project axioms, `#check`, or `#print` remain; the axiom audit
  uses only `propext`, `Classical.choice`, and `Quot.sound`.
