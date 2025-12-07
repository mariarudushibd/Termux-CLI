"""Plugins tests"""

import pytest

class TestBasePlugin:
    """Tests for BasePlugin."""
    
    def test_plugin_info(self):
        """Test plugin info method."""
        from plugins.base import BasePlugin
        
        class TestPlugin(BasePlugin):
            name = "test"
            description = "A test plugin"
            version = "1.0.0"
            
            def execute(self):
                return "executed"
        
        plugin = TestPlugin()
        info = plugin.get_info()
        
        assert info["name"] == "test"
        assert info["version"] == "1.0.0"

class TestPluginRegistry:
    """Tests for PluginRegistry."""
    
    def test_register_plugin(self):
        """Test registering a plugin."""
        from plugins.registry import PluginRegistry
        from plugins.base import BasePlugin
        
        class MyPlugin(BasePlugin):
            name = "my_plugin"
            def execute(self):
                pass
        
        PluginRegistry.register(MyPlugin)
        assert PluginRegistry.get("my_plugin") == MyPlugin
        
        # Cleanup
        PluginRegistry.unregister("my_plugin")
