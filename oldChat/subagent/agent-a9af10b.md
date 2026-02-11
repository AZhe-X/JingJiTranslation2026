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
  "content": "YES — This is the exact same logic we applied to the Preface spoilers. If we spent an entire deliberation cycle protecting the Essay 3 punchline from the general reader, we should not then hand the standby reader a prompt that says \"report whether the final example produced a different response than the first two.\" That primes the very recognition the sequence is designed to produce organically. The reporting questions should be delivered post-reading, not pre-reading. The profile should contain only: who you are, how to read, and the general instruction \"pay attention to your experience as you read.\"",
  "summary": "YES — same logic as Preface spoilers, deliver questions post-reading"
}

---

