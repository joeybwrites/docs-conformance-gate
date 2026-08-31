# Part 1: Audit memo for Plugins

Status: Analysis settled; the prose is an AI-assisted draft for Joey's voice pass.

## Slice, and why Plugins

The take-home suggested **Skills**, **Plugins**, and **Connectors** as cross-cutting primitives. I looked at all three, plus Cowork, Claude Tag, Claude for M365, and the Claude Code plugin documentation, and chose **Plugins**.

Plugins are the compositional primitive: they package skills, connectors, commands, agents, hooks, and other capabilities into something reusable. Their documentation therefore has to reconcile vocabulary, platform behavior, authoring, distribution, and lifecycle guidance that several other sections own. That makes Plugins the point where estate-level organization either holds together or starts asking the reader to assemble the system alone.

Connectors are the healthiest comparison case because their documentation exposes a broad lifecycle through a developed left navigation. Claude Tag is another positive control for section-level structure. I use both as evidence for what a more coherent path can look like, not as additional audit targets.

## 1. What's wrong, prioritized

**Headline: the plugin documentation is substantially complete in pieces, but no page owns the cross-surface model and lifecycle as a coherent whole.**

The problem isn't that the information broadly doesn't exist. The overview, submission page, Claude Code authoring guide, technical reference, support articles, policies, and submission forms collectively cover a great deal. The problem is **distributed completeness**: readers have to reconstruct one journey across page hierarchies, domains, and product surfaces, while several copied definitions and availability claims have already drifted apart.

### P1: No canonical cross-surface plugin model

The live pages describe several overlapping plugin models:

- `plugins/overview` presents plugins across Claude Code and Cowork and lists skills, MCP connectors, slash commands, and sub-agents.
- `cowork/guide/plugins` includes hooks as another Cowork component.
- Current support guidance says plugins can be installed in web Chat, Desktop Chat, and Cowork; skills work across all three, while hooks and sub-agents run only in Cowork.
- The Claude Code guide and reference document a broader authoring system that includes skills, agents, hooks, MCP and LSP servers, monitors, executables, settings, and other Code-specific mechanics.

Those statements don't all need to become identical. Some differences are legitimate because the surfaces differ. The failure is that no canonical artifact tells the reader which component or behavior applies on which surface. Silence must remain **unknown**, not be converted into unsupported. A sourced surface-by-component matrix would make both the known support and the documentation gaps explicit.

### P2: Repeated flat definitions hide surface scope and drift

Several pages define plugins by restating a local component list. The overview lists four components, the Cowork guide adds hooks, connector documentation describes a narrower bundle, and Claude Tag frames plugins around skills. Some of this is contextual, but the pages usually don't mark it that way.

The result is a definition problem created by duplication. A reader can get different answers to “what can a plugin contain?” without being told whether the difference reflects product behavior, page scope, or stale documentation. One canonical definition plus a surface-aware matrix would let other pages summarize locally without creating another source of truth.

### P3: Availability guidance contradicts newer product guidance

The overview says Cowork plugin support is beta, plugins are saved locally, and organization-wide sharing and management are “coming in the weeks ahead.” Newer Cowork and support guidance documents organization-managed plugins as shipped and says plugins are available across web Chat, Desktop Chat, and Cowork for paid plans.

This is more than stale wording. It changes where readers believe plugins work and what administrators can manage. Relative promises such as “coming in the weeks ahead” make the problem predictable because they decay without announcing that they have become wrong.

### P4: Page ownership and handoffs are under-specified

The overview and submission pages aren't empty. The overview defines the concept, explains every named component, provides examples, and routes to several next steps. The submission page covers distribution choices, plugin quality, MCP setup, security, eligibility, validation, submission, status, and automatic updates.

The practical authoring guide and technical reference also do their jobs well. They own package anatomy, implementation, testing, debugging, migration, schemas, CLI behavior, syncing, caching, troubleshooting, and versioning.

The reader-facing problem is the handoff between those owners. The overview identifies Claude Code as the origin and build destination, but it doesn't place the authoring guide and technical reference inside a complete lifecycle or route readers to the exact section that owns each next step. The submission page summarizes the happy path but leaves decision-critical review and exception details either one hierarchy away or unstated. Crossing properties isn't the defect. An unframed, premature, or ambiguous crossing is.

### P5: Small hygiene problems make the larger drift cheaper to repeat

The slice also contains terminology variation (`sub-agent` versus `subagent`), non-canonical or redirect-dependent links, uneven component linking, and undated lifecycle language. Each problem is minor alone. Together they are exactly the class of deterministic defect a conformance gate should catch before it becomes estate-wide inconsistency.

## 2. Delete or merge, and what happens to readers

**Delete nothing.** The pages have legitimate jobs. The problem is unclear ownership and missing connective structure, not obvious dead weight.

Use this page-ownership model:

- **`claude.com/docs/plugins/overview`** owns the cross-product concept, platform relationship, sourced support matrix, availability, and lifecycle map.
- **`claude.com/docs/plugins/submit`** owns submission readiness, eligibility, review governance, publication outcomes, and exception recovery.
- **`code.claude.com/docs/en/plugins`** remains the practical authoring tutorial.
- **`code.claude.com/docs/en/plugins-reference`** remains the technical source of truth.
- **Anthropic's “Use plugins in Claude” support page** owns installation and use guidance for web Chat, Desktop Chat, and Cowork.
- **`code.claude.com/docs/en/discover-plugins`** owns plugin discovery and installation in Claude Code.

Reinforce by reference, not by copy. The higher-level pages should summarize decision-critical consequences, state why the destination owns the next step, and link to the precise section or a dedicated task page. The Claude Code pages stay in place because their depth and audience are appropriate. If a page moves or is renamed inside Claude Docs, preserve the old route with a redirect.

## 3. Proposed information architecture, and what it takes to get there

The Plugins overview becomes the lifecycle map:

- **What a plugin is:** one canonical, cross-surface definition.
- **Where plugins work:** current availability and platform relationship.
- **What plugins can contain:** a sourced surface-by-component matrix with `supported`, `unsupported`, and `unknown` states.
- **The lifecycle:** discover, build, validate, submit, publish, and maintain, with each stage naming its owning page.
- **Next steps:** framed links to the exact authoring, reference, installation, marketplace, and submission sections.

The submission page keeps its existing happy path and adds the decision-critical layer it owns:

- Required inputs and eligibility for each submission surface.
- How local validation relates to automated safety screening and directory review.
- Review states and where Claude.ai and Console authors track them.
- Rejection and remediation paths.
- Publication outcomes, failed-update behavior, rollback, deprecation, delisting, ownership transfer, and incident handling.

Detailed build procedures, schemas, CLI mechanics, and version resolution stay in the Claude Code guide and reference. The higher-level pages route to them with enough local context that a person or agent can choose the right next step without guessing.

Implementation is bounded: one canonical matrix, one overview update, one submission-layer update, framed links, and any necessary redirects or scope banners. It isn't a rewrite of every plugin-adjacent page.

## 4. Measurement, and how I'd instrument it

The improvement is real only if the slice becomes both **internally consistent** and **task-complete across its handoffs**.

### Leading indicator: the conformance gate

Run the Part 3 gate in CI against deterministic rules:

- **Surface-claim conformance:** component and availability claims must name a surface and match the sourced matrix. Unknown cells remain a confirmation backlog, not automatic failures.
- **Canonical ownership:** copied definitions, contradictory availability statements, and duplicated lifecycle facts are flagged against their owner.
- **Prerequisite bridging:** core concepts are linked on first mention unless the page explicitly declares them as assumed knowledge.
- **Contextualized handoffs:** a decision-critical cross-property link must summarize the relevant consequence, name why the destination owns the step, and target the precise section or a registered dedicated task page.
- **Link, terminology, and freshness checks:** flag non-canonical routes, terminology drift, and undated relative-time promises.

### Structural journey checks

Define representative tasks and their expected owners:

- Understand what a plugin is and where it works.
- Choose a target surface and supported component set.
- Build and test a plugin.
- Prepare and submit it.
- Interpret review status or recover from rejection.
- Understand how a published community plugin updates or rolls back.

The check isn't “did the reader stay on one domain?” It is “could the reader identify the next owner, understand why the handoff was happening, and land on the exact guidance needed?” A broken or ambiguous handoff is a located defect rather than a subjective depth score.

### Lagging signals

- Completion and abandonment across the documented lifecycle paths.
- Click-through and return behavior at framed cross-property handoffs.
- Internal-search reformulation and zero-result rates for plugin tasks.
- “Was this helpful?” results and plugin-tagged support tickets.
- Repeated questions about surface support, validation versus review, update behavior, and recovery paths.

The gate predicts where the documentation can fail. Reader behavior and support data confirm whether those failures matter. The target state is not fewer outbound clicks by itself; it is fewer ambiguous handoffs, fewer contradictory claims, and higher completion of the task the reader came to perform.
