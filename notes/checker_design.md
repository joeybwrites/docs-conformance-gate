# Conformance Gate — Design (Part 3 + Part 1 measurement)

Status: DESIGN, forming. Not locked.

Enforces the Part 2 standard for the Plugins slice as deterministic, machine-checkable rules with non-compensating (blind-reviewer-style) verdicts. Prototype scope: 1–2 rule families end-to-end on the real corpus; the rest designed + stubbed.

## Rule families

### R-A. Surface-scoped component conformance (fixes the drift)
- Input: a registry declaring, per surface (Cowork / Claude Code), the plugin component set.
- Check: any page enumerating plugin components must match the surface-scoped set for the surface it addresses; naming a Code-only component (LSP, monitors, themes, bin) without scoping it to Claude Code = violation.
- Verdict: divergent set = Revise; availability contradiction ("coming soon" vs "shipped") = Block.

### R-B. Prerequisite bridging — Joey's "what we expect users to know per page" (STAR of the measurement story)
Turns JF1 "assumes prerequisite knowledge" (un-checkable as quality) into a deterministic rule.
- Inputs:
  - **Concept registry**: core concepts (plugin, skill, connector, MCP, slash command, sub-agent, hook, marketplace, manifest, scope, …) each with a canonical definition page + aliases.
  - **Per-page assumed-knowledge budget**: page frontmatter `assumes: [concept, …]` — what the reader may already know.
- Check: for each registry concept a page mentions that is NOT in `assumes`, the page must link to that concept's canonical page on first mention (minimum bar) or define it inline. Neither → violation `unbridged prerequisite: <concept> @ line N`.
- Output: line-level, e.g. `submit.md:42 mentions "MCP connector" — not in assumes, no canonical link`.

### R-C. Link canonicalization
Flag non-canonical internal-link FORMS (doubled `/docs/docs/`, alias paths absent from llms.txt). Status-only checkers PASS these (they resolve) — so flag by form, not HTTP code.

### R-D. Off-property core-concept offloading
Flag in-scope plugin pages whose ONLY path to a core concept is an outbound link to an out-of-scope property (code.claude.com / support.claude.com). Operationalizes the "pull forward" finding.

### R-E. Terminology + decaying-time language
Canonical terms (sub-agent). Flag relative-time promises ("coming soon", "in the weeks ahead") in availability sections.

## Measurement (Part 1 bullet 4)

### Estate-health metrics (from the gate — leading indicator, runs in CI)
Unbridged-prerequisite violations per page / total · surface-unscoped component claims · % plugin pages passing all rules · off-property core-concept offloads.

### User-journey audit (Joey's "prospective audit of the user journey")
Define canonical reader tasks + the minimal in-estate page path each requires:
- "Cold reader: what is a plugin + what can it contain" → overview
- "Cowork user: install a plugin" → overview → cowork/guide/plugins → marketplace
- "Developer: prepare a plugin for submission" → overview → submit

Deterministic journey check: following ONLY in-estate links, can a reader traverse the path with (a) every concept bridged [R-B] and (b) no forced off-property hop for a core step [R-D]? A break = journey failure, located at the page.
**Keep it structural (bridging + reachability), NOT an LLM "is this smooth" grade** — that's the un-checkable trap.

### Real instrumentation (the "how you'd instrument it" — telemetry, ground-truth/lagging)
Off-property exit rate on plugin pages · internal-search zero-result rate for plugin queries · "was this helpful" votes · support tickets tagged plugins · (if available) task-completion funnels for the journeys above. **The gate predicts; telemetry confirms.** Track both over time.

## Evaluating the checker itself (Part 3 requirement)
- **False positives**: main source = generic-word collisions (R-B: "skill"/"agent" as common nouns) + undeclared-but-legit assumptions. Levers: prefer multi-word canonical terms, first-mention only, the `assumes` frontmatter. Tune toward RECALL (a missed bridge confuses a reader; a false flag costs a writer ~10s to dismiss) but cap FP so the report stays credible — state the target + the reason.
- **Degradation detection**: violation count tracked in CI; a PR that adds unbridged concepts raises it and can block merge. Registry-coverage meta-check: concepts frequent across the estate but absent from the registry = registry going stale.
- **Anti-staleness ("stale artifact in 6 months?")**: gate runs in CI on every docs PR; registry versioned WITH the docs; `assumes` lives in page frontmatter (maintained with the page); failing gate blocks merge. It can't rot silently because it runs on every change and fails loudly.
