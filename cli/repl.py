"""REPL - Interactive read-eval-print loop"""

from pathlib import Path
from typing import Optional

class REPL:
    """Interactive REPL for the coding agent."""
    
    def __init__(self, working_dir: str = ".", model: str = None):
        self.working_dir = Path(working_dir).resolve()
        self.model = model
        self.running = False
        self.history = []
    
    def run(self):
        """Start the REPL loop."""
        self.running = True
        self._print_welcome()
        
        while self.running:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue
                
                if user_input.startswith('/'):
                    self._handle_command(user_input)
                else:
                    self._process_input(user_input)
                    
            except KeyboardInterrupt:
                print("\nUse /exit to quit.")
            except EOFError:
                break
    
    def _print_welcome(self):
        """Print welcome message."""
        print("="*50)
        print("  Termux-CLI - Local Coding Agent")
        print(f"  Working directory: {self.working_dir}")
        print("  Type /help for commands")
        print("="*50)
    
    def _handle_command(self, cmd: str):
        """Handle slash commands."""
        from .commands import CommandRegistry
        command = CommandRegistry.get(cmd.split()[0])
        if command:
            command.execute()
        else:
            print(f"Unknown command: {cmd}")
    
    def _process_input(self, user_input: str):
        """Process user input through the agent."""
        self.history.append(user_input)
        # Agent processing logic here
        print("Processing...")
