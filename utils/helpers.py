"""Helper functions"""

import os
import hashlib
from pathlib import Path
from typing import Any, Dict, List

def ensure_dir(path: str) -> Path:
    """Ensure directory exists."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p

def get_file_hash(filepath: str) -> str:
    """Get MD5 hash of file."""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def truncate_string(s: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate string to max length."""
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix

def deep_merge(base: Dict, override: Dict) -> Dict:
    """Deep merge two dictionaries."""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def is_binary_file(filepath: str) -> bool:
    """Check if file is binary."""
    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            return b'\x00' in chunk
    except:
        return True
