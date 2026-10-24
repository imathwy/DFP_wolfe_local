module

public import ReasLib.Optimization.DFP.Polar.General.Continuation

/-!
# Lemma 4 — infinite continuation of the actual matrix recurrence

Source label: `lem:polar-continuation` in the manuscript supplied as `2.zip`.
The normalized trajectory has slow error `O(τ^(1-β))` and fast error
`O(τ^(1+β))`; the odd phase has the same transverse error order. Every
physical matrix is positive definite with positive off-diagonal entry,
radius factor and secant curvature. All constants precede the final choice
of a sufficiently large starting index.
-/

#check DFP.Polar.General.Continuation.existsContinuationEstimates
