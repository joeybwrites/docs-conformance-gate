# Part 3 — Conformance gate: design, prototype scope, evaluation

The rules live in `../standards/plugin_style_guide.md` (S1–S8). This doc does not redefine them (single owner); it specifies **which are prototyped, how the prototype runs on the real corpus, how the checker is evaluated, and the fuller gate as designed-not-built.** The prompt invites "notes about what you'd build out" when the plan outruns the time — the classifier vision below is exactly that.

## What ships in Part 3

- **One working vertical slice** that RUNS on the real corpus and shows what it found (with real false positives). Two-deep-beats-four-thin: depth on one check, not a shallow four.
- This design doc, marking the fuller gate as designed, not built.

## The prototype — the connective-tissue check (S4 + S5)

Chosen because it is the most deterministic slice AND it measures the fragmentation headline directly, and it has a ready known-positive: the reference sweep found **10 of 17 cross-reference pages name plugins without linking the plugin docs.**

- **S4 — prerequisite bridging.** Inputs: a **concept registry** (core concepts → owning page + aliases) and each page's `assumes:` frontmatter. Check: for every registry concept a page mentions that is not in its `assumes`, require a first-mention link to the owner. Output: line-level violations (`page:line — concept "X" used, not assumed, not linked`).
- **S5 — handoff presence (deterministic core).** For off-property links (`code.claude.com`, `support.claude.com`) in a decision context: require an adjacent summary + ownership sentence, and a `#anchor` **unless** the target is a registered dedicated task page (per the ownership registry). Flag bare-root / unframed handoffs.

Corpus: pulled from `claude.com/docs/llms.txt`, in-scope surfaces. Runs headless; emits a report keyed by page/line/rule. `assumes:`, `content-type:`, and the registry are the declared inputs (maintained with the pages), so the check can't rot silently.

**Known-positives (must fire — R3-style):** the 10 unlinked cross-reference pages; the doubled-`/docs/docs/` home-page links (S6, a cheap bonus); optionally the Chat availability contradiction (S3).

## Evaluating the checker (Part 3 asks for this explicitly)

- **False positives.** Gold case from the sweep: **"Enterprise SSO plug-in"** (Microsoft's hyphenated term on entra-broker / connectors-m365) is NOT a Claude plugin — the matcher must separate "plugin" from "plug-in" and generic uses. Plus generic-word collisions ("skill"/"agent" as common nouns). Levers: prefer multi-word canonical terms, first-mention-only, and the `assumes:`/registry inputs. **Tolerance:** tuned toward recall — a missed bridge confuses a reader; a false flag costs a writer ~10s to dismiss — but capped so the report stays credible. State the number and the reason.
- **Degradation.** Violation count tracked in CI; a PR that adds unbridged concepts raises it and can block merge. Registry-coverage meta-check: concepts frequent across the estate but absent from the registry = the registry going stale.
- **Anti-staleness ("what keeps this from being a stale artifact in six months?").** Runs in CI on every docs PR; the registry and the `assumes:`/`content-type:` frontmatter live with the pages; a failing gate blocks merge. It fails loudly on every change rather than rotting quietly.

## The fuller gate — a page classifier (DESIGNED, not built)

A per-page classifier whose **role assignment selects which checks fire** — an extension of S7's `content-type`, **not a parallel checker** (one home per rule, R1). Four dimensions (Joey's framing, audited):

1. **Expected incoming knowledge** ("semi-knowledge-graph") = S4 + `assumes:`. **Tractable form is the per-page `assumes:` list, not a hand-maintained cross-page knowledge graph** — a KG of concept prerequisites is the expensive, rot-prone part (the exact anti-staleness failure this gate exists to prevent). Keep the KG as the mental model; build `assumes:`.
2. **Required supporting-material references, interlinked** = S4 + S5. (Re-expression of existing rules, deliberately not a separate check.)
3. **Bounded config-in-miniature** = S5 + a **duplication ceiling** *(a genuine addition to S5)*: a config summary must (a) stay under a length cap, (b) link to its owner, (c) not verbatim-overlap the owner's canonical block. "Useful" past that proxy is a human call — automating it would make this a quality-grader, which the whole design avoids.
4. **Terminality / journey-completeness** *(a genuine addition)* — **a team-sourced, DECLARED input, per intended reader-goal**, gathered via standard tech-writing discovery (interview the feature team on expected usage). The checker enforces **conformance-to-declaration**: "declared terminal for goal X → does the page satisfy X in-page, or does it dangle?" It is **not** machine-inferred, and it is **not** a flat page label (a page is terminal for one goal and a hub for another — e.g. the overview is terminal for "what is a plugin?" and a hub for "how do I build one?").
   - **This is the one dimension a take-home structurally cannot prototype:** its ground truth lives with teams the candidate has no access to in a 6-hour exercise. That makes it a **Part 4 capability** (adoption / inter-team work without authority) — and the honest reason it is designed here, not built.

**Validation.** The classifier's labels need a **reader-task set** (journey paths) as ground truth, or they are unfalsifiable assertions — the same discipline any checker needs (a confident-wrong classifier is worse than none).

## Measurement it feeds (Part 1 §4)

Gate metrics are the **leading** indicator (unbridged-prerequisite count, unframed-handoff count, % pages clean — in CI). The **structural journey audit** (can a reader traverse discovery→build→…→maintain in-estate with every concept bridged and no unframed off-property hop?) is the coherence measure. **Telemetry** is ground truth (off-property exit rate on plugin pages, internal-search zero-result rate, "was this helpful", plugin-tagged tickets). The gate predicts; telemetry confirms.
