# Verdict tiers — worked examples + the note returned to the owning team

Four variants of the `plugins/overview` redraft, each engineered to land on one tier of the non-compensating verdict schema. Run them:

```bash
python ../../conformance_gate.py .
```

**Non-compensating:** a page's verdict is its *worst* finding. `verdict_reject.md` is otherwise a clean, well-linked page — one contradiction is enough to block it. That's the point of tiers over a score.

---

## SHIP — `verdict_ship.md`
No findings. Clear to publish.

## SHIP WITH NOTES — `verdict_ship_with_notes.md`
Non-blocking; publishable as-is.
- **Finding:** S6, line 31 — the "See also" connectors link uses a doubled `/docs/docs/` prefix.
- **Note to team:** "Clear to ship. One cleanup for a follow-up PR: normalize `/docs/docs/connectors/overview` to `/docs/connectors/overview`. It resolves via redirect today, but it's a duplicate URL and shouldn't be minted new."

## REVISE — `verdict_revise.md`
Blocking (must fix before merge).
- **Finding:** S5, line 27 — the "More" section links the Claude Code guide with no framing and no anchor.
- **Note to team:** "Please revise before merge. The 'More' link drops the reader onto code.claude.com with no summary of what they'll find, no statement of why Claude Code owns that step, and no section anchor. Add a one-line frame + link the exact section, or remove the link. Re-run the gate to confirm."

## REJECT — `verdict_reject.md`
Blocking (do not merge).
- **Finding:** S3, line 27 — states plugin availability in Chat as settled fact.
- **Note to team:** "Do not merge. The Availability section asserts plugins are fully available in Chat as settled fact, but that availability is a live, unresolved contradiction between the support guidance and `cowork/guide/plugins`. Publishing it makes the docs assert something the estate itself contradicts. Describe Chat availability as unresolved and link the support matrix, or resolve the conflict with the availability owner first — then re-submit."
