# Part 3 — Plugin documentation conformance gate (prototype)

A small, deterministic checker that enforces a machine-checkable subset of the plugin documentation standard (`../standards/plugin_style_guide.md`) and runs on a real slice of Claude Docs. Stdlib Python, no dependencies, no model in the loop — its verdicts are reproducible and reviewable. This README states only what the implementation actually does.

The full rule set and the designed-but-not-built gate (the page classifier, terminality as a team-sourced declaration, the duplication ceiling) live in `../notes/checker_design.md`. This prototype builds one vertical slice end to end.

## What this prototype checks

| Rule | Enforces |
|---|---|
| **S4** | Prerequisite bridging — the **first reader-visible mention** of a concept must itself link to that concept's owner (unless the concept is in `assumes:` / `canonical_for:`). A later link does not cure an unlinked first mention. |
| **S5** | Contextualized cross-property handoff — an off-property link must be framed and either carry a `#anchor` or target a registered dedicated destination. **This is a high-recall framing *proxy* (presence of an ownership cue or a summary clause); it does not prove the prose is a genuinely adequate summary + ownership explanation.** |
| **S6** | Link form — no doubled `/docs/docs/` prefixes |
| **S3** | *Possible* contradiction of the evidenced state — regex-detected contradiction **candidates** (curated `contradiction_patterns`) with a negation guard. **Deliberately not an automatic Reject** (see Verdicts). |
| **FM** | Frontmatter contract — `title`, `content-type`, `assumes`, `canonical_for` present, with `assumes`/`canonical_for` as arrays. Partial/malformed frontmatter is flagged and disables exemptions (so a scalar `assumes:` can't silence S4). |

Fenced ` ```code``` ` blocks and `` `inline code` `` are blanked before scanning, so documentation examples aren't flagged as live claims.

Declared inputs live in `registry.json` (concept→owner registry, off-property hosts, dedicated destinations, cues, severities, contradictions) and in each page's frontmatter — all maintained *with* the docs.

## Verdict schema (adjustable levers)

Findings roll up into one **non-compensating** verdict per page — the page's tier is its *worst* finding.

| Verdict | Triggered by | Exit |
|---|---|---|
| **Ship** | no findings | pass (exit 0) |
| **Ship with Notes** | only `note`-severity findings (S6) | pass (exit 0) |
| **Revise** | any `revise`-severity finding (S3, S4, S5, FM) | block |
| **Reject** | any `block`-severity finding | block |

**Honest limitation:** with the default levers, the automated gate reaches **up to Revise**. **Reject is not auto-assigned**, because the checker cannot adjudicate a contradiction's polarity beyond a negation guard, nor tell a *stale* claim from the *newer correct* one — so a detected contradiction is surfaced as an **owner decision** (Revise), not an automatic Reject. Reject remains in the schema as a human/owner disposition, or as a lever: set `severities.S3 = "block"` in `registry.json` to make contradictions auto-Reject if an org wants that stance.

**Levers, not code.** The rule→severity map, tier names, `contradiction_patterns`, and `batch_clauses` all live in `registry.json`; retune them without touching `conformance_gate.py`. Worked examples per tier are in `fixtures/verdicts/` (`NOTES.md` has the note returned to the owning team).

**Batch verdict.** Point the gate at many pages (a PR's changeset) and it emits one **batch disposition**, non-compensating across the set — the worst page holds the batch. Exit code = number of blocking files (Revise/Reject), capped at 100; Ship / Ship with Notes exit 0.

## Input contract

The gate expects **one actual doc page with top-level frontmatter.** A pre-standard page or a meta-doc (like `standards/plugin_overview_before_after.md`) has no valid frontmatter, so it gets an FM finding and its S4 concept results may be phantoms. Run the gate on pages, not meta-docs.

## Run it

```bash
python test_gate.py                       # expectation-based regression suite (asserts verdicts)
python fetch_corpus.py                    # pull the curated real-corpus slice into corpus/
python conformance_gate.py fixtures/      # ALL fixtures (recursive: rule, verdict, rigor)
python conformance_gate.py corpus/        # the live 5-page slice
python conformance_gate.py --json corpus/plugins_overview.md
```

`README.md` / `NOTES.md` are skipped when scanning a directory (repo meta-files). Full captured output: `sample_output.txt`.

## What it found on the real corpus

`fetch_corpus.py` pulls a **curated 5-page slice** of the live docs — it does **not** derive the full corpus from `llms.txt`. That slice, run 2026-08-31, produces **62 raw findings**, all pages Revise. These are the checker's **raw output, not an adjudicated list of confirmed defects** — every page's FM finding is expected (no live page carries the proposed frontmatter yet), and a share of the S4 count is downstream of that same missing frontmatter. The table below is the machine's read, with the signal worth a human's attention called out:

| Page | Raw findings | Signal worth a look |
|---|--:|---|
| `docs/index` (home) | 30 | 26 doubled `/docs/docs/` links (S6) — the estate's front door |
| `plugins/submit` | 11 | unlinked-first-mention primitives + unframed off-property handoffs |
| `plugins/overview` | 8 | primitives named before they're linked; bare off-property handoffs |
| `cowork/guide/plugins` | 7 | names the primitives, links none at first mention |
| `connectors/overview` | 6 | unlinked-first-mention primitives |

Every page also carries an FM finding, and because missing frontmatter disables the `assumes:`/`canonical_for:` exemptions, some S4 findings on these pages may be phantoms — the checker says so in the FM finding itself. The 62 is a starting point for triage, not a defect count to report upward.

**The 10-of-17 "cross-reference pages don't link plugins" figure is design evidence** from a broader estate sweep — it is *not* exercised by this five-page run, which is a focused demonstration slice.

## Deployment reality (before this is a CI gate)

This becomes a CI gate only after an adoption strategy exists (see Part 4) **and** a migration path: because every current live page lacks the proposed frontmatter, a naive turn-on would flag the whole estate. Deployment needs a **baseline / report-only phase**, a **changed-pages-only rule**, or a staged frontmatter rollout — not a hard block on day one.

## Where rigor testing hardened it (and the honest residue)

Tested against the real before/after and corpus; the following were found and fixed:
- **S5 framing FP** — registered destinations are framed by a descriptive label; the strict cue/word test applies only to arbitrary off-property links.
- **`plugins-reference`** registered as a whole-page destination.
- **FM contract** — required fields validated; malformed frontmatter is flagged, not silently honored.
- **Fenced/inline code** ignored, so examples aren't flagged.
- **S3 safety** — a negation guard (so "not available in Chat" / "do not say … available" aren't treated as positive claims) and a downgrade from auto-Reject to owner-decision, because source adjudication isn't implementable deterministically here.
- **S4 first-mention** — enforces the written rule (first mention must carry the link), guarded by `fixtures/fail_s4_first_mention.md`.

**Residue, stated honestly:** legal/policy links can still be flagged as unframed handoffs (a registry-tuning call); findings aren't de-duplicated; S5 is a framing proxy, not a semantic judge; S3 only catches curated patterns, not novel contradictions.

## Evaluating the checker itself

**False-positive tolerance:** tuned toward recall — a missed bridge/handoff confuses a reader; a false flag costs a writer ~10s. The dominant FP source (missing frontmatter) is designed to disappear as pages adopt the standard, demonstrated by `fixtures/pass_overview.md` running clean.

**Regression suite:** `test_gate.py` asserts the expected verdict and rule set for every fixture, including the hardening negatives (same-line first mention, inline code, HTML comments, vague S5 labels, lookalike owner URLs, block-list frontmatter arrays). Run it as the regression gate — `fail_*` must fire, `pass_overview` must stay clean. A concept frequent across the estate but absent from `registry.json` signals the registry going stale.

**Anti-staleness (design intent):** wired into a docs-PR CI job (none is included here) it would fail loudly on every change; declared inputs live with the docs; and it is deterministic, so a reviewer can always see *why* a line was flagged.

## Files

- `conformance_gate.py` — the checker
- `test_gate.py` — expectation-based regression suite (asserts verdict + rules per fixture)
- `registry.json` — declared inputs + levers
- `fetch_corpus.py` — pulls the curated 5-page slice
- `fixtures/` — rule fixtures (incl. `fail_s4_first_mention.md`), `verdicts/` (per-tier + `NOTES.md`), `rigor/` (non-compensating, code-fence, and the six hardening negatives)
- `corpus/` — the fetched slice (gitignored; reproducible via `fetch_corpus.py`)
- `sample_output.txt` — captured run (all fixtures, corpus, the meta-doc demo, and JSON)
