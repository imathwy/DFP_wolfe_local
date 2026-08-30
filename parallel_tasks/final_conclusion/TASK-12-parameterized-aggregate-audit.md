# TASK-12: Final parameterized aggregate audit

## Objective

Run one clean, reproducible check of the parameterized release after TASK-11 and
write the final coverage/effort report. This task is read-only with respect to
Lean source.

## Ownership

Do not edit Lean files or generated artifacts. Write only logs under `/tmp` and
update `FINAL_AGGREGATE_CHECK_REPORT.md` plus this handoff section.

## Check order

1. Freeze and hash TASK-08--11 sources.
2. Run each exact target with `lake lean` once, serially through the coordinator.
3. Run Main and `DFPWolfe.lean`.
4. Import the facade from an ephemeral probe, resolve the parameterized theorem,
   and print axioms for the actual exported negative-convergence declaration.
5. Scan the owned release slice for `sorry`, `admit`, `sorryAx`, project axioms,
   and production `#check`/`#print`.

## Acceptance criteria

The report must distinguish a true paper-faithful result from the already green
fixed-parameter result, list stale artifacts, and give a remaining-work estimate
if any parameterized gate is still open. Do not infer RC0 from an artifact alone.

## Dependencies and estimate

Runs after TASK-11. Expected effort: **0.5--1 day** plus coordinator wait time.

## Handoff

Completed on 2026-08-30. The final report
`FINAL_AGGREGATE_CHECK_REPORT.md` records the exact hashes and serial RC0
checks for TASK-08--15, the facade export probe, allowed axioms, and the
semantic level-set and matrix identity conclusions. The paper-range
strong-Wolfe negative convergence theorem and the matrix-facing identity
corollary are verified; no additional aggregate blocker remains.
