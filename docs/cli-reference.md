# CLI Reference

## Usage

```bash
termux-cli [OPTIONS] [PROMPT]
```

## Options

| Option | Description |
|--------|-------------|
| `--dir, -d PATH` | Set working directory |
| `--model, -m MODEL` | Specify AI model |
| `--config, -c FILE` | Use custom config file |
| `--verbose, -v` | Enable verbose/debug output |
| `--print, -p` | Print response and exit (non-interactive) |
| `--output-format FORMAT` | Output format: text, json, stream-json |
| `--mcp` | Enable MCP mode |
| `--mcp-server` | Run as MCP server |
| `--resume SESSION_ID` | Resume previous session |
| `--version` | Show version |
| `--help` | Show help |

## Running with Prompt Input

```bash
# Single prompt, print response and exit
termux-cli -p "Explain this codebase"

# Pipe input
echo "Fix the bug in main.py" | termux-cli -p

# From file
termux-cli -p < prompt.txt

# With specific output format
termux-cli --output-format json -p "List all functions"
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `TERMUX_CLI_MODEL` | Default model |
| `TERMUX_CLI_CONFIG` | Config file path |
| `TERMUX_CLI_DEBUG` | Enable debug mode |

## Examples

```bash
# Start interactive session
termux-cli

# Work in specific directory
termux-cli --dir ~/projects/myapp

# Use local Ollama model
termux-cli --model ollama/codellama

# Run with verbose logging
termux-cli -v

# Resume previous session
termux-cli --resume abc123
```
