"""Plugin loader - Dynamically loads plugins"""

import importlib
import os
from pathlib import Path
from typing import List, Type

from .base import BasePlugin

class PluginLoader:
    """Dynamically loads plugins from directory."""
    
    def __init__(self, plugin_dir: str = None):
        self.plugin_dir = Path(plugin_dir) if plugin_dir else None
        self.loaded_plugins: List[BasePlugin] = []
    
    def load_all(self) -> List[BasePlugin]:
        """Load all plugins from plugin directory."""
        if not self.plugin_dir or not self.plugin_dir.exists():
            return []
        
        # Discovery and loading logic
        return self.loaded_plugins
    
    def load_plugin(self, module_path: str) -> BasePlugin:
        """Load a single plugin by module path."""
        module = importlib.import_module(module_path)
        return module
