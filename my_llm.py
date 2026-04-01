import os
from typing import Optional
from openai import OpenAI
from hello_agents import HelloAgentsLLM


class MyLLM(HelloAgentsLLM):
    #暂时留空 这是一个自定义的LLM客户端
    def __init__(
            self,
            model: Optional[str] = None, 
            api_key: Optional[str] = None,
            base_url: Optional[str] = None, 
            provider: Optional[str] = "auto",
            **kwargs
    ):
        #下面进行对于modelscope模型的供应
        if provider == "modelscope":
            print("正在使用自定义的modelscope供应")
            self.provider = "modelscope"
            #开始进行解析
            self.api_key = api_key or os.getenv("MODELSCOPE_API_KEY")
            self.base_url = base_url or os.getenv("BASE_URL_MODELSCOPE") or "https://api-inference.modelscope.cn/v1/"

            #验证凭证解析
            if not self.api_key:
                raise ValueError("ModelScope API key not found. Please set MODELSCOPE_API_KEY environment variable.")
            
            #设置模型和其他参数
            self.model = model or os.getenv("LLM_MODEL_ID") or "Qwen/Qwen2.5-VL-72B-Instruct"
            self.temperature = kwargs.get("temperature",0.7)
            self.max_tokens = kwargs.get("max_tokens")
            self.timeout = kwargs.get("timeout") or os.getenv("TIMEOUT")
            #创建OpenAI客户端实例
            self._client  = OpenAI(api_key= self.api_key,base_url= self.base_url,timeout= self.timeout)
            #这里由于modelscope兼容这个OpenAI,所以可以直接用OpenAI来创建客户端

        else:
            #这里父类HelloAgentsLLM与我们自己定义的有差别，自己的只是个简略版
            super().__init__(model= model,api_key=api_key,base_url=base_url,provider= provider,**kwargs)
