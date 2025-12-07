"""Code executor - Runs code safely in chosen directory"""

import subprocess
from pathlib import Path

class Executor:
    """Executes code safely in sandboxed environment."""
    
    def __init__(self, working_dir: str):
        self.working_dir = Path(working_dir)
    
    def run_python(self, code: str):
        """Execute Python code."""
        pass
    
    def run_shell(self, command: str):
        """Execute shell command."""
        pass
    
    def run_file(self, filepath: str):
        """Execute a file based on its extension."""
        pass
