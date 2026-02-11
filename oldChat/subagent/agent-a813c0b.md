## team-lead at 2026-02-11 08:41:57

*Vote: move What to Report to standalone file*

Vote requested: Should we move the "What to Report" section (lines 65-95 of the Standby Reader Profile) out of the Profile.md and into a standalone file?

The reasoning: Profile.md will be used as the prompt to generate/spawn the reader agent. If "What to Report" (including the per-essay questions, final prompts, and critical experiential checks) is part of that prompt, the reader will see all those questions BEFORE reading — which could bias their experience (e.g., knowing they'll be asked "What happened to your experience across the three examples?" for Essay 3 could prime them to watch for it).

Moving it to a standalone file means we can give the reader the profile (role, personality, reading instructions) at spawn, and then deliver the reporting questions AFTER they finish reading each piece — keeping the reading experience uncontaminated.

Vote YES to move "What to Report" to a standalone file, or NO to keep it in the profile. Brief reasoning please.

---

## Claude at 2026-02-11 08:42:04

[tool: SendMessage]
{
  "type": "message",
  "recipient": "team-lead",
  "content": "**YES** — This is exactly right, and the reasoning is the same principle we applied to the Preface spoiler resolution. If the reader knows in advance they will be asked \"Was there a moment where something clicked or shifted?\" they will be watching for clicks and shifts rather than simply reading. The cat example works precisely because the reader does not know it is coming or what it is supposed to do. Pre-loading the reporting questions would turn the reader from a genuine experiential subject into a self-monitoring observer — which is, in the author's own terms, a different structural position entirely. Deliver the questions after each reading, not before.",
  "summary": "YES — pre-loaded questions would bias the experien
... [truncated]

---

