"""Base plugin class - All plugins inherit from this"""

from abc import ABC, abstractmethod
from typing import Any, Dict

class BasePlugin(ABC):
    """Base class for all plugins."""
    
    name: str = "base"
    description: str = ""
    version: str = "1.0.0"
    
    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """Execute the plugin's main functionality."""
        pass
    
    def setup(self):
        """Called when plugin is loaded."""
        pass
    
    def teardown(self):
        """Called when plugin is unloaded."""
        pass
    
    def get_info(self) -> Dict[str, str]:
        """Return plugin information."""
        return {
            'name': self.name,
            'description': self.description,
            'version': self.version
        }
