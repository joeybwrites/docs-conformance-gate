# Part 2 delivery map

Status: Settled. This file is the map for the three Part 2 artifacts, not a fourth deliverable.

## Thesis carried forward from Part 1

The plugin documentation is substantially complete across the estate but fragmented across pages, properties, and product surfaces. Part 2 standardizes page ownership, surface-scoped claims, contextualized handoffs, and decision-critical summaries. It does not duplicate the Claude Code authoring guide or technical reference.

## Deliverables

1. **`plugin_style_guide.md`**
   - Defines the page-ownership model.
   - Provides eight deterministic conformance rules.
   - Defines role-specific templates for overview, submission, and creation pages.

2. **`plugin_component_matrix.md`**
   - Proposes the canonical surface-by-component model.
   - Uses evidence-bounded `supported`, `unsupported`, and `unknown` states.
   - Preserves contradictions and documentation silence instead of guessing through them.

3. **`plugin_overview_before_after.md`**
   - Applies the standard to one bounded page: `plugins/overview`.
   - Makes the overview the lifecycle map.
   - Gives Cowork a concrete first-use path instead of naming it only as a supported surface.
   - Frames precise handoffs to the pages that own authoring, reference, installation, and submission.

## Scope boundary

- `claude.com/docs/plugins/overview` owns the cross-product concept, platform relationship, support matrix, availability, lifecycle map, and concise surface-use orientation.
- `claude.com/docs/plugins/submit` owns submission readiness, governance, outcomes, and exceptions.
- `code.claude.com/docs/en/plugins` owns practical authoring.
- `code.claude.com/docs/en/plugins-reference` owns technical specifications and mechanics.
- Anthropic's “Use plugins in Claude” support page owns the full installation, use, customization, marketplace, and management procedures for web Chat, Desktop Chat, and Cowork.
- `code.claude.com/docs/en/discover-plugins` owns discovery and installation in Claude Code.

Cross-property links are not defects. A handoff fails only when it is unframed, ambiguous, premature, or aimed at the wrong destination.

## Part 3 connection

The Part 3 gate should prototype one or two rule families end to end on the real corpus. The remaining Part 2 rules can be designed and represented as future checks without expanding the implementation scope.
