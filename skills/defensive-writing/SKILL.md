---
name: defensive-writing
description: "防御性写作模式。启用后要求每一句输出都至少包含图中的一个防御性句式。Use when user asks for 防御性写作, defensive writing, 谨慎表达, 免责声明体, 模糊表述, 不确定性表达, 每句话加免责, 说话留余地, hedge every sentence, cautious wording, or to speak in hedged/defensive style. Triggers: 防御性写作, 防御性表达, 免责声明, 谨慎表达, 不确定, 留余地, hedge, hedging, defensive writing, 说话别太绝对, 模糊一点."
---

# 防御性写作

IRON LAW: 之后输出的每一句话，都必须至少包含下列 10 条句式中的至少 1 条。没有句式的句子不允许出现。

## 句式表（仅限图中句式）

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

详见 [references/hedge-patterns.md](references/hedge-patterns.md)。配图见 [assets/hedge-map.webp](assets/hedge-map.webp)。

## 执行规则

- 只使用以上 10 条句式，不自行添加、改写或扩展。
- 输出前将内容拆成独立句子/条目；每一句（含标题、列表项、表格单元中的独立表述）都必须包含至少 1 条句式原文。
- 将句式原样嵌入句中或紧邻该句，保证该句文本命中句式字符串。
- 交付前逐句自检；可用脚本检查：

```bash
python3 scripts/check_hedges.py "要检查的文本"
```
