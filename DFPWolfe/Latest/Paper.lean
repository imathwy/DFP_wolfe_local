/-
Copyright (c) 2026 Zichen Wang. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Zichen Wang
-/
module

public import DFPWolfe.Latest.Theorem_1_StrongWolfeCounterexample
public import DFPWolfe.Latest.Corollary_2_IdentityInitialization
public import DFPWolfe.Latest.Theorem_3_PlanarConvergence
public import DFPWolfe.Latest.Lemma_4_PolarContinuation
public import DFPWolfe.Latest.Lemma_5_PolarGeometry
public import DFPWolfe.Latest.Lemma_6_PolarInterpolation
public import DFPWolfe.Latest.Lemma_7_PlanarSecantDegeneration
public import DFPWolfe.Latest.Sequences
public import DFPWolfe.Latest.Proposition_8_CenterManifold

/-!
# DFP counterexample — the general polar construction

This entry follows the latest `arXiv.tex`: Theorem 1, Corollary 2,
Theorem 3, Lemmas 4–7 and the independent Proposition 8, together with the
unnumbered comparisons on the same actual Wolfe orbit. Both Wolfe parameters
and the Hessian Hölder exponent
range over their full admissible intervals. The quantitative identity
normalization and all-dimensional extension retain the prescribed source data.

The earlier center-manifold and fixed-exponent polar constructions remain
available through `DFPWolfe.Paper` and `DFPWolfe.V21.Paper`. The latest
manuscript has eight numbered results and restores the independent
center-manifold section. Its endpoint-value Wolfe estimates are proved without
separation hypotheses; the interpolation entry retains the stated disjoint-ball
condition. See `DFPWolfe/Latest/README.md` for correspondence.
-/
