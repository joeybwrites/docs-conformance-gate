# Claude customization docs: merged working findings

This is still a working read, not the final audit. I haven't finished capturing every URL, quotation, or piece of page-level evidence yet. What I'm trying to pin down is where the documentation feels healthy, where it starts making assumptions about the reader, and which part of the system is actually worth auditing more deeply.

The findings below keep that distinction explicit: the observations are strong enough to guide the next pass, but they don't become final verdicts until the evidence fields are complete.

These started as my independent scan findings. I'm keeping that provenance visible so I can compare them with the assistant's audit after both arms have formed, instead of letting one quietly shape the other.

## Scope decision

After scanning connectors, skills, and plugins, connectors currently look like the healthiest part of the group. The left navigation is fairly complete, and the documentation covers most of the lifecycle I would expect: what MCPs are, how to build and bundle a connector, authentication options, testing, troubleshooting, publishing, and some higher-level integrations.

That doesn't mean the connector documentation is finished or problem-free. It means that, compared with the other two areas, I can see a reasonably complete path through the material.

Skills and plugins are more attractive audit targets. Skills have useful creation guidance, but a lot of it is concentrated on one page. Plugins are probably the stronger focus because they touch several Claude customization surfaces at once. A plugin can bundle skills, MCP connectors, slash commands, and sub-agents. So the plugin documentation has to do more than explain a directory structure: it has to help the reader understand how those parts fit together.

Right now, I don't think it consistently does that.

### Scope frame

- **Primary focus:** Plugins
- **Secondary focus:** Skills
- **Comparison case:** Connectors
- **Reason:** Plugins compose several customization primitives but appear to provide less local orientation and lifecycle support than connectors.
- **Current confidence:** Directionally strong, pending page-level evidence collection.

## Finding 1: Plugin pages assume the reader already understands the component parts

The plugin pages refer to skills, MCP connectors, slash commands, and sub-agents, but those terms aren't always linked or lightly explained where they appear. That may be fine for someone who's already read through the rest of the Claude documentation. It's less useful for someone who lands directly on the plugin page because they want to understand what a plugin is or decide whether they should build one.

This creates a slightly backwards experience. Plugins are the point where several Claude features come together, but the documentation for that combined surface gives the reader less orientation than some of the individual features do.

I don't think the fix is to repeat the full connector, skill, command, and sub-agent documentation on every plugin page. But the page does need a compact explanation of what a plugin can contain, what each component contributes, and where to go next for the full implementation details. The component names should also be links anywhere the reader is being asked to understand plugin anatomy or prepare a submission.

### Audit frame

- **Page(s):** Plugin overview and plugin submission pages. Canonical URLs still needed.
- **Evidence observed:** The submission material names component types and points readers toward other Claude documentation and the plugin marketplace, but doesn't provide enough local context to orient a cold entrant.
- **Evidence still required:** Capture the exact passages and verify whether each term is linked, hoverable, and keyboard-accessible in the rendered page.
- **Class:** IA/findability · terminology · gap
- **Severity:** High candidate

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

### Audit frame

- **Page(s):** Plugin submission page. Canonical URL still needed.
- **Evidence observed:** Setup, directory, security, sign-in, and submission guidance is present, while a substantial portion of the supporting explanation is delegated to deeper pages and marketplace links.
- **Evidence still required:** Record the current section sequence, map every outbound link, and identify the reader question each destination is expected to answer.
- **Class:** Lifecycle/scope drift · IA/findability · gap
- **Severity:** High candidate

## Finding 3: Skills have useful creation guidance, but the example path leaves the documentation too quickly

The skills documentation covers a fair amount on the creation page: how to create a custom skill, what is required, how the Markdown files are structured and maintained, and how supporting resources and brand colors can be handled.

The weaker point is the example path. The documentation points readers toward GitHub for examples, particularly as the skills become more expansive. GitHub is a reasonable place to keep a larger example library, but it asks the reader to leave the explanatory context of the documentation at the moment they're trying to turn the rules into a mental model.

I think the documentation should contain at least one minimal example and one moderately composed example, with short annotations explaining why each part exists. After that, GitHub makes sense as the place to explore larger or more specialized implementations.

The distinction matters because examples inside documentation and examples inside repositories do different jobs. The first should teach. The second can show breadth, realistic structure, and implementation detail.

I also want to determine whether the current skills page is doing too many jobs at once. If creation, testing, maintenance, and examples can't be made easy to navigate on one page, the better answer may be a small connected section instead of continually expanding a single page.

### Audit frame

- **Page(s):** Skills overview or create-custom-skills page and the linked Skills GitHub examples. Canonical URLs still needed.
- **Evidence observed:** The page covers custom-skill requirements, Markdown structure and maintenance, brand colors, and supporting resources, then points to GitHub for examples, including more expansive skills.
- **Evidence still required:** Record which examples appear locally, which require leaving the docs, and whether the external examples explain the design choices they demonstrate.
- **Class:** Gap · IA/findability
- **Severity:** Medium candidate

## Comparative observation: Connectors show what a more complete lifecycle can look like

Connectors are useful here even if they don't become the primary audit target. Their documentation appears to provide a more developed information architecture and a broader lifecycle than the plugin material does.

That gives me a useful comparison instead of an abstract claim that the plugin docs “need more detail.” I can compare the two areas across the same questions:

- Can a reader understand the concept from a cold landing?
- Can they see how the documentation is organized?
- Can they build and test the thing?
- Can they troubleshoot it?
- Can they understand publication and what happens afterward?
- Can they find the next relevant page without already knowing Claude's internal vocabulary?

If connectors answer more of those questions locally than plugins do, that's evidence of an uneven documentation model across closely related customization surfaces.

### Comparison frame

- **Page(s):** Connector documentation section. Canonical URLs still needed.
- **Observed strengths:** Healthy left navigation and coverage of MCP concepts, building, bundling, authentication, testing, troubleshooting, publishing behavior, and higher-level integrations.
- **Analytical use:** Compare plugins and connectors using the same lifecycle and findability dimensions instead of relying on a generalized judgment about depth.
- **Caution:** This is a comparative first-scan impression, not a finding that connector documentation needs no changes.

## Working thesis

My current thesis is that Claude's customization documentation explains its individual capabilities unevenly. Connector documentation provides a comparatively complete and navigable lifecycle. Plugin documentation, even though it combines several of those capabilities, assumes more background knowledge and provides less local orientation.

That creates an inversion: the most interconnected customization surface is also one of the least self-explanatory.

The answer isn't to duplicate every underlying guide inside the plugin section. It's to give readers a unified vocabulary, explain how the pieces relate, and provide a complete path from first encounter through submission and maintenance. The deeper pages can supply implementation detail once the reader understands the system they're entering.

## Evidence pass

Before promoting these candidate findings into the final audit:

- Record canonical URLs and exact page titles for every page in scope.
- Quote or closely transcribe the specific lines that name skills, MCP connectors, slash commands, and sub-agents.
- Verify whether those terms are linked, hoverable, and keyboard-accessible in the rendered pages.
- Map every link leaving the plugin submission page and state what question each destination is expected to answer.
- Compare plugin and connector left-navigation depth and lifecycle coverage using the same dimensions.
- Test one or two concrete reader tasks, such as understanding plugin anatomy from a cold landing or preparing a plugin for submission.

Until I capture that evidence, these remain candidate findings and a working thesis, not final verdicts.
