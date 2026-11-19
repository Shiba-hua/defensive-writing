#!/usr/bin/env python3
"""Check that every sentence contains at least one hedge pattern from the image."""

import re
import sys

PATTERNS = [
    "这只是我看到的信息，不是完整事实",
    "这里的判断仅供参考，不构成最终结论",
    "可能存在我未掌握的信息，结论或有偏差",
    "我无法确认这一定正确",
    "目前证据不足，暂不作确定判断",
    "这只是其中一种可能，需结合更多背景判断",
    "还有其他可能解释，不能视为唯一结论",
    "以上为基于当前信息的推测，并非定论",
    "这仅基于有限经验，不能作为确定结论",
    "不同语境下可能有不同理解，以上仅为一种解释",
]


def split_sentences(text: str):
    parts = re.split(r"[。！？!?；;\n]+", text)
    return [p.strip() for p in parts if p.strip()]


def check(text: str):
    sentences = split_sentences(text)
    if not sentences:
        return True, []
    missing = []
    for i, s in enumerate(sentences, 1):
        if not any(p in s for p in PATTERNS):
            missing.append((i, s))
    return len(missing) == 0, missing


def main():
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    ok, missing = check(text)
    if ok:
        print("OK: every sentence contains at least one hedge pattern.")
        return 0
    for i, s in missing:
        print(f"MISS sentence {i}: {s}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
