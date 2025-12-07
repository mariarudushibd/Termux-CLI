"""OpenAI integration - GPT models"""

import os
from typing import List, Dict, Generator, Optional

from .base import BaseModel

class OpenAIModel(BaseModel):
    """OpenAI GPT model integration."""
    
    name = "openai"
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        super().__init__(api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model
        self.client = None
    
    def _get_client(self):
        if self.client is None:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
            except ImportError:
                raise ImportError("openai package required: pip install openai")
        return self.client
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Send chat completion request."""
        client = self._get_client()
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content
    
    def stream(self, messages: List[Dict[str, str]], **kwargs) -> Generator[str, None, None]:
        """Stream chat completion."""
        client = self._get_client()
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            stream=True,
            **kwargs
        )
        for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
