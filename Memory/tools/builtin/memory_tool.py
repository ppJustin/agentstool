#负责agent的记忆工具
'''
能够为本框架提供记忆能力的工具实现，可以添加到agent中，让其增添记忆功能
'''

from typing import Dict, Any, List
from datetime import datetime

from ..base import Tool, ToolParameter
from ...memory import MemoryManager, MemoryConfig

from Code_base.tool import Tool , ToolParameter
from hello_agents import SimpleAgent, HelloAgentsLLM, ToolRegistry
from hello_agents.tools import MemoryTool