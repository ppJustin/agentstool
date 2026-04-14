#这里定义了HelloAgentsLLM的具体实现细节
import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict,List

load_dotenv()

class HelloAgentsLLM:
    '''
    基础的LLM客户端
    只能去调用兼容OpenAI接口的服务
    '''
    def __init__(self,model:str = None,apikey : str = None,baseUrl:str = None,timeout : int = None) -> None:
        #初始化客户端
        self.model = model or os.getenv("LLM_MODEL_ID")
        apikey = apikey or os.getenv("LLM_API_KEY")
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or os.getenv("LLM_TIMEOUT",60)

        if not all([self.model,apikey,baseUrl]):
            raise ValueError
        
        self.client = OpenAI(api_key=apikey,base_url=baseUrl,timeout=timeout)

    def think(self,messages:List[Dict[str,str]],temperature : float = 0) -> str:
        #成功调用大模型进行思考
        print(f"正在调用大模型{self.model}")
        try:
            response = self.client.chat.completions.create(
                 #API调用链
                model=self.model,
                messages=messages,                            #对话历史列表
                temperature=temperature,
                stream=True,                                   #是否流式逐字返回
            )
        
            #正在处理流式响应
            print("大语言模型调用成功：")
            collect_content = []
            for chunk in response:              #第1次循环: chunk = {"choices":[{"delta":{"content":"你"}}]}
                    #chunk 是一个 Pydantic 模型对象，不是字典
                content = chunk.choices[0].delta.content or ""
                print(content,end="",flush = True)
                collect_content.append(content)
            print()     #默认换行，end设置成空字符等于不换行
            return "".join(collect_content)
    
        except Exception as e:
            print(f"调用LLM API时发生错误：{e}")
            return None


#_____客户端使用示例
if __name__ == '__main__':
    try:
            llmClient = HelloAgentsLLM()

            exempleMessage = [
                {"role":"system","content":"You are a helpful assistant that whites Python code"},
                {"role":"user","content":"今天北京的天气如何"}
            ]

            print("调用LLM")
            responseTxt = llmClient.think(exempleMessage)
            if responseTxt:
                print("---完整响应--")
                print(responseTxt)

    except ValueError as e:
        print(e)
