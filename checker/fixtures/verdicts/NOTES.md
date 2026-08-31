# Verdict tiers — worked examples + the note returned to the owning team

Four variants of the `plugins/overview` redraft, each engineered to exercise one part of the non-compensating verdict schema. Run them:

```bash
python ../../conformance_gate.py .
```

**Non-compensating:** a page's verdict is its *worst* finding. That's the point of tiers over a score.

---

## SHIP — `verdict_ship.md`
No findings. Clear to publish.

## SHIP WITH NOTES — `verdict_ship_with_notes.md`
Non-blocking; publishable as-is.
- **Finding:** S6, line 31 — a "See also" connectors link uses a doubled `/docs/docs/` prefix.
- **Note to team:** "Clear to ship. One cleanup for a follow-up PR: normalize `/docs/docs/connectors/overview` to `/docs/connectors/overview`. It resolves via redirect today, but it's a duplicate URL and shouldn't be minted new."

## REVISE — `verdict_revise.md`
Blocking (must fix before merge).
- **Finding:** S5, line 27 — the "More" section links the Claude Code guide with no framing and no anchor.
- **Note to team:** "Please revise before merge. The 'More' link drops the reader onto code.claude.com with no summary of what they'll find, no statement of why Claude Code owns that step, and no section anchor. Add a one-line frame + link the exact section, or remove the link."

## OWNER DECISION (Revise by default) — `verdict_owner_decision.md`
Blocking, and flagged for a human owner — **not** an automatic Reject.
- **Finding:** S3, line 27 — asserts plugin availability in Chat as settled fact, which the matrix records as a live, unresolved contradiction.
- **Why not an auto-Reject:** the checker can't adjudicate which source is current (the "Chat" claim vs. `cowork/guide/plugins`), so it surfaces the passage for a human decision rather than rejecting it outright. Set `severities.S3 = "block"` in `registry.json` to make contradictions verdict as **Reject** automatically.
- **Note to team:** "Owner decision needed. This states Chat availability as settled fact, but that availability is a live contradiction between the support guidance and `cowork/guide/plugins`. Describe it as unresolved and link the support matrix, or resolve the conflict with the availability owner before this ships."

---

**On Reject:** with the default levers, the automated gate reaches up to Revise. Reject is a disposition a human owner applies (or the S3 lever above), because deciding that a claim is *definitively* false — not just conflicting — needs source adjudication the checker doesn't do.
