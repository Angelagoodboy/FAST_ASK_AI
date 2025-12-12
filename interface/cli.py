import argparse
from service.text_service import generate_limited_text


def run_cli():
    """CLI 入口：解析参数，不包含业务逻辑"""

    parser = argparse.ArgumentParser(description="DeepSeek 文本生成（带字数限制）")
    parser.add_argument("prompt", type=str, help="用户输入内容")
    parser.add_argument("--limit", type=int, default=100, help="输出字数限制")

    args = parser.parse_args()

    try:
        result = generate_limited_text(args.prompt, args.limit)
        print(result)
    except Exception as e:
        print(f"[ERROR] {e}")
