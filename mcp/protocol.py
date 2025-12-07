"""MCP Protocol - Protocol definitions and handlers"""

from enum import Enum
from typing import Any, Dict, Optional
from dataclasses import dataclass

class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"
    NOTIFICATION = "notification"
    ERROR = "error"

@dataclass
class MCPMessage:
    """Base MCP message structure."""
    jsonrpc: str = "2.0"
    id: Optional[str] = None
    method: Optional[str] = None
    params: Optional[Dict] = None
    result: Optional[Any] = None
    error: Optional[Dict] = None

class Protocol:
    """MCP Protocol handler."""
    
    @staticmethod
    def create_request(method: str, params: Dict, id: str) -> Dict:
        """Create an MCP request."""
        return {
            "jsonrpc": "2.0",
            "id": id,
            "method": method,
            "params": params
        }
    
    @staticmethod
    def create_response(id: str, result: Any) -> Dict:
        """Create an MCP response."""
        return {
            "jsonrpc": "2.0",
            "id": id,
            "result": result
        }
    
    @staticmethod
    def parse_message(data: Dict) -> MCPMessage:
        """Parse incoming MCP message."""
        return MCPMessage(**data)
