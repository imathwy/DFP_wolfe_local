# Latest manuscript: general polar construction

Import `DFPWolfe.Latest.Paper` for the manuscript in
`20251117-DFP/arXiv.tex`. Its SHA256 is
`2a22ecf8e12959dd584a11732ba1836319eb16dd583059c283e4513b3dbbbdca`.
The current entry has seven numbered results: Theorem 1, Corollary 2,
Theorem 3 and Lemmas 4–7. The preliminary polar direction, Wolfe, realization
and two-cycle statements are exposed by the supporting general modules.

The counterexample covers every `0 < η₁ < η₂ < 1`, every `β ∈ (0,1)`, every
`ε ∈ (0,1)` and every dimension `n ≥ 2`. The construction uses the actual
two-cycle, normalized matrix recurrence, fast contraction, slow tube, paired
tail-product radii and explicit cutoff interpolation. The planar convergence
and secant-degeneration proofs use the same hypotheses as the manuscript.

## Numbered correspondence

| Paper result | LaTeX label | Navigation | Main declaration |
| --- | --- | --- | --- |
| Theorem 1 | `thm:main` | [Theorem 1](Theorem_1_StrongWolfeCounterexample.lean) | [main](Main.lean#L342) |
| Corollary 2 | `cor:identity-initialization` | [Corollary 2](Corollary_2_IdentityInitialization.lean) | [identityInitialization](Main.lean#L377) |
| Theorem 3 | `thm:planar-convergence` | [Theorem 3](Theorem_3_PlanarConvergence.lean) | [planarConvergenceCases](PlanarConvergence.lean#L25) |
| Lemma 4 | `lem:polar-continuation` | [Lemma 4](Lemma_4_PolarContinuation.lean) | [existsContinuationEstimates](../../ReasLib/Optimization/DFP/Polar/General/Continuation.lean#L1027) |
| Lemma 5 | `lem:polar-geometry` | [Lemma 5](Lemma_5_PolarGeometry.lean) | [existsSourceGeometry](../../ReasLib/Optimization/DFP/Polar/General/ActualGeometry.lean#L52) |
| Lemma 6 | `lem:polar-interpolation` | [Lemma 6](Lemma_6_PolarInterpolation.lean) | [existsSourceObjectiveData](../../ReasLib/Optimization/DFP/Polar/General/Objective.lean#L774) |
| Lemma 7 | `lem:planar-degeneration` | [Lemma 7](Lemma_7_PlanarSecantDegeneration.lean) | [planarDegeneration](SecantDegeneration.lean#L24) |

Theorem 1 proves strong Wolfe at every step, gradient norms tending to one,
global `β`-Hölder regularity with the prescribed Hessian accuracy, the unique
origin minimizer and the complete unit-circle accumulation set. Every larger
Hölder exponent in `(β,1]` fails on the actual initial level set.

Corollary 2 applies the positive square root of the actual planar initial
matrix before the all-dimensional extension. It gives exact identity
initialization, positive gradient liminf and a nondegenerate centered ellipse.

Theorem 3 permits arbitrary initial data and the full weak-Wolfe range, with
finite stationary termination or convergence of the iterates and gradients.
Lemma 7 is the general planar secant-degeneration statement and does not add a
DFP or Lipschitz-Hessian assumption.

## Same-orbit comparisons

[Sequences](Sequences.lean) retains the actual planar certificate, objective,
starting index, points, gradients, accepted step lengths and inverse Hessians.
Its source and canonical packages formalize the manuscript's unnumbered
comparisons: opposite even/odd gradient-ratio corrections and failure of
eventual gradient monotonicity, nonsummable step lengths, Xu-scalar phase
comparison, nonzero accepted-endpoint derivatives, the full circle cluster set,
and the determinant/free-coefficient asymptotics used after Lemma 7.

The all-dimensional package retains the literal identity-block extension of
the same planar certificate. The principal comparison proofs are in
[SequenceAsymptotics](../../ReasLib/Optimization/DFP/Polar/General/SequenceAsymptotics.lean)
and [GradientOscillation](../../ReasLib/Optimization/DFP/Polar/General/GradientOscillation.lean).

## Preserved historical center-manifold route

The preceding manuscript's independent center-manifold analysis remains
available in [Proposition_8_CenterManifold.lean](Proposition_8_CenterManifold.lean),
`DFPWolfe.V21.CenterManifold`, `CenterEndpoints` and `CenterDesign`. It is not
imported by the current `Latest.Paper`, because the `20251117-DFP` manuscript
does not contain that section. The original center-manifold route and the
fixed-exponent polar route remain exported through `DFPWolfe.Paper` and
`DFPWolfe.V21.Paper`.

## Validation

Run from the repository root:

```sh
lake lean DFPWolfe/Latest/Paper.lean
lake lean DFPWolfe/Latest/Sequences.lean
lake lean DFPWolfe.lean
python3 -B scripts/audit_latest.py --manuscript /path/to/20251117-DFP/arXiv.tex
```

The audit manifest contains 27 declarations for the current general-polar
results and same-orbit comparisons. The preserved historical modules are
checked through their own exported roots.
All audited declarations use only `propext`, `Classical.choice` and
`Quot.sound`; source scans reject proof placeholders and custom axioms.
