"""Tests for MCP module"""

import pytest

class TestMCPProtocol:
    """Tests for MCP protocol handling."""
    
    def test_create_request(self):
        """Test creating MCP request."""
        from mcp.protocol import Protocol
        
        request = Protocol.create_request(
            method="tools/call",
            params={"name": "read_file", "arguments": {"path": "test.txt"}},
            id="req-1"
        )
        
        assert request["jsonrpc"] == "2.0"
        assert request["method"] == "tools/call"
        assert request["id"] == "req-1"
    
    def test_create_response(self):
        """Test creating MCP response."""
        from mcp.protocol import Protocol
        
        response = Protocol.create_response(
            id="req-1",
            result={"content": "file contents"}
        )
        
        assert response["jsonrpc"] == "2.0"
        assert response["id"] == "req-1"
        assert response["result"]["content"] == "file contents"

class TestMCPTools:
    """Tests for MCP tool registry."""
    
    def test_register_tool(self):
        """Test registering a tool."""
        from mcp.tools import MCPTools
        
        tools = MCPTools()
        tools.register(
            name="test_tool",
            description="A test tool",
            input_schema={"type": "object"},
            handler=lambda: "result"
        )
        
        assert tools.get_tool("test_tool") is not None
    
    def test_list_tools(self):
        """Test listing tools."""
        from mcp.tools import MCPTools
        
        tools = MCPTools()
        tools.register(
            name="tool1",
            description="Tool 1",
            input_schema={},
            handler=lambda: None
        )
        tools.register(
            name="tool2",
            description="Tool 2",
            input_schema={},
            handler=lambda: None
        )
        
        tool_list = tools.list_tools()
        assert len(tool_list) == 2
        names = [t["name"] for t in tool_list]
        assert "tool1" in names
        assert "tool2" in names
