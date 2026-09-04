<!--
title: Meta编程助手Muse Code结束测试：推出三档订阅方案，主打极致性价比
cover: https://cdn.thenewstack.io/media/2026/09/93db7838-tri-wiranto-gfv_lfaayac-unsplash-scaled.jpg
summary: Meta正式发布编程助手Muse Code，引入三档月度订阅套餐，以高性价比与Claude Code和Codex竞争。新版本增加了跨会话消息、工作流调度及撤回功能，并推出SDK支持第三方开发，旨在通过更灵活的定价与功能扩展占领市场。
-->

Meta正式发布编程助手Muse Code，引入三档月度订阅套餐，以高性价比与Claude Code和Codex竞争。新版本增加了跨会话消息、工作流调度及撤回功能，并推出SDK支持第三方开发，旨在通过更灵活的定价与功能扩展占领市场。

> 译自：[Meta's Claude Code rival exits beta with three new subscription tiers — and it's pushing hard on price](https://thenewstack.io/muse-code-sdk-pricing/)
> 
> 作者：Paul Sawers

**Meta [已正式](https://developer.meta.com/ai/resources/blog/muse-code-new-plans-and-features/) 发布 [Muse Code](https://developer.meta.com/ai/products/muse-code/) 并结束测试阶段**，此时距离该编程代理首次 [亮相](https://thenewstack.io/meta-muse-code/) 还不到一个月。

除了提供大量新功能和一个 SDK 外，Meta 还引入了三款新的订阅计划，价格从每月 5 美元到 50 美元不等，为该产品增加了可预测的月度定价，而该产品在发布之初就因大幅低于竞争对手的编程代理价格而脱颖而出。

Muse Code 由 Meta 自家的 [Muse Spark 1.2 模型](https://developer.meta.com/ai/models/muse-spark/) 驱动，实际上是 Meta 对 Anthropic 的 Claude Code 和 OpenAI 的 Codex 的回应：这是一个基于终端的编程代理，旨在处理大型代码库中的复杂软件工程任务。

在最初的版本中，Muse Code 就已经包含了异步后台代理，这些代理在整个编码会话中保持活跃，以收集信息并支持主要代理。Meta 还将其宣传为能够处理大型存储库中长期工程任务的工具，从规划变更到编写和验证代码均可覆盖。

在正式公开发布版本中，Meta 增加了几项新功能。其中之一是会话间消息传递，当多个 Muse Code 会话的工作重叠时，它们可以直接共享上下文和状态。

![Muse Code 中的会话间消息传递](https://cdn.thenewstack.io/media/2026/09/7b600f4b-gif-1-1intersessionmessaging.gif)

*Muse Code 中的会话间消息传递*

除此之外，Meta 还引入了工作流（Workflows），它建立在现有的多代理功能之上，通过协调专业代理团队来完成更大规模的任务，在不同阶段之间传递中间工作，并在最后返回单个结果。开发人员还可以通过专门的工作流控制室监控和引导这些代理。

另一个值得注意的补充是撤回功能，它允许开发人员将对话和代码更改回滚到 Muse Code 会话中的早期时间点。

![Muse Code 中的撤回功能](https://cdn.thenewstack.io/media/2026/09/905a22b7-rewindgif.gif)

*Muse Code 中的撤回功能*

## 定价因素

Muse Code 在发布时最具争议的方面之一是其定价设置。当时，Meta 提供了两种按量付费层级。其标准层级的收费标准为每百万输入 Token 1.25 美元，每百万输出 Token 4.25 美元，而所谓的“贡献者”层级将这些费率分别大幅削减至 0.10 美元和 0.20 美元。当然，其中的隐患在于，贡献者用户必须同意将其提示词和完成内容用于帮助改进 Meta 的产品，一些工程主管在当时 [告诉 *The New Stack*](https://thenewstack.io/meta-muse-code/)，这一权衡将使其无法用于他们的专有代码。

> “Muse Code 在发布时最具争议的方面之一是其定价设置。”

然而，价格并不能说明全部情况。*The New Stack* 曾让 Muse Code 和 Claude Code [执行相同的三个编程任务](https://thenewstack.io/meta-muse-claude-code/)。虽然 Muse Code 的成本要低得多，但它消耗了更多的 Token，并且在重构任务上产生了较弱的结果，在另一个任务中还留下了死代码。这引发了一个更广泛的问题，即其价格在多大程度上真正反映了完成有用工作的成本。

随着正式发布，Meta 在现有的按量付费选项之外，引入了三档订阅层级。

日常使用计划（Everyday Usage）每月 5 美元；高频使用计划（High Usage）每月 15 美元，承诺提供三倍的使用量；而 50 美元的重度使用计划（Power Usage）则提供 10 倍的使用量。Meta 表示，5 美元的计划通常每 5 小时提供 10 到 50 次请求，具体数量取决于工作的复杂程度。

![Muse Code 订阅定价](https://cdn.thenewstack.io/media/2026/09/77b02204-pricingtier-1024x391.webp)

*Muse Code 订阅定价*

这使得 Muse Code 的标称订阅价格远低于其主要竞争对手。Anthropic 将 Claude Code 包含在每月 20 美元的 Pro 计划中，而其 100 美元的 Max 5x 和 200 美元的 Max 20x 计划分别提供 Pro 计划单会话使用量的 5 倍和 20 倍。OpenAI 也采取了类似的方法：Codex 包含在 20 美元的 Plus 计划中，而其 100 美元和 200 美元的 Pro 层级分别提供 Plus 使用量的 5 倍和 20 倍。

然而，这些计划实际购买的编程工作量更难比较。Anthropic 目前并未公布 Pro、Max 5x 或 Max 20x 的具体 Claude Code 提示词数量；相反，它将两个 Max 额度表示为 Pro 的倍数。它还实施了五小时和每周的使用限制。另一方面，OpenAI 在 [其定价页面](https://learn.chatgpt.com/docs/pricing) 上提供了一些帮助：对于 GPT-5.6 Sol，它估计在 Plus 计划下每五小时可进行 10–100 次本地 Codex 消息交互；Pro 5x 为 50–500 次；Pro 20x 为 200–2,000 次。即便如此，OpenAI 表示实际使用量会随模型、任务复杂性、上下文、推理和工具等因素而变化，因此 Meta 的 10 到 50 次请求估计仍然无法直接进行简单对比。

> “在经历了 Claude 和 ChatGPT 的使用限制风波后，这显得简单得让人耳目一新。”

高级机器学习工程师 [Muhammad Navaid](https://www.linkedin.com/in/mnavaidd/) 周二在社交媒体上强调了 Meta 比例定价结构的简单性，即每次价格上涨都直接对应于广告宣传的使用量增长。“在经历了 Claude 和 ChatGPT 的 [使用限制风波](https://thenewstack.io/claude-code-usage-limits/) 后，这显得简单得让人耳目一新，” 他在 [LinkedIn 上写道](https://www.linkedin.com/feed/update/urn:li:activity:7500515585143844864/)。“老实说，AI 编程订阅就应该这样运作。”

其他人对如此低的价格最终意味着什么则不那么热情。Msty AI 的联合创始人兼首席执行官 [Ashok Gelal](https://www.linkedin.com/in/ashokgelal/) 将这种定价描述为“低得难以置信”，但暗示了伴随 Muse Code 最初发布的数据担忧。

“这里最大的担忧是 Meta 本身，” Gelal 在 X 上 [写道](http://x.com/ashokgelal/status/2094517356349333543)。

## 基于 Muse Code 进行构建

虽然新的订阅改变了开发人员为 Muse Code 付费的 *方式*，但公开发布的另一个方面扩展了他们可以用它做什么。一个目前处于开发人员预览阶段的 [新 SDK](https://github.com/meta-models/muse-code-sdk)，将 Muse Code 的功能扩展到了命令行界面之外。

在 [X 上的一篇帖子](https://x.com/finkd/status/2094500475710099945?s=20) 中，Mark Zuckerberg 指出，其目标是使开发人员能够基于 Muse Code 构建自己的代理。

“将它们嵌入到你的应用程序中，连接自定义工具，流式传输进度，并稍后恢复会话，” Zuckerberg [写道](https://x.com/finkd/status/2094500479866736747?s=20)。

在实际层面上，该 SDK 允许开发人员以编程方式控制 Muse Code——这意味着他们自己的软件可以启动和恢复会话、发送指令、处理响应并对代理的操作做出反应，而不是需要某人通过终端手动操作 Muse Code。这可以支持从 IDE 集成和内部工程工具到基于 Muse Code 构建的独立代理产品的一切应用。

Meta 在这方面并不孤单。Anthropic 的 [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) 同样允许开发人员围绕 Claude Code 的功能构建应用程序，而 OpenAI 提供了一个 [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk)，用于将其编程代理嵌入到其他工具和服务中。

Meta 还发布了 Muse 会话协议 ([MSP](https://github.com/meta-models/muse-code-sdk/tree/main/schema/msp))，这是外部客户端用于与 Muse Code 会话通信的底层协议。开发人员可以使用 Meta 的 TypeScript SDK 或直接用其他语言实现 MSP。

更广泛的意义可能在于，Meta 向第三方开发开放 Muse Code 的速度之快。在 CLI 测试版发布不到一个月后，它就已经为开发人员提供了将 Muse Code 嵌入到他们自己的界面、应用程序和代理中的工具。

Meta 之所以行动迅速，是因为它不得不这么做。Claude Code 和 Codex 已经占据了先发优势，这让 Muse Code 在价格和功能上不得不进行激烈的竞争。