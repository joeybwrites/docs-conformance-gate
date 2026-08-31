# Findings Pool — combined + ranked (Part 1 input)

Both arms land here AFTER independent scanning. Dedupe, rank, and pick the ONE problem class to thread through Parts 2–3. Part 3 needs a deterministic, machine-checkable rule, so the committed class must be operationalizable into a hard check.

## AI arm

### Sampling pass 1 — plugin-adjacent (skills/overview, plugins/overview, cowork/guide/plugins)

Concrete, page-level defects (evidence quoted). NOTE: these three pages were plugin-adjacent by selection, so a plugin cluster is expected — breadth test pending before trusting it as THE finding.

- **D1 — Availability CONTRADICTION (high, cross-page).** `plugins/overview`: *"Org-wide sharing and management are coming in the weeks ahead."* (future). `cowork/guide/plugins`: *"administrators can require certain plugins for everyone in the organization. Required plugins install automatically."* (present). One page says the capability is unreleased; another documents it as shipped.
- **D2 — Plugin-component definition drifts (high, cross-page).** `plugins/overview`: bundles *"MCP connectors, skills, slash commands, and sub-agents"* (4, no hooks). `cowork/guide/plugins`: *"skills, MCP connectors, subagents, slash commands, or hooks"* (5, WITH hooks). The definition of the core noun varies by page.
- **D3 — Terminology inconsistency (med, deterministic).** "sub-agents" vs "subagents"; component labeled "Sub-agents" vs "Agents" for the same thing.
- **D4 — Non-canonical alias link + journey mismatch (med, CORRECTED after verify).** `cowork/guide/plugins` links twice to `/docs/cowork/3p/extensions`. **Verified: NOT a 404** — it redirects to the `third-party/claude-desktop/extensions` page ("MCP, plugins, skills, and hooks"). Two real defects remain: (a) a non-canonical path alias not present in `llms.txt` (link hygiene); (b) worse — a Cowork "admin provisioning" link lands a normal Team/Enterprise admin on **Claude-Desktop-on-3P**-specific provisioning (managed config + filesystem), not the claude.ai admin-console path they actually need. Downgraded from "broken link"; the real defect is the journey, not a 404.
- **D5 — Decaying relative-time claims (med, deterministic).** "coming in the weeks ahead," "currently saved locally" — undated promissory language in availability sections, guaranteed to rot.
- **D6 — Authoring punted off-site (med, journey).** Canonical "create a skill/plugin" links route to `code.claude.com/docs` (out of scope); a Cowork reader's create-path leaves claude.com/docs.

**Candidate deterministic rules for Part 3 (from the above):** (a) internal-link integrity vs the real page set [D4]; (b) canonical-term conformance [D3]; (c) decaying-time-language lint [D5]; (d) the differentiator — cross-page claim consistency for a defined entity (plugin component set / availability) that per-file linters can't evaluate [D1, D2].

### Sampling pass 2 — breadth test (connectors/what-to-build, office-agents/connectors-and-skills, claude-tag/skills-repo)

**Verdict: the drift is estate-wide, not plugin-local. Same entity, different definition on every surface.**

**"What IS a plugin?" — four incompatible definitions:**
- `plugins/overview`: connectors + skills + slash commands + sub-agents (**4**)
- `cowork/guide/plugins`: skills + connectors + subagents + slash commands + **hooks** (**5**)
- `connectors/what-to-build`: "installable bundle of skills and connectors"; component list = Skills, MCP connector refs, slash commands (**3**); and separately "a plugin can contain: skills only / a connector / skills+connectors" (**skills+connectors only**)
- `claude-tag/skills-repo`: "A plugin bundles one or more skills together" (**skills only**)

**"What IS a skill?" — four glosses:**
- `skills/overview`: "directories containing instructions, scripts, and resources… a `SKILL.md` file"
- `claude-tag/skills-repo`: "a set of instructions that teaches Claude how to use a specific tool or process"
- `connectors/what-to-build`: "user-shared micro-workflows"
- `office-agents/connectors-and-skills`: "reusable task recipes"

**Distribution-model claim on ONE page only (unreconciled):** `what-to-build`: *"Skills are not a standalone directory type. Plugins are the distribution mechanism for skills—you can't submit a skill to the directory on its own."* `skills/overview` presents skills as independently creatable and never states this constraint.

**Three doc properties; core journeys leak across all three:** `claude.com/docs` (in scope), `code.claude.com/docs` (authoring — OUT of scope; `skills-repo` links it 5×), `support.claude.com/articles` (a third surface; `connectors-and-skills` routes "Use Skills" + custom-connector guidance there). The canonical "how to build/format" always lives off `claude.com/docs`.

**Terminology drift confirmed:** sub-agents / subagents / Agents for one concept.

### Independent finding (AI arm), NOT yet committed
The cross-cutting primitives — **Skills, Plugins, Connectors** (and sub-parts: slash commands, sub-agents, hooks) — have **no single canonical definition, component set, availability status, or terminology.** Every surface that re-documents them redefines them, and the canonical authoring path is punted to two other doc properties. This is a *unification/standardization* defect — exactly the layer the role owns — and it is **corpus-level**, which a per-file linter cannot catch.

**Part 3 deterministic rule this implies:** a **canonical-vocabulary conformance gate** — a registry declares, per primitive, its canonical definition, component set, availability/status, canonical term, and canonical authoring link; the checker scans every in-scope page, extracts where it defines/enumerates a primitive, and flags divergence. Non-compensating verdict (blind-reviewer-style): an availability contradiction [D1] = Block; a divergent component set [D2] = Revise; a terminology slip [D3] = warn. Plus deterministic sub-checks already evidenced: internal-link integrity [D4], cross-property/out-of-scope-link leakage, decaying-time language [D5].

### Sampling pass 3 — primitive hubs (skills/how-to, plugins/submit, connectors/overview, cowork/overview)

**Plugin component set — now a countable majority + outliers:**
- 4 (connectors, skills, slash commands, sub-agents), NO hooks: `plugins/overview`, `plugins/submit`, `connectors/overview` (**3 agree**)
- 5 (adds **hooks**): `cowork/guide/plugins`
- ≤3: `what-to-build` (skills+connectors[+slash commands]); `skills-repo` (skills only); `cowork/overview` ("and more")
- Note: the *operational install page* is the one that says hooks ARE a component → the 3 "overview" pages may be UNDER-specifying. A registry resolves it: human sets the true set, checker flags every divergent enumeration (no need to guess which is right).

**Terminology — canonical now clear:** "sub-agent" (hyphen) on `plugins/submit`, `connectors/overview`, `cowork/overview`; "subagents" only on `cowork/guide/plugins`. Canonical = hyphen; 1 clean violation. Deterministic.

**Canonical page missing a rule its siblings state (gap, checkable):** the plugin-as-distribution constraint — *"you can't submit a skill to the directory on its own"* (`what-to-build`), corroborated by `skills/how-to` and `connectors/overview` — is ABSENT from `skills/overview`, the primary skills page. Required-claim-presence check.

**Cross-property leakage — quantified:** `plugins/submit` routes to FOUR other properties: `code.claude.com` (×4), `support.claude.com` (×2), `platform.claude.com` (×2), `claude.com/plugins`. The "how do I build/ship" journey consistently leaves `claude.com/docs`. Deterministic per-page external-property link count.

**Availability has no single home:** `connectors/overview` = 5-row table; `plugins/overview` = 2-row; `what-to-build` = "Works in" row; `cowork/guide/plugins` = prose. Same facts, four formats, four locations — plus the D1 contradiction.

**Atomic spec facts (checker-friendly):** `skills/how-to`: "Claude.ai limits descriptions to **200 characters**"; "SKILL.md under **500 lines**"; name "max **64 characters**." Exactly the pin-to-canonical-value facts a conformance gate targets.

### Sampling pass 4 — anti-tunnel breadth (docs home `/index`, claude-tag/overview, office-agents/overview)

**NEW defect class (B): non-canonical internal-link forms.** The docs HOME page emits every product link with a doubled prefix — `/docs/docs/connectors/overview`, `/docs/docs/skills/overview` … all 9 cards. The Claude Tag hero repeats it (`/docs/docs/claude-tag/...`), while the SAME page's prose links use the correct single `/docs/...`. **Verified: these do NOT 404** — `/docs/docs/connectors/overview` resolves to Connectors overview via redirect tolerance. So the defect is canonicalization, not breakage: duplicate URLs for one page, emitted by the custom landing/hero components, latent-fragile if tolerance changes. Deterministic + highest-traffic (the estate's front door). Pairs with D4's alias path.
  - **Checker-design consequence:** a naive link-checker that only tests HTTP status PASSES these (they resolve). The real check must flag non-canonical link *form* (doubled prefix; alias paths absent from `llms.txt`), not just 404s. Strong "where the checker got it wrong" material for Part 3.

**Positive control for Part 2:** `claude-tag/overview` states availability cleanly in one place — "available on Team and Enterprise plans… not Free, Pro, or Max, or third-party." The model the scattered plugin/connector availability statements should conform to.

**Negative control:** `office-agents/overview` — clean single-prefix links, consistent per-app framing. Low-defect; the checker must NOT false-positive here.

### Part 0 conclusion — independent arm (13 pages, 6 surfaces + home). NOT committed; holding for Joey's arm + prior unseal.

Two robust, evidence-backed problem classes:
- **(A) Cross-surface canonical-vocabulary drift** [the differentiator] — Skills/Plugins/Connectors have no single definition, component set, availability, or term across surfaces. Corpus-level; per-file linters can't see it. Directly = the role's "unification/standardization layer."
- **(B) Non-canonical internal-link forms** [the deterministic quick-win] — doubled `/docs/docs/` prefix on landing components + alias paths; resolve today, but duplicate-URL and fragile.

**Recommended commit (pending ratification):** thread **(A)** through Parts 1–3 as the headline (it's the role); fold **(B)**, terminology, and decaying-time language in as additional rule families in the Part 3 gate. Part 3 = a **canonical-vocabulary + link-canonicalization conformance gate**: a registry (the Part 2 standard) declares the true term / component-set / availability / canonical-link-form per primitive; the checker flags divergence with non-compensating (blind-reviewer-style) verdicts, run on the real corpus with known false-positives.

## Joey arm

Independent scan of Connectors, Skills, Plugins, Cowork, Claude Tag, M365, Science, 3P (full text in `joey_findings.md`). Direction: **Plugins primary** (compositional surface — combines skills, connectors, slash commands, sub-agents); Connectors = healthy benchmark.

- **JF1 (high) — Plugin pages assume prerequisite knowledge, no local conceptual bridge.** Component terms named but not clickable / unexplained in place. Fix: a compact "What a plugin can contain" block — one-sentence defs + links + a composition example.
- **JF2 (high) — Submission page too sparse for a high-consequence workflow.** Leans on outbound links; no self-contained "I have a plugin → what's reviewed, what to prepare, what's next." Fix: staged checklist (prereqs → anatomy → validation/security → submit → review → publish → maintenance).
- **JF3 (med) — Skills guidance concentrated on one page; examples punt to GitHub** vs a graduated in-doc path.
- **Thesis:** the *most compositional* concept (Plugins) is among the *least self-explanatory*.
- **Joey's own flag:** leaning Plugins-update-pass, but "could be a hole to fall into considering how many interconnected pieces touch it."

## Ranked (post-convene) — three-way compare

**SLICE: all three arms converge on Plugins.** Joey (compositional, sparse base page) · the AI arm (drift thickest here) · **prior UNSEALED** ("lifecycle/capability-model drift across Plugins surfaces"). Two independent paths + the prior all land on Plugins → slice is robust.

**The arms DIVERGE on the PROBLEM — this is the whole game:**
- **Joey's lens = DEPTH/orientation.** Pages too sparse, assume prerequisites, punt examples. Naively scoped ("rewrite the plugin section") this is unbounded + editorial → NOT machine-checkable. **This is the hole Joey named.**
- **The AI arm's lens = CONSISTENCY/conformance.** The plugin *definition itself* contradicts across the estate (4 component lists; D1 availability contradiction; sub-agents/subagents). Deterministic → buildable as Part 3.

**Same root cause:** the base page is sparse AND assumes prerequisites *because there is no canonical definition of a plugin* — every surface improvises a partial one, so none can serve as authoritative orientation. Two angles on one disease: **no single source of truth for the compositional primitive.**

**The bridge (why Joey's arm is NOT sidelined):** "is this page well-oriented?" is un-checkable, but **"does this page contain the elements the standard REQUIRES?" is deterministic.** Convert quality → required-element presence, and Joey's depth findings become checker rules:
- JF1 "terms not clickable" → **every primitive named must hyperlink to its canonical page** (deterministic).
- JF1 "no local orientation" → **an intro page must contain the canonical 'What a plugin can contain' block** (required-section presence).
- JF2 "submission too sparse" → **the submission page must contain the required lifecycle sections** (required-heading presence).

## Committed problem class — RECOMMENDED (pending Joey's ratification)

**Slice: Plugins. Frame: conformance to a standard, NOT rewrite.** This subsumes BOTH arms and escapes the hole.

- **Part 1 (audit):** Plugins. Headline: the most compositional primitive has no canonical definition; each surface improvises → it is simultaneously *inconsistent* (AI arm) and *under-orienting* (Joey). Priority: (1) availability contradiction [ships broken]; (2) component-set drift [4 defs]; (3) orientation gap [cold readers can't form a model because there's no canonical model to show]. Connectors + Claude Tag = positive-control exemplars.
- **Part 2 (standard):** the canonical **plugin spec** — one definition, component set, availability, terminology + required orientation block + required lifecycle sections. Before/after = the submission page (fixes JF2 sparseness AND its definition conflict at once).
- **Part 3 (checker):** conformance gate enforcing Part 2. Rule families (all deterministic): (1) component-set conformance vs registry; (2) linked-vocabulary; (3) required-section presence; (4) availability-claim conformance; (5) terminology; (6) link canonicalization; (7) decaying-time language. **Prototype scope: 1–2 families end-to-end** (component-set + linked-vocabulary hit both arms) on the real corpus with known false-positives; rest designed, stubbed. Non-compensating, blind-reviewer-style verdicts.

**Why this beats "update the plugin docs":** bounded (spec + gate, not open-ended rewrite), deterministic (Part 3 rewards a working check), and it IS the role ("unification/standardization layer"). Joey's depth findings survive as Part 1 priorities, Part 2 required elements, AND Part 3 required-element rules.

## Reference map — sub-agent sweep A (connectors / skills / plugins / cowork / office-agents; 59 pages)

Answers Joey's "how many pages reference plugins, forward/backward" for these 5 surfaces. Sweep B (claude-tag + broader estate) still running.

- 19 pages reference plugins; 2 SELF, **17 cross-reference** (11 FORWARD, 6 BACKWARD).
- **HEADLINE: 10 of 17 cross-reference pages name plugins but do NOT link the plugin docs.** P4 quantified, and the baseline the checker's linked-vocabulary rule (R-B / S4) would flag.
- **The entire Claude for M365 (office-agents) surface links plugins ZERO times** — every mention points to GitHub, a blog, or a sibling office-agents page, including BACKWARD dependencies (`claude-for-msft-365-install`, the FSI plugin set) where the reader most needs the plugin docs.
- **`office-agents/fsi-plugins` is a full plugin-install guide living under office-agents, not `/docs/plugins/`, and links back to neither plugin doc** — a concrete merge/re-home candidate for §2 (misplaced content, not a deletion).
- Clean, well-linked cluster (= target state): connectors/overview + what-to-build + submission, and skills/overview + how-to — consistently link `/docs/plugins/overview` + `/docs/plugins/submit`.
- Several connectors "building" pages (index, review-criteria, after-publishing) treat plugins as a co-equal submission/build type but link only to GitHub or what-to-build, not the plugin docs.

Feeds: P4 (now quantified), the checker corpus + R-B baseline (10 known link-failures to test against), and §2/§3 (fsi-plugins re-home; M365 as the worst-connected surface).

## Reference map — sub-agent sweep B (claude-tag / third-party / government / claude-science)

- **~46 pages reference plugins** here (claude-tag 27, third-party 9, government 9, science 1). With Sweep A's 19, **~65 pages across the estate reference plugins** — a large blast radius, which is precisely why the definition must be single-sourced.
- **The drift is worse than the 4-way in Part 1 — it's 6–7 way, and the disagreement centers on the two most consequential components, CONNECTORS and HOOKS:**
  - claude-tag (glossary, add-connections#attach-plugins, skills-repo): **plugin = skills ONLY** (connectors explicitly a separate concept)
  - third-party/extensions: **5** — MCP connectors, skills, slash commands, hooks, sub-agents
  - government/desktop/plugins: **4** — skills, slash commands, sub-agents, hooks (NO connectors)
  - government/config/settings: skills, slash commands, sub-agents + "can also carry hooks and declare connectors"
  - (+ earlier: plugins/overview 4-no-hooks; cowork/guide 5-with-hooks; what-to-build skills+connectors)
- **CLAUDE TAG IS A DISCONNECTED ONTOLOGY ISLAND.** Its own skills-only plugin definition AND its own canonical anchor (`add-connections#attach-plugins`); **27 plugin references, ZERO links to `/docs/plugins/overview`.** Third-party + both government definition pages DO link the canonical page. The estate runs TWO parallel plugin canons.
- **The matrix needs an ENABLED/DISABLED dimension, not just present/absent:** government notes a plugin's declared local MCP server "is disabled and does not run" in Claude for Government. Component support is per-surface at the BEHAVIOR level, not just the declaration level.
- **Real Part-3 false-positive material:** the sweep correctly EXCLUDED "Enterprise SSO plug-in" (Microsoft's hyphenated term on entra-broker / connectors-m365) — not a Claude plugin. The checker's concept-matching must separate "plugin" from "plug-in"/generic uses. Concrete "where a naive checker gets it wrong" case.

Feeds: P1/P2 (drift upgraded 4-way → 6–7-way + the Claude Tag island); the Part 2 matrix (rows now include Claude Tag + a per-surface enablement dimension); the checker corpus (~65 pages) + R-B FP handling (plug-in vs plugin).
