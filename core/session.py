"""Session management - Handles agent sessions"""

from datetime import datetime
from typing import Optional

class Session:
    """Manages an agent session with context and history."""
    
    def __init__(self, session_id: Optional[str] = None):
        self.session_id = session_id or self._generate_id()
        self.created_at = datetime.now()
        self.messages = []
    
    def _generate_id(self) -> str:
        """Generate unique session ID."""
        import uuid
        return str(uuid.uuid4())
    
    def add_message(self, role: str, content: str):
        """Add a message to session history."""
        self.messages.append({'role': role, 'content': content})
