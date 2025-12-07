#!/usr/bin/env python3
"""Example: Running Termux-CLI as MCP server"""

import asyncio
from mcp.server import MCPServer
from mcp.tools import MCPTools
from tools.file_ops import FileOperations
from tools.code_runner import CodeRunner

async def main():
    # Initialize tools
    file_ops = FileOperations(".")
    code_runner = CodeRunner(".")
    
    # Create MCP tools registry
    mcp_tools = MCPTools()
    
    # Register tools
    mcp_tools.register(
        name="read_file",
        description="Read contents of a file",
        input_schema={
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path"}
            },
            "required": ["path"]
        },
        handler=lambda path: file_ops.read(path)
    )
    
    # Start server
    server = MCPServer(host="localhost", port=8080)
    print("Starting MCP server on localhost:8080...")
    await server.start()

if __name__ == "__main__":
    asyncio.run(main())
