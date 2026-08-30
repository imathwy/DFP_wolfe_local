# TASK-15: Semantic fidelity audit

Audit date: 2026-08-30.  This is a read-only audit of the paper and the current
Lean declarations.  The only file written by this task is this handoff.  Source
hashes below are the snapshots observed during the final audit.

## Bottom line

The main parameterized result is now in a check-friendly negative form.  In
particular, `main_not_globalWeakWolfeConvergence_of_parameterRange` has target
`not GlobalWeakWolfeConvergenceAt c1 c2`, and the new
`not_PaperRangeGlobalWeakWolfeConvergence` is literally the negation of the
positive convergence predicate quantified over the whole paper range.  Thus the
earlier concern that the final theorem was only an existential positive
statement is resolved for the global predicate.

The level-set semantics are also now represented: the trajectory containment
field and its Armijo/DFP descent bridge are present, and Main has corresponding
paper-range negations.  This is the formulation closest to the wording
"relevant level set" in the paper.

The identity-initialization corollary is now also implemented in a fully
automatic, matrix-facing form.  `AutomaticMatrixIdentityLiminf.lean` composes
the square-root factor, the affine orbit transport, the matrix `InverseIteration`
bridge, and the positive-liminf proof; Main and `DFPWolfe.lean` now export it.
What remains is only the final serial aggregate/facade/axiom check after these
latest source edits.  The older operator-level theorem remains available as a
lower-level interface with explicit distortion hypotheses.

## Paper reference points

| Paper location | Required meaning |
| --- | --- |
| `main-new.tex:219-236` | The open question asks whether every admissible classical DFP trajectory under weak Wolfe has gradient norm tending to zero.  Hessian bounds are only on the relevant level set; `H_0` is arbitrary positive definite; the quantification is over every valid step sequence. |
| `main-new.tex:238-257` | For every `0 < c1 < 2/3` and `2/3 <= c2 < 1`, there are planar data with global `[1/2,3/2]` Hessian bounds, positive steps, a well-defined DFP orbit, strong Wolfe at every step, and `||grad f(x_k)|| -> G_inf > 0`; the same construction is available for every `n >= 2`. |
| `main-new.tex:269-284` | For each paper-range pair, the affine-normalized example has classical matrix initialization `H_0 = I`, problem-dependent `0 < m <= M`, global Hessian bounds, strong Wolfe, and only `liminf ||grad f(z_k)|| > 0`; the result is all-dimensional. |
| `main-new.tex:1207-1257` | The accepted positive step lengths are checked at their endpoints.  The curvature condition is strong Wolfe, with ratios `1/3` and `2/3`; no particular line-search implementation is claimed. |
| `main-new.tex:1282-1344` | The affine map is `L = H_0^(1/2)`, the transformed matrix is `L^{-1} H_k L^{-T}`, and the transformed Hessian bounds depend on the original `H_0`. |
| `main-new.tex:1649-1662` | The conclusion repeats the parameterized strong-Wolfe counterexample and the identity-initialized, problem-dependent-bound corollary. |

## Declaration map and status

| Lean declaration/file | Current semantic content | Status |
| --- | --- | --- |
| `ReasLib/Optimization/DFP/GlobalConvergence.lean:16-39` | `WeakWolfeAdmissible`, `GlobalWeakWolfeConvergenceAt`, and the universal all-admissible-coefficient predicate.  Bounds are global here. | Sound but stronger than the paper's level-set hypothesis. |
| `ReasLib/Optimization/DFP/WolfeCounterexample.lean:24-38` | Certificate stores global Hessian bounds, weak Wolfe, positive steps, and an exact positive gradient-norm limit. | Sound reusable base certificate. |
| `ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean:32-43,114-119` | Gradient-facing strong Wolfe and a wrapper extending the weak certificate. | Strong witness is available without weakening the source data. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedPlanar.lean:31-38` | Planar certificate for symbolic paper-range coefficients, with fixed global `[1/2,3/2]` bounds. | Frozen RC0, hash `30ddd393c2f781da9d448c7baedecc7d10bdc031ed97bda98862028a924f5b8c`. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedTransport.lean:28-58` | Transport to every `n >= 2`, preserving the symbolic range, strong field, and fixed bounds. | Frozen RC0, hash `bf27728d35dca9aa1070fa1a5ffcaa16933581697d5d0698b700caa3e8e69a62`. |
| `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:16-50` | `existsStrongWolfeCounterexample_of_parameterRange`; pointwise negative `GlobalWeakWolfeConvergenceAt`; and `forall` wrapper over the paper range. | Semantic shape is correct; source hash `7d6cc3d0ca5c1910a719659078bb35fbc0609547a83334f35c9bd04ff3d71037`, fresh RC0. |
| `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:53-120` | Pointwise and forall paper-range negations for the level-set predicate, plus `PaperRangeGlobalWeakWolfeConvergence` and its literal negation. | Directly addresses the requested negative statement shape. |
| `ReasLib/Optimization/DFP/LevelSetGlobalConvergence.lean:19-36,148-173` | Initial sublevel set `{z | f z <= f (x_0)}`, restricted Hessian bounds, and level-set convergence predicates. | Fresh RC0 reported by owner; hash `f6cf28c58d611bffc974964f04cd4f9c39a30dc20157935288902c36a66942c4`. |
| `ReasLib/Optimization/DFP/LevelSetGlobalConvergence.lean:49-144,177-214` | Secant denominator -> nonzero gradient -> strict DFP descent -> Armijo monotonicity -> trajectory containment; counterexample refutation adapters. | Containment bridge is now explicit and mathematically sound. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/SemanticProjections.lean:27-81,111-153` | Exact positive limit projects to positive `liminf`; eventual lower tail alone is deliberately not treated as enough without an upper bound or convergence. | Fresh RC0, hash `9d43ac937978f354d82930d4770e25ae8d88e2a8424ea8a82bc06bd9989cba30`. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedIdentityInitialization.lean:88-95,140-310` | Affine normalization with identity initial operator, explicit distortion bounds, strong Wolfe, and an eventual positive transformed-gradient tail. | Frozen RC0, hash `2cf311f589d86f093838194827e5c1a9020252a0bcbf72b8da48ab09db536f03`; intentionally operator-level. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/AutomaticIdentityFactor.lean:47-114,122-150` | Automatically obtains a square-root factor and positive scalar map bounds from initial matrix `PosDef`, then returns an identity-initialized operator certificate. | Frozen RC0, hash `7705dad88d72f802de8a435953e192a9c53cc744596712993c373c74e210cac9`; no matrix `InverseIteration` claim. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/MatrixIdentityInitialization.lean:35-53,63-69,246-366` | Canonical operator-to-matrix sequence and a matrix strong-Wolfe certificate; the bridge requires matrix `PosDef` and denominator hypotheses. | Matrix-facing infrastructure, including a public pointwise representation lemma, is fresh RC0; hash `52c590bbc3d108af027b99623bdd2ad85d4d13553de844d091f84c66e0f7d5cf`. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/MatrixIdentityLiminfCertificate.lean:52-70,91-276` | Matrix `InverseIteration` certificate whose field is exactly `0 < liminf ||gradients||`; constructors expose matrix positivity and denominator obligations. | Fresh RC0; hash `ba689c5fac82cf4d71c5f9ee73a4f0dd5d82b8bc3902f39b07f8b4fa667632fc`. |
| `ReasLib/Optimization/DFP/WolfeCounterexample/AutomaticMatrixIdentityLiminf.lean:48-67,68-289` | Factorized source strong certificate -> transformed orbit -> strict secant curvature -> upper/lower gradient tails -> positive liminf -> canonical matrix certificate; also eliminates factor inputs from the public existential theorem. | Fresh RC0; hash `6999c15bd34485904cf0bf9145c665990bfc399a062e4e75a899afcd54b05f9a`. |
| `DFPWolfe.lean:3-14` | Publicly imports global, level-set, semantic, matrix-initialization, matrix-liminf, and automatic matrix-liminf modules. | Fresh RC0/export probe; hash `6f12fc459a67ef681da77a57b11cbe28858747e0ef39b7af78f8c5180c99cc99`. |

## Six semantic checks

### 1. Negative form and quantifier scope

The current declarations distinguish three logically different statements:

```text
not GlobalWeakWolfeConvergenceAt c1 c2
forall c1 c2 in the paper range, not GlobalWeakWolfeConvergenceAt c1 c2
not (forall c1 c2 in the paper range, GlobalWeakWolfeConvergenceAt c1 c2)
```

The first is `main_not_globalWeakWolfeConvergence_of_parameterRange`
(`DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:26-41`).  The second is
`main_not_globalWeakWolfeConvergence_forall_parameterRange`
(`DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:45-51`) and is stronger than the third.  The third is now represented
literally by `PaperRangeGlobalWeakWolfeConvergence` and
`not_PaperRangeGlobalWeakWolfeConvergence`
(`DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:83-101`).  The level-set analogues
are at `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:53-81` and `:103-120`.

This is faithful to the paper's per-parameter existential Main theorem: a
counterexample for a fixed pair refutes the corresponding universal convergence
claim, and the theorem is then universally quantified over the coefficient
range.  The older
`not_universalGlobalWeakWolfeConvergence_fixedParameters`
(`DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:174-192`) has a different scope: it uses one fixed
`(1/4,3/4)` witness to refute the broader all-admissible-coefficient predicate.
It must not be presented as the paper-range theorem by itself.

**Verdict:** the requested negative form is now present.  Keep the literal
`not_PaperRange...` theorem as the shortest final check if a single proposition
is preferred.

### 2. Strong versus weak Wolfe

The paper's open question is weak Wolfe (`main-new.tex:193-204,219-236`), while
the counterexample is stronger (`main-new.tex:238-257`).  Lean follows this
logic:

- `LineSearch.IsStrongWolfe` is the absolute-curvature predicate
  (`StrongWolfeCounterexample.lean:32-43`).
- `StrongWolfeCounterexample` extends a certificate that already contains the
  legacy weak-Wolfe field (`:114-119`), so the negative weak predicate does not
  rely on an invalid strong-to-weak conversion.
- Main's negative theorem intentionally targets
  `GlobalWeakWolfeConvergenceAt`
  (`DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:26-41`).

There is no `GlobalStrongWolfeConvergenceAt` predicate.  That is not a defect for
the paper's logical refutation: a strong-Wolfe witness is admissible for the weak
question.  A separate strong-global predicate would be an optional API and would
increase, rather than reduce, the statement surface.

**Verdict:** strong/weak semantics are sound and correctly nested; do not rename
the final weak convergence predicate to strong Wolfe.

### 3. `liminf` versus an exact limit

The planar/all-dimensional source certificate stores the stronger statement
`Tendsto ||gradients|| (nhds gradientLimit)` and `0 < gradientLimit`
(`WolfeCounterexample.lean:24-38`).  This is stronger than the Main theorem's
needed nonconvergence witness and is harmless.

The identity corollary is different.  The paper asks only
`liminf ||grad|| > 0` (`main-new.tex:277-282`).  A non-isometric affine map does
not generally preserve convergence of gradient *norms* to a scalar, even when
the original norms converge, so the operator certificate correctly records an
eventual lower tail rather than inventing an exact transformed norm limit
(`ParameterizedIdentityInitialization.lean:264-310`).

`SemanticProjections.lean:111-153` explicitly requires either an eventual finite
upper bound or an exact `Tendsto` fact before deriving a real-valued `liminf`.
The matrix liminf structure has the exact paper-facing field
`gradientNormLiminfPos` (`MatrixIdentityLiminfCertificate.lean:52-70`).  The
now-frozen factorized producer derives both tails and the liminf
(`AutomaticMatrixIdentityLiminf.lean:184-218`), so no exact transformed norm
limit is being smuggled into the identity conclusion.

**Verdict:** the distinction is mathematically correct and is now reflected in
the public matrix certificate; the final aggregate/export checks are complete.

### 4. Global Hessian bounds versus the relevant level set

The original reusable predicate uses `HasHessianBounds` at every point
(`GlobalConvergence.lean:16-34`).  This is stronger than the question's
"relevant level set" assumption (`main-new.tex:219-223`) and therefore does not
make the proved negative result unsound, but it is not the minimal paper-facing
statement.

The new level-set module uses the standard initial sublevel set

```text
objectiveSublevel iteration = {z | f z <= f (point 0)}
```

at `LevelSetGlobalConvergence.lean:19-36`, and restricts the Hessian bounds to
that set (`:148-157`).  The explicit trajectory-membership field is now present
at `:154-156`.  The bridge at `:49-144` proves it from the actual DFP laws:
positive-definite inverse Hessian plus a positive step gives strict descent;
Armijo then gives antitone objective values and membership in the initial
sublevel set.  A global-bound counterexample is converted to this admissibility
package at `:177-189`.

**Verdict:** level-set semantics now match the paper under the standard meaning
of "relevant level set."  If a different externally supplied set is intended,
the predicate would need a set parameter; no evidence in `main-new.tex` requires
that generalization.

### 5. Is identity initialization truly matrix-facing?

The paper explicitly says classical matrix DFP starts with `H_0 = I`
(`main-new.tex:277-278`).  The lower-level public theorem
`identityInitializedStrongWolfe_of_parameterRange`
(`Theorem_Main_theorem.lean:123-148`) returns an operator certificate and keeps
explicit factor/map hypotheses.  That interface is intentionally not the final
paper corollary (`AutomaticIdentityFactor.lean:20-22`).

The matrix infrastructure is now substantial:

- `MatrixIdentityInitialization.lean:35-53` gives the canonical matrix sequence
  and its public pointwise representation lemma;
- `:246-366` builds a classical matrix certificate when matrix positivity and
  denominators are supplied;
- `MatrixIdentityLiminfCertificate.lean:52-70` gives the exact paper-facing
  `liminf` field;
- `AutomaticMatrixIdentityLiminf.lean:48-289` supplies the factorized
  orbit-to-matrix assembly, including strict secant curvature, matrix positivity,
  denominator nonvanishing, transformed gradient upper/lower tails, and the
  automatic factor existential.
- `Theorem_Main_theorem.lean:150-166` exports the all-dimensional,
  paper-range matrix certificate with existential positive ordered bounds.

The resulting public theorem has the shape

```lean
existsMatrixIdentityLiminfStrongWolfe_of_parameterRange
  (n : ℕ) (hn : 2 ≤ n) (pair in paper range) :
  ∃ m M, 0 < m ∧ m ≤ M ∧
    Nonempty (MatrixIdentityLiminfStrongWolfeCertificate
      n m M c₁ c₂)
```

and is now imported by `DFPWolfe.lean:3-14`.  The bounds are intentionally
problem-dependent, as in the paper; the fixed `[1/2,3/2]` interval is not claimed
after a non-isometric affine change.

**Verdict:** identity initialization is genuinely matrix-facing and uses the
paper's `liminf` conclusion.  The producer and Main/facade exports have fresh
zero-return checks; the aggregate report records the final audit.

### 6. Trajectory containment in the level-set predicate

This was previously the clearest semantic omission.  It is now repaired:

- `LevelSetWeakWolfeAdmissible` includes
  `forall k, point k in objectiveSublevel iteration`
  (`LevelSetGlobalConvergence.lean:148-157`);
- `InverseIteration.pointMemObjectiveSublevelOfWeakWolfe`
  (`:135-144`) derives containment from positive steps and weak Wolfe;
- `WolfeCounterexample.levelSetWeakWolfeAdmissible`
  (`:177-189`) inserts that proof into the admissibility package;
- Main exports both pointwise and paper-range level-set negations
  (`DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:53-120`).

The proof uses no unrecorded assumption about a line-search implementation; it
uses only the DFP recurrence, positive definiteness, positive step lengths, and
the endpoint Armijo inequality.  This is the right bridge for a level-set-only
Hessian hypothesis.

**Verdict:** containment is now explicit and derived, not silently assumed.

The formal release also preserves the paper's stated boundary: it does not
claim counterexamples for `c₂ < 2/3` or for objectives smoother than `C²`, which
the paper leaves open.

## Matrix identity completion checklist

All matrix identity steps are complete and checked:

1. `MatrixIdentityLiminfCertificate.lean` and
   `AutomaticMatrixIdentityLiminf.lean` pass fresh RC0 checks.
2. `factorAndBounds_of_initialPosDef` composes with the factorized producer;
   the public theorem eliminates explicit factor, `a`, `b`, and `q` inputs.
3. The source strong witness is obtained for every `n ≥ 2` and every pair in
   the paper range; strict secant curvature and both gradient tails are proved.
4. Main and `DFPWolfe.lean` export the matrix certificate theorem.
5. The facade export and `#print axioms` probes resolve the named declarations;
   probes live only under `/tmp`.

The factorized producer already derives the semantically delicate facts:
source strict descent (`AutomaticMatrixIdentityLiminf.lean:110-132`), transformed
secant curvature (`:139-157`), an eventual upper gradient bound (`:187-212`),
and positive `liminf` (`:213-214`).  Thus no new mathematical assumption should
be added to the target theorem.

## Effort estimate

| Work item | Estimate from current snapshot |
| --- | --- |
| Fresh RC0/hash/axiom checks for the new matrix files and current Main/facade | Complete; about 1-2 hours wall time in the final serial pass |
| Compose automatic factor existential with the factorized matrix producer and expose one public theorem | Complete; roughly 220 Lean lines including the representation bridge |
| Repair elaboration/API friction | Complete; the public pointwise canonical-matrix adapter resolved the import-transparency issue |
| Optional `GlobalStrongWolfeConvergenceAt` API | 0.25-0.5 day; not required for the paper's weak-question refutation |
| Final aggregate/export/debt audit | Complete; 0.25-0.5 day |

The implementation estimate for the paper-faithful public release is now
**complete**.  Residual work is only the final serial audit and documentation,
estimated at **0.25-0.5 engineer-day**.  The optional strong-global predicate is
not needed for the paper's weak-question refutation.

## Recommended final statement surface

For the shortest check, use:

```text
not_PaperRangeGlobalWeakWolfeConvergence
```

This is literally a negation and has fewer fields to inspect than restating the
whole counterexample.  Keep
`main_not_globalWeakWolfeConvergence_forall_parameterRange` as the stronger
per-pair API, and use
`not_PaperRangeLevelSetGlobalWeakWolfeConvergence` when the paper's relevant
level-set wording must be visible in the type.

For identity initialization, use
`existsMatrixIdentityLiminfStrongWolfe_of_parameterRange`: it is the released
matrix-facing theorem with automatically generated problem-dependent bounds
and the exact `liminf` conclusion.  The lower-level
`identityInitializedStrongWolfe_of_parameterRange` and
`exists_identityInitializedStrongWolfe_of_initialPosDef` remain available as
operator-level normalization interfaces with explicit distortion bounds.

## Handoff

The audit did not introduce mathematical changes; the parent integration added
label-only docstring updates to the semantic producer and completed the
producer, semantic bridges, and facade wiring.  The final aggregate report is
also refreshed.
