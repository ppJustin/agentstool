# 在你的代码中运行这个看看
import sys
from pathlib import Path

# ✅ 只需要在这里加一次
sys.path.insert(0, str(Path(__file__).parent.parent))


from dotenv import load_dotenv
from Core.llm import HelloAgentsLLM
from Code_base.registy import ToolRegistry
from Code_base.calculator import CalculatorTool
from Agents.simple_agent import MySimpleAgent

load_dotenv()       #加载环境变量



llm = HelloAgentsLLM()      #创建实例

'''
# 测试1:基础对话Agent（无工具）
print("=== 测试1:基础对话 ===")
basic_agent = MySimpleAgent(
    name="基础助手",
    llm=llm,
    system_prompt="你是一个友好的AI助手，请用简洁明了的方式回答问题。"
)

response1 = basic_agent.run("你好，请详细地介绍一下自己，以及你的功能")
print(f"基础对话响应: {response1}\n")
'''



'''
# 测试2:带工具的Agent
print("=== 测试2:工具增强对话 ===")
tool_registry = ToolRegistry()      #工具注册表
calculator = CalculatorTool()       #
tool_registry.register_tool(calculator)

enhanced_agent = MySimpleAgent(
    name="增强助手",
    llm=llm,
    system_prompt="你是一个智能助手，可以使用工具来帮助用户。",
    tool_registry=tool_registry,
    enable_tool_calling=True
)

response2 = enhanced_agent.run("请帮我计算 15 * 8 + 32")
print(f"工具增强响应: {response2}\n")
'''



# 测试4:动态添加工具
basic_agent = MySimpleAgent(
    name="基础助手",
    llm=llm,
    system_prompt="你是一个友好的AI助手，请用简洁明了的方式回答问题。"
)

calculator = CalculatorTool() 
print("\n=== 测试4:动态工具管理 ===")
print(f"添加工具前: {basic_agent.has_tools()}")
basic_agent.add_tool(calculator)
print(f"添加工具后: {basic_agent.has_tools()}")
print(f"可用工具: {basic_agent.list_tools()}")

# 查看对话历史
print(f"\n对话历史: {len(basic_agent.get_history())} 条消息")