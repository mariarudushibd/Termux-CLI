#!/usr/bin/env python3
"""Example: Creating a custom plugin"""

from plugins.base import BasePlugin
from plugins.registry import PluginRegistry

class WeatherPlugin(BasePlugin):
    """Example plugin that fetches weather info."""
    
    name = "weather"
    description = "Get weather information for a location"
    version = "1.0.0"
    
    def execute(self, location: str = "New York"):
        """Fetch weather for location."""
        return f"Weather for {location}: Sunny, 72°F"
    
    def setup(self):
        print(f"Weather plugin v{self.version} loaded")

# Register the plugin
PluginRegistry.register(WeatherPlugin)

if __name__ == "__main__":
    plugin = WeatherPlugin()
    result = plugin.execute("San Francisco")
    print(result)
