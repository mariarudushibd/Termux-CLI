"""Plugins module - Extensible plugin system"""

from .base import BasePlugin
from .loader import PluginLoader
from .registry import PluginRegistry

__all__ = ['BasePlugin', 'PluginLoader', 'PluginRegistry']
