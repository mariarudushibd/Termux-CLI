"""Git operations - Git commands integration"""

import subprocess
from pathlib import Path
from typing import List, Optional, Dict
from dataclasses import dataclass

@dataclass
class GitResult:
    """Result of git operation."""
    success: bool
    output: str
    error: str

class GitOperations:
    """Git command integration."""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
    
    def _run_git(self, *args) -> GitResult:
        """Run a git command."""
        cmd = ['git'] + list(args)
        try:
            result = subprocess.run(
                cmd,
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            return GitResult(
                success=result.returncode == 0,
                output=result.stdout.strip(),
                error=result.stderr.strip()
            )
        except Exception as e:
            return GitResult(success=False, output="", error=str(e))
    
    def status(self) -> GitResult:
        """Get git status."""
        return self._run_git('status', '--short')
    
    def diff(self, staged: bool = False) -> GitResult:
        """Get git diff."""
        args = ['diff']
        if staged:
            args.append('--staged')
        return self._run_git(*args)
    
    def add(self, files: List[str] = None) -> GitResult:
        """Stage files."""
        if files:
            return self._run_git('add', *files)
        return self._run_git('add', '.')
    
    def commit(self, message: str) -> GitResult:
        """Create a commit."""
        return self._run_git('commit', '-m', message)
    
    def log(self, count: int = 10) -> GitResult:
        """Get recent commits."""
        return self._run_git('log', f'-{count}', '--oneline')
    
    def branch(self) -> GitResult:
        """List branches."""
        return self._run_git('branch', '-a')
    
    def checkout(self, branch: str) -> GitResult:
        """Checkout a branch."""
        return self._run_git('checkout', branch)
