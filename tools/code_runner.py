"""Code runner - Execute code in various languages"""

import subprocess
import tempfile
import os
from pathlib import Path
from typing import Tuple, Optional
from dataclasses import dataclass

@dataclass
class ExecutionResult:
    """Result of code execution."""
    stdout: str
    stderr: str
    returncode: int
    success: bool

class CodeRunner:
    """Execute code in multiple languages."""
    
    LANGUAGE_COMMANDS = {
        'python': ['python3', '-c'],
        'javascript': ['node', '-e'],
        'ruby': ['ruby', '-e'],
        'bash': ['bash', '-c'],
        'sh': ['sh', '-c'],
    }
    
    def __init__(self, working_dir: str = ".", timeout: int = 30):
        self.working_dir = Path(working_dir).resolve()
        self.timeout = timeout
    
    def run(self, code: str, language: str = "python") -> ExecutionResult:
        """Execute code in specified language."""
        if language not in self.LANGUAGE_COMMANDS:
            return ExecutionResult(
                stdout="",
                stderr=f"Unsupported language: {language}",
                returncode=1,
                success=False
            )
        
        cmd = self.LANGUAGE_COMMANDS[language] + [code]
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.working_dir,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            return ExecutionResult(
                stdout=result.stdout,
                stderr=result.stderr,
                returncode=result.returncode,
                success=result.returncode == 0
            )
        except subprocess.TimeoutExpired:
            return ExecutionResult(
                stdout="",
                stderr="Execution timed out",
                returncode=-1,
                success=False
            )
    
    def run_file(self, filepath: str) -> ExecutionResult:
        """Run a code file based on extension."""
        path = Path(filepath)
        ext = path.suffix.lower()
        
        ext_to_cmd = {
            '.py': ['python3'],
            '.js': ['node'],
            '.rb': ['ruby'],
            '.sh': ['bash'],
        }
        
        if ext not in ext_to_cmd:
            return ExecutionResult(
                stdout="",
                stderr=f"Unknown file type: {ext}",
                returncode=1,
                success=False
            )
        
        cmd = ext_to_cmd[ext] + [str(filepath)]
        result = subprocess.run(
            cmd,
            cwd=self.working_dir,
            capture_output=True,
            text=True,
            timeout=self.timeout
        )
        return ExecutionResult(
            stdout=result.stdout,
            stderr=result.stderr,
            returncode=result.returncode,
            success=result.returncode == 0
        )
