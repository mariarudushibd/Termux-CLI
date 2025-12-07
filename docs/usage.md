# Usage Guide

## Starting the Agent

```bash
# Start in current directory
termux-cli

# Start in specific directory
termux-cli --dir /path/to/project

# Use specific model
termux-cli --model claude-3-sonnet
termux-cli --model gpt-4
termux-cli --model ollama/codellama
```

## Interactive Commands

Once running, use these commands:

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear conversation history |
| `/exit` | Exit the agent |
| `/model <name>` | Switch AI model |
| `/dir <path>` | Change working directory |

## Example Session

```
> Show me the project structure

I'll list the files in your project:

├── src/
│   ├── main.py
│   └── utils.py
├── tests/
├── README.md
└── setup.py

> Create a new function to parse JSON files

I'll add a JSON parsing function to utils.py...
```

## Tips

1. Be specific about file paths
2. Review changes before confirming
3. Use `/clear` to reset context for new tasks
