# Joey — Independent Scan Findings (blind arm)

Your own findings from scanning `claude.com/docs`, kept separate from the assistant's audit so the two arms stay independent. We compare after both form — converge = strong signal, diverge = look harder. Dump freely; ranking comes later, don't let format slow you.

**Per finding (loose):**
- **Page(s):** URL(s)
- **What's wrong:**
- **Evidence:** the actual line / section
- **Class:** IA/findability · lifecycle/scope drift · terminology · redundancy · gap · other
- **Severity:** high / med / low

---

## Scan direction

The strongest audit candidates are **Skills** and **Plugins**, with **Plugins** currently the more promising primary focus because the plugin documentation has to connect several customization surfaces: skills, MCP connectors, slash commands, and sub-agents. Connectors appear comparatively healthy and may be more useful as a benchmark for documentation depth and navigation than as the main problem area.

## Candidate finding 1 — Plugin pages assume prerequisite knowledge without providing a local conceptual bridge

- **Page(s):** Plugin overview and plugin submission pages. Exact URLs to capture.
- **What's wrong:** The plugin documentation names constituent features—MCP connectors, skills, slash commands, and sub-agents—but does not make those terms clickable or provide lightweight explanations in place. A reader who lands on the plugin material directly may not understand what each component contributes or how the pieces form a plugin.
- **Evidence:** On the submission page, the component types are presented as assumed vocabulary rather than navigable concepts. The page sends readers elsewhere in the Claude documentation and toward the plugin marketplace, but does not supply enough local context to orient a cold entrant. Capture the exact passages and link behavior during the evidence pass.
- **Class:** IA/findability · terminology · gap
- **Severity:** high candidate
- **Why it matters:** Plugins are an integration layer. The more concepts a page composes, the more orientation it needs. Some intentional repetition would reduce prerequisite hunting and help readers form a usable mental model before setup or submission.
- **Possible remediation:** Add a compact “What a plugin can contain” section with one-sentence definitions, links to each component’s documentation, and a simple example that shows how the components work together. Use the same linked vocabulary on the submission page.

## Candidate finding 2 — The plugin submission page is too sparse for a high-consequence workflow

- **Page(s):** Plugin submission page. Exact URL to capture.
- **What's wrong:** The page covers setup, directory expectations, security, sign-in, and submission at a high level, but relies heavily on outbound or deeper documentation links. It does not appear to offer a self-contained path from “I have a plugin” to “I understand what will be reviewed, what I must prepare, and what happens next.”
- **Evidence:** The current page points readers to other Claude documentation and the plugin marketplace. Capture the exact section sequence, required steps, and destination links during the evidence pass.
- **Class:** lifecycle/scope drift · IA/findability · gap
- **Severity:** high candidate
- **Why it matters:** Submission is a transition point with real failure costs. Readers should not have to reconstruct prerequisites and lifecycle expectations across several pages while preparing to publish.
- **Possible remediation:** Turn the page into a staged checklist: prerequisites, package anatomy, validation/security checks, sign-in and submission, review expectations, publication outcomes, and post-publication maintenance. Link outward for depth while keeping the minimum complete workflow on the page.

## Candidate finding 3 — Skills guidance is concentrated and sends example-seeking readers out of the documentation

- **Page(s):** Skills overview/create-custom-skills page and linked Skills GitHub examples. Exact URLs to capture.
- **What's wrong:** The documentation covers how to create custom skills, required structure, Markdown maintenance, brand colors, and supporting resources, but much of the guidance is concentrated on a single page. Examples route readers to GitHub instead of giving them a graduated learning path inside the documentation.
- **Evidence:** The page points to GitHub for examples, including more expansive skills. Capture which examples are shown locally, which require leaving the docs, and whether the external examples explain why their design choices work.
- **Class:** gap · IA/findability
- **Severity:** medium candidate
- **Why it matters:** Readers need a short example they can understand in context before they are ready to inspect a repository. External examples are useful as a library, but they should extend an in-doc progression rather than substitute for it.
- **Possible remediation:** Embed one minimal and one moderately composed example in the docs, annotate the important decisions, then link to GitHub as the advanced example library. Consider splitting creation, testing, maintenance, and examples into a small connected section if the single page cannot support progressive disclosure cleanly.

## Comparative observation — Connectors look healthier

- **Page(s):** Connector documentation section. Exact URLs to capture.
- **Observation:** Connectors appear to have a healthy left navigation and broader lifecycle coverage: building, bundling, MCP concepts, authentication types, testing, troubleshooting, publishing behavior, and higher-level integrations.
- **Use in the audit:** Treat connectors as a comparison case. The audit can ask why plugins—a bundle that may include connectors and other Claude features—receive less local orientation and lifecycle explanation than connectors themselves.
- **Caution:** This is a comparative impression from the first scan, not yet a finding that connector documentation needs no changes.

## Emerging audit thesis

Claude’s customization documentation explains individual capabilities unevenly. Connector documentation offers a comparatively complete, navigable lifecycle, while plugin documentation—the surface that combines multiple customization primitives—assumes more prior knowledge and provides less local orientation. The result is an inversion: the most compositional concept is among the least self-explanatory. A stronger plugin section would unify the vocabulary of Claude customization, explain how the pieces relate, and provide a complete path from first encounter through submission and maintenance without duplicating every underlying guide.

## Evidence pass still needed

- Record canonical URLs and page titles for every page in scope.
- Quote or closely transcribe the specific lines that name skills, MCP connectors, slash commands, and sub-agents.
- Verify whether those terms are truly unlinked in rendered pages, including keyboard focus and hover behavior.
- Map every outbound/deeper link from the plugin submission page and note the question each destination is expected to answer.
- Compare plugin and connector left-navigation depth and lifecycle coverage using the same dimensions.
- Identify one or two concrete reader tasks to test, such as “understand plugin anatomy from a cold landing” and “prepare a plugin for submission.”

