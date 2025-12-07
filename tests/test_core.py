"""Core module tests"""

import pytest
from pathlib import Path
import tempfile

class TestAgent:
    """Tests for Agent class."""
    
    def test_agent_init(self):
        """Test agent initialization."""
        from core.agent import Agent
        agent = Agent()
        assert agent is not None
    
    def test_agent_with_working_dir(self):
        """Test agent with custom working directory."""
        from core.agent import Agent
        with tempfile.TemporaryDirectory() as tmpdir:
            agent = Agent(working_dir=tmpdir)
            assert agent.working_dir == tmpdir

class TestMemory:
    """Tests for Memory class."""
    
    def test_memory_add(self):
        """Test adding messages to memory."""
        from core.memory import Memory
        memory = Memory()
        memory.add("user", "Hello")
        memory.add("assistant", "Hi there!")
        assert len(memory.messages) == 2
    
    def test_memory_clear(self):
        """Test clearing memory."""
        from core.memory import Memory
        memory = Memory()
        memory.add("user", "Hello")
        memory.clear()
        assert len(memory.messages) == 0

class TestSession:
    """Tests for Session class."""
    
    def test_session_id_generation(self):
        """Test session ID is generated."""
        from core.session import Session
        session = Session()
        assert session.session_id is not None
        assert len(session.session_id) > 0
