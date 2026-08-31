# Bounded Cowork and Claude Code plugin component matrix

Status: Content settled and evidence-bounded; a draft for Joey's review. This is the artifact whose absence lets “what a plugin contains” drift across the estate. Plugin pages should reference it under S1/S2 instead of restating another flat list.

**Scope — bounded, not all-surface.** This matrix covers exactly two surfaces, **Cowork** and **Claude Code**. It is deliberately not an all-surface matrix. Other surfaces (Claude Tag, Claude for Government, Claude Desktop on 3P, Claude for M365) are sketched under "Further surfaces" below and each requires a **separately confirmed row** — with its own cited sources — before it may be folded into the table. Do not read a surface's absence from the table as an evidenced state.

**Orientation:** in the table below, **components are rows** and **surfaces are columns**. Each cell carries an evidenced state for that component on that surface, plus a source.

**States are evidence-bounded:**
- `supported` — a cited page establishes it.
- `unsupported` — a cited page establishes the negative.
- `unknown` — the in-scope docs are **silent** on this component for this surface. **Silence is never converted to `unsupported`.**
- `not applicable` — the surface does **not have this component concept** at all, so the question does not arise. Distinct from `unknown`: `unknown` means the docs could answer but don't; `not applicable` means there is nothing to answer.

Every `supported`/`unsupported` cell carries a source. `unknown` is itself a finding: it marks a cell the docs never answer and the product/docs team must confirm. Sources on `code.claude.com` are cited because that property is the canonical owner of Claude Code authoring (see the page-ownership model); it is a *source*, not an audit target.

## Cowork vs Claude Code

| Component | Cowork | Claude Code | Source(s) |
|---|---|---|---|
| Skills | supported | supported | [plugins/overview](https://claude.com/docs/plugins/overview); [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins); [code.claude.com/plugins](https://code.claude.com/docs/en/plugins) (all retrieved 2026-08-31) |
| MCP connectors | supported | supported | [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins); [plugins/overview](https://claude.com/docs/plugins/overview); [code.claude.com/plugins](https://code.claude.com/docs/en/plugins) (retrieved 2026-08-31) |
| Slash commands | supported | supported | [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins); [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31) |
| Sub-agents | supported | supported | [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins); [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31) |
| Hooks | supported | supported | [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins) ("skills, connectors, subagents, slash commands, or hooks"); [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31) |
| LSP servers | **unknown** | supported | Claude Code: [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31). **Cowork: docs silent — unknown, NOT unsupported.** |
| Background monitors *(experimental, Code-only)* | **unknown** | supported *(experimental)* | Claude Code: [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31), documented as experimental. Cowork: silent → unknown. |
| Themes *(experimental, Code-only)* | **unknown** | supported *(experimental)* | Claude Code: [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31), documented as experimental. Cowork: silent → unknown. |
| `bin/` executables | **unknown** | supported (conditional) | Claude Code: [code.claude.com/plugins-reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31); note it is excluded from plugins distributed via claude.ai org settings. Cowork: silent → unknown. |
| Settings defaults | **unknown** | supported | Claude Code: [code.claude.com/plugins](https://code.claude.com/docs/en/plugins) (retrieved 2026-08-31). Cowork: silent → unknown. |

**Reading:** do not read the `unknown` cells as "Cowork supports less." They mean the Cowork docs do not state it. The single highest-value edit in the slice is turning the Cowork `unknown` cells into cited `supported`/`unsupported`. Cells marked *experimental* are documented for Claude Code only and may change or be withdrawn; treat them as provisional even where cited.

## Where plugins run

As retrieved on **2026-08-31**, support guidance says plugins can be installed and used in **web Chat**, **Desktop Chat**, and **Cowork** on paid plans. Skills bundled in a plugin work across all three; hooks and sub-agents run only in Cowork and appear disabled in Chat. Source: [support.claude.com/en/articles/13837440-use-plugins-in-claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) (retrieved 2026-08-31).

Claude Code plugin support is separately established by [code.claude.com/docs/en/plugins](https://code.claude.com/docs/en/plugins) and [its reference](https://code.claude.com/docs/en/plugins-reference) (retrieved 2026-08-31).

This conflicts with [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins) (retrieved 2026-08-31), which says plugins aren't used in Chat. The matrix must preserve that as a **live availability contradiction**, not pick either statement as settled truth. The availability owner needs to resolve it.

**Note on P2/P3 (correctness, distinct from coverage):** [plugins/overview](https://claude.com/docs/plugins/overview) *omits* hooks from its component list while [cowork/guide/plugins](https://claude.com/docs/cowork/guide/plugins) includes them. This is an **incomplete / inconsistent enumeration** to reconcile — one page's list is less complete than the other's — not a support fact, and not a direct contradiction (neither page asserts hooks are unsupported). Separately, the org-management availability contradiction (P3) is a correctness defect the matrix does not resolve; it is flagged for the availability owner.

## Further surfaces (each documents its own model)

Evidence-bounded, kept brief. Each surface below needs its own **separately confirmed row** — with cited sources — before it may be added to the matrix above; these sketches are not yet table rows.

- **Claude Tag** — defines a plugin as **skills** (supported; source: [claude-tag/admins/skills-repo](https://claude.com/docs/claude-tag/admins/skills-repo), [/concepts/glossary](https://claude.com/docs/claude-tag/concepts/glossary), [/admins/add-connections](https://claude.com/docs/claude-tag/admins/add-connections), retrieved 2026-08-31). It treats connections as a *separate* concept, so other components as plugin parts are **unknown** here (not asserted unsupported). Never links the canonical [/docs/plugins/overview](https://claude.com/docs/plugins/overview).
- **Claude for Government (Desktop)** — skills, slash commands, sub-agents, hooks `supported` (source: [government/desktop/plugins](https://claude.com/docs/government/desktop/plugins), [/config/plugins-and-connectors](https://claude.com/docs/government/config/plugins-and-connectors), retrieved 2026-08-31); a plugin's declared **local MCP server is disabled and does not run** (source: [government/security-and-data-handling](https://claude.com/docs/government/security-and-data-handling), retrieved 2026-08-31) — a declared-but-disabled state, which is the motivating case for the proposed *enabled/disabled* dimension noted under "Why this shape."
- **Claude Desktop on 3P** — MCP connectors, skills, slash commands, hooks, sub-agents `supported` (source: [third-party/claude-desktop/extensions](https://claude.com/docs/third-party/claude-desktop/extensions), retrieved 2026-08-31).
- **Claude for M365** — surfaces connectors + skills; consumes the `claude-for-msft-365-install` plugin but documents no plugin-*authoring* model, so authoring is **not applicable** here — the surface has no authoring concept, distinct from `unknown` (source: [office-agents/connectors-and-skills](https://claude.com/docs/office-agents/connectors-and-skills), [/fsi-plugins](https://claude.com/docs/office-agents/fsi-plugins), retrieved 2026-08-31).

## Why this shape
Components are rows, surfaces are columns, and cells carry an evidenced state + source. That makes S2 machine-checkable: a page's component enumeration is checked against the evidenced column for the surface it addresses, and `unknown` cells are surfaced as the confirmation backlog rather than asserted either way.

**Future work — an enabled/disabled dimension.** The current matrix records only `supported` / `unsupported` / `unknown` / `not applicable`. The Claude for Government case (a declared-but-disabled local MCP server) shows that *declaration ≠ runtime*, so a full model would also carry an **enabled/disabled** state alongside support. That dimension is **proposed, not yet populated** — the table above does not represent it — and is flagged here as future work.
