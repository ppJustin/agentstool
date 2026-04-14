import requests

response = requests.post(
    "http://10.2.14.79:8002/v1/chat/completions",
    json={
        "model": "Qwen/Qwen1.5-0.5B-Chat",
        #这里如果使用的是绝对路径的话要加上请求头
        #"model": "/home/pzj/.cache/huggingface/hub/models--Qwen--Qwen1.5-0.5B-Chat/snapshots/4d14e384a4b037942bb3f3016665157c8bcb70ea/",
        "messages": [
            {"role": "user", "content": "今天北京的天气如何"}
        ],
        "max_tokens": 100
    }
)

print(response.json()["choices"][0]["message"]["content"])