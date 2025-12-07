# Termux-CLI Project Instructions

## Overview

Termux-CLI is a lightweight coding agent that runs in your terminal and Termux (Android). It can read, modify, and run code on your machine in any chosen directory.

## Project Structure

- `core/` - Main agent logic and orchestration
- `cli/` - Command line interface and REPL
- `tools/` - File ops, code runner, shell, search, git
- `models/` - AI model integrations (OpenAI, Anthropic, Ollama)
- `plugins/` - Extensible plugin system
- `mcp/` - Model Context Protocol implementation
- `config/` - Configuration management
- `prompts/` - System and user prompts
- `utils/` - Utility functions

## Code Style

- Python 3.8+ compatible
- Use type hints for all function signatures
- Add docstrings to all public classes and functions
- Follow PEP 8 (enforced by ruff)
- Maximum line length: 100 characters

## Commands

- **Install**: `pip install -e .`
- **Test**: `pytest tests/ -v`
- **Lint**: `ruff check .`
- **Format**: `black .`
- **Build**: `python -m build`

## Key Features

- Slash commands system (`/help`, `/init`, `/memory`)
- AGENTS.md memory management
- MCP protocol support
- Multi-model support (Claude, GPT, Ollama)
- Plugin architecture
- Termux/Android compatibility

## Development Notes

- Keep dependencies minimal for Termux compatibility
- Test on both Linux and Termux environments
- Maintain backward compatibility with Python 3.8
