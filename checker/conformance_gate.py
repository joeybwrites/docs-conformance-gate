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
  S3  possible contradiction  - regex-detected contradiction CANDIDATE; NOT an
                                automatic Reject (owner decision by default).
  FM  frontmatter contract    - required fields present and well-typed.

Findings roll up into a non-compensating verdict (Ship / Ship with Notes /
Revise / Reject). Exit code = number of BLOCKING files (Revise or Reject),
capped at 100; Ship and Ship with Notes exit 0. That makes it suitable to drop
into a CI job later (no CI config is included in this prototype).

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
    fm = lines[1:end]
    i = 0
    while i < len(fm):
        ln = fm[i]
        if ":" not in ln:
            i += 1
            continue
        k, v = ln.split(":", 1)
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):        # inline array
            inner = v[1:-1].strip()
            meta[k] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        elif v == "":                                    # possible YAML block list
            items, j = [], i + 1
            while j < len(fm) and fm[j].lstrip().startswith("- "):
                items.append(fm[j].lstrip()[2:].strip())
                j += 1
            if items:
                meta[k] = items
                i = j
                continue
            meta[k] = ""
        else:
            meta[k] = v
        i += 1
    return meta, end + 1


def visible_text(line: str) -> str:
    """Reduce a line to reader-visible prose: drop inline `code` spans and turn
    [text](url) into text, so concept detection ignores URLs and code."""
    line = re.sub(r"`[^`]*`", " ", line)
    return LINK_RE.sub(lambda m: m.group(1), line)


def mask_code(lines):
    """Blank fenced code blocks (``` / ~~~), preserving line count, so rules
    never match documentation examples. Line numbers stay correct."""
    out, fence = [], None
    for ln in lines:
        s = ln.lstrip()
        if fence is None and (s.startswith("```") or s.startswith("~~~")):
            fence = s[:3]
            out.append("")
        elif fence is not None:
            out.append("")
            if s.startswith(fence):
                fence = None
        else:
            out.append(ln)
    return out


def host_of(url: str):
    m = HOST_RE.match(url)
    return m.group(1) if m else None


_DOCS_HOSTS = {"claude.com", "code.claude.com", "support.claude.com"}


def is_owner_link(url: str, owner_match: str) -> bool:
    """True only when url points at the concept owner on an allowed docs host
    (or is a site-relative path), matched at a path/anchor boundary. Prevents
    substring lookalikes like evil.com/skills/overview or /skills/overview-x."""
    host = host_of(url)
    if host is not None and host not in _DOCS_HOSTS:
        return False
    needle = "/" + owner_match
    idx = url.find(needle)
    if idx < 0:
        return False
    end = idx + len(needle)
    return end == len(url) or url[end] in "/#?)"


def segments(line: str):
    """Yield (text, url) in reading order: url=None for plain prose spans,
    url=target for a link's visible text. Lets a rule test the FIRST occurrence."""
    pos = 0
    for m in LINK_RE.finditer(line):
        if m.start() > pos:
            yield line[pos:m.start()], None
        yield m.group(1), m.group(2)
        pos = m.end()
    if pos < len(line):
        yield line[pos:], None


def mask_html_comments(lines):
    """Blank HTML comments (single- and multi-line), preserving line count, so
    rules don't match commentary the reader never sees."""
    out, in_c = [], False
    for ln in lines:
        if in_c:
            if "-->" in ln:
                out.append(ln[ln.index("-->") + 3:])
                in_c = False
            else:
                out.append("")
        elif "<!--" in ln:
            head = ln[:ln.index("<!--")]
            rest = ln[ln.index("<!--"):]
            if "-->" in rest:
                out.append(head + re.sub(r"<!--.*?-->", " ", rest))
            else:
                out.append(head)
                in_c = True
        else:
            out.append(ln)
    return out


def check_page(path: Path, reg: dict) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    meta, body_off = parse_frontmatter(text)
    lines = mask_html_comments(mask_code(text.splitlines()))  # ignore fenced code + HTML comments
    body = lines[body_off:]

    findings: list[dict] = []

    # ---- FM: frontmatter contract ----
    # The standard requires title/content-type/assumes/canonical_for, with
    # assumes/canonical_for as arrays. Partial or malformed frontmatter yields a
    # clear FM finding and disables exemptions, so a scalar `assumes: plugin`
    # can't silence S4 (nor get iterated character by character).
    fm_problems = []
    if not meta:
        fm_problems.append("no frontmatter block found")
    else:
        for field in ("title", "content-type", "assumes", "canonical_for"):
            if field not in meta:
                fm_problems.append(f"missing `{field}`")
        for field in ("assumes", "canonical_for"):
            if field in meta and not isinstance(meta[field], list):
                fm_problems.append(f"`{field}` must be an array")
    if fm_problems:
        findings.append({
            "rule": "FM", "line": 1, "subject": "",
            "detail": "frontmatter contract: " + "; ".join(fm_problems)
                      + ". Exemptions are inactive, so S4 findings here may be phantoms.",
        })
    assumes = ({a.lower() for a in meta["assumes"]}
               if isinstance(meta.get("assumes"), list) else set())
    canonical = ({c.lower() for c in meta["canonical_for"]}
                 if isinstance(meta.get("canonical_for"), list) else set())

    # ---- S4: prerequisite bridging ----
    # The FIRST reader-visible mention of a concept must itself be a link to the
    # concept's owner (unless declared in assumes/canonical_for). A later link
    # does not cure an unlinked first mention.
    for cid, spec in reg["concepts"].items():
        if cid.lower() in assumes or cid.lower() in canonical:
            continue
        alias_pat = re.compile(
            r"\b(" + "|".join(re.escape(a) for a in
                              sorted(spec["aliases"], key=len, reverse=True)) + r")\b",
            re.IGNORECASE)
        hit = None  # (lineno, bridged) for the FIRST occurrence, in reading order
        for i, ln in enumerate(body):
            for seg_text, url in segments(ln):
                if alias_pat.search(visible_text(seg_text)):
                    hit = (body_off + i + 1,
                           url is not None and is_owner_link(url, spec["owner_match"]))
                    break
            if hit is not None:
                break
        if hit is None:
            continue  # concept not used here
        if not hit[1]:
            findings.append({
                "rule": "S4", "line": hit[0], "subject": cid,
                "detail": f'"{cid}" first appears here but this mention does not link '
                          f'to its owner ({spec["owner_match"]}); the first mention must '
                          f'carry the link (not in assumes/canonical_for)',
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
            if any(is_owner_link(url, spec["owner_match"]) for spec in reg["concepts"].values()):
                continue
            base = url.split("#")[0].rstrip("/")
            registered = base in task_pages
            has_anchor = "#" in url
            cue_present = any(c in window for c in cues)
            label_words = re.findall(r"\w+", m.group(1).lower())
            generic = {"here", "this", "that", "page", "more", "read", "learn",
                       "go", "click", "see", "link", "docs", "the", "it"}
            descriptive = len(label_words) >= 2 and not all(w in generic for w in label_words)
            if registered:
                # A registered destination is an intentional handoff target, but a
                # vague all-generic label ("see here") still isn't real framing.
                framed = cue_present or descriptive
            else:
                # An arbitrary off-property link needs an ownership cue or a real
                # summary clause (>=6 words) before it. This is a PROXY for a
                # genuine summary + ownership explanation; it cannot prove one.
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

    # ---- S6: link form (bonus) ---- (inline code already ignored via masking)
    for idx, ln in enumerate(lines):
        if "/docs/docs/" in re.sub(r"`[^`]*`", " ", ln):
            findings.append({
                "rule": "S6", "line": idx + 1, "subject": "",
                "detail": "doubled '/docs/docs/' link prefix",
            })

    # ---- S3: possible contradiction of the evidenced state ----
    # Regex-detected contradiction CANDIDATES. Deliberately NOT an automatic
    # Reject (severity is a registry lever, default "revise" = owner decision):
    # a negation guard is the only polarity handling, and the gate cannot tell a
    # stale claim from the newer correct one. A match flags the passage for a
    # human owner. (The fuller design compares structured claims to the matrix.)
    body_text = "\n".join(body)
    neg_re = re.compile(r"\b(not|never|no longer|cannot|can't|isn't|aren't|"
                        r"don't|doesn't|won't|do not|does not)\b", re.IGNORECASE)
    for cp in reg.get("contradiction_patterns", []):
        for m in re.finditer(cp["pattern"], body_text, re.IGNORECASE):
            pre = body_text[max(0, m.start() - 40):m.start()]
            if neg_re.search(pre) or neg_re.search(m.group(0)):
                continue  # negated / cautionary phrasing is not a positive claim
            line = body_off + body_text[:m.start()].count("\n") + 1
            findings.append({
                "rule": "S3", "line": line, "subject": cp["id"],
                "detail": "possible contradiction (owner decision): " + cp["reason"],
                "note": cp.get("note", ""),
            })
            break  # one finding per pattern
    return findings


_SKIP_NAMES = {"readme.md", "notes.md"}  # repo meta-files, not doc pages


def collect(paths):
    files = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            files.extend(sorted(f for f in pp.rglob("*.md")
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
    # Non-blocking tiers (Ship / Ship with Notes) exit 0; Revise / Reject block.
    blocking = sum(1 for _v, sev in verdicts.values() if sev in ("revise", "block"))

    # Batch verdict: non-compensating across the whole set — the worst page sets
    # the batch's disposition, so a single Reject holds the whole changeset.
    order = reg["severity_order"]
    batch_sev = "clean"
    for _v, sev in verdicts.values():
        if order.index(sev) > order.index(batch_sev):
            batch_sev = sev
    batch_verdict = reg["verdicts"][batch_sev]
    batch_clause = reg.get("batch_clauses", {}).get(batch_sev, "")

    if args.json:
        out = {
            "batch": {"verdict": batch_verdict, "severity": batch_sev, "clause": batch_clause},
            "pages": {f: {"verdict": verdicts[f][0], "severity": verdicts[f][1], "findings": finds}
                      for f, finds in results.items()},
        }
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
              f"Ship / Ship with Notes exit 0.")
        print(f"BATCH VERDICT: {batch_verdict.upper()} - {batch_clause}")

    sys.exit(min(blocking, 100))


if __name__ == "__main__":
    main()
