"""CLI commands - Available terminal commands"""

from typing import Callable, Dict

class Command:
    """Represents a CLI command."""
    
    def __init__(self, name: str, handler: Callable, description: str = ""):
        self.name = name
        self.handler = handler
        self.description = description
    
    def execute(self, *args, **kwargs):
        return self.handler(*args, **kwargs)

class CommandRegistry:
    """Registry of available commands."""
    
    commands: Dict[str, Command] = {}
    
    @classmethod
    def register(cls, name: str, description: str = ""):
        """Decorator to register a command."""
        def decorator(func: Callable):
            cls.commands[name] = Command(name, func, description)
            return func
        return decorator
    
    @classmethod
    def get(cls, name: str) -> Command:
        return cls.commands.get(name)
    
    @classmethod
    def list_all(cls) -> Dict[str, Command]:
        return cls.commands

# Built-in commands
@CommandRegistry.register('/help', 'Show available commands')
def cmd_help():
    """Show help message."""
    print("Available commands:")
    for name, cmd in CommandRegistry.list_all().items():
        print(f"  {name}: {cmd.description}")

@CommandRegistry.register('/clear', 'Clear conversation history')
def cmd_clear():
    """Clear conversation."""
    print("Conversation cleared.")

@CommandRegistry.register('/exit', 'Exit the agent')
def cmd_exit():
    """Exit the agent."""
    print("Goodbye!")
    exit(0)
