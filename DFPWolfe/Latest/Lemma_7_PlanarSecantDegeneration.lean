module

public import DFPWolfe.Latest.SecantDegeneration

/-!
# Lemma 7 — degeneration of general planar secant sequences

Source label: `lem:planar-degeneration` in the manuscript supplied as `2.zip`.
If a nonstationary weak-Wolfe planar sequence does not converge to its
strongly convex objective's minimizer, its free secant coefficient
`λₖ = κₖ₋₁ det Hₖ` is bounded by a constant times the product of consecutive
step norms and tends to zero. The matrices are bounded and their smallest
eigenvalues tend to zero. Only positive definiteness and the previous secant
equation are assumed; this general result reuses the earlier proof.
-/

#check DFPWolfe.Latest.planarDegeneration
