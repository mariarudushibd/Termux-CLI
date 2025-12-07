# Model Context Protocol (MCP)

Termux-CLI supports MCP for extended capabilities and tool integration.

## What is MCP?

MCP (Model Context Protocol) is a standard for connecting AI agents to external tools and services. It allows Termux-CLI to:

- Access external APIs and services
- Use tools from MCP servers
- Expose its own tools to other agents

## Configuration

Add MCP servers to your config:

```json
{
  "mcp": {
    "enabled": true,
    "servers": [
      {
        "name": "filesystem",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
      },
      {
        "name": "github",
        "command": "npx", 
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "your-token"
        }
      }
    ]
  }
}
```

## Using MCP Tools

Once configured, MCP tools appear automatically:

```
> /mcp
Connected MCP servers:
  - filesystem (3 tools)
  - github (5 tools)

> Use the github tool to list my repos
```

## MCP Slash Commands

MCP servers can expose prompts as slash commands:

```
/mcp__github__list_prs
/mcp__github__pr_review 456
```

## Running as MCP Server

Termux-CLI can run as an MCP server:

```bash
termux-cli --mcp-server
```

Exposed tools:
- `read_file` - Read file contents
- `write_file` - Write to file
- `edit_file` - Edit file content
- `run_code` - Execute code
- `shell_exec` - Run shell command
- `search_files` - Search for files
- `git_status` - Get git status

## Termux MCP Setup

For Termux on Android:

```bash
pkg install nodejs
npm install -g @anthropic-ai/mcp-cli
```
