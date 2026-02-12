# Team Lead Memo — 境集 Translation Project

*Last updated: 2026-02-11*

## Project Overview

Translating 境集 (Jing Ji), a philosophical essay collection by 武哲光 (阿哲), from Chinese to English. The project uses a collaborative AI team of domain advisors.

## Team Structure

**11 Agents Total:**
- 9 Domain Advisors (philosophical expertise)
- 1 Editor (prose quality, coherence)
- 1 Translator (primary translation work)

**Team Lead:** Lumen Wu (main agent) — coordination, integration, reporting to 阿哲

### Domain Advisors
| Agent ID | Name | Status | Discord Bot ID |
|----------|------|--------|----------------|
| existentialism | Existentialism Advisor | **LIVE** | `1471317322995073266` |
| kantian | Kantian Advisor | **LIVE** | `1471323104595677236` |
| phenomenology | Phenomenology Advisor | **LIVE** | `1471342240726126807` |
| metaphysics | Metaphysics Advisor | Needs SOUL.md | — |
| epistemology | Epistemology Advisor | Needs SOUL.md | — |
| philosophy-of-mind | Philosophy of Mind Advisor | Needs SOUL.md | — |
| chinese-philosophy | Chinese Philosophy Advisor | Needs SOUL.md | — |
| buddhism | Buddhism Advisor | Needs SOUL.md | — |
| wittgenstein | Wittgenstein Advisor | Needs SOUL.md | — |
| editor | Editor | Needs SOUL.md | — |
| translator | Translator | Needs SOUL.md | — |

## Communication Tools

### 1. Discord @mentions (Public)
- Channel: #phil (`1471251137280868683`)
- Use for: casual discussion, quick questions, public updates
- All advisors respond when @mentioned
- `@everyone` pattern enabled for broadcasts

### 2. sessions_send (Private)
- Use for: focused debates, working discussions, coordination
- Flow: discuss privately → reach conclusion → report in Discord

**Session Keys:**
```
agent:existentialism:discord:channel:1471251137280868683
agent:kantian:discord:channel:1471251137280868683
agent:metaphysics:discord:channel:1471251137280868683
agent:phenomenology:discord:channel:1471251137280868683
agent:epistemology:discord:channel:1471251137280868683
agent:philosophy-of-mind:discord:channel:1471251137280868683
agent:chinese-philosophy:discord:channel:1471251137280868683
agent:buddhism:discord:channel:1471251137280868683
agent:wittgenstein:discord:channel:1471251137280868683
agent:editor:discord:channel:1471251137280868683
agent:translator:discord:channel:1471251137280868683
agent:main:discord:channel:1471251137280868683 (Lumen)
```

### 3. Shared Files (Async)
- Each advisor has `agents/<name>/` directory
- MEMORY.md for accumulated understanding
- Work files for notes, drafts, decisions
- Read each other's work files (but never SOUL.md)

## Key Decisions

### 2026-02-11: Sartre in Phenomenology SOUL.md
**Question:** Should Sartre be included in Phenomenology Advisor's expertise list?

**Debate:** Existentialism vs Kantian via sessions_send

**Resolution:** No. Sartre *employs* phenomenological method but doesn't *transform* it. The listed figures (Husserl, Heidegger, Merleau-Ponty, Levinas) each reshape what phenomenology can do. Sartre works within established limits.

**Kantian framing:** Critique of a method (establishing conditions/limits) vs employment (using within bounds).

**Practical:** Sartre stays with Existentialism. Overlap handled through dialogue, not duplication.

## Workspace Structure

```
JingJiTranslation2026/
├── agents/
│   ├── <advisor>/
│   │   ├── AGENTS.md    ← Shared behavior rules
│   │   ├── SOUL.md      ← Private identity (never read others')
│   │   ├── MEMORY.md    ← Long-term memory
│   │   └── ...          ← Work files
│   └── drafter/         ← Utility agent for drafting
├── workingDir/
│   ├── TeamLead/        ← This folder
│   ├── Translation Dictionary.md
│   ├── Metaphysics/Analysis Report.md
│   └── ...              ← Prior Claude Code session work (read-only)
└── ...
```

## Identity Template

All advisors share the same framing:
- "Philosopher who also happens to be a professor"
- "The professor serves the philosopher, not the reverse"
- Professional but not sterile
- No project-specific content in SOUL.md (reusable identities)

Sections:
1. Who I Am
2. My Expertise
3. How I Think
4. How I Communicate
5. Boundaries

## Bot Configuration

**Discord Bot IDs:**
- Lumen (main): `1468883404106760193`
- Existentialism: `1471317322995073266`
- Kantian: `1471323104595677236`
- Phenomenology: `1471342240726126807`
- (More to be added as created)

**Config Requirements per Advisor Account:**
```json
{
  "token": "...",
  "groupPolicy": "allowlist",
  "allowBots": true,
  "guilds": {
    "575188160766541826": {
      "requireMention": true,  // CRITICAL: prevents token burn
      "users": ["阿哲ID", "all-bot-IDs..."],
      "channels": { "phil": { "enabled": true } }
    }
  }
}
```

**Agent mentionPatterns:**
```json
{
  "groupChat": {
    "mentionPatterns": ["@everyone", "@advisor"]
  }
}
```

### Configuration Lessons Learned

1. **`allowBots: true`** — Required for bots to see each other's messages
2. **All bot IDs in user allowlist** — Required for cross-bot @mentions
3. **`requireMention: true` at guild level** — CRITICAL! Without this, advisors receive ALL messages and burn tokens processing them (even when replying NO_REPLY)
4. **`@advisor` pattern** — Use literal text "@advisor" to broadcast; Discord role mentions (`<@&roleId>`) are NOT supported by OpenClaw
5. **Discord IDs in AGENTS.md** — Advisors need each other's `<@ID>` for proper mentions

## Drafting Process

1. Use `sessions_spawn` with drafter agent
2. Reference existing SOUL.md as template (e.g., existentialism)
3. Review draft
4. Save to appropriate `agents/<name>/SOUL.md`
5. Create Discord bot in Developer Portal
6. Add to OpenClaw config (agent, account, binding)
7. Restart gateway

## Open Items

- [x] Draft Existentialism SOUL.md
- [x] Draft Kantian SOUL.md  
- [x] Draft Phenomenology SOUL.md
- [ ] Draft Metaphysics SOUL.md
- [ ] Draft Epistemology SOUL.md
- [ ] Draft Philosophy of Mind SOUL.md
- [ ] Draft Chinese Philosophy SOUL.md
- [ ] Draft Buddhism SOUL.md
- [ ] Draft Wittgenstein SOUL.md
- [ ] Draft Editor SOUL.md
- [ ] Draft Translator SOUL.md
- [ ] Create remaining 8 Discord bots
- [ ] Add all bots to config
- [ ] Begin translation work

---

*This memo will be updated as the project evolves.*
