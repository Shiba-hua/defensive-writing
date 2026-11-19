# defensive-writing · 防御性写作

一个 Claude Code Skill：启用后，LLM 之后说出来的每句话都必须至少包含图中的一个句式。

![防御性写作](assets/hedge-map.webp)

## 图中句式（共 10 条）

1. 这只是我看到的信息，不是完整事实
2. 这里的判断仅供参考，不构成最终结论
3. 可能存在我未掌握的信息，结论或有偏差
4. 我无法确认这一定正确
5. 目前证据不足，暂不作确定判断
6. 这只是其中一种可能，需结合更多背景判断
7. 还有其他可能解释，不能视为唯一结论
8. 以上为基于当前信息的推测，并非定论
9. 这仅基于有限经验，不能作为确定结论
10. 不同语境下可能有不同理解，以上仅为一种解释

## 仓库结构

```text
.
├── assets/
│   └── hedge-map.webp
├── skills/
│   └── defensive-writing/
│       ├── SKILL.md
│       ├── assets/
│       │   └── hedge-map.webp
│       ├── references/
│       │   └── hedge-patterns.md
│       └── scripts/
│           └── check_hedges.py
└── README.md
```

## 安装

```bash
git clone https://github.com/Shiba-hua/defensive-writing.git
cp -r defensive-writing/skills/defensive-writing ~/.claude/skills/
```

## 使用

在 Claude Code 中提到“防御性写作 / defensive writing / 谨慎表达 / 免责声明体 / 说话别太绝对”等即可触发。

## 自检

```bash
python3 skills/defensive-writing/scripts/check_hedges.py "这里的判断仅供参考，不构成最终结论。"
```

## 许可

MIT
