# defensive-writing · 防御性写作

一个 Claude Code Skill：启用后，LLM 之后说出来的每一句话都必须至少命中图中词表的一个词/短语。

![防御性写作](assets/hedge-map.webp)

## 词表（图中原词）

- **中心**：不是……而是
- **外围六区块**：不能证明（不完全、不足以证明、不能仅凭、只能证明）；并非（不足以说明、不必然、不能只看、不能只凭、不能仅看、不能做、并不是、不是说）；不等于（不能据此、不意味着、不能确认、不能简单、不构成）；不能·底（不能把、不保证、不一定、不能承诺、无法证明、更准确地说）；不代表（不能确定、不能当作、无法说明、不能断定、不能仅靠）；不能·左上（不能推出、不能断言、不能视为、只能说明、不能认定）
- **中间过渡**：并不、不等同于、不证明、并不能、不能说明、尚不能、不能

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

提到“防御性写作 / defensive writing / 谨慎表达 / 说话别太绝对”等即可触发；启用后每句话必须命中词表至少 1 个词条。

## 自检

```bash
python3 skills/defensive-writing/scripts/check_hedges.py "样本文本。"
```

## 许可

MIT
