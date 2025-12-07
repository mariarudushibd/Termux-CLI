"""Input validators"""

import re
from pathlib import Path
from typing import Optional

def validate_path(path: str, must_exist: bool = False) -> tuple[bool, Optional[str]]:
    """Validate a file path."""
    try:
        p = Path(path)
        if must_exist and not p.exists():
            return False, f"Path does not exist: {path}"
        return True, None
    except Exception as e:
        return False, str(e)

def validate_url(url: str) -> tuple[bool, Optional[str]]:
    """Validate a URL."""
    pattern = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    if pattern.match(url):
        return True, None
    return False, "Invalid URL format"

def validate_model_name(name: str) -> tuple[bool, Optional[str]]:
    """Validate model name."""
    valid_patterns = [
        r'^gpt-[34]',
        r'^claude-',
        r'^llama',
        r'^mistral',
        r'^codellama'
    ]
    for pattern in valid_patterns:
        if re.match(pattern, name, re.IGNORECASE):
            return True, None
    return False, f"Unknown model: {name}"
