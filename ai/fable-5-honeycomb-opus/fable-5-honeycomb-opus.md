<!--
title: Anthropic再次延长Fable 5免费期，并对Cursor中发现的新模型保持沉默
cover: https://cdn.thenewstack.io/media/2020/09/0b3d6f97-glitch-2463383_1280.jpg
summary: Anthropic再次延长Claude Fable 5的免费试用期至7月19日，但因未重置使用额度引发用户不满。同时，疑似名为Claude Honeycomb的神秘模型在Cursor中短暂曝光，引发社区对其即为Claude Opus 5的猜测。
-->

Anthropic再次延长Claude Fable 5的免费试用期至7月19日，但因未重置使用额度引发用户不满。同时，疑似名为Claude Honeycomb的神秘模型在Cursor中短暂曝光，引发社区对其即为Claude Opus 5的猜测。

> 译自：[Anthropic extends Fable 5 again — and won't talk about what developers found inside Cursor](https://thenewstack.io/fable-5-honeycomb-opus/)
> 
> 作者：Amanda Caswell

Anthropic 已将其付费订阅用户对 Claude Fable 5 的增强访问权限延长至 7 月 19 日，这是五周内的第三次延期。该公司在周日晚间，即前一个截止日期到期的前几个小时宣布了这一举措。

此决定是在人们对 Anthropic 下一个重大模型发布的猜测日益增长之际做出的。本周早些时候，一个名为“Claude Honeycomb EAP”的未发布模型曾在 Cursor 中短暂出现，这助长了社区关于 Opus 5 可能在本月底前推出的理论。

## Fable 5 免费访问权限延长

Pro、Max、Team 以及符合条件的 Enterprise 计划订阅用户可以在 7 月 19 日太平洋时间晚上 11:59:59 之前，继续以不超过每周使用配额 50% 的额度免费使用 Fable 5，无需额外付费。Anthropic 还将 Claude Code 每周费率限制的 50% 临时提升延长至同一日期。

促销结束后，Fable 5 的使用费将按每百万输入 token 10 美元和每百万输出 token 50 美元计费，这与 Anthropic 最昂贵的层级持平。

## 用户要求重置使用额度

由于 Anthropic 在不重置用户 Fable 5 配额的情况下再次延长促销期，用户感到越来越沮丧。在 Reddit 的讨论帖中，订阅用户表示，如果他们已经耗尽了包含的使用量，那么再提供一周的访问权限几乎没有什么好处。

许多用户将 Anthropic 的做法与 OpenAI 进行了对比（后者在服务中断或出现意外需求后偶尔会重置使用上限），并认为重置配额将使他们在每次延期期间有更好的机会测试该模型。一些用户表示，缺乏重置功能正促使他们去尝试竞争对手的模型。

## 仍未永久恢复

在美国商务部于 6 月 30 日取消限制后，Anthropic 于 7 月 1 日恢复了对 Fable 5 的访问，将免费期延长至 7 月 7 日，同时引入了 50% 的每周使用上限。在该截止日期到期前几小时，该公司将优惠推迟至 7 月 12 日。随后，在周日晚上，它又做了一次，将免费访问期限延长至 7 月 19 日。

这些反复的延期本身已经成为一个故事。Anthropic 于 6 月 9 日推出了 Claude Fable 5，最初提供的免费访问期至 6 月 22 日。然而，仅仅三天后，该计划就因出口管制指令被迫在 6 月 12 日在全球范围内禁用了 Fable 5 和 Mythos 5，从而陷入混乱。

Claude Code 首席工程师 Thariq 曾表示，一旦公司拥有足够的计算能力，Anthropic 打算将 Fable 5 作为一项标准订阅福利带回。然而，Anthropic 尚未提供具体时间表，并且经过五周的滚动延期后，该模型在临时优惠到期后仍会回退到预付费使用积分模式。

## Honeycomb EAP 短暂浮出水面

还有迹象表明 Anthropic 可能还有另一个模型在酝酿之中。7 月 8 日，开发者 @chetaslua 在 Cursor 的模型选择器中发现了一个名为 Claude Honeycomb EAP 的未知模型。

该列表在几个小时内消失，但该开发者分享的屏幕截图在 X、Hacker News 和开发者论坛上流传开来。

图像似乎显示 Honeycomb 将某些敏感提示路由至 Claude Opus 4.8，而不是直接处理它们。Anthropic 既未证实也未否认此次泄露，且该模型并未出现在公司的公共 API 或文档中。

该早期访问模型被描述为具有逐轮控制、安全回退、一百万 token 上下文窗口以及“超高努力（extra high effort）”推理模式的 Anthropic 研究模型。据报道，在它被移除之前，只运行了两个提示。

引起开发者注意的是它的安全行为。根据泄露的列表，敏感提示被路由至 Claude Opus 4.8，而不是直接处理。Anthropic 已经为 Fable 5 记录了一种类似的回退机制，即某些网络安全请求会自动路由至 Opus 4.8。如果 Honeycomb 向下路由至 Opus 4.8，许多开发者认为这表明该未发布模型在能力上位于其之上。

## Honeycomb 的竞争风险很高

这一理论之所以受到关注，是因为 Honeycomb 泄露的规格与已发布的 Fable 5 架构非常吻合，包括自适应思维、一百万 token 上下文窗口以及 Opus 4.8 安全回退。一些开发者现在推测 Honeycomb EAP 是 Claude Opus 5 的早期预览版，可能会在 7 月底前发布。

虽然 Fable 5 在诸如 SWE-bench Pro 等存储库级编码基准测试中仍保持着最强的已发布结果，但包括 OpenAI 的 GPT-5.6 Sol 和 xAI 的 Grok 4.5 在内的竞争对手，现在正以极低的价格瞄准同样的高端开发者市场。

这给 Anthropic 带来了压力。如果 Honeycomb 最终成为 Claude Opus 5，它将需要提供显著的性能优势——或者更具竞争力的定价策略——才能证明 Fable 5 高昂成本的合理性。

> Honeycomb 将需要提供显著的性能优势——或者更具竞争力的定价策略——才能证明 Fable 5 高昂成本的合理性。

当目前的促销活动在 7 月 19 日到期时，Fable 5 的使用将切换到 Anthropic 的预付费积分系统。按每百万输入 token 10 美元和每百万输出 token 50 美元计算，它是该公司目前最昂贵的通用模型。相比之下，Claude Opus 4.8 的价格为每百万输出 token 25 美元。

降低这些成本是有方法的。提示缓存（Prompt caching）可将缓存输入 token 的价格降低 90%，而 Anthropic 的批处理 API（Batch API）则为不需要立即响应的作业将输入和输出定价减半。对于计划内或离线工作负载，这有效地使 Fable 5 的定价与 Opus 4.8 持平。

最高的成本出现在长时间运行的代理工作流中。Fable 5 专为诸如扩展编码会话、大规模文档分析和多步研究等任务而构建，具有一百万 token 的上下文窗口和高达 [128,000 输出 token](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5#:~:text=up%20to%20128k%20output%20tokens%20per%20request.) 的能力。这些工作负载可能会产生大量输出，导致成本增加的速度比短对话式聊天快得多。

对于不需要这些功能的用户来说，Claude Sonnet 5 是一个成本低得多的替代方案。Anthropic 目前的默认模型在 2026 年 8 月 31 日之前，每百万输入 token 收费 2 美元，每百万输出 token 收费 10 美元，之后将分别增加到 3 美元和 15 美元。虽然它缺乏 Fable 5 的一百万 token 上下文窗口和最大输出限制，但它在大多数日常编码和推理任务中表现出色。