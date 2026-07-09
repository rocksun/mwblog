<!--
title: 让 Claude 说“原始人语”可能并没有你想象中那么节省 Token
cover: https://cdn.thenewstack.io/media/2026/07/a7a3e7c7-tri-wiranto-cnyq0g8-ewk-unsplash-scaled.jpg
summary: 随着 AI 开发工具成本上升，开发者尝试用原始人语模式压缩回复以节省 Token。然而，JetBrains 测试显示，该方法在实际编程任务中的节约效果仅为 8.5%，远低于声称的 65%，且对模型推理能力无明显影响。
-->

随着 AI 开发工具成本上升，开发者尝试用原始人语模式压缩回复以节省 Token。然而，JetBrains 测试显示，该方法在实际编程任务中的节约效果仅为 8.5%，远低于声称的 65%，且对模型推理能力无明显影响。

> 译自：[Getting Claude Code to grunt in Caveman-speak might not save as many tokens as you think](https://thenewstack.io/caveman-mode-token-savings/)
> 
> 作者：Paul Sawers

开发者们正愈发关注 AI 编程工具的运行成本，这不无道理。GitHub 最近将 Copilot 转为基于所选模型的按量计费模式，而另一家 AI 代理初创公司则表示，[从 Anthropic 切换到 DeepSeek](https://thenewstack.io/lindy-deepseek-anthropic-switch/) 能为公司节省数百万美元。

在此背景下，开发者们一直在寻找通过减少 AI 回复中冗余填充和填充内容来降低 Token 消耗的方法。最终目标是让代理尽可能直接地回答，在尽可能少的字数内完成任务，同时不丢失任何实质内容。这似乎被称为“原始人模式”——放弃冠词和语法，转而使用简短、生硬的片段，模仿老情景喜剧和卡通中刻板的咕哝原始人风格。

事实上，一些开发者可能从 [The Grug Brained Developer](https://grugbrain.dev/) 中认出这一点。这是一篇由 [htmx](https://htmx.org/) 的创建者 [Carson Gross](https://bigsky.software/cv/) 撰写的关于软件设计的长文，全文完全使用这种断断续续、生硬的风格。但这一次，目标不是代码复杂度，而是 AI 回复中的冗余。

## “技能让代理像原始人一样说话”

这个想法以不同的形式出现。企业搜索巨头 Elastic 为 Elasticsearch 构建了自己的版本，报告称在八个内部测试场景中平均减少了 63.6% 的 Token。

Elastic 的 Salesforce 工程总监 [Sri Kolagani](https://www.linkedin.com/in/sriharideep/) [在四月份的一篇博客文章中写道](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)，LLM 在回答周围包裹的对话式填充内容在查询 Elasticsearch 时带来了实际成本，而你真正需要的是索引名称、字段映射和 ES|QL 查询，而不是客套话。

“这不仅仅是令人讨厌，而且代价高昂，”Kolagani 写道。“每一个 Token 都要花钱并增加延迟。对于生产环境的 Elasticsearch 查询，这种开销会迅速累积。”

然而，真正走红的工具是由荷兰开发者 [Julius Brussee](https://www.linkedin.com/in/julius-brussee/) 在 [GitHub](https://github.com/juliusbrussee/caveman) 上构建的一个免费、可安装的 Claude Code 技能。它获得了数万个星标和 Fork，并在 [Hacker News](https://news.ycantorator.com/item?id=47647455) 等在线社区引发了头版讨论。

> “这不仅仅是令人讨厌，而且代价高昂。每一个 Token 都要花钱并增加延迟。对于生产环境的 Elasticsearch 查询，这种开销会迅速累积。”

其宣传语（用它自己的原始人语言）：

“技能让代理像原始人一样说话。为什么用多 Token，少用就行。填充物死掉。代码，命令保持字节精确。”

它的头条主张？减少 65% 的输出 Token。

## 原始人对话的节省效果，经受检验

[JetBrains](https://www.jetbrains.com/)（包括 IntelliJ 和 Rider 在内的 IDE 背后的公司）决定测试该特定技能，而不是照单全收其 65% 的节省宣传。

JetBrains 的工程师 [Denis Shiryaev](https://www.linkedin.com/in/dshiryaev/) [在七月份的一篇博客文章中写道](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)，他们使用 [Harbor](https://www.harborframework.com/)（一个开源代理评估框架）和来自 [SkillsBench](https://www.skillsbench.ai/)（一个旨在衡量 AI 代理技能实际帮助程度的社区基准）的任务，在 Claude Code 上针对 86 个真实编码任务运行了配对基准测试，比较了启用该技能与未修改的会话。

宣传与结果之间的差距并不小。广告称节省：65%。JetBrains 实际测得：8.5%，这一数字只有在测试规模扩大后才稳定下来。事实上，早期对 10 个任务的测试最初显示更接近 30%。

这一差距最终归结为该技能在真实编码项目中能处理和不能处理的内容，与它测量 headline 数字时所用的那种随意聊天交流之间的区别。

> “广告中的节省来自聊天式的散文回答。代理输出是不同的。”

“广告中的节省来自聊天式的散文回答。代理输出是不同的，”Shiryaev 写道，并指出代码、差异、工具调用和精确的错误字符串主导了 Token 流，而该技能对此类内容保持原样。“只有工具调用之间的叙述被压缩了，而且内容并不多，”他补充道。

## 像穴居人一样说话会让 Claude 变笨吗？

这是该技能刚走红时几乎立即出现的一个担忧，[Reddit 上的评论者](https://www.reddit.com/r/ClaudeAI/comments/1sble09/taught_claude_to_talk_like_a_caveman_to_use_75/)担心，强迫 AI 模型以一种精简、表达能力较差的语调回答，可能会牺牲其推理能力。

JetBrains 的基准测试表明，这种担忧并不成立，至少在它测试的任务中是这样。在 86 次配对运行中，启用技能和常规会话的任务结果在统计上没有区别。

Shiryaev 对“原始人模式”的总体评价是：它是“安全的，风格上是诚实的，但在节省方面夸大其词”。

“如果你喜欢就用吧，”Shiryaev 在那篇博客文章中写道。“它很有趣，而且在质量上不会让你付出任何可衡量的代价。只是不要指望在日常代理任务中节省巨大开支：个位数的百分比是现实的上限。”