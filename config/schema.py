"""Config schema validation"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class ValidationError:
    """Validation error details."""
    path: str
    message: str

CONFIG_SCHEMA = {
    "model": {
        "type": "object",
        "properties": {
            "provider": {"type": "string", "enum": ["openai", "anthropic", "ollama"]},
            "name": {"type": "string"},
            "temperature": {"type": "number", "min": 0, "max": 2},
            "max_tokens": {"type": "integer", "min": 1}
        }
    },
    "agent": {
        "type": "object",
        "properties": {
            "max_iterations": {"type": "integer", "min": 1, "max": 100},
            "auto_approve": {"type": "boolean"},
            "safe_mode": {"type": "boolean"}
        }
    }
}

def validate_config(config: Dict[str, Any]) -> List[ValidationError]:
    """Validate configuration against schema."""
    errors = []
    
    # Basic validation
    if "model" in config:
        model = config["model"]
        if "provider" in model:
            if model["provider"] not in ["openai", "anthropic", "ollama"]:
                errors.append(ValidationError(
                    path="model.provider",
                    message=f"Invalid provider: {model['provider']}"
                ))
        if "temperature" in model:
            if not 0 <= model["temperature"] <= 2:
                errors.append(ValidationError(
                    path="model.temperature",
                    message="Temperature must be between 0 and 2"
                ))
    
    return errors
