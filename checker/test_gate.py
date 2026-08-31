#!/usr/bin/env python3
"""Expectation-based test harness for the conformance gate.

Unlike `conformance_gate.py fixtures/` (a demonstration that prints findings),
this asserts the EXPECTED verdict and finding-rules for each fixture, including
the negative cases the hardened rules must handle. Exit 0 = all pass.

    python test_gate.py
"""
import sys
from pathlib import Path

import conformance_gate as g

HERE = Path(__file__).parent
REG = g.load_registry(HERE / "registry.json")


def outcome(rel):
    findings = g.check_page(HERE / rel, REG)
    verdict, _sev = g.verdict_for(findings, REG)
    return verdict, sorted({f["rule"] for f in findings})


# (fixture, expected verdict, rules that MUST appear, rules that must NOT appear)
CASES = [
    ("fixtures/pass_overview.md",                      "Ship",            [],          ["S3", "S4", "S5", "S6", "FM"]),
    ("fixtures/fail_s4_unbridged.md",                  "Revise",          ["S4"],      []),
    ("fixtures/fail_s4_first_mention.md",              "Revise",          ["S4"],      []),
    ("fixtures/fail_s5_unframed.md",                   "Revise",          ["S5"],      []),
    ("fixtures/fail_s6_doubled_prefix.md",             "Ship with Notes", ["S6"],      ["S3", "S4", "S5"]),
    ("fixtures/verdicts/verdict_ship.md",              "Ship",            [],          ["S3", "S4", "S5", "S6", "FM"]),
    ("fixtures/verdicts/verdict_ship_with_notes.md",   "Ship with Notes", ["S6"],      ["S3", "S4", "S5"]),
    ("fixtures/verdicts/verdict_revise.md",            "Revise",          ["S5"],      []),
    ("fixtures/verdicts/verdict_owner_decision.md",    "Revise",          ["S3"],      []),
    ("fixtures/rigor/mixed_note_and_block.md",         "Revise",          ["S3", "S6"], []),
    ("fixtures/rigor/code_fence_examples.md",          "Ship",            [],          ["S3", "S4", "S5", "S6"]),
    # Hardening negatives:
    ("fixtures/rigor/same_line_first_mention.md",      "Revise",          ["S4"],      []),
    ("fixtures/rigor/inline_code.md",                  "Ship",            [],          ["S4", "S6"]),
    ("fixtures/rigor/html_comment.md",                 "Ship",            [],          ["S3"]),
    ("fixtures/rigor/vague_s5_label.md",               "Revise",          ["S5"],      []),
    ("fixtures/rigor/lookalike_url.md",                "Revise",          ["S4"],      []),
    ("fixtures/rigor/block_array_frontmatter.md",      "Ship",            [],          ["FM", "S4"]),
]


def main():
    failures = 0
    for rel, exp_v, must, mustnot in CASES:
        verdict, rules = outcome(rel)
        ok = (verdict == exp_v
              and all(r in rules for r in must)
              and all(r not in rules for r in mustnot))
        print(f"{'PASS' if ok else 'FAIL'}  {rel:<48} -> {verdict:<16} {rules}")
        if not ok:
            failures += 1
            print(f"      expected {exp_v!r}; include {must}; exclude {mustnot}")
    print(f"\n{len(CASES) - failures}/{len(CASES)} tests passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
