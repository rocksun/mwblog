<!--
title: MiniMax Token价格减半，你的AI智能体账单可能不会变少
cover: https://cdn.thenewstack.io/media/2026/10/8cbfd8b7-silali-banerjee-azkv8asolwq-unsplash-1-scaled.jpg
summary: MiniMax发布M3.1 Flash模型并宣称降价过半、智能体成本降低70%。虽然Token单价大幅下降，但由于任务中Token消耗量波动及较高的幻觉率，其实际降本效果仍需结合具体工作负载进行评估。
-->

MiniMax发布M3.1 Flash模型并宣称降价过半、智能体成本降低70%。虽然Token单价大幅下降，但由于任务中Token消耗量波动及较高的幻觉率，其实际降本效果仍需结合具体工作负载进行评估。

> 译自：[MiniMax just halved its token prices. Your AI agent bill may not follow.](https://thenewstack.io/minimax-flash-agent-costs/)
> 
> 作者：Amanda Caswell

MiniMax周一发布了 M3.1 Flash，称其将智能体成本降低了 70%。每 Token 价格下降了一半，这占了该说法的 一部分。其余部分取决于智能体完成工作所消耗的 Token 数量，而 MiniMax 尚未说明其是如何测量这一数据的。

该[公司](https://www.minimax.io/blog/minimax-m31f)列出的价格为：每百万输入 Token 0.15 美元，每百万输出 Token 0.60 美元，每百万缓存输入 Token 0.015 美元，并声称其推理速度比上一代模型 M3 快近三倍。70% 的降幅是需要检验的数据；更便宜的费率卡只有在智能体也能以更少循环次数完成任务时才真正有用。

> 70% 的降幅是需要检验的数据；更便宜的费率卡只有在智能体也能以更少循环次数完成任务时才真正有用。

## 任务成本分析

一项[关于智能体编程任务中 Token 消耗的研究](https://arxiv.org/abs/2604.22750)发现，重复运行同一任务消耗的 Token 最多可达 30 倍，其中输入 Token 占了大部分使用量，这使得在不知晓其测试了哪些工作负载的情况下，很难评估 MiniMax 宣称的 70% 节省率。

[Artificial Analysis](https://artificialanalysis.ai/models/minimax-m3-1-flash) 提供了独立的对比。在其[公告](https://x.com/ArtificialAnlys/status/2112211865128608002)中，该公司指出 M3.1 Flash 在智能指数（Intelligence Index）任务中的平均成本为每个 0.22 美元，低于 M3 的 0.51 美元，降幅为 57%。这低于 MiniMax 宣称的 70% 的节省率，不过这两个数字来自不同的工作负载。

## 编程与电脑使用

编程得分几乎不分伯仲。M3.1 Flash 在 DeepSWE v1.1 上的得分为 73.7%，微幅落后于 MiniMax 选作对比对象的 Claude Opus 5（74%），并比 GPT-5.6 Sol 的 73% 高出一个百分点。*[VentureBeat](https://venturebeat.com/technology/minimaxs-new-m3-1-flash-beats-deepseek-and-opus-5-on-a-key-business-benchmark-at-lower-cost-but-with-a-high-hallucination-rate)* 在同一表格中将 DeepSeek V4.1 Flash 1017 列为 77 分。Anthropic 较新的 Opus 5.5 未列入该表，因此如果你要与当前的 Opus 进行基准测试，请运行你自己的评估。在 Artificial Analysis 的智能指数上，M3.1 Flash 得分为 42，与 GLM-5.3 Flash 并列，领先于 Gemini 3.8 Flash（41分），落后于 DeepSeek V4.1 Flash 1017（45分）。

> 电脑使用（Computer use）是该模型看起来最薄弱的地方。

电脑使用是该模型看起来最薄弱的地方。它在 OSWorld V2 上的得分为 61.7，MiniMax 称这在国产模型中处于领先地位，但 VentureBeat 指出它落后于最强的 Anthropic 和 OpenAI 模型。

MiniMax 还报告称其在 CyberGym 上获得 82% 的分数，并表示其内部安全专家评估该模型在代码审计、修补、渗透测试、恶意软件分析和逆向工程方面表现强劲。发布博客并未说明这些评估是如何进行的，因此在独立第三方测试之前，这些安全声明只能视为 MiniMax 的一面之词。

## 自信的回答，不确定的准确性

发布中最具影响力的发现来自 Artificial Analysis 的 AA-Omniscience 基准测试。M3.1 Flash 对事实类问题的回答正确率为 56%，领先于 DeepSeek V4.1 Flash 的 43%。

不过，它尝试了几乎每一个问题，其非正确回答中约有 93% 是错误答案，而不是选择弃权。其总体的全知（Omniscience）得分为 16。[Artificial Analysis 总结该结果](https://x.com/ArtificialAnlys/status/2112211865128608002)为：高准确率被高幻觉率所抵消。

外部分析师得出了类似的观点。[*The Decoder*](https://the-decoder.com/minimax-m3-1-flash-shows-chinas-ai-price-race-has-no-floor-in-sight/) 描述该模型会尝试回答每一个测试问题，在不确定时不会拒绝回答，因此将该模型用于知识密集型工作的企业可能需要添加验证、检索、护栏或人工审核。

## DeepSeek 的折扣何时适用

DeepSeek 是自然的对比对象。其 [V4.1 Flash 定价](https://api-docs.deepseek.com/quick_start/pricing/)在非高峰期与 MiniMax 的 0.15 美元输入和 0.60 美元输出费率相匹配。工作日协调世界时（UTC）01:00 至 04:00 以及 06:00 至 10:00 的高峰期，这些费率将翻倍，中国法定节假日除外。DeepSeek 的缓存输入成本为每百万 Token 0.003 美元，而 MiniMax 为 0.015 美元。

对于在白天工作的纽约或旧金山团队来说，大多数请求都落在 DeepSeek 的非高峰期窗口，但夜间批处理作业将落在高峰期。上述研究发现，输入 Token 占了智能体成本的大头，因此缓存费率可能比标价更重要。

## Space Bunny 与未解之谜

Space Bunny 是那个在 MiniMax 确认其为 M3.1 Flash 早期构建版之前，处理了超过 20万亿（注：原文原文为200 trillion，即200万亿） Token 的神秘模型。该版本支持一百万 Token 的上下文窗口，因此一个大型代码库可以放入单个提示词中。不过，如果你测试过预览版，不要假设其行为与正式发布版相匹配。模型在预览版和发布版之间会发生变化。

据[报道称权重将于 10 月 23 日推出](https://venturebeat.com/technology/minimaxs-new-m3-1-flash-beats-deepseek-and-opus-5-on-a-key-business-benchmark-at-lower-cost-but-with-a-high-hallucination-rate)，尽管 MiniMax 自己的文章只写了“稍后”。许可证尚未公布，对于任何考虑在自己的硬件上运行该模型的人来说，这是一个重要的考量因素。更强大的 Pro 模型也在路上，目前尚无具体日期。

> 更强大的 Pro 模型也在路上，目前尚无具体日期。