"""Default configurations"""

DEFAULTS = {
    "model": {
        "provider": "anthropic",
        "name": "claude-3-sonnet-20240229",
        "temperature": 0.7,
        "max_tokens": 4096
    },
    "agent": {
        "max_iterations": 10,
        "auto_approve": False,
        "safe_mode": True
    },
    "tools": {
        "enabled": [
            "file_ops",
            "code_runner",
            "shell",
            "search",
            "git_ops"
        ],
        "shell": {
            "timeout": 60,
            "blocked_commands": []
        },
        "code_runner": {
            "timeout": 30,
            "languages": ["python", "javascript", "bash"]
        }
    },
    "ui": {
        "theme": "default",
        "show_tokens": False,
        "syntax_highlighting": True
    },
    "mcp": {
        "enabled": False,
        "servers": []
    }
}
