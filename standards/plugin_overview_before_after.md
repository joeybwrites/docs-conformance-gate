# Part 2 before/after: `plugins/overview`

Status: Final.

**Why this page.** The plugin docs are substantially complete but fragmented: discovery, building, validation, submission, publication, and maintenance each live somewhere, but no page assembles them. The reader has to do that work. The overview is the natural lifecycle map, but it still has to work as an overview. This rewrite preserves the explanation, examples, and practical orientation of the live page, then gives that writing a stronger spine: a cross-product model, an evidence-bounded matrix, and framed handoffs to the pages that own each stage.

---

## BEFORE (current page, condensed with issues flagged)

> **Plugins overview:** *…bundle MCP connectors, skills, slash commands, and sub-agents.* `[P2: flat, surface-blind definition; omits hooks that cowork/guide/plugins includes]`
>
> **What plugins do:** explains the value of packaging workflows, tools, and instructions together. `[keep: useful reader orientation and product value]`
>
> **Plugin directory:** shows 11 role- and workflow-based examples. `[keep: makes the abstraction concrete]`
>
> **Origins in Claude Code:** explains the directory and manifest model. `[keep, then clarify the relationship among Claude Code, Chat, Desktop, and Cowork]`
>
> **How plugins compose capabilities:** explains Skills, MCP connectors, Slash commands, and Sub-agents. `[keep the explanatory table; add hooks, consistent links, and surface scope]`
>
> **Availability:** says Cowork support is beta and organization-wide management is “coming in the weeks ahead.” `[P3/P5: contradicted elsewhere and guaranteed to decay]`
>
> **Next steps:** points to the directory, Claude Code creation guide, Skills, and Connectors. `[P4/S5: useful destinations, but not assembled into a lifecycle or consistently routed to the section that owns the next task]`

The current page isn't empty. Its strongest material should survive. The missing layer is the connective model that tells readers where plugins work, how the component set changes by surface, and where to go after orientation.

---

## AFTER (complete overview rewrite)

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

The components a plugin can use depend on where it runs. This page is the starting point for the cross-product model and the plugin lifecycle. Use the [surface-by-component support matrix](./plugin_component_matrix) for sourced support details, then follow the lifecycle links below when you're ready to install, build, submit, or maintain one.

## What plugins do

Plugins let you define how Claude should approach recurring work, which tools and data it can use, and which workflows people can invoke directly. Because plugin components are file-based, teams can review, test, version, and share the same operating context instead of relying on one person's setup.

A sales plugin, for example, could connect Claude to a CRM and knowledge base, teach it the team's sales process, expose a command for prospect research, and delegate competitive analysis to a sub-agent. The connector supplies access, the skill supplies judgment and process, the command gives the user a reliable entry point, and the sub-agent handles a bounded parallel task. Together they create a coherent workflow; separately they are building blocks.

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

Plugins originated in Claude Code, which remains the authoring home for package structure, testing, debugging, and distribution. Plugins can also package capabilities for Claude's conversational and collaborative surfaces, but the component set changes by surface.

> **Editorial dependency:** Before publication, confirm the canonical availability model for web Chat, Desktop Chat, and Cowork. Current official guidance conflicts on Chat support. Replace this note and the provisional rows below with one product-approved statement; don't ask readers to reconcile the sources themselves.

| Surface | Use it for | Important distinction |
|---|---|---|
| **Web Chat** | `[Confirm before publication]` | `[Confirm supported plugin components]` |
| **Desktop Chat** | `[Confirm before publication]` | `[Confirm supported plugin components]` |
| **Cowork** | Complex, multi-step work that can use files and delegated workstreams | Supports skills, connectors, slash commands, sub-agents, and hooks; see the matrix for components the docs leave unknown |
| **Claude Code** | Building, testing, debugging, and distributing plugins | The authoring guide and technical reference own the full implementation model |

## Use plugins in Cowork

Cowork is where a plugin can become more than a set of instructions. In addition to the skills and connectors available through the package, Cowork can run hooks at defined points in a workflow and delegate bounded work to sub-agents. That makes it the right surface for plugins built around multi-step work, files, or parallel workstreams.

To install one, open the **Cowork** tab, then go to **Customize → Plugins → Browse plugins** and select **Install**. After installation, type `/` or select the **+** button to see the skills the plugin added. Select a skill to view its details. Hooks and sub-agents are separate plugin components; their behavior is defined by the plugin rather than by that skills menu.

You can also adapt an installed plugin without rebuilding it from scratch. Open the plugin, select **Customize** in the upper-right corner, and Cowork starts a new task with a prompt for modifying the plugin. Select **Let's go**, then work with Claude to adjust its skills and connectors around your workflow.

Plugins uploaded manually through Cowork are stored locally on your computer. A plugin can still connect to cloud services, but custom connectors used in Cowork must point to a server Anthropic can reach over the public internet; they can't rely on a service available only inside your local network. Only install plugins from sources you trust, especially when a package includes a local MCP server that can run with local permissions.

For the current installation interface, marketplace controls, and organization-managed behavior, see [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

## How plugins compose capabilities

A plugin can combine several component types. The table below explains the job each component does; the [support matrix](./plugin_component_matrix) remains the source for where each one is supported.

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

Plugins are available in Claude Code. Claude also supports organization-managed plugin distribution, including plugins that are optional, automatically installed, or required.

> **Editorial dependency:** Add the confirmed plan and surface availability statement here before publication, with a dated support source or changelog. Avoid relative promises such as “coming in the weeks ahead,” which quickly become stale.

## Next steps

- **Use a plugin:** [Browse the directory](https://claude.com/plugins-for/cowork) or [install one in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).
- **Use one in Cowork:** Install it from **Cowork → Customize → Plugins**, then find its skills with `/` or the **+** button and select one to view its details.
- **Build and test:** Follow the [Claude Code plugin quickstart](https://code.claude.com/docs/en/plugins#quickstart).
- **Check a technical requirement:** Use the [plugins reference](https://code.claude.com/docs/en/plugins-reference).
- **Submit publicly:** Review [submission readiness and directory requirements](/docs/plugins/submit#submitting-your-plugin).
- **Install in Claude Code:** Use [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins).
- **Resolve platform support:** Check the [surface-by-component matrix](./plugin_component_matrix).

---

## What changed and why

| Change | Fixes | Rule |
|---|---|---|
| Preserved the live page's value proposition, examples, component explanations, and directory orientation | prevents the lifecycle model from becoming an IA skeleton | content quality |
| Added a complete Cowork use path covering installation, invocation, customization, connector reachability, and local-package trust | prevents the cross-product model from stopping at surface identification | S1, S7, S8 |
| Added a written platform relationship and a sourced support matrix | P1, P2 | S1, S2 |
| Kept the explanatory component table while moving support claims into the matrix | P1, P2, P4 | S1, S2, S4 |
| Added the lifecycle map, with each stage naming its owner or follow-up gap | fragmentation | S7 |
| Replaced unscoped root links with framed handoffs to the guide, reference, support, and submission owners | P4 | S5 |
| Replaced the decaying availability promise with a dated fact-check dependency and kept the source contradiction out of reader-facing copy | P3, P5 | S3 |
| Scoped validation, screening, community-catalog pinning, nightly sync, and version resolution to the contexts that document them | corrects “the docs lack information” without universalizing downstream mechanics | S1, S5 |
| Added agentic build guidance without creating a second agent-only source of truth | agentic usability | S7, S8 |

**Bounding note.** This is a full overview, not a duplicate authoring guide. It explains the model, gives the reader enough narrative and examples to understand it, and connects the lifecycle. Package construction stays in the Claude Code guide; exact mechanics stay in the reference; submission owns readiness through outcomes.

**Open value.** The matrix still carries `unknown` cells and a live Chat contradiction the documentation doesn't resolve. Turning those into cited support states is the highest-value follow-up, and the product/docs team has to confirm it. This page can't invent the answer.
