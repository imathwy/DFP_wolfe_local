# Final Aggregate Check Report

Audit date: 2026-08-30. All checks below were run serially with `lake lean`
after the last source edit. No source writer or batch compiler was active during
the final pass.

## Frozen Source Set

| File | SHA256 | Check |
|---|---|---|
| `ReasLib/Optimization/DFP/GlobalConvergence.lean` | `8fd4d4e38487eaf97a53ac3214f23e229d4cc06bbff6385bb9db30c42514620f` | RC0 |
| `ReasLib/Optimization/DFP/TwoPhaseOrbit/ParameterizedWolfe.lean` | `54e3ca6f5e525a5e4e6f44405a080afb594327a739714eca8f01c5951979a749` | RC0 |
| `ReasLib/Optimization/DFP/StrongWolfeCounterexample.lean` | `94b2257e2e0f21891a4153d7b8d5f870d0c3c21f726519db580969d6a66a6d1a` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/IdentityInitialization.lean` | `5a6b522b6ce6f3006518dbd2cd3f4d8ad1957c529e971c313db0e20885be4817` | RC0 |
| `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_2_3_Uniformly_convex_weak_Wolfe_DFP_counterexample_in_dimension_two.lean` | `8ffbb46fe7b1cdf0ad83362d094f00c76f8ec58f7a1e98a46cacf424d9f19560` | RC0 |
| `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_2_4_Counterexample_in_every_dimension_n_ge2.lean` | `a9d5346598c3647abe5c03f7f272a2d97e679e392dbaad0236de3fc625f8481a` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedPlanar.lean` | `30ddd393c2f781da9d448c7baedecc7d10bdc031ed97bda98862028a924f5b8c` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedTransport.lean` | `bf27728d35dca9aa1070fa1a5ffcaa16933581697d5d0698b700caa3e8e69a62` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/ParameterizedIdentityInitialization.lean` | `2cf311f589d86f093838194827e5c1a9020252a0bcbf72b8da48ab09db536f03` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/AutomaticIdentityFactor.lean` | `7705dad88d72f802de8a435953e192a9c53cc744596712993c373c74e210cac9` | RC0 |
| `ReasLib/Optimization/DFP/LevelSetGlobalConvergence.lean` | `f6cf28c58d611bffc974964f04cd4f9c39a30dc20157935288902c36a66942c4` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/SemanticProjections.lean` | `9d43ac937978f354d82930d4770e25ae8d88e2a8424ea8a82bc06bd9989cba30` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/MatrixIdentityInitialization.lean` | `52c590bbc3d108af027b99623bdd2ad85d4d13553de844d091f84c66e0f7d5cf` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/MatrixIdentityLiminfCertificate.lean` | `ba689c5fac82cf4d71c5f9ee73a4f0dd5d82b8bc3902f39b07f8b4fa667632fc` | RC0 |
| `ReasLib/Optimization/DFP/WolfeCounterexample/AutomaticMatrixIdentityLiminf.lean` | `6999c15bd34485904cf0bf9145c665990bfc399a062e4e75a899afcd54b05f9a` | RC0 |
| `DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean` | `7d6cc3d0ca5c1910a719659078bb35fbc0609547a83334f35c9bd04ff3d71037` | RC0 |
| `DFPWolfe.lean` | `6f12fc459a67ef681da77a57b11cbe28858747e0ef39b7af78f8c5180c99cc99` | RC0 |

The checks were run in dependency order, ending with Main and the top-level
facade. Warnings are inherited style, unused-variable, deprecation, or module
header warnings; there were no Lean errors.

## Export And Axiom Probe

An ephemeral source importing only `DFPWolfe` resolved these final names:

```text
DFP.main_not_globalWeakWolfeConvergence_of_parameterRange
DFP.main_not_globalWeakWolfeConvergence_forall_parameterRange
DFP.main_not_levelSetGlobalWeakWolfeConvergence_of_parameterRange
DFP.main_not_levelSetGlobalWeakWolfeConvergence_forall_parameterRange
DFP.not_PaperRangeGlobalWeakWolfeConvergence
DFP.not_PaperRangeLevelSetGlobalWeakWolfeConvergence
DFP.existsMatrixIdentityLiminfStrongWolfe_of_parameterRange
```

The probe also resolved the matrix certificate projection
`DFP.WolfeCounterexample.MatrixIdentityLiminfStrongWolfeCertificate.gradientNorm_liminf_pos`.
An application probe instantiated the global and level-set negative theorems and
the matrix existential at `(n, c₁, c₂) = (2, 1/4, 3/4)`; it returned RC0.
`#print axioms` on the per-pair, literal-negation, and matrix declarations
reported only:

```text
[propext, Classical.choice, Quot.sound]
```

The temporary probe was deleted. Production files contain no `#check` or
`#print` commands.

## Debt Scan

The release slice above has no executable `sorry`, `admit`, `sorryAx`, or
project-defined `axiom`. The only textual matches for `admit` are ordinary
English prose such as “admits a certificate”. No new helper contains a
prohibited embedded proof fragment; proof obligations in the automatic matrix
producer are named local facts.

## What Is Proved

For every

```text
0 < c₁ < 2 / 3,   2 / 3 ≤ c₂ < 1,   n ≥ 2,
```

there is a strong-Wolfe counterexample with global Hessian bounds
`[1/2, 3/2]`, positive steps, a well-defined classical DFP orbit, and gradient
norms converging to a positive limit. Because the strong certificate contains
the legacy weak-Wolfe field, Main proves the check-friendly negative statement

```text
¬ GlobalWeakWolfeConvergenceAt c₁ c₂
```

for each pair. The fixed `(1/4, 3/4)` aliases remain for compatibility.

The level-set API uses the initial sublevel set
`{z | f z ≤ f (point 0)}` and restricts Hessian bounds to that set. Its
admissibility predicate explicitly records trajectory containment; the bridge
proves containment from `PosDef`, positive steps, the DFP recurrence, and
Armijo monotonicity. Main exports the corresponding per-pair and paper-range
negative theorems.

The identity-initialization result is now genuinely matrix-facing. The
automatic factor producer takes the initial matrix `PosDef`, constructs its
square-root coordinate change and positive distortion constants, transports the
orbit, proves strict secant curvature and an eventual upper/lower gradient tail,
and constructs a classical matrix `InverseIteration`. Main exports:

```text
∃ m M, 0 < m ∧ m ≤ M ∧
  Nonempty (MatrixIdentityLiminfStrongWolfeCertificate n m M c₁ c₂)
```

The certificate has `H₀ = I`, global problem-dependent Hessian bounds, strong
Wolfe steps, and exactly the paper-facing `0 < liminf ‖∇f(xₖ)‖` conclusion.
No exact transformed gradient-norm limit is assumed.

## Semantic Boundary

`GlobalWeakWolfeConvergenceAt` remains the reusable global-Hessian predicate;
`LevelSetGlobalWeakWolfeConvergenceAt` is the paper-faithful relevant-level-set
variant. The negative theorem is stated for weak Wolfe because that is the open
question, while the witness is stronger (strong Wolfe). The literal negation
wrappers `not_PaperRangeGlobalWeakWolfeConvergence` and
`not_PaperRangeLevelSetGlobalWeakWolfeConvergence` are convenient shortest
checks, while the `main_not_*_forall_parameterRange` declarations retain the
stronger statement that every pair in the range fails.

The release intentionally follows the paper's proven scope
`0 < c₁ < 2/3`, `2/3 ≤ c₂ < 1`, and `C²` regularity. The paper leaves the
`c₂ < 2/3` and smoother-than-`C²` variants open; no Lean declaration silently
claims those stronger extensions.

## Effort And Handoff

The requested semantic and representation work is complete. Remaining effort is
only optional cleanup of inherited warnings and documentation, estimated at
`0.25-0.5` engineer-day. A separate `GlobalStrongWolfeConvergenceAt` predicate
would be an optional API and is not needed for the refutation.

The automatic matrix producer handoff is in
[`TASK-16-automatic-matrix-identity-liminf.md`](TASK-16-automatic-matrix-identity-liminf.md).
The semantic-fidelity details and paper line mapping are in
[`TASK-15-semantic-fidelity-audit.md`](TASK-15-semantic-fidelity-audit.md).
