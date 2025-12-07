"""Search tool - Search files and content"""

import os
import re
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class SearchMatch:
    """A search match result."""
    file: str
    line_number: int
    line_content: str
    match: str

class Search:
    """Search files and content."""
    
    def __init__(self, working_dir: str = "."):
        self.working_dir = Path(working_dir).resolve()
    
    def find_files(self, pattern: str, path: str = ".") -> List[str]:
        """Find files matching glob pattern."""
        search_path = self._resolve_path(path)
        matches = list(search_path.rglob(pattern))
        return [str(m.relative_to(self.working_dir)) for m in matches]
    
    def grep(self, pattern: str, path: str = ".", 
             file_pattern: str = "*") -> List[SearchMatch]:
        """Search for pattern in files."""
        search_path = self._resolve_path(path)
        results = []
        regex = re.compile(pattern)
        
        for file_path in search_path.rglob(file_pattern):
            if file_path.is_file():
                try:
                    matches = self._search_file(file_path, regex)
                    results.extend(matches)
                except (UnicodeDecodeError, PermissionError):
                    continue
        
        return results
    
    def _search_file(self, filepath: Path, regex) -> List[SearchMatch]:
        """Search within a single file."""
        matches = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                for match in regex.finditer(line):
                    matches.append(SearchMatch(
                        file=str(filepath.relative_to(self.working_dir)),
                        line_number=line_num,
                        line_content=line.strip(),
                        match=match.group()
                    ))
        return matches
    
    def _resolve_path(self, path: str) -> Path:
        """Resolve path relative to working directory."""
        p = Path(path)
        if not p.is_absolute():
            p = self.working_dir / p
        return p
