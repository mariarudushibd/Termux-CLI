"""Base model class - Common model interface"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Generator

class BaseModel(ABC):
    """Abstract base class for AI models."""
    
    name: str = "base"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
    
    @abstractmethod
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Send messages and get response."""
        pass
    
    @abstractmethod
    def stream(self, messages: List[Dict[str, str]], **kwargs) -> Generator[str, None, None]:
        """Stream response tokens."""
        pass
    
    def count_tokens(self, text: str) -> int:
        """Estimate token count."""
        return len(text) // 4  # Rough estimate
