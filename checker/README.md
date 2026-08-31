# Part 3 — Plugin documentation conformance gate (prototype)

A small, deterministic checker that enforces a machine-checkable subset of the plugin documentation standard (`../standards/plugin_style_guide.md`) and runs on the **real** Claude Docs corpus. Stdlib Python, no dependencies, no model in the loop — its verdicts are reproducible and reviewable.

The full rule set and the designed-but-not-built gate (the page classifier, terminality as a team-sourced declaration, the duplication ceiling) live in `../notes/checker_design.md`. This prototype builds one vertical slice end to end — two phases deep beats four thin.

## What this prototype checks

| Rule | Enforces |
|---|---|
| **S4** | Prerequisite bridging — every core concept a page uses that isn't in its `assumes:` (or that it's `canonical_for:`) must link to that concept's owner |
| **S5** | Contextualized cross-property handoff — an off-property link must be framed and either carry a `#anchor` or target a registered dedicated destination |
| **S6** | Link form (bonus) — no doubled `/docs/docs/` prefixes |
| **FM** | Input contract — the file has no parseable top-level frontmatter (see below) |

Declared inputs live in `registry.json` (concept→owner registry, off-property hosts, dedicated destinations, ownership cues) and in each page's `assumes:` / `canonical_for:` / `content-type:` frontmatter — all maintained *with* the docs.

## Input contract

The gate expects **one actual doc page with top-level frontmatter.** When a file has none — a pre-standard live page, or a meta-doc like `standards/plugin_overview_before_after.md` — the `assumes:`/`canonical_for:` exemptions can't apply, so the gate emits an **FM** finding and any S4 concept findings on that file may be phantoms (e.g. "plugin" flagged on the plugins page itself). Run the gate on pages, not on meta-docs. This behavior was added *because* rigor-testing against the real before/after doc produced phantom S4s — the FM finding makes that failure legible instead of silent.

## Run it

```bash
python fetch_corpus.py                  # pull the real in-scope pages into corpus/
python conformance_gate.py corpus/      # run on the live corpus
python conformance_gate.py fixtures/    # run on the pass / fail fixtures
python conformance_gate.py --json corpus/plugins_overview.md
```

Exit code = number of files with findings (0 = clean), so it drops straight into CI. Full captured output: `sample_output.txt`.

## What it found on the real corpus

Five live pages, all with findings — **57 total** (`fetch_corpus.py` snapshot, 2026-08-31). Every page also carries an FM finding: none of the live pages carry the standard's frontmatter yet.

| Page | Findings | Real signal |
|---|--:|---|
| `docs/index` (home) | 30 | **26 doubled `/docs/docs/` links (S6)** — every product link on the estate's front door is a non-canonical duplicate URL |
| `plugins/submit` | 11 | unlinked primitives (S4) + 6 unframed/unanchored off-property handoffs (S5) |
| `plugins/overview` | 6 | `slash command` / `sub-agent` named but unlinked (S4); 2 bare off-property handoffs (S5) |
| `cowork/guide/plugins` | 6 | names skills, connectors, slash commands, sub-agents, hooks — links none (S4) |
| `connectors/overview` | 4 | `connector`, `slash command`, `sub-agent` unlinked (S4) |

The S4 spread is the fragmentation finding made countable; the home-page S6 cluster is one deterministic high-traffic defect. Both are the connective-tissue problems Part 1 named.

## Where the checker got it wrong, and what rigor testing fixed

Running against the **real** `plugin_overview_before_after.md` (not just a hand-made fixture) surfaced four issues; three are now fixed, and the honest residue is documented:

- **Fixed — framing heuristic false positive.** A registered destination with a short bulleted label (`**Install in Claude Code:** [Discover and install plugins]`) was flagged "unframed" by a crude 6-word threshold. Now: a registered destination is framed by a descriptive (≥2-word) label; the word-count/cue test only applies to arbitrary off-property links.
- **Fixed — `plugins-reference` root links.** The reference is consulted whole, so it's now a **registered dedicated destination** (root links to it are valid handoffs). Decision recorded by the author.
- **Fixed — silent phantom S4s.** Meta-docs and pre-standard pages now get an explicit **FM** finding instead of confusing concept flags (see Input contract).
- **Known residue (honest).** Legal/policy links (`directory-terms`, `directory-policy`) are still flagged as unframed — a registry-tuning call. Findings aren't de-duplicated (same URL twice on a line reports twice). Concept matching is word-boundary and excludes the hyphenated `plug-in`, so "Enterprise SSO plug-in" is correctly *not* matched, but generic senses of "skill"/"agent" could still collide — mitigated by multi-word aliases and the bridge exemption (a link to a concept's owner is treated as S4 bridging, not an S5 handoff).

## Evaluating the checker itself

**False-positive tolerance, and why.** Tuned toward **recall**: a missed prerequisite bridge or an unframed handoff confuses a reader; a false flag costs a writer ~10 seconds to dismiss. But capped so the report stays credible — the dominant FP source (missing frontmatter) is designed to disappear as pages adopt the standard, not by weakening the rule. Demonstrated: `fixtures/pass_overview.md` (a real page with frontmatter) runs **clean**.

**How I'd know if it degraded.** Violation count tracked in CI; a PR that adds unbridged concepts or bare handoffs raises it. Registry-coverage meta-check: a concept frequent across the estate but absent from `registry.json` signals the registry going stale. The fixtures are the regression suite — `fail_s4/s5/s6` must keep firing and `pass_overview` must stay clean.

**What keeps it from being a stale artifact in six months.** It runs in CI on every docs PR and fails loudly (nonzero exit blocks merge), so it can't rot silently. Its declared inputs — `registry.json` and page frontmatter — live with the docs and are updated by the same PR that changes them. It is deliberately deterministic, so a reviewer can always see *why* a line was flagged.

## Files

- `conformance_gate.py` — the checker
- `registry.json` — declared inputs (concept→owner, hosts, dedicated destinations, cues)
- `fetch_corpus.py` — pulls the real corpus
- `fixtures/` — `pass_overview.md` (clean) + `fail_s4/s5/s6` (each fires one rule)
- `corpus/` — the fetched live pages (gitignored; reproducible via `fetch_corpus.py`)
- `sample_output.txt` — captured run (fixtures, the meta-doc input-contract demo, and the real corpus)
