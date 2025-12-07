"""MCP Tools - Tool definitions for MCP"""

from typing import Any, Callable, Dict, List
from dataclasses import dataclass

@dataclass
class ToolDefinition:
    """Definition of an MCP tool."""
    name: str
    description: str
    input_schema: Dict
    handler: Callable

class MCPTools:
    """Manager for MCP tools."""
    
    def __init__(self):
        self.tools: Dict[str, ToolDefinition] = {}
    
    def register(self, name: str, description: str, 
                 input_schema: Dict, handler: Callable):
        """Register a new tool."""
        self.tools[name] = ToolDefinition(
            name=name,
            description=description,
            input_schema=input_schema,
            handler=handler
        )
    
    def get_tool(self, name: str) -> ToolDefinition:
        """Get a tool by name."""
        return self.tools.get(name)
    
    def list_tools(self) -> List[Dict]:
        """List all tools with their schemas."""
        return [
            {
                'name': t.name,
                'description': t.description,
                'inputSchema': t.input_schema
            }
            for t in self.tools.values()
        ]
    
    async def execute(self, name: str, params: Dict) -> Any:
        """Execute a tool."""
        tool = self.tools.get(name)
        if not tool:
            raise ValueError(f"Tool not found: {name}")
        return await tool.handler(**params)
