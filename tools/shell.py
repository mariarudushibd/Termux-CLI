"""Shell tool - Execute shell commands"""

import subprocess
import shlex
from pathlib import Path
from typing import Optional
from dataclasses import dataclass

@dataclass
class ShellResult:
    """Result of shell command execution."""
    stdout: str
    stderr: str
    returncode: int
    command: str

class Shell:
    """Execute shell commands safely."""
    
    # Commands that are blocked for safety
    BLOCKED_COMMANDS = {
        'rm -rf /',
        'dd if=',
        ':(){:|:&};:',  # Fork bomb
    }
    
    def __init__(self, working_dir: str = ".", timeout: int = 60):
        self.working_dir = Path(working_dir).resolve()
        self.timeout = timeout
    
    def execute(self, command: str) -> ShellResult:
        """Execute a shell command."""
        # Safety check
        if self._is_dangerous(command):
            return ShellResult(
                stdout="",
                stderr="Command blocked for safety reasons",
                returncode=1,
                command=command
            )
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.working_dir,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            return ShellResult(
                stdout=result.stdout,
                stderr=result.stderr,
                returncode=result.returncode,
                command=command
            )
        except subprocess.TimeoutExpired:
            return ShellResult(
                stdout="",
                stderr="Command timed out",
                returncode=-1,
                command=command
            )
    
    def _is_dangerous(self, command: str) -> bool:
        """Check if command is potentially dangerous."""
        cmd_lower = command.lower()
        for blocked in self.BLOCKED_COMMANDS:
            if blocked in cmd_lower:
                return True
        return False
