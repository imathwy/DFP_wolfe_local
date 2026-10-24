# Latest manuscript: general polar and independent center-manifold constructions

Import `DFPWolfe.Latest.Paper` for the latest `arXiv.tex` checked on
October 24, 2026. It has eight numbered results. Its counterexample covers
every `0 < η₁ < η₂ < 1`, every `β ∈ (0,1)`, every Hessian accuracy
`ε ∈ (0,1)`, and every dimension `n ≥ 2`.

The construction follows the paper's stable two-cycle, actual normalized
matrix recurrence, Lyapunov fast contraction and slow invariant tube,
paired tail-product radii, and explicit cutoff interpolation. The general
planar convergence and secant degeneration results reuse the unchanged
proofs from the earlier revision. The earlier counterexample constructions
remain available through the [original index](../README.md) and
[v21 index](../V21/README.md).

## Numbered correspondence

The proof links below jump directly to declaration lines on GitHub. Each
numbered navigation file records the source label and mathematical statement.

| Paper result | LaTeX label | Navigation | Proof declaration |
| --- | --- | --- | --- |
| Theorem 1 | `thm:main` | [Theorem 1](Theorem_1_StrongWolfeCounterexample.lean) | [main](Main.lean#L342) |
| Corollary 2 | `cor:identity-initialization` | [Corollary 2](Corollary_2_IdentityInitialization.lean) | [identityInitialization](Main.lean#L377) |
| Theorem 3 | `thm:planar-convergence` | [Theorem 3](Theorem_3_PlanarConvergence.lean) | [planarConvergenceCases](PlanarConvergence.lean#L25) |
| Lemma 4 | `lem:polar-continuation` | [Lemma 4](Lemma_4_PolarContinuation.lean) | [existsContinuationEstimates](../../ReasLib/Optimization/DFP/Polar/General/Continuation.lean#L1027) |
| Lemma 5 | `lem:polar-geometry` | [Lemma 5](Lemma_5_PolarGeometry.lean) | [existsSourceGeometry](../../ReasLib/Optimization/DFP/Polar/General/ActualGeometry.lean#L52) |
| Lemma 6 | `lem:polar-interpolation` | [Lemma 6](Lemma_6_PolarInterpolation.lean) | [existsSourceObjectiveData](../../ReasLib/Optimization/DFP/Polar/General/Objective.lean#L774) |
| Lemma 7 | `lem:planar-degeneration` | [Lemma 7](Lemma_7_PlanarSecantDegeneration.lean) | [planarDegeneration](SecantDegeneration.lean#L24) |
| Proposition 8 | `cm-center-proposition` | [Proposition 8](Proposition_8_CenterManifold.lean) | [centerProposition](../V21/CenterManifold.lean#L2068) |

Theorem 1 proves strong Wolfe at every step, gradient norms tending to one,
globally `β`-Hölder Hessians within `ε` of identity, the unique origin
minimizer, and the complete unit-circle accumulation set in an embedded
plane. Every higher exponent in `(β,1]` fails on the original initial level
set. No continuation, feasibility, separation or regularity assumption is
left to the caller.

Corollary 2 normalizes by the positive square root of the actual planar
initial matrix before extending dimension. The initial inverse Hessian is
exactly identity, the gradient norm has positive liminf, and the accumulation
set is a centered ellipse. Its
[quantitative entry](Main.lean#L397)
retains the precise planar Hessian bounds `λmin(H₀)/2` and
`3λmax(H₀)/2`, the lower bound `liminf ‖g̃ₖ‖ ≥ √λmin(H₀)`, and the
corresponding minimum and maximum with one after identity-block extension.

Theorem 3 allows arbitrary initial data and the full weak Wolfe range,
with finite stationary termination or convergence of both iterates and
gradients. Lemma 7 applies to general positive definite secant sequences;
it requires neither a DFP update nor a Lipschitz Hessian.

## Independent center-manifold analysis

[Proposition 8 and Section 6](Proposition_8_CenterManifold.lean) reuse the
actual spectral recurrence and C⁷ invariant graph in
[centerProposition](../V21/CenterManifold.lean#L2068), with derivative eigenvalues
`1`, `−1/9`, `0`, graph coefficients `198/5` and `8`, positive definite
iterates and inverse-cubic scale. The same section retains the center
cancellation coefficient `−116/5`, limiting-amplitude coefficient `13/3`,
positive gradient limit and complete limiting circle.

[CenterEndpoints](CenterEndpoints.lean) proves the translated quadratic
endpoint decrease ratios with uniform `O(εⱼ)` remainders, their exact limits
`2/3` and `5/6`, and endpoint Wolfe inequalities for
`0 < η₁ < 2/3` and `2/3 ≤ η₂ < 1`. These concern the same actual
center-manifold trajectory and require no support separation premise.
[Conditional interpolation](../V21/CenterInterpolation.lean) preserves
the source's pairwise-disjoint open balls and eventual `εⱼ²` support radii.
The general polar counterexample and this independent recurrence need not
produce the same trajectory.

| Section 6 refinement | Declaration |
| --- | --- |
| Control cancellation | [`centerControlCancellation`](CenterEndpoints.lean#L20) |
| Uniform endpoint ratio errors | [`quadraticEndpointRatioErrors`](CenterEndpoints.lean#L60) |
| Same-source endpoint Wolfe family | [`sourceFamilyWithEndpointProperties`](CenterEndpoints.lean#L299) |

## Comparisons on the same orbit

[The planar sequence entry](Sequences.lean#L48) retains the complete actual construction from
Theorem 1, including its objective, starting index, points, gradients,
accepted step lengths and inverse Hessians. Its source and canonical
sequence packages prove the manuscript's unnumbered comparisons:

| Source passage | Conclusions on the same actual Wolfe orbit |
| --- | --- |
| `sec:known-results`, gradient ratios | Even and odd ratios are `1 ∓ φ(γ*) τ^(1+β) + O(τ²)`, with a common positive remainder constant; eventual strict opposite phase signs and failure of both directions of eventual monotonicity. |
| `sec:known-results`, path length | Step norms are comparable to `τ`; their series is not summable and partial path lengths tend to infinity. |
| `sec:known-results`, Xu's scalar | Phase equivalents `δE ell τ²` and `δO τ²`; next-even/current-odd ratio tends to `δE ell/δO > 1`; failure of eventual nonincrease. |
| `sec:known-results`, accepted endpoints and iterates | Endpoint directional derivatives are eventually nonzero; the full cluster set is the circle and the iterates converge to no point. |
| After `lem:planar-degeneration` | Secant curvature tends to one; `det Hₖ` and the original `λₖ = κₖ₋₁ det Hₖ` are equivalent to `τ²/γ*`; `λₖ` has the order of consecutive physical step-norm products. |

[The all-dimensional sequence entry](Sequences.lean#L62) also retains the literal
identity-block extension of that same planar certificate. The principal
comparison proofs are in
[SequenceAsymptotics](../../ReasLib/Optimization/DFP/Polar/General/SequenceAsymptotics.lean)
and [GradientOscillation](../../ReasLib/Optimization/DFP/Polar/General/GradientOscillation.lean).

## Source and validation

The current `arXiv.tex` has SHA256
`3b1bf3c932b7ad3f2d24e6246a354224f52049015584a2902ed5db64d52f9101`.
Its source labels determine this index. The general polar proof was first
completed against `2.zip`; this revision restores Proposition 8 and the
independent center-manifold section.

```sh
lake lean DFPWolfe/Latest/Paper.lean
lake lean DFPWolfe/Latest/Sequences.lean
lake lean DFPWolfe.lean
```

These entries and all eight numbered navigation files pass Lean 4.32.0.
The general-polar audit of 26 principal declarations, the 114-declaration
sequence audit, and the 11-declaration gradient audit use only `propext`,
`Classical.choice`, and `Quot.sound`. The source contains no proof
placeholders or custom axioms; temporary audit commands are removed after
checking. Style warnings remain in the imported library.

The `arXiv.tex` update additionally checks the restored Proposition 8 entry,
the pure quadratic endpoint module and the combined paper/root entries.
Its fresh 19-declaration axiom audit includes the new endpoint proofs,
Proposition 8, conditional interpolation and the general-polar main results.
It uses the same three permitted logical foundations.
