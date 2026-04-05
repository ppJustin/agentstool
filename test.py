#专属main函数来测试MyLLM函数
from dotenv import load_dotenv
from my_llm import MyLLM

load_dotenv()

#实例化MyLLM类
llm = MyLLM(provider="modelscope")

#准备消息
messages = [{"role":"user","content":"你好，介绍一下你自己"}]

#开始调用模型，父类定义的方法无需重写
response = llm.think(messages)          #这里response是一个构造器

#打印响应
print("ModelScope Response:")

'''
定义的think方法返回的是一个构造器，为了进行流式相应，所以这里需要对构造器进行遍历来执行结果
'''
for chunk in response:
    pass