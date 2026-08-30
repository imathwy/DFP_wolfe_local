# DFP Wolfe parallel infrastructure roadmap

Status: live snapshot, 2026-08-22.

## Implementation snapshot

Proof-complete companion APIs as of 2026-08-22:

- `ReasLib/Analysis/Calculus/Deriv/GlobalInverse.lean`
- `ReasLib/Analysis/Calculus/Deriv/GlobalInverseBounds.lean`
- `ReasLib/Optimization/DFP/InverseUpdate/QuadraticForm.lean`
- `ReasLib/Optimization/DFP/InverseUpdate/Scaling.lean`
- `ReasLib/Optimization/DFP/AbstractSecantStep/Identities.lean`
- `ReasLib/Analysis/Asymptotics/ParabolicRecurrence.lean`
- `ReasLib/Topology/ContinuousMap/SmallLipschitzGraph/Transform.lean`
- `ReasLib/Topology/ContinuousMap/SmallLipschitzGraph/FixedPoint.lean`
- `ReasLib/Analysis/Calculus/ContDiff/SupportBounds.lean`
- `ReasLib/Analysis/Calculus/ContDiff/AffineBounds.lean`
- `ReasLib/Analysis/Calculus/ContDiff/ProductRule.lean`
- `ReasLib/Analysis/Calculus/ContDiff/CrossDerivative.lean`
- `ReasLib/LinearAlgebra/Matrix/PosDef/CauchySchwarz.lean`
- `ReasLib/Analysis/Calculus/FiniteTaylorJet/Ext.lean`
- `ReasLib/Analysis/Calculus/FiniteTaylorJet/OfFunctionOperations.lean`
- `ReasLib/Analysis/Calculus/FiniteTaylorJet/UniformRemainder/Transport.lean`
- `ReasLib/LinearAlgebra/EuclideanSpace/OrthogonalSum.lean`
- `ReasLib/Optimization/DFP/OrthogonalSum/Transport.lean`
- `ReasLib/Analysis/Calculus/Gradient/OrthogonalSum.lean`
- `ReasLib/Optimization/DFP/OrthogonalSum/Lift.lean`
- `ReasLib/Optimization/DFP/Orbit/Characterization.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/MixedMap/Basic.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion/LeadingTransverse/Basic.lean`
- `ReasLib/Analysis/Asymptotics/UniformRemainder/Diagonal.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion/LeadingTransverse/Asymptotic.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/GraphJet/Basic.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/Basic.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/StateJetAssembly.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/Combination.lean`
- `ReasLib/Analysis/Asymptotics/UniformRemainder/ContinuousLinearMap.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/RadiusJet/Specialization.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/Transverse.lean`
- `ReasLib/Analysis/Asymptotics/ContinuousMultilinearMap.lean`
- `ReasLib/Analysis/Calculus/FiniteTaylorJet/PeanoComparison.lean`
- `ReasLib/Analysis/Calculus/FiniteTaylorJet/FlatPath.lean`
- `ReasLib/Analysis/Calculus/FiniteTaylorJet/SplitComparison.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/Assembly.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/MixedFlatPath.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/HessianAssembly.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/BasisHessianAssembly.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/ScaleStationarity.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/ScaleStationaryAssembly.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/GermCongruence.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/FirstLegScaleExpansion.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/SecondLegScaleExpansion.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/PureScaleJets.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/AnalyticJetGerm.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/WeightedDefectJets.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/StateJetClosure.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/UniformZeroJet.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/StateJetDomainFactors.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/StateJetRemainderUniform.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/StateJetCommonDomain.lean`
- `ReasLib/Geometry/Euclidean/Angle/AbsToReal.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FirstLeg/Continuity.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/SecondLeg/Continuity.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/Continuity.lean`

All fifty-eight targets pass their isolated `lake lean` checks and contain no local proof
placeholders.  Package L's exact state-jet adapters intentionally inherit `sorryAx` only from
the three upstream scalar jet theorems; their conditional assembly cores are axiom-clean.
`GlobalInverseBounds.lean` now includes the arbitrary-order family-uniform inverse derivative
bound, and `ParabolicRecurrence.lean` includes the full generic asymptotic equivalence theorem.
They have deliberately not been imported into files owned by the main pipeline while those
files are locked. Package F's structural extensionality and core remainder-transport tranches
are complete; higher `IsUniformOn` integration remains deferred while the finite-jet API is
still being integrated.

The state-jet common-domain tranche is now proof-complete in companion modules:
`remainder_uniform_orderFive` gives one fifth-order constant and radius on every closed
coefficient ball, `domainFactors_uniform_lower_bound` gives one positive lower bound and
radius for all thirteen regularity factors, and
`stateJetsCommonDomain_via_uniform_remainder` combines them with a radius below `1 / 4`,
while `uniformRemainderOn_via_commonDomain` repackages the same estimate as an
`IsUniformRemainderOn` certificate.  All four declarations have axiom set
`[propext, Classical.choice, Quot.sound]`; none depends on `sorryAx`.  The original
`StateJet.stateJetsCommonDomain` and `StateJet.uniformRemainderOn` remain paper-facing
integration steps for their current owner and can be replaced by these companion proofs.

The observable branch-continuity tranche is also proof-complete in unlocked companions.
`Real.Angle.continuous_abs_toReal` removes the principal-representative branch cut by
identifying `|θ.toReal|` with `arccos (Angle.cos θ)`.  The FirstLeg and SecondLeg companions
export continuity at `(0, 2, 1)` for every output-metric entry, output-gradient entry,
canonical-frame entry, and the complete coordinate pair.  The Observables companion then
exports continuity of both endpoint oriented angles, both absolute-value branch margins, and
every relative-frame-product entry.  These declarations have axiom set
`[propext, Classical.choice, Quot.sound]` and contain no placeholders.

The locked `ObservableJet.branchFactors_continuousAt` can now be integrated by five finite
cases: project the two coordinate-pair theorems to their first coordinates, use
`DFP.TwoLeg.relativeFrameEntry_continuousAt 0 0`, and use the two endpoint-margin theorems.
At the latest observed locked snapshot its statement still ends in `sorry`; do not duplicate
the component expansions in that paper-facing file.

The recurrence module also includes checked `p = 1` and `p = 3` specializations; the latter is
the exponent used by the quartic DFP slow recurrence in `source/main.tex`.

No `FixedPointDefect` wrapper was created: local Mathlib 4.32 already provides the stronger
canonical `ContractingWith` fixed-point defect, iteration-error, and map-perturbation bounds.

This document records infrastructure gaps found while comparing the current Lean repository
with `source/main.tex`. It is an execution plan for work that can proceed beside the main
pipeline without sharing write ownership of live paper-facing files.

## Coordination contract

- The main pipeline owns the paper-facing files under
  `DFPWolfe/Required_Lean_mathlib_Infrastructure_for_the_DFP_Counterexample/`.
- I.13--I.16, I.26, and I.8a are active red zones. Side tasks must not edit them unless the
  orchestrator explicitly transfers ownership.
- Before every write, recheck the exact target's integration lock and mtime. Assign at most one
  writer per file; a missing lock is not by itself proof of exclusive ownership.
- Generic results go in a narrowly named `ReasLib` companion module. A paper-facing wrapper
  later imports that module; generic modules never import `DFPWolfe`.
- Validate only the owned target with `lake lean <target_file>`. Do not run `lake build`.
- The repository is currently almost entirely untracked and the main pipeline is live, so a
  clean `git diff` is not a reliable ownership signal. File ownership must be explicit.

## Immediate semantic correction

The I.14 statement `LocalCutoff.CenterProjection.antilipschitzWith` previously concluded

```lean
AntilipschitzWith lower (map χ ρ L N ζ)
```

and was corrected on 2026-08-20 to

```lean
AntilipschitzWith lower⁻¹ (map χ ρ L N ζ)
```

Mathlib defines `AntilipschitzWith K f` by
`dist x y ≤ K * dist (f x) (f y)`. A derivative lower bound
`lower ≤ deriv f x` therefore gives the reciprocal constant `lower⁻¹`.
The affine map `f x = 0.5 * x` is a counterexample to the old statement.

Downstream status:

- `inverse_lipschitzWith` already uses `lower⁻¹`.
- I.15's rate and slope assumptions already use `lower⁻¹`.
- I.16's bunching factors already use `lower⁻¹` or `lower⁻¹ ^ r`.
- There are currently no Lean call sites of the corrected theorem.
- `M2FQualityAudits/DataSorry_93cb873dbd694d3588ef018012a0d9ad.lean` is a stale generated
  snapshot containing the old type. Regenerate it through the quality-audit pipeline; do not
  hand-edit the generated copy.

Official proof ingredients:

- [one-dimensional mean value and monotonicity](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/Analysis/Calculus/Deriv/MeanValue.lean)
- [antilipschitz definitions and inverse estimates](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/Topology/MetricSpace/Antilipschitz.lean)
- [smoothness of inverse homeomorphisms](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/Analysis/Calculus/ContDiff/Operations.lean#L958-L973)

## Dependency fan-out

```text
InverseUpdate
  -> AbstractSecantStep
  -> Lemma 3.2a
  -> Propositions 3.6/3.7
  -> A1
  -> leg maps and complete state map

FiniteTaylorJet + UniformRemainder
  -> I.8a
  -> A5c/A5d/A5e and Lemma 3.14
  -> finite-smooth graph transform

SmallLipschitzGraph
  -> I.12 -> I.13 -> I.14 -> I.15 -> I.16
  -> C^ν invariant graph

ParabolicRecurrence
  -> I.19
  -> scalar slow dynamics
  -> orbit asymptotics

SmoothCutoff + affine bump bounds
  -> I.25 -> I.26 -> I.27 -> I.28 -> I.29 -> I.30
  -> global C² strongly convex realization
```

## Parallel package A: quantitative global inverse

Priority: P0. Conflict risk: low when implemented as a new module.

Proposed targets:

```text
ReasLib/Analysis/Calculus/Deriv/GlobalInverse.lean
ReasLib/Analysis/Calculus/Deriv/GlobalInverseBounds.lean
```

Statement deliverables:

- `strictMono_of_deriv_ge`
- `tendsto_atTop_of_deriv_ge`
- `tendsto_atBot_of_deriv_ge`
- `surjective_of_deriv_ge`
- `bijective_of_deriv_ge`
- `antilipschitzWith_of_deriv_ge`, with constant `lower⁻¹`
- `contDiff_invFun`
- `lipschitzWith_invFun`

The finite-order uniform bounds on higher inverse derivatives are a separate package. Do not
make the first package depend on Faà di Bruno.

`GlobalInverseBounds.lean` supplies explicit bounds through order three and a proof-complete
arbitrary-order family-uniform contract. A temporary import-level adapter was compiled against
I.14 for `bijective`, `inverse_contDiff`, `strictMono`, `lipschitzWith`,
`antilipschitzWith`, `inverse_lipschitzWith`, and `inverse_iteratedDeriv_le`. The last theorem
instantiates with the graph space as the parameter type and closes by
`simpa only [LocalCutoff.CenterProjection.inverse]`. The locked paper-facing file was not
modified; `eq_id_of_abs_ge` remains outside Package A.

Proof route:

1. Convert `ContDiff` to differentiability.
2. Apply `strictMono_of_deriv_pos`.
3. Use `mul_sub_le_image_sub_of_le_deriv` for the coercive two-point estimate.
4. Derive the two limits at infinity and apply `Continuous.surjective`.
5. Split the order of two real points and package the estimate using
   `AntilipschitzWith.of_le_mul_dist`.
6. Use `AntilipschitzWith.to_rightInverse` for the inverse Lipschitz theorem.
7. For inverse smoothness, construct the order isomorphism/homeomorphism and apply
   `Homeomorph.contDiff_symm_deriv`.

Acceptance:

- The target file compiles independently.
- The antilipschitz constant is syntactically and mathematically `lower⁻¹`.
- A small affine-map probe checks the constant convention.
- The paper-facing I.14 file can import the module without a reverse import.
- At proof stage, an ephemeral `#print axioms` audit shows no `sorryAx`.

## Parallel package B: inverse-form DFP identities

Priority: P0. Conflict risk: low in new companion modules.

Proposed targets:

```text
ReasLib/Optimization/DFP/InverseUpdate/QuadraticForm.lean
ReasLib/Optimization/DFP/InverseUpdate/Scaling.lean
ReasLib/Optimization/DFP/AbstractSecantStep/Identities.lean
```

Statement deliverables:

- `inverseDFPUpdate_apply`
- `inverseDFPUpdate_mulVec_secant`
- `inverseDFPUpdate_isHermitian`
- `inverseDFPUpdate_smul_pair`
- positive denominator lemmas
- `Matrix.PosDef.inverseDFPUpdate`
- `preconditionedGradient_ne_zero`
- positivity of the gradient and preconditioned energies
- `stepLength_pos`
- `predictedDecrease_eq_stepLength_mul_gradientEnergy`
- `secantCurvature_eq_stepLength_sq_mul_preconditionedEnergy`
- `secantCurvature_eq_tau_mul_predictedDecrease`

Proof route for positive definiteness:

1. Rewrite the downdate quadratic form as the squared norm of an
   `H`-orthogonal projection residual.
2. Obtain positive semidefiniteness from a congruence or a norm-square identity.
3. Treat `s sᵀ / (sᵀ y)` as a positive rank-one term.
4. Prove the two nonnegative terms cannot vanish simultaneously for a nonzero vector.
5. Finish with `Matrix.PosDef.of_dotProduct_mulVec_pos`.

Use the official, pinned
[Mathlib matrix positive-definite API](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/LinearAlgebra/Matrix/PosDef.lean).
No proof-complete Lean 4 DFP/BFGS implementation was found on GitHub.

Acceptance:

- Finite-dimensional tests on `Fin 1` and `Fin 2`.
- The secant equation simplifies to the expected vector equality.
- Scaling both secant vectors leaves the update unchanged under nonzero scale.
- The positive-definiteness theorem has no extra assumptions not present in I.2.

## Parallel package C: parabolic recurrence

Priority: P1. Conflict risk: very low.

Proposed target:

```text
ReasLib/Analysis/Asymptotics/ParabolicRecurrence.lean
```

Lemma chain:

1. Normalize the recurrence error.
2. Prove `ε (n + 1) / ε n -> 1`.
3. Prove the reciprocal-power forward difference tends to `a * p`.
4. Apply a generic forward-difference-to-linear-growth lemma.
5. Convert reciprocal-power growth back to the final `IsEquivalent`.

Primary reuse:

- [`stolz_cesaro_infty_case_1`](https://github.com/michelsol/more-math/blob/0786fa7475e01de69f6b436aa8a4844742222fdb/Other/stolz-cesaro.lean)
  is proof-complete, imports only Mathlib, and is Apache-2.0. It was written for Lean 4.15,
  so port the theorem into the local API rather than adding the whole repository as a dependency.
- [Erdos1014OQ03](https://github.com/rjwalters/lean-genius/blob/f9c62750e76180f15c7bd6c5759be320d7feffdc/proofs/Proofs/Erdos1014OQ03.lean)
  is a proof-complete Cesàro/telescoping template on Lean 4.31. The repository has no root
  license at the pinned commit, so use the proof architecture only; do not copy code.

Acceptance:

- The generic Stolz/Cesàro lemma is independent of the DFP namespace.
- Test the `p = 1` specialization.
- Expose the `p = 3` specialization used by the quartic DFP slow recurrence.
- I.19 becomes a short application of the generic module.
- Preserve attribution if Apache-licensed code is materially adapted.

## Parallel package D: graph-transform support

Priority: P1. Conflict risk: low in a new module; high inside live I.15.

Completed targets:

```text
ReasLib/Topology/ContinuousMap/SmallLipschitzGraph/Transform.lean
ReasLib/Topology/ContinuousMap/SmallLipschitzGraph/FixedPoint.lean
```

Core statement:

```lean
theorem dist_rightInverse_rightInverse_le
    (hf : AntilipschitzWith K f)
    (hfi : Function.RightInverse fi f)
    (hgi : Function.RightInverse gi g)
    (hfg : ∀ x, dist (f x) (g x) ≤ C) :
    dist (fi y) (gi y) ≤ K * C
```

Also add subtype bridges for point evaluation and the sup metric:

- `dist (ζ u) (η u) ≤ dist ζ η`
- `dist ζ η ≤ C ↔ ∀ u, dist (ζ u) (η u) ≤ C`, with the needed nonempty hypothesis
- use Mathlib's canonical `ContractingWith.dist_le_of_fixedPoint` and
  `ContractingWith.dist_fixedPoint_le` for defect-distance bounds
- use `ContractingWith.aposteriori_dist_iterate_fixedPoint_le`,
  `ContractingWith.apriori_dist_iterate_fixedPoint_le`, and
  `ContractingWith.fixedPoint_lipschitz_in_map`; do not reimplement these canonical estimates

The completed fixed-point companion supplies only the missing graph-specific bridge. A
pointwise defect bound gives distance to the unique fixed-point graph; pointwise closeness of
two uniformly contracting transforms gives the exact `C / (1 - K)` fixed-point bound; and a
parameter family that is pointwise `L`-Lipschitz has a fixed-point graph map that is
`L / (1 - K)`-Lipschitz. Each result first upgrades a pointwise estimate to the inherited sup
metric and then calls Mathlib's canonical contraction theorem.

External reuse:

- [CRNT GraphTransform](https://github.com/marpaia/crnt-lean/blob/99137993e729c8add247388718a22a0e0f393dab/CRNT/Dynamics/GraphTransform.lean)
  is proof-complete, MIT-licensed, and on Lean 4.31.
- Reuse its `GraphTransformData` packaging, fixed-point uniqueness, and defect-distance
  organization only after the local contraction estimate is proved.
- Do not expect it to prove reparametrization inverse bounds, map-to-self, slope/radius
  preservation, the local contraction rate, or fixed-point equivalence with flow invariance.
  Its `op_dist_le` field assumes precisely the hard estimate needed by I.15.

Alternative architecture:

- The Apache-2.0 Lean directory of
  [civic-alignment-program](https://github.com/dhofheinz/civic-alignment-program/tree/852066f06822b78e3ece6307ffd873e3ed085b31/lean)
  contains proof-complete Nemytskii substitution, Green-operator, and planar
  Hadamard--Perron developments on Lean 4.33-rc1.
- Use this only as an architecture reference if the direct graph transform stalls. Its
  hyperbolic assumptions do not cover the DFP center eigenvalue `1`.

Acceptance completed:

- The support module imports only Mathlib and stable ReasLib modules.
- Pointwise estimates lift to `ContractingWith` without re-proving bounded-function metric facts.
- Both completed targets pass isolated `lake lean` with zero output.
- A consumer derives the pointwise parameter-Lipschitz estimate at an arbitrary graph argument.
- All three fixed-point theorems have only `propext`, `Classical.choice`, and `Quot.sound`
  in their axioms audit; no `sorryAx`.
- No edit is made to I.15 until the main pipeline transfers ownership.

## Parallel package E: support and affine-bump bounds

Priority: P1. Conflict risk: low in a generic module.

Proposed targets:

```text
ReasLib/Analysis/Calculus/ContDiff/SupportBounds.lean
ReasLib/Analysis/Calculus/ContDiff/AffineBounds.lean
ReasLib/Analysis/Calculus/ContDiff/ProductRule.lean
```

Statement deliverables:

- iterated derivatives vanish outside `tsupport`
- support monotonicity for first and iterated derivatives
- compact support implies a global bound on each fixed iterated derivative
- a bridge from a bound on `tsupport f` to a global bound
- reusable affine reparametrization/scaling bounds for first and second derivatives
- the second Fréchet derivative's four-term pointwise Leibniz formula

Primary reuse:

- [OSReconstruction SmoothCutoff](https://github.com/xiyin137/OSreconstruction/blob/135ed13df64ab2ba777475358e8d66ee983c291b/OSReconstruction/GeneralResults/SmoothCutoff.lean)
  is proof-complete, Apache-2.0, and on Lean 4.29.
- Selectively port the compact-support and bounded-iterated-derivative argument. Do not add
  OSReconstruction as a package dependency.
- Prefer current Mathlib `ContDiffBump` lemmas whenever they already close the goal.

Acceptance:

- Plateau, support inclusion, and compact-support statements are independent.
- Scaling exponents are explicit and checked for derivative orders one and two.
- Bounds are global, not only conditional on membership in the bump's support.
- Existing `ShrinkingSupportFinsum` and `ContDiff/ZeroExtension` are reused, not duplicated.

## Parallel package F: finite Taylor jets

Priority: P2 until the jet API stabilizes. Conflict risk: medium.

Proposed targets:

```text
ReasLib/Analysis/Calculus/FiniteTaylorJet/Ext.lean
ReasLib/Analysis/Calculus/FiniteTaylorJet/UniformRemainder/Transport.lean
```

Current ownership snapshot: the I.8a pipeline intent still owns write access to
`FiniteTaylorJet/Operations.lean` and `FiniteTaylorJet/Uniform.lean`. Do not edit those
owners or extend the companion API into `IsUniformOn` until that write set is released and
the promoted public API has passed final validation.

The independent `Ext.lean` tranche was completed without touching that write set: it imports
only the stable base `FiniteTaylorJet` module and provides coefficientwise extensionality,
an equality iff for coefficients, an iff between one-variable `ofFunction` jet equality and
equality of the corresponding `iteratedDeriv` values, and the zero-function-jet criterion.
Its isolated target and an order-four `ε ^ 5` zero-jet consumer both compile. An axioms audit
shows only `propext`, `Classical.choice`, and `Quot.sound`, with no `sorryAx`.

The general extensionality statement is intentionally phrased using the public `coeff`
projection: `scalarCoeff` is opaque across this module boundary. For derivative-constructed
jets, the public `scalarCoeff_ofFunction` theorem still gives the sharper one-variable
`iteratedDeriv` criterion.

The independent `UniformRemainder/Transport.lean` tranche is also complete. It provides
continuous-linear postcomposition at the coefficient, evaluation, and remainder levels;
product-jet evaluation and remainder identities; and `mono`, `congr`, continuous-linear
postcomposition, and product transport for `FiniteTaylorJet.IsUniformRemainderOn`. Its
isolated target compiles, and all nine theorem-level declarations have the same clean axioms
audit with no `sorryAx`. The two warnings replayed during validation are pre-existing warnings
from `FiniteTaylorJet/UniformRemainder.lean`, not from the new companion.

First isolate the low-risk API:

- coefficientwise extensionality
- `ofFunction` coefficient formula
- zero jet iff the relevant derivatives vanish
- `congr`, `subset`, continuous-linear-map, and product transport

Keep the compact-parameter uniform Peano theorem as a separate hard task.

External templates:

- [RNCTaylorPeano](https://github.com/kaplan196883/QIQT-H/blob/d42633d22e6ac98d222b71aeadcbd8a93afa9d0e/lean/mathlib/QIQTH/RNCTaylorPeano.lean)
- [GeodesicTaylorCompact](https://github.com/kaplan196883/QIQT-H/blob/d42633d22e6ac98d222b71aeadcbd8a93afa9d0e/lean/mathlib/QIQTH/GeodesicTaylorCompact.lean)

Both proof bodies are complete at the pinned commit and use Lean 4.30. No explicit license was
found for the relevant tree, so only reproduce the mathematical/proof architecture:

```text
continuous iterated derivative
  -> bounded on compact parameter set
  -> derivative Lipschitz estimate
  -> uniform Taylor remainder
```

Do not copy source text without obtaining license clearance.

Acceptance:

- The easy structural API compiles before work begins on the uniform remainder.
- Polynomial and singleton-compact probes cover the degenerate cases.
- Companion files use only stable public jet declarations and do not edit I.8a.

## Parallel package G: Euclidean orthogonal sums for I.31

Priority: P1. Conflict risk: low in the generic companion, high in the locked DFP wrapper.

Completed targets:

```text
ReasLib/LinearAlgebra/EuclideanSpace/OrthogonalSum.lean
ReasLib/Optimization/DFP/OrthogonalSum/Transport.lean
ReasLib/Analysis/Calculus/Gradient/OrthogonalSum.lean
ReasLib/Optimization/DFP/OrthogonalSum/Lift.lean
ReasLib/Optimization/DFP/Orbit/Characterization.lean
```

The proof-complete generic layer now provides the canonical left continuous-linear embedding,
its two coordinate formulas, preservation of the real inner product, identity-block matrix
extension, all four block-entry formulas, matrix action on an embedded vector, the exact
finite-support quadratic-form splitting formula, and preservation/reflection of
`Matrix.PosDef`. The positive-definiteness equivalence has the same generality as the locked
I.31 statement: it assumes only `[DecidableEq κ]` and does not require either index type to be
finite.

The forward positive-definiteness proof decomposes an arbitrary `ι ⊕ κ →₀ ℝ` vector with
`Finsupp.sumFinsuppEquivProdFinsupp`. Its quadratic form is the `H` quadratic form plus a sum
of squares. If the left component is nonzero, strict positivity comes from `H.PosDef`; if it
vanishes, nonzeroness of the full vector forces a nonzero right component. Reflection uses
`Matrix.PosDef.submatrix` on `Sum.inl`.

The DFP transport companion uses only public module-boundary APIs. It proves transport of
`steps`, `gradientChanges`, and `directions`; dot-product and left-vector-multiplication
identities; and identity-block preservation by `Matrix.inverseDFPUpdate`. The update theorem
is denominator-total, matching Lean's zero-safe inverse definition, so it needs no curvature
or nonvanishing hypothesis.

The gradient companion defines the two continuous-linear coordinate projections and the
quadratic orthogonal-sum objective. It proves the left/right projection identities, dual and
inner-product transport, restriction of the objective to the left summand, transport of a
certified gradient, and the resulting gradient formula. The lift companion adds the reverse
differentiability implication at embedded points, transports a complete `DFP.IsOrbit`, and
proves that the weak Wolfe conditions are equivalent before and after embedding.
The orbit-characterization companion separately packages the four structure fields as a
conjunction, covering the sole proof hole in the I.31-owned `Orbit.lean`.

Drop-in adapters were compiled in an ephemeral consumer against the definitions in the locked
`ReasLib/Optimization/DFP/OrthogonalSum.lean`:

| Locked I.31 declaration | Reusable proof/API |
| --- | --- |
| `DFP.IsOrbit.iff` | `DFP.IsOrbit.components_iff` |
| `embed_apply_inl` | `EuclideanSpace.OrthogonalSum.inl_apply_inl` |
| `embed_apply_inr` | `EuclideanSpace.OrthogonalSum.inl_apply_inr` |
| `inner_embed` | `EuclideanSpace.OrthogonalSum.inner_inl` |
| `matrix_mulVec_embed` | `EuclideanSpace.OrthogonalSum.extendMatrix_mulVec_inl` |
| `matrix_posDef_iff` | `EuclideanSpace.OrthogonalSum.extendMatrix_posDef_iff` |
| `steps_embed` | `DFP.OrthogonalSum.Transport.steps_inl` |
| `gradientChanges_embed` | `DFP.OrthogonalSum.Transport.gradientChanges_inl` |
| `directions_embed` | `DFP.OrthogonalSum.Transport.directions_inl` |
| `inverseDFPUpdate_matrix` | `DFP.OrthogonalSum.Transport.inverseDFPUpdate_extendMatrix_inl` |
| `objective_embed` | `EuclideanSpace.OrthogonalSum.Gradient.objective_inl` |
| `hasGradientAt_objective_embed` | `EuclideanSpace.OrthogonalSum.Gradient.hasGradientAt_objective_inl` |
| `gradient_objective_embed` | `EuclideanSpace.OrthogonalSum.Gradient.gradient_objective_inl` |
| `DFP.IsOrbit.orthogonalSum` | `DFP.OrthogonalSum.Lift.isOrbit` |
| `LineSearch.IsWeakWolfe.orthogonalSum_iff` | `DFP.OrthogonalSum.Lift.weakWolfe_iff` |

These adapters work by definitional equality: `DFP.OrthogonalSum.embed` and
`DFP.OrthogonalSum.matrix` have the same bodies as the generic `inl` and `extendMatrix`, while
the locked objective has the same body as the gradient companion's `objective`. No edit was
made to either locked I.31 target. All fourteen holes in `OrthogonalSum.lean`, plus the sole
hole in `Orbit.lean`, now have checked direct adapters, so their owner can replace each
`sorry` without reopening the mathematical proofs.

Acceptance completed:

- isolated `lake lean` on all five completed targets: exit 0; the generic, transport, and
  gradient targets have zero output, while the two Orbit consumers only replay the pre-existing
  `Orbit.lean:45` `sorry` warning
- one comprehensive ephemeral consumer checks direct adapters for all fourteen locked I.31
  orthogonal-sum declarations, and a second checks the locked orbit characterization: compile
- axioms audits for the generic/transport/gradient/lift/orbit theorem sets (6/6/7/3/1): only
  `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`
- no external proof text was copied; the implementation uses local Mathlib v4.32 APIs

## Parallel package H: mixed two-leg basic interfaces

Priority: P1. Conflict risk: low in new companions; high in the locked mixed-map owners.

Completed targets:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/MixedMap/Basic.lean
ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion/LeadingTransverse/Basic.lean
```

The first companion proves the componentwise parameter-set membership formula, the explicit
canonical input formula, and the removable zero-radius value of the mixed map. The second
proves both definitional formulas for the weighted transverse increment and affine leading
map, computes the affine map's exact Fréchet derivative through a continuous-linear affine
decomposition, and verifies the fixed coefficient pair `(198 / 5, 8)`.

Direct adapters were compiled for seven locked declarations:

| Locked declaration | Reusable proof/API |
| --- | --- |
| `mem_parameterSet` | `DFP.TwoLeg.Mixed.mem_parameterSet_iff` |
| `input_apply` | `DFP.TwoLeg.Mixed.input_eq` |
| `map_zero` | `DFP.TwoLeg.Mixed.map_base` |
| `transverseIncrement_apply` | `DFP.TwoLeg.Mixed.transverseIncrement_eq` |
| `leadingTransverse_apply` | `DFP.TwoLeg.Mixed.leadingTransverse_eq` |
| `leadingTransverse_fderiv_apply` | `DFP.TwoLeg.Mixed.leadingTransverse_fderiv` |
| `leadingTransverse_fixedCoefficient` | `DFP.TwoLeg.Mixed.leadingTransverse_fixed` |

The statement `map_fixedScale` remains with its owner.  The algebraic and asymptotic
bookkeeping for `transverseIncrement_asymptotic` is now isolated in Package I; its only
remaining analytic inputs are the existing `shapeExpansion` and `scaleExpansion` certificates.
No theorem in these basic companions invokes those certificates or any other declaration
containing `sorry`.

Acceptance completed:

- isolated `lake lean` on both companions: exit 0; output only replays warnings from imported
  locked files
- all seven original-signature adapters compile
- all seven new theorems have only `propext`, `Classical.choice`, and `Quot.sound` in their
  axioms audits; no `sorryAx`
- no edit was made to `MixedMap.lean`, `LeadingTransverse.lean`, or the live first-leg target

## Parallel package I: parabolic diagonal remainder and transverse asymptotics

Priority: P1. Conflict risk: low in new companions; high in the locked expansion owners.

Completed targets:

```text
ReasLib/Analysis/Asymptotics/UniformRemainder/Diagonal.lean
ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion/LeadingTransverse/Asymptotic.lean
```

`UniformRemainder/Diagonal.lean` proves that a uniform order-two remainder, restricted to
`r = ε ^ 2` and normalized by `ε ^ 3`, is `o(1)` on the deleted neighborhood of zero.  The
proof works for an arbitrary real normed space and for an eventually admissible parameter
path, so it can be reused by other parabolic blow-up arguments.

`LeadingTransverse/Asymptotic.lean` defines the exact shape and scale remainders and proves:

- the pointwise normalized-error identity away from `ε = 0`;
- eventual membership of `(ε, P, J)` in `parameterSet β B` when `β > 0` and the fixed pair is
  in the coefficient ball;
- `transverseIncrement_asymptotic_of_uniformRemainders`, which combines the two scalar
  diagonal estimates with `IsLittleO.prod_left` and rewrites them to the exact transverse
  expression.

An ephemeral original-signature adapter compiles by choosing `β = 1 / 8` and
`B = dist (P, J) 0 + 1`, then supplying `shapeExpansion` and `scaleExpansion`.  Consequently,
the locked `transverseIncrement_asymptotic` hole no longer contains independent algebra,
filter, or product-norm work: it is reduced exactly to those two analytic expansion theorems.
The adapter was not added as a production theorem because those two current inputs still
contain `sorry`.

Acceptance completed:

- isolated `lake lean` on both new targets: exit 0
- the ephemeral exact-signature adapter: compile
- axioms audits for the generic diagonal theorem and all three new asymptotic theorems: only
  `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`
- source scans find no `sorry`, `admit`, or `axiom` in either new file and no `.rej` under
  `ReasLib`
- no edit was made to `MixedExpansion.lean`, `LeadingTransverse.lean`, or the live first-leg
  target

## Parallel package J: graph-jet and joint-state-jet interfaces

Priority: P2. Conflict risk: low in new companions; high in the original jet owners.

Completed targets:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/GraphJet/Basic.lean
ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/Basic.lean
```

The graph-jet companion exposes the general polynomial graph path and the fixed slow-graph
path with coefficients `(198 / 5, 8, -9 / 5, 0)`.  The proofs use only definitional unfolding
and normalization of the negative quartic coefficient.

The state-jet companion exposes the exact three-coordinate residual and the ordered vector of
thirteen common-domain factors by definitional equality.  It also supplies
`uniformRemainderOn_of_commonDomain`, which projects the residual bound from a common-domain
certificate and explicitly converts the natural fifth power to `Real.rpow` exponent `5`.

This last bridge makes the original `StateJet.uniformRemainderOn` a direct consequence of
`stateJetsCommonDomain`; an ephemeral original-signature adapter compiles.  Thus that hole has
no remaining independent compactness or asymptotic work once the common-domain theorem lands.

Acceptance completed:

- isolated `lake lean` on both companions: exit 0; output only replays upstream placeholder
  warnings
- both original GraphJet signatures compile directly against the clean replacements
- `remainder_eq` and `domainFactors_eq` have the exact original definitional interfaces
- an original-signature `uniformRemainderOn` adapter compiles from `stateJetsCommonDomain`
  and `uniformRemainderOn_of_commonDomain`
- all five new theorems have only `propext`, `Classical.choice`, and `Quot.sound` in their
  axioms audits; no `sorryAx`
- source scans find no `sorry`, `admit`, or `axiom` in either new file; no original jet or
  live first-leg source was edited

## Parallel package K: uniform-remainder projections and jet specializations

Priority: P1. Conflict risk: low in new companions; high in the original jet owners.

Completed targets:

```text
ReasLib/Analysis/Asymptotics/UniformRemainder/ContinuousLinearMap.lean
ReasLib/Optimization/DFP/TwoPhaseControls/RadiusJet/Specialization.lean
ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/Transverse.lean
```

`ContinuousLinearMap.lean` transports a uniform remainder through an arbitrary continuous
linear map with coefficient `‖L‖ * C`.  Its sharper `fst` and `snd` corollaries preserve `C`
under product projections by using the max product norm directly.

`RadiusJet/Specialization.lean` isolates the rational-coefficient normalization that turns the
general weighted radius jet at `(198 / 5, 8, -9 / 5, 0)` into the slow-graph jet
`1 - 3 * ε ^ 3 + (5 / 2) * ε ^ 4`.

`StateJet/Transverse.lean` names the two-component transverse remainder, proves it is exactly
the `snd` projection of the joint state remainder, and transfers the same uniform coefficient
with the new product-projection API.

Because `StateJet` already imports `TransverseJet`, this bridge is deliberately post-StateJet;
importing it back into the original `TransverseJet.lean` would create a cycle.  Downstream code
can nevertheless derive the original `weightedTransverseRemainder` signature from the joint
state remainder without reproving a product-norm estimate.

Acceptance completed:

- isolated `lake lean` on all three companions: exit 0; the generic analysis target has zero
  output
- the original `slowGraphNormalizedRadiusJet` signature compiles from the weighted jet and the
  specialization theorem
- the original transverse uniform-remainder expression compiles from the StateJet bound and
  `transverseRemainder_uniform_of_state`
- all six new theorems have only `propext`, `Classical.choice`, and `Quot.sound` in their
  axioms audits; no `sorryAx`
- source scans find no tactic-level `sorry`, `admit`, or `axiom`, and no patch artifacts
- `StateJet.lean` was concurrently updated by its owner during this package; its source mtime
  was observed and no write was made to it or to the live first-leg target

## Parallel package L: finite-jet operations and componentwise state-jet assembly

Priority: P0 for Appendix Proposition A.5e. Conflict risk: low in the new modules; high in the
pipeline-owned `StateJet.lean`.

Completed targets:

```text
ReasLib/Analysis/Calculus/FiniteTaylorJet/OfFunctionOperations.lean
ReasLib/Optimization/DFP/TwoPhaseControls/StateJetAssembly.lean
ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/Combination.lean
```

`OfFunctionOperations.lean` proves that `ofFunction` commutes with product formation, that the
difference of two `C^m` functions with equal finite jets has zero jet, and that two component
zero jets assemble into a product zero jet.  These are general `FiniteTaylorJet` APIs and do
not depend on the DFP development.

`StateJetAssembly.lean` is deliberately pre-`StateJet`: it imports only `TransverseJet` and
the generic operations, defines the exact joint residual, proves all three component residuals
are `C^4` from `stateMapAnalytic` and `analyticAt_radiusFactor`, and assembles their scalar jet
certificates.  An ephemeral adapter with the original `StateJet.weightedStateJet` signature
compiles after a definitional `change`.  Therefore the main owner can integrate it without an
import cycle by importing `StateJetAssembly` and replacing the local proof body with the
checked adapter.

`StateJet/Combination.lean` is the post-`StateJet` projection interface.  Its clean theorem
`weightedStateJet_of_componentJets` exposes the minimal logical dependency: three scalar zero
jets imply the joint zero jet.  `weightedStateJet_via_components` records the exact current
reuse of `weightedNormalizedRadiusJet`, `weightedTransversePDefectJet`, and
`weightedTransverseHDefectJet`.

Acceptance completed:

- isolated `lake lean` on all three new targets: exit 0
- the original `weightedStateJet` statement compiles against the pre-import assembly in an
  ephemeral adapter
- the three generic finite-jet theorems, all six component smoothness theorems, and both
  conditional assembly theorems have only `propext`, `Classical.choice`, and `Quot.sound` in
  their axioms audits
- the two exact joint adapters have `sorryAx` precisely because the three scalar jet theorems
  they consume are still upstream placeholders; no new local placeholder was introduced
- source scans find no `sorry`, `admit`, or `axiom` in any Package L target and no patch
  artifacts
- `StateJet.lean` changed concurrently during this work (latest observed mtime
  `2026-08-21 18:03:56 +0800`); it and `FirstLeg.lean` were not edited

## Parallel package M: Peano comparison and flat transverse-slice jets

Priority: P0 for Appendix Proposition A.5b/A.5c. Conflict risk: low in the nineteen new modules;
high in the locked `RadiusJet.lean` and `TransverseJet.lean`, which were not edited.

Completed new targets, plus one extended existing finite-jet operations target:

```text
ReasLib/Analysis/Asymptotics/ContinuousMultilinearMap.lean
ReasLib/Analysis/Calculus/ContDiff/CrossDerivative.lean
ReasLib/Analysis/Calculus/FiniteTaylorJet/PeanoComparison.lean
ReasLib/Analysis/Calculus/FiniteTaylorJet/OfFunctionOperations.lean  (extended)
ReasLib/Analysis/Calculus/FiniteTaylorJet/FlatPath.lean
ReasLib/Analysis/Calculus/FiniteTaylorJet/SplitComparison.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/Assembly.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/MixedFlatPath.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/HessianAssembly.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/BasisHessianAssembly.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/ScaleStationarity.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/ScaleStationaryAssembly.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/GermCongruence.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/FirstLegScaleExpansion.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/SecondLegScaleExpansion.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/PureScaleJets.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/AnalyticJetGerm.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/WeightedDefectJets.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/StateJetClosure.lean
```

`PeanoComparison.lean` supplies equality from a little-o difference of jet evaluations, the
pointwise Peano remainder of `ofFunction`, and equality of derivative-constructed jets from a
translated `o(h^m)` comparison. It also supplies the directly usable `O(h^(m+1))` bridge and
an eventually-equal-functions bridge. `OfFunctionOperations.lean` now carries addition and
subtraction congruence for equal derivative-constructed jets.

`FlatPath.lean` proves that along `a + ε^3 • v₃ + ε^4 • v₄`, the order-four jet of an analytic
map only sees its value and first Fréchet derivative at `a`. The proof uses the analytic quadratic
remainder, `‖ε^3 v₃ + ε^4 v₄‖^2 = O(ε^6)`, and the Peano comparison bridge.

`FlatSliceJets.lean` applies this theorem to the zero-scale slice and proves the exact
coefficient-dependent portions of the three locked weighted jets:

- normalized radius: cubic/quartic coefficients `(5 * P + 6 * H) / 18`
- updated shape: cubic/quartic coefficients `(6 * H - P) / 9`
- updated high coordinate: constant through order four

`SplitComparison.lean` packages the generic `full = scale + flat - base + O(h^(m+1))` jet
assembly step. `FlatSliceJets/Assembly.lean` specializes it into three proof-complete
conditional wrappers for normalized radius, updated shape, and updated high coordinate. Each
wrapper needs only the corresponding pure-scale jet and an order-five mixed-interaction bound;
its conclusion is definitionally the paper-facing A.5b/A.5c target after unfolding
`graphJetPath`.

`ContinuousMultilinearMap.lean` proves a general diagonal finite-difference bound: if
`x = O(α)`, `y = O(α)`, and `y = O(β)`, then the diagonal difference of an `n`-linear map is
`O(α^(n-1) β)`. `MixedFlatPath.lean` combines this estimate with the analytic power-series
remainder and proves that, along `ε • u + ε^3 • v₃ + ε^4 • v₄`, a single quadratic cross
condition implies the entire mixed difference is `O(ε^5)`.

`HessianAssembly.lean` specializes that theorem to the three DFP observables, replacing each
opaque mixed-remainder hypothesis by one explicit `iteratedFDeriv ℝ 2` cross value.
`BasisHessianAssembly.lean` then uses multilinearity to reduce the coefficient-dependent
cross direction `(0,P₃,H₃)` to the two fixed axes `(0,1,0)` and `(0,0,1)`.
`ContDiff/CrossDerivative.lean` supplies the final generic bridge: local vanishing of the
`u`-directional derivative along the line `a + t • v`, together with `C²`, implies that the
`(u,v)` iterated second derivative vanishes, via the chain rule and Hessian symmetry.

`ScaleStationarity.lean` proves that the signed-scale derivative of radius, recovered shape,
and recovered high is zero at every positive point of the zero-scale slice. It upgrades this
to vanishing against every transverse Hessian direction and exports the six fixed shape/high
basis values. `ScaleStationaryAssembly.lean` therefore removes every mixed-Hessian hypothesis
from the three conditional assembly theorems; only the matching pure-scale jet remains.

`GermCongruence.lean` packages equality modulo `O(ε^n)` and proves the algebra needed by the
explicit calculation, including multiplication, reciprocal recovery, division, and the
locally positive square-root branch. `FirstLegScaleExpansion.lean` proves the four first-leg
factor expansions modulo `O(ε^5)`. `SecondLegScaleExpansion.lean` propagates them through the
second leg and proves the radius, shape, and high expansions at `(p,h)=(2,1)`.
`PureScaleJets.lean` bridges those order-five germs to order-four `FiniteTaylorJet` equalities
and assembles the full coefficient-dependent weighted jets.
`AnalyticJetGerm.lean` supplies the converse bridge used by the reparameterized graph defect:
analytic scalar functions with equal order-`m` `ofFunction` jets agree modulo
`O(ε^(m+1))`. `WeightedDefectJets.lean` combines that bridge with the radius and signed-scale
germs to prove the shape and high graph-invariance defect jets. `StateJetClosure.lean` converts
the normalized-radius and two defect jets into three scalar zero jets and then assembles the
joint state residual without using the old scalar placeholders.

Closure completed for A.5b/A.5c:

1. The pure-scale radius contribution is `(-300 / 18) ε^3 + (54 / 18) ε^4`, the shape
   contribution is `(348 / 9) ε^3 - (18 / 9) ε^4`, and the high contribution is `8 ε^3`.
2. All six basis mixed Hessians vanish by scale stationarity, so there is no remaining opaque
   mixed-interaction assumption through degree four.
3. The three locked paper-facing theorem statements were reproduced in a temporary adapter;
   after importing `FlatSliceJets.PureScaleJets`, each compiles with
   `simpa only [graphJetPath] using` the corresponding theorem below:
   - `weightedNormalizedRadiusJet_via_scaleStationarity`
   - `weightedTransversePJet_via_scaleStationarity`
   - `weightedTransverseHJet_via_scaleStationarity`
4. The two graph-invariance defect statements compile directly against
   `weightedTransversePDefectJet_via_scaleStationarity` and
   `weightedTransverseHDefectJet_via_scaleStationarity`.
5. The existing `StateJet.weightedStateJet` proof compiles after keeping its
   `remainder = jointResidual` rewrite and replacing the final call by
   `StateJetAssembly.weightedJointResidualJet_via_scaleStationarity`.

No further pure-scale, mixed-jet, defect, or joint-residual algebra is needed for these six
paper-facing leaves.

Acceptance completed:

- isolated `lake lean` on all twenty touched Package M targets: exit 0
- the original twenty-five audited public theorems and the thirteen newly audited germ,
  factor-expansion, pure-scale, and final assembly boundaries, plus the seven analytic-germ,
  defect, and joint-closure boundaries, have only `propext`, `Classical.choice`, and
  `Quot.sound`; no `sorryAx`
- exact temporary adapters for the one `RadiusJet`, four `TransverseJet`, and one
  `StateJet` paper-facing statements pass `lake lean`
- source scans find no `sorry`, `admit`, or custom `axiom`
- `RadiusJet.lean`, `TransverseJet.lean`, `StateJet.lean`, and `FirstLeg.lean` were not edited
- the broad `FiniteTaylorJet` memory lock was respected: `MixedFlatPath.lean` was placed under
  the independently owned `FlatSliceJets/` directory rather than added to that locked directory
- `FlatSliceJets.lean` only reads public `stateMap_fderiv_apply` from the locked
  `StateMap/Linearization.lean`; its observed mtime stayed `2026-08-21 18:02:08 +0800`
- no external source code was copied for Package M

## External-source reuse policy

A 2026-08-21 GitHub repository/code search found no proof-complete Lean development of DFP or
BFGS under weak Wolfe conditions that could be imported here. The relevant optimization hits
were executable libraries, while StatLean's advertised optimization coverage is first-order;
none supplied the mixed analytic jet or quasi-Newton counterexample proof needed here.
Package M therefore reuses only official Mathlib APIs:

- [analytic power series and iterated Fréchet derivatives](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/Analysis/Analytic/IteratedFDeriv.lean)
- [formal multilinear series and partial sums](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/Analysis/Calculus/FormalMultilinearSeries.lean)
- [continuous multilinear-map norm and finite-difference estimates](https://github.com/leanprover-community/mathlib4/blob/81a5d257c8e410db227a6665ed08f64fea08e997/Mathlib/Analysis/Normed/Module/Multilinear/Basic.lean)

| Source | Pin | Lean | License status | Allowed reuse |
| --- | --- | --- | --- | --- |
| mathlib4 | `81a5d257...` / local v4.32.0 | 4.32 | Apache-2.0 | Direct API use |
| michelsol/more-math | `0786fa7...` | 4.15 | Apache-2.0 | Port one theorem with attribution |
| rjwalters/lean-genius | `f9c6275...` | 4.31 | No root license found | Architecture only |
| kaplan196883/QIQT-H | `d42633d...` | 4.30 | No license found for Lean tree | Architecture only |
| xiyin137/OSreconstruction | `135ed13...` | 4.29 | Apache-2.0 | Selective attributed port |
| marpaia/crnt-lean | `9913799...` | 4.31 | MIT | Packaging/template port |
| dhofheinz/civic-alignment-program/`lean` | `852066f...` | 4.33-rc1 | Apache-2.0 | Architecture or attributed port |

Rules:

1. Keep commit-pinned source links beside any material adaptation.
2. Do not add any whole external repository as a Lake dependency.
3. Prefer a theorem re-proved against local Mathlib v4.32 APIs over copying a dependency chain.
4. If a source lacks a compatible explicit license, use only mathematical ideas and proof shape.
5. Record meaningful copied/adapted code in the eventual repository attribution file.
6. Every port must compile in isolation before a paper-facing wrapper imports it.

## Existing infrastructure not to duplicate

The following areas were proof-complete in the audit snapshot:

- `RealSymmetric2` and `RealSymmetric2/Eigenframe`
- `LinearAlgebra/SpectralRadius/ContractingNorm`
- `SmallLipschitzGraph`, including nonempty and complete-space instances
- uniform-remainder algebra, reparameterization, square-root, and matrix transports
- `PSeries` and `PositiveProduct`
- `Topology/Circle/VanishingStep`
- isolation and shrinking-ball infrastructure
- `ShrinkingSupportFinsum`
- `ContDiff/ZeroExtension`
- Euclidean Hessian, Loewner, and strong-convexity infrastructure

## Dispatch order

Start immediately and independently:

1. Package A: quantitative global inverse.
2. Package B: DFP update and secant identities.
3. Package C: parabolic recurrence.
4. Package E: support bounds.

Start Package D in its new support module, but leave I.15 integration to the main owner.
Start Package F only after the main pipeline freezes the public finite-jet API.

If only three side workers are available, choose A, B, and C. If a fourth is available, choose E.
Package D's inverse-stability lemma is a good small follow-up once A fixes the constant convention.

## Proof-stage execution handoff

This proof plan has now been executed for P1--P10. Every packet target compiles independently
without `sorry`; the matrix positive-definite Cauchy--Schwarz bridge is also complete.
Paper-facing integration remains with the main pipeline while its locks are live.

The baseline is Lean/Mathlib 4.32 with Mathlib pinned at `81a5d257...`. The table below is
retained as the historical dispatch and difficulty record. In particular, P9 now includes the
arbitrary-order family-uniform inverse derivative bound, not only orders one through three.

### Disjoint proof packets

| Packet | Exact target | First deliverable | Difficulty |
| --- | --- | --- | --- |
| P1 | `ReasLib/Topology/ContinuousMap/SmallLipschitzGraph/Transform.lean` | all four metric statements | easy |
| P2 | `ReasLib/Analysis/Calculus/ContDiff/SupportBounds.lean` | all five support statements | easy |
| P3 | `ReasLib/Analysis/Asymptotics/ParabolicRecurrence.lean` | Cesàro leaf and specializations | easy first tranche; hard final theorem |
| P4 | `ReasLib/Analysis/Calculus/ContDiff/AffineBounds.lean` | first-order affine bound | easy; second order medium |
| P5 | `ReasLib/Optimization/DFP/InverseUpdate/QuadraticForm.lean` | raw identities, then positivity | medium/core |
| P6 | `ReasLib/Optimization/DFP/InverseUpdate/Scaling.lean` | scaling and invariance | easy/medium after P5 |
| P7 | `ReasLib/Optimization/DFP/AbstractSecantStep/Identities.lean` | energy and curvature identities | easy/medium after P5 |
| P8 | `ReasLib/Analysis/Calculus/Deriv/GlobalInverse.lean` | monotonicity through inverse Lipschitz | medium; inverse smoothness high |
| P9 | `ReasLib/Analysis/Calculus/Deriv/GlobalInverseBounds.lean` | inverse derivative orders one to three | high; arbitrary order extreme |
| P10 | `ReasLib/Analysis/Calculus/ContDiff/ProductRule.lean` | second Fréchet product rule | medium |

P1--P4 are mutually independent. P5 owns only `QuadraticForm.lean`; P6 and P7 start after P5's
names freeze. P8 is independent of P1--P7. Never give two workers the same file, and do not
integrate into a paper-facing file while its current lock is live.

### P1: graph-transform metric leaves

- `dist_apply_le`: `BoundedContinuousFunction.dist_coe_le_dist`.
- `dist_le_iff`: `BoundedContinuousFunction.dist_le_iff_of_nonempty`.
- `dist_rightInverse_rightInverse_le`: apply `AntilipschitzWith.le_mul_dist`, rewrite both
  `Function.RightInverse` equations, then apply the pointwise perturbation estimate.
- `contractingWith_of_dist_apply_le_mul`: use `LipschitzWith.of_dist_le_mul` and lift the
  pointwise estimate through the preceding `dist_le_iff`.

Afterward use Mathlib's `ContractingWith.dist_le_of_fixedPoint`, `dist_fixedPoint_le`,
`aposteriori_dist_iterate_fixedPoint_le`, `apriori_dist_iterate_fixedPoint_le`, and
`fixedPoint_lipschitz_in_map`; do not add a project-local fixed-point-defect wrapper.

### P2, P4, and P10: calculus leaves

For `SupportBounds.lean`, use `support_iteratedFDeriv_subset` or
`tsupport_iteratedFDeriv_subset` plus `image_eq_zero_of_notMem_tsupport`. Combine
`ContDiff.continuous_iteratedFDeriv'`, `HasCompactSupport.iteratedFDeriv`, and
`Continuous.bounded_above_of_compact_support` for the global bound. Normalize the first- and
second-order corollaries with `norm_iteratedFDeriv_one` and `norm_iteratedFDeriv_fderiv`.

For the first affine bound, use the one-step Fréchet chain rule and
`ContinuousLinearMap.opNorm_comp_le`. For order two, expand with `iteratedFDeriv_two_apply`,
apply the chain rule twice, and use
`ContinuousMultilinearMap.norm_compContinuousLinearMap_le`. Do not use the generic
`norm_iteratedFDeriv_comp_le`: it contributes a factorial absent from the target.

For `ProductRule.lean`, get differentiability of `fderiv f` and `fderiv g` from
`ContDiffAt.fderiv_right`, expand twice with `fderiv_fun_mul`, identify fixed-direction
evaluation with `fderiv_clm_apply`, and differentiate the local first-order identity using
`Filter.EventuallyEq.fderiv_eq`. No new public bridge is needed.

### P3: parabolic recurrence

The first theorem is shorter through local Cesàro than through a Stolz port:

1. Apply `Filter.Tendsto.cesaro` to `u (j + 1) - u j`.
2. Telescope using `Finset.sum_range_sub`.
3. Remove `u 0 / n` with `tendsto_const_div_atTop_nhds_zero_nat`.

Then close `tendsto_invPow_forwardDiff_of_isBigO` by composing the ratio, decrement, and
inverse-power lemmas. The quadratic and quartic results are specializations plus numeral
normalization.

The hard inverse-power step is complete using the continuous divided slope of
`r ↦ (r ^ p)⁻¹` at `r = 1`. This avoids a case split when the successive ratio is exactly one.
The final theorem first proves `(ε j ^ p)⁻¹ ~ a * p * j`, then applies
`Asymptotics.IsEquivalent.rpow` and positivity to recover `ε`.

The pinned `more-math` theorem `stolz_cesaro_infty_case_1` is a proof-complete Apache-2.0
fallback for future non-unit denominators. Do not port it for `b n = n`, because local
Mathlib already supplies `Filter.Tendsto.cesaro`. No external source code was copied.

### P5--P7: DFP algebra and the missing bridge

Before the core positivity proof, assign an explicit target such as
`ReasLib/LinearAlgebra/Matrix/PosDef/CauchySchwarz.lean` for:

```lean
#check Matrix.PosDef.dotProduct_mulVec_sq_le
```

The theorem is proof-complete in `ReasLib/LinearAlgebra/Matrix/PosDef/CauchySchwarz.lean`.

Use `B := Matrix.toBilin' H`, `LinearMap.BilinForm.apply_sq_le_of_symm`,
`Matrix.toBilin'_apply'`, `Matrix.isSymm_toBilin'_iff_isSymm`,
`Matrix.isHermitian_iff_isSymm`, and `Matrix.PosDef.dotProduct_mulVec_pos`. This keeps
`[DecidableEq n]` and a `Matrix.toInnerProductSpace` local instance out of the public surface.
It reduces `inverseDFPUpdate_projectedQuadratic_nonneg` to `inv_mul_le_iff₀`.

Strict positivity still needs the equality case. Put
`w = x - ((y dot H*y)^(-1) * (x dot H*y)) • y`. If `w != 0`, positive definiteness makes
the projected term positive. If `w = 0`, then `x` is a multiple of `y`; `0 < s dot y` and
`x != 0` make the final rank-one term positive. Do not prove pointwise positivity by calling
the packaged `Matrix.PosDef.inverseDFPUpdate` theorem that it is meant to construct.

For scaling, first prove locally the zero-safe identity
`(c^2 * d)^(-1) * c^2 = d^(-1)` from `c != 0`; the original denominators need not be nonzero,
so an unconditional `field_simp` is unsound. The abstract-secant identities then normalize
from the existing displacement, gradient-change, and step-length definitions.

### P8--P9: quantitative inverse functions

Use this order in `GlobalInverse.lean`:

1. `strictMono_of_deriv_pos` and `NNReal.coe_pos`.
2. `mul_sub_le_image_sub_of_le_deriv` for coercive end estimates.
3. `Filter.tendsto_atTop.2` and the `atBot` analogue.
4. continuity plus `Continuous.surjective`, then strict-monotone injectivity.
5. `AntilipschitzWith.of_le_mul_dist`, `Real.dist_eq`, and reciprocal arithmetic.
6. `AntilipschitzWith.to_rightInverse` and `Function.rightInverse_invFun`.
7. An order-isomorphism/homeomorphism with `Homeomorph.contDiff_symm_deriv`; if needed, use
   the local inverse theorem at `Function.invFun f y` and inverse uniqueness.

For inverse derivative bounds, order one uses `HasDerivAt.of_local_left_inverse` and
`iteratedDeriv_one`. Orders two and three use `iteratedDeriv_comp_two` and
`iteratedDeriv_comp_three`, yielding bounds
`B2 * lower^(-3)` and `3 * B2^2 * lower^(-5) + B3 * lower^(-4)`.

The arbitrary-order proof avoids isolating a length-one ordered partition. Differentiate
`(f' ∘ g) * g' = 1` at order `j - 1`; the `k = 0` Leibniz term contains the highest derivative
of `g`, while every `k ≥ 1` term contains only lower inverse derivatives. Bound derivatives of
`f' ∘ g` with `iteratedDeriv_comp_eq_sum_orderedFinpartition`, where each part size is at most
`k < j`, and close a strong induction with finite `NNReal` sums.

### Proof completion checklist

1. Confirm the exact target lock and write ownership before editing.
2. Replace only that target's `:= sorry` bodies; keep public statements stable.
3. Run `lake lean <exact-target>` and never `lake build`.
4. Run an ephemeral `#print axioms` probe, then delete it.
5. Record any adapted external theorem with repository, commit, and license.
6. Integrate into a paper-facing consumer only after its ownership transfers.


## Integration checklist

For every package:

- assign exact file ownership before editing
- read the current target immediately before applying a patch
- preserve imports from generic to specific
- use one semantic module per task; do not create `Basic.lean`
- compile the owned target with `lake lean`
- compile the direct paper-facing consumer only after ownership is transferred
- re-run the quality audit rather than editing generated `M2FQualityAudits` snapshots
- report source commit, license, adapted theorem names, and local API differences
- at proof stage, remove `sorry` and run an ephemeral `#print axioms` audit

## Observable C9 side packet (2026-08-22)

This side packet closes the smoothness input for all thirteen scalar observables without editing
the live paper-facing `ObservableJet.lean`.

### Proof-complete delivered modules

The following thirteen additional companion modules pass isolated `lake lean` checks and contain
no local `sorry`, `admit`, or `axiom` declarations:

- `ReasLib/Analysis/Calculus/ContDiff/VecCons.lean`
- `ReasLib/Analysis/Calculus/ContDiff/DotProduct.lean`
- `ReasLib/Analysis/Calculus/ContDiff/MatrixMulVec.lean`
- `ReasLib/Analysis/Calculus/ContDiff/MatrixDiagonal.lean`
- `ReasLib/Analysis/Calculus/ContDiff/MatrixOf.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/FirstLeg/Analyticity.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/SecondLeg/Analyticity.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/Smoothness.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/CenterSmoothness.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/GradientNormSmoothness.lean`
- `ReasLib/Geometry/Euclidean/Plane/OrientedAngleToReal.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/EndpointAngleSmoothness.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/CoordinateSmoothness.lean`

The center module removes both line-search singularities algebraically.  In particular, it
extracts an explicit `ε ^ 2` factor from each displacement and proves the remaining vector
factor is nonzero at `(0, 2, 1)`.  This gives smoothness of both original step norms despite
the norm function being nonsmooth at the zero vector.  It exports:

- `CenterCancellation.halfCenterDisplacement_contDiffAt`
- `CenterCancellation.fullCenterDisplacement_contDiffAt`
- `CenterCancellation.firstStepNorm_contDiffAt`
- `CenterCancellation.secondStepNorm_contDiffAt`

The gradient module exports arbitrary-order smoothness of the initial, intermediate, and final
gradient norms.  The endpoint module exports arbitrary-order smoothness of both principal real
angle representatives.  The reusable geometric input is:

- `EuclideanPlane.oangle_toReal_eq_arctan_sub_of_pos`
- `EuclideanPlane.contDiffAt_oangle_toReal_of_pos`

The final aggregation theorem
`DFP.TwoLeg.observableCoordinateVector_contDiffAt` proves arbitrary-order joint smoothness of
the explicitly ordered `Fin 13 → ℝ` observable vector.

### Exact handoff for `ObservableJet.contDiffAt_coordinatesAlongGraphJetPath`

The complete proof was checked in an isolated standalone file.  The paper-facing module should
add:

```lean
public import ReasLib.Optimization.DFP.TwoPhaseControls.Observables.CoordinateSmoothness
import all ReasLib.Optimization.DFP.TwoPhaseControls.GraphJet
```

The second import is currently necessary under the module system: without it, the existing
`fun_prop` and `simp [DFP.TwoLeg.graphJetPath]` calls later in `ObservableJet.lean` see the
definition as unexposed.  At the observed snapshot this caused independent errors at the
graph-path continuity/base-value sites, in addition to the three remaining placeholders.

The `contDiffAt_coordinatesAlongGraphJetPath` body can then be replaced by the following
checked proof shape:

```lean
by
  let path : (((ℝ × ℝ) × (ℝ × ℝ)) × ℝ) → ℝ × ℝ × ℝ :=
    Function.uncurry (fun η : (ℝ × ℝ) × (ℝ × ℝ) ↦ fun ε : ℝ ↦
      DFP.TwoLeg.graphJetPath η.1.1 η.1.2 η.2.1 η.2.2 ε)
  have hpath : ContDiffAt ℝ 9 path (θ, 0) := by
    dsimp only [path, Function.uncurry_apply_pair]
    unfold DFP.TwoLeg.graphJetPath
    fun_prop
  have hbase : path (θ, 0) = (0, 2, 1) := by
    simp [path, DFP.TwoLeg.graphJetPath]
  have houter : ContDiffAt ℝ 9
      (fun x : ℝ × ℝ × ℝ ↦ coordinates (DFP.TwoLeg.observableMap x))
      (0, 2, 1) := by
    simpa only [coordinates] using
      DFP.TwoLeg.observableCoordinateVector_contDiffAt 9
  rw [← hbase] at houter
  have hcomp := houter.comp (θ, 0) hpath
  apply hcomp.congr_of_eventuallyEq
  filter_upwards [] with z
  rcases z with ⟨η, ε⟩
  rfl
```

Do not duplicate the thirteen coordinate proofs in `ObservableJet.lean`; the aggregation
theorem is the stable reuse boundary.

### Remaining observable integration packets

These packets are disjoint once the live `ObservableJet.lean` owner performs the small C9
integration above:

1. **O1, main-owner only:** add the two imports, replace the C9 placeholder, and recheck the
   existing branch-factor proof after exposing `graphJetPath`.
2. **O2, side-proof candidate:** derive `ObservableJet.uniformOn` from the checked joint
   `ContDiffAt ℝ 9` theorem and the generic finite-Taylor uniformity API.  Develop this in a
   standalone theorem or companion until the main file lock transfers.
3. **O3, after O2:** combine the existing thirteen state-domain lower bounds, the five
   `branchFactorsCommonDomain` bounds, and the order-nine uniform remainder into
   `observableJetsCommonDomain`.  This packet should contain only radius/minimum bookkeeping;
   it should not unfold DFP formulas.

### External reuse decision for this packet

No external source code was copied.  The proofs use only local Mathlib 4.32 APIs for
`ContDiffAt.norm`, arctangent smoothness, oriented-angle identities, finite products, and
matrix/vector assembly.  The GitHub search found no proof-complete Lean DFP/BFGS or weak-Wolfe
development that can replace these arguments.

Keep the pinned Apache-2.0 `more-math` Stolz--Cesàro theorem only as a future option for
non-unit denominators; the present recurrence uses Mathlib's `Filter.Tendsto.cesaro`.
`marpaia/crnt-lean` may be reused only for fixed-point packaging patterns: it does not provide
the maps-to-self, reparametrization, or contraction estimates needed by I.15.  Repositories
without an explicit compatible license remain architecture-only references.

### O2/O3 completion update

The O2 and O3 side packets are now proof-complete in two further unlocked companions:

- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/GraphJetSmoothness.lean`
- `ReasLib/Optimization/DFP/TwoPhaseControls/Observables/CommonDomain.lean`

`graphObservableFamily_contDiffAt` proves arbitrary-order joint smoothness on the entire
zero-scale coefficient fiber, and `graphObservableFamily_uniformOn` produces the order-nine
uniform derivative-constructed jets on every closed coefficient ball.

`observableBranchFactorsCommonDomain` supplies the common positive lower bound for all five
branch margins.  `observableJetsCommonDomain_via_companions` then combines it with
`StateJet.domainFactors_uniform_lower_bound` and the uniform order-nine remainder, using one
radius below `1 / 4` for all eighteen factors.

Both modules pass isolated source and exact-`.olean` checks, contain no local placeholders, and
their key declarations have axiom set `[propext, Classical.choice, Quot.sound]`.

All four paper-facing wrappers were checked together against duplicate definitions matching
`ObservableJet.lean`.  The main owner can add:

```lean
public import ReasLib.Optimization.DFP.TwoPhaseControls.Observables.CommonDomain
import all ReasLib.Optimization.DFP.TwoPhaseControls.Observables.CommonDomain
import all ReasLib.Optimization.DFP.TwoPhaseControls.GraphJet
```

Then the C9 theorem reduces to:

```lean
by
  have h := DFP.TwoLeg.graphObservableFamily_contDiffAt 9 θ
  unfold DFP.TwoLeg.graphObservableFamily DFP.TwoLeg.observableCoordinates at h
  unfold coordinates
  exact h
```

The existing `branchFactorsCommonDomain` may either be retained after exposing
`graphJetPath`, or replaced by:

```lean
by
  have h := DFP.TwoLeg.observableBranchFactorsCommonDomain B hB
  unfold DFP.TwoLeg.observableBranchFactors at h
  unfold branchFactors
  exact h
```

The `uniformOn` body is:

```lean
by
  have _hB := hB
  dsimp only
  have h := DFP.TwoLeg.graphObservableFamily_uniformOn B
  unfold DFP.TwoLeg.graphObservableFamily DFP.TwoLeg.observableCoordinates at h
  unfold coordinates
  exact h
```

The `observableJetsCommonDomain` body is:

```lean
by
  dsimp only
  have h := DFP.TwoLeg.observableJetsCommonDomain_via_companions B hB
  unfold DFP.TwoLeg.graphObservableFamily DFP.TwoLeg.observableCoordinates at h
  unfold DFP.TwoLeg.observableDomainFactors DFP.TwoLeg.observableBranchFactors at h
  unfold coordinates domainFactors branchFactors
  exact h
```

Thus all three placeholders observed in `ObservableJet.lean` have proof-complete companion
implementations.  Only the locked main-owner integration and its exact source check remain.

## Finite-dimensional square-root closure (2026-08-22)

The remaining placeholder in
`ReasLib/Analysis/InnerProductSpace/SquareRoot.lean` cannot be closed by the current CFC
adapter at its stated arbitrary-real-Hilbert-space generality.  An isolated elaboration probe
fails to synthesize

```lean
NonUnitalContinuousFunctionalCalculus ℝ (E →L[ℝ] E) IsSelfAdjoint
```

for an arbitrary real Hilbert space.  In the pinned Mathlib tree, the continuous-endomorphism
`CStarAlgebra` instance is provided for complex Hilbert spaces, not for the real operator
algebra in that statement.  Therefore the existing
`exists_sqrtEquiv_of_lowerBound_of_cfc` is a valid conditional adapter, but it is not a proof
of the original unconditional theorem.  Do not hide this gap by adding a non-synthesizable
local typeclass assumption to the original statement.

The finite-dimensional case needed by Euclidean DFP consumers is now proof-complete in:

```text
ReasLib/Analysis/InnerProductSpace/SquareRootFiniteDimensional.lean
```

Its theorem
`ContinuousLinearMap.exists_sqrtEquiv_of_lowerBound_of_finiteDimensional` has the same
conclusion as the original theorem and adds only `[FiniteDimensional ℝ E]`.  The proof:

1. transports the operator along `stdOrthonormalBasis.repr`;
2. reflects positivity and invertibility through `Matrix.toEuclideanCLM`;
3. applies the existing positive-definite matrix CFC square root; and
4. conjugates the square-root equivalence back through the orthonormal coordinates.

The exact source check and exact `.olean` generation both pass with zero output.  A direct
original-conclusion consumer compiles, the source contains no proof placeholders, and the
axiom audit reports only `[propext, Classical.choice, Quot.sound]`.

Reuse rule: finite-dimensional downstream code should import this new companion directly.
A truly infinite-dimensional real consumer still needs either upstream real-operator
functional calculus or a separate complexification/spectral-theorem construction; the
unconditional `SquareRoot.lean` placeholder remains an API blocker rather than an algebraic
DFP blocker.

The companion also exports
`exists_sqrtEquiv_normalizing_of_lowerBound_of_finiteDimensional`, which additionally proves
that pushing `H` forward through the inverse square-root coordinates gives the identity.  It
has the same clean axiom set as the factorization theorem.

## Live `ObservableJet` integration audit (2026-08-22)

At the latest observed owner snapshot, `ObservableJet.lean` has source bodies for
all three former placeholders: joint `C^9`, `uniformOn`, and `observableJetsCommonDomain`.
The last theorem is currently implemented by manual radius bookkeeping.

The dependency audit matters: its call to
`DFP.TwoLeg.StateJet.stateJetsCommonDomain` still has `[propext, sorryAx,
Classical.choice, Quot.sound]` in the current compiled environment.  Therefore source-level
removal of `sorry` from `ObservableJet.lean` does not yet make that theorem axiom-clean.

The proof-clean replacement remains the checked wrapper:

```lean
public import ReasLib.Optimization.DFP.TwoPhaseControls.Observables.CommonDomain
import all ReasLib.Optimization.DFP.TwoPhaseControls.Observables.CommonDomain

by
  dsimp only
  have h := DFP.TwoLeg.observableJetsCommonDomain_via_companions B hB
  unfold DFP.TwoLeg.graphObservableFamily DFP.TwoLeg.observableCoordinates at h
  unfold DFP.TwoLeg.observableDomainFactors DFP.TwoLeg.observableBranchFactors at h
  unfold coordinates domainFactors branchFactors
  exact h
```

Its axiom set is `[propext, Classical.choice, Quot.sound]` with no `sorryAx`.
The locked owner should route the final theorem through this companion (or first make the
StateJet dependency clean) rather than treating an empty source-level placeholder scan as
proof completion.

### StateJet clean facade update

The public dependency audit isolates the contamination precisely:

- `remainder_apply` and `domainFactors_apply` are axiom-clean;
- the old `weightedStateJet`, `stateJetsCommonDomain`, and `uniformRemainderOn` carry
  `sorryAx` in their current compiled forms;
- the scale-stationary closure and both common-domain companions are axiom-clean.

A stable exact-signature entry point now exists in:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/StateJet/ScaleStationaryClosure.lean
```

It exports `DFP.TwoLeg.StateJet.weightedStateJet_via_scaleStationarity`, with
the exact conclusion of `weightedStateJet`.  Its proof rewrites `remainder` to the joint
assembly residual and calls `weightedJointResidualJet_via_scaleStationarity`, bypassing the
older scalar-jet dependency chain.

Exact source compilation, exact `.olean` generation, original-signature consumption, and
the axiom audit all pass; the theorem depends only on
`[propext, Classical.choice, Quot.sound]`.

Together with `stateJetsCommonDomain_via_uniform_remainder`
and `uniformRemainderOn_via_commonDomain`, this provides clean public replacements for
all three currently contaminated StateJet declarations.  A same-signature
`ObservableJet.observableJetsCommonDomain` consumer was recompiled against the latest owner
`.olean`; it also depends only on `[propext, Classical.choice, Quot.sound]`.

#### Fresh upstream audit after the TransverseJet owner update

The previous `sorryAx` result is now identified as an object-file ordering issue,
not a remaining mathematical gap in the latest source chain:

- the current radius jet, all five transverse jet/remainder theorems, and
  `StateJetAssembly.weightedJointResidualJet` are axiom-clean;
- `StateJet.lean` imports exactly that clean transverse/assembly chain and has no source sorry;
- its existing `.olean` predates the newly generated `TransverseJet.olean`;
- the current `ObservableJet.olean` was built against that older StateJet object.

Consequently, rebuilding `StateJet` and then `ObservableJet` in dependency order should remove
the inherited `sorryAx`; this is an evidence-based inference pending the lock owners' rebuild.
The clean facade and companion wrapper remain immediately verified alternatives.  No locked
target was rebuilt or modified during this audit.

## Endpoint-angle coordinate-reduction packet (2026-08-22)

`EndpointAngleJet.lean` remained locked throughout this packet and was neither edited nor
rebuilt. Three independent companion layers now remove the geometric and arctangent
bookkeeping from its remaining `slowSecond` calculation:

```text
ReasLib/Geometry/Euclidean/Plane/FrameOrientedAngle.lean
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/CoordinateReduction.lean
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/CoordinateReductionAtBase.lean
```

The exported interfaces are:

- `EuclideanPlane.oangle_frame_mulVec`: a common positively oriented unit frame preserves
  the oriented angle of two coordinate vectors;
- `EuclideanPlane.oangle_frame_mulVec_toReal_eq_arctan_sub_of_pos`: after that cancellation,
  the principal real lift is the difference of the two slope arctangents;
- `DFP.TwoLeg.secondEndpointAngleIncrement_toReal_eq_arctan_sub_of_localData`: the pointwise
  two-leg observable reduction under its exact chart, positivity, and factorization data;
- `DFP.TwoLeg.secondEndpointAngleIncrement_toReal_eq_arctan_sub_eventually`: all those local
  hypotheses are discharged on one neighborhood of `(0, 2, 1)`.

All three sources pass exact `lake env lean` checks, their exact `.olean` files were generated,
and all four declarations have axiom set `[propext, Classical.choice, Quot.sound]` with no
`sorryAx`. The slow-path owner can pull the last theorem back along `slowGraphJetPath` and work
only with the two scalar slopes

```text
ε^2 * FirstLeg.gradientFactors(...).2 / FirstLeg.gradientFactors(...).1
SecondLeg.outputGradient(..., 1) / SecondLeg.outputGradient(..., 0).
```

A subsequent direct audit against the current definitions corrected the internal scalar split.
The exact current-source targets through order six are:

```text
intermediate slope = ε^2 + (66/5) ε^5 +  (7/5) ε^6 + O(ε^7)
final slope        =       -(38/5) ε^5 + (29/5) ε^6 + O(ε^7).
```

For the intermediate slope, the slow-path factors are
`Q = 1 - 2 ε^3 - (5/2) ε^4 + O(ε^5)` and
`U = 1 + (56/5) ε^3 - (11/10) ε^4 + O(ε^5)`, hence
`ε^2 U/Q = ε^2 + (66/5) ε^5 + (7/5) ε^6 + O(ε^7)`.
The second-leg residual factors independently give
`q = 1 - (9/2) ε^4 + O(ε^5)` and
`v = -(38/5) ε^3 + (29/5) ε^4 + O(ε^5)`.

Their arctangent difference still gives exactly
`-ε^2 - (104/5) ε^5 + (71/15) ε^6 + O(ε^7)`; the extra `1/3` in the sixth-order coefficient is
the cubic term of the intermediate slope.

The duplicated private arctangent proof in `EndpointAngleJet.lean` and `FrameAngleJet.lean`
has also been extracted to:

```text
ReasLib/Analysis/Asymptotics/ArctanTaylor.lean
```

It exports `Real.arctan_sub_cubic_isBigO` and the composition wrapper
`Real.arctan_comp_sub_cubic_isBigO`. Exact compilation and the axiom audit pass with the same
clean axiom set. Future owners should import this companion instead of maintaining another
private copy.

### Concurrent leaf-package audit

- `ReasLib/Analysis/Calculus/ContDiff/SupportBoundsClean.lean` now contains five complete,
  exact-signature-style clean replacements for the support/compact-support derivative bounds.
  It compiles exactly, and every declaration is free of `sorryAx`.
- `ReasLib/LinearAlgebra/Matrix/PosDef/CauchySchwarz.lean` already contains the independently
  reproduced weighted positive-definite Cauchy--Schwarz bridge
  `Matrix.PosDef.dotProduct_mulVec_sq_le`; `QuadraticForm.lean` now imports and uses it.
- The I.19 recurrence target was already filled and compiled by its lock owner. Its Cesàro
  proof uses `Filter.Tendsto.cesaro`, `Finset.sum_range_sub`, and
  `tendsto_const_div_atTop_nhds_zero_nat`; no competing companion was created.
## Slow-second scalar and mixed-path infrastructure (2026-08-22)

The corrected scalar-to-angle closure is proof-complete in:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/SlowSecondReduction.lean
```

It exports the two scalar slope definitions, their corrected degree-six polynomials,
`slowSecondEndpointAngle_eq_arctan_sub_eventually`, and
`slowSecond_of_slope_remainders`.  The last theorem reduces the original `slowSecond`
statement exactly to the two order-seven scalar remainder hypotheses while proving all frame
cancellation, arctangent Taylor, cubic-correction, and coefficient algebra internally.

Two further reusable algebra layers were added:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/QuotientGerm.lean
ReasLib/Optimization/DFP/TwoPhaseControls/FlatSliceJets/MixedCubicQuarticCross.lean
```

`DFP.TwoLeg.EqModPow.of_eq` and `EqModPow.div_approx` expose the quotient-germ proof
previously duplicated privately in FirstLeg, SecondLeg, AmplitudeJet, and NormJet calculations.
`FiniteTaylorJet.partialSum_five_mixed_cubic_quartic_sub_cross_isBigO` and
`FiniteTaylorJet.analytic_mixed_cubic_quartic_sub_cross_isBigO` retain the unique order-four
linear--cubic Hessian cross term and bound everything else by `O(ε^5)`.  The coefficient is
exactly one copy of `iteratedFDeriv ℝ 2 f a ![u, v₃]`: the two formal-series cross monomials,
each carrying the quadratic Taylor normalization, combine through the symmetric derivative sum.

All six public declarations above pass exact source checks, exact `.olean` generation, and
axiom audits with only `[propext, Classical.choice, Quot.sound]`.

### Refreshed GitHub reuse boundary

A commit-pinned audit of
[marpaia/crnt-lean at `99137993`](https://github.com/marpaia/crnt-lean/tree/99137993e729c8add247388718a22a0e0f393dab)
confirmed that `CRNT/Dynamics/GraphTransform.lean` cleanly packages
`ContractingWith.fixedPoint`, fixed-point uniqueness, the defect estimate, and Lipschitz
dependence on the operator.  Its `GraphTransformData.op_dist_le` is an input, however, and its
center-manifold layer similarly takes the Lyapunov--Perron displacement estimate as data.
Therefore it remains reusable only after the local DFP map-to-self, reparametrization, and
contraction estimates are proved; it cannot close I.15 or I.16 by import.  A source scan of the
exported CRNT tree found no `sorry`, and its repository CI documents the standard axiom audit.

The refreshed GitHub search again found no proof-complete Lean DFP/BFGS weak-Wolfe development.
For the mixed Taylor calculation, the only direct code dependency remains the pinned official
Mathlib analytic/formal-multilinear-series API; no external source was copied.

### Completed slow-second closure

The two previously open scalar leaves and their final composition are now proof-complete in:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/SlowSecondSlopes/Intermediate.lean
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/SlowSecondSlopes/Final.lean
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/SlowSecondSlopes/Closure.lean
```

`slowFirstLegGradientFactors_eqModPow_five` derives the corrected `Q/U` germs from
scale stationarity, the vanishing mixed Hessian term, and the finite Taylor comparison.
`slowIntermediateSlope_remainder` and `slowFinalSlopeRemainder` then prove the corrected
scalar expansions with coefficients `(66/5, 7/5)` and `(-38/5, 29/5)`, respectively.

`slowSecondRemainder` applies those two theorems to `slowSecond_of_slope_remainders` and has
exactly the conclusion of the still pipeline-owned `EndpointAngleJet.slowSecond` statement.
The locked paper-facing file need only import or delegate to this closure once ownership is
available; none of the long scalar calculations needs to be copied into it.

All three sources and their exact build-path `.olean` files compile.  A second independent
source compilation and axiom audit found no placeholder dependency: the public theorems use
only `[propext, Classical.choice, Quot.sound]`.

### Frame-angle scalar reduction

A separate low-conflict companion was added at:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/FrameAngleJet/SlowGraphReduction.lean
```

It defines the relative-frame tangent coordinate directly as `M 1 0 / M 0 0`, proves the
exact coordinate identity with `Real.arctan`, and initially reduced
`slowGraphFrameAngleRemainder` to one scalar germ.  That last leaf is now proof-complete in:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/FrameAngleJet/SlowGraphSlope.lean
```

`rawFrameQuotient_algebra` packages the four-entry quotient calculation,
`slowGraphRelativeFrameSlopeGerm` proves the raw slope polynomial through order seven, and
`slowGraphFrameAngleRemainder_viaSlope` has the unconditional conclusion of the legacy
frame-angle theorem.  The raw sixth-order coefficient is `-17/5`; the cubic arctangent
correction contributes `+9`, producing `28/5`.  None of these declarations imports the
sorry-backed legacy theorem.

### Amplitude and norm observable closure

The amplitude calculation and the reusable raw-frame data were extracted into:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/AmplitudeJet/SlowGraphRemainder.lean
```

This module uses only the stable underlying FirstLeg/SecondLeg/observable modules.  It exports
`slowGraphFirstLegFactorGerms`, `slowGraphSecondLegAmplitudeGerm`,
`slowGraphRawFrameGerms`, and `slowGraphAmplitudeRemainderDirect`.  The last theorem has the
exact conclusion of the legacy amplitude remainder without importing `AmplitudeJet.lean`.
The four raw-frame germs are also the shared input used by `SlowGraphSlope.lean`, avoiding a
second copy of the full explicit square-root and quotient calculation.

The two missing step-norm finite jets are cleanly recovered from the already complete remainder
theorems in:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/NormJet/CleanStepJets.lean
```

Together with `NormJet/CleanJets.lean`, the clean companion layer now covers all five top-level
slow-graph norm jets: first and second step norms plus initial, intermediate, and final gradient
norms.  The paper-facing declarations in `NormJet.lean` can delegate to these companions once
their owner integrates them; no explicit norm expansion needs to be repeated.

All amplitude, frame-angle, and norm companion declarations pass exact source and build-path
`.olean` checks.  Their axiom audits contain only `[propext, Classical.choice, Quot.sound]`.
A combined import probe checking all nine public observable conclusions also compiles.

### Center cancellation bridge and remaining blocker

The previously private local identification of the observable center displacement with its
singularity-cancelled formula is now public in:

```text
ReasLib/Optimization/DFP/TwoPhaseControls/Observables/CenterCancellationBridge.lean
```

It exports the pair theorem `centerDisplacements_eventuallyEq_canceled` and coordinatewise
`fullCenterDisplacement_eventuallyEq_canceled` / `halfCenterDisplacement_eventuallyEq_canceled`.
All three are exactly compiled and axiom-clean, and the live `CenterJet.lean` was not modified.

A current-source symbolic audit confirms the two remaining full-center coefficients:
the low coordinate is `-(116/5) ε^6 + (38/5) ε^7 + O(ε^8)`, while the high coordinate is
`-(508/5) ε^8 + O(ε^9)`.  The remaining hard lemma is not coefficient algebra: for a general
path with `p,h = slowGraph + O(ε^5)`, the low observable must gain three powers of `ε` and the
high observable four powers.  Generic smoothness alone preserves only `O(ε^5)`, so the next
safe package should prove this weighted transverse-transport estimate using the public
cancellation bridge and the newly exposed factor germs.


### Completed CenterJet closure and weighted transverse transport

The remaining full-center obstruction is now split into four proof-complete companion layers:

~~~text
ReasLib/Analysis/Calculus/FiniteTaylorJet/WeightedPerturbation.lean
ReasLib/Optimization/DFP/TwoPhaseControls/CenterJet/SlowGraphRemainder.lean
ReasLib/Optimization/DFP/TwoPhaseControls/CenterJet/TransverseStability.lean
ReasLib/Optimization/DFP/TwoPhaseControls/CenterJet/Closure.lean
~~~

FiniteTaylorJet.weighted_transverse_isBigO packages the convex-set mean-value estimate:
an input perturbation O(a) and a slice-derivative bound O(b) give an output perturbation
O(a*b). Its power-law specialization weighted_transverse_pow_isBigO gives
O(ε^(m+k)) directly. This is an integral-free wrapper around Mathlib's canonical
Convex.norm_image_sub_le_of_norm_fderiv_le.

For the DFP full-center map, canceledFullCenterDisplacement_eq_weightedFactors proves the
stronger local exact structure

~~~text
low coordinate  = ε^3 * fullCenterLowTransverseFactor
high coordinate = ε^4 * fullCenterHighTransverseFactor,
~~~

where both factors are C¹ at (0,2,1) and the high factor itself contains an additional
explicit ε. Consequently canceledFullCenterDisplacement_stabilityUnderGraphJets transports
fifth-order graph errors to O(ε^8) in the low coordinate and O(ε^9) in the high coordinate.

Independently, slowGraphFullCenterLowRemainder and slowGraphFullCenterHighRemainder establish
the exact polynomial-path models

~~~text
low  = -(116/5) ε^6 + (38/5) ε^7 + O(ε^8)
high = -(508/5) ε^8 + O(ε^9).
~~~

The high proof extracts the common ε² scale and verifies the remaining seventh-order
cancellation directly. slowFullLowRemainderViaStability and
slowFullHighRemainderViaStability then use the public cancellation bridge to combine the
transverse estimates with those two slow-graph computations. Their conclusions are identical
to the two still pipeline-owned declarations in CenterJet.lean; that legacy file can replace
each sorry by delegating to the corresponding clean closure theorem when its owner integrates
the companions.

All four new sources pass exact source compilation and exact build-path .olean generation.
Every public theorem audited here depends only on [propext, Classical.choice, Quot.sound],
with no sorryAx, admit, custom axiom, or legacy CenterJet theorem dependency. A combined import
probe covering amplitude, frame angle, the second endpoint angle, all five norm jets, both
full-center remainders, and the transverse stability theorem compiles successfully.

### Clean closure of all thirteen slow-graph observable jets

The three remaining observable leaves and their aggregate are now proof-complete in:

~~~text
ReasLib/Optimization/DFP/TwoPhaseControls/CenterJet/HalfRemainder.lean
ReasLib/Optimization/DFP/TwoPhaseControls/EndpointAngleJet/SlowFirstRemainder.lean
ReasLib/Optimization/DFP/TwoPhaseControls/ObservableJet/CleanSpecialization.lean
~~~

`CenterCancellation.canceledHalfCenterDisplacement_coordinates` gives the exact canceled
half-center formula

~~~text
low  = [2(p+1)/(3(1+2ε^3+ε^4))] ε^3,
high = [2(p+1)/(3(1+2ε^3+ε^4))] ε^5.
~~~

It yields `slowHalfLowRemainderViaCancellation` and
`slowHalfHighRemainderViaCancellation`, together with order-three and order-five finite jets,
without importing the legacy `CenterJet.lean` module.

For the first endpoint angle,
`firstEndpointAngleIncrement_toReal_eq_arctan_sub_eventually` reduces the oriented angle to
the difference of two scalar arctangents in the positive first-coordinate chart.
`slowFirstRemainder` then proves

~~~text
-2 ε^2 - (122/5) ε^5 + (88/15) ε^6 + O(ε^7)
~~~

using an exact rational slope certificate and the shared
`Real.arctan_comp_sub_cubic_isBigO`; `slowFirst_eqModPow_seven` exposes the same result as a
germ. This module does not import the legacy `EndpointAngleJet.lean` or its unfinished second
endpoint declaration.

Finally, `ObservableJet.cleanSlowOrder`, `cleanSlowPolynomial`, and
`slowGraphJetsClean (i : Fin 13)` assemble all thirteen coordinate jets directly from
`observableCoordinates`. The aggregate deliberately avoids `ObservableJet.lean` and uses the
clean amplitude, frame-angle, half/full-center, first/second-endpoint, and norm declarations.
The norm companion modules still transitively import the legacy `NormJet.lean`, but the five
theorems actually used have independent proof terms and clean axiom audits.

Exact source checks, exact Lake-path `.olean` generation, and an independent combined import
probe all pass. The aggregate theorem and every newly exported leaf depend only on
`[propext, Classical.choice, Quot.sound]`; no `sorryAx`, `admit`, custom axiom, or old
paper-facing observable theorem occurs in their proof dependencies. The old Appendix A.6g
declaration can therefore delegate to `slowGraphJetsClean` once its pipeline owner is ready.

The exact drop-in conversion is also compiled in:

~~~text
ReasLib/Optimization/DFP/TwoPhaseControls/ObservableJet/CleanCompatibility.lean
~~~

`slowGraphJets_viaClean` has the original `slowOrder` / `slowPolynomial` / `coordinates`
statement verbatim, but its proof is a definitional conversion from `slowGraphJetsClean`.
Its axiom audit is likewise standard-only, so an owner can replace the old body with this
single theorem without changing the paper-facing API.

### Clean orbit-level full-center drift

The center result has also been lifted through the physical orbit layer in:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/CenterDisplacementClean.lean
~~~

The existing half-center displacement and bound theorems were already axiom-clean. The two
full-center theorems were not: their only `sorryAx` dependency was the private normalized
observable remainder calling the legacy `CenterJet.slowFullLowRemainder` and
`slowFullHighRemainder`. The new `slowCurveFullCenterDriftClean` and
`slowCurveFullCenterDriftBoundClean` retain the old statements and route that leaf through
`CenterJet.slowFullLowRemainderViaStability` and
`slowFullHighRemainderViaStability`. Both exact builds and their independent axiom audit pass
with only `[propext, Classical.choice, Quot.sound]`.

### Independent-radius mixed expansion audit

The six remaining declarations in `MixedExpansion.lean` and
`MixedExpansion/PhysicalDrift.lean` are not consequences of the graph-specialized jet layer.
Their radius `r` is independent of the control `b`, whereas the completed graph infrastructure
couples the physical radius to `ε^2`. The missing common core is a cancellation-safe extension
of the mixed state and observable map near `r = 0`, jointly smooth in `(b, r, P, J)`, together
with its low-order derivative certificates.

Once that core exists, the radius/shape/scale/amplitude/frame remainder wrappers can reuse
`FiniteTaylorJet.isUniformOn_of_contDiffAt` and the existing uniform-remainder algebra. The
center statement is strictly harder: its remainder is bounded by `G |b| |r|^3`, so ordinary
Taylor control by `G |r|^3` is insufficient. A proof must expose an exact `b` factor (or prove
vanishing on the full `b = 0` fiber and use a uniform mean-value bound).

The recommended next target is therefore not a monolithic `MixedExpansion/Clean.lean`, but:

~~~text
ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion/IndependentRadiusJet.lean
~~~

It should package the canceled evaluator, actual-to-canceled equality on one uniform
neighborhood, joint `C^3` regularity, the five low-order coefficient certificates, and the
center `b * r^3` factor. Current Lean consumers use only `shapeExpansion` and
`scaleExpansion`; the graph-specific A.7--A.9 results do not depend on these six sorries.

### Graph-transform top-coefficient uniqueness

The contraction part of the finite-order graph-transform bootstrap is now isolated in:

~~~text
ReasLib/Analysis/Calculus/LocalCutoff/GraphJetTransform/FixedPointRegularity.lean
~~~

`coeffDistance_top_eq_zero_of_fixedPoints` applies the existing top-coefficient contraction
estimate to two fixed bounded graph jets whose lower coefficients agree. The bunching
constant is strictly below one, so their top sup-distance vanishes.
`topCoeff_eq_of_fixedPoints` converts this to pointwise equality of the top coefficients.
Both theorems compile exactly and are axiom-clean.

This is intentionally not yet a `ContDiff` bootstrap. Two genuinely new bridges remain:
construction of a bounded top-coefficient fixed section over a fixed lower holonomic jet,
and a holonomicity/closed-derivative theorem identifying that section with the next true
derivative.

### Pointwise-disjoint summability infrastructure

The generic infinite-sum bridge is now available in:

~~~text
ReasLib/Analysis/Calculus/ContDiff/DisjointFinsumSummable.lean
~~~

It proves summability and single/zero `tsum` formulas for a family whose function support is
subsingleton, then specializes these results to pairwise-disjoint topological supports.
Finite support is deliberately delegated to Mathlib's canonical
`summable_of_hasFiniteSupport`. All eight declarations pass exact source/`.olean` checks and
depend only on `[propext, Classical.choice, Quot.sound]`. This is the reusable base for the
paper-specific endpoint-bump pointwise formulas.

### Clean limiting-circle and endpoint-set layer

The paper-facing Definition 4.8b companion is complete in:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Definition_4_8b_Limiting_circle_and_endpoint_closed_set_candidate_EndpointSetClean.lean
~~~

It supplies clean even/odd endpoint formulas, the affine-unit-vector and metric-sphere
descriptions of the limit circle, closedness of that circle, the closed-set-candidate
membership formula, and closedness when every endpoint-sequence cluster point lies on the
circle. The proof uses definition equation lemmas plus
`IsClosed.union_range_of_mapClusterPt`, never the legacy sorry theorems. A fresh-source audit
also exposed and fixed the required direct `import all` of the underlying ReasLib definition
module; the final source, exact `.olean`, and all seven axiom audits now pass.
### Clean orbit convergence, tails, and uniform amplitude bounds

The clean observable remainders now propagate through the full slow orbit without using the
legacy amplitude or center modules:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/AmplitudeLimitClean.lean
ReasLib/Optimization/DFP/TwoPhaseOrbit/AmplitudeBoundsClean.lean
ReasLib/Optimization/DFP/TwoPhaseOrbit/CenterConvergenceClean.lean
ReasLib/Optimization/DFP/TwoPhaseOrbit/CenterTailClean.lean
~~~

`slowCurveAmplitudeExistsPositiveLimitClean` combines the clean amplitude drift with the
exact next-amplitude ratio and the positive-product infrastructure. The modulus and uniform
bound theorems in `AmplitudeBoundsClean` retain the legacy statements while depending only on
that clean limit chain. `slowCurveCenterTendstoClean` and the boundary/middle tail theorems use
the clean full-center drift; the boundary tail proof uses `hasSum_nat_add_iff'`,
`Finset.sum_range_sub`, `norm_tsum_le_tsum_norm`, and the sixth-power tail rather than a legacy
center theorem. Every exported declaration in these four modules has an exact source/`.olean`
check and a standard-only axiom audit.

### Clean limiting-circle geometry

The positive-radius geometry wrappers are complete in:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_8b_Limiting_circle_geometry_Clean.lean
~~~

`limitCircle_nonemptyClean`, `isCompact_limitCircleClean`, and
`infDist_limitCircleClean` reduce through `limitCircle_eq_sphereClean` to Mathlib's canonical
sphere nonemptiness, compactness, and infimum-distance formulas. They do not call the legacy
Lemma 4.8b geometry declarations and their axiom audits are standard-only.

### Clean endpoint correction and bump interpolation layer

The paper-facing endpoint definitions and the first pointwise bump layers are now isolated in:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_5_2_Endpoint_correction_definitions_Clean.lean
  Lemma_5_3a_Pointwise_summability_and_unique_active_bump_Clean.lean
  Lemma_5_4_First_and_second_derivative_formulas_for_each_bump_Clean.lean
  Lemma_5_9_Endpoint_interpolation_jets_Clean.lean
~~~

The first file exposes nine exact even/odd center, correction, radius, and scale identities
from definition equations and the already-clean endpoint-gradient parity formulas. Lemma 5.3a
specializes the generic disjoint-support summability API to the endpoint bumps; Lemma 5.4
delegates the two derivative formulas to the canonical affine-bump calculus. Finally,
`bumpCorrection_endpointClean`, `bumpCorrection_hasGradientAt_endpointClean`, and
`bumpCorrection_gradient_endpointClean` prove the endpoint value and gradient jets directly
from local support separation and the center-gradient theorem. None of these declarations
calls its legacy paper theorem. Independent fresh-source and axiom audits pass throughout.

### Refined external-reuse boundary

The pinned `marpaia/crnt-lean` graph-transform implementation is reusable for the Banach
fixed-point packaging on bounded continuous sections: it constructs a fixed section from an
operator contraction and proves uniqueness, defect estimates, and operator-perturbation
bounds. Its center-manifold construction remains a C0 Lyapunov--Perron fixed section, so it
does not supply the missing holonomicity/closed-derivative bridge for the local DFP graph jet.

`CRNT/Dynamics/FenichelC1Manifold.lean` provides a different reusable pattern: the implicit
function theorem yields a C1 manifold when the desired graph is the fiberwise zero set of a
smooth fast field with invertible fiber derivative. This can replace the graph-transform
regularity route only after the DFP invariance equation is recast in that form; it is not a
drop-in proof of the current fixed-point statement. Repository/code search found no external
proof-complete Lean formalization of DFP/BFGS under weak Wolfe. The direct reusable Taylor
layer remains Mathlib's analytic power-series and iterated-derivative API.

### Uniform center tails, endpoint corrections, and endpoint-gradient norms

The family-uniform orbit estimates are now clean in:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_7a_Uniform_center_tail_bounds_over_all_sufficiently_small_initial_scales_Clean.lean
  Lemma_5_2_Decay_of_the_endpoint_correction_vectors_Clean.lean
ReasLib/Optimization/DFP/TwoPhaseOrbit/EndpointGradientLimitClean.lean
~~~

`slowCurveCenterTailUniformBoundClean` does not infer a common constant from per-orbit
Big-O data. It telescopes the clean full-center increments and combines uniform amplitude,
full/half displacement, and sixth-power-tail constants before the initial scale is chosen.
The endpoint-correction theorem is then a parity wrapper using the clean even/odd identities.
The endpoint-gradient module proves convergence of the normalized two phase gradients from
local continuity at the canceled base, and obtains common positive lower/upper bounds by
combining a fixed local interval with `slowCurveAmplitudeUniformBoundsClean`.
All four new exported results have fresh-source and standard-only axiom audits.

### Exact endpoint interpolation and flattened iteration helpers

The clean endpoint interpolation chain now continues through:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Proposition_5_13_Exact_endpoint_value_and_gradient_interpolation_Clean.lean
  Proposition_5_14_The_realized_endpoint_sequence_is_the_exact_classical_DFP_orbit_Iteration_Clean.lean
~~~

Proposition 5.13 supplies the realized-objective endpoint value, gradient certificate,
prescribed gradient formula, and gradient-change/secant identities using the clean Lemma 5.9
jets. The iteration companion supplies axiom-clean even/odd formulas for the flattened metric
and exact step-length sequences by unfolding the two definitions; it never calls the legacy
parity theorems.

### Isolation-radius contract audit

The existing clean estimates do not yet justify the three Lemma 5.1 statements. The old
`slowCurveUniformEndpointSeparation` controls an infimum distance to a punctured set, but its
statement alone does not rule out two different endpoint indices representing the same point.
Consequently it cannot establish endpoint injectivity, an actual hypothesis needed by the
pairwise-disjoint isolation-ball theorem. It also supplies no family-uniform upper bound on
the consecutive endpoint distance, which is needed for the interpolation-radius upper bound.

The correct hard bridge should expose, with constants selected before the initial scale:

~~~text
c ε_k^2 <= dist (endpoint k) y              for y on the limiting circle,
c ε_k^2 <= dist (endpoint k) (endpoint l)   for k != l,
dist (endpoint k) (endpoint (k+1)) <= C ε_k^2.
~~~

The first two clauses give circle avoidance and injectivity. Together with the third they
feed the already existing canonical APIs
`Metric.le_infDist_union_range_diff_singleton_of_indexed_bound`,
`Metric.pairwiseDisjoint_isolationClosedBall`,
`Metric.disjoint_closedBall_of_lt_infDist`, and
`Metric.infDist_le_dist_of_mem`.

The remaining dynamics/winding chain is:
phase-radius quantitative control, clean amplitude-tail migration, endpoint-to-circle
uniform separation, the physical-angle perturbation and polar-gap results, positive winding
and cycle-count bounds, then amplitude-gap/near-return separation. Only after those leaves
are clean should the all-pairs separation and Lemma 5.1 wrappers be assembled.

### Canonical single-bump estimates already available

No new affine-bump bound file is needed. `AffineCutoffBump.lean` already contains
`AffineBump.norm_scaledLinearBump_le`,
`norm_fderiv_scaledLinearBump_le`, and
`norm_secondFDeriv_scaledLinearBump_le`; the corresponding constants are respectively
of order `M0 * ‖a‖ * rho`, `(M1 + M0) * ‖a‖`, and
`(M2 + 2*M1) * ‖a‖ / rho`. The smooth-cutoff 0/1/2 derivative bounds and all three affine
lemmas have standard-only axiom audits. Thus Lemma 5.5's remaining paper-specific blocker is
exactly the clean two-sided interpolation-radius estimate, not missing calculus infrastructure.


### Clean phase-radius, amplitude-tail, and limit-circle bridge

The orbit-level radius approximation and the missing amplitude-tail migration are now
axiom-clean in:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_12_Uniform_phase_radius_approximation_Clean.lean
ReasLib/Optimization/DFP/TwoPhaseOrbit/AmplitudeTailClean.lean
~~~

`slowCurvePhaseRadiusErrorIsBigOClean` gives a common two-phase cubic error estimate.
`slowCurvePhaseRadiusErrorIsLittleOClean` combines that estimate with fourth-power scale
summability to obtain the required little-o of the squared scale. The family-uniform theorem
selects all constants before the initial scale and uses the explicit modulus `ωR η = C * η`.
Its proof derives the normalized-gradient cubic estimate from the clean finite jets, transports
it from the polynomial graph to an arbitrary fifth-order graph by a strict-derivative estimate,
and then combines it with the clean center-tail and amplitude bounds.
`slowCurveAmplitudeTailEquivalentClean` is the exact clean migration of the first-order
amplitude tail. All four public results have exact build-path artifacts and standard-only
axiom audits. Together with `infDist_limitCircleClean`, these modules remove the dependency
blocker for a clean Lemma 4.20 companion.

### Full realized DFP orbit and dimension extension

The clean endpoint interpolation chain now reaches the complete orbit theorem:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Proposition_5_14_The_realized_endpoint_sequence_is_the_exact_classical_DFP_orbit_Clean.lean
  Corollary_6_7_Extension_to_every_dimension_n_ge2_Clean.lean
~~~

`DFP.TwoPhaseOrbit.realizedObjective_isOrbitClean` has the same statement as the legacy
Proposition 5.14. The proof supplies the missing first-leg frame reconstruction and proves
orthogonal equivariance of the inverse-DFP update, then combines the clean endpoint value and
gradient interpolation with the even/odd metric and step-length formulas. It does not call the
legacy Proposition 5.14, Lemma 5.13, or parity theorems.

The two clean Corollary 6.7 results transport the planar Hessian bounds through the canonical
orthogonal-sum objective and prove the embedded gradient-norm equivalence pointwise. They are
deliberately limited to the two genuinely missing mathematical statements; existing orbit,
Wolfe, and positive-definiteness transports are not rewrapped. A combined import audit of the
phase-radius theorem, full realized-orbit theorem, both dimension-extension results, and the
amplitude-tail theorem reports only `propext`, `Classical.choice`, and `Quot.sound`.

### Quantitative inverse constant regression check

The center-projection inverse statement remains corrected to
`AntilipschitzWith lower⁻¹`; using `lower` itself would reverse the constant convention in
Mathlib's `AntilipschitzWith`. The paper infrastructure file and the underlying
`Real.antilipschitzWith_inv_of_pos_le_deriv` / `Real.lipschitzWith_invFun_of_pos_le_deriv`
companion were freshly recompiled, and both theorem axiom audits are standard-only.

### Clean limit-circle distance and different-scale separation

The radial approximation now reaches both the per-orbit limiting-circle comparison and the
family-uniform different-scale separation layer:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/AmplitudeTailUniformClean.lean
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_20_Endpoint_distance_to_the_limiting_circle_Clean.lean
  Lemma_4_13_Separation_for_significantly_different_scales_Clean.lean
~~~

`slowCurveEndpointLimitCircleDistanceEquivalentClean` combines the clean amplitude-tail
equivalence with the two phase-radius little-o estimates and the exact sphere-distance
formula; `slowCurveEndpointRadiusIsLittleODistanceClean` then drops one scale order. The
uniform amplitude-tail theorem selects its constants before the initial scale, and the two
Lemma 4.13 results use it to obtain a common radial gap and endpoint-separation bound for
significantly different cycle scales. Fresh source checks, exact build-path artifacts, and
axiom audits for all five public declarations report only `propext`, `Classical.choice`, and
`Quot.sound`.

### Clean step-length and first descent identities

The proof-complete downstream optimization chain has begun in:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/StepLengthClean.lean
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_6_1_Exact_Armijo_decrease_ratio_identity_Clean.lean
  Lemma_6_2_Step_descent_and_correction_ratio_scaling_Clean.lean
~~~

`slowCurveTotalStepLengthNotSummableClean` obtains divergence from the clean endpoint-gradient
lower bound and the scale-summability infrastructure. `realizedObjective_decreaseRatioClean`
is the exact Armijo-ratio identity for the realized objective. The first clean Lemma 6.2
result, `slowCurvePhaseStepNormUniformBoundsClean`, combines the two normalized step-norm jets
with clean uniform amplitude bounds and phase validity, giving common positive multiples of
the endpoint radius for both phases and every sufficiently small slow-curve orbit. These
declarations have fresh source/exact-olean checks and standard-only axiom audits.

### Clean angle-lift branch control and endpoint-angle modulus

The branch-selection layer and the quantitative endpoint-angle remainder are now isolated in:

~~~text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_8c1_Compatible_real_lifts_of_the_physical_endpoint_polar_angles_Clean.lean
ReasLib/Optimization/DFP/TwoPhaseOrbit/EndpointAngleRemainderClean.lean
~~~

The clean Lemma 4.8c1 companion proves the real-lift zero/successor identities and the local
branch-induction theorem that identifies the polar-minus-gradient lift with the principal
oriented-angle correction whenever the polar, gradient, and correction gaps stay below the
specified principal intervals. It does not claim the orbit-level smallness hypotheses; those
are supplied by the subsequent center-tail perturbation argument.

`slowCurveEndpointAngleRemainderModulusClean` rebuilds the common order-two remainder modulus
from the independently proved clean first- and second-endpoint slow-graph remainders, a local
smooth-observable transport to arbitrary fifth-order graph jets, and the canonical uniform
remainder API. It does not import the legacy endpoint-angle specialization or remainder
module. Both companions have exact artifacts and standard-only axiom audits.

### Complete clean Lemma 6.2 scaling package

The four quantitative phase bounds are now proof-complete in:

~~~text
ReasLib/Optimization/DFP/TwoPhaseControls/QuadraticBounds.lean
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_6_2_Step_descent_and_correction_ratio_scaling_Clean.lean
  Lemma_6_2_Step_descent_and_correction_ratio_scaling_PredictedDecreaseClean.lean
  Lemma_6_2_Step_descent_and_correction_ratio_scaling_CorrectionRatioClean.lean
  Lemma_6_2_Step_descent_and_correction_ratio_scaling_StepRatioClean.lean
~~~

`QuadraticBounds.lean` supplies explicit two-dimensional quadratic-form, deviation, and
curvature-quotient estimates. The four paper companions then give the uniform step-norm,
predicted-decrease, correction-ratio, and step-ratio bounds. Their common constants are chosen
before the initial scale; the ratio proofs use phase validity to eliminate the positive powers
of the scale. Every public declaration was freshly source-checked, emitted to its exact build
path, and audited to depend only on `propext`, `Classical.choice`, and `Quot.sound`.

### Clean physical-angle and near-return separation chain

The angle and radial case split needed for all-pairs endpoint separation is now proof-complete:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/
  PolarGradientAngleError.lean
  EndpointAngleGap.lean
  AngularGapSeparation.lean
  NearReturnWinding.lean
  ScaleSeparation.lean
  EndpointDistance.lean
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_16_Cycle_count_inequality_for_a_near_return_Clean.lean
  Lemma_4_18_Radial_gap_after_one_or_many_near_return_windings_Clean.lean
  Lemma_4_19_Near_return_endpoint_separation_after_phase_radius_errors_Clean.lean
~~~

The local lift induction is instantiated using common endpoint-gradient lower bounds and
uniform center tails. This yields cubic polar-to-gradient lift error, explicit consecutive
polar-gap bounds, positive winding for near returns, the cycle-count inequality, and finally
an amplitude gap that absorbs the two phase-radius errors. The significantly-different-scale
and endpoint-to-circle companions have already been promoted into the canonical
`ScaleSeparation.lean` and `EndpointDistance.lean` modules. The remaining clean Lemma 4.21
work is therefore an exhaustive index/scale/angle case split plus a family-uniform
endpoint-to-circle lower bound, not a missing local geometric estimate.

### Clean one-turn amplitude-drop asymptotic

The sharper one-turn radial drop is now proved in:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/
  FrameAngleDriftClean.lean
  OneTurnAmplitudeDropClean.lean
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_18a_Sharper_one_turn_radial_drop_asymptotic_Clean.lean
~~~

`slowCurveFrameRotationClean` transports the clean slow-graph frame-slope expansion to an
arbitrary fifth-order invariant graph. For the amplitude law, the available clean little-o
statement is deliberately not strengthened to the legacy sixth-order claim. Instead,
`slowCurveOneTurnAmplitudeDropAsymptoticClean` proves a genuine fifth-order normalized
amplitude-ratio remainder by a strict-derivative graph transport and uses a revised summation
ledger whose accumulated error is cubic in the starting scale. This is sufficient for the
same one-turn equivalence. The source, Lake artifacts, and public axiom audit are clean; the
paper-facing Lemma 4.18a companion is only a typed wrapper over that theorem.

### Clean endpoint isolation, bump support, and Armijo closure

The uniform all-pairs separation and interpolation-support layer is now proof-complete:

~~~text
ReasLib/Optimization/DFP/TwoPhaseOrbit/
  EndpointIsolation.lean
  EndpointDistance.lean
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/
  Lemma_4_21_Uniform_all_pairs_endpoint_separation_Clean.lean
  Lemma_5_1_Isolation_radii_and_pairwise_disjoint_interpolation_balls_Clean.lean
  Lemma_5_1_Isolation_radii_and_pairwise_disjoint_interpolation_balls_AdjacentEndpointDistanceClean.lean
  Lemma_5_5_Uniform_supportwise_value_gradient_and_Hessian_bounds_Clean.lean
  Lemma_5_6_Support_distance_is_comparable_to_the_cycle_scale_Clean.lean
  Lemma_6_3_Armijo_inequality_with_c_1_1_4_Clean.lean
~~~

Clean Lemma 4.21 performs the exhaustive endpoint-pair case split and supplies both uniform
pair separation and a uniform endpoint-to-limit-circle lower bound. Clean Lemma 5.1 combines
those estimates with the adjacent-step upper bound to obtain two-sided interpolation-radius
bounds, pairwise-disjoint closed interpolation balls, and disjointness from the limiting
circle. Lemma 5.5 applies the canonical affine-cutoff-bump estimates to obtain uniform
supportwise value, gradient, and Hessian bounds.

Clean Lemma 5.6 now uses the canonical endpoint-distance equivalence together with the
little-o squared-radius estimate: the bump support lies in a ball whose radius is eventually
at most one quarter of the endpoint-to-circle distance, so the support distance remains
between positive multiples of the cycle scale. Its second result packages the interpolation
radius upper bound as a Big-O statement. The canonical `EndpointDistance.lean` implementation
was also switched from the legacy amplitude-tail theorem to the clean amplitude-tail API, so
both canonical distance declarations are now axiom-clean. Finally, clean Lemma 6.3 combines
the four clean Lemma 6.2 phase bounds with the exact decrease-ratio identity to prove the
uniform lower ratio and the Armijo inequality. All declarations listed here have exact Lake
artifacts and public axiom audits containing only `propext`, `Classical.choice`, and
