# Article-to-Lean correspondence

This manuscript follows the source-link convention used by the TR-LALM paper.
Theorem-like blocks carry `leanDeclTag` links in the TeX source, while
formalized prose claims carry compact `leanClaimTag` links.

The machine-readable companion `sentence-locks.json` inventories the natural
language in the abstract, body, theorem statements, proof explanations, and
figure/table captions. It has two explicit lock layers: `statement_anchors`
(the nine theorem-like statements) and `inline_anchors` (the compact links in
the abstract, introduction, verification, and appendix). Sentence records
carry `sentence_ids` back to their local anchor when a claim is explicitly
marked. The current manifest (schema version 3) contains 585 sentence records,
65 Lean-locked sentences, and 520 auditable boundary records. Forty of the 50
inline anchors have a sentence-level link; the remaining ten are
formula-only navigation anchors. Citation, numerical, proof-
explanatory, and editorial sentences are never silently promoted to Lean
claims. The generator is `tools/generate_sentence_locks.py`.

The manifest separately labels 234 mathematical prose records as
`unmapped-claim`: these are an explicit review worklist, not purported Lean
proofs. They can be promoted only after a declaration with matching binders and
quantifiers is identified.

All links are pinned to Lean commit
`e308927f5b7930bdd002f0c0e42b9d112ad821cb`. A source line is a navigation
anchor; the declaration named below is the semantic identity.

## Article statements

| Article statement | Principal Lean declaration | Status |
| --- | --- | --- |
| Main theorem | `DFP.existsStrongWolfeCounterexample_of_parameterRange`; `DFP.main_not_globalWeakWolfeConvergence_of_parameterRange` | exact paper-range certificate plus direct negation |
| Level-set formulation | `LevelSetGlobalWeakWolfeConvergenceAt`; `DFP.main_not_levelSetGlobalWeakWolfeConvergence_of_parameterRange` | exact relevant-level-set predicate and its parameterized negation |
| Identity initialization | `DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange` | matrix-facing certificate with positive gradient `liminf` |
| DFP update identities | `DFP.AbstractSecantStep.nextGradient_formula`; `DFP.AbstractSecantStep.nextInverseHessian_formula` | exact |
| Local invariant graph | `LocalInvariantGraph.existsOfComplexSpectralRadiusLtOne` | exact abstract theorem |
| Rescaled recurrence and invariant center manifold | `DFP.TwoLeg.stateMapAnalytic`; `DFP.TwoLeg.stateMap_fderiv_apply`; `DFP.TwoLeg.exists_localForwardInvariantSlowCurve`; `DFP.TwoLeg.slowGraphSignedRecurrence` | compound statement represented by focused declarations |
| Two-step asymptotic expansions | `DFP.TwoLeg.slowCurveAmplitudeDrift`; `DFP.TwoPhaseOrbit.slowCurveFrameRotation`; `DFP.TwoPhaseOrbit.slowCurveFullCenterDrift`; `DFP.TwoPhaseOrbit.slowCurveHalfCenterDisplacement`; endpoint-angle declarations | compound statement represented by focused declarations |
| Scalar asymptotics and limiting circle | `DFP.TwoPhaseOrbit.slowCurveScalarAsymptotics`; `DFP.TwoPhaseOrbit.slowCurveEndpointClusterSet_eq_limitCircle` | exact compound interface |
| Uniform separation | `DFP.TwoPhaseOrbit.slowCurveUniformEndpointSeparation` | exact |
| Disjoint-support interpolation | `DFP.TwoLeg.SlowCurve.bumpCorrectionExtension`; endpoint interpolation declarations | exact compound interface |
| Parameterized Wolfe verification | `DFP.TwoLeg.SlowCurve.endpointArmijo_of_lt_two_thirds`; `DFP.TwoPhaseOrbit.endpointCurvatureCertificates_of_ge_two_thirds` | full paper range `0 < c₁ < 2/3`, `2/3 ≤ c₂ < 1` |

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
propositions. Proof explanations are retained in the inventory as
`proof-prose:boundary` unless an explicit claim tag identifies a formal
interface. Assigning a declaration to unsupported text would overstate what
the formalization verifies. The distinction is intentional: a theorem-like or
explicitly tagged claim is locked to a declaration, while non-theorem prose is
locked to an auditable boundary category.

The endpoint interpolation display also states the pointwise Hessian identity
`∇²f(xₖ)=I`. The current Lean API proves the value and gradient interfaces and
the global Hessian bounds, but has no standalone named declaration for that
pointwise identity; it therefore remains a recorded review boundary rather
than an invented Lean link.

## Maintenance rule

When the manuscript changes, update both `main.tex` and this table. A link is
accepted only when its Lean statement has been checked for the same binders,
parameter range, assumptions, conclusion, and limiting semantics. File names
or historical numbering alone are not sufficient evidence of correspondence.
