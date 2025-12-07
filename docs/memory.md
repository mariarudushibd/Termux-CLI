# Memory Management with AGENTS.md

Termux-CLI uses a hierarchical memory system to maintain context across sessions.

## Memory Hierarchy

| Level | Location | Purpose | Shared With |
|-------|----------|---------|-------------|
| Enterprise | `/etc/termux-cli/AGENTS.md` | Organization policies | All users |
| User | `~/.termux-cli/AGENTS.md` | Personal preferences | All your projects |
| Project | `./AGENTS.md` | Team instructions | Team via git |
| Local | `./AGENTS.local.md` | Private preferences | Just you |

## Quick Start

### Initialize Project Memory

```bash
termux-cli
> /init
```

This creates `AGENTS.md` with a starter template.

### Add Memories

Start input with `#` to add a memory:

```
> # Always use type hints in Python code
Memory added to project.
```

### Edit Memories

```
> /memory
```

Opens AGENTS.md in your editor.

## AGENTS.md Format

```markdown
# Project Instructions

## Overview
@README.md

## Code Style
- Use 2-space indentation
- Prefer const over let in JavaScript
- Always add docstrings

## Commands
- Build: `npm run build`
- Test: `npm test`
- Deploy: `./scripts/deploy.sh`

## Architecture
- Frontend: React + TypeScript
- Backend: Python FastAPI
- Database: PostgreSQL
```

## Import System

Use `@path` to import other files:

```markdown
# Main Instructions
@README.md
@docs/architecture.md
@~/.termux-cli/personal-style.md
```

- Relative paths are from AGENTS.md location
- `~` expands to home directory
- Maximum 5 levels of nested imports

## Best Practices

1. **Be specific**: "Use 2-space indentation" not "Format code properly"
2. **Use structure**: Group related instructions under headings
3. **Keep updated**: Review as project evolves
4. **Use imports**: Keep AGENTS.md clean, details in linked files
