"""Memory module - Conversation and context memory"""

from typing import List, Dict, Any

class Memory:
    """Manages conversation history and context."""
    
    def __init__(self, max_tokens: int = 8000):
        self.max_tokens = max_tokens
        self.messages: List[Dict[str, Any]] = []
        self.context: Dict[str, Any] = {}
    
    def add(self, role: str, content: str):
        """Add message to memory."""
        self.messages.append({'role': role, 'content': content})
    
    def get_context(self) -> List[Dict[str, Any]]:
        """Get messages within token limit."""
        return self.messages
    
    def clear(self):
        """Clear memory."""
        self.messages = []
