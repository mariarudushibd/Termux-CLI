"""Anthropic integration - Claude models"""

import os
from typing import List, Dict, Generator, Optional

from .base import BaseModel

class AnthropicModel(BaseModel):
    """Anthropic Claude model integration."""
    
    name = "anthropic"
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-sonnet-20240229"):
        super().__init__(api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        self.client = None
    
    def _get_client(self):
        if self.client is None:
            try:
                from anthropic import Anthropic
                self.client = Anthropic(api_key=self.api_key)
            except ImportError:
                raise ImportError("anthropic package required: pip install anthropic")
        return self.client
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Send message to Claude."""
        client = self._get_client()
        
        # Extract system message if present
        system = ""
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system = msg["content"]
            else:
                chat_messages.append(msg)
        
        response = client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=system,
            messages=chat_messages,
            **kwargs
        )
        return response.content[0].text
    
    def stream(self, messages: List[Dict[str, str]], **kwargs) -> Generator[str, None, None]:
        """Stream response from Claude."""
        client = self._get_client()
        
        system = ""
        chat_messages = []
        for msg in messages:
            if msg["role"] == "system":
                system = msg["content"]
            else:
                chat_messages.append(msg)
        
        with client.messages.stream(
            model=self.model,
            max_tokens=4096,
            system=system,
            messages=chat_messages,
            **kwargs
        ) as stream:
            for text in stream.text_stream:
                yield text
