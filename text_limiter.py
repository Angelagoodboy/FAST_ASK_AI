def build_limited_prompt(user_prompt: str, limit: int) -> str:
    """
    构造限制字数的 Prompt。
    """
    return (
        f"请严格限制在 {limit} 字以内回答以下问题：\n"
        f"{user_prompt}\n"
        f"请严格控制字数，不允许超过 {limit} 字。"
    )
