"""Agent class - Main coding agent implementation"""

class Agent:
    """Main coding agent that orchestrates all operations."""
    
    def __init__(self, working_dir: str = None):
        self.working_dir = working_dir
        self.memory = None
        self.tools = []
    
    def run(self, prompt: str):
        """Process a user prompt and execute actions."""
        pass
    
    def load_tools(self):
        """Load available tools."""
        pass
