# Latest manuscript: correctness and correspondence review

Reviewed manuscript: `arXiv.tex`, SHA256
`3b1bf3c932b7ad3f2d24e6246a354224f52049015584a2902ed5db64d52f9101`.
The proof sources reviewed here are those of commit
`4586350c4fa93ce7ff8fc9c344154ffc5229bbb7`. This review adds validation and
documentation; it does not change their mathematical statements or proofs.

## Statement and proof checks

| Result | Checks against the manuscript |
| --- | --- |
| Theorem 1 | `main` quantifies over every admissible Wolfe pair, `ε, β ∈ (0,1)` and `n ≥ 2`. `CounterexampleProperties.accuracy_bounds` supplies the requested `1 ± ε` bounds in addition to the certificate's fixed `1/2, 3/2` bounds. Global Hölder continuity, failure of every exponent in `(β,1]` on the actual initial level set, and gradient limit one concern the same objective and iteration. |
| Corollary 2 | The positive square-root change of variables is applied in the plane before extension. The certificate requires initial inverse Hessian exactly identity and positive gradient liminf. `EllipseObjectiveProperties` requires an injective image of the circle with two-dimensional range, so the ellipse is not allowed to degenerate. The quantitative entry retains the exact source eigenvalue bounds. |
| Theorem 3 | `IsOrbit.stepLengthPos` supplies positive step lengths. `IsWeakWolfe` includes `0 < c₁ < c₂ < 1`; those hypotheses are not missing from the public wrapper. Regularity is local Lipschitz continuity near the initial level set, not a global Lipschitz assumption. Finite stopping is represented by stationary continuation. |
| Lemma 4 | `existsContinuationEstimates` proves the actual recurrence's tube bounds, physical feasibility and odd-phase remainder. The constants and threshold precede every sufficiently large starting index. The public theorem does not assume an invariant tube or feasible trajectory. |
| Lemma 5 | `existsSourceGeometry` combines the same radial trajectory with angular estimates and near/far separation. The all-pair separation, physical step bounds and complete circle cluster set are conclusions. Constants remain uniform in the final starting index. |
| Lemma 6 | `existsSourceObjectiveData` constructs the explicit cutoff objective from proved geometry. The objective certificate includes the endpoint jets, global regularity and convexity, and initial-level-set Hölder obstruction. The complete actual geometry witness is retained for subsequent comparisons. |
| Lemma 7 | The wrapper uses a general positive definite secant iteration and weak Wolfe conditions; it adds neither the DFP update nor Lipschitz Hessian regularity. Degeneration is conditional on nonconvergence, as in the source. |
| Proposition 8 | The reused independent spectral recurrence has the source initialization, eigenvalues, C⁷ invariant graph, graph coefficients and inverse-cubic scale. Its existence proof is independent of the general-polar counterexample. |

The general construction follows the stable two-cycle, two-parameter normalized
map, fast contraction and slow restoring tube, paired radial products, geometric
separation and explicit interpolation. Existing linear-coordinate and
dimension-extension results transport a supplied certificate; they do not
substitute an older fixed-parameter counterexample for the source construction.

## Same-witness checks and Section 6

`PlanarConstruction.sourceData.actualGeometry` and `sourceIdentity` retain the
actual points, gradients, matrices and objective. `sequenceProperties` uses this
evidence directly. Its gradient expansions, phase oscillation, nonsummable path
length, Xu scalar comparisons, endpoint derivatives, curvature limit, determinant
and free-coefficient equivalents therefore concern the same planar counterexample.
`mainWithSequenceProperties` retains that planar package and its literal
identity-block extension. It does not separately restate every planar scalar
comparison as a formula on arbitrary-dimensional matrices.

For Section 6, `sourceFamilyWithEndpointProperties` selects one actual C⁷ source
graph and uses the same trajectory and center limit throughout. The uniform
quadratic endpoint error constant is chosen before the initial scale. The exact
ratio identity and the vanishing scale give limits `2/3` and `5/6`; shrinking the
initial-scale threshold gives endpoint Armijo and strong curvature without a
support-separation premise. The theorem permits all `c₂ ≥ 2/3`, which includes
the manuscript's `c₂ < 1` range.

The separate `centerManifoldConditionalInterpolation` retains pairwise-disjoint
open balls and eventual support radii comparable to `εⱼ²`. The Section 6
endpoint result is not an unconditional global interpolated counterexample.
The general-polar construction proves its own separation unconditionally.

No statement mismatch or proof gap was found in these checks. Existing imported
library style warnings remain; this is not a claim that every helper has had a
new line-by-line style review.

## Reproduce the automated checks

With the pinned Lean/mathlib dependencies available, run from the repository:

```sh
python3 -B -m unittest discover -s scripts -p 'test_*.py'
python3 -B scripts/audit_latest.py
```

Use `--lake /path/to/project/lake-wrapper` when a workspace supplies a check
wrapper. In remote-only mode the script uses `m2f-agent-lean-check` instead.
The script invokes target checks, never `lake build`.

The [audit manifest](../../scripts/latest_audit.json) contains 38 actual
declarations, including all eight numbered navigation targets, the main source
construction, quantitative normalization, same-orbit comparisons and Section 6
refinements. The script:

1. Scans all `DFPWolfe` and `ReasLib` Lean sources and both root entries for
   placeholders and custom axioms, ignoring nested comments and strings.
2. Rejects retained audit commands in `ReasLib` and navigation targets omitted
   from the manifest.
3. Checks `DFPWolfe.lean`, including the historical proof routes, and compiles an
   ephemeral `#print axioms` probe for the actual declarations.
4. Rejects missing or duplicate results and any dependency outside `propext`,
   `Classical.choice`, and `Quot.sound`.
5. Records source hashes and checks that the Lean files did not change during
   validation. Logs and JSON results stay under ignored `.work/`; the probe is
   removed even if a check fails.

The same checks run in CI. Six parser regression tests include missing output,
malformed output, unexpected declarations, duplicate output, and rejection of
`sorryAx` and project-defined axioms. Kernel acceptance and source correspondence
are different checks: the script verifies the former audit conditions; the
table above records the latter review. Numerical experiments, floating-point
plots and MATLAB performance comparisons are outside this Lean proof coverage.

The local rerun for this review passed: 538 Lean source files scanned, the
combined root checked, all 38 declaration audit results received, and only the
three permitted axioms found. All six regression tests passed. The source hashes
were unchanged through the check and the temporary audit source was removed.
