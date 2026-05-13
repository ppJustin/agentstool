#负责agent的记忆工具
'''
能够为本框架提供记忆能力的工具实现，可以添加到agent中，让其增添记忆功能
'''

from typing import Dict, Any, List
from datetime import datetime

from Code_base.tool import Tool , ToolParameter
import MemoryManager, MemoryConfig