# my_react_agent.py
import re
from pathlib import Path
import sys
from typing import Optional
from Core.react_agent import ReActAgent
from Core.llm import HelloAgentsLLM
from Core.config import Config 
from Core.message import Message
from Code_base.registry import ToolRegistry


sys.path.insert(0, str(Path(__file__).parent.parent))


class MyReActAgent(ReActAgent):
    """
    重写的ReAct
    """

    def __init__(
        self,
        name: str,
        llm: HelloAgentsLLM,
        tool_registry: ToolRegistry,
        system_prompt: Optional[str] = None,
        config: Optional[Config] = None,
        max_steps: int = 5,
        custom_prompt: Optional[str] = None
    ):
        super().__init__(
            name, 
            llm,
            tool_registry,
            system_prompt, 
            config,
            max_steps,
            custom_prompt)
        print(f"✅ {name} 初始化完成，最大步数: {max_steps}")

    def run(self, input_text: str, **kwargs) -> str:
        """运行ReAct Agent,重写Run方法"""
        self.current_history = []
        current_step = 0

        print(f"\n🤖 {self.name} 开始处理问题: {input_text}")

        while current_step < self.max_steps:
            current_step += 1
            print(f"\n--- 第 {current_step} 步 ---")

            # 1. 构建提示词
            tools_desc = self.tool_registry.get_tools_description()
            history_str = "\n".join(self.current_history)
            prompt = self.prompt_template.format(
                tools=tools_desc,
               question=input_text,
               history=history_str
           )

            # 2. 调用LLM
            messages = [{"role": "user", "content": prompt}]
            response_text = self.llm.invoke(messages, **kwargs)

            if not response_text:
                print("❌ 错误：LLM未能返回有效响应。")
                break
            # 3. 解析输出
            thought, action = self._parse_output(response_text)
            if thought:
                print(f"🤔 思考: {thought}")
            
            if not action:
                print("⚠️ 警告：未能解析出有效的Action，流程终止。")
                break


            # 4. 检查完成条件
            if action and action.startswith("Finish"):
                final_answer = self._parse_action_input(action)
                self.add_message(Message(input_text, "user"))
                self.add_message(Message(final_answer, "assistant"))
                print(f"🎉 最终答案: {final_answer}")
                return final_answer

            # 5. 执行工具调用
            if action:
                tool_name, tool_input = self._parse_action(action)
            if not tool_name or tool_input is None:
                self.current_history.append("Observation: 无效的Action格式，请检查。")
                continue
            print(f"🎬 行动: {tool_name}[{tool_input}]")
            observation = self.tool_registry.execute_tool(tool_name, tool_input)
            print(f"👀 观察: {observation}")
            self.current_history.append(f"Action: {action}")
            self.current_history.append(f"Observation: {observation}")

        # 达到最大步数
        final_answer = "抱歉，我无法在限定步数内完成这个任务。"
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(final_answer, "assistant"))
        return final_answer


