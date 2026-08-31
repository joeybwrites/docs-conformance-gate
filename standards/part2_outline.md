# Part 2 — Standard + Content-Type Template (ROUGH OUTLINE)

Status: rough scaffold, to be populated from Part 1 (P1–P5). Not locked.

The prompt requires rules "a reviewer — or a machine — could apply the same way twice." So every rule is written to be machine-checkable, which wires it straight into the Part 3 gate (`notes/checker_design.md`).

## A. Style spec — the conformance rules (excerpt)

Each rule: the rule (imperative, testable) · the P# it prevents · the machine check.

- **S1 — Canonical definition, single source.** Each core concept (plugin, skill, connector, MCP, slash command, sub-agent, hook) is DEFINED on exactly one canonical page; every other mention links to it, none restates the definition inline. [prevents P2 drift] — check: the definition phrase appears on >1 page = fail.
- **S2 — Surface-scoped claims.** Any statement of what a plugin contains / where it works names the surface (Cowork vs Claude Code) or references the canonical surface×component matrix. A surface-specific component stated as universal = fail. [P1] — check: component enumeration vs the registry's surface set.
- **S3 — Single availability source, dated.** Availability/lifecycle status lives in one place; no page contradicts it; no undated relative-time promises ("coming soon", "in the weeks ahead"). [P3, P5] — check: availability claim vs canonical + relative-time regex.
- **S4 — Prerequisite bridging.** Every core concept a page uses that is not in its `assumes:` frontmatter links to its canonical page on first mention. [P4] — check: R-B.
- **S5 — In-estate core path.** A core task step is completable without an outbound hop off-property; off-property links are "for more depth," never the only path. [P4] — check: R-D.
- **S6 — Canonical link form + terminology.** No doubled-prefix/alias link forms; canonical terms only (sub-agent). [P5] — check: R-C, R-E.

## B. Content-type template — "Capability overview page"

The type the plugin overview IS. A page of this type MUST contain, in order:

- **Frontmatter:** `title`, `assumes: [...]`, `canonical_for: [...]` (concepts this page is the single source of truth for)
- **What it is** — the 1–2 sentence canonical definition (if `canonical_for`), else a link to it
- **What it contains / components** — the component set; if surface-varying, the **surface×component matrix** (required for plugins)
- **Where it works + availability** — surface support + status, single-sourced, dated
- **Scopes / governance** (if applicable)
- **Get started / create** — the E2E happy path per surface, in-estate; link out only for depth
- **Next steps** — install / marketplace / reference links

Cross-cutting rules: every primitive named in any section links to its canonical page (S4); every "contains/works" claim is surface-scoped (S2) and single-sourced (S1/S3).

## C. Before/after rewrite target
Candidate: **`plugins/submit`** (carries P4 sparseness + a P2 definition conflict) OR **`plugins/overview`** (highest traffic, home of the matrix). [pending Joey]

## D. To populate from Part 1
- Fill the surface×component matrix from the two-models finding (Cowork subset vs Claude Code full set).
- Seed the concept registry (S1/S4) from the primitives list.
- Pull the exact drift quotes (P2) as the "what this rule prevents" examples.
