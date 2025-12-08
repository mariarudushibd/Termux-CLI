<div align="center">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Termux.svg/1280px-Termux.svg.png" alt="Termux Logo" width="150"/>

# Termux-CLI 🖥️

### Lightweight coding agent that runs in your terminal & Termux

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/mariarudushibd/Termux-CLI?style=social)](https://github.com/mariarudushibd/Termux-CLI)

**A powerful local coding agent that can read, modify, and run code on your machine in any chosen directory.**

*Works seamlessly on Linux, macOS, and Android (via Termux)*

[Features](#-features) • [Quick Start](#-quick-start) • [Usage](#-usage) • [Documentation](#-documentation) • [Contributing](#-contributing)

---

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### 🤖 AI-Powered Coding Agent
Intelligent code assistance with Claude, GPT, or local Ollama models

### 📁 File Operations
Read, write, edit, and search files with ease

### ⚡ Code Execution
Run Python, JavaScript, Bash, and more directly

### 🔧 Slash Commands
Built-in and custom commands (`/help`, `/init`, `/review`)

</td>
<td width="50%">

### 🧠 Memory System
Persistent context with `AGENTS.md` files

### 🔌 Plugin Architecture
Extend functionality with custom plugins

### 🔗 MCP Support
Model Context Protocol integration

### 📱 Termux Compatible
Full support for Android terminal

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Installation

```bash
# Using pip
pip install termux-cli

# Or from source
git clone https://github.com/mariarudushibd/Termux-CLI.git
cd Termux-CLI
pip install -e .
```

### 📱 Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python git
pip install termux-cli
```

### 🔑 Set API Key

```bash
export ANTHROPIC_API_KEY="your-key-here"
# Or use local Ollama (no key needed)
```

### ▶️ Run

```bash
# Interactive mode
termux-cli

# With specific directory
termux-cli --dir /path/to/project

# Single prompt
termux-cli -p "Explain this codebase"
```

---

## 📖 Usage

### 💬 Interactive Session

```
$ termux-cli

==========================================
  Termux-CLI - Local Coding Agent
  Working directory: /home/user/project
  Type /help for commands
==========================================

> Show me the project structure

I'll list the files in your project:
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
├── README.md
└── setup.py

> Create a function to parse JSON files

I'll add a JSON parsing function to utils.py...
```

### ⚡ Slash Commands

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/init` | Initialize project with AGENTS.md |
| `/memory` | Edit memory files |
| `/model [name]` | Change AI model |
| `/clear` | Clear conversation |
| `/review` | Request code review |
| `/exit` | Exit the agent |

### 🎯 Custom Commands

Create reusable prompts:

```bash
# Project command
mkdir -p .termux-cli/commands
echo "Review this code for security issues" > .termux-cli/commands/security.md

# Use it
> /security
```

### 🧠 Memory with AGENTS.md

Create an `AGENTS.md` file to give the agent persistent context:

```markdown
# Project Instructions

## Code Style
- Use type hints
- Add docstrings to functions

## Commands
- Build: `npm run build`
- Test: `pytest tests/`

## Architecture
@docs/architecture.md
```

---

## 🏗️ Project Structure

```
termux-cli/
├── core/           # Main agent logic
│   ├── agent.py    # Agent orchestration
│   ├── executor.py # Code execution
│   ├── memory.py   # AGENTS.md memory system
│   └── session.py  # Session management
├── cli/            # Command line interface
│   ├── main.py     # Entry point
│   ├── repl.py     # Interactive REPL
│   ├── slash_commands.py  # Command system
│   └── ui.py       # Terminal UI
├── tools/          # Agent capabilities
│   ├── file_ops.py # File operations
│   ├── code_runner.py  # Code execution
│   ├── shell.py    # Shell commands
│   ├── search.py   # File search
│   └── git_ops.py  # Git integration
├── models/         # AI integrations
│   ├── anthropic.py  # Claude
│   ├── openai.py     # GPT
│   └── ollama.py     # Local models
├── plugins/        # Plugin system
├── mcp/            # MCP protocol
├── config/         # Configuration
├── prompts/        # Prompt templates
└── docs/           # Documentation
```

---

## 🔧 Configuration

Create `.termux-cli.json` in your project or home directory:

```json
{
  "model": {
    "provider": "anthropic",
    "name": "claude-3-sonnet-20240229"
  },
  "agent": {
    "max_iterations": 10,
    "safe_mode": true
  },
  "tools": {
    "enabled": ["file_ops", "code_runner", "shell", "search", "git_ops"]
  }
}
```

---

## 🔌 MCP Integration

Connect to MCP servers for extended capabilities:

```json
{
  "mcp": {
    "enabled": true,
    "servers": [
      {
        "name": "github",
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    ]
  }
}
```

---

## 📚 Documentation

<table>
<tr>
<td>

- 📦 [Installation Guide](docs/installation.md)
- 📖 [Usage Guide](docs/usage.md)
- 🛠️ [CLI Reference](docs/cli-reference.md)
- ⚡ [Slash Commands](docs/slash-commands.md)

</td>
<td>

- 🧠 [Memory Management](docs/memory.md)
- 🔗 [MCP Integration](docs/mcp.md)
- 📱 [Termux Setup](docs/termux-setup.md)
- 🔌 [Plugin Development](docs/plugins.md)

</td>
</tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Setup development environment
git clone https://github.com/mariarudushibd/Termux-CLI.git
cd Termux-CLI
./scripts/setup.sh

# Run tests
./scripts/test.sh
```

### 🌟 Contributors

Thanks to all our contributors!

<a href="https://github.com/mariarudushibd/Termux-CLI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=mariarudushibd/Termux-CLI" />
</a>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Inspired by:
- **[Claude Code](https://claude.ai/code)** - Anthropic's coding agent
- **[Termux](https://termux.dev/)** - Android terminal emulator
- **[XFCE Terminal](https://gitlab.xfce.org/apps/xfce4-terminal)** - Terminal architecture reference

---

<div align="center">

### Made with ❤️ for developers who code everywhere

**[⭐ Star us on GitHub](https://github.com/mariarudushibd/Termux-CLI)** | **[🐛 Report Bug](https://github.com/mariarudushibd/Termux-CLI/issues)** | **[✨ Request Feature](https://github.com/mariarudushibd/Termux-CLI/issues)**

</div>
