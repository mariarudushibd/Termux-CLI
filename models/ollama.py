"""Ollama integration - Local models"""

import json
import requests
from typing import List, Dict, Generator, Optional

from .base import BaseModel

class OllamaModel(BaseModel):
    """Ollama local model integration."""
    
    name = "ollama"
    
    def __init__(self, model: str = "llama2", base_url: str = "http://localhost:11434"):
        super().__init__()
        self.model = model
        self.base_url = base_url
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Send chat request to Ollama."""
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": False,
                **kwargs
            }
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    
    def stream(self, messages: List[Dict[str, str]], **kwargs) -> Generator[str, None, None]:
        """Stream response from Ollama."""
        response = requests.post(
            f"{self.base_url}/api/chat",
            json={
                "model": self.model,
                "messages": messages,
                "stream": True,
                **kwargs
            },
            stream=True
        )
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                data = json.loads(line)
                if "message" in data and "content" in data["message"]:
                    yield data["message"]["content"]
    
    def list_models(self) -> List[str]:
        """List available Ollama models."""
        response = requests.get(f"{self.base_url}/api/tags")
        response.raise_for_status()
        return [m["name"] for m in response.json().get("models", [])]
