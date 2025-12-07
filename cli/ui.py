"""Terminal UI - Rich terminal interface components"""

from typing import List, Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.syntax import Syntax
    from rich.markdown import Markdown
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

class TerminalUI:
    """Rich terminal UI components."""
    
    def __init__(self):
        if HAS_RICH:
            self.console = Console()
        else:
            self.console = None
    
    def print_code(self, code: str, language: str = "python"):
        """Print syntax-highlighted code."""
        if HAS_RICH:
            syntax = Syntax(code, language, theme="monokai", line_numbers=True)
            self.console.print(syntax)
        else:
            print(code)
    
    def print_markdown(self, text: str):
        """Print formatted markdown."""
        if HAS_RICH:
            md = Markdown(text)
            self.console.print(md)
        else:
            print(text)
    
    def print_panel(self, content: str, title: str = ""):
        """Print content in a panel."""
        if HAS_RICH:
            panel = Panel(content, title=title)
            self.console.print(panel)
        else:
            print(f"--- {title} ---")
            print(content)
            print("-" * 20)
    
    def print_error(self, message: str):
        """Print error message."""
        if HAS_RICH:
            self.console.print(f"[red]Error:[/red] {message}")
        else:
            print(f"Error: {message}")
    
    def print_success(self, message: str):
        """Print success message."""
        if HAS_RICH:
            self.console.print(f"[green]Success:[/green] {message}")
        else:
            print(f"Success: {message}")
