"""Memory module - AGENTS.md based memory system

Hierarchical memory system inspired by Claude Code:
1. Enterprise/System policy (read-only)
2. Project memory (AGENTS.md or .termux-cli/AGENTS.md)
3. User memory (~/.termux-cli/AGENTS.md)
4. Local project memory (AGENTS.local.md - gitignored)
"""

import os
import re
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class MemoryFile:
    """Represents a memory file."""
    path: Path
    content: str
    scope: str  # enterprise, project, user, local
    priority: int  # Higher = more precedence

class AgentMemory:
    """Manages hierarchical memory using AGENTS.md files."""
    
    MEMORY_FILENAME = "AGENTS.md"
    LOCAL_MEMORY_FILENAME = "AGENTS.local.md"
    PROJECT_DIR = ".termux-cli"
    
    def __init__(self, working_dir: str = "."):
        self.working_dir = Path(working_dir).resolve()
        self.memory_files: List[MemoryFile] = []
        self.messages: List[Dict[str, Any]] = []
        self.context: Dict[str, Any] = {}
        self._load_all_memories()
    
    def _load_all_memories(self):
        """Load all memory files in priority order."""
        self.memory_files = []
        
        # 1. Enterprise policy (lowest priority, loaded first)
        enterprise_paths = self._get_enterprise_paths()
        for path in enterprise_paths:
            if path.exists():
                self._load_memory_file(path, "enterprise", 1)
        
        # 2. User memory
        user_path = Path.home() / self.PROJECT_DIR / self.MEMORY_FILENAME
        if user_path.exists():
            self._load_memory_file(user_path, "user", 2)
        
        # 3. Project memory (recursive up from cwd)
        self._load_project_memories()
        
        # 4. Local project memory (highest priority)
        local_path = self.working_dir / self.LOCAL_MEMORY_FILENAME
        if local_path.exists():
            self._load_memory_file(local_path, "local", 4)
    
    def _get_enterprise_paths(self) -> List[Path]:
        """Get enterprise memory paths for current OS."""
        import platform
        system = platform.system()
        
        if system == "Darwin":  # macOS
            return [Path("/Library/Application Support/TermuxCLI/AGENTS.md")]
        elif system == "Linux":
            # Check for Termux
            if os.environ.get("PREFIX", "").startswith("/data/data/com.termux"):
                return [Path(os.environ["PREFIX"]) / "etc/termux-cli/AGENTS.md"]
            return [Path("/etc/termux-cli/AGENTS.md")]
        elif system == "Windows":
            return [Path("C:/Program Files/TermuxCLI/AGENTS.md")]
        return []
    
    def _load_project_memories(self):
        """Load project memories, recursing up from cwd."""
        current = self.working_dir
        found_memories = []
        
        # Walk up the directory tree
        while current != current.parent:
            # Check for AGENTS.md in directory
            for mem_path in [
                current / self.MEMORY_FILENAME,
                current / self.PROJECT_DIR / self.MEMORY_FILENAME,
            ]:
                if mem_path.exists():
                    found_memories.append(mem_path)
            current = current.parent
        
        # Load in reverse order (higher directories first)
        for i, path in enumerate(reversed(found_memories)):
            self._load_memory_file(path, "project", 3)
    
    def _load_memory_file(self, path: Path, scope: str, priority: int):
        """Load a single memory file."""
        try:
            content = path.read_text(encoding="utf-8")
            
            # Process imports (@path/to/file)
            content = self._process_imports(content, path.parent)
            
            self.memory_files.append(MemoryFile(
                path=path,
                content=content,
                scope=scope,
                priority=priority
            ))
        except Exception as e:
            print(f"Warning: Could not load memory file {path}: {e}")
    
    def _process_imports(self, content: str, base_dir: Path, depth: int = 0) -> str:
        """Process @import references in memory files."""
        if depth > 5:  # Max recursion depth
            return content
        
        pattern = r'^@([^\s]+)$'
        lines = content.split('\n')
        result_lines = []
        
        for line in lines:
            match = re.match(pattern, line.strip())
            if match:
                import_path = match.group(1)
                
                # Handle home directory
                if import_path.startswith('~'):
                    full_path = Path(import_path).expanduser()
                else:
                    full_path = base_dir / import_path
                
                if full_path.exists():
                    imported_content = full_path.read_text(encoding="utf-8")
                    imported_content = self._process_imports(
                        imported_content, full_path.parent, depth + 1
                    )
                    result_lines.append(f"# Imported from {import_path}")
                    result_lines.append(imported_content)
                else:
                    result_lines.append(f"# [Import not found: {import_path}]")
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    def get_system_prompt(self) -> str:
        """Get combined memory content for system prompt."""
        # Sort by priority (higher priority = later = overrides)
        sorted_memories = sorted(self.memory_files, key=lambda m: m.priority)
        
        sections = []
        for mem in sorted_memories:
            sections.append(f"# Memory ({mem.scope}): {mem.path.name}")
            sections.append(mem.content)
            sections.append("")
        
        return "\n".join(sections)
    
    def add(self, role: str, content: str):
        """Add message to conversation memory."""
        self.messages.append({"role": role, "content": content})
    
    def get_context(self) -> List[Dict[str, Any]]:
        """Get conversation messages."""
        return self.messages
    
    def clear(self):
        """Clear conversation memory."""
        self.messages = []
    
    def init_project_memory(self) -> Path:
        """Initialize AGENTS.md for current project."""
        mem_path = self.working_dir / self.MEMORY_FILENAME
        
        if mem_path.exists():
            return mem_path
        
        template = '''# Project Instructions for Termux-CLI

## Project Overview
@README.md

## Code Style
- Use descriptive variable names
- Add docstrings to all public functions
- Follow PEP 8 for Python code

## Common Commands
- Build: `python -m build`
- Test: `pytest tests/`
- Lint: `ruff check .`

## Important Notes
- Always run tests before committing
- Update documentation for new features
'''
        
        mem_path.write_text(template, encoding="utf-8")
        return mem_path
    
    def add_memory(self, content: str, scope: str = "project") -> bool:
        """Add a memory entry to appropriate file."""
        if scope == "local":
            path = self.working_dir / self.LOCAL_MEMORY_FILENAME
        elif scope == "user":
            path = Path.home() / self.PROJECT_DIR / self.MEMORY_FILENAME
            path.parent.mkdir(parents=True, exist_ok=True)
        else:
            path = self.working_dir / self.MEMORY_FILENAME
        
        existing = ""
        if path.exists():
            existing = path.read_text(encoding="utf-8")
        
        new_content = existing.rstrip() + "\n\n- " + content + "\n"
        path.write_text(new_content, encoding="utf-8")
        
        # Reload memories
        self._load_all_memories()
        return True
