# TASK-05: Paper-to-Lean coverage and API audit

## Objective

Produce an evidence-based inventory of what the paper claims and what the Lean
library actually exports. This is a read-only task for Lean source; it prevents
the integration session from accidentally claiming a hidden or stale result.

## Ownership

Do not edit Lean source, generated `.olean` files, or audit snapshots. Write only
the report:

```text
parallel_tasks/final_conclusion/FINAL_CONCLUSION_COVERAGE_REPORT.md
```

## Audit questions

Map at least these paper items to exact declarations and line numbers:

1. The weak-Wolfe global-convergence question.
2. The parameterized Main theorem.
3. The strong-Wolfe endpoint verification.
4. The positive gradient limit/nonconvergence conclusion.
5. The all-dimensional extension.
6. The identity-initialization corollary.
7. Optional geometric claims: limiting circle, unbounded rotation, interpolation,
   and numerical/line-search remarks.
8. The top-level facade and whether a client can name the final theorem through it.

Classify every item as `complete`, `partial`, `missing`, or `optional`, and cite
the paper and Lean paths. Distinguish source declarations from fresh artifacts;
record source/artifact hashes and mtimes only after rechecking them.

## Required conclusion

End the report with two explicit recommendations:

- the smallest sound final theorem that can be checked now;
- the additional work required for exact paper fidelity.

Also state whether a fixed `(1/4,3/4)` witness is being used to refute a universal
claim over constants, or whether the report requires an all-parameter theorem.

## Acceptance criteria

- The report has exact line references and no unsupported “green” claims.
- It confirms whether `Theorem_Main_theorem.lean` contains a declaration or only
  `#check`/`#print` commands.
- It lists all files that the integration task must own, with no proposed overlapping
  writers.

## Dependencies and estimate

Fully parallel and read-only. Estimated human effort: **0.5--1 working day**.

## Handoff

The read-only inventory is in
`parallel_tasks/final_conclusion/FINAL_CONCLUSION_COVERAGE_REPORT.md`.
It separates the cheap fixed-witness negation from the paper's parameterized
strong-Wolfe statement, records source/artifact freshness, and keeps Main/facade
wiring in Wave 2 rather than silently treating it as already exported.
