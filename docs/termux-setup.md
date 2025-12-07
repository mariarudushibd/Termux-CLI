# Termux Setup Guide

Complete guide for setting up Termux-CLI on Android using Termux.

## Prerequisites

1. **Install Termux** from [F-Droid](https://f-droid.org/packages/com.termux/) (not Play Store)
2. **Grant storage access**: `termux-setup-storage`

## Installation

### 1. Update Packages

```bash
pkg update && pkg upgrade -y
```

### 2. Install Required Packages

```bash
# Python and essential tools
pkg install python python-pip git -y

# Build tools (for some packages)
pkg install clang libffi openssl -y

# Optional: Node.js for MCP servers
pkg install nodejs -y

# Optional: Better terminal experience
pkg install tmux neovim -y
```

### 3. Install Termux-CLI

```bash
# Using pip
pip install termux-cli

# Or from source
git clone https://github.com/mariarudushibd/Termux-CLI.git
cd Termux-CLI
pip install -e .
```

### 4. Configure API Key

```bash
# Add to ~/.bashrc or ~/.zshrc
export ANTHROPIC_API_KEY="your-key-here"

# Or use local Ollama (no API key needed)
termux-cli --model ollama/llama2
```

## Running Ollama on Termux

```bash
# Install Ollama (requires proot-distro)
pkg install proot-distro
proot-distro install ubuntu
proot-distro login ubuntu

# Inside Ubuntu
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &
ollama pull codellama
```

## Recommended Packages

| Package | Purpose |
|---------|----------|
| `python` | Python runtime |
| `git` | Version control |
| `nodejs` | MCP servers, JS execution |
| `clang` | C/C++ compiler |
| `rust` | Rust development |
| `golang` | Go development |
| `tmux` | Terminal multiplexer |
| `neovim` | Text editor |
| `openssh` | SSH access |
| `termux-api` | Android API access |

## Tips

### Use External Keyboard

Termux works best with a physical keyboard. Enable extra keys row:

```bash
mkdir -p ~/.termux
echo "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]" > ~/.termux/termux.properties
```

### Access Phone Storage

```bash
termux-setup-storage
cd ~/storage/shared
```

### Keep Session Alive

```bash
termux-wake-lock
```

### Run in Background

Use `tmux` to keep sessions running:

```bash
tmux new -s agent
termux-cli
# Ctrl+B, D to detach
# tmux attach -t agent to reconnect
```
