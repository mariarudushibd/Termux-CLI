# Termux-CLI 🖥️

A powerful local coding agent that runs from your terminal. Read, modify, and run code on your machine in any chosen directory.

## Features

- 🤖 **AI-Powered Coding Agent** - Intelligent code assistance
- 📁 **File Operations** - Read, write, and modify files
- ⚡ **Code Execution** - Run code in multiple languages
- 🔌 **Plugin System** - Extensible architecture
- 🔗 **MCP Support** - Model Context Protocol integration
- 🏠 **Local First** - Runs entirely on your machine

## Installation

```bash
pip install termux-cli
```

## Quick Start

```bash
# Start the agent in current directory
termux-cli

# Start in a specific directory
termux-cli --dir /path/to/project
```

## Project Structure

```
termux-cli/
├── core/           # Main agent logic
├── plugins/        # Plugin system
├── mcp/            # Model Context Protocol
├── cli/            # Command line interface
├── tools/          # Agent tools
├── models/         # AI model integrations
├── config/         # Configuration
├── utils/          # Utilities
├── prompts/        # Prompt templates
├── tests/          # Test suite
├── docs/           # Documentation
├── examples/       # Examples
└── scripts/        # Setup scripts
```

## License

MIT License
