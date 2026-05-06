# test_reflection_agent.py
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


from dotenv import load_dotenv
from Core.llm import HelloAgentsLLM
from my_planandsolve_agent import MyPlanAndSolveAgent  # 导入您的 Agent

llm = HelloAgentsLLM()


load_dotenv()

code_agent = MyPlanAndSolveAgent(
    name="我的代码生成助手",
    llm=llm,

)

# 测试使用
result = code_agent.run("帮我写一个查询天气的Python代码")