"""Settings - Application settings"""

import os
import json
from pathlib import Path
from typing import Any, Optional, Dict

class Settings:
    """Application settings manager."""
    
    CONFIG_FILE = ".termux-cli.json"
    
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = Path(config_path) if config_path else self._find_config()
        self._settings: Dict[str, Any] = {}
        self._load()
    
    def _find_config(self) -> Path:
        """Find config file in current or home directory."""
        local_config = Path.cwd() / self.CONFIG_FILE
        if local_config.exists():
            return local_config
        return Path.home() / self.CONFIG_FILE
    
    def _load(self):
        """Load settings from file."""
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                self._settings = json.load(f)
        else:
            from .defaults import DEFAULTS
            self._settings = DEFAULTS.copy()
    
    def save(self):
        """Save settings to file."""
        with open(self.config_path, 'w') as f:
            json.dump(self._settings, f, indent=2)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        keys = key.split('.')
        value = self._settings
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default
    
    def set(self, key: str, value: Any):
        """Set a setting value."""
        keys = key.split('.')
        target = self._settings
        for k in keys[:-1]:
            target = target.setdefault(k, {})
        target[keys[-1]] = value
