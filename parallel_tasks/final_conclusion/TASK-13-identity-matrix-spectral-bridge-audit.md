# TASK-13: Identity matrix and spectral bridge audit

## Objective

Determine whether the conditional operator-level identity-initialization
certificate can be upgraded to the paper's unconditional matrix-facing
corollary from an arbitrary positive-definite initial inverse Hessian.

## Ownership

This is a read-only audit. Do not edit Lean source or generated artifacts. Record
only reusable existing declarations, exact missing bridges, and a grounded effort
estimate. Any later implementation must be assigned a separate new target file.

## Questions

1. Can existing matrix `PosDef`/square-root APIs produce a continuous linear
   equivalence `L` and the factor equation `H₀ = L.pushforward 1`?
2. Can finite-dimensional norm/order lemmas derive explicit positive `a`, `b`,
   and `q` for the Hessian and gradient transports?
3. Is there an existing `Operator.IsOrbit` to matrix `InverseIteration` bridge
   that preserves positive secant denominators and the strong-Wolfe field?

## Acceptance

The audit must distinguish an available theorem from a merely plausible route,
list exact declaration names/files, and state whether the current conditional
TASK-10 interface is already the correct release boundary.

## Handoff

Completed on 2026-08-30. The factor itself is available unconditionally from
`Matrix.PosDef.sqrtEquiv`, `sqrtEquiv_pushforward_one`, and
`sqrtEquiv_symm_pushforward`. Scalar lower/upper bounds are also derivable from
the positive spectrum and the Hermitian operator norm, but there is no one-step
matrix-to-CLM Loewner adapter. The larger missing bridge is the arbitrary
continuous-linear-equivalence conversion from `Operator.IsOrbit` back to a
matrix `InverseIteration`, including transformed matrix positive definiteness
and secant-denominator preservation.

TASK-14 implemented the factor/scalar/operator-bound portion in
`AutomaticIdentityFactor.lean` (fresh RC0), and TASK-15 completed the
operator-orbit-to-matrix `InverseIteration` bridge in
`AutomaticMatrixIdentityLiminf.lean` (fresh RC0).  The resulting theorem is
exported through Main and `DFPWolfe.lean`; the conditional operator theorem
remains available as a reusable intermediate interface.
