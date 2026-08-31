# docs-conformance-gate

A take-home response for the Technical Documentation & Content Engineer (Claude Docs) role: an audit of the Claude Docs **Plugins** slice, a documentation standard that would prevent the problems found, a working conformance checker that enforces a machine-checkable subset of it on the real docs, and an adoption plan.

> Provenance: the analysis, the standard, and the checker are settled. [`work_log.md`](work_log.md) is the full workflow and AI-use disclosure.

## The four parts

- **Part 1 — Audit.** [`audit/part1_audit_memo.md`](audit/part1_audit_memo.md) (the memo) + [`audit/joeyb_findings.md`](audit/joeyb_findings.md) (working findings). Thesis: the plugin docs are substantially complete but **fragmented** — no page owns the cross-surface model and the lifecycle as a coherent whole, so readers reconstruct the journey across pages, properties, and product surfaces.
- **Part 2 — Standard.** [`standards/`](standards/) — the style guide ([`plugin_style_guide.md`](standards/plugin_style_guide.md)), an evidence-bounded surface×component matrix ([`plugin_component_matrix.md`](standards/plugin_component_matrix.md)), and a bounded before/after of `plugins/overview` ([`plugin_overview_before_after.md`](standards/plugin_overview_before_after.md)) with a why-note.
- **Part 3 — System.** [`checker/`](checker/) — a deterministic, stdlib-only conformance gate that runs on a real-corpus slice and rolls findings into a non-compensating verdict (Ship / Ship with Notes / Revise / Reject) with adjustable config levers. See [`checker/README.md`](checker/README.md).
- **Part 4 — Adoption.** [`adoption/part4_adoption.md`](adoption/part4_adoption.md).

Design and "what I'd build out" notes: [`notes/checker_design.md`](notes/checker_design.md). Claude-use disclosure and work log: [`work_log.md`](work_log.md).

## Run the checker

```bash
cd checker
python test_gate.py                     # expectation-based regression suite (asserts verdicts)
python fetch_corpus.py                  # pull the real 5-page corpus slice
python conformance_gate.py fixtures/    # all fixtures (rule, verdict, rigor)
python conformance_gate.py corpus/      # the live slice
python conformance_gate.py --json corpus/plugins_overview.md
```

Python 3, no dependencies. Exit code = number of blocking files (Revise/Reject), capped at 100; Ship and Ship with Notes exit 0.

## AI use

Built with Claude (via Claude Code) as the primary surface, encouraged by the assignment and disclosed by material contribution in [`work_log.md`](work_log.md).
