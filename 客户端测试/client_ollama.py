from hello_agents import HelloAgentsLLM

llm_client = HelloAgentsLLM(
    provider="ollama",
    model="llama3",
    base_url="http://localhost:8080/v1",  # 加上 http://
    api_key="ollama"                        #本地无需api_key
)

# 测试调用
response = llm_client.think(        #返回的一个生成器对象
    messages=[{"role": "user", "content": "你好，请简单介绍一下你自己"}]
)

for chunk in response:
    pass