# TASK-02: Parameterized Wolfe range

## Objective

Lift the current fixed `(c₁,c₂) = (1/4,3/4)` endpoint estimates to the paper's
range

```text
0 < c₁ < 2/3,    2/3 ≤ c₂ < 1.
```

This is the main mathematical gap between the current Lean endpoint and the
paper's Main theorem. It is not just a theorem-header change: the current
`phaseDecreaseRatioLowerBound`/`endpointArmijo` APIs expose only a `1/2` ratio
and `c₁ = 1/4`.

## Ownership

Write only this new companion module:

```text
ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean
```

Keep the existing `TwoPhaseOrbit/Wolfe.lean` APIs unchanged. Do not edit the
paper-facing Theorem 2.3/2.4 files; Task 06 will integrate the new declarations.

## Required deliverables

1. A parameterized Armijo/decrease-ratio theorem whose hypotheses explicitly
   contain `0 < c₁` and `c₁ < 2/3`.
2. A parameterized endpoint strong-curvature theorem for `2/3 ≤ c₂`, using the
   exact phase ratios `1/3` and `2/3` where possible.
3. Adapters in the exact shape needed by `LineSearch.IsWeakWolfe` and, if the
   strong predicate is exposed by Task 03, its endpoint shape as well.
4. A short note in the handoff explaining whether the proof uses the asymptotic
   limits from `main-new.tex` or only a conservative lower bound. A conservative
   `1/4` theorem is not sufficient for this task.

## Proof guidance

- Prefer existing ratio/limit lemmas and a uniform small-scale choice depending
  on `c₁`; do not hard-code `1/8` or `1/4` in the new parameterized API.
- Reuse `strongCurvature_of_tau_values` and the existing line-ratio facts instead
  of reconstructing the DFP algebra.
- Keep the construction interfaces abstract. Do not unfold the realized objective
  or the full two-phase orbit in a new main proof.
- If a required asymptotic lemma is missing, report its exact statement and stop
  rather than weakening the target to the fixed case.

## Acceptance criteria

- `lake lean ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean`
  returns zero.
- No placeholders or project axioms.
- The API is usable by a later planar theorem without changing existing certificate
  definitions.
- Include source hash and a minimal example invocation in the handoff.

## Dependencies and estimate

Independent of Tasks 01, 03, and 04 at the file level. It reads
`TwoPhaseOrbit/Wolfe.lean`, `TwoPhaseControls/LineRatio.lean`, and the abstract
secant Wolfe modules. Estimated human effort: **1--3 working days**; use the upper
end if the asymptotic Armijo estimate needs to be rebuilt rather than adapted.

## Handoff

Implemented in `ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean`.

- Frozen SHA256: `54e3ca6f5e525a5e4e6f44405a080afb594327a739714eca8f01c5951979a749`.
- Target check: `lake lean ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean`, RC0;
  only an unused-argument warning remains.
- The Armijo result takes `0<c₁<2/3`; endpoint weak/strong curvature takes
  `2/3≤c₂<1` and uses exact phase ratios `1/3` and `2/3`.
- The construction uses exposed asymptotic uniform bounds with a margin-dependent
  small-scale choice; it does not hard-code `1/4`.
- No placeholders, project axioms, `#check`, or `#print` remain.
