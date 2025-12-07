# Installation Guide

## Requirements

- Python 3.8+
- pip or uv package manager

## Installation Methods

### Using pip

```bash
pip install termux-cli
```

### Using uv (recommended)

```bash
uv pip install termux-cli
```

### From source

```bash
git clone https://github.com/mariarudushibd/Termux-CLI.git
cd Termux-CLI
pip install -e .
```

## Termux Installation

For Android Termux:

```bash
pkg update && pkg upgrade
pkg install python
pip install termux-cli
```

## API Keys

Set your API key for the AI provider:

```bash
# For Anthropic Claude
export ANTHROPIC_API_KEY="your-key-here"

# For OpenAI
export OPENAI_API_KEY="your-key-here"

# Or use local Ollama (no key needed)
termux-cli --model ollama/llama2
```

## Verify Installation

```bash
termux-cli --version
termux-cli --help
```
