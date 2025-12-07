"""Output formatters"""

from typing import Any, Dict, List
import json

def format_json(data: Any, indent: int = 2) -> str:
    """Format data as JSON."""
    return json.dumps(data, indent=indent, default=str)

def format_table(headers: List[str], rows: List[List[Any]], padding: int = 2) -> str:
    """Format data as ASCII table."""
    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    
    # Build table
    lines = []
    
    # Header
    header_line = " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers))
    lines.append(header_line)
    lines.append("-" * len(header_line))
    
    # Rows
    for row in rows:
        row_line = " | ".join(str(c).ljust(widths[i]) for i, c in enumerate(row))
        lines.append(row_line)
    
    return "\n".join(lines)

def format_code_block(code: str, language: str = "") -> str:
    """Format code as markdown code block."""
    return f"```{language}\n{code}\n```"

def format_file_size(size_bytes: int) -> str:
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} PB"

def format_duration(seconds: float) -> str:
    """Format duration in human-readable format."""
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        return f"{seconds/60:.1f}m"
    else:
        return f"{seconds/3600:.1f}h"
