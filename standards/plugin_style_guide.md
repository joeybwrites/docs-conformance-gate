# Plugin documentation standard (style-guide excerpt + content-type templates)

Status: Final. The plugin documentation isn't broadly missing information. It's largely complete across the estate but distributed across page hierarchies and properties, so readers have to reconstruct the lifecycle themselves. This standard establishes **clear page ownership, contextualized handoffs, and decision-critical summaries** without duplicating the Claude Code tutorial or reference. Each rule is written so a reviewer, or a machine in Part 3, can apply it the same way twice. Companion: `plugin_component_matrix.md`.

## Page ownership model (the spine)

| Page | Owns |
|---|---|
| `claude.com/docs/plugins/overview` | Cross-product concept, platform relationship, surface×component matrix, availability, lifecycle map, and concise surface-use orientation |
| `claude.com/docs/plugins/submit` | Submission readiness, eligibility, governance, review states, decision points, publication outcomes, exception recovery |
| `code.claude.com/docs/en/plugins` | The practical authoring tutorial (package anatomy, build steps, testing, debugging) |
| `code.claude.com/docs/en/plugins-reference` | Technical source of truth (schemas, paths, scopes, CLI, syncing, caching, troubleshooting, versioning) |
| `support.claude.com/en/articles/13837440-use-plugins-in-claude` | Full installation, use, customization, marketplace, and management procedures for web Chat, Desktop Chat, and Cowork |
| `code.claude.com/docs/en/discover-plugins` | Dedicated discovery and installation guidance for Claude Code |

A page shouldn't duplicate material another page owns. It **summarizes** the decision-critical facts where the reader makes a choice, then **hands off** to the owner.

## Governing principles

- **One owner per fact; everyone else summarizes and links.** The Part 1 drift, with plugins defined several different ways, is a duplication failure: pages restated definitions and diverged. Ownership and framed handoffs replace that duplication.
- **A page an agent can execute is a page a human can follow.** Agent-executable documentation needs explicit prerequisites, expected outcomes, validation, evidence, failure handling, and stop points — applied to **the steps that page owns**, not as one universal procedure imposed everywhere.

## A. Style rules (each: rule · problem it prevents · machine check)

| # | Rule | Prevents | Machine check (Part 3) |
|---|------|----------|------------------------|
| **S1** | **Canonical definition, single owner.** Each core concept (plugin, skill, connector/MCP, slash command, sub-agent, hook) is *defined* on exactly one owning page; every other mention summarizes at most one sentence and links. | P2 drift | Definition phrase appears on >1 page → fail. |
| **S2** | **Surface-scoped claims, matrix-backed.** A statement of what a plugin contains or where it runs names the surface or references the matrix, and matches the matrix's evidenced state for that surface. | P1 two-model collision | Component enumeration vs the matrix row for the named surface. |
| **S3** | **Single availability source, dated.** Availability/lifecycle status has one owner; no page contradicts it; no undated relative-time promises ("coming soon", "in the weeks ahead"). | P3 contradiction, P5 | Availability claim vs owner; relative-time regex in availability sections. |
| **S4** | **Prerequisite bridging.** Every core concept a page uses that is not in its `assumes:` frontmatter links to its owning page on first mention. | P4 / JF1 | For each registry concept mentioned and not in `assumes`, require a first-mention link. |
| **S5** | **Contextualized cross-property handoff.** Crossing from `claude.com/docs` to `code.claude.com` or `support.claude.com` is legitimate, not a failure. A handoff for a decision-critical step must (a) summarize the decision-critical information the reader needs, (b) state why the destination owns that step, and (c) link to the precise section. A dedicated task page may be linked at its root when the ownership registry identifies the whole page as the destination. **Flag unframed, premature, or ambiguous handoffs.** | P4 offloading (correctly scoped) | An off-property decision link must carry an adjacent summary and ownership sentence. Require a `#anchor` unless the target URL matches a dedicated task page in the ownership registry; an unregistered bare root or unframed link fails. |
| **S6** | **Canonical link form + terminology.** No doubled-prefix (`/docs/docs/…`) or alias link forms; canonical terms only ("sub-agent", not "subagents"). | P5 | Doubled-prefix / alias regex; term denylist. |
| **S7** | **Role-specific required sections.** A page's required sections are keyed to its owned role. **Creation page:** package anatomy, implementation steps, testing, debugging. **Submission page:** readiness, eligibility, required inputs, validation's relationship to review, review states, decision points, publication outcomes, exception recovery. **Lifecycle-map (overview) page:** definition, platform relationship, matrix, availability, surface-use orientation, lifecycle map. The orientation gives readers a concrete first-use path without duplicating the dedicated procedure owner. *A submission page must not duplicate the authoring guide's package tree or build procedure.* | JF2, fragmentation | Required-heading presence keyed to the page's declared `content-type` / role. |
| **S8** | **Owned steps are executable.** For the steps a page owns (per S7), each carries explicit prerequisites, an expected outcome, validation/evidence of success, failure handling, and marked decision/stop points for irreversible or user-decision actions — so an agent stops and asks and a human doesn't miss them. Applied per role; not a universal template. | high-consequence safety, agentic-usability | Owned procedure steps missing a prerequisites/outcome/validation block, or a submit/publish step with no marked stop point → fail. |

`assumes:`, `canonical_for:`, and `content-type:` are page frontmatter the standard introduces; they are the inputs S1/S2/S4/S7 check against and are maintained with the page (Part 3 anti-staleness).

## B. Content-type templates (role-keyed required sections)

### `content-type: lifecycle-map` (the overview)
Definition (owned) · platform relationship · **surface×component matrix** (reference, never restate) · availability (owned, dated) · **surface-use orientation** (a concrete first-use path plus a handoff to the full procedure owner) · **lifecycle map** (discovery → use → build → validate → submit → publish → maintain, each stage naming its owning page) · framed handoffs to build/reference. Every primitive linked [S4]; every "contains/works" claim matrix-backed [S2].

### `content-type: submission` (the submit page)
Readiness · eligibility · required inputs · how validation relates to review · review states · **decision & stop points** [S8] · publication outcomes · exception recovery. Summarizes consequential downstream facts (local validation, safety screening, pinning, marketplace sync) where the author decides, and links to the owner for mechanics [S5]. Does **not** restate the authoring package tree or build steps.

### `content-type: creation` (authoring tutorial — owned on code.claude.com; specified here only so the estate agrees on ownership)
Package anatomy · implementation steps · testing · debugging, each executable [S8].

## C. Before/after (Part 2 deliverable)
Applied to `plugins/overview` — see `plugin_overview_before_after.md`.
