## team-lead at 2026-02-11 00:05:25

*Add classical Chinese quotation format to your Memo*

Please add the following convention to your Memo.md under a new section (e.g., "Classical Chinese Quotation Format"):

**Format for 文言 (classical Chinese) quotations:**

1. Present original 文言 text as a **block quote**
2. Follow with **glossed English translation** — key terms glossed on first occurrence as "English (漢字, pinyin)", e.g., "humaneness (仁, ren)"
3. After first introduction, use **plain English only** — e.g., just "humaneness"
4. **现象X compounds** (现象仁, 现象礼, 现象义) keep the "phenomenal" prefix **always** — never drop it. The distinction between "humaneness" (classical concept) and "phenomenal humaneness" (author's coinage for lived experience) is load-bearing for the argument.

**Refinements:**
- Re-gloss briefly at **register transitions** — when the same term (e.g., 仁) shifts from classical quotation to the author's modern analysis, add a brief "(仁)" reminder
- Only gloss **philosophically load-bearing terms**, not every content word
- For the author's coined compounds (现象仁 etc.), no romanization needed after first gloss — "phenomenal humaneness" is self-explanatory
- Make the 文言/modern Chinese boundary visible through **formatting** (block-indent for classical quotations vs. running text for the author's analysis)

This was unanimously endorsed by all 9 experts.

---

## Claude at 2026-02-11 00:05:28

[tool: Read]
{
  "file_path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "offset": 240
}

---

## Claude at 2026-02-11 00:05:33

Now I can see the full Memo. I need to add the classical Chinese quotation format convention. I'll add it after the Register Strategy section (section 3) since it directly relates to register handling, or as a new subsection. Looking at the structure, it fits best as a new section after the Register Strategy.

[tool: Edit]
{
  "replace_all": false,
  "file_path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "old_string": "### 4. Structural Principles",
  "new_string": "### 4. Classical Chinese Quotation Format\n\n**Format for 文言 (classical Chinese) quotations:**\n\n1. Present original 文言 text as a **block quote**\n2. Follow with **glossed English translation** — key terms glossed on first occurrence as \"English (漢字, pinyin)\", e.g., \"humaneness (仁, ren)\"\n3. After first introduction, use **plain English only** — e.g., just \"humaneness\"\n4. **现象X compounds** (现象仁, 现象礼, 现象义) keep the \"phenomenal\" prefix **always** — never drop it. The distinction between \"humaneness\" (classical concept) and \"phenomenal humaneness\" (author's coinage for lived experien
... [truncated]

---

## Claude at 2026-02-11 00:05:54

Now I need to renumber the subsequent sections (5, 6 become 6, 7).

[tool: Edit]
{
  "replace_all": false,
  "file_path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "old_string": "### 5. Structural Principles",
  "new_string": "### 5. Structural Principles"
}

---

## Claude at 2026-02-11 00:05:59

The numbering is already correct since I inserted section 4 and the old section 4 became section 5. Let me verify the subsequent sections need renumbering.

[tool: Grep]
{
  "pattern": "^### \\d+\\.",
  "path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "output_mode": "content",
  "-n": true
}

---

## Claude at 2026-02-11 00:06:05

There are two section 5s. I need to fix the numbering.

[tool: Edit]
{
  "replace_all": false,
  "file_path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "old_string": "### 5. Translator's Apparatus (Planned)",
  "new_string": "### 6. Translator's Apparatus (Planned)"
}

---

## Claude at 2026-02-11 00:08:09

[tool: Edit]
{
  "replace_all": false,
  "file_path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "old_string": "### 6. Expert Consultation Results (All Resolved)",
  "new_string": "### 7. Expert Consultation Results (All Resolved)"
}

---

## Claude at 2026-02-11 00:08:14

Now let me confirm the numbering is correct.

[tool: Grep]
{
  "pattern": "^### \\d+\\.",
  "path": "/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md",
  "output_mode": "content",
  "-n": true
}

---

## Claude at 2026-02-11 00:08:18

Numbering is now correct: 1 through 7 in sequence.

[tool: SendMessage]
{
  "type": "message",
  "recipient": "team-lead",
  "content": "Done. Added the classical Chinese quotation format as section 4 in the Memo.md (under \"Overall Translation Approach\"), with all four points and four refinements as specified. Renumbered subsequent sections (Structural Principles is now 5, Translator's Apparatus is 6, Expert Consultation Results is 7).\n\nFile: `/Users/el/Dropbox/10.Kernel/11.Vault/Tower/L. Legenravend/49 Workspace/Translator/Memo.md`, line 404.",
  "summary": "Added classical Chinese quotation format to Memo.md as section 4"
}

---

