# Claude customization docs: merged working findings

This is still a working read, not the final audit. I haven't finished capturing every URL, quotation, or piece of page-level evidence yet. What I'm trying to pin down is where the documentation feels healthy, where it starts making assumptions about the reader, and which part of the system is actually worth auditing more deeply.

The findings below keep that distinction explicit: the observations are strong enough to guide the next pass, but they don't become final verdicts until the evidence fields are complete.

These started as my independent scan findings. I'm keeping that provenance visible so I can compare them with the assistant's audit after both arms have formed, instead of letting one quietly shape the other.

**This file is working research, not the Part 1 deliverable.** The finished audit is [`part1_audit_memo.md`](part1_audit_memo.md); this document is the raw independent-arm input that fed it. The `Current confidence` / `Current status` / `Canonical URLs still needed` fields below are deliberate working-research markers — they record what a next evidence pass would still nail down, and are not open gaps in the memo.

## Scope decision

After scanning connectors, skills, and plugins, connectors currently look like the healthiest part of the group. The left navigation is fairly complete, and the documentation covers most of the lifecycle I would expect: what MCPs are, how to build and bundle a connector, authentication options, testing, troubleshooting, publishing, and some higher-level integrations.

That doesn't mean the connector documentation is finished or problem-free. It means that, compared with the other two areas, I can see a reasonably complete path through the material.

Skills and plugins are more attractive audit targets. Skills have useful creation guidance, but a lot of it is concentrated on one page. Plugins are probably the stronger focus because they touch several Claude customization surfaces at once. A plugin can bundle skills, MCP connectors, slash commands, and sub-agents. So the plugin documentation has to do more than explain a directory structure: it has to help the reader understand how those parts fit together.

Right now, I don't think it consistently does that.

### Scope frame

- **Primary focus:** Plugins
- **Secondary focus:** Skills
- **Comparison case:** Connectors
- **Cross-cutting axis:** Agentic usability
- **Reason:** The plugin overview and submission pages explain the core concepts reasonably well, but the author journey is distributed across the overview, submission guide, Claude Code guide and reference, connector policy, directory terms, and two submission surfaces.
- **Current confidence:** Directionally strong, pending page-level evidence collection.

### Page ownership boundary

The reorganization only works if each page has a clear job:

- **`claude.com/docs/plugins/overview`:** Own the cross-product concept, Claude Code/Cowork relationship, surface support model, and central lifecycle map.
- **`claude.com/docs/plugins/submit`:** Own submission readiness, eligibility, review governance, publication outcomes, and exception paths.
- **`code.claude.com/docs/en/plugins`:** Own the practical authoring tutorial: choosing plugins, creating one, package structure, testing, debugging, sharing, submitting, and migration.
- **`code.claude.com/docs/en/plugins-reference`:** Own the technical contract: component specifications, schemas, paths, scopes, CLI behavior, syncing, caching, troubleshooting, distribution, and versioning.

The first two pages should summarize decision-critical consequences and route at the right moment. They shouldn't absorb the tutorial or reference material from the second two.

## Additional evaluation axis: Agentic guidance

There's another reader in this system that the plugin documentation should account for: the agent helping someone build the plugin.

The hypothesis behind this axis is that at least some plugin authors will use Claude Code or another agentic coding environment while they build. If that holds, the page doesn't only need to explain the concept to a person. It should make the work legible enough that a person can hand the guidance to an agent, define a bounded task, and verify what comes back without the agent having to guess at prerequisites, package structure, validation, or security expectations.

The current submission page already moves in this direction. It explains that plugins can include dynamically activated skills and delegated sub-agents, and it introduces a `SETUP.md` skill that Claude follows when configuring bundled MCP servers. So the gap isn't that agentic guidance is absent. The question is whether that guidance is organized well enough to support an end-to-end, bounded build and submission task without making the human or agent reconstruct the workflow across several documentation surfaces.

That doesn't mean creating a second, agent-only version of the documentation or adding a vague “build this with Claude” prompt. The stronger move is to make the canonical page more executable for both audiences. Clear prerequisites, explicit file layouts, ordered procedures, expected outputs, validation steps, failure states, and decision points all help a human reader. They also give an agent fewer gaps to fill with plausible but unsupported assumptions.

For an updated plugin page, I would consider including:

- A bounded statement of what the reader or agent is building.
- Explicit prerequisites and supported starting states.
- A canonical package tree with required and optional components labeled.
- Ordered implementation steps with expected outputs.
- Validation and security checks that can be run before submission.
- Common failure states, likely causes, and recovery steps.
- Clear points where the agent should stop and ask for a user decision instead of choosing silently.
- A compact handoff checklist or reusable task brief grounded in the page's canonical guidance.

The last item matters, but it should come after the documentation is structurally sound. A copyable agent brief can't compensate for missing lifecycle guidance. It can only make good guidance easier to operationalize.

### Evaluation frame

- **Core question:** Can a reader use this page to give an agent a bounded plugin task and then verify the result?
- **Class:** Agentic usability · procedural completeness · IA/findability
- **Current status:** Cross-cutting evaluation axis, not yet a confirmed finding.
- **Evidence required:** Test a representative plugin task using only the current documentation. Record clarification requests, unsupported assumptions, structural errors, omitted validation or security steps, and the evidence available to verify completion.
- **Comparison:** Repeat the same task against the proposed page structure using the same model, prompt, starting state, and environment. Compare intervention count, observed errors or omissions, and verification completeness. Treat a single paired run as exploratory evidence, not a generalized rate.
- **Design constraint:** Improve the canonical documentation for human and agent use rather than creating a parallel source of truth that can drift.

## Finding 1: Plugin concepts are explained, but the operational journey is fragmented

The overview page is stronger than my first scan suggested. It defines plugins, explains what they do, gives a directory of examples, places them in both Claude Code and Cowork, and defines all four component types with concrete examples. The submission page reinforces that model, explains three distribution paths, introduces `SETUP.md`, covers basic security, and provides a submission happy path.

So the defensible problem isn't “the information isn't there.” A lot of it is there, and some of it is quite good.

The problem is that a reader still has to assemble one author journey across several pages and domains. The overview defines a Claude Code plugin as a versioned directory with `plugin.json`, then says Cowork has full plugin support without clearly stating whether the same artifact, component behavior, and configuration transfer unchanged. The next-step routes cover browsing, creating, skills, connectors, and submission, but they don't present a single discover, build, validate, submit, publish, update, and maintain path.

The submission page continues that pattern. Installation guidance lives in the Claude Code docs. Marketplace setup lives on another Claude Code page. Security and directory requirements move into support articles. A permissions detail points into connector-submission documentation. Technical construction moves to the plugin guide and reference. The actual forms live on Claude.ai and Console.

The two Claude Code pages close more gaps than my initial scan accounted for. The authoring guide provides a full quickstart, package layout, local testing, debugging, sharing, community submission, migration, and next-step routes. The reference documents components, manifest fields, installation scopes, Claude.ai-synced plugins, CLI operations, troubleshooting, and version management. Those details aren't absent, and they shouldn't be copied into the higher-level overview.

Some of that separation is correct. A single overview page shouldn't duplicate the full reference, policy, and submission forms. But it should act as the central map: show the complete lifecycle, explain which decisions belong at each stage, clarify the Claude Code and Cowork relationship, and route readers to deeper material after they understand where they are in the process.

### Audit frame

- **Page(s):** `https://claude.com/docs/plugins/overview` and `https://claude.com/docs/plugins/submit`
- **Evidence observed:** Both pages provide substantial conceptual and procedural guidance, while routing stages of the same author journey across Claude Docs, Claude Code Docs, Support, Claude.ai, Console, and the plugin directory.
- **Evidence still required:** Map every stage and destination, then test whether a first-time author can identify the correct next page and understand the Claude Code/Cowork contract without outside assistance.
- **Class:** IA/findability · cross-platform contract · lifecycle fragmentation
- **Severity:** Medium candidate, potentially higher if task testing shows material failure or rework.

## Finding 2: The submission page covers the happy path but leaves governance and exception handling opaque

The submission page isn't generally sparse. It explains distribution options, community versus Anthropic Verified plugins, what makes a coherent plugin, MCP setup, connector safety, directory terms, security, eligibility, validation, submission, status tracking, and automatic updates after publication.

That gives an author a workable happy path: use a public GitHub repository, run `claude plugin validate`, choose an eligible form, submit, and wait for review. For Claude.ai submissions, the page also identifies where review status appears. After publication, repository updates are mirrored automatically and screened without another submission.

The weaker part is everything that happens when the happy path branches or fails. The page doesn't preview what either form requires, explain whether the Claude.ai and Console paths are functionally equivalent, or identify where Console authors track status. “Basic automated review” has no visible rubric, status definitions, rejection categories, remediation path, or appeal process.

The linked Claude Code authoring guide does explain that the review pipeline runs the same `claude plugin validate` check plus automated safety screening, and that validation warnings don't fail unless the author uses `--strict`. So that relationship isn't absent from the documentation estate. It is decision-critical submission information that currently sits one hierarchy away from the page where an author is preparing to submit.

The same distinction applies after publication. The authoring guide explains that approved community plugins are pinned to a commit SHA, CI updates that pin as new commits arrive, and the public catalog syncs nightly. The technical reference explains how explicit versions, commit SHAs, and archive digests control update behavior. That information exists, but the submission page doesn't summarize how its automatic-mirroring promise connects to those mechanics.

The remaining gaps are narrower and more consequential: which repository branch feeds the pin, what happens when update screening fails, whether the prior release stays active, how rollback works, and how authors should handle deprecation, delisting, ownership transfer, repository disappearance or privatization, security incidents, and changes to verification status.

I would preserve the existing happy path and add a compact governance and exception layer:

1. A preflight summary of required form inputs and repository expectations.
2. What `claude plugin validate` checks, and what remains subject to directory review.
3. Whether Claude.ai and Console submissions share the same review and status model.
4. Review stages, status definitions, and likely decision outcomes.
5. Rejection, remediation, and resubmission paths.
6. Update-screening behavior, versioning, rollback, and notification.
7. Deprecation, delisting, ownership transfer, and security-incident handling.

The detailed policies can remain on their canonical pages. The submission page should summarize the decision-critical parts and make the handoffs explicit enough that authors don't have to infer the operating model.

### Audit frame

- **Page(s):** `https://claude.com/docs/plugins/submit`
- **Evidence observed:** The submission page provides the normal-case sequence. The Claude Code guide and reference supply validation, commit-pinning, synchronization, and version-management mechanics, but review criteria, Console tracking, exception recovery, and failed-update behavior remain unstated or lack a local summary.
- **Evidence still required:** Inspect both submission forms plus the directory terms and policy before classifying the remaining items as absent from the estate.
- **Class:** Lifecycle/governance · exception handling · IA/findability
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

My current thesis is no longer that Claude's plugin information is broadly missing or that the pages fail to explain the component model. Both the overview and submission pages do a fair amount well.

The problem is distributed completeness. The documentation estate contains much of the necessary information, but a reader has to reconstruct one author journey across multiple page hierarchies, domains, policies, references, and submission surfaces. The material is often complete at the page-set level without being complete at the task level.

The answer isn't to collapse every guide and reference into one oversized page. It's to make the plugin overview the central lifecycle map and the submission page the central source for submission readiness, review governance, and exception handling. The Claude Code authoring guide should remain the practical tutorial, and the plugins reference should remain the technical source of truth. The higher-level pages should summarize decision-critical information locally, then route readers outward for implementation depth. That same structure would also support bounded agentic work without asking an agent to invent the connective tissue between pages.

## Evidence pass

Before promoting these candidate findings into the final audit:

- Build a stage-by-stage map from discovery through maintenance and identify which page currently owns each stage.
- Map every link leaving the overview and submission pages and state what question each destination is expected to answer.
- Verify whether Claude Code and Cowork use the same artifact, manifest, components, and update semantics, or document the differences.
- Treat the Claude Code authoring guide and plugins reference as canonical for build and technical mechanics; pull forward summaries and routes, not copied procedures.
- Inspect both submission forms plus the directory terms and policy before classifying the remaining governance and exception information as absent from the estate.
- Test concrete reader tasks such as choosing a distribution path, preparing a submission, responding to rejection, and rolling back a failed published update.
- Compare plugin and connector lifecycle coverage using the same dimensions.
- Run one bounded agentic task from the current plugin guidance and record clarifications, unsupported assumptions, omissions, and verification evidence.

Until I capture that evidence, these remain candidate findings and a working thesis, not final verdicts.
