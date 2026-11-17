# Latest manuscript: correctness and correspondence review

Reviewed manuscript: `20251117-DFP/arXiv.tex`, SHA256
`2a22ecf8e12959dd584a11732ba1836319eb16dd583059c283e4513b3dbbbdca`.
The current Lean entry is the general polar construction and its seven numbered
results. The older center-manifold route is retained separately and is not
presented as a result of this manuscript.

## Statement and proof checks

| Result | Checks against the manuscript |
| --- | --- |
| Theorem 1 | `main` quantifies over every admissible Wolfe pair, `ε, β ∈ (0,1)` and `n ≥ 2`. The same actual objective and iteration supply the `1 ± ε` Hessian bounds, global `β`-Hölder continuity, failure of every exponent in `(β,1]` on the initial level set, gradient limit one, unique minimizer and unit-circle cluster set. |
| Corollary 2 | The positive square-root change of variables is applied in the plane before extension. The resulting certificate has initial inverse Hessian exactly identity, positive gradient liminf and a nondegenerate ellipse in the embedded plane. |
| Theorem 3 | `IsOrbit.stepLengthPos` supplies positive step lengths. `IsWeakWolfe` includes `0 < c₁ < c₂ < 1`; local Lipschitz continuity is required only near the initial level set. Finite stopping is represented by stationary termination. |
| Lemma 4 | `existsContinuationEstimates` proves the actual recurrence's tube bounds, physical feasibility and odd-phase remainder, with constants chosen before the final starting index. |
| Lemma 5 | `existsSourceGeometry` combines the same radial trajectory with angular estimates and all-pair separation. Physical step bounds and the complete circle cluster set are conclusions. |
| Lemma 6 | `existsSourceObjectiveData` constructs the explicit cutoff objective from the proved geometry, endpoint jets, global regularity, convexity and initial-level-set Hölder obstruction. |
| Lemma 7 | `planarDegeneration` uses a general positive-definite secant iteration and weak Wolfe conditions. It is conditional on nonconvergence and adds neither a DFP update nor Lipschitz Hessian regularity. |

The general construction follows the manuscript's stable two-cycle, normalized
matrix recurrence, fast contraction, slow restoring tube, paired radial
products, separation estimate and cutoff interpolation. The source certificate
is not replaced by an older fixed-parameter construction.

## Same-witness checks

`PlanarConstruction.sourceData.actualGeometry` and `sourceIdentity` retain the
actual points, gradients, matrices and objective. `sequenceProperties` uses
this evidence directly. Its gradient expansions, phase oscillation,
nonsummable path length, Xu-scalar comparison, endpoint derivatives, curvature
limit, determinant and free-coefficient equivalents therefore concern the same
planar counterexample. `mainWithSequenceProperties` retains its literal
identity-block extension.

The new manuscript has no center-manifold section. The preceding revision's
independent spectral recurrence remains available in
`DFPWolfe.Latest.Proposition_8_CenterManifold`, `DFPWolfe.V21.CenterManifold`,
`CenterEndpoints` and `CenterDesign`; those modules are historical support and
are excluded from `DFPWolfe.Latest.Paper`.

## Reproduce the automated checks

From the repository root, run:

```sh
python3 -B -m unittest discover -s scripts -p 'test_*.py'
python3 -B scripts/audit_latest.py \
  --manuscript /volume/math/users/zcwang/m2f-sdk-distributed-workspace-v2/repos/DFP_wolfe_local/20251117-DFP/arXiv.tex
```

The supplied manuscript hash is checked before and after Lean validation. The
manifest contains 27 declarations for the current general-polar results and
same-orbit comparisons. The preserved historical modules remain checked
through their own exported roots.
The script scans all Lean sources and both roots for placeholders and custom
axioms, rejects retained audit commands in `ReasLib`, checks the combined root,
and compiles an ephemeral `#print axioms` probe. Only `propext`,
`Classical.choice` and `Quot.sound` are permitted.

The checked source tree passed the combined root and declaration audit with the
manuscript hash matched and source hashes unchanged. Numerical experiments,
finite-interpolant plots and MATLAB comparisons are outside this Lean proof
coverage.
