# Final conclusion coverage report

> Superseded aggregate: this historical audit describes the fixed-only
> intermediate state. The current parameterized status, exact hashes, RC0
> checks, and final semantic/matrix conclusions are recorded in
> [`FINAL_AGGREGATE_CHECK_REPORT.md`](FINAL_AGGREGATE_CHECK_REPORT.md), audited
> 2026-08-30.

Audit snapshot: 2026-08-29. Lean source was read only for this report. Statuses
distinguish mathematical source declarations from build artifacts; an `.olean`
is not treated as evidence for a newer source file.

## Executive result

The smallest honest final conclusion already supported by checked declarations
is the following fixed-parameter statement:

> Classical inverse-form DFP is not globally convergent under the standard weak
> Wolfe conditions: at `(c1,c2) = (1/4,3/4)` there is, in every dimension
> `n >= 2`, a globally `C^2` objective with Hessian bounds `[1/2,3/2]`, positive
> accepted steps, and a well-defined DFP trajectory whose gradient norms tend to
> a positive limit.

The natural Lean-facing conclusion should therefore be a *negation* of a named
global-convergence predicate. This has a smaller statement surface than restating
the entire construction and matches the logical shape of the open question in
`main-new.tex:219-236`: the conjecture is universal, so one admissible trajectory
refutes it. `ReasLib/Optimization/DFP/GlobalConvergence.lean` now supplies that
generic predicate and the certificate-to-negation adapters, but the final
paper-facing witness theorem still has to be wired in TASK-06.

Exact paper fidelity is not complete. The current published Lean theorem fixes
the coefficients at `(1/4,3/4)` and stores only weak Wolfe; the paper's Main
theorem is parameterized by every `0 < c1 < 2/3`, `2/3 <= c2 < 1`, asserts strong
Wolfe, and has a separate identity-initialized corollary. The first-wave companion
modules for those three gaps now compile independently; their outputs still need
to be assembled into the paper-facing planar/all-dimensional theorem.

## Coverage matrix

| Paper claim | Paper location | Current Lean evidence | Status | Gap |
| --- | --- | --- | --- | --- |
| Universal weak-Wolfe global-convergence question | `main-new.tex:219-236` | `DFP.InverseIteration`, `DFP.WolfeCounterexample`; new `DFP.GlobalWeakWolfeConvergenceAt` and `DFP.UniversalGlobalWeakWolfeConvergence` in `ReasLib/Optimization/DFP/GlobalConvergence.lean:16-39` | partial | Predicate/adapters compile, but no paper-facing theorem yet instantiates the existing witness and exports the negation. |
| Fixed planar counterexample | `main-new.tex:238-254` specialized to `(1/4,3/4)` and weak Wolfe | `DFP.existsPlanarWeakWolfeCounterexample`, `Theorem_2_3_...lean:27-262` | complete at fixed weak constants | The declaration is weaker than the paper in coefficient range and Wolfe strength. |
| Parameterized Main theorem | `main-new.tex:238-257` | `ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean` (RC0, SHA `54e3ca6f...`) supplies range-specific Armijo/curvature adapters; `Theorem_2_3_...lean:27-36` remains fixed | partial | Build a new planar certificate that consumes the parameterized endpoint APIs and then expose its all-dimensional transport. |
| Strong-Wolfe endpoint verification | `main-new.tex:1207-1257` | `ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean` (RC0, SHA `94b2257e...`) defines the predicate, endpoint adapter, and orthogonal/isometry transports; existing paper assembly still uses weak Wolfe | partial | Wire the strong certificate into the new planar/all-dimensional theorem; no change to the old weak certificate is required. |
| Positive gradient limit and nonconvergence | `main-new.tex:1259-1280`, especially `1263-1269` | `slowCurveEndpointGradientNormTendsto`; assembled into `gradientNormTendsto` at `Theorem_2_3_...lean:217-261`; `WolfeCounterexample.gradientLimitPos` | complete for the fixed witness | Needs only the new logical negation wrapper for the concise final conclusion. |
| Every dimension `n >= 2` | `main-new.tex:255-256`, `1272-1280` | `DFP.existsWeakWolfeCounterexample`, `Theorem_2_4_...lean:17-46`, via orthogonal sum and isometric pullback | complete at fixed weak constants | Not re-exported by the facade; the new strong parameterized transport still needs integration. |
| Identity initialization | `main-new.tex:269-284`, proof `1282-1344` | `ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean` (RC0, SHA `5a6b522b...`) packages an operator-level certificate with `H 0 = 1`, bounds `(m*a,M*b)`, Wolfe transport, and a positive eventual gradient lower bound | partial | Decide how this operator certificate is presented in the paper-facing matrix theorem and add the final corollary/wrapper. |
| Limiting circle | `main-new.tex:840-901` | `DFP.TwoPhaseOrbit.limitCircle`; compact/closed wrappers; `slowCurveEndpointClusterSet_eq_limitCircle` is referenced by the paper wrapper | complete as infrastructure | Optional for the final nonconvergence statement and need not be rechecked in TASK-06. |
| Unbounded rotation/winding | `main-new.tex:151-154`, conclusion `1656-1658` | Paper wrappers `Lemma_4_8_Unbounded_frame_winding.lean` and `Lemma_4_8a_...`; canonical near-return/frame-angle modules | complete as infrastructure | Optional explanatory geometry, not a final theorem prerequisite. |
| Endpoint interpolation and global Hessian control | `main-new.tex:909-1198` | `contDiff_two_slowCurveRealizedObjective` and `slowCurveRealizedObjectiveHessianBounds`, `Proposition_5_12a_...lean:16-...`; exact orbit wrapper `Proposition_5_14_...` | complete for fixed construction | Parameterized assembly must choose a common small scale depending on `c1`. |
| Numerical and line-search implementation remarks | `main-new.tex:1440-1643` | No final Lean declaration required | optional | These are experiments/remarks and should not be included in the trusted theorem surface. |
| User-facing main/facade export | Paper title/abstract and `main-new.tex:1649-1662` | `Theorem_Main_theorem.lean:9-13` contains only two `#check`s and one `#print axioms`; `DFPWolfe.lean:3` public-imports only Theorem 2.3 | missing | TASK-06 must replace command-only wrapper content with named declarations and public-import the chosen final module(s), including Theorem 2.4/global negation. |

## Exact logical scope

The current witness uses fixed `(c1,c2) = (1/4,3/4)`. It can soundly refute:

1. `GlobalWeakWolfeConvergenceAt (1/4) (3/4)`, the fixed-coefficient universal
   convergence claim; and
2. `UniversalGlobalWeakWolfeConvergence`, because that proposition quantifies
   over *all* admissible coefficients and therefore includes `(1/4,3/4)`.

It does **not** prove the paper's stronger all-parameter existential theorem:
for every pair in the stated range, a counterexample exists. The distinction
must remain explicit in theorem names and docstrings.

The new generic negation file currently exposes:

- `DFP.WolfeCounterexample.weakWolfeAdmissible`;
- `DFP.not_tendsto_zero_of_pos_limit`;
- `DFP.not_globalWeakWolfeConvergenceAt_of_counterexample`; and
- `DFP.not_universalGlobalWeakWolfeConvergence_of_counterexample`.

Its target check returned RC0 on source SHA
`8fd4d4e38487eaf97a53ac3214f23e229d4cc06bbff6385bb9db30c42514620f`.
The remote check did not leave a local `.olean`, so this report records the RC,
not an artifact claim.

## Source and artifact snapshot

| Module | Source SHA / mtime | Artifact SHA / mtime | Assessment |
| --- | --- | --- | --- |
| Theorem 2.3 | `8ffbb46f...`, 2026-08-23 14:12:40 +0800 | `0bef8111...`, 2026-08-29 18:27:31 +0800 | artifact newer than source; fixed weak theorem available |
| Theorem 2.4 | `a9d53465...`, 2026-08-23 20:02:43 +0800 | `c7692949...`, 2026-08-29 18:28:12 +0800 | artifact newer than source; fixed weak all-dimension theorem available |
| Main wrapper | `d01b95e9...`, 2026-08-29 18:29:48 +0800 | `c6949cc4...`, 2026-08-23 21:41:49 +0800 | artifact stale and source has no named theorem |
| `DFPWolfe.lean` | `10fd1053...`, 2026-08-27 01:14:38 +0800 | no current top-level artifact located in this audit | facade not certified and does not expose all-dimensional/final negation theorem |
| Global convergence companion | `8fd4d4e3...`, 2026-08-29 19:07:22 +0800 | no local artifact from remote transport | target check RC0; integration pending |
| Parameterized Wolfe companion | `54e3ca6f...`, 2026-08-29 19:21:01 +0800 | target artifact present in the local cache after RC0 | frozen companion; not yet imported by the paper-facing theorem |
| Strong-Wolfe companion | `94b2257e...`, 2026-08-29 19:23:48 +0800 | target artifact status not used as source evidence | frozen companion; not yet imported by the paper-facing theorem |
| Identity-initialization companion | `5a6b522b...`, 2026-08-29 19:33:30 +0800 | target artifact present after RC0 | frozen operator-level corollary; matrix-facing wrapper remains |

Hashes are identifiers for the audited snapshots, not substitutes for TASK-07's
fresh aggregate checks.

## Integration ownership

To avoid overlapping writers, TASK-06 should own only:

- `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean`;
- `DFPWolfe.lean`.

It should import, not modify, the outputs owned by TASK-01 through TASK-04:

- `ReasLib/Optimization/DFP/GlobalConvergence.lean`;
- `ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean`;
- `ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean`;
- `ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean`.

TASK-07 owns no Lean source and performs the final checks/audits only after all
writers freeze their source hashes.

## Recommendations and remaining effort

### Smallest sound final theorem now

Add one named theorem in the Main wrapper that obtains the fixed witness from
`DFP.existsWeakWolfeCounterexample` and concludes
`not GlobalWeakWolfeConvergenceAt (1/4) (3/4)`. Optionally add the immediate
corollary `not UniversalGlobalWeakWolfeConvergence`. This is the clearest direct
formal answer to the global-convergence question and has the fewest statement
fields to inspect.

After TASK-01, this is chiefly integration work: approximately **0.5-1 working
day**, including facade and final axiom/debt checks.

### Additional work for exact paper fidelity

1. Consume the now-green parameterized `c1 < 2/3` Armijo and `c2 >= 2/3`
   endpoint APIs (TASK-02) in a new planar certificate.
2. Consume the now-green strong-Wolfe certificate and transport module (TASK-03)
   in that planar/all-dimensional assembly.
3. Present the now-green identity-initialized operator certificate (TASK-04) as
   the paper-facing matrix/coordinate-change corollary, retaining its explicit
   transformed bounds and positive gradient lower-tail.
4. Reassemble the planar theorem for arbitrary coefficients, transport it to all
   dimensions, add named Main/negative convergence declarations, and expose them
   through `DFPWolfe` (TASK-06).
5. Run frozen-hash target, aggregate, debt, and axiom audits (TASK-07).

Given the now-green first-wave companions, the remaining fixed-parameter release
is mainly Wave-2 wiring plus one aggregate check: **0.5-1 working day**. A
paper-faithful parameterized strong-Wolfe theorem still needs the planar assembly,
all-dimensional transport, identity-corollary presentation, and facade exports;
estimate **1.5-3 engineer-days** if those APIs fit directly, or **3-6 days** if
matrix/operator conversion and identity initialization require new bridges. The
concise fixed-parameter negative theorem remains the recommended first release
boundary even if exact paper fidelity takes longer.

## Current superseding status (2026-08-30)

The previously listed parameterized gaps have since been closed by TASK-08--11,
and the semantic level-set and matrix identity follow-up was closed by TASK-15.
`ParameterizedPlanar.lean`, `ParameterizedTransport.lean`, and
`ParameterizedIdentityInitialization.lean` all pass fresh RC0 checks; Main and
`DFPWolfe.lean` now export the symbolic-range strong certificate, the named
negative `GlobalWeakWolfeConvergenceAt` and level-set theorems, and the
matrix-facing identity `liminf` certificate. The lower-level identity result
remains operator-level and conditional on explicit factor/Loewner/gradient
bounds, while the public matrix theorem derives those data automatically. See
the superseding aggregate report for the authoritative hashes and proof audit.
