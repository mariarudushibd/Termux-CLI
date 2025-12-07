# Installation Guide

## Requirements

- Python 3.8 or higher
- pip or uv package manager

## Installation Methods

### Using pip (Recommended)

```bash
pip install termux-cli
```

### Using uv

```bash
uv pip install termux-cli
```

### From Source

```bash
git clone https://github.com/mariarudushibd/Termux-CLI.git
cd Termux-CLI
pip install -e .
```

### Development Installation

```bash
git clone https://github.com/mariarudushibd/Termux-CLI.git
cd Termux-CLI
pip install -e ".[dev]"
```

## Platform-Specific Instructions

### Linux

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install python3 python3-pip git
pip install termux-cli
```

### macOS

```bash
# Using Homebrew
brew install python3
pip3 install termux-cli
```

### Termux (Android)

```bash
pkg update && pkg upgrade
pkg install python git
pip install termux-cli

# Optional: for MCP servers
pkg install nodejs
```

### Windows

```bash
# Install Python from python.org
pip install termux-cli
```

## API Keys Setup

### Anthropic (Claude)

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### OpenAI (GPT)

```bash
export OPENAI_API_KEY="sk-..."
```

### Local Models (Ollama)

No API key needed. Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull codellama
termux-cli --model ollama/codellama
```

## Verify Installation

```bash
termux-cli --version
termux-cli --help

# Test with a simple prompt
termux-cli -p "Hello, what can you do?"
```

## Troubleshooting

### Python Version

```bash
python3 --version  # Should be 3.8+
```

### Missing Dependencies

```bash
pip install --upgrade pip
pip install termux-cli --force-reinstall
```

### Permission Issues

```bash
pip install --user termux-cli
```
