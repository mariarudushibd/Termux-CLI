"""Pytest configuration and fixtures"""

import pytest
import tempfile
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)

@pytest.fixture
def sample_files(temp_dir):
    """Create sample files for testing."""
    files = {
        "main.py": "print('Hello, World!')",
        "utils.py": "def helper(): pass",
        "README.md": "# Test Project",
    }
    for name, content in files.items():
        (temp_dir / name).write_text(content)
    return temp_dir

@pytest.fixture
def mock_agent(temp_dir):
    """Create a mock agent for testing."""
    from core.agent import Agent
    return Agent(working_dir=str(temp_dir))
