# Configuration

## Config File

Termux-CLI looks for `.termux-cli.json` in:
1. Current directory
2. Home directory (`~/.termux-cli.json`)

## Example Configuration

```json
{
  "model": {
    "provider": "anthropic",
    "name": "claude-3-sonnet-20240229",
    "temperature": 0.7,
    "max_tokens": 4096
  },
  "agent": {
    "max_iterations": 10,
    "auto_approve": false,
    "safe_mode": true
  },
  "tools": {
    "enabled": ["file_ops", "code_runner", "shell", "search", "git_ops"],
    "shell": {
      "timeout": 60
    }
  },
  "ui": {
    "theme": "default",
    "syntax_highlighting": true
  }
}
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `TERMUX_CLI_CONFIG` | Custom config path |
| `TERMUX_CLI_MODEL` | Default model |
