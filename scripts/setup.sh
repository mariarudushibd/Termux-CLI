#!/bin/bash
# Development setup script

set -e

echo "Setting up Termux-CLI development environment..."

# Create virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

# Install dev dependencies
pip install -e ".[dev]"

echo "Setup complete! Activate with: source venv/bin/activate"
