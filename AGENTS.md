# AGENTS.md — PROOF stage (strict rules, Lean 4 + mathlib)

You are a coding agent in a Lean 4 + mathlib workspace rooted at `LEAN_ROOT`.

## Lean validation transport

When `M2F_AGENT_REMOTE_LEAN_ONLY=1`, never use a local Lean/Lake/Elan/LSP
installation. Validate only with `m2f-agent-lean-check <target_file>`.
`lake lean <target_file>` is a compatibility shim for that same remote command;
all other `lake` commands and direct `lean`/`elan` commands are blocked. Never
search for or invoke an absolute local toolchain path.

Your mission in the **PROOF** stage:
- Given existing declaration skeletons, **replace the relevant `sorry` with proofs**.
- The target file must pass the configured target check.

This file is the PROOF-stage rules source; the orchestrator copies it to `LEAN_ROOT/AGENTS.md` before each Codex call.

---

## A. Hard constraints (do not violate)

1) Edit scope
- Edit **only** the file explicitly provided by the orchestrator (`target_file` / `lean_file` in meta).
- Do not touch any other file. Do not rename/move files.

2) No embedded proof fragments inside terms
- Do not embed proofs inside a larger term (e.g. `⟨..., by ...⟩`, `(by ...)` used as a subterm, etc.).
- It is OK to use `by ...` as the *top-level proof* of a `lemma` / `theorem`.
- If a term construction requires a proof obligation, introduce a **separate named lemma** and reference it.

3) Definitions must be proof-free
- Inside a `def` / `abbrev` body, do not use `by ...`.
- If a definition body must be a placeholder, use `:= sorry` (never `by sorry`).

4) No axiom
- Never introduce `axiom`.
- Final proof success requires the current item's owned target slice and theorem-local support files to contain no `sorry`, `admit`, or `sorryAx`, followed by `#print axioms` on the actual main declaration. The orchestrator executes that audit in an ephemeral source and deletes it; proof agents must not add or retain `#check` or `#print` in `ReasLib/` source. A reported `sorryAx` may be accepted only as recorded debt inherited from an earlier failed item after this local-cleanliness check; project-defined axioms and audits that cannot execute or parse still fail closed. The accepted logical foundations are `propext`, `Classical.choice`, and `Quot.sound`.

5) Docstrings are required
- Every new helper declaration must have its own docstring immediately above it: `/-- ... -/`

5.1) Label must be preserved in docstrings
- The orchestrator provides a `label` for the current textbook entry.
- Do not remove it from existing docstrings.
- If you introduce any helper declarations dedicated to proving this entry:
  - Include the `label` in their docstrings as well, but **do not** make the helper docstring start with the raw `label`.
  - Recommended helper-docstring template: `/-- Helper for <label>: ... -/`
  - Only the **main** theorem/lemma for this entry should have a docstring that starts with the `label` (to avoid accidental “multiple decls per label” conventions).

5.2) Helper naming and docstring quality
- Name helper declarations by their own mathematical role, not by bookkeeping or textbook numbering.
- Do **not** encode raw label numbers in helper names unless that numbering is genuinely part of the mathematical object’s established name.
- Helper docstrings should describe what the helper states/does mathematically, not how its proof works.
- Write helper docstring formulas in Lean-renderable style: Lean identifiers, actual declaration expressions, and Unicode symbols such as `π`, `𝒰`, `F`, `⟶`, `≃`, `⊗`, and `ᵒᵖ`. Avoid raw TeX commands such as `\check`, `\mathcal`, `\to`, and `\bullet` when an equivalent Lean/Unicode expression is available.
- Helper names should follow mathlib naming conventions: use mathematical meaning, prefer lowerCamelCase for ordinary helper defs/lemmas/theorems, reserve underscores for established API families such as `mem_foo`, `coe_foo`, `foo_iff`, `foo_apply`, and `foo_def`, make `_iff` names genuine biconditionals, avoid namespace duplication, and prefer standard American spelling.

6) Mathlib first
- Prefer existing mathlib lemmas/definitions.
- Avoid re‑defining standard structures; prove equivalences or provide instances/lemmas instead.

7) Imports and module paths
- Do not introduce inconsistent imports.
- Never import modules under `M2F.<project>...`. Use `<project>.Chapters...` etc.

8) Dependency-order policy (strong default in prompts)
- Build the proof only from `dependencies` (from item metadata), their transitive prerequisites, and mathlib.
- Search/use order should be:
  - first the current item's direct `dependencies`;
  - then their natural companion lemmas/obvious nearby support lemmas already in scope;
  - only then broader mathlib search/routes.
- Default rule: do **not** import or rely on declarations that are later than the current target (later JSON items / later textual order in file).
- In particular, for per-item infra files, do not solve an earlier item by importing a later-item module (e.g. proving `Infra:25:4` by importing `InvariantU`).
- If a later declaration is genuinely unavoidable, state the exact declaration and concrete reason explicitly in feedback/notes so orchestrator logs can track the exception.
- Do not “skip missing prerequisites” by jumping to later theorems; request re-plan and ask for the prerequisite to be proved in the correct dependency order.

---

## B. Proof workflow and stability (codex-friendly)

1) Prove, do not refactor
- Keep statements intact unless a minimal change is required for correctness/type‑checking.
- Keep edits local to the targeted label/declaration.

1.1) Preserve mathematical meaning
- If the statement is mathematically sound (i.e. “the problem is not wrong”), do not change its meaning:
  - Do not weaken/strengthen assumptions or conclusions.
  - Do not change quantifiers/binders or switch to a different (non-equivalent) formulation just to make the proof easier.
- Only adjust a statement when it is genuinely inconsistent/ill-typed relative to the intended meaning; in that case keep the change minimal and explain the reason in your feedback/notes.

1.1.1) Target vs helper statements
- The restrictions in 1.1 apply to the **target textbook declaration** you are proving (the theorem/lemma/def corresponding to the current label/content).
- For **helper** declarations that you introduce (or previously introduced) to support the proof:
  - You may revise their statements as needed to make the proof go through (including adding/removing hypotheses), as long as the helper statements remain **mathematically correct** and preferably **general/reusable**.
  - Do not use helper-statement edits to “smuggle in” extra assumptions that effectively strengthen the target theorem; the target theorem’s statement must stay faithful to the intended book meaning.
  - If you discover a helper statement is **mathematically false / missing assumptions**, do not try to force a proof. Instead, **restate the helper to a correct version** (typically by adding the missing hypotheses or weakening the conclusion) and update all downstream call sites accordingly.
    - Do **not** treat this as a “bad statement” unless the **target textbook declaration itself** is false/unprovable as written.
    - If you cannot complete the repair in this attempt, keep the file compiling and request re-plan with: (i) the corrected helper statement, (ii) the list of call-site changes, and (iii) a brief reason why the old helper was false.

1.2) Universe mismatch exception (Lean-technical, meaning-preserving)
- If a proof is blocked because the *statement itself* does not type-check due to a **universe/implicit-binder mismatch**, you may adjust the **declaration header/signature** in a way that preserves the intended mathematical meaning.
- Allowed header adjustments include (non-exhaustive):
  - Change `Type*` / `Sort*` binders to `Type u` / `Sort u` to align universes with other parameters.
  - Add `universe u v ...` declarations and use them in binder types.
  - Align index types in covers/families: `{ι : Type u}` vs `{ι : Type*}` when `Y : Type u`.
  - Make implicit universe arguments explicit when needed (e.g. `.{u}`) without changing the proposition.
- Not allowed:
  - Any change that weakens/strengthens assumptions or conclusions, changes the quantified mathematical content, or “patches” by adding extra assumptions.
  - Switching to a different (non-equivalent) formulation just to make the proof easier.

2) Use helper lemmas
- First build the **main proof skeleton** (main invariant/object + top-level decomposition + expected finishing route); do not start by generating a long helper list before the main route is clear.
- Treat proof-side helper/API choices as if the result may later live in mathlib: prefer canonical reusable helper lemmas, abstract routes, and elimination of local proof-script scaffolding that would not survive upstream review.
- Introduce a thin **adapter/helper lemma** only when the main route is already clear and you are blocked by interface alignment (binder order, coercions, transport shape, rewrite shape, map lemma shape, etc.).
- **Large-construction proof-interface rule (required):** when a statement/target contains a large construction, do not make the main proof unfold or simplify that construction in place. This applies to long morphism composites, structured data records, quotient/localization/fiber/pullback/base-change objects, descent data, choice-built witnesses, and any construction with many projections or transports. First give the construction a small proof interface: name the meaningful components, choose stable normal forms or projection lemmas, and prove the specific `spec`/compatibility/naturality/normalization facts used by the source proof. The main proof should depend only on those interface lemmas, usually via short `calc` chains or direct projection rewrites. For morphism equalities this often means proving component-level bridge squares such as `t ≫ targetBridge.hom = sourceBridge.hom ≫ d`; for data objects it means proving projection/spec/API lemmas rather than exposing the constructor body. Put plumbing (`Category.assoc`, iso cancellations, `Functor.map_comp`, coercions, transports, record projections, quotient eliminators) behind tiny adapter lemmas and consume them with `simp only` or direct rewrites; avoid broad `simp`, repeated `change`/`convert`, or target-local unfolding over the whole construction.
- If the proof needs a canonical typeclass fact, first try to obtain it via existing instances (`infer_instance`) before introducing an explicit supporting theorem or local `have`.
- If an existing lemma/theorem call is passing a typeclass fact explicitly even though the fact is already available through the instance context, prefer deleting that explicit parameter and relying on typeclass inference.
- Do not introduce a local `letI` for an instance that is already inferable from the current context. Use `infer_instance` / ordinary typeclass search instead.
- Treat every new `local instance`, `attribute [local instance]`, or genuinely non-inferable `letI` as exceptional. First try a reusable named instance, explicit noncanonical parameter, finer helper declaration, or named comparison bridge. If a local instance path is truly necessary, put the exact required `-- Local instance justification (<category>): <specific reason>` immediately above it; convenience or a bare elaboration failure is insufficient.
- Do not introduce local notation/infix/prefix/postfix, local syntax/macro, or non-instance local attributes merely to shorten a proof. Reuse existing notation or promote stable vocabulary to named/owner-scoped reusable API. An unavoidable local surface needs an immediate kind-appropriate `Local declaration justification` with a concrete source-local/parser/metaprogramming/automation reason.
- If the proof is long or brittle, introduce a small set of reusable helper lemmas with good names and docstrings.
- Avoid deeply nested `have` chains; keep the main proof flat and readable.
  - **Naming (required):** any helper `lemma`/`def`/`abbrev` you introduce must be named according to its mathematical meaning (not `helper1`, `tmp`, `h1`, `lemma_1_2`, etc.).
  - **Reusability (required):** prefer helper lemmas that are as general as reasonable (so later proofs can reuse them), not overly specialized to a single line of the current proof.
  - **Abstraction level (required):** state helper lemmas at the most natural mathlib-facing abstraction level that still matches the proof. Prefer reusable lemmas about the canonical objects/maps/relations already present in mathlib or the project, rather than ad hoc wrappers tied only to this local proof script.
  - **Do not stay concrete by default (required):** if the main theorem can be executed through an abstract/canonical route, prefer that route first. Use concrete carriers/representatives/local expansions only when the abstract route genuinely fails or the source theorem itself is concrete.
  - **Helper drift guard (required):** do not repeatedly weaken/relocalize a statement-facing helper just to get Lean to accept the next line. If a helper has already been weakened once and the route still fails, reconsider the main proof route instead of continuing to degrade the helper into a patch lemma.
  - **When to extract a standalone helper (required):** extract a `have` into a named helper lemma when it has independent mathematical meaning, is plausibly reusable, gives a cleaner statement than the immediate local goal, or is mainly needed as a reusable rewrite/ext/transport fact.
  - **When to keep it local (required):** keep a step as a local `have` when it is just one-off goal reshaping, local algebraic cleanup, a transient instance assembly, or another fact with no natural standalone mathematical statement. If it can be restated cleanly at a higher abstraction level, do not freeze it into a local term-specific lemma.
  - **Instance-first discipline (required):** if a local fact is already a natural consequence of available typeclass instances, do not introduce a new `have h : IsX T := ...` or a standalone helper theorem just to restate it. Prefer `infer_instance` / ordinary instance search, and add an explicit helper only when instance search genuinely needs a bridge.
  - **No redundant explicit named arguments (required):** if ordinary elaboration and the expected type already determine named parameters such as `(R := ...)`, `(S := ...)`, or explicit universe arguments, do not write them. Keep them only when Lean really needs them for disambiguation.
  - **No redundant coercion notation (required):** if the expected type already lets Lean insert the obvious coercion from a bundled object/subtype to its carrier, do not write explicit carrier notation like `↥(...)`. Keep explicit coercions only when they are needed for disambiguation or readability.
  - **Short namespace-qualified constants (required):** if the expected type or an explicit type ascription already determines the namespace of a constant, prefer the shorter readable form rather than repeating the full namespace path.
  - **No inferable `letI` (required):** if a local instance is already inferable, do not add a redundant `letI`; reserve `letI` for genuinely non-inferable local bridges that materially change the local instance context.
  - **Helper scope classification (required):** when you introduce a standalone helper, decide whether it is only `file_local` reusable or genuinely `upstream_worthy` for the surrounding chapter API. Default to `file_local` unless the helper has clear independent reuse value beyond the current proof.
  - **Long‑range progress (required):** unless you hit a concrete Lean blocker, each attempt should implement the proof skeleton and prove multiple key helper lemmas in the same pass (avoid tiny 1–2 line edits that don’t materially advance the proof).
  - **Agent A substantial progress rule (required):** every Agent A attempt must produce material proof progress (e.g., fewer `sorry`, solved key subgoals, or proved helper lemmas), not cosmetic/no-op edits.
  - **Only exception:** if the target statement is mathematically wrong/unprovable as written, stop forcing local edits and report it as `failed_bad_statement` with a concrete reason.
  - If you must leave a helper lemma as `:= sorry` during a re-plan request, ensure the *statement* is mathematically correct and still reasonably general; do not invent false lemmas to unblock.

2.1) Proof decision ladder (required)
- Before introducing new proof scaffolding, follow this ladder:
  1. Reuse an existing dependency/mathlib lemma directly if it already closes the step.
  2. If the route is clear and the mismatch is only interface-level, add a thin adapter/rewrite helper.
  3. If a local fact has independent mathematical meaning or clear reuse, extract a standalone helper lemma at the natural abstraction level.
  4. Only fall back to more concrete/model-specific unfolding after the abstract/canonical route has been tried seriously.
  5. If several helper statements would work, prefer the one with the weakest sufficient hypotheses and the strongest natural reusable conclusion.

3) Prefer stable tactics
- Prefer deterministic tactics/steps (`simp`, `rw`, `constructor`, `refine`, `calc`, `linarith`/`nlinarith` when appropriate).
- Avoid relying on “suggestion” tactics/macros (e.g. `simp?`, `exact?`) in final code.
- Prefer `fun ... ↦` over `λ`.
- Do not chain tactics with semicolons; keep each tactic step explicit.
- Put `by` at the end of the preceding line, not on a line by itself.
- Use `·` to structure side goals instead of braces.
- Prefer a single `rw [...]` / `simp [...]` over many tiny consecutive rewrites/simplifications when the resulting proof stays readable.
- Prefer `rwa [...]` / `simpa [...]` when the final step is `rw`/`simp` followed immediately by `exact h`.
- If a local fact will mainly be used for rewriting/simplification, prefer formulating it as a rewrite-friendly lemma instead of burying it inside a procedural proof.
- If a local fact is mainly about equality of structured objects, prefer an extensional statement/route when appropriate.
- If a local fact is mainly about transport through maps/coercions, prefer a `map_*` / coercion-compatible statement shape over a bespoke procedural argument.
- Prefer first putting goals into a standard `rw`/`simp`/`ext`/`calc`/`constructor`/`refine` friendly shape before reaching for heavier tactics.
- Use heavier closing tactics (`linarith`, `nlinarith`, `omega`, etc.) after the statement has been normalized into a good shape, not as the first substitute for structural organization.
- Avoid `rw [show ...]` and `show ... from` conversion shortcuts; if a nontrivial conversion is needed, state it as a readable local or named helper and rewrite through that helper.
- Avoid `change` when a direct `rw`, definitional reduction, or a helper lemma will do.
- For cast/transport goals (base ring -> fraction ring / algebraMap), prefer proving the source-ring identity first and then mapping it (`simpa using congrArg (algebraMap _ _) h` or a canonical `map_*` lemma).
- Avoid brittle patterns that rewrite into an artificial goal via `change` and then close it with numeral-cast lemmas (for example `map_intCast`) unless that lemma is exactly the intended mathematical step.
- If `linter.flexible` warnings appear, follow the hint-driven rewrite style: run `simp?` and replace broad `simp` with `simp only [...]`, and use `suffices`/`have` to state intermediate goals explicitly instead of repeatedly mutating `⊢`.
- Do not use `open Classical`; use a local `classical` only when the proof genuinely needs classical reasoning.
- Do not use `haveI` inside tactic proofs; use `have`/`obtain` and explicit terms instead.
- Prefer `ext` over manual extensionality lemmas when applicable.
- Avoid unnecessary type annotations and overly nested `have` chains; flatten the proof or extract a helper lemma instead.

4) Compilation discipline
- The orchestrator checks with `lake lean <file>`.
- Do **not** run `lake build`.
- Warnings discipline:
  - Do not silence lints/warnings via `set_option` or disabling linters.
  - If asked to clean non-`sorry` warnings, fix them by adjusting code (unused args/vars, simplifying `simp`, etc.).

5) Source-proof fidelity rule
- Preserve the source proof's governing structure instead of greedily following the easiest local Lean recursion.
- Before committing to a route, identify: the main object being controlled, the global invariant/rank, and the bridge lemmas linking the source objects to Lean objects.
- Build the proof skeleton from those ingredients first; treat induction as a fallback when that structure cannot be realized directly.
- Prefer proof architectures organized by global objects such as intervals, chains, extremal constructions, universal properties, or rank functions.
- Keep Lean-technical translations subordinate to the mathematical idea; they should support the skeleton, not determine it.
- If a route compiles locally but obscures the source proof's core idea, stop and redesign the skeleton before adding more tactic glue.

---

## C. Multi‑agent protocol (C plans → A proves → B fixes)

When a planning/fallback protocol is in use, follow these contracts:

1) **Agent C plan block**
- Agent C outputs exactly one JSON plan wrapped by:
  - `<<<AGENT_C_PLAN>>>`
  - `<<<END_AGENT_C_PLAN>>>`

2) **Agent A feedback block**
- Agent A must end with exactly one JSON feedback block wrapped by:
  - `<<<AGENT_A_FEEDBACK>>>`
  - `<<<END_AGENT_A_FEEDBACK>>>`
- `status="needs_replan"`:
  - You are blocked structurally; leave only small, well‑scoped `sorry`.
  - The file must still compile (no Lean errors besides explicit `sorry`).
  - Be specific about blockers and what lemmas are needed.
  - Report the stabilized frontier: what part of the main skeleton is already verified, which helper lemmas/subgoals are closed, and the first remaining blocker that prevents final closure.
- `status="failed_bad_statement"`:
  - Use this only when the target statement itself is mathematically false/inconsistent as written.
  - Provide a concrete mathematical reason (do not use this for ordinary proof difficulty).
- `status="ok"`:
  - Structure is stable; **no `sorry` remain** in the targeted work.
  - Any remaining issues should be low‑level fixups (imports/typos/tactics) for Agent B.

3) **Agent B**
- Agent B only does low‑level fixes (imports/typos/local tactic tweaks), not re‑planning.

---

## D. Tooling expectations

- Prefer using Lean LSP tooling (if available) for diagnostics/goals/completions.
- Do not run `lake build`.
- **Mandatory before finishing (Agent A and Agent B):** after you edit the target file, you must run:
  - `lake lean <target_file>`
  and only finish when there are **no Lean errors** (warnings are OK unless explicitly asked to clean them).
  If errors remain, you must attempt to fix them yourself before handing off.
- The orchestrator validates with `lake lean <file>`, but do not rely on the orchestrator to discover basic errors for you.
