# Part 2 before/after: `plugins/overview`

Status: Publication draft with explicit editorial dependencies. The reader-facing rewrite below is submission-ready prose; the two dependencies it can't resolve on its own (the confirmed Chat/Cowork availability model and the matrix's `unknown` cells) are named as editorial dependencies rather than papered over, because the product/docs team owns those answers. This is not "Final" in the sense of no open questions — it is complete as a governed draft that states its open questions instead of inventing answers.

**Why this page.** The plugin docs are substantially complete but fragmented: discovery, building, validation, submission, publication, and maintenance each live somewhere, but no page assembles them. The reader has to do that work. The overview is the natural lifecycle map, but it still has to work as an overview. This rewrite preserves the explanation, examples, and practical orientation of the live page, then gives that writing a stronger spine: a cross-product model, an evidence-bounded matrix, and framed handoffs to the pages that own each stage.

---

## BEFORE (current live page, reproduced verbatim)

Source: [`claude.com/docs/plugins/overview`](https://claude.com/docs/plugins/overview), retrieved 2026-08-31 via `checker/fetch_corpus.py`. Reproduced exactly as fetched (the page is authored in MDX, so its `<Note>` / `<Columns>` / `<Card>` components appear as written); only the `.md` export's leading llms.txt documentation-index banner is omitted, as it is a fetch artifact and not page content.

````markdown
# Plugins overview

> Extend Claude with reusable capability packages that bundle MCP connectors, skills, slash commands, and sub-agents

Plugins are reusable capability packages that extend Claude with custom functionality. They bundle together [MCP connectors](/docs/connectors/overview), [skills](/docs/skills/overview), slash commands, and sub-agents into a single shareable unit — turning Claude into a specialist tailored to your role, team, and company.

## What plugins do

Plugins let you define how you like work done, which tools and data to pull from, how to handle critical workflows, and what slash commands to expose so your team gets consistent outcomes. Every component is file-based, so plugins are easy to build, edit, and share.

As your team builds and shares plugins, Claude becomes a cross-functional expert. Best practices get baked into every interaction, so leaders and admins can spend less time enforcing processes and more time improving them.

## Plugin directory

To help you get started, Anthropic has open-sourced 11 plugins built and used internally:

| Plugin                 | What it does                                                  |
| ---------------------- | ------------------------------------------------------------- |
| **Productivity**       | Manage tasks, calendars, and daily workflows                  |
| **Enterprise search**  | Find information across your company's tools and docs         |
| **Sales**              | Research prospects, prep deals, and follow your sales process |
| **Finance**            | Analyze financials, build models, and track key metrics       |
| **Data**               | Query, visualize, and interpret datasets                      |
| **Legal**              | Review documents, flag risks, and track compliance            |
| **Marketing**          | Draft content, plan campaigns, and manage launches            |
| **Customer support**   | Triage issues, draft responses, and surface solutions         |
| **Product management** | Write specs, prioritize roadmaps, and track progress          |
| **Biology research**   | Search literature, analyze results, and plan experiments      |
| **Plugin Create**      | Create and customize new plugins from scratch                 |

Browse the full collection at [claude.com/plugins](https://claude.com/plugins-for/cowork) or use the Plugin Create plugin to build your own.

## Origins in Claude Code

Plugins originated in [Claude Code](https://code.claude.com/docs/en/plugins), where developers create and distribute them as versioned, shareable directories. A Claude Code plugin lives in a directory with a manifest (`plugin.json`) that defines its identity, version, and available components.

<Note>
  For technical details on plugin structure, manifests, and configuration, see the [Claude Code plugins reference](https://code.claude.com/docs/en/plugins-reference).
</Note>

## Plugins in Cowork

Plugins are fully supported in [Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork), Anthropic's agentic workspace for complex, multi-step knowledge work. In Cowork, Claude runs inside an isolated virtual machine environment, executes tasks in parallel workstreams, and writes outputs directly to your file system — and plugins extend all of that capability.

A sales plugin, for example, could connect Claude to your CRM and knowledge base, teach it your sales process, and give you slash commands for everything from prospect research to call follow-ups. You define what goes in the plugin once, and Claude pulls from that context whenever it's relevant.

## How plugins compose capabilities

| Plugin component   | What it adds                                                      | Example                                                                         |
| ------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Skills**         | Specialized instructions Claude follows when relevant tasks arise | A "brand voice" skill that activates when drafting external communications      |
| **MCP connectors** | Access to external tools and data                                 | A connector to a CRM that lets Claude read and update deal records              |
| **Slash commands** | Explicit, user-triggered workflows                                | `/sales:prospect-research` to kick off a structured research workflow           |
| **Sub-agents**     | Delegated workstreams that run in parallel                        | A sub-agent that handles competitive analysis while another drafts the proposal |

## Availability

Plugin support in Cowork is available as a beta for all paid Claude users. Plugins are currently saved locally to your machine. Org-wide sharing and management are coming in the weeks ahead.

| Platform          | Plugin support                                                     |
| ----------------- | ------------------------------------------------------------------ |
| **Claude Code**   | Full plugin support — create, install, and use plugins             |
| **Claude Cowork** | Full plugin support — plugins extend agentic, multi-step workflows |

Looking to submit your own plugin? See [Submitting your plugin](/docs/plugins/submit#submitting-your-plugin).

## Next steps

<Columns cols={2}>
  <Card title="Plugin directory" icon="grid-2" href="https://claude.com/plugins-for/cowork">
    Browse the full plugin collection.
  </Card>

  <Card title="Create plugins" icon="code" href="https://code.claude.com/docs/en/plugins">
    Build and distribute plugins in Claude Code.
  </Card>

  <Card title="Skills overview" icon="sparkles" href="/docs/skills/overview">
    Learn how skills work as a core plugin component.
  </Card>

  <Card title="Connectors overview" icon="plug" href="/docs/connectors/overview">
    Understand MCP connectors that plugins can bundle.
  </Card>
</Columns>
````

**Problems flagged in the current page (mapped to the audit).** The page isn't empty — its value proposition, examples, and component table should survive. The issues are:

- **Opening definition** — flat and surface-blind (`bundle MCP connectors, skills, slash commands, and sub-agents`); omits hooks, which the Cowork guide includes as a component. *(P2)*
- **Origins in Claude Code** — explains the directory/manifest model but never clarifies the relationship among Claude Code, Chat, Desktop, and Cowork. *(P1)*
- **How plugins compose capabilities** — the explanatory table is worth keeping, but it lists no hooks, links none of the primitives, and states no surface scope. *(P1, P2, P4)*
- **Availability** — says Cowork support is beta and org-wide management is "coming in the weeks ahead"; the relative-time promise is guaranteed to decay, and the Chat availability picture is contradicted elsewhere in the estate. *(P3, P5)*
- **Next steps** — points to useful destinations (directory, Claude Code creation guide, Skills, Connectors) but doesn't assemble them into a lifecycle or route the reader to the section that owns each next task. *(P4)*

The missing layer is the connective model: where plugins work, how the component set changes by surface, and where to go after orientation.

---

## AFTER (overview rewrite — publication draft with explicit editorial dependencies)

```yaml
---
title: Plugins overview
content-type: lifecycle-map
assumes: []
canonical_for: [plugin]
---
```

# Plugins

Plugins are reusable capability packages that turn Claude into a specialist for a role, team, or workflow. A plugin can combine instructions, tools, data connections, and delegated work into one shareable unit, so people don't have to rebuild the same setup one piece at a time.

The components a plugin can use depend on where it runs. This page is the starting point for the cross-product model and the plugin lifecycle. Use the [surface-by-component support matrix](./plugin_component_matrix.md) for sourced support details, then follow the lifecycle links below when you're ready to install, build, submit, or maintain one.

## What plugins do

Plugins let you define how Claude should approach recurring work, which tools and data it can use, and which workflows people can invoke directly. Because plugin components are file-based, teams can review, test, version, and share the same operating context instead of relying on one person's setup.

A sales plugin, for example, could connect Claude to a CRM and knowledge base, teach it the team's sales process, expose a [slash command](https://code.claude.com/docs/en/plugins-reference#skills) for prospect research, and delegate competitive analysis to a [sub-agent](https://code.claude.com/docs/en/plugins-reference#agents). The [connector](/docs/connectors/overview) supplies access, the [skill](/docs/skills/overview) supplies judgment and process, the command gives the user a reliable entry point, and the sub-agent handles a bounded parallel task. Together they create a coherent workflow; separately they are building blocks.

## Start with an existing plugin

Anthropic publishes plugins for common roles and workflows. These examples are useful both as ready-to-use packages and as references for how related capabilities can fit together.

| Plugin | What it helps with |
|---|---|
| **Productivity** | Tasks, calendars, and daily workflows |
| **Enterprise search** | Finding information across company tools and documentation |
| **Sales** | Prospect research, deal preparation, and repeatable sales processes |
| **Finance** | Financial analysis, modeling, and metric tracking |
| **Data** | Querying, visualizing, and interpreting datasets |
| **Legal** | Document review, risk identification, and compliance workflows |
| **Marketing** | Content development, campaign planning, and launches |
| **Customer support** | Issue triage, response drafting, and solution discovery |
| **Product management** | Specifications, roadmap prioritization, and progress tracking |
| **Biology research** | Literature search, analysis, and experiment planning |
| **Plugin Create** | Building and customizing a plugin from scratch |

[Browse the plugin directory](https://claude.com/plugins-for/cowork), or start with **Plugin Create** if you want Claude to help shape an existing template around your workflow.

## Where plugins work

Plugins originated in Claude Code. Claude Code documentation owns technical package authoring and structure — the package layout, testing, debugging, and distribution model. Plugins can also package capabilities for Claude's conversational and collaborative surfaces, but the component set changes by surface.

The table below is orientation, not a second canonical component list. The [surface-by-component support matrix](./plugin_component_matrix.md) is the source of record for what each surface supports, including the cells the documentation currently leaves unknown; use this table to get your bearings and the matrix to settle any specific question.

One conflict is worth surfacing here rather than hiding, because it is a live documentation-governance gap and not a reader error: the Cowork guide states that plugins are **not** used in Chat, while the Claude support article describes plugin availability **in** Chat. The overview does not resolve this by choosing a side. Until the product and docs teams reconcile the two sources, treat Chat availability as unresolved and defer to the matrix.

| Surface | Use it for | Important distinction |
|---|---|---|
| **Chat (web and desktop)** | Conversational plugin use — but availability is disputed across official sources (see the note above) | Sources conflict on whether plugins run in Chat and which components apply; the [matrix](./plugin_component_matrix.md) is canonical |
| **Cowork** | Complex, multi-step work that can use files and delegated workstreams | Supports skills, connectors, slash commands, sub-agents, and [hooks](https://code.claude.com/docs/en/plugins-reference#hooks); see the [matrix](./plugin_component_matrix.md) for components the docs leave unknown |
| **Claude Code** | Building, testing, debugging, and distributing plugins | The authoring guide and technical reference own the full implementation model |

## Use plugins in Cowork

Chat can already combine skills and connectors, so packaging those is not what sets Cowork apart. The defensible distinction is narrower: Cowork can **run hooks and delegate to sub-agents**, which Chat does not. That makes Cowork the right surface for plugins built around multi-step work, files, or parallel workstreams — the same package that would only supply instructions and data access in Chat can additionally fire validation hooks and hand bounded tasks to sub-agents here.

Installing, invoking, and customizing a plugin in Cowork all happen through the Cowork interface: you browse and install from the **Customize → Plugins** panel, surface the skills a plugin added with `/` or the **+** button, and use **Customize** to adapt an installed plugin around your workflow. Manually uploaded plugins are stored locally on your own machine, so trust matters — install only from sources you trust, especially when a package bundles a local MCP server that runs with local permissions.

This overview does not reproduce the full click-path, because that interface and its marketplace and organization-management controls change and are owned elsewhere. [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) owns the complete install, use, customize, and management path; follow it for the current steps.

## How plugins compose capabilities

A plugin can combine several component types. The table below explains the job each component does; the [support matrix](./plugin_component_matrix.md) remains the source for where each one is supported.

| Component | What it adds | Example |
|---|---|---|
| [**Skills**](/docs/skills/overview) | Task-specific instructions Claude applies when relevant | A brand-voice skill used while drafting external communication |
| [**MCP connectors**](/docs/connectors/overview) | Access to external tools and data | A CRM connector that reads and updates deal records |
| [**Slash commands**](https://code.claude.com/docs/en/plugins-reference#skills) | An explicit, user-triggered workflow | `/sales:prospect-research` starts a repeatable research process |
| [**Sub-agents**](https://code.claude.com/docs/en/plugins-reference#agents) | Delegated work with a bounded role and context | A competitive-analysis agent works while the main thread drafts a proposal |
| [**Hooks**](https://code.claude.com/docs/en/plugins-reference#hooks) | Actions that run at defined points in a workflow | A validation hook checks an output after Claude writes it |

Claude Code supports additional plugin components and configuration. Use the [plugins reference](https://code.claude.com/docs/en/plugins-reference) when you need exact schemas, paths, scopes, CLI behavior, syncing, caching, or versioning.

## Build with Claude

You can use **Plugin Create** to shape a plugin interactively. Before asking Claude to build or modify one, identify the target surface, supported components, expected package, validation step, and any decision that should return to you.

For technical authoring, start with the [Claude Code plugin quickstart](https://code.claude.com/docs/en/plugins#quickstart). It covers package anatomy, implementation, local testing, debugging, sharing, and migration. Use the [plugins reference](https://code.claude.com/docs/en/plugins-reference) for exact behavior, and give Claude those requirements instead of asking it to infer them from the overview.

## The plugin lifecycle

The pages below take you from finding a plugin through maintaining one. Start with the stage that matches your task; each destination owns the detailed instructions for that part of the lifecycle.

| Stage | What you decide or do | Start here |
|---|---|---|
| **Discover and install** | Find a plugin and install it on the surface you're using | [Install in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) · [Discover and install in Claude Code](https://code.claude.com/docs/en/discover-plugins) |
| **Use in Cowork** | Invoke bundled skills, run Cowork-capable workflows, or customize an installed plugin around your work | [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) owns the current interface and management details. |
| **Build** | Author the package, test it, and debug it | [Create plugins](https://code.claude.com/docs/en/plugins#quickstart). Claude Code owns authoring. |
| **Validate** | For community submission, run the same structural validation used by the review pipeline; automated safety screening is separate | [Community-marketplace submission](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace) owns the mechanics. |
| **Submit** | Provide a public GitHub repository, run validation, confirm eligibility, and choose the Claude.ai or Console form | Follow [Submitting your plugin](/docs/plugins/submit#submitting-your-plugin) for readiness checks and the submission path. |
| **Publish** | Track Claude.ai review status and understand the documented automatic-update behavior | Return to [Submitting your plugin](/docs/plugins/submit#submitting-your-plugin) for current status and update guidance. |
| **Maintain** | For approved community-marketplace plugins, the catalog pins a commit SHA, CI bumps that pin as commits arrive, and the public catalog syncs nightly. Other source types follow their own version rules. | [Community submission](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace) owns catalog behavior; [version management](https://code.claude.com/docs/en/plugins-reference#version-management) owns update mechanics. |

These cross-property links are intentional handoffs. Each one tells you what decision is next and why that destination owns it. Links target the relevant section unless the destination is already a dedicated task page, such as an installation guide.

## Availability and management

Plugins are available in Claude Code today. Claude also supports organization-managed plugin distribution, so an administrator can make a plugin optional, install it automatically, or require it. Availability across the conversational surfaces — Chat and Cowork — is the part the documentation does not yet state consistently; see the conflict flagged under **Where plugins work** and defer to the [support matrix](./plugin_component_matrix.md) for the current per-surface picture. This page deliberately avoids relative timing promises such as “coming in the weeks ahead,” which decay into inaccuracy the moment they ship.

> **Editorial dependency (draft):** One item here is not yet resolvable from the documentation and is owned by the product/docs team: the confirmed cross-surface availability model. When it is settled, state it in this section with a dated support source or changelog entry, and reconcile the Chat/Cowork conflict called out above. This note is why the artifact is labeled a publication draft rather than final.

## Next steps

The lifecycle table above is the routing hub: pick the stage that matches your task — discover, install, use, build, validate, submit, publish, or maintain — and follow the owner it names. It already carries those links, so they are not repeated here. Two orientation shortcuts are worth keeping close:

- **Try one now:** [browse the directory](https://claude.com/plugins-for/cowork) or [install a plugin in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).
- **Settle a per-surface support question:** consult the canonical [surface-by-component matrix](./plugin_component_matrix.md).

---

## What changed and why

| Change | Fixes | Rule |
|---|---|---|
| Preserved the live page's value proposition, examples, component explanations, and directory orientation | prevents the lifecycle model from becoming an IA skeleton | content quality |
| Linked the first meaningful mention of each primitive (skill, connector, slash command, sub-agent, hook) to its owner, so the prose and the Cowork/surface sections no longer name them bare before the component table links them | primitives appeared bare ahead of the table | S4 |
| Narrowed "Claude Code is the authoring home" to "Claude Code documentation owns technical package authoring and structure" | over-broad ownership claim | S1 |
| Compressed the Cowork section from a full install/customize/local-storage procedure to orientation plus a framed handoff to the Support page that owns install/use/customize/management | the overview was duplicating an owned procedure | S1, S5, S7 |
| Replaced the "more than a set of instructions" framing with the defensible distinction that Cowork runs hooks and sub-agents while Chat does not (Chat also combines skills and connectors) | prior claim was not the real differentiator | S1 |
| Added a written platform relationship and a sourced support matrix | P1, P2 | S1, S2 |
| Kept the explanatory component table while moving support claims into the matrix, and fixed every matrix link to the repository-valid `./plugin_component_matrix.md` path | P1, P2, P4; broken relative links | S1, S2, S4 |
| Added the lifecycle map, with each stage naming its owner or follow-up gap; compressed "Next steps" so it stops re-listing the lifecycle links | fragmentation; duplication | S7 |
| Replaced unscoped root links with framed handoffs to the guide, reference, support, and submission owners | P4 | S5 |
| Replaced the decaying availability promise with a labeled editorial dependency, and surfaced the Chat-availability source contradiction to readers as a governance flag instead of resolving it by picking a source | P3, P5 | S3 |
| Removed the `[Confirm before publication]` placeholder cells and relabeled the artifact a publication draft with explicit editorial dependencies, rather than calling it "Final" while author TODOs sat in reader-facing tables | placeholder tokens in reader copy | S3 |
| Scoped validation, screening, community-catalog pinning, nightly sync, and version resolution to the contexts that document them | corrects “the docs lack information” without universalizing downstream mechanics | S1, S5 |
| Added agentic build guidance without creating a second agent-only source of truth | agentic usability | S7, S8 |

**Bounding note.** This is a full overview, not a duplicate authoring guide. It explains the model, gives the reader enough narrative and examples to understand it, and connects the lifecycle. Package construction stays in the Claude Code guide; exact mechanics stay in the reference; submission owns readiness through outcomes.

**Open value.** The matrix still carries `unknown` cells and a live Chat contradiction the documentation doesn't resolve. Turning those into cited support states is the highest-value follow-up, and the product/docs team has to confirm it. This page can't invent the answer.
