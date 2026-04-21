#消息系统中枢

from typing import Optional,Dict,Any,Literal
from datetime import datetime
from pydantic import BaseModel

#定义消息系统中角色的类型，并限制角色的取值
MessageRole = Literal["user","assistant","system","tool"]

class Message(BaseModel):
        #定义的消息类
    content : str
    role : MessageRole
    timestamp : Optional[datetime] = None   #时间戳
    metadata : Optional[Dict[str,Any]] = None       #元数据

    def __init__(self,content:str,role:MessageRole,**kwargs):
        super().__init__(
            content = content,
            role = role,
            timestamp = kwargs.get("timestamp",datetime.now()),
            metadata = kwargs.get("metadata",{})
        )

    def to_dict(self) -> Dict[ str, Any]:
        '''转换为字典格式（标准化OpenAI API的格式）'''
        return {
            "role" : self.role,
            "content" : self.content
        }
    
    def __str__(self) -> str:
        '''字符串信息处理'''
        return f"[{self.role}] {self.content}"