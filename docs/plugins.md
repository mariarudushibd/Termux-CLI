# Plugin Development

## Creating a Plugin

```python
from plugins.base import BasePlugin
from plugins.registry import PluginRegistry

class MyPlugin(BasePlugin):
    name = "my_plugin"
    description = "Does something useful"
    version = "1.0.0"
    
    def execute(self, *args, **kwargs):
        # Your plugin logic here
        return "Result"
    
    def setup(self):
        # Called when plugin loads
        pass
    
    def teardown(self):
        # Called when plugin unloads
        pass

# Register the plugin
PluginRegistry.register(MyPlugin)
```

## Plugin Directory

Place plugins in `~/.termux-cli/plugins/` for auto-loading.

## Available Hooks

- `on_message` - Called for each user message
- `on_tool_call` - Called before tool execution
- `on_response` - Called before displaying response
