## team-lead at 2026-02-11 04:36:25

*经验 and 体验 both *

Follow-up on the 经验 vote. The author (team lead) raises a concern:

If we set 经验 → "experience" as main, then both 经验 AND 体验 have "experience" as their main translation. The full mapping would be:

- 感受 → "feeling" / "felt experience"
- 体验 → "experience"
- 经验 → "experience"
- 感觉 → "sensation"

Two different Chinese terms with the same English main translation. Is this acceptable, or does it create a problem?

If you think it's fine, explain why. If you think it's a problem, what's your solution — should one of them change?

---

## Claude at 2026-02-11 04:36:35

[tool: SendMessage]
{
  "type": "message",
  "recipient": "team-lead",
  "content": "**It's a problem.** Two distinct Chinese terms with the same English default means the translator has no guidance for the default case, and the reader loses a distinction the author maintains.\n\n**Solution: flip 经验 to \"empirical experience\" as main.**\n\nI was wrong in my previous vote. I was optimizing for naturalness in isolation (经验的总结 → \"summary of experience\" sounds better), but in the context of a four-term system where each term needs a distinct default, disambiguation takes priority over elegance. The compounds still read fine: \"summary of empirical experience,\" \"prediction from empirical experience,\" \"abstraction of empirical experience\" — heavier, yes, but clear.\n\n**Revised mapping:**\n- 感受 → \"feeling\
... [truncated]

---

## Claude at 2026-02-11 04:36:38

Reversed my position. With both 经验 and 体验 defaulting to "experience," the translator loses guidance and the reader loses a distinction the author maintains. The correct move is **"empirical experience"** as the main for 经验, giving four distinct English defaults across the four-term system. Systematic clarity over case-by-case naturalness when building a dictionary.

---

