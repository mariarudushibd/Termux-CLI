"""Plugin registry - Manages available plugins"""

from typing import Dict, Optional, Type
from .base import BasePlugin

class PluginRegistry:
    """Central registry for all plugins."""
    
    _plugins: Dict[str, Type[BasePlugin]] = {}
    
    @classmethod
    def register(cls, plugin_class: Type[BasePlugin]):
        """Register a plugin class."""
        cls._plugins[plugin_class.name] = plugin_class
    
    @classmethod
    def get(cls, name: str) -> Optional[Type[BasePlugin]]:
        """Get a plugin by name."""
        return cls._plugins.get(name)
    
    @classmethod
    def list_all(cls) -> Dict[str, Type[BasePlugin]]:
        """List all registered plugins."""
        return cls._plugins.copy()
    
    @classmethod
    def unregister(cls, name: str):
        """Unregister a plugin."""
        cls._plugins.pop(name, None)
