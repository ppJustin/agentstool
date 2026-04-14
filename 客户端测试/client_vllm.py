from hello_agents import HelloAgentsLLM

llm_client = HelloAgentsLLM(
    provider="vllm",
    #使用绝对路径
    model="/home/pzj/.cache/huggingface/hub/models--Qwen--Qwen1.5-0.5B-Chat/snapshots/4d14e384a4b037942bb3f3016665157c8bcb70ea/",
    #model="Qwen/Qwen1.5-0.5B-Chat",
    base_url="http://10.2.14.79:8002/v1",  # 加上 http://
    api_key="vllm"
)

# 测试调用
response = llm_client.think(        #返回的一个生成器对象
    messages=[{"role": "user", "content": "你好，请详细地介绍一下你自己"}]
)

for chunk in response:
    pass