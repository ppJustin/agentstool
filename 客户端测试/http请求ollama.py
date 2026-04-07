import requests

response = requests.post(
    "http://localhost:8080/api/chat",  # 改用 Ollama 原生 API 端点
    json={
        "model": "llama3",  # 使用你实际下载的模型名
        "messages": [
            {"role": "user", "content": "你使用的是什么架构,用中文回答"}
        ],
        "stream": False
    }
)

# 打印结果
print(response.json()["message"]["content"])