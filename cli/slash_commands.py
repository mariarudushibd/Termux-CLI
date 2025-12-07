"""Slash Commands - Custom command system inspired by Claude Code

Supports:
- Built-in commands (/help, /clear, /exit, etc.)
- Custom project commands (.termux-cli/commands/)
- User commands (~/.termux-cli/commands/)
- MCP commands (/mcp__server__tool)
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass, field
import frontmatter

@dataclass
class SlashCommand:
    """Represents a slash command."""
    name: str
    description: str
    handler: Optional[Callable] = None
    source: str = "built-in"  # built-in, project, user, mcp
    content: str = ""
    allowed_tools: List[str] = field(default_factory=list)
    argument_hint: str = ""
    model: Optional[str] = None

class SlashCommandRegistry:
    """Registry for all slash commands."""
    
    PROJECT_COMMANDS_DIR = ".termux-cli/commands"
    USER_COMMANDS_DIR = "~/.termux-cli/commands"
    
    def __init__(self, working_dir: str = "."):
        self.working_dir = Path(working_dir).resolve()
        self.commands: Dict[str, SlashCommand] = {}
        self._register_builtins()
        self._load_custom_commands()
    
    def _register_builtins(self):
        """Register built-in commands."""
        builtins = [
            ("/help", "Show available commands", self._cmd_help),
            ("/clear", "Clear conversation history", self._cmd_clear),
            ("/exit", "Exit the agent", self._cmd_exit),
            ("/compact", "Compact conversation with optional focus", self._cmd_compact),
            ("/config", "Open settings", self._cmd_config),
            ("/cost", "Show token usage statistics", self._cmd_cost),
            ("/init", "Initialize project with AGENTS.md", self._cmd_init),
            ("/memory", "Edit memory files (AGENTS.md)", self._cmd_memory),
            ("/model", "Select or change AI model", self._cmd_model),
            ("/mcp", "Manage MCP server connections", self._cmd_mcp),
            ("/permissions", "View or update permissions", self._cmd_permissions),
            ("/resume", "Resume a conversation", self._cmd_resume),
            ("/review", "Request code review", self._cmd_review),
            ("/status", "Show version, model, account info", self._cmd_status),
            ("/todos", "List current todo items", self._cmd_todos),
            ("/vim", "Enter vim mode", self._cmd_vim),
        ]
        
        for name, desc, handler in builtins:
            self.commands[name] = SlashCommand(
                name=name,
                description=desc,
                handler=handler,
                source="built-in"
            )
    
    def _load_custom_commands(self):
        """Load custom commands from project and user directories."""
        # Project commands
        project_dir = self.working_dir / self.PROJECT_COMMANDS_DIR
        self._load_commands_from_dir(project_dir, "project")
        
        # User commands
        user_dir = Path(self.USER_COMMANDS_DIR).expanduser()
        self._load_commands_from_dir(user_dir, "user")
    
    def _load_commands_from_dir(self, directory: Path, source: str):
        """Load commands from a directory."""
        if not directory.exists():
            return
        
        for md_file in directory.rglob("*.md"):
            try:
                post = frontmatter.load(md_file)
                name = "/" + md_file.stem
                
                # Get namespace from subdirectory
                rel_path = md_file.relative_to(directory)
                if len(rel_path.parts) > 1:
                    namespace = ":".join(rel_path.parts[:-1])
                    source_label = f"{source}:{namespace}"
                else:
                    source_label = source
                
                self.commands[name] = SlashCommand(
                    name=name,
                    description=post.get("description", post.content.split("\n")[0][:50]),
                    content=post.content,
                    source=source_label,
                    allowed_tools=post.get("allowed-tools", "").split(", ") if post.get("allowed-tools") else [],
                    argument_hint=post.get("argument-hint", ""),
                    model=post.get("model")
                )
            except Exception as e:
                print(f"Error loading command {md_file}: {e}")
    
    def execute(self, command_str: str, context: Any = None) -> str:
        """Execute a slash command."""
        parts = command_str.split(maxsplit=1)
        cmd_name = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        
        if cmd_name not in self.commands:
            return f"Unknown command: {cmd_name}. Use /help for available commands."
        
        cmd = self.commands[cmd_name]
        
        # Built-in command with handler
        if cmd.handler:
            return cmd.handler(args, context)
        
        # Custom command - process template
        content = cmd.content
        
        # Replace $ARGUMENTS with all args
        content = content.replace("$ARGUMENTS", args)
        
        # Replace positional arguments $1, $2, etc.
        arg_parts = args.split()
        for i, arg in enumerate(arg_parts, 1):
            content = content.replace(f"${i}", arg)
        
        # Process file references (@file)
        content = self._process_file_refs(content)
        
        # Process bash commands (!`command`)
        content = self._process_bash_commands(content)
        
        return content
    
    def _process_file_refs(self, content: str) -> str:
        """Replace @filepath with file contents."""
        pattern = r'@([\w./\-]+)'
        
        def replace_file(match):
            filepath = match.group(1)
            full_path = self.working_dir / filepath
            try:
                return full_path.read_text()
            except:
                return f"[File not found: {filepath}]"
        
        return re.sub(pattern, replace_file, content)
    
    def _process_bash_commands(self, content: str) -> str:
        """Execute !`command` and replace with output."""
        pattern = r'!`([^`]+)`'
        
        def run_command(match):
            import subprocess
            cmd = match.group(1)
            try:
                result = subprocess.run(
                    cmd, shell=True, capture_output=True,
                    text=True, timeout=30, cwd=self.working_dir
                )
                return result.stdout or result.stderr
            except:
                return f"[Command failed: {cmd}]"
        
        return re.sub(pattern, run_command, content)
    
    def list_commands(self) -> List[SlashCommand]:
        """List all available commands."""
        return sorted(self.commands.values(), key=lambda c: c.name)
    
    # Built-in command handlers
    def _cmd_help(self, args: str, ctx: Any) -> str:
        lines = ["Available commands:\n"]
        for cmd in self.list_commands():
            hint = f" {cmd.argument_hint}" if cmd.argument_hint else ""
            lines.append(f"  {cmd.name}{hint} - {cmd.description} ({cmd.source})")
        return "\n".join(lines)
    
    def _cmd_clear(self, args: str, ctx: Any) -> str:
        return "__CLEAR__"
    
    def _cmd_exit(self, args: str, ctx: Any) -> str:
        return "__EXIT__"
    
    def _cmd_compact(self, args: str, ctx: Any) -> str:
        return f"Compacting conversation... Focus: {args or 'general'}"
    
    def _cmd_config(self, args: str, ctx: Any) -> str:
        return "Opening configuration..."
    
    def _cmd_cost(self, args: str, ctx: Any) -> str:
        return "Token usage: 0 input, 0 output"
    
    def _cmd_init(self, args: str, ctx: Any) -> str:
        return "__INIT__"
    
    def _cmd_memory(self, args: str, ctx: Any) -> str:
        return "__MEMORY__"
    
    def _cmd_model(self, args: str, ctx: Any) -> str:
        return f"__MODEL__:{args}" if args else "Current model: claude-3-sonnet"
    
    def _cmd_mcp(self, args: str, ctx: Any) -> str:
        return "MCP servers: None configured"
    
    def _cmd_permissions(self, args: str, ctx: Any) -> str:
        return "Permissions: file_ops, code_runner, shell, search, git_ops"
    
    def _cmd_resume(self, args: str, ctx: Any) -> str:
        return "__RESUME__"
    
    def _cmd_review(self, args: str, ctx: Any) -> str:
        return "Starting code review..."
    
    def _cmd_status(self, args: str, ctx: Any) -> str:
        return "Termux-CLI v0.1.0 | Model: claude-3-sonnet | Status: Ready"
    
    def _cmd_todos(self, args: str, ctx: Any) -> str:
        return "No todos in current session"
    
    def _cmd_vim(self, args: str, ctx: Any) -> str:
        return "Entering vim mode..."
