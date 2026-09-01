#!/usr/bin/env python3
"""Build a conservative article-to-Lean lock manifest.

The publication TeX contains two different kinds of language:

* theorem-like mathematical statements, which can be locked to Lean
  declarations;
* background, proof-navigation, empirical, and editorial prose, which must be
  recorded but must not be presented as machine-checked propositions.

This tool intentionally keeps those categories separate.  It discovers every
theorem-like environment and every explicit ``leanClaimTag`` in ``main.tex``,
validates their source anchors, and records all prose sentences with an
explicit boundary status.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "main.tex"
OUT = ROOT / "sentence-locks.json"
SNAPSHOT = "e308927f5b7930bdd002f0c0e42b9d112ad821cb"


class Decl(tuple):
    __slots__ = ()

    @property
    def name(self) -> str:
        return self[0]

    @property
    def file(self) -> str:
        return self[1]

    @property
    def line(self) -> int:
        return self[2]

    @property
    def relation(self) -> str:
        return self[3]


def decl(name: str, file: str, line: int, relation: str) -> Decl:
    return Decl((name, file, line, relation))


THEOREM_FILE = (
    "DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_"
    "under_weak_Wolfe_/Theorem_Main_theorem.lean"
)
BASE = "DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/"

DECLS: dict[str, Decl] = {
    "main": decl(
        "DFP.existsStrongWolfeCounterexample_of_parameterRange",
        THEOREM_FILE,
        17,
        "paper-range strong-Wolfe counterexample certificate",
    ),
    "main-negation": decl(
        "DFP.main_not_globalWeakWolfeConvergence_of_parameterRange",
        THEOREM_FILE,
        27,
        "direct negation of the fixed-coefficient global-convergence predicate",
    ),
    "identity": decl(
        "DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange",
        THEOREM_FILE,
        155,
        "identity-initialized matrix certificate with positive gradient liminf",
    ),
    "dfp-iteration": decl(
        "DFP.InverseIteration.ofSequences",
        BASE + "Definition_2_1_Classical_inverse_form_DFP_iteration.lean",
        11,
        "inverse-form DFP recurrence interface",
    ),
    "weak-wolfe": decl(
        "LineSearch.IsWeakWolfe",
        BASE + "Definition_2_2_Standard_weak_Wolfe_conditions.lean",
        8,
        "standard weak-Wolfe predicate",
    ),
    "strong-wolfe": decl(
        "LineSearch.IsStrongWolfe",
        "ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean",
        34,
        "standard strong-Wolfe predicate",
    ),
    "global-predicate": decl(
        "GlobalWeakWolfeConvergenceAt",
        "ReasLib/Optimization/DFP/GlobalConvergence.lean",
        27,
        "fixed-coefficient global-convergence predicate",
    ),
    "levelset-predicate": decl(
        "LevelSetGlobalWeakWolfeConvergenceAt",
        "ReasLib/Optimization/DFP/LevelSetGlobalConvergence.lean",
        161,
        "fixed-coefficient level-set global-convergence predicate",
    ),
    "levelset-negation": decl(
        "DFP.main_not_levelSetGlobalWeakWolfeConvergence_of_parameterRange",
        THEOREM_FILE,
        57,
        "direct negation of the level-set convergence predicate",
    ),
    "cycle-state": decl(
        "CycleBoundaryState.ofParams",
        BASE + "Definition_3_1_Canonical_cycle_boundary_state.lean",
        11,
        "canonical cycle-boundary state",
    ),
    "abstract-step": decl(
        "DFP.AbstractSecantStep.ofMatrices",
        BASE + "Definition_3_2_Abstract_secant_step_with_prescribed_line_ratio.lean",
        15,
        "abstract secant step with prescribed line ratio",
    ),
    "line-ratio": decl(
        "DFP.AbstractSecantStep.lineRatio",
        BASE + "Lemma_3_3_Exact_line_ratio_identity.lean",
        11,
        "exact secant-curvature to predicted-decrease ratio",
    ),
    "controls": decl(
        "TwoPhaseControls.phase",
        BASE + "Definition_3_4_Two_phase_controls.lean",
        17,
        "two-phase secant controls",
    ),
    "update-gradient": decl(
        "DFP.AbstractSecantStep.nextGradient_formula",
        BASE + "Proposition_3_6_Exact_one_step_gradient_map.lean",
        14,
        "exact one-step gradient update",
    ),
    "update-hessian": decl(
        "DFP.AbstractSecantStep.nextInverseHessian_formula",
        BASE + "Proposition_3_7_Exact_one_step_DFP_matrix_map.lean",
        10,
        "exact one-step inverse-Hessian update",
    ),
    "graph": decl(
        "LocalInvariantGraph.existsOfComplexSpectralRadiusLtOne",
        BASE + "Lemma_Local_invariant_graph_for_a_map.lean",
        15,
        "local invariant graph theorem",
    ),
    "state-map": decl(
        "DFP.TwoLeg.stateMapAnalytic",
        BASE + "Lemma_Blown_up_map_and_invariant_slow_curve.lean",
        10,
        "analytic extension of the two-leg state map",
    ),
    "slow-curve": decl(
        "DFP.TwoLeg.exists_localForwardInvariantSlowCurve",
        BASE + "Lemma_Blown_up_map_and_invariant_slow_curve.lean",
        54,
        "forward-invariant slow curve and its jets",
    ),
    "recurrence": decl(
        "DFP.TwoLeg.slowGraphSignedRecurrence",
        BASE + "Lemma_3_18_Parabolic_center_recurrence.lean",
        13,
        "parabolic center recurrence",
    ),
    "state-linearization": decl(
        "DFP.TwoLeg.stateMap_fderiv_apply",
        BASE + "Lemma_Blown_up_map_and_invariant_slow_curve.lean",
        25,
        "linearization of the rescaled state map",
    ),
    "orbit": decl(
        "DFP.TwoPhaseOrbit.ofSlowCurveExact",
        BASE + "Definition_3_19b_Exact_infinite_abstract_two_phase_orbit.lean",
        13,
        "exact infinite two-phase orbit",
    ),
    "amplitude": decl(
        "DFP.TwoLeg.slowCurveAmplitudeDrift",
        "ReasLib/Optimization/DFP/TwoPhaseControls/AmplitudeJet.lean",
        1592,
        "cycle amplitude drift",
    ),
    "frame": decl(
        "DFP.TwoPhaseOrbit.slowCurveFrameRotation",
        "ReasLib/Optimization/DFP/TwoPhaseOrbit/FrameAngleDrift.lean",
        17,
        "unwrapped frame rotation",
    ),
    "center": decl(
        "DFP.TwoPhaseOrbit.slowCurveFullCenterDrift",
        "ReasLib/Optimization/DFP/TwoPhaseOrbit/CenterDisplacement.lean",
        509,
        "full-cycle center drift",
    ),
    "half-center": decl(
        "DFP.TwoPhaseOrbit.slowCurveHalfCenterDisplacement",
        "ReasLib/Optimization/DFP/TwoPhaseOrbit/CenterDisplacement.lean",
        329,
        "half-cycle center displacement",
    ),
    "frame-winding": decl(
        "DFP.TwoPhaseOrbit.slowCurveFrameAngleTendstoAtBot",
        BASE + "Lemma_4_8_Unbounded_frame_winding.lean",
        13,
        "unbounded unwrapped frame-angle winding",
    ),
    "angle-first": decl(
        "slowCurveFirstEndpointAngleIncrement",
        BASE + "Lemma_3_24_Leading_within_cycle_endpoint_gradient_angle_increments.lean",
        14,
        "first within-cycle endpoint angle increment",
    ),
    "angle-second": decl(
        "slowCurveSecondEndpointAngleIncrement",
        BASE + "Lemma_3_24_Leading_within_cycle_endpoint_gradient_angle_increments.lean",
        34,
        "second within-cycle endpoint angle increment",
    ),
    "circle": decl(
        "DFP.TwoPhaseOrbit.slowCurveEndpointClusterSet_eq_limitCircle",
        BASE + "Lemma_4_9_Full_limiting_circle_as_the_endpoint_accumulation_set.lean",
        15,
        "endpoint cluster set equals the limiting circle",
    ),
    "scalar": decl(
        "DFP.TwoPhaseOrbit.slowCurveScalarAsymptotics",
        BASE + "Lemma_Scalar_asymptotics.lean",
        11,
        "scalar asymptotics and limiting data",
    ),
    "separation": decl(
        "DFP.TwoPhaseOrbit.slowCurveUniformEndpointSeparation",
        BASE + "Lemma_Uniform_separation.lean",
        10,
        "uniform endpoint separation",
    ),
    "bump": decl(
        "DFP.TwoLeg.SlowCurve.bumpCorrectionExtension",
        BASE + "Lemma_Disjoint_bump_extension.lean",
        11,
        "global disjoint-bump extension",
    ),
    "objective": decl(
        "DFP.TwoPhaseOrbit.realizedObjective",
        BASE + "Definition_5_11_Global_realized_objective.lean",
        8,
        "global realized objective",
    ),
    "interpolation": decl(
        "DFP.TwoPhaseOrbit.realizedObjective_endpoint",
        BASE + "Proposition_5_13_Exact_endpoint_value_and_gradient_interpolation.lean",
        17,
        "endpoint value interpolation",
    ),
    "gradient-interpolation": decl(
        "DFP.TwoPhaseOrbit.realizedObjective_gradient_formula_endpoint",
        BASE + "Proposition_5_13_Exact_endpoint_value_and_gradient_interpolation.lean",
        25,
        "endpoint gradient interpolation",
    ),
    "hessian": decl(
        "slowCurveRealizedObjectiveHessianBounds",
        BASE + "Proposition_5_12a_Global_Hessian_bounds.lean",
        59,
        "global Hessian bounds",
    ),
    "convexity": decl(
        "slowCurveRealizedObjective_strongConvexOn",
        BASE + "Corollary_5_12b_Global_strong_and_uniform_convexity.lean",
        16,
        "global strong and uniform convexity",
    ),
    "realized-orbit": decl(
        "DFP.TwoPhaseOrbit.realizedObjective_isOrbit",
        BASE + "Proposition_5_14_The_realized_endpoint_sequence_is_the_exact_classical_DFP_orbit.lean",
        10,
        "realized endpoint sequence is a classical DFP orbit",
    ),
    "decrease": decl(
        "DFP.TwoPhaseOrbit.realizedObjective_decreaseRatio",
        BASE + "Lemma_6_1_Exact_Armijo_decrease_ratio_identity.lean",
        10,
        "exact objective decrease ratio",
    ),
    "armijo": decl(
        "DFP.TwoLeg.SlowCurve.endpointArmijo_of_lt_two_thirds",
        "ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean",
        407,
        "Armijo inequality for every coefficient in the paper range",
    ),
    "curvature": decl(
        "DFP.TwoPhaseOrbit.endpointCurvatureCertificates_of_ge_two_thirds",
        "ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean",
        310,
        "endpoint strong/weak curvature certificates for every c₂ ≥ 2 / 3",
    ),
    "cycle-spec": decl(
        "CycleBoundaryState.spec",
        "ReasLib/Optimization/DFP/CycleBoundaryState.lean",
        115,
        "metric and gradient specification of a cycle-boundary state",
    ),
    "first-matrix": decl(
        "TwoPhaseControls.first_matrix",
        "ReasLib/Optimization/DFP/TwoPhaseControls.lean",
        34,
        "first phase matrix formula",
    ),
    "first-tau": decl(
        "TwoPhaseControls.first_tau",
        "ReasLib/Optimization/DFP/TwoPhaseControls.lean",
        40,
        "first phase line-ratio formula",
    ),
    "second-matrix": decl(
        "TwoPhaseControls.second_matrix",
        "ReasLib/Optimization/DFP/TwoPhaseControls.lean",
        50,
        "second phase matrix formula",
    ),
    "second-tau": decl(
        "TwoPhaseControls.second_tau",
        "ReasLib/Optimization/DFP/TwoPhaseControls.lean",
        56,
        "second phase line-ratio formula",
    ),
    "matrix-positive": decl(
        "TwoPhaseControls.matrix_posDef",
        "ReasLib/Optimization/DFP/TwoPhaseControls.lean",
        83,
        "positive definiteness of each phase matrix",
    ),
    "spectrum-range": decl(
        "TwoPhaseControls.spectrum_mem",
        "ReasLib/Optimization/DFP/TwoPhaseControls.lean",
        140,
        "spectral bounds for each phase matrix",
    ),
    "preconditioned-energy": decl(
        "DFP.AbstractSecantStep.preconditionedEnergy_pos",
        "ReasLib/Optimization/DFP/AbstractSecantStep.lean",
        151,
        "positivity of the preconditioned energy denominator",
    ),
    "secant-image-energy": decl(
        "DFP.AbstractSecantStep.secantImageEnergy_pos",
        "ReasLib/Optimization/DFP/AbstractSecantStep.lean",
        192,
        "positivity of the secant-image energy denominator",
    ),
    "next-gradient-eigenframe": decl(
        "DFP.AbstractSecantStep.nextGradient_eigenframe",
        "ReasLib/Optimization/DFP/AbstractSecantStep/Eigenframe.lean",
        83,
        "entrywise next-gradient formula in the eigenframe",
    ),
    "second-step-remainder": decl(
        "DFP.TwoLeg.NormJet.slowCurveSecondStepRemainder",
        "ReasLib/Optimization/DFP/TwoPhaseControls/NormJet.lean",
        3529,
        "second-step norm expansion remainder",
    ),
    "intermediate-gradient-remainder": decl(
        "DFP.TwoLeg.NormJet.slowIntermediateGradientRemainder",
        "ReasLib/Optimization/DFP/TwoPhaseControls/NormJet.lean",
        1590,
        "intermediate gradient-norm expansion remainder",
    ),
    "final-gradient-remainder": decl(
        "DFP.TwoLeg.NormJet.slowFinalGradientRemainder",
        "ReasLib/Optimization/DFP/TwoPhaseControls/NormJet.lean",
        1818,
        "final gradient-norm expansion remainder",
    ),
    "mixed-radius": decl(
        "DFP.TwoLeg.Mixed.radiusExpansion",
        "ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion.lean",
        2097,
        "mixed-variable radius expansion",
    ),
    "mixed-shape": decl(
        "DFP.TwoLeg.Mixed.shapeExpansion",
        "ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion.lean",
        2113,
        "mixed-variable shape expansion",
    ),
    "mixed-scale": decl(
        "DFP.TwoLeg.Mixed.scaleExpansion",
        "ReasLib/Optimization/DFP/TwoPhaseControls/MixedExpansion.lean",
        2128,
        "mixed-variable scale expansion",
    ),
    "mixed-amplitude": decl(
        "DFP.TwoLeg.Mixed.amplitudeExpansion",
        "ReasLib/Optimization/DFP/TwoPhaseControls/PhysicalDrift.lean",
        2578,
        "mixed-variable amplitude expansion",
    ),
    "mixed-frame": decl(
        "DFP.TwoLeg.Mixed.frameAngleExpansion",
        "ReasLib/Optimization/DFP/TwoPhaseControls/PhysicalDrift.lean",
        2615,
        "mixed-variable frame-angle expansion",
    ),
    "mixed-center": decl(
        "DFP.TwoLeg.Mixed.centerDisplacementExpansion",
        "ReasLib/Optimization/DFP/TwoPhaseControls/PhysicalDrift.lean",
        2652,
        "mixed-variable center-displacement expansion",
    ),
    "gradient-limit": decl(
        "DFP.TwoPhaseOrbit.slowCurveEndpointGradientNormTendsto",
        BASE + "Lemma_6_5_Positive_limiting_gradient_norm_at_every_endpoint.lean",
        13,
        "positive limiting endpoint gradient norm",
    ),
    "posdef": decl(
        "DFP.TwoPhaseOrbit.endpointMetric_posDef",
        BASE + "Lemma_6_6_Positive_definiteness_of_every_DFP_matrix.lean",
        12,
        "positive definiteness of every DFP matrix",
    ),
    "transport": decl(
        "DFP.IsOrbit.orthogonalSum",
        BASE + "Corollary_6_7_Extension_to_every_dimension_n_ge2.lean",
        17,
        "orthogonal direct-sum orbit transport",
    ),
    "norm-transport": decl(
        "orthogonalSumGradientNormTendsto_iff",
        BASE + "Corollary_6_7_Extension_to_every_dimension_n_ge2.lean",
        71,
        "preservation of gradient-norm limits under embedding",
    ),
    "valley": decl(
        "DFP.TwoLeg.NormJet.eventuallyStrictGradientNormValley",
        BASE + "Remark_6_8_Gradient_norms_are_not_eventually_monotone.lean",
        32,
        "strict within-cycle gradient-norm valley",
    ),
    "steps-diverge": decl(
        "DFP.TwoPhaseOrbit.slowCurveTotalStepLengthNotSummable",
        BASE + "Remark_6_9_The_total_step_length_diverges.lean",
        53,
        "non-summability of total step length",
    ),
    "appendix-entrywise": decl(
        "DFP.AbstractSecantStep.nextInverseHessian_eigenframe",
        BASE + "Appendix_Lemma_A_1_Entrywise_one_step_formulas.lean",
        10,
        "entrywise one-step formulas",
    ),
    "appendix-det": decl(
        "Matrix.det_inverseDFPUpdate",
        BASE + "Appendix_Lemma_A_2_Determinant_identity_for_the_one_step_map.lean",
        11,
        "DFP determinant identity",
    ),
    "appendix-state": decl(
        "DFP.TwoLeg.stateMap_apply",
        BASE + "Appendix_Proposition_A_5a_Exact_complete_two_leg_state_map.lean",
        95,
        "complete two-leg state map",
    ),
    "appendix-amplitude": decl(
        "DFP.TwoLeg.amplitudeRemainderOfSlowGraphJets",
        BASE + "Appendix_Lemma_A_7_Specialized_amplitude_expansion.lean",
        13,
        "specialized amplitude expansion",
    ),
    "appendix-angle": decl(
        "slowCurveFrameAngleExpansion",
        BASE + "Appendix_Lemma_A_8_Specialized_frame_angle_expansion.lean",
        18,
        "specialized frame-angle expansion",
    ),
    "appendix-center": decl(
        "DFP.TwoLeg.CenterJet.slowFullLowRemainder",
        BASE + "Appendix_Lemma_A_9_Specialized_center_displacement_expansion.lean",
        6,
        "specialized center-displacement expansion",
    ),
    "appendix-steps": decl(
        "DFP.TwoLeg.NormJet.slowCurveFirstStepRemainder",
        BASE + "Appendix_Lemma_A_11_Step_norm_expansions.lean",
        15,
        "step-norm expansion",
    ),
    "appendix-gradient": decl(
        "DFP.TwoLeg.NormJet.slowInitialGradientRemainder",
        BASE + "Appendix_Lemma_A_12_Gradient_norm_expansions.lean",
        13,
        "gradient-norm expansion",
    ),
}


BLOCK_KEYS = {
    "thm:main": ("main", "main-negation", "transport", "norm-transport"),
    "cor:identity-initialization": ("identity",),
    "prop:one-step": (
        "abstract-step", "line-ratio", "update-gradient", "update-hessian",
        "preconditioned-energy", "secant-image-energy",
    ),
    "lem:graph-transform": ("graph",),
    "lem:center-manifold": (
        "state-map", "state-linearization", "slow-curve", "recurrence",
    ),
    "lem:two-step-expansions": ("amplitude", "frame", "center", "half-center", "angle-first", "angle-second"),
    "lem:scalar-asymptotics": ("scalar", "circle"),
    "lem:separation": ("separation",),
    "lem:disjoint-interpolation": ("bump", "interpolation", "gradient-interpolation", "hessian"),
}


INLINE_LABELS = {
    "main counterexample": ("main",),
    "scalar and circle limits": ("scalar", "circle"),
    "uniform separation": ("separation",),
    "identity normalization": ("identity",),
    "dimension transport": ("transport", "norm-transport"),
    "paper-range counterexample": ("main", "main-negation"),
    "identity-initialized corollary": ("identity",),
    "nonmonotone gradient norms": ("valley",),
    "infinite total step length": ("steps-diverge",),
    "dfp iteration": ("dfp-iteration",),
    "weak wolfe": ("weak-wolfe",),
    "strong wolfe": ("strong-wolfe",),
    "global convergence predicate": ("global-predicate",),
    "level-set global convergence predicate": (
        "levelset-predicate", "levelset-negation",
    ),
    "all-dimensional transport": ("transport", "norm-transport"),
    "gradient norm transport": ("norm-transport",),
    "gradient-norm valley": ("valley",),
    "non-summable step lengths": ("steps-diverge",),
    "negative global-convergence result": ("main-negation",),
    "unbounded frame winding": ("frame-winding",),
    "realized objective": ("objective",),
    "line-ratio identity": ("line-ratio",),
    "abstract secant step": ("abstract-step",),
    "canonical cycle state": ("cycle-state", "cycle-spec"),
    "two-phase controls": (
        "controls", "first-matrix", "first-tau", "second-matrix", "second-tau",
        "matrix-positive", "spectrum-range",
    ),
    "exact infinite orbit": ("orbit",),
    "limiting circle": ("circle",),
    "bump correction": ("bump",),
    "global realized objective": ("objective",),
    "global hessian bounds": ("hessian",),
    "strong convexity": ("convexity",),
    "endpoint interpolation": ("interpolation", "gradient-interpolation"),
    "realized dfp orbit": ("realized-orbit",),
    "exact decrease ratio": ("decrease",),
    "armijo verification": ("armijo",),
    "curvature verification": ("curvature",),
    "cycle state specification": ("cycle-spec",),
    "two-phase matrix and ratio formulas": (
        "first-matrix", "first-tau", "second-matrix", "second-tau",
        "matrix-positive", "spectrum-range",
    ),
    "entrywise DFP formulas": (
        "appendix-entrywise", "next-gradient-eigenframe",
    ),
    "mixed-variable expansions": (
        "mixed-radius", "mixed-shape", "mixed-scale", "mixed-amplitude",
        "mixed-frame", "mixed-center",
    ),
    "mixed physical drift expansions": (
        "mixed-amplitude", "mixed-frame", "mixed-center",
    ),
    "second-step expansion": ("second-step-remainder",),
    "intermediate gradient expansion": ("intermediate-gradient-remainder",),
    "final gradient expansion": ("final-gradient-remainder",),
    "positive gradient limit": ("gradient-limit",),
    "positive dfp matrices": ("posdef",),
    "identity initialization": ("identity",),
    "identity-initialized certificate": ("identity",),
    "entrywise dfp formulas": (
        "appendix-entrywise", "next-gradient-eigenframe",
    ),
    "dfp determinant identity": ("appendix-det",),
    "complete two-leg state map": ("appendix-state",),
    "amplitude expansion": ("appendix-amplitude",),
    "frame-angle expansion": ("appendix-angle",),
    "center-displacement expansion": ("appendix-center",),
    "step and gradient expansions": (
        "appendix-steps", "second-step-remainder",
    ),
    "gradient-norm expansions": (
        "appendix-gradient", "intermediate-gradient-remainder",
        "final-gradient-remainder",
    ),
}


def strip_comments(line: str) -> str:
    escaped = False
    for i, ch in enumerate(line):
        if ch == "%" and not escaped:
            return line[:i]
        escaped = ch == "\\" and not escaped
        if ch != "\\":
            escaped = False
    return line


def clean_inline(text: str) -> str:
    text = re.sub(r"\\lean(?:DeclTagExtra|DeclTag|ClaimTag)\s*\{[^{}]*\}(?:\s*\{[^{}]*\}){1,2}", " ", text)
    text = re.sub(r"\\(?:cite|ref|eqref|label|pageref)\s*\{[^{}]*\}", " [reference] ", text)
    text = re.sub(r"\\(?:textbf|textit|texttt|emph|underline)\s*\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:footnote|thanks)\s*\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z]+\*?(?:\[[^]]*\])?", " ", text)
    text = re.sub(r"\$[^$\n]*\$", " [math] ", text)
    text = text.replace("&", " ").replace("\\\\", " ")
    text = text.replace("{", " ").replace("}", " ").replace("~", " ")
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> list[str]:
    out: list[str] = []
    start = 0
    for i, ch in enumerate(text):
        if ch not in ".?!":
            continue
        if ch == "." and re.search(r"(?:e|i|eg|ie|fig|sec|app)$", text[:i].strip(), re.I):
            continue
        if i + 1 < len(text) and not text[i + 1].isspace():
            continue
        part = text[start : i + 1].strip()
        if len(part) >= 16:
            out.append(part)
        start = i + 1
    tail = text[start:].strip()
    if len(tail) >= 24:
        out.append(tail)
    return out


def section_name(title: str, current: str) -> str:
    low = title.lower()
    tests = (
        ("introduction", "introduction"),
        ("classical dfp question", "statement"),
        ("overview of the construction", "strategy"),
        ("construction of a nonconvergent", "alternating-sequence"),
        ("construction of a uniformly convex", "global-objective"),
        ("verification of the counterexample", "completion"),
        ("numerical experiments", "numerics"),
        ("conclusion", "conclusion"),
        ("algebraic verification", "app-algebra"),
    )
    for needle, name in tests:
        if needle in low:
            return name
    return current


def validate_decl(d: Decl) -> None:
    path = ROOT.parent / d.file
    if not path.is_file():
        raise SystemExit(f"missing Lean source: {d.file}")
    lines = path.read_text(encoding="utf-8").splitlines()
    total = len(lines)
    if not 1 <= d.line <= total:
        raise SystemExit(f"invalid line {d.line} in {d.file} (1..{total})")
    leaf = d.name.rsplit(".", 1)[-1]
    window = "\n".join(lines[max(0, d.line - 2): min(total, d.line + 2)])
    if leaf not in window:
        raise SystemExit(
            f"declaration {d.name} is not near line {d.line} in {d.file}"
        )


def validate_source_anchor(file: str, line: int) -> None:
    """Ensure every TeX source link names a real file and line."""
    path = ROOT.parent / file
    if not path.is_file():
        raise SystemExit(f"missing Lean source anchor: {file}")
    total = len(path.read_text(encoding="utf-8").splitlines())
    if not 1 <= line <= total:
        raise SystemExit(f"invalid Lean source anchor {line} in {file} (1..{total})")


def lean_records(keys: tuple[str, ...]) -> list[dict[str, object]]:
    result = []
    for key in keys:
        d = DECLS[key]
        result.append({
            "declaration": d.name,
            "file": d.file,
            "line": d.line,
            "relation": d.relation,
            "snapshot": SNAPSHOT,
        })
    return result


def stable_id(section: str, line: int, text: str, occurrence: int) -> str:
    value = f"{section}\n{line}\n{occurrence}\n{text}"
    return "S-" + hashlib.sha1(value.encode("utf-8")).hexdigest()[:12]


def main() -> None:
    source = TEX.read_text(encoding="utf-8")
    for d in DECLS.values():
        validate_decl(d)
    lines = source.splitlines()

    # Every theorem-like environment is a formal statement anchor.  The map is
    # keyed by the TeX label, so the identity survives line movement.
    statement_anchors: list[dict[str, object]] = []
    for m in re.finditer(
        r"\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[([^]]*)\])?",
        source,
    ):
        line = source.count("\n", 0, m.start()) + 1
        end = re.search(r"\\end\{" + re.escape(m.group(1)) + r"\}", source[m.end() :])
        block = source[m.end() : m.end() + (end.start() if end else 0)]
        label_match = re.search(r"\\label\{([^}]*)\}", block)
        label = label_match.group(1) if label_match else None
        title = m.group(2) or m.group(1)
        keys = BLOCK_KEYS.get(label or "", ())
        statement_anchors.append({
            "id": label or f"unlabeled-{line}",
            "kind": m.group(1),
            "title": title,
            "tex_line": line,
            "label": label,
            "lock": "lean" if keys else "review",
            "lean": lean_records(keys),
            "boundary_reason": None if keys else "no reviewed declaration map for this statement",
        })

    # Explicit inline tags are separate anchors.  They are not expanded to an
    # entire paragraph, which prevents one link from falsely certifying nearby
    # sentences.
    inline_anchors: list[dict[str, object]] = []
    for m in re.finditer(
        r"\\leanDeclTag(?:Extra)?\s*\{([^{}]*)\}\s*\{(\d+)\}",
        source,
    ):
        validate_source_anchor(m.group(1), int(m.group(2)))
    for m in re.finditer(
        r"\\leanClaimTag\s*\{([^{}]*)\}\s*\{([^{}]*)\}\s*\{(\d+)\}",
        source,
    ):
        line = source.count("\n", 0, m.start()) + 1
        label = m.group(1)
        validate_source_anchor(m.group(2), int(m.group(3)))
        keys = INLINE_LABELS.get(label.lower(), ())
        inline_anchors.append({
            "id": f"inline-{line}-{label.lower().replace(' ', '-')}",
            "label": label,
            "tex_line": line,
            "lock": "lean" if keys else "review",
            "lean": lean_records(keys),
            "source_file": m.group(2),
            "source_line": int(m.group(3)),
            "boundary_reason": None if keys else "unrecognized inline correspondence label",
        })

    # Prose inventory.  Unlike the first bootstrap pass, this walk includes
    # theorem statements, proof explanations, and figure/table captions.  A
    # sentence is marked `lean` only when it is inside a mapped theorem block
    # or is adjacent to an explicit `leanClaimTag`; all other prose keeps an
    # auditable boundary status.
    sentence_records: list[dict[str, object]] = []
    paragraph_records: list[dict[str, object]] = []
    current_section = "introduction"
    paragraph: list[tuple[int, str]] = []
    env_stack: list[str] = []
    env_labels: list[str | None] = []
    math_delimited = False
    occurrence: dict[str, int] = {}
    theorem_envs = {"theorem", "lemma", "proposition", "corollary"}
    structural_envs = {"abstract"}
    skip_envs = {
        "equation", "equation*", "align", "align*", "gather", "gather*",
        "multline", "multline*", "displaymath", "math", "figure", "table",
        "tabular", "tabular*", "center", "array", "aligned", "alignedat",
        "gathered", "split", "cases", "matrix", "pmatrix", "bmatrix",
        "Bmatrix", "vmatrix", "Vmatrix", "smallmatrix", "thebibliography",
    }

    def context_info() -> tuple[str, str | None]:
        if "proof" in env_stack:
            return "proof", None
        for index in range(len(env_stack) - 1, -1, -1):
            if env_stack[index] in theorem_envs:
                return "theorem", env_labels[index]
        if "abstract" in env_stack:
            return "abstract", None
        if env_stack:
            return "embedded", None
        return "prose", None

    def flush() -> None:
        nonlocal paragraph
        if not paragraph:
            return
        raw = " ".join(value for _, value in paragraph)
        cleaned = clean_inline(raw)
        context, statement_label = context_info()
        keys = BLOCK_KEYS.get(statement_label or "", ()) if context == "theorem" else ()
        lean = lean_records(keys)
        indices: list[int] = []
        for sentence in split_sentences(cleaned):
            key = f"{current_section}\n{sentence}"
            n = occurrence.get(key, 0)
            occurrence[key] = n + 1
            if current_section == "numerics":
                category, reason = "empirical", "numerical or figure/table evidence"
            elif "\\cite" in raw:
                category, reason = "citation", "claim about external literature"
            elif context == "proof":
                category, reason = "proof-prose", "proof explanation without a sentence-level declaration"
            elif context == "theorem":
                category, reason = "formal-statement", "theorem block has no reviewed declaration map"
            else:
                category, reason = "editorial", "prose without an explicit Lean claim anchor"
            if context == "prose" and (
                "[math]" in sentence
                or re.search(
                    r"\b(?:gradient|hessian|dfp|wolfe|converge|convergence|uniformly convex|eigen|interpolat|orbit|asymptot|matrix)\b",
                    sentence,
                    re.I,
                )
            ):
                category = "unmapped-claim"
                reason = "mathematical sentence has no explicit Lean claim anchor"
            if "hessian identity follows" in sentence.lower():
                category = "review-boundary"
                reason = "no standalone named Lean declaration for the pointwise identity ∇²f(xₖ)=I"
            lock = "lean" if lean else "boundary"
            record = {
                "id": stable_id(current_section, paragraph[0][0], sentence, n),
                "line_start": paragraph[0][0],
                "line_end": paragraph[-1][0],
                "section": current_section,
                "context": context,
                "text": sentence,
                "category": category,
                "lock": lock,
                "lean": lean.copy(),
                "anchor_ids": [],
                "boundary_reason": None if lean else reason,
            }
            indices.append(len(sentence_records))
            sentence_records.append(record)
        paragraph_records.append({
            "line_start": paragraph[0][0],
            "line_end": paragraph[-1][0],
            "section": current_section,
            "context": context,
            "statement_label": statement_label,
            "sentence_indices": indices,
        })
        paragraph = []

    in_document = False
    for lineno, original in enumerate(lines, 1):
        if "\\begin{document}" in original:
            in_document = True
            continue
        if not in_document:
            continue
        if "\\begin{thebibliography}" in original:
            flush()
            break
        raw = strip_comments(original)
        heading = re.match(r"\s*\\section\*?\{([^{}]*)\}", raw)
        if heading:
            flush()
            current_section = section_name(heading.group(1), current_section)
            continue
        if re.match(r"\s*\\subsection", raw):
            flush()
            continue

        # Display math can use `\[...\]` rather than a named environment.
        # Keep it out of prose paragraphs while retaining the surrounding
        # explanatory sentences for sentence-level locks.
        if math_delimited:
            if r"\]" in raw or raw.strip().endswith("$$"):
                math_delimited = False
            continue
        if re.match(r"\s*\\\[", raw) or raw.strip().startswith("$$"):
            flush()
            math_delimited = True
            if r"\]" in raw[raw.find("\\[") + 2:] or (
                raw.strip().endswith("$$") and len(raw.strip()) > 2
            ):
                math_delimited = False
            continue

        begin = re.match(r"\s*\\begin\{([^}]+)\}", raw)
        if begin:
            env = begin.group(1)
            if env in theorem_envs or env == "proof" or env in skip_envs \
                    or env in structural_envs:
                flush()
                # Matrix/alignment environments are often opened and closed
                # on one source line; do not leave a stale skip frame in that
                # case.
                if re.search(rf"\\end\{{{re.escape(env)}\}}", raw[begin.end():]):
                    continue
                label_match = re.search(r"\\label\{([^}]*)\}", raw)
                env_stack.append(env)
                env_labels.append(label_match.group(1) if label_match else None)
                continue

        end = re.match(r"\s*\\end\{([^}]+)\}", raw)
        if end:
            env = end.group(1)
            if env_stack and env_stack[-1] == env:
                flush()
                env_stack.pop()
                env_labels.pop()
                continue

        if env_stack and env_stack[-1] in skip_envs:
            continue

        # A theorem label can be on its own line after the environment begins.
        if env_stack and env_stack[-1] in theorem_envs and env_labels[-1] is None:
            label_match = re.search(r"\\label\{([^}]*)\}", raw)
            if label_match:
                env_labels[-1] = label_match.group(1)

        if raw.lstrip().startswith("\\lean"):
            flush()
            continue
        if not raw.strip():
            flush()
            continue
        paragraph.append((lineno, raw))
    flush()

    # Captions are prose even though their surrounding figure/table is omitted
    # from the converter-compatible PaperForge draft.  Keep them as empirical
    # boundary records so the inventory does not silently lose their claims.
    for match in re.finditer(r"\\caption(?:\[[^]]*\])?\{([^{}]*)\}", source):
        line = source.count("\n", 0, match.start()) + 1
        cleaned = clean_inline(match.group(1))
        for sentence in split_sentences(cleaned):
            key = f"numerics\n{sentence}"
            n = occurrence.get(key, 0)
            occurrence[key] = n + 1
            sentence_records.append({
                "id": stable_id("numerics", line, sentence, n),
                "line_start": line,
                "line_end": line,
                "section": "numerics",
                "context": "caption",
                "text": sentence,
                "category": "empirical",
                "lock": "boundary",
                "lean": [],
                "anchor_ids": [],
                "boundary_reason": "figure or table caption is computational evidence",
            })

    # Bind each explicit inline tag to the nearest prose paragraph.  This keeps
    # the lock local to the sentence(s) the author marked, rather than granting
    # an entire surrounding section a declaration by proximity alone.
    for anchor in inline_anchors:
        line = int(anchor["tex_line"])
        preceding = [
            paragraph for paragraph in paragraph_records
            if paragraph["sentence_indices"]
            and int(paragraph["line_end"]) < line
            and line - int(paragraph["line_end"]) <= 4
        ]
        # Tags are authored after the claim they certify.  Prefer the nearest
        # preceding paragraph; do not attach a formula-only tag to unrelated
        # prose that happens to follow it.
        nearest = max(preceding, key=lambda p: int(p["line_end"]), default=None)
        if nearest is None:
            anchor["sentence_ids"] = []
            continue
        # Select the sentence(s) whose wording actually matches the label.
        # A tag after a long paragraph must not certify every unrelated claim
        # in that paragraph by mere physical proximity.
        indices = list(nearest["sentence_indices"])
        label_terms = [
            term.rstrip("s") for term in re.findall(r"[a-z]+", str(anchor["label"]).lower())
            if term not in {"and", "the", "of", "for", "with", "to", "a", "an", "in", "on"}
        ]
        scored = []
        for index in indices:
            text = str(sentence_records[index]["text"]).lower()
            score = sum(term in text for term in label_terms)
            if re.search(r"\b(?:do not|does not|not assert|leave open)\b", text):
                score -= 2
            scored.append((score, index))
        best_score = max((score for score, _ in scored), default=0)
        if best_score > 0:
            selected = [index for score, index in scored if score == best_score]
        else:
            selected = indices[-1:] if indices else []
        sentence_ids: list[str] = []
        for index in selected:
            record = sentence_records[index]
            if anchor["lock"] == "lean":
                record["lock"] = "lean"
                record["category"] = "formal-claim"
                record["lean"] = list(anchor["lean"])
                record["boundary_reason"] = None
                record["anchor_ids"].append(anchor["id"])
                sentence_ids.append(record["id"])
        anchor["sentence_ids"] = sentence_ids

    # Theorem anchors own all sentence records emitted from their theorem block.
    for anchor in statement_anchors:
        sentence_ids = [
            record["id"] for record in sentence_records
            if record.get("context") == "theorem"
            and record.get("section")
            and anchor.get("label")
            and any(
                paragraph["statement_label"] == anchor["label"]
                and index < len(sentence_records)
                and sentence_records[index]["id"] == record["id"]
                for paragraph in paragraph_records
                for index in paragraph["sentence_indices"]
            )
        ]
        anchor["sentence_ids"] = sentence_ids

    counts: dict[str, int] = {}
    for rec in sentence_records:
        key = f"{rec['category']}:{rec['lock']}"
        counts[key] = counts.get(key, 0) + 1
    manifest = {
        "schema_version": 3,
        "source": {
            "file": "DFP_counterexample/main.tex",
            "sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
            "snapshot_commit": SNAPSHOT,
        },
        "policy": {
            "statement_lock": "Every labeled theorem-like environment and every explicit leanClaimTag is locked to one or more reviewed Lean declarations.",
            "sentence_lock": "A sentence receives a Lean lock only from its mapped theorem block or its nearest explicit claim tag; all other sentences retain a boundary lock.",
            "prose_boundary": "Citation, empirical, proof-explanatory, and editorial text is retained with an explicit boundary category; it is not silently presented as a Lean theorem.",
            "stable_identity": "Sentence IDs are content hashes; statement IDs are TeX labels.",
        },
        "counts": {
            **counts,
            "statement_anchors": len(statement_anchors),
            "inline_anchors": len(inline_anchors),
        },
        "total_sentences": len(sentence_records),
        "coverage": {
            "included_contexts": ["abstract", "prose", "theorem", "proof", "caption"],
            "excluded_content": [
                "display-math bodies (the displayed formula remains in its anchor record)",
                "bibliography entries after the thebibliography environment",
                "preamble and author metadata",
            ],
            "inline_anchors_with_sentence_ids": sum(
                bool(anchor.get("sentence_ids")) for anchor in inline_anchors
            ),
            "inline_anchors_without_sentence_ids": sum(
                not bool(anchor.get("sentence_ids")) for anchor in inline_anchors
            ),
            "unmapped_claim_count": sum(
                record["category"] == "unmapped-claim"
                for record in sentence_records
            ),
        },
        "sentences": sentence_records,
        "statement_anchors": statement_anchors,
        "inline_anchors": inline_anchors,
    }
    OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUT),
        "sentences": len(sentence_records),
        "statement_anchors": len(statement_anchors),
        "inline_anchors": len(inline_anchors),
        "counts": counts,
    }, indent=2))


if __name__ == "__main__":
    main()
