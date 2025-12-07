# API Reference

## Core Module

### Agent

```python
from core.agent import Agent

agent = Agent(working_dir="/path/to/project")
response = agent.run("Your prompt here")
```

**Parameters:**
- `working_dir` (str): Working directory for file operations

**Methods:**
- `run(prompt: str) -> str`: Process prompt and return response
- `load_tools()`: Load available tools

### AgentMemory

```python
from core.memory import AgentMemory

memory = AgentMemory(working_dir=".")
prompt = memory.get_system_prompt()
```

**Methods:**
- `get_system_prompt() -> str`: Get combined memory content
- `add(role: str, content: str)`: Add message to conversation
- `clear()`: Clear conversation memory
- `init_project_memory() -> Path`: Create AGENTS.md
- `add_memory(content: str, scope: str)`: Add memory entry

### Session

```python
from core.session import Session

session = Session()
session.add_message("user", "Hello")
```

## Tools Module

### FileOperations

```python
from tools.file_ops import FileOperations

ops = FileOperations(working_dir=".")
content = ops.read("file.txt")
ops.write("file.txt", "content")
ops.edit("file.txt", "old", "new")
```

### CodeRunner

```python
from tools.code_runner import CodeRunner

runner = CodeRunner(working_dir=".", timeout=30)
result = runner.run("print('hello')", language="python")
print(result.stdout, result.success)
```

### Shell

```python
from tools.shell import Shell

shell = Shell(working_dir=".", timeout=60)
result = shell.execute("ls -la")
print(result.stdout)
```

### Search

```python
from tools.search import Search

search = Search(working_dir=".")
files = search.find_files("*.py")
matches = search.grep("def main", file_pattern="*.py")
```

### GitOperations

```python
from tools.git_ops import GitOperations

git = GitOperations(repo_path=".")
status = git.status()
git.add(["file.py"])
git.commit("Add feature")
```

## Models Module

### AnthropicModel

```python
from models.anthropic import AnthropicModel

model = AnthropicModel(model="claude-3-sonnet-20240229")
response = model.chat([{"role": "user", "content": "Hello"}])

# Streaming
for chunk in model.stream(messages):
    print(chunk, end="")
```

### OllamaModel

```python
from models.ollama import OllamaModel

model = OllamaModel(model="codellama")
models = model.list_models()
response = model.chat([{"role": "user", "content": "Hello"}])
```

## Plugins Module

### Creating a Plugin

```python
from plugins.base import BasePlugin
from plugins.registry import PluginRegistry

class MyPlugin(BasePlugin):
    name = "my_plugin"
    description = "Does something useful"
    version = "1.0.0"
    
    def execute(self, *args, **kwargs):
        return "result"

PluginRegistry.register(MyPlugin)
```

## MCP Module

### MCPServer

```python
from mcp.server import MCPServer

server = MCPServer(host="localhost", port=8080)
server.register_tool("my_tool", handler)
await server.start()
```

### MCPClient

```python
from mcp.client import MCPClient

client = MCPClient()
await client.connect("http://localhost:8080")
result = await client.call_tool("tool_name", {"arg": "value"})
```

## CLI Module

### SlashCommandRegistry

```python
from cli.slash_commands import SlashCommandRegistry

registry = SlashCommandRegistry(working_dir=".")
result = registry.execute("/help")
commands = registry.list_commands()
```
