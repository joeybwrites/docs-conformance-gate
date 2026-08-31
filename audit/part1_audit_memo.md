# Part 1 — Audit Memo: Plugins

## Slice, and why Plugins

The take home suggested **Skills** / **Plugins** / **Connectors** as the cross-cutting primitives. I looked at all three plus **Cowork**, **Claude Tag**, and **Claude for M365**, and chose **Plugins**.

Plugins is the *compositional* primitive: a plugin is a container for the others — skills, connectors, slash commands, sub-agents, and more. Its documentation therefore has to reconcile every other primitive's vocabulary in one place, which makes it the surface where the estate's standardization gaps concentrate and compound. Connectors, by contrast, is the healthiest primitive (complete lifecycle coverage, deep left-nav), and Claude Tag is the best-structured product section overall. I use both as positive controls for the target state — not as the problem.

## 1. What's wrong (prioritized)

**Headline: "plugin" has no canonical definition anywhere in Claude Docs, because the term spans two different capability models the docs don't currently reconcile**

**P1 — Two unreconciled plugin models; no surface×component matrix.** *(root cause; everything below is a symptom)*
- A **Claude Code** plugin can contain skills, agents, hooks, MCP servers, LSP servers, background monitors, themes, `bin/` executables, and default settings (documented on code.claude.com).
- A **Cowork** plugin, per claude.com/docs, is a subset: skills, connectors, agents, hooks.
- Nowhere on claude.com/docs does one artifact state which components each surface supports. So a Cowork user cannot learn what a *Cowork* plugin can contain without leaving to a Claude-Code-scoped property (code.claude.com) that documents a superset they may not be able to use. Fix the canonical model + matrix and the drift, the sparseness, and the off-property offloading all become enforceable.

**P2 — The "what a plugin contains" definition drifts four ways.**
- `plugins/overview`: "MCP connectors, skills, slash commands, and sub-agents" (4, no hooks)
- `cowork/guide/plugins`: "skills, connectors, subagents, slash commands, or hooks" (5, +hooks)
- `connectors/building/what-to-build`: "an installable bundle of skills and connectors" (2–3)
- `claude-tag/admins/skills-repo`: "a plugin bundles one or more skills together" (skills only)

Any two of these pages give a reader a different answer to "what is a plugin."

**P3 — A hard availability contradiction (ships broken).** `plugins/overview` says org-wide plugin management is *"coming in the weeks ahead"* (unreleased); `cowork/guide/plugins` documents administrators requiring org-wide plugins that *"install automatically"* (shipped). One page says future, one says present.

**P4 — The plugin pages assume prerequisites and offload setup off-property.** The overview and submission pages name their component primitives without defining or linking them in place, and route the actual "how to build/configure" to code.claude.com. The submission page alone links out to four other properties (code.claude.com ×4, support.claude.com ×2, platform.claude.com ×2, claude.com/plugins). A reader who lands cold can't form a working mental model without leaving. This is the reader-facing cost of P1.

**P5 — Terminology + link hygiene (individually minor, cheap, exactly what a gate prevents).** "sub-agents" vs "subagents"; the docs home page emits every product link with a doubled `/docs/docs/...` prefix (resolves via redirect tolerance, but duplicate-URL and fragile); `cowork/guide/plugins` links an alias path (`/docs/cowork/3p/extensions`) absent from the index; undated promissory language ("coming in the weeks ahead") will rot.

## 2. Delete / merge — and what happens to readers on those URLs

**Delete: nothing.** No page here is dead weight; the problem is fragmentation and missing canon, not necessarily a surplus of information. Any propsective deletes could happen after page visibility has been resolved and user behavior/page traffic gives metrics and information about where users are congregating for specific information.

**Merge / consolidate under one banner** (the model is Skills and Claude Tag — each a coherent, self-contained section):
- Establish a single canonical Plugins section on claude.com/docs that owns the cross-product model: what a plugin is, the component set, the **surface×component support matrix**, availability, scopes, and the create/convert/install/marketplace flow.
- **Pull forward** from code.claude.com (`/en/plugins`, `/en/plugins-reference`) and `plugins/submit` only the *cross-product* concepts + the matrix. **Leave on code.claude.com** the genuinely Code-specific mechanics — the CLI (`claude plugin *`, `--plugin-dir`), the `~/.claude` layout, and the Code-only components (LSP, monitors, themes, `bin/`, the full Claude Code hook-event catalog).
- **Reinforce by reference, not by copy.** The canonical definition + matrix live in exactly one page; every other page links or embeds it. Repeating the definition inline is what produced the four-way drift in P2 — re-duplicating it would reseed the same problem. Reader reinforcement, single source of truth.

**What happens to readers on the affected URLs:**
- The code.claude.com plugin pages **stay** (they serve Claude Code developers) and gain a scope banner — "This covers Claude Code plugin specifics; for the cross-product plugin model and Cowork, see claude.com/docs/plugins" — plus an upward link. No redirect, no broken bookmark.
- Any consolidated or renamed in-estate page gets a redirect from its old path to the canonical one, so existing links and search results resolve.
- The doubled-prefix and alias links are rewritten to canonical form, so redirect tolerance stops being load-bearing.

## 3. Proposed information architecture (and what it takes to get there)

Target section, modeled on Skills / Claude Tag self-containment. Starting proposal, not final:

- **Overview**
  - What a plugin is — the one canonical definition
  - Plugin components + **surface×component support matrix** (Cowork vs Claude Code) — the centerpiece artifact
  - Plugin scopes + availability — single source; resolves the P3 contradiction
- **Create a plugin**
  - In Cowork — the full local flow
  - In Claude Code — short section + link out to the expansive code.claude.com docs
- **Convert / bundle existing skills & connectors into a plugin**
- **Next steps**
  - Discover & install plugins from the marketplace
  - Set up a marketplace
  - Reference (link out to code.claude.com plugins-reference)

**What it takes to get there:**
- Author the canonical artifact *first*: the surface×component matrix + the single definition. Everything else references it.
- Adopt a frontmatter `assumes:` convention (declared prerequisites per page) so orientation becomes enforceable — see §4.
- Redirects for any moved/renamed page; scope banners on the code.claude.com plugin pages.
- Scope estimate: a section consolidation + one net-new canonical page + redirects — **not** a rewrite of every plugin-adjacent page. The interconnected pages get re-pointed at canon, not rewritten.

## 4. Measurement — and how you'd instrument it

The improvement is real only if the plugin section becomes **self-orienting** (a cold reader forms a working model without leaving the estate) and **internally consistent** (no page contradicts the canon). Both are measurable.

**Leading indicator — the conformance gate (Part 3), run in CI:**
- **Prerequisite-bridging violations.** Each page declares an `assumes:` budget; the gate flags any core concept a page uses that is neither assumed nor linked to its canonical definition on first mention. Metric: unbridged-prerequisite count per page, and % of plugin pages at zero. This is the direct measure of "does the page assume what it shouldn't" — P4 made countable.
- **Component-set conformance.** Pages enumerating plugin components must match the surface-scoped canonical set; divergence, or a Code-only component named as universal, is flagged (P1/P2).
- **Off-property offloading.** Plugin pages whose only path to a core concept is an outbound link to code.claude.com / support.claude.com (P4).
- **Link + term hygiene.** Non-canonical link forms, terminology violations, decaying-time language (P5).

**User-journey audit (structural, not a vibe-grade).** Define the canonical reader tasks and their minimal in-estate page paths — "understand what a plugin is and what it can contain" (→ Overview); "install a plugin in Cowork" (→ Overview → install → marketplace); "prepare a plugin for submission" (→ Overview → submit). The gate checks each path is traversable following only in-estate links, with every concept bridged and no forced off-property hop for a core step. A break is a located failure, not an opinion.

**Ground truth — telemetry (the lagging signal):**
- Off-property exit rate on plugin pages (clicks out to code.claude.com / support).
- Internal-search zero-result rate for plugin queries.
- "Was this helpful" votes and plugin-tagged support tickets.
- Where available, task-completion funnels for the journeys above.

The gate predicts; telemetry confirms. **Target state:** the surface×component matrix exists and is linked from every plugin page; zero unbridged-prerequisite violations in the Plugins section; the off-property exit rate on the overview/install pages falls; and "what can a plugin contain / does Cowork support X" tickets drop.
