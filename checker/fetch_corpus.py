#!/usr/bin/env python3
"""Download the in-scope plugin corpus (Markdown) for the conformance gate.

Stdlib only. Each claude.com/docs page has a Markdown twin at <url>.md.
Re-run to refresh the corpus. These are the REAL current pages, so the gate's
output against them is a snapshot of the live estate (pre-standard: none of
them carry the `assumes:` / `canonical_for:` / `content-type:` frontmatter the
standard introduces, which is itself part of what the run shows).
"""
import pathlib
import sys
import urllib.request

PAGES = {
    "plugins_overview.md":      "https://claude.com/docs/plugins/overview.md",
    "plugins_submit.md":        "https://claude.com/docs/plugins/submit.md",
    "connectors_overview.md":   "https://claude.com/docs/connectors/overview.md",
    "cowork_guide_plugins.md":  "https://claude.com/docs/cowork/guide/plugins.md",
    "docs_home.md":             "https://claude.com/docs/index.md",
}

out = pathlib.Path(__file__).parent / "corpus"
out.mkdir(exist_ok=True)
rc = 0
for name, url in PAGES.items():
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "conformance-gate/0.1"})
        data = urllib.request.urlopen(req, timeout=20).read().decode("utf-8", "replace")
        (out / name).write_text(data, encoding="utf-8")
        print(f"ok   {name}  ({len(data)} bytes)")
    except Exception as e:  # noqa: BLE001 - report and continue
        print(f"FAIL {name}: {e}", file=sys.stderr)
        rc = 1
sys.exit(rc)
