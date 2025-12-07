#!/bin/bash
# Run tests
set -e
python -m pytest tests/ -v --cov=. --cov-report=term-missing
