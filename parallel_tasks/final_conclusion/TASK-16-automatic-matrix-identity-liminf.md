# TASK-16: Automatic Matrix Identity Liminf Bridge

## Objective

Complete the unconditional matrix-facing identity-initialization corollary.
Starting from the paper-range strong-Wolfe counterexample and its positive-
definite initial inverse Hessian, construct the square-root coordinate change,
retain the transformed orbit explicitly, and return a classical matrix
`InverseIteration` certificate with the paper's `0 < liminf ‖∇f(xₖ)‖`
conclusion.

## Deliverable

```text
ReasLib/Optimization/DFP/WolfeCounterexample/AutomaticMatrixIdentityLiminf.lean
```

The public existential theorem is
`exists_matrixIdentityLiminfStrongWolfe_of_initialPosDef`.  Main wraps it as
`DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange`, eliminating the
explicit factor and distortion constants from the paper-facing API.

## Semantic obligations

- `H₀ = I` is a matrix equality in the resulting `DFP.InverseIteration`.
- Hessian bounds are global and problem-dependent, with `0 < m ≤ M`.
- Every step satisfies strong Wolfe, hence also the weak-Wolfe predicate used by
  the global-convergence question.
- The transformed gradient norm is proved to have an eventual positive lower
  bound and an eventual finite upper bound; `positive_liminf_of_eventually_lower_upper`
  then gives the real-valued strict `liminf`.  No exact transformed norm limit
  is assumed.
- Matrix positive definiteness and secant denominators are proved from the
  normalized orbit and strict secant curvature, rather than inferred from an
  opaque `Nonempty` witness.

## Verification

- Source SHA256:
  `6999c15bd34485904cf0bf9145c665990bfc399a062e4e75a899afcd54b05f9a`
- Fresh `lake lean` target check: RC0, warnings only.
- Static scan: no `sorry`, `admit`, `sorryAx`, project `axiom`, `#check`, or
  `#print`; no prohibited embedded proof fragments.
- Axioms of the factorized and existential theorems:
  `[propext, Classical.choice, Quot.sound]`.

## Ownership

This producer imports `AutomaticIdentityFactor`,
`MatrixIdentityLiminfCertificate`, `SemanticProjections`, and the level-set
descent bridge. Main and `DFPWolfe.lean` are the integration owners; this file
is frozen and should not be edited for facade changes.
