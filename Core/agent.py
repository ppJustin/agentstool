#Agent类 顶层抽象 
from abc import ABC , abstractmethod
from typing import Optional,Any
from .message import Message
from .llm import HelloAgentsLLM
from .config import Config

class Agent(ABC):
    '''定义一个Agent基类'''

    def __init__(
            self,
            name : str,
            llm : HelloAgentsLLM,
            system_prompt : Optional[str] = None,
            config : Optional[Config] = None
    ):
        self.name = name
        self.llm = llm
        self.system_prompt = system_prompt
        self.config = config or Config()
        self._history : list[Message] = []       #列表中元素是Message类实例
    @abstractmethod
    def run(self,input_text:str,**kwargs) -> str:       #用户输入文本
        #必须有run方法来运行Agent
        pass

    def add_message(self,message:Message):  #无返回值
        '''添加消息到历史的聊天记录中'''
        self._history.append(message)

    def clear_history(self):
        '''清空历史记录/清楚上下文'''
        self._history.clear()

    def get_history(self) -> list[Message]:
        '''获取所有的聊天记录'''
        return self._history.copy()     #复制份源列表，防止被进行数据篡改
    
    def __str__(self) -> str:
        return f"Agent(name={self.name},provider={self.llm.provider})"
    

