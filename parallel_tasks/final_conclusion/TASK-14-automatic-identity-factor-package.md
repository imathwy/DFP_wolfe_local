# TASK-14: Automatic identity factor package

## Objective

Reduce the conditional TASK-10 identity interface by deriving its factor and
quantitative map bounds automatically from the positive-definite initial inverse
Hessian of a parameterized strong-Wolfe certificate.

## Sole ownership

Write only this new file:

```text
ReasLib/Optimization/DFP/WolfeCounterexample/AutomaticIdentityFactor.lean
```

Do not edit TASK-10, Main, the facade, or matrix/operator infrastructure.

## Required result

For a `StrongWolfeCounterexample (Fin n) (1/2) (3/2) c₁ c₂` in the paper range,
derive a positive factor `L`, explicit positive scalar bounds `a,b,q`, and the
factor/map inequalities required by
`identityInitializedStrongWolfe_of_factorized`; return the resulting
identity-initialized strong operator certificate. Keep the output bounds
explicit and do not claim a matrix `InverseIteration` conversion.

## Acceptance

Fresh `lake lean` RC0, no local debt/probes/embedded proof fragments, and an
axiom audit using only the accepted foundations. If an API prevents the full
automatic package, retain a sound smaller factor/bound lemma and document the
exact first blocker.

## Handoff

Completed and frozen. `AutomaticIdentityFactor.lean` is 7,213 bytes, SHA256
`7705dad88d72f802de8a435953e192a9c53cc744596712993c373c74e210cac9`, and its
fresh `lake lean` check returned RC0 with warnings only. The helper
`factorAndBounds_of_initialPosDef` uses the existing positive-operator lower
bound and matrix square-root APIs; the public
`exists_identityInitializedStrongWolfe_of_initialPosDef` then supplies
`a = q = μ` and `b = ‖A‖ + 1` to the TASK-10 strong operator certificate. Static
debt/probe/embedded scans are clean. The module is now publicly imported by
`DFPWolfe.lean`. The former matrix-congruence follow-up is completed by
`AutomaticMatrixIdentityLiminf.lean` and the TASK-15 Main export; this file
remains the reusable lower-level operator package.
