from execution.deepseek_api import call_deepseek


def request_once(prompt: str) -> str:
    """
    Loop 层：执行一次 API 请求，未来可以加入重试或批处理。
    """
    return call_deepseek(prompt)
