#!/usr/bin/env python3
"""Check that every sentence contains at least one word/phrase from the image."""

import re
import sys

# 图中原词，去重后的扁平表（中心句式「不是……而是」单独处理）
HEDGES = [
    "不能证明", "不完全", "不足以证明", "不能仅凭", "只能证明",
    "并非", "不足以说明", "不必然", "不能只看", "不能只凭", "不能仅看",
    "不能做", "并不是", "不是说",
    "不等于", "不能据此", "不意味着", "不能确认", "不能简单", "不构成",
    "不能把", "不保证", "不一定", "不能承诺", "无法证明", "更准确地说",
    "不代表", "不能确定", "不能当作", "无法说明", "不能断定", "不能仅靠",
    "不能推出", "不能断言", "不能视为", "只能说明", "不能认定",
    "并不", "不等同于", "不证明", "并不能", "不能说明", "尚不能", "不能",
]


def hits(sentence: str) -> bool:
    if any(h in sentence for h in HEDGES):
        return True
    return "不是" in sentence and "而是" in sentence


def split_sentences(text: str):
    parts = re.split(r"[。！？!?；;\n]+", text)
    return [p.strip() for p in parts if p.strip()]


def check(text: str):
    sentences = split_sentences(text)
    missing = [(i, s) for i, s in enumerate(sentences, 1) if not hits(s)]
    return len(missing) == 0, missing


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    ok, missing = check(text)
    if ok:
        print("OK: every sentence hits at least one pattern.")
        return 0
    for i, s in missing:
        print(f"MISS sentence {i}: {s}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
