#!/bin/bash
# Installation script for Termux-CLI
# Supports: Linux, macOS, Termux (Android)

set -e

echo "========================================"
echo "  Termux-CLI Installation Script"
echo "========================================"

# Detect platform
if [ -d "$PREFIX" ] && [ -f "$PREFIX/bin/pkg" ]; then
    echo "Platform: Termux (Android)"
    PLATFORM="termux"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Platform: Linux"
    PLATFORM="linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Platform: macOS"
    PLATFORM="macos"
else
    echo "Platform: Unknown ($OSTYPE)"
    PLATFORM="unknown"
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Python 3 not found. Installing..."
    if [ "$PLATFORM" == "termux" ]; then
        pkg install python -y
    elif [ "$PLATFORM" == "linux" ]; then
        sudo apt-get update && sudo apt-get install python3 python3-pip -y
    elif [ "$PLATFORM" == "macos" ]; then
        brew install python3
    fi
fi

PYTHON_VERSION=$(python3 --version 2>&1)
echo "Python: $PYTHON_VERSION"

# Install using uv or pip
if command -v uv &> /dev/null; then
    echo "Installing with uv..."
    uv pip install -e .
elif command -v pip3 &> /dev/null; then
    echo "Installing with pip..."
    pip3 install -e .
else
    echo "Error: No package manager found"
    exit 1
fi

echo ""
echo "Installation complete!"
echo "Run 'termux-cli --help' to get started."
