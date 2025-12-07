# MCP Integration

Termux-CLI supports the Model Context Protocol (MCP) for extended capabilities.

## Enabling MCP

```json
{
  "mcp": {
    "enabled": true,
    "servers": [
      {
        "name": "filesystem",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
      }
    ]
  }
}
```

## Running as MCP Server

Termux-CLI can also run as an MCP server:

```bash
termux-cli --mcp-server
```

## Available MCP Tools

When running as server, these tools are exposed:

- `read_file` - Read file contents
- `write_file` - Write to file
- `run_code` - Execute code
- `shell_exec` - Run shell command
- `search_files` - Search for files
