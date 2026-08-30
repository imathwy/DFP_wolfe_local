# TASK-07: Final aggregate validation and audit

## Objective

Run the final checks after Task 06 is merged, with a reproducible record of source
hashes, return codes, artifact freshness, and theorem axioms. This task is a gate,
not a place to patch source.

## Ownership

No Lean source edits. Write logs only under `/tmp` and a final report:

```text
parallel_tasks/final_conclusion/FINAL_AGGREGATE_CHECK_REPORT.md
```

Do not edit generated files under `M2FQualityAudits/` or hand-create `.olean` files.

## Check order

1. Recheck hashes/mtimes for every newly integrated companion module.
2. Run each changed target with `lake lean <exact-target-file>` (or the configured
   `m2f-agent-lean-check` transport when required).
3. Run the named Main theorem wrapper.
4. Run `lake lean DFPWolfe.lean`.
5. In an ephemeral scratch source, import the final module and run `#print axioms`
   on the actual exported theorem. Delete the scratch source afterward.
6. Run a targeted debt scan on the owned final slice; distinguish inherited
   dependencies from local placeholders.

Never run `lake build`, never launch duplicate checks while another session owns the
Lean coordinator, and do not infer success from an artifact whose source hash does
not match.

## Acceptance criteria

- Every claimed final theorem has a fresh zero-return target check.
- The facade resolves the theorem by its public name.
- The axiom set contains only `propext`, `Classical.choice`, and `Quot.sound` (or
  an explicitly documented inherited foundation accepted by the project policy).
- The report lists warnings separately from errors and records any stale artifact.

## Dependencies and estimate

Runs after Task 06; it is not a parallel source-editing task. Estimated human effort:
**0.5--1 working day**, with wall-clock time potentially longer if the shared Lean
coordinator is queued.

## Handoff

> Historical handoff: the fixed-only status below was superseded by the
> parameterized aggregate audit on 2026-08-30. Use
> `FINAL_AGGREGATE_CHECK_REPORT.md` for the current release boundary.

Completed for the fixed-parameter release on 2026-08-29.

- Main wrapper SHA256: `d1356ba212b8136c18f251cc0bb8f3c6d4205e4a0a92d5a7b6ecc693b4a5125d`.
- `DFPWolfe.lean` SHA256: `131d0965b5abb6b0ee7cfe56575267ec60902c18e5d5c231fdc5ae738b28ab76`.
- Both direct checks returned RC0; an ephemeral facade probe resolved the named
  negative theorems and printed only `[propext, Classical.choice, Quot.sound]`.
- The fixed public statements are
  `¬ GlobalWeakWolfeConvergenceAt (1 / 4) (3 / 4)` and
  `¬ UniversalGlobalWolfeConvergence`.
- The stronger paper quantifier over every admissible `(c₁,c₂)` remains the next
  integration gate; see TASK-08--TASK-12.

TASK-08--TASK-11 completed that integration gate. TASK-15 subsequently added
the level-set containment semantics and completed the automatic matrix
identity-initialization `liminf` bridge. Use the current aggregate report for
the released hashes and theorem surface.
