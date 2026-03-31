
from hello_agents import SimpleAgent, HelloAgentsLLM
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 无指定自动检测provider，从环境变量中寻找
llm = HelloAgentsLLM()



# 创建SimpleAgent
agent = SimpleAgent(
    name="AI助手",
    llm=llm,
    system_prompt="你是一个有用的AI助手"
)

# 对话
response = agent.run("你好！请介绍一下自己")
print(response)

# 工具模块
from hello_agents.tools import CalculatorTool
calculator = CalculatorTool()


print(response)

# 查看对话历史
print(f"历史消息数: {len(agent.get_history())}")
