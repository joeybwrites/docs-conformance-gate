---
title: Plugins overview
content-type: lifecycle-map
assumes: []
canonical_for: [plugin]
---
# Plugins

Plugins are reusable capability packages that turn Claude into a specialist for a role, team, or workflow. A plugin can combine instructions, tools, data connections, and delegated work into one shareable unit, so people don't have to rebuild the same setup one piece at a time.

The components a plugin can use depend on where it runs. This page is the starting point for the cross-product model and the plugin lifecycle. Use the [surface-by-component support matrix](./plugin_component_matrix) for sourced support details, then follow the lifecycle links below when you're ready to install, build, submit, or maintain one.

## What plugins do

Plugins let you define how Claude should approach recurring work, which tools and data it can use, and which workflows people can invoke directly. Because plugin components are file-based, teams can review, test, version, and share the same operating context.

A sales plugin, for example, could connect Claude to a CRM and knowledge base, teach it the team's sales process, expose a command for prospect research, and delegate competitive analysis to a sub-agent. The connector supplies access, the skill supplies judgment and process, the command gives the user a reliable entry point, and the sub-agent handles a bounded parallel task.

## How plugins compose capabilities

A plugin can combine several component types. The table below explains the job each component does; the [support matrix](./plugin_component_matrix) remains the source for where each one is supported.

| Component | What it adds |
|---|---|
| [**Skills**](/docs/skills/overview) | Task-specific instructions Claude applies when relevant |
| [**MCP connectors**](/docs/connectors/overview) | Access to external tools and data |
| [**Slash commands**](https://code.claude.com/docs/en/plugins-reference#skills) | An explicit, user-triggered workflow |
| [**Sub-agents**](https://code.claude.com/docs/en/plugins-reference#agents) | Delegated work with a bounded role and context |
| [**Hooks**](https://code.claude.com/docs/en/plugins-reference#hooks) | Actions that run at defined points in a workflow |

Claude Code supports additional plugin components and configuration. The [plugins reference](https://code.claude.com/docs/en/plugins-reference) is the source of truth when you need exact schemas, paths, scopes, CLI behavior, syncing, caching, or versioning.

## The plugin lifecycle

The pages below take you from finding a plugin through maintaining one. Each destination owns the detailed instructions for that part of the lifecycle.

| Stage | What you decide or do | Start here |
|---|---|---|
| **Discover and install** | Find a plugin and install it on the surface you're using | [Install in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) |
| **Build** | Author the package, test it, and debug it | [Create plugins](https://code.claude.com/docs/en/plugins#quickstart). Claude Code owns authoring. |
| **Submit** | Provide a public repository, run validation, confirm eligibility | Follow [Submitting your plugin](/docs/plugins/submit#submitting-your-plugin) for readiness checks. |
| **Maintain** | Understand catalog pinning and nightly sync | [version management](https://code.claude.com/docs/en/plugins-reference#version-management) owns the update mechanics. |

These cross-property links are intentional handoffs. Each one tells you what decision is next and why that destination owns it.

## Next steps

- **Build and test:** the [Claude Code plugin quickstart](https://code.claude.com/docs/en/plugins#quickstart) owns package anatomy, testing, and debugging.
- **Install in Claude Code:** [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins).
- **Resolve platform support:** the [surface-by-component matrix](./plugin_component_matrix).
