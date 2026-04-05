import requests

response = requests.post(
    "http://10.2.14.79:8002/v1/chat/completions",
    json={
        "model": "Qwen/Qwen1.5-0.5B-Chat",
        "messages": [
            {"role": "user", "content": "请帮我写一个Python算法"}
        ],
        "max_tokens": 100
    }
)

print(response.json()["choices"][0]["message"]["content"])