# test_reflection_agent.py
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


from dotenv import load_dotenv
from Core.llm import HelloAgentsLLM
from my_reflection_agent import MyReflectionAgent  # 导入您的 Agent

llm = HelloAgentsLLM()


load_dotenv()

code_prompts = {
    "initial": "你是Python专家，请编写函数:{task}",
    "reflect": "请审查代码的算法效率:\n任务:{task}\n代码:{content}",
    "refine": "请根据反馈优化代码:\n任务:{task}\n 上一轮回答：{last_attempt}反馈:{feedback}"
}
code_agent = MyReflectionAgent(
    name="我的代码生成助手",
    llm=llm,
    system_prompt=code_prompts
)

# 测试使用
result = code_agent.run("写一个二分法函数")
print(f"最终结果: {result}")