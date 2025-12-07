"""Prompts module - System and user prompts"""

from .system import SYSTEM_PROMPT, get_system_prompt
from .templates import PromptTemplate

__all__ = ['SYSTEM_PROMPT', 'get_system_prompt', 'PromptTemplate']
