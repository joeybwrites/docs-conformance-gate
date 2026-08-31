---
title: Plugins overview
content-type: lifecycle-map
assumes: []
canonical_for: [plugin]
---
# Plugins

A plugin bundles Claude capabilities — [skills](/docs/skills/overview) and [connectors](/docs/connectors/overview) — into one shareable package. Which components apply depends on the surface; the [support matrix](./plugin_component_matrix) is the sourced record.

## Components

| Component | What it adds |
|---|---|
| [Skills](/docs/skills/overview) | Task-specific instructions |
| [MCP connectors](/docs/connectors/overview) | External tools and data |
| [Slash commands](https://code.claude.com/docs/en/plugins-reference#skills) | User-triggered workflows |
| [Sub-agents](https://code.claude.com/docs/en/plugins-reference#agents) | Delegated parallel work |
| [Hooks](https://code.claude.com/docs/en/plugins-reference#hooks) | Actions at defined points |

## Build and maintain

Claude Code owns authoring: start with the [Claude Code plugin quickstart](https://code.claude.com/docs/en/plugins#quickstart). The [plugins reference](https://code.claude.com/docs/en/plugins-reference) is the source of truth for schemas and versioning.

## Availability

Plugins are available in Claude Code and Cowork; see the [support matrix](./plugin_component_matrix) for surface-by-surface detail, with any unresolved conflicts flagged there rather than stated as settled here.
