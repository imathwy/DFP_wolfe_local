# Final-conclusion parallel work packages

This directory splits the remaining work after comparing `main-new.tex` with the
current Lean endpoint. Each task has a separate Markdown brief so it can be handed
to another session without reconstructing the context.

## Recommended waves

| Wave | Tasks | Can run together? | Result |
|---|---|---|---|
| 1 | `TASK-01`, `TASK-02`, `TASK-03`, `TASK-04`, `TASK-05` | Yes, with the ownership rules below | New predicates/adapters, parameterized APIs, identity corollary, and a coverage report |
| 2 | `TASK-06` | After the relevant Wave 1 outputs are frozen | Main theorem and top-level facade wiring |
| 3 | `TASK-07` | After Task 06 | One clean aggregate check and axiom/debt audit |
| 4 | `TASK-08`, `TASK-09`, `TASK-10` | Design/audit can run together; writes are isolated | Paper-faithful parameterized planar, all-dimensional, and identity-initialized certificates |
| 5 | `TASK-11` | After the Wave 4 theorem names are frozen | Public parameterized API and explicit quantifier-facing Main theorem |
| 6 | `TASK-12` | After Task 11 | Final parameterized aggregate check and effort/status report |
| 7 | `TASK-13` | Read-only follow-up after Task 12 | Identity matrix/spectral bridge audit and effort refinement |
| 8 | `TASK-15`, `TASK-16` | After Tasks 13--14 | Semantic-fidelity audit, level-set containment, and automatic matrix-liminf release |

Task 05 is read-only with respect to Lean source. Tasks 01--04 must write only
their new companion files. Task 06 is the only task allowed to edit the existing
Main wrapper or `DFPWolfe.lean`. Task 07 must not edit source files. In Wave 4,
each of Tasks 08--10 owns one new file; no task may edit another task's file.
Task 11 is the only Wave 4 task allowed to edit the existing Main wrapper or
`DFPWolfe.lean`, and Task 12 is read-only.

## Wave 1 status

| Task | Status | Frozen deliverable |
|---|---|---|
| `TASK-01` | complete | `GlobalConvergence.lean`, RC0, SHA `8fd4d4e3...` |
| `TASK-02` | complete | `ParameterizedWolfe.lean`, RC0, SHA `54e3ca6f...` |
| `TASK-03` | complete | `StrongWolfeCounterexample.lean`, RC0, SHA `94b2257e...` |
| `TASK-04` | complete | `IdentityInitialization.lean`, RC0, SHA `5a6b522b...` |
| `TASK-05` | complete | `FINAL_CONCLUSION_COVERAGE_REPORT.md` |

## Wave 2 and 3 status

| Task | Status | Frozen deliverable |
|---|---|---|
| `TASK-06` | complete | Main wrapper + minimal `DFPWolfe.lean`, both RC0 |
| `TASK-07` | complete | `FINAL_AGGREGATE_CHECK_REPORT.md`, export and axiom audit |
| `TASK-08` | complete | Parameterized planar strong-Wolfe certificate (new file only) |
| `TASK-09` | complete | All-dimensional transport of the parameterized certificate (new file only) |
| `TASK-10` | complete | Parameterized identity-initialization corollary (new file only) |
| `TASK-11` | complete | Public parameterized Main/facade wiring |
| `TASK-12` | complete | Final parameterized aggregate audit |
| `TASK-13` | complete | Identity matrix/spectral bridge audit |
| `TASK-14` | complete | Automatic identity factor/map package |
| `TASK-15` | complete | Semantic-fidelity audit, level-set containment, and final matrix-liminf integration |
| `TASK-16` | complete | Automatic matrix identity-liminf producer and handoff |

## Current endpoint, as of 2026-08-30

- The paper asks the weak-Wolfe global-convergence question and states a stronger
  strong-Wolfe counterexample for every `0 < c₁ < 2/3`, `2/3 ≤ c₂ < 1`:
  [`main-new.tex`](../../main-new.tex:219).
- The reusable certificate currently stores global Hessian bounds, a positive-step
  DFP orbit, **weak** Wolfe only, and a positive gradient-norm limit:
  [`WolfeCounterexample.lean`](../../ReasLib/Optimization/DFP/WolfeCounterexample.lean:24).
- The legacy planar and all-dimensional endpoint theorems specialize to
  `(c₁,c₂) = (1/4,3/4)`; the new TASK-08/09 modules provide the full symbolic
  coefficient range:
  [`Theorem_2_3...lean`](../../DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_2_3_Uniformly_convex_weak_Wolfe_DFP_counterexample_in_dimension_two.lean:27),
  [`Theorem_2_4...lean`](../../DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_2_4_Counterexample_in_every_dimension_n_ge2.lean:17).
- `Theorem_Main_theorem.lean` now contains named fixed-parameter and
  parameterized negative convergence theorems, level-set variants, and no
  production `#check`/`#print`:
  [`Theorem_Main_theorem.lean`](../../DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean:5).
- `DFPWolfe.lean` is a compact theorem-facing facade and exports both fixed and
  parameterized Main APIs, the level-set semantics, and the matrix identity
  `liminf` certificate:
  [`DFPWolfe.lean`](../../DFPWolfe.lean:3).

## Shared rules

1. Recheck the exact source hash and mtime immediately before writing. External
   sessions have previously rewritten the generated files atomically.
2. One writer per source file. Do not edit another task's owned file, even to fix
   a typo; report the blocker to the integration task.
3. Follow the repository `AGENTS.md`: edit only the assigned target, use
   `lake lean <target>`, never `lake build`, and do not retain `#check` or
   `#print axioms` probes in production source.
4. Do not add `sorry`, `admit`, `sorryAx`, or project axioms. A temporary axiom
   probe belongs in `/tmp` and must be deleted after the audit.
5. Record the final source hash, target-check return code, artifact status, and
   any remaining warning in the handoff message.

## Decision that must be recorded

The phrase “negative global convergence theorem” has two possible quantifier
readings:

```text
not (for every admissible c₁,c₂, global convergence holds)
```

which a single `(1/4,3/4)` witness can refute, versus

```text
for every c₁,c₂ in the paper's range, global convergence fails.
```

The second is the paper's stronger statement and requires parameterizing the
Armijo construction. No task may silently replace the second reading by the
first.

## Current release boundary

The checked release now proves a strong-Wolfe counterexample for each
`0 < c₁ < 2 / 3`, `2 / 3 ≤ c₂ < 1`, in every dimension `n ≥ 2`, and the named
negative `GlobalWeakWolfeConvergenceAt` theorem for each such pair. The fixed
`(1/4,3/4)` aliases remain for compatibility. The level-set predicate now
records explicit trajectory containment, and its paper-range negation is
exported as well. Identity initialization is available as a genuine matrix
`InverseIteration` certificate with automatically generated problem-dependent
Hessian bounds and the exact positive `liminf` conclusion; the lower-level
operator interfaces remain available for reuse.
