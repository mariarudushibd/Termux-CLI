"""Tests for slash command system"""

import pytest
import tempfile
from pathlib import Path

class TestSlashCommands:
    """Tests for SlashCommandRegistry."""
    
    def test_builtin_commands(self, temp_dir):
        """Test built-in commands are registered."""
        from cli.slash_commands import SlashCommandRegistry
        
        registry = SlashCommandRegistry(str(temp_dir))
        commands = registry.list_commands()
        
        names = [c.name for c in commands]
        assert "/help" in names
        assert "/clear" in names
        assert "/exit" in names
        assert "/init" in names
    
    def test_help_command(self, temp_dir):
        """Test /help output."""
        from cli.slash_commands import SlashCommandRegistry
        
        registry = SlashCommandRegistry(str(temp_dir))
        result = registry.execute("/help")
        
        assert "Available commands" in result
        assert "/help" in result
    
    def test_custom_command(self, temp_dir):
        """Test loading custom command from file."""
        from cli.slash_commands import SlashCommandRegistry
        
        # Create custom command
        cmd_dir = temp_dir / ".termux-cli" / "commands"
        cmd_dir.mkdir(parents=True)
        (cmd_dir / "review.md").write_text("Review this code for bugs")
        
        registry = SlashCommandRegistry(str(temp_dir))
        
        assert "/review" in [c.name for c in registry.list_commands()]
    
    def test_arguments_replacement(self, temp_dir):
        """Test $ARGUMENTS replacement."""
        from cli.slash_commands import SlashCommandRegistry
        
        cmd_dir = temp_dir / ".termux-cli" / "commands"
        cmd_dir.mkdir(parents=True)
        (cmd_dir / "fix.md").write_text("Fix issue #$ARGUMENTS")
        
        registry = SlashCommandRegistry(str(temp_dir))
        result = registry.execute("/fix 123")
        
        assert "Fix issue #123" in result
    
    def test_positional_args(self, temp_dir):
        """Test $1, $2 positional arguments."""
        from cli.slash_commands import SlashCommandRegistry
        
        cmd_dir = temp_dir / ".termux-cli" / "commands"
        cmd_dir.mkdir(parents=True)
        (cmd_dir / "pr.md").write_text("Review PR #$1 by $2")
        
        registry = SlashCommandRegistry(str(temp_dir))
        result = registry.execute("/pr 456 alice")
        
        assert "PR #456" in result
        assert "alice" in result

@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)
