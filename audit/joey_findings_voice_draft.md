# Claude customization docs: working audit findings

This is still a working read, not the final audit. I haven't finished capturing URLs, quotations, or every piece of page-level evidence yet. What I'm trying to pin down is where the documentation feels healthy, where it starts making assumptions about the reader, and which part of the system is actually worth auditing more deeply.

## Where I think the focus should be

After scanning connectors, skills, and plugins, connectors currently look like the healthiest part of the group. The left navigation is fairly complete, and the documentation covers most of the lifecycle I would expect: what MCPs are, how to build and bundle a connector, authentication options, testing, troubleshooting, publishing, and some higher-level integrations.

That doesn't mean the connector documentation is finished or problem-free. It means that, compared with the other two areas, I can see a reasonably complete path through the material.

Skills and plugins are more attractive audit targets. Skills have useful creation guidance, but a lot of it is concentrated on one page. Plugins are probably the stronger focus because they touch several Claude customization surfaces at once. A plugin can bundle skills, MCP connectors, slash commands, and sub-agents. So the plugin documentation has to do more than explain a directory structure: it has to help the reader understand how those parts fit together.

Right now, I don't think it consistently does that.

## Finding 1: The plugin documentation assumes the reader already understands the component parts

The plugin pages refer to skills, MCP connectors, slash commands, and sub-agents, but those terms aren't always linked or lightly explained where they appear. That may be fine for someone who's already read through the rest of the Claude documentation. It's less useful for someone who lands directly on the plugin page because they want to understand what a plugin is or decide whether they should build one.

This creates a slightly backwards experience. Plugins are the point where several Claude features come together, but the documentation for that combined surface gives the reader less orientation than some of the individual features do.

I don't think the fix is to repeat the full connector, skill, command, and sub-agent documentation on every plugin page. But the page does need a compact explanation of what a plugin can contain, what each component contributes, and where to go next for the full implementation details. The component names should also be links anywhere the reader is being asked to understand plugin anatomy or prepare a submission.

At minimum, I would add:

- A short “What a plugin can contain” section.
- One-sentence definitions of skills, connectors, slash commands, and sub-agents.
- Direct links to the relevant documentation.
- A small example showing how two or more of those parts work together in an actual plugin.

I still need to capture the exact pages and language where these terms appear without links, and verify the rendered link, hover, and keyboard behavior before treating this as a final finding.

## Finding 2: The submission page is sparse relative to the consequences of the workflow

The plugin submission page covers the basics: setup, directory expectations, security, the submission process, and the fact that the user needs to be signed in. But it also pushes a fair amount of the explanation into other pages and deeper links across the Claude documentation, including the plugin marketplace.

So a user who lands on the submission page cold may be able to see individual requirements without having a complete picture of the workflow. They still have to reconstruct what needs to exist before submission, what may be validated or reviewed, and what happens after the plugin is submitted or published.

Submission is where the documentation should probably become more explicit, not less. It's a higher-consequence point in the lifecycle, and ambiguity there can turn into failed submissions, unnecessary rework, or security mistakes.

I would restructure the page as a staged path:

1. What must already exist.
2. What the plugin package should contain.
3. What to validate locally, including security checks.
4. How sign-in and submission work.
5. What happens during review.
6. What publishing changes for the author and users.
7. What ongoing maintenance looks like.

The page can still link outward for detailed implementation guidance. The key is that the minimum complete workflow should be understandable without making the reader assemble it from several separate pages.

I need to map the current outbound links and identify what question each linked page is expected to answer. That will make it clearer whether the problem is missing information, poor sequencing, or simply weak connective tissue.

## Finding 3: Skills have useful creation guidance, but the example path leaves the documentation too quickly

The skills documentation does cover a fair amount on the creation page: how to create a custom skill, what is required, how the Markdown files are structured and maintained, and how supporting resources and brand colors can be handled.

The weaker point is the example path. The documentation points readers toward GitHub for examples, particularly as the skills become more expansive. GitHub is a reasonable place to keep a larger example library, but it asks the reader to leave the explanatory context of the documentation at the moment they are trying to turn the rules into a mental model.

I think the documentation should contain at least one minimal example and one moderately composed example, with short annotations explaining why each part exists. After that, GitHub makes sense as the place to explore larger or more specialized implementations.

The distinction matters because examples inside documentation and examples inside repositories do different jobs. The first should teach. The second can show breadth, realistic structure, and implementation detail.

I also want to determine whether the current skills page is doing too many jobs at once. If creation, testing, maintenance, and examples can't be made easy to navigate on one page, the better answer may be a small connected section instead of continually expanding a single page.

## Comparative read: Connectors show what a more complete lifecycle can look like

Connectors are useful here even if they do not become the primary audit target. Their documentation appears to provide a more developed information architecture and a broader lifecycle than the plugin material does.

That gives me a useful comparison rather than an abstract claim that the plugin docs “need more detail.” I can compare the two areas across the same questions:

- Can a reader understand the concept from a cold landing?
- Can they see how the documentation is organized?
- Can they build and test the thing?
- Can they troubleshoot it?
- Can they understand publication and what happens afterward?
- Can they find the next relevant page without already knowing Claude’s internal vocabulary?

If connectors answer more of those questions locally than plugins do, that is evidence of an uneven documentation model across closely related customization surfaces.

## Working thesis

My current thesis is that Claude’s customization documentation explains its individual capabilities unevenly. Connector documentation provides a comparatively complete and navigable lifecycle. Plugin documentation, even though it combines several of those capabilities, assumes more background knowledge and provides less local orientation.

That creates an inversion: the most interconnected customization surface is also one of the least self-explanatory.

The answer isn't to duplicate every underlying guide inside the plugin section. It's to give readers a unified vocabulary, explain how the pieces relate, and provide a complete path from first encounter through submission and maintenance. The deeper pages can supply implementation detail once the reader understands the system they're entering.

## Evidence I still need

- Canonical URLs and exact titles for every page in scope.
- The specific lines that name skills, MCP connectors, slash commands, and sub-agents.
- Confirmation of whether those terms are linked, hoverable, or keyboard-accessible in the rendered pages.
- A map of the links leaving the plugin submission page and the purpose of each destination.
- A side-by-side comparison of plugin and connector navigation and lifecycle coverage.
- One or two concrete reader tasks, such as understanding plugin anatomy from a cold landing or preparing a plugin for submission.

Until I capture that evidence, these are candidate findings and a working thesis, not final verdicts.
