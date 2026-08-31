# Plugin surface×component support matrix

Status: Final, evidence-bounded. This is the artifact whose absence lets “what a plugin contains” drift across the estate. Plugin pages should reference it under S1/S2 instead of restating another flat list.

**States are evidence-bounded:**
- `supported` — a cited page establishes it.
- `unsupported` — a cited page establishes the negative.
- `unknown` — the in-scope docs are silent. **Silence is never converted to `unsupported`.**

Every `supported`/`unsupported` cell carries a source. `unknown` is itself a finding: it marks a cell the docs never answer and the product/docs team must confirm. Sources on `code.claude.com` are cited because that property is the canonical owner of Claude Code authoring (see the page-ownership model); it is a *source*, not an audit target.

## Cowork vs Claude Code

| Component | Cowork | Claude Code | Source(s) |
|---|---|---|---|
| Skills | supported | supported | plugins/overview; cowork/guide/plugins; code.claude.com/plugins |
| MCP connectors | supported | supported | cowork/guide/plugins; plugins/overview; code.claude.com/plugins |
| Slash commands | supported | supported | cowork/guide/plugins; code.claude.com/plugins-reference |
| Sub-agents | supported | supported | cowork/guide/plugins; code.claude.com/plugins-reference |
| Hooks | supported | supported | cowork/guide/plugins ("skills, connectors, subagents, slash commands, or hooks"); code.claude.com/plugins-reference |
| LSP servers | **unknown** | supported | Claude Code: code.claude.com/plugins-reference. **Cowork: docs silent — unknown, NOT unsupported.** |
| Background monitors | **unknown** | supported | Claude Code: code.claude.com/plugins-reference. Cowork: silent → unknown. |
| Themes | **unknown** | supported | Claude Code: code.claude.com/plugins-reference. Cowork: silent → unknown. |
| `bin/` executables | **unknown** | supported (conditional) | Claude Code: code.claude.com/plugins-reference; note it is excluded from plugins distributed via claude.ai org settings. Cowork: silent → unknown. |
| Settings defaults | **unknown** | supported | Claude Code: code.claude.com/plugins. Cowork: silent → unknown. |

**Reading:** do not read the `unknown` cells as "Cowork supports less." They mean the Cowork docs do not state it. The single highest-value edit in the slice is turning the Cowork `unknown` cells into cited `supported`/`unsupported`.

## Where plugins run

As retrieved on **2026-08-31**, support guidance says plugins can be installed and used in **web Chat**, **Desktop Chat**, and **Cowork** on paid plans. Skills bundled in a plugin work across all three; hooks and sub-agents run only in Cowork and appear disabled in Chat. Source: `https://support.claude.com/en/articles/13837440-use-plugins-in-claude`.

Claude Code plugin support is separately established by `code.claude.com/docs/en/plugins` and its reference.

This conflicts with `cowork/guide/plugins`, which says plugins aren't used in Chat. The matrix must preserve that as a **live availability contradiction**, not pick either statement as settled truth. The availability owner needs to resolve it.

**Note on P2/P3 (correctness, distinct from coverage):** `plugins/overview` *omits* hooks from its component list while cowork/guide/plugins includes them — a same-surface **contradiction** to reconcile, not a support fact. Likewise the org-management availability contradiction (P3) is a correctness defect the matrix does not resolve; it is flagged for the availability owner.

## Further surfaces (each documents its own model)

Evidence-bounded, kept brief; each needs its own confirmed row.

- **Claude Tag** — defines a plugin as **skills** (supported; source: claude-tag/admins/skills-repo, /concepts/glossary, /admins/add-connections). It treats connections as a *separate* concept, so other components as plugin parts are **unknown** here (not asserted unsupported). Never links the canonical `/docs/plugins/overview`.
- **Claude for Government (Desktop)** — skills, slash commands, sub-agents, hooks `supported` (source: government/desktop/plugins, /config/plugins-and-connectors); a plugin's declared **local MCP server is disabled and does not run** (source: government/security-and-data-handling) — a declared-but-disabled state, which is why the matrix needs *enabled/disabled* alongside supported/unsupported.
- **Claude Desktop on 3P** — MCP connectors, skills, slash commands, hooks, sub-agents `supported` (source: third-party/claude-desktop/extensions).
- **Claude for M365** — surfaces connectors + skills; consumes the `claude-for-msft-365-install` plugin but documents no plugin-*authoring* model, so authoring is `unknown`/not-applicable here (source: office-agents/connectors-and-skills, /fsi-plugins).

## Why this shape
Rows = surfaces, columns = components, cells carry an evidenced state + source (+ an enablement note where declaration ≠ runtime). That makes S2 machine-checkable: a page's component enumeration is checked against the evidenced row for the surface it addresses, and `unknown` cells are surfaced as the confirmation backlog rather than asserted either way.
