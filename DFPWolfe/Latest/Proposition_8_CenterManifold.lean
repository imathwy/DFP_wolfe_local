module

public import DFPWolfe.V21.CenterManifold
public import DFPWolfe.V21.CenterInterpolation
public import DFPWolfe.Latest.CenterEndpoints

/-!
# Proposition 8 — the independent alternating center-manifold recurrence

Source label: `cm-center-proposition` in the latest `arXiv.tex`.
The exact spectral recurrence has derivative eigenvalues `1`, `−1/9`, `0`,
a locally invariant C⁷ graph, the source cubic graph coefficients `198/5`
and `8`, and inverse-cubic slow scale. Its literal initialized trajectory
has positive definite matrices at every stage.

The following Section 6 entries retain the same physical recurrence,
two-step center cancellation, limiting amplitude, full limiting circle,
and conditional explicit interpolation. The new quadratic endpoint entry
proves the phase decreases `2/3`, `5/6` and endpoint Wolfe inequalities
before imposing any interpolation-support separation condition.
The two constructions are independent; they need not produce the same orbit.
-/

#check DFPWolfe.V21.CenterManifold.centerProposition
#check DFPWolfe.V21.CenterManifold.centerManifoldAsymptotics
#check DFPWolfe.V21.CenterInterpolation.centerManifoldConditionalInterpolation
#check DFPWolfe.Latest.CenterEndpoints.quadraticEndpointRatioErrors
#check DFPWolfe.Latest.CenterEndpoints.sourceFamilyWithEndpointProperties
