from loop.text_loop import request_once
from utils.text_limiter import build_limited_prompt


def generate_limited_text(prompt: str, limit: int) -> str:
    """
    接收用户 prompt，拼接限制字数的提示词，并调用 DeepSeek 模型。
    
    Args:
        prompt: 用户文本
        limit: 限制字数
    
    Returns:
        模型返回的文本（已限制字数）
    """
    if limit <= 0:
        raise ValueError("limit 必须大于 0")

    final_prompt = build_limited_prompt(prompt, limit)
    return request_once(final_prompt)
