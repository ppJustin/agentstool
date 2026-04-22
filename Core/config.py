#用于配置管理的代码文件
import os
from typing import Optional,Any,Dict
from pydantic import BaseModel

class Config(BaseModel):
    '''客户端配置类，把所有需要调整的设置项集中放在一个地方，方便统一管理和修改。'''

    #LLM配置
    default_model:str = "gpt-3.5-turbo"     #default-默认值
    default_provider :str = "openai"
    temperature : float = 0.7
    max_tokens : Optional[int] = None

    #系统配置
    debug : bool = False
    log_level : str = "INFO"

    #其他配置
    max_history_length : int = 100

    @classmethod
    def from_env(cls) -> "Config":
        '''从环境变量中获取配置'''
        return cls(
            debug = os.getenv("DEBUG","false").lower() == "true",
            log_level = os.getenv("LOG_LEVEL","INFO"),
            temperature = float(os.getenv("TEMPERATURE","0.7")),
            max_tokens = int(os.getenv("MAX_TOKENS")) if os.getenv("MAX_TOKENS") else None,
        )       #返回一个config类型的对象
    
    def to_dict(self) -> Dict(str,Any):
        #转化为字典
        return self.model_dump()
    #将Pydantic对象转换成Python字典，方便读取