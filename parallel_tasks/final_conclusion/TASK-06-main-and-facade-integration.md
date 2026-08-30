# TASK-06: Main theorem and facade integration

## Objective

Turn the current paper-facing wrapper into a real, named final API. Replace the
source-level `#check`/`#print` endpoint with theorem declarations and expose the
chosen final result through `DFPWolfe.lean`.

## Ownership

This is the only task allowed to edit these existing files:

```text
DFPWolfe/A_uniformly_convex_counterexample_to_global_convergence_of_DFP_under_weak_Wolfe_/Theorem_Main_theorem.lean
DFPWolfe.lean
```

Do not edit any ReasLib proof module or Theorem 2.3/2.4 proof. Wait until the
upstream companion APIs are frozen and their hashes are recorded.

## Required deliverables

1. A named theorem for the selected endpoint. At minimum, expose the current
   fixed-constant weak-Wolfe result; if Task 01 is complete, expose its explicit
   negative global-convergence theorem as the user-facing main theorem.
2. Preserve separate reusable existential certificate theorems. Do not hide all
   data inside an opaque proposition if clients need the orbit/Hessian projections.
3. Add the all-dimensional public import (or the new final module) to `DFPWolfe.lean`.
4. Remove production `#check` and `#print axioms` commands; those belong in an
   ephemeral audit file.
5. Keep docstrings and labels compliant with `AGENTS.md`.

## Quantifier guard

Do not call a fixed `(1/4,3/4)` theorem “for every Wolfe pair.” If parameterized
Task 02 is not available, use a name/docstring that says `fixedParameters` or
otherwise makes the limitation explicit.

## Acceptance criteria

- `lake lean` passes both owned files independently.
- An external scratch file can import `DFPWolfe` and resolve the final theorem by
  name (not merely through a `#check` in the source).
- No source-level `#check`, `#print`, `sorry`, `admit`, or project axiom remains in
  the owned files.
- Handoff records the exact public theorem names and imported modules.

## Dependencies and estimate

Depends on Task 01 for a negative endpoint; Tasks 02--04 are required only if the
paper-faithful strong/all-parameter/identity result is selected. Estimated human
effort: **0.5--1 working day**, plus any time waiting for dependency artifacts.

