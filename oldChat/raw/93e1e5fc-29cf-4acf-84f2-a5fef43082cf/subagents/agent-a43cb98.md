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
  "content": "**YES** — This is the same logic we applied to the Preface spoilers. If the reader knows in advance they'll be asked about \"what happened to your experience across the three examples\" in Essay 3, they'll watch for it rather than experiencing it naturally. The whole point of a standby reader is to test whether the experiential sequences work on an unprimed mind. Delivering the reporting questions after each reading preserves the integrity of the test. The profile should contain only role, personality, and the instruction to read in prescribed order — everything else comes after.",
  "summary": "YES: same spoiler logic applies to reader prompts"
}

---

## Claude at 2026-02-11 08:42:07

Voted YES. Same spoiler-protection principle: unprimed experience first, structured reporting after. Awaiting next task.

---

