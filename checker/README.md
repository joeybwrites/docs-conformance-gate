# Part 3 — Plugin documentation conformance gate (prototype)

A small, deterministic checker that enforces a machine-checkable subset of the plugin documentation standard (`../standards/plugin_style_guide.md`) and runs on the **real** Claude Docs corpus. Stdlib Python, no dependencies, no model in the loop — its verdicts are reproducible and reviewable.

The full rule set and the designed-but-not-built gate (the page classifier, terminality as a team-sourced declaration, the duplication ceiling) live in `../notes/checker_design.md`. This prototype builds one vertical slice end to end — two phases deep beats four thin.

## What this prototype checks

| Rule | Enforces | From the standard |
|---|---|---|
| **S4** | Prerequisite bridging — every core concept a page uses that isn't in its `assumes:` (or that it's `canonical_for:`) must link to that concept's owner | fixes fragmentation / P4 |
| **S5** | Contextualized cross-property handoff — off-property links must be framed (ownership/summary cue) and carry a `#anchor` unless the target is a registered dedicated task page | P4, correctly scoped |
| **S6** | Link form (bonus) — no doubled `/docs/docs/` prefixes | P5 |

Declared inputs live in `registry.json` (the concept→owner registry, off-property hosts, dedicated task pages) and in each page's `assumes:` / `canonical_for:` / `content-type:` frontmatter — all maintained *with* the docs.

## Run it

```bash
python fetch_corpus.py                  # pull the real in-scope pages into corpus/
python conformance_gate.py corpus/      # run on the live corpus
python conformance_gate.py fixtures/    # run on the pass / fail fixtures
python conformance_gate.py --json corpus/plugins_overview.md
```

Exit code = number of files with findings (0 = clean), so it drops straight into CI. Full captured output: `sample_output.txt`.

## What it found on the real corpus

Five live pages, all with findings — **54 total** (`fetch_corpus.py` snapshot, 2026-08-31):

| Page | Findings | Highlights |
|---|--:|---|
| `docs/index` (home) | 29 | **26 doubled `/docs/docs/` links (S6)** — every product link on the estate's front door is a non-canonical duplicate URL |
| `plugins/submit` | 11 | unlinked primitives (S4) + 6 unframed/unanchored off-property handoffs (S5) |
| `plugins/overview` | 6 | `slash command` / `sub-agent` named but unlinked (S4); 3 bare off-property handoffs (S5) |
| `cowork/guide/plugins` | 5 | names skills, connectors, slash commands, sub-agents, hooks — links none of them (S4) |
| `connectors/overview` | 3 | `connector`, `slash command`, `sub-agent` unlinked (S4) |

The S4 spread is the fragmentation finding made countable: pages name the primitives but don't connect them. The home-page S6 cluster is a single, high-traffic, deterministic defect. Both are exactly the connective-tissue problems Part 1 named.

## Where the checker got it wrong (false positives — reported, not hidden)

1. **`plugin` flagged on `plugins/overview` and `plugins/submit`; `connector` on `connectors/overview`.** The live pages don't carry the standard's `canonical_for:` / `assumes:` frontmatter, so the checker can't know the page *owns* the concept. **This FP is the argument for the frontmatter:** the same page rewritten with `canonical_for: [plugin]` — `fixtures/pass_overview.md` — runs **clean**. The remedy is adoption of the standard, not loosening the check.
2. **Legal/policy links** (`directory-terms`, `directory-policy`) flagged as unframed handoffs. Conventionally bare; a registry-tuning call (register them, or add a policy allowance).
3. **No de-duplication** — a page that links the same URL twice on one line reports twice (`plugins/submit` line 16).
4. **Concept matching** is word-boundary and excludes the hyphenated `plug-in` (so Microsoft's "Enterprise SSO plug-in" is correctly *not* matched), but generic senses of "skill"/"agent" could still collide — mitigated by multi-word aliases and the bridge exemption (a link to a concept's owner is treated as S4 bridging, not an S5 handoff — the fix for the first FP round, see git history).

## Evaluating the checker itself

**False-positive tolerance, and why.** Tuned toward **recall**: a missed prerequisite bridge or an unframed handoff confuses a reader; a false flag costs a writer ~10 seconds to dismiss. But capped so the report stays credible — and the dominant FP source (missing frontmatter) is designed to disappear as pages adopt the standard, not by weakening the rule. Target and demonstrated: **near-zero FP on pages that carry the frontmatter** (`pass_overview.md` = 0).

**How I'd know if it degraded.** Violation count tracked in CI; a PR that adds unbridged concepts or bare handoffs raises it. Registry-coverage meta-check: a concept that appears often across the estate but is absent from `registry.json` signals the registry going stale. The fixtures are the regression suite — `fail_s4/s5/s6` must keep firing and `pass_overview` must stay clean.

**What keeps it from being a stale artifact in six months.** It runs in CI on every docs PR and fails loudly (nonzero exit blocks merge), so it can't rot silently. Its declared inputs — `registry.json` and the page frontmatter — live with the docs and are updated by the same PR that changes them. It is deliberately deterministic, so a reviewer can always see *why* a line was flagged.

## Files

- `conformance_gate.py` — the checker
- `registry.json` — declared inputs (concept→owner, hosts, task pages, cues)
- `fetch_corpus.py` — pulls the real corpus
- `fixtures/` — `pass_overview.md` (clean) + `fail_s4/s5/s6` (each fires one rule)
- `corpus/` — the fetched live pages
- `sample_output.txt` — captured run
