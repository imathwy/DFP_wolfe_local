# Article-to-Lean correspondence

This manuscript follows the source-link convention used by the TR-LALM paper.
Theorem-like blocks carry `leanDeclTag` links in the TeX source, while
formalized prose claims carry compact `leanClaimTag` links.

The machine-readable companion `sentence-locks.json` inventories every prose
sentence and has two explicit lock layers: `statement_anchors` (the nine
theorem-like statements) and `inline_anchors` (the compact links in the
abstract, introduction, verification, and appendix). Every sentence in the
inventory has a `boundary` record unless it is represented by one of those
formal anchors; citation and empirical sentences are never silently promoted
to Lean claims. The generator is `tools/generate_sentence_locks.py`.

All links are pinned to Lean commit
`e308927f5b7930bdd002f0c0e42b9d112ad821cb`. A source line is a navigation
anchor; the declaration named below is the semantic identity.

## Article statements

| Article statement | Principal Lean declaration | Status |
| --- | --- | --- |
| Main theorem | `DFP.existsStrongWolfeCounterexample_of_parameterRange`; `DFP.main_not_globalWeakWolfeConvergence_of_parameterRange` | exact paper-range certificate plus direct negation |
| Identity initialization | `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange` | matrix-facing certificate with positive gradient `liminf` |
| DFP update identities | `DFP.AbstractSecantStep.nextGradient_formula`; `DFP.AbstractSecantStep.nextInverseHessian_formula` | exact |
| Local invariant graph | `LocalInvariantGraph.existsOfComplexSpectralRadiusLtOne` | exact abstract theorem |
| Rescaled recurrence and invariant center manifold | `DFP.TwoLeg.stateMapAnalytic`; `DFP.TwoLeg.stateMap_fderiv_apply`; `DFP.TwoLeg.exists_localForwardInvariantSlowCurve`; `DFP.TwoLeg.slowGraphSignedRecurrence` | compound statement represented by focused declarations |
| Two-step asymptotic expansions | `DFP.TwoLeg.slowCurveAmplitudeDrift`; `DFP.TwoPhaseOrbit.slowCurveFrameRotation`; `DFP.TwoPhaseOrbit.slowCurveFullCenterDrift`; `DFP.TwoPhaseOrbit.slowCurveHalfCenterDisplacement`; endpoint-angle declarations | compound statement represented by focused declarations |
| Scalar asymptotics and limiting circle | `DFP.TwoPhaseOrbit.slowCurveScalarAsymptotics`; `DFP.TwoPhaseOrbit.slowCurveEndpointClusterSet_eq_limitCircle` | exact compound interface |
| Uniform separation | `DFP.TwoPhaseOrbit.slowCurveUniformEndpointSeparation` | exact |
| Disjoint-support interpolation | `DFP.TwoLeg.SlowCurve.bumpCorrectionExtension`; endpoint interpolation declarations | exact compound interface |

## Coverage boundary

The formal correspondence covers mathematical definitions, proved claims,
construction invariants, asymptotic statements, and the final theorem chain.
It intentionally does not attach Lean declarations to:

- reports about what cited papers state;
- prose describing the organization of the manuscript;
- numerical values, figures, tables, SciPy behavior, or regression fits;
- authorial scope statements such as claims explicitly not made;
- open problems and future work.

Those sentences are natural-language evidence or metadata, not Lean
propositions. Assigning a declaration to them would overstate what the
formalization verifies. The distinction is intentional: a theorem-like
sentence is locked to a declaration, while non-theorem prose is locked to an
auditable boundary category.

## Maintenance rule

When the manuscript changes, update both `main.tex` and this table. A link is
accepted only when its Lean statement has been checked for the same binders,
parameter range, assumptions, conclusion, and limiting semantics. File names
or historical numbering alone are not sufficient evidence of correspondence.
