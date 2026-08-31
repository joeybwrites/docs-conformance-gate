#!/usr/bin/env python3
"""Plugin documentation conformance gate (prototype).

Implements a deterministic subset of the plugin documentation standard
(../standards/plugin_style_guide.md):

  S4  prerequisite bridging   - every core concept a page uses that is not in
                                its `assumes:` frontmatter (and that it is not
                                `canonical_for:`) must link to the concept's
                                owning page.
  S5  contextualized handoff  - an off-property link (code.claude.com /
                                support.claude.com) must be framed (an
                                ownership/summary cue nearby) and either carry
                                a #anchor or target a registered dedicated
                                task page.
  S6  link form (bonus)       - no doubled '/docs/docs/' prefixes.

Runs on Markdown files or directories. Exit code = number of files with
findings (0 == clean), so it drops straight into CI.

    python conformance_gate.py fixtures/ corpus/
    python conformance_gate.py --json corpus/plugins_overview.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
HOST_RE = re.compile(r"https?://([^/]+)")


def load_registry(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(text: str):
    """Minimal YAML frontmatter: `key: value` and `key: [a, b]`.
    Returns (meta, body_offset_in_lines)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, 0
    meta: dict = {}
    for ln in lines[1:end]:
        if ":" not in ln:
            continue
        k, v = ln.split(":", 1)
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            meta[k] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        else:
            meta[k] = v
    return meta, end + 1


def visible_text(line: str) -> str:
    """Replace [text](url) with text, so concept detection ignores URLs."""
    return LINK_RE.sub(lambda m: m.group(1), line)


def host_of(url: str):
    m = HOST_RE.match(url)
    return m.group(1) if m else None


def check_page(path: Path, reg: dict) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    meta, body_off = parse_frontmatter(text)
    lines = text.splitlines()
    body = lines[body_off:]

    assumes = {a.lower() for a in (meta.get("assumes") or [])}
    canonical = {c.lower() for c in (meta.get("canonical_for") or [])}
    findings: list[dict] = []

    # Input contract: the gate expects one actual doc page with top-level
    # frontmatter. A file with none (a pre-standard page, or a meta-doc such as
    # a before/after) has no `assumes`/`canonical_for` to honor, so its S4
    # results may be phantoms. Announce that rather than silently over-flagging.
    if not meta:
        findings.append({
            "rule": "FM", "line": 1, "subject": "",
            "detail": "no frontmatter parsed; the standard expects "
                      "title/content-type/assumes/canonical_for. Exemptions are "
                      "inactive, so any S4 concept findings below may be phantoms.",
        })

    all_targets = [url for ln in body for _t, url in
                   ((m.group(1), m.group(2)) for m in LINK_RE.finditer(ln))]

    # ---- S4: prerequisite bridging ----
    for cid, spec in reg["concepts"].items():
        if cid.lower() in assumes or cid.lower() in canonical:
            continue
        alias_pat = re.compile(
            r"\b(" + "|".join(re.escape(a) for a in
                               sorted(spec["aliases"], key=len, reverse=True)) + r")\b",
            re.IGNORECASE)
        first_line = None
        for idx, ln in enumerate(body):
            if alias_pat.search(visible_text(ln)):
                first_line = body_off + idx + 1
                break
        if first_line is None:
            continue  # concept not used here
        if not any(spec["owner_match"] in url for url in all_targets):
            findings.append({
                "rule": "S4", "line": first_line, "subject": cid,
                "detail": f'"{cid}" is used but never linked to its owner '
                          f'({spec["owner_match"]}); it is not in assumes/canonical_for',
            })

    # ---- S5: contextualized cross-property handoff ----
    off_hosts = set(reg["off_property_hosts"])
    task_pages = {u.rstrip("/") for u in reg["dedicated_task_pages"]}
    cues = [c.lower() for c in reg["ownership_cues"]]
    for idx, ln in enumerate(body):
        lineno = body_off + idx + 1
        window = " ".join(visible_text(b) for b in body[max(0, idx - 1): idx + 2]).lower()
        for m in LINK_RE.finditer(ln):
            url = m.group(2)
            if host_of(url) not in off_hosts:
                continue
            # A link whose target is a concept's owner is a bridge (S4's domain),
            # not a decision handoff — do not hold it to S5's framing requirement.
            if any(spec["owner_match"] in url for spec in reg["concepts"].values()):
                continue
            base = url.split("#")[0].rstrip("/")
            registered = base in task_pages
            has_anchor = "#" in url
            cue_present = any(c in window for c in cues)
            if registered:
                # A registered destination is an intentional handoff target;
                # a descriptive (>=2-word) label frames it adequately.
                framed = cue_present or len(re.findall(r"\w+", m.group(1))) >= 2
            else:
                # An arbitrary off-property link needs an ownership cue or a
                # real summary clause (>=6 words) before it.
                framed = cue_present or len(re.findall(r"\w+", ln[:m.start()])) >= 6
            problems = []
            if not (has_anchor or registered):
                problems.append("no #anchor and not a registered task page")
            if not framed:
                problems.append("no ownership/summary framing nearby")
            if problems:
                findings.append({
                    "rule": "S5", "line": lineno, "subject": url,
                    "detail": "off-property handoff: " + "; ".join(problems),
                })

    # ---- S6: link form (bonus) ----
    for idx, ln in enumerate(lines):
        if "/docs/docs/" in ln:
            findings.append({
                "rule": "S6", "line": idx + 1, "subject": "",
                "detail": "doubled '/docs/docs/' link prefix",
            })

    # ---- S3: contradiction of the evidenced state (Block) ----
    # Curated + configurable: registry `contradiction_patterns` are claims known
    # to contradict the matrix's evidenced state. Deterministic (regex), and a
    # LEVER the docs/product team edits as truths shift or conflicts are found.
    # (The fuller design compares structured claims to the matrix directly.)
    body_text = "\n".join(body)
    for cp in reg.get("contradiction_patterns", []):
        m = re.search(cp["pattern"], body_text, re.IGNORECASE)
        if m:
            line = body_off + body_text[:m.start()].count("\n") + 1
            findings.append({
                "rule": "S3", "line": line, "subject": cp["id"],
                "detail": cp["reason"], "note": cp.get("note", ""),
            })
    return findings


_SKIP_NAMES = {"readme.md", "notes.md"}  # repo meta-files, not doc pages


def collect(paths):
    files = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            files.extend(sorted(f for f in pp.glob("*.md")
                                if f.name.lower() not in _SKIP_NAMES))
        else:
            files.append(pp)  # explicit path is honored as-is
    return files


def verdict_for(findings, reg):
    """Non-compensating verdict: a page's disposition is its WORST finding's
    tier. Severities and tier names come from registry.json, so they are
    adjustable levers rather than hard-coded policy. Returns (verdict, severity)."""
    order = reg["severity_order"]
    sev_map = reg["severities"]
    worst = "clean"
    for f in findings:
        sev = sev_map.get(f["rule"], "revise")
        if sev in order and order.index(sev) > order.index(worst):
            worst = sev
    return reg["verdicts"][worst], worst


def main():
    ap = argparse.ArgumentParser(description="Plugin docs conformance gate (prototype).")
    ap.add_argument("paths", nargs="+", help="Markdown files or directories")
    ap.add_argument("--registry", default=str(Path(__file__).parent / "registry.json"))
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    reg = load_registry(Path(args.registry))
    results = {str(f): check_page(f, reg) for f in collect(args.paths)}
    verdicts = {f: verdict_for(finds, reg) for f, finds in results.items()}
    # Non-blocking tiers (Ship / Ship with Notes) pass CI; Revise / Reject block.
    blocking = sum(1 for _v, sev in verdicts.values() if sev in ("revise", "block"))

    if args.json:
        out = {f: {"verdict": verdicts[f][0], "severity": verdicts[f][1], "findings": finds}
               for f, finds in results.items()}
        print(json.dumps(out, indent=2))
    else:
        for f, finds in results.items():
            name = Path(f).name
            verdict, _sev = verdicts[f]
            suffix = f"  ({len(finds)} finding(s))" if finds else ""
            print(f"{verdict.upper():<16}{name}{suffix}")
            for fd in sorted(finds, key=lambda x: (x["line"], x["rule"])):
                s = f' [{fd["subject"]}]' if fd["subject"] else ""
                print(f'    {fd["rule"]}  line {fd["line"]}{s}: {fd["detail"]}')
                if fd.get("note"):
                    print(f'        note to owner: {fd["note"]}')
        print(f"\n{blocking} of {len(results)} file(s) block (Revise or Reject); "
              f"Ship / Ship with Notes pass CI.")

    sys.exit(min(blocking, 100))


if __name__ == "__main__":
    main()
