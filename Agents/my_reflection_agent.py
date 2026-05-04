# my_react_agent.py
import re
from pathlib import Path
import sys
from typing import Optional, List, Tuple
from Core.reflection_agent import ReflectionAgent,Memory
from Core.llm import HelloAgentsLLM
from Core.config import Config 


sys.path.insert(0, str(Path(__file__).parent.parent))


DEFAULT_PROMPTS = {
    "initial": """
请根据以下要求完成任务:

任务: {task}

请提供一个完整、准确的回答。
""",
    "reflect": """
请仔细审查以下回答，并找出可能的问题或改进空间:

# 原始任务:
{task}

# 当前回答:
{content}

请分析这个回答的质量，指出不足之处，并提出具体的改进建议。
如果回答已经很好，请回答"无需改进"。
""",
    "refine": """
请根据反馈意见改进你的回答:

# 原始任务:
{task}

# 上一轮回答:
{last_attempt}

# 反馈意见:
{feedback}

请提供一个改进后的回答。
"""
}


class MyReflectionAgent(ReflectionAgent):
    """
    重写的Reflectionagent
    """
    def __init__(        
        self,
        name: str,
        llm: HelloAgentsLLM,
        system_prompt: Optional[dict[str,str]] = None,
        config: Optional[Config] = None,
        max_steps: int = 5,):

        super().__init__(llm)
        self.name = name
        self.llm = llm
        self.system_prompt = system_prompt
        self.max_steps = max_steps
        self.config = config

        if system_prompt is not None:
            self.initial_prompt = system_prompt.get("initial", DEFAULT_PROMPTS["initial"])
            self.reflect_prompt = system_prompt.get("reflect", DEFAULT_PROMPTS["reflect"])
            self.refine_prompt = system_prompt.get("refine", DEFAULT_PROMPTS["refine"])
        else:
            self.initial_prompt = DEFAULT_PROMPTS["initial"]
            self.reflect_prompt = DEFAULT_PROMPTS["reflect"]
            self.refine_prompt = DEFAULT_PROMPTS["refine"]
        
        print(f'✅{name}初始化完成，最大步数: {max_steps}')

    def run(self, task, **kwargs):

        #1.初始执行
        print(f"\n--- 开始处理任务 ---\n任务: {task}")
        initial_message = self._get_llm_response(self.initial_prompt.format(task=task))
        self.memory.add_record("execution", initial_message)

        #2.迭代执行
        for i in range(self.max_steps):
            print(f"\n--- 第 {i+1}/{self.max_steps} 轮迭代 ---")

            # a. 反思
            print("\n-> 正在进行反思...")
            last_message = self.memory.get_last_execution()
            reflect_prompt = self.reflect_prompt.format(task=task, content = last_message)
            feedback = self._get_llm_response(reflect_prompt)
            self.memory.add_record("reflection", feedback)

            # b. 检查是否需要停止
            if "无需改进" in feedback:
                print("\n✅ 反思认为代码已无需改进，任务完成。")
                break

            # c. 优化
            print("\n-> 正在进行优化...")
            refine_prompt = self.refine_prompt.format(
                task=task,
                last_attempt=last_message,
                feedback=feedback
            )
            refined_message = self._get_llm_response(refine_prompt)
            self.memory.add_record("execution", refined_message)
        
        final_message = self.memory.get_last_execution()
        print(f"\n--- 任务完成 ---\n最终生成的回答:\n{final_message}\n```")
        return final_message
    



