# docs-conformance-gate — Work Log & Claude-Use Disclosure

This log is the workflow disclosure for the Claude Docs take-home (Technical Documentation & Content Engineer, Claude Docs). It records each working session, the surface that did the work, and the six-hour on-clock accounting. Pre-build orientation is carried forward so the disclosure is self-contained.

The assignment invites Claude transcripts/chats/workflows and states usage "won't count for or against you." This log is the primary Claude-use record; the raw chat session is not submitted.

**AI tools disclosed by material contribution.** Claude (via Claude Code) is the primary build surface for the audit, standard, and checker. A second AI tool was used only for the initial site orientation and some checker-approach research — as a stability fallback while a Claude Code issue on this machine was resolved — and is noted where it contributed below.

## Clock accounting

- **Cap:** ~6 hours on-clock. Over-run is allowed if the state at the 6-hour mark is clearly marked.
- **Counted budget at Session 2 start:** 0:00. Prior orientation was reclassified off-clock (see Session 1).
- **On-clock** = real audit/build actions. Repo scaffold, reading the plan, and breaks are off-clock. Breaks: stop, break, resume.

## Session 1 — disclosed pre-build orientation (OFF-CLOCK)

- **2026-08-26, second AI tool (stability fallback while a Claude Code issue was resolved), ~8 min (reclassified off-clock 2026-08-31).** Live-site orientation of the public Claude Docs estate *before* any slice was chosen. Ruled out Skills page-count sparsity as an unsupported defect (sparsity is not a defect without reader-journey evidence). Produced no deliverable content — it ruled a hypothesis out. Output: `preliminary_site_scan.md` (retained as provenance, not a finding).
- **Checker-approach research (second AI tool, 08-26/27).** Compared Vale, markdownlint, textlint, Lychee, and a small corpus-aware script. Provisional direction: the smallest deterministic checker that enforces one Part 1 finding; prefer a transparent corpus scanner with inspectable rules + tests for cross-page/lifecycle claims; non-compensating verdict precedence (a gating failure can't be offset by clean prose); positive + negative fixtures; real-corpus output.
- **Repo scaffold (Claude Code, 2026-08-31 00:21 ET).** Private repo `joeybwrites/docs-conformance-gate` created + cloned. Infrastructure only; no findings or deliverable content.

**Method note (double-blind):** the orientation formed a prior hypothesis — lifecycle / capability-model language drift across Plugins surfaces. That prior is **sealed**. Session 2's Part 0 re-audits the estate independently and compares against the prior only after reaching its own finding, so the committed problem class is not pre-decided.

## Session 2 — on-clock build (Claude Code)

- **Surface:** Claude Code. Working brain sealed for take-home focus; this log and all deliverables carry no unrelated private content.
- **Clock START: 2026-08-31 1:08 PM ET.**

### Part 0 — bounded inventory (on-clock)

- Independent inventory of the in-scope `claude.com/docs` estate from `llms.txt`. In scope: Connectors, Cowork, Claude for M365, Plugins, Claude Tag, Skills. **Out of scope:** `platform.claude.com/docs`, `code.claude.com/docs`.
- Goal: surface the top problems with page-level evidence, then confirm ONE problem class to thread through Parts 2–3. Part 3 needs a deterministic, machine-checkable rule.
**Inventory — in-scope estate from `llms.txt` (pulled 1:08 PM ET):**

Assignment-named estate (Background): Connectors, Cowork, Claude for M365, Plugins, Claude Tag, Skills.

| Surface | Pages in `llms.txt` |
|---|---|
| Claude Tag (`claude-tag/`) | ~63 |
| Connectors (`connectors/`) | ~37 |
| Claude for M365 (`office-agents/`) | 13 |
| Cowork (`cowork/`) | 6 |
| Skills (`skills/`) | 2 |
| Plugins (`plugins/`) | 2 |

Also on `claude.com/docs` but NOT named in the assignment's estate list: Claude Science (~28), Claude Desktop on 3P (`third-party/`, ~35), Claude for Government (~40), Welcome/index.

**Observations recorded as hypotheses to TEST, not findings:**
1. The Background's enumeration of "Claude's apps" is already narrower than the live estate (Science, Government, 3P Desktop unmentioned).
2. Skills / Plugins / Connectors are cross-cutting primitives — each recurs inside multiple surfaces (Cowork installs plugins; M365 `connectors-and-skills`; Claude Tag `skills-repo`; Government desktop `plugins`/`skills`; 3P desktop `extensions` = MCP/plugins/skills/hooks). Same primitive, many homes → candidate for definition/lifecycle drift, which is corpus-level (cross-page), not per-page.
3. Page-count asymmetry (Skills/Plugins at 2 each vs. Connectors ~37, Claude Tag ~63) is recorded as **raw data only** — per the method note, sparsity is not a defect without reader-journey evidence.

**Next on-clock action:** sample representative pages across surfaces to surface concrete, page-level defects before naming a problem class. Priors stay sealed.

**Part 0 sampling (13 pages, 6 in-scope surfaces + docs home).** Two robust problem classes surfaced independently (full evidence + quotes in `notes/findings_pool.md`): (A) cross-surface canonical-vocabulary drift for Skills/Plugins/Connectors (definition, component set, availability, terminology differ per surface — corpus-level); (B) non-canonical internal-link forms (doubled `/docs/docs/` prefix on landing components + alias paths — verified to resolve, so a canonicalization defect, not 404s). Two "verify before asserting" corrections logged (D4 alias, home-page links) — both looked like broken links, both resolve. **Not committed:** the problem class is ratified with Joey after his independent scan + the prior unseal.

**Convene + commit (Joey ratified): slice = Plugins, framing = conformance not rewrite.** Three-way compare (Joey / the AI assistant / unsealed prior) all converged on Plugins; divergence was depth (Joey) vs consistency (the AI arm), resolved via "required-element presence" bridging both. Joey's cross-property question surfaced the mechanism: "plugin" spans two unreconciled models (Claude Code full vs Cowork subset), no surface×component matrix in-estate. code.claude.com read for CONTEXT only (out-of-scope, to inform an in-scope IA proposal — not audited as a deliverable).

**Part 1 — Audit memo DRAFTED** (`audit/part1_audit_memo.md`): slice justification, 5 prioritized problems (root-cause first), merge/redirect treatment (reinforce-by-reference, scope banners, no deletions), proposed IA, and measurement (conformance gate as leading indicator + structural journey audit + telemetry as ground truth). AI-assisted draft; Joey voices/finalizes. Checker/measurement design seeded in `notes/checker_design.md`. Next: Joey redlines Part 1 → Part 2 (the standard).
