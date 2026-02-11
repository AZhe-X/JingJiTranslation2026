## team-lead at 2026-02-11 08:41:57

*Vote: move What to Report to standalone file*

Vote requested: Should we move the "What to Report" section (lines 65-95 of the Standby Reader Profile) out of the Profile.md and into a standalone file?

The reasoning: Profile.md will be used as the prompt to generate/spawn the reader agent. If "What to Report" (including the per-essay questions, final prompts, and critical experiential checks) is part of that prompt, the reader will see all those questions BEFORE reading — which could bias their experience (e.g., knowing they'll be asked "What happened to your experience across the three examples?" for Essay 3 could prime them to watch for it).

Moving it to a standalone file means we can give the reader the profile (role, personality, reading instructions) at spawn, and then deliver the reporting questions AFTER they finish reading each piece — keeping the reading experience uncontaminated.

Vote YES to move "What to Report" to a standalone file, or NO to keep it in the profile. Brief reasoning please.

---

## Claude at 2026-02-11 08:42:08

[tool: SendMessage]
{
  "type": "message",
  "recipient": "team-lead",
  "content": "**YES** — This is exactly right, and the reasoning is a direct application of the framework's own principles. If the reader knows in advance that they'll be asked about the Essay 3 progression or the meme contrast, they read those passages in \"test-taking mode\" rather than experiential mode — they attend to what they expect to be asked about rather than to what actually happens to them. This is the difference between first-person experience (what the text is designed to produce) and third-person observation (watching yourself have an experience because you know you'll report on it). The former is what we need to test; the latter contaminates it.\n\nDelivering the reporting questions AFTER each piece preserves the phenomenol
... [truncated]

---

## Claude at 2026-02-11 08:42:12

Voted **YES** — pre-knowledge of specific reporting questions would shift the reader from experiential mode to test-taking mode, contaminating exactly what we need to measure. Questions should be delivered after reading, not before. Awaiting next task.

---

