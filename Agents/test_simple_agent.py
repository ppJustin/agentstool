

#这是对阶段性代码的简单测试文件
from dotenv import load_dotenv
from Core.llm import HelloAgentsLLM
from Code_base.registy import ToolRegistry
from Code_base.calculator import CalculatorTool
from simple_agent import MySimpleAgent

load_dotenv()       #加载环境变量



llm = HelloAgentsLLM()      #创建实例

# 测试1:基础对话Agent（无工具）
print("=== 测试1:基础对话 ===")
basic_agent = MySimpleAgent(
    name="基础助手",
    llm=llm,
    system_prompt="你是一个友好的AI助手，请用简洁明了的方式回答问题。"
)

response1 = basic_agent.run("你好，请介绍一下自己")
print(f"基础对话响应: {response1}\n")