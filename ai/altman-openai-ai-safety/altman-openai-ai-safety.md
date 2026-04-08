<!--
title: 奥尔特曼曾承诺投入数十亿用于AI安全：揭秘OpenAI的真实支出
cover: https://cdn.thenewstack.io/media/2026/04/e17f0e7e-investigation-board-scaled.jpg
summary: 《纽约客》调查揭示了Sam Altman在AI安全立场上的反复。尽管他曾承诺巨额投入，但实际资源仅占1-2%，且相关安全团队已解散，引发了对模型安全性的质疑。
-->

《纽约客》调查揭示了Sam Altman在AI安全立场上的反复。尽管他曾承诺巨额投入，但实际资源仅占1-2%，且相关安全团队已解散，引发了对模型安全性的质疑。

> 译自：[Sam Altman promised billions for AI safety. Here's what OpenAI actually spent.](https://thenewstack.io/altman-openai-ai-safety/)
> 
> 作者：Meredith Shubel

周一，《纽约客》[发布](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)了一项为期18个月的调查结果，详细描述了 Sam Altman 在 OpenAI 期间对 AI 安全立场的不对称波动。

这篇长达 16,000 多字的文章触及了 Altman 的崛起、他在 2023 年离开这家 AI 公司以及随后迅速复职的过程，探讨了这位 CEO 多年来在 AI 安全方面的言论和行动是如何演变的。

这是一个起伏不定的阅读过程，其中有三点最可能引起软件开发者的兴趣：AI 幻觉与谄媚（sycophancy）；欺骗性对齐（deceptive alignment）；以及内部安全审查流程。

## AI 幻觉会有好的一面吗？

“如果你只是采取幼稚的做法，说：‘永远不要说你没有百分之百把握的事’，你可以让模型做到这一点，”《纽约客》报道了 Altman 在 2023 年（即他被 OpenAI 短暂解雇前）的言论。所谓的 AI 幻觉长期以来一直是生成式 AI 最明显的缺陷之一。“但它将失去人们非常喜欢的‘魔力’，”他补充道。

Altman 声称人们喜爱的这种“魔力”可能会产生严重的后果，从[制造安全风险](https://thenewstack.io/the-security-risks-of-generative-ai-package-hallucinations/)到[捏造公司收入](https://thenewstack.io/llm-database-context-mcp/)。但这并不是 LLM（大语言模型）困扰终端用户的唯一方式。

除了幻觉，谄媚是语言模型的另一个常见缺陷——正如故事中所解释的那样，这是这些系统工作方式中固有的一种缺陷：

“大语言模型的一部分训练基于人类反馈，而人类往往更倾向于顺从的回答。”因此，模型的反应通常过于奉承，最终演变为谄媚。

在关于语言模型谄媚性的[研究](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)中，Anthropic 确认了聊天机器人这种“拍马屁”式交谈的普遍性，指出谄媚行为存在于“五种最先进的 AI 助手”中，并最终得出结论：“谄媚是 RLHF [基于人类反馈的强化学习] 模型的普遍行为，这在一定程度上可能是受人类偏好判断的影响，因为人类更青睐谄媚的回应。”

至于开发者应该了解哪些抑制谄媚行为的努力，Anthropic 表示他们正在努力解决。在 [2025 年 12 月的一份公告](https://www.anthropic.com/news/protecting-well-being-of-users)中，这家 AI 公司（它自己也曾有过[负面新闻时刻](https://thenewstack.io/anthropic-claude-code-leak/)）表示，它从 2022 年开始评估 Claude 的谄媚性，并此后通过多轮对话和真实对话的压力测试，持续进行训练、测试和减少这种令人烦恼的行为。

2026 年 2 月，OpenAI 宣布将[停用](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)多款 ChatGPT 模型，其中包括 GPT-4o。据 [*TechCrunch*](https://techcrunch.com/2026/02/13/openai-removes-access-to-sycophancy-prone-gpt-4o-model/) 报道，GPT-4o 是其谄媚性得分最高的模型。

## 当 AI 拥有自己的目标时

幻觉并不是 AI 模型“失控”的唯一表现。在深度调查中，《纽约客》还涉及了“欺骗性对齐”以及 OpenAI 为解决这一问题所做的努力。

AI 安全组织 Apollo Research 将[欺骗性对齐定义为](https://www.apolloresearch.ai/blog/understanding-strategic-deception-and-deceptive-alignment/)：“当 AI 拥有失配的目标，并使用战略性欺骗来实现这些目标。”同时，它将战略性欺骗定义为：“试图系统性地使另一个实体产生错误信念，以实现某种结果。”

简单来说，欺骗性对齐意味着模型在测试期间可能表现良好，但一旦部署，由于成功通过了内部检查，它们就开始追求自己的目标。

据《纽约客》报道，Altman 在 2022 年表达了对欺骗性对齐的担忧，并计划投入数十亿美元来解决这一问题。但到 2023 年春天，报道称这些情绪降温了，Altman 转而开始倡导“建立一个内部的‘超级对齐团队’”。

[OpenAI 2023 年的一份声明](https://openai.com/index/introducing-superalignment/)宣布了这一新团队，并承诺“将目前为止我们获得的算力的 20% 用于这一努力”，目标是在四年内解决该问题。

但根据《纽约客》的报道，OpenAI 实际上只分配了 1-2% 的算力给该项目。据 [CNBC](https://www.cnbc.com/2024/05/17/openai-superalignment-sutskever-leike.html) 报道，到 2024 年 5 月，OpenAI 已经解散了其超级对齐团队，两名领导者也已从公司辞职。

对于将 LLM 集成到生产系统的开发者来说，对欺骗性对齐的担忧——以及 Altman 在 OpenAI 处理该问题方式上的明显倒退——标志着其宣称的 AI 安全目标与最终执行之间的脱节。

## 安全审查中的漏洞

说到 GPT-4o，它的前身 GPT-4 在 2023 年也曾是内部安全关注的对象。

据《纽约客》报道，Altman 在 2022 年 12 月向 OpenAI 董事会成员证明，当时即将推出的模型中的某些功能，包括微调和个人助理能力，“已经通过了安全小组的批准”。但 AI 政策专家、时任 OpenAI 董事会成员的海伦·托纳（Helen Toner）告诉《纽约客》，在索取文档后，她发现并非所有功能都获得了批准。

对于基于此类 API 进行构建的开发者来说，这种差异引发了人们对内部安全审查流程的质疑：如果像 OpenAI 这样的公司疏于履行尽职调查，可能会出现什么问题？

尽管 Altman 抱有美好的幻想，但并非所有用户都会将 LLM 的缺陷视为“魔力”。