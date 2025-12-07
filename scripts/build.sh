#!/bin/bash
# Build distribution packages
set -e
rm -rf dist/ build/ *.egg-info/
python -m build
echo "Build complete! Packages in dist/"
