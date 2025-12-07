"""File operations - Read, write, edit files"""

import os
from pathlib import Path
from typing import List, Optional

class FileOperations:
    """File operation tools."""
    
    def __init__(self, working_dir: str = "."):
        self.working_dir = Path(working_dir).resolve()
    
    def read(self, filepath: str) -> str:
        """Read file contents."""
        path = self._resolve_path(filepath)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def write(self, filepath: str, content: str) -> bool:
        """Write content to file."""
        path = self._resolve_path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    def edit(self, filepath: str, old_text: str, new_text: str) -> bool:
        """Replace text in file."""
        content = self.read(filepath)
        if old_text not in content:
            raise ValueError("Text not found in file")
        new_content = content.replace(old_text, new_text, 1)
        return self.write(filepath, new_content)
    
    def list_dir(self, path: str = ".") -> List[str]:
        """List directory contents."""
        dir_path = self._resolve_path(path)
        return os.listdir(dir_path)
    
    def exists(self, filepath: str) -> bool:
        """Check if file exists."""
        return self._resolve_path(filepath).exists()
    
    def _resolve_path(self, filepath: str) -> Path:
        """Resolve path relative to working directory."""
        path = Path(filepath)
        if not path.is_absolute():
            path = self.working_dir / path
        return path
