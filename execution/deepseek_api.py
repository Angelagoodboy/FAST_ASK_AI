import requests
import os

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"


def call_deepseek(prompt: str) -> str:
    """
    执行层：只负责执行 DeepSeek API 调用，不做任何逻辑处理。
    """
    if DEEPSEEK_API_KEY is None:
        raise RuntimeError("请设置环境变量 DEEPSEEK_API_KEY")

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        API_URL,
        json=payload,
        headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]
