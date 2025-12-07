# Slash Commands

Slash commands let you control Termux-CLI behavior and execute custom prompts.

## Built-in Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `/exit` | Exit the agent |
| `/compact [focus]` | Compact conversation with optional focus |
| `/config` | Open settings |
| `/cost` | Show token usage statistics |
| `/init` | Initialize project with AGENTS.md |
| `/memory` | Edit memory files |
| `/model [name]` | Select or change AI model |
| `/mcp` | Manage MCP server connections |
| `/permissions` | View or update permissions |
| `/resume` | Resume a conversation |
| `/review` | Request code review |
| `/status` | Show version, model, status |
| `/todos` | List current todo items |
| `/vim` | Enter vim mode |

## Custom Commands

Create custom commands as Markdown files:

### Project Commands

```bash
mkdir -p .termux-cli/commands
echo "Review this code for security issues" > .termux-cli/commands/security.md
```

Use with: `/security`

### User Commands

```bash
mkdir -p ~/.termux-cli/commands
echo "Explain this code simply" > ~/.termux-cli/commands/explain.md
```

## Command Features

### Arguments

```markdown
# .termux-cli/commands/fix-issue.md
Fix issue #$ARGUMENTS following our coding standards
```

Usage: `/fix-issue 123`

### Positional Arguments

```markdown
# .termux-cli/commands/review-pr.md
Review PR #$1 with priority $2 and assign to $3
```

Usage: `/review-pr 456 high alice`

### File References

```markdown
Review the implementation in @src/utils/helpers.py
```

### Bash Execution

```markdown
---
allowed-tools: Bash(git:*)
---

Current status: !`git status`
Create commit for these changes.
```

### Frontmatter Options

```markdown
---
description: Create a git commit
argument-hint: [message]
allowed-tools: Bash(git:*)
model: claude-3-5-haiku
---

Create commit with message: $ARGUMENTS
```
