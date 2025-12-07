"""Tests for AGENTS.md memory system"""

import pytest
import tempfile
from pathlib import Path

class TestAgentMemory:
    """Tests for AgentMemory class."""
    
    def test_init_empty_dir(self, temp_dir):
        """Test memory init in empty directory."""
        from core.memory import AgentMemory
        memory = AgentMemory(str(temp_dir))
        assert memory is not None
        assert len(memory.memory_files) == 0
    
    def test_load_project_memory(self, temp_dir):
        """Test loading AGENTS.md from project."""
        from core.memory import AgentMemory
        
        # Create AGENTS.md
        agents_md = temp_dir / "AGENTS.md"
        agents_md.write_text("# Project Instructions\n- Use type hints")
        
        memory = AgentMemory(str(temp_dir))
        assert len(memory.memory_files) == 1
        assert "type hints" in memory.get_system_prompt()
    
    def test_import_files(self, temp_dir):
        """Test @import functionality."""
        from core.memory import AgentMemory
        
        # Create files
        (temp_dir / "style.md").write_text("Use 2-space indentation")
        (temp_dir / "AGENTS.md").write_text("# Instructions\n@style.md")
        
        memory = AgentMemory(str(temp_dir))
        prompt = memory.get_system_prompt()
        assert "2-space indentation" in prompt
    
    def test_init_project_memory(self, temp_dir):
        """Test initializing new AGENTS.md."""
        from core.memory import AgentMemory
        
        memory = AgentMemory(str(temp_dir))
        path = memory.init_project_memory()
        
        assert path.exists()
        assert "Project Instructions" in path.read_text()
    
    def test_add_memory(self, temp_dir):
        """Test adding memory entries."""
        from core.memory import AgentMemory
        
        # Create initial AGENTS.md
        (temp_dir / "AGENTS.md").write_text("# Instructions")
        
        memory = AgentMemory(str(temp_dir))
        memory.add_memory("Always use descriptive names")
        
        content = (temp_dir / "AGENTS.md").read_text()
        assert "descriptive names" in content

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
