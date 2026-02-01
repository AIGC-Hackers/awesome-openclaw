# OpenClaw Skills

Skills are modular extensions that add new capabilities to OpenClaw. The official skill repository is **ClawHub**.

## ClawHub

ClawHub is the official skill directory for OpenClaw.

- **Website:** [https://clawhub.com/](https://clawhub.com/)
- **GitHub:** [https://github.com/openclaw/clawhub](https://github.com/openclaw/clawhub)
- **Docs:** [https://docs.openclaw.ai/tools/skills](https://docs.openclaw.ai/tools/skills)

## Installing Skills

Install skills using the clawhub CLI:

```bash
# npm
npx clawhub@latest install <skill-name>

# pnpm
pnpm dlx clawhub@latest install <skill-name>

# bun
bunx clawhub@latest install <skill-name>
```

## Featured Skills

### Communication

| Skill | Description |
|-------|-------------|
| **Slack** | Control Slack - messaging, reactions, pins |
| **WhatsApp CLI** | Send WhatsApp messages via wacli |
| **iMessage** | macOS iMessage integration |
| **Himalaya** | Email via IMAP/SMTP |

### Productivity

| Skill | Description |
|-------|-------------|
| **Apple Notes** | Manage Apple Notes via memo CLI |
| **Apple Reminders** | Manage Apple Reminders via remindctl |
| **Notion** | Notion API integration |
| **Obsidian** | Obsidian vault management |
| **CalDAV Calendar** | Sync CalDAV calendars (iCloud, Google, etc.) |
| **Todozi** | Eisenhower matrix task management |

### Development

| Skill | Description |
|-------|-------------|
| **GitHub** | GitHub CLI (gh) integration |
| **Claude Code** | MCP integration for sub-agents |
| **AI Code Review** | Agent-ready code review |
| **AI Changelog** | Generate changelogs from git |

### Media & Content

| Skill | Description |
|-------|-------------|
| **YouTube Watcher** | Fetch and read video transcripts |
| **Summarize** | Summarize URLs, podcasts, files |
| **Bird** | X/Twitter CLI |
| **Weather** | Weather forecasts |

### Automation

| Skill | Description |
|-------|-------------|
| **Browser Use** | Cloud browser automation |
| **Peekaboo** | macOS UI capture and automation |
| **1Password** | 1Password CLI integration |

## Community Skills

| Resource | Link |
|----------|------|
| Awesome OpenClaw Skills | [GitHub](https://github.com/VoltAgent/awesome-openclaw-skills) |
| OpenClaw Foundry | [GitHub](https://github.com/lekt9/openclaw-foundry) |
| Claude Code Skill | [GitHub](https://github.com/Enderfga/openclaw-claude-code-skill) |

## Creating Your Own Skills

OpenClaw can create its own skills! Ask your agent to build a skill for a specific task.

For creating and publishing skills:
- [Skills Documentation](https://docs.openclaw.ai/tools/skills)
- [Skill Creator Skill](https://clawhub.com/skill/skill-creator)
- [ClawHub Website](https://clawhub.com/)

## Security Warning

⚠️ **Always review skills before installing!**

- Only install skills from trusted sources
- Check the skill's code on GitHub
- Be cautious of skills requesting broad permissions
- See: [Malicious Skill Warning](https://www.reddit.com/r/vibecoding/comments/1qpnybr/found_a_malicious_skill_on_the_frontpage_of/)

---

*Last updated: 2026-02-01*
