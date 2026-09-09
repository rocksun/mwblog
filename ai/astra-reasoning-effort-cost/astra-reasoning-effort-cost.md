<!--
title: OpenAI新模型Token单价上涨2.5倍，为何开发者反而节省了成本？
cover: https://cdn.thenewstack.io/media/2026/09/981dfc43-second-breakfast-dkvcldi20oi-unsplash-scaled.jpg
summary: 尽管OpenAI新模型GPT-6 Astra的Token单价上涨2.5倍，但因其推理效率更高，能通过更少的步骤完成任务，反而帮助开发者降低了总运营成本，证明了模型推理能力与成本之间的动态平衡。
-->

尽管OpenAI新模型GPT-6 Astra的Token单价上涨2.5倍，但因其推理效率更高，能通过更少的步骤完成任务，反而帮助开发者降低了总运营成本，证明了模型推理能力与成本之间的动态平衡。

> 译自：[OpenAI's new model costs 2.5x more per token — and developers are saving money anyway](https://thenewstack.io/astra-reasoning-effort-cost/)
> 
> 作者：Amanda Caswell

GPT-6 Astra 对考虑从 GPT-5.6 Sol 升级的开发者来说有一个明显的问题：它的 Token 成本高出 2.5 倍，但 OpenAI 认为许多开发者仍然应该升级，然后调低推理设置。

OpenAI 的 [Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/)（Codex 工程主管）[周末在 X 上发帖](https://x.com/thsottiaux)表示：“为了让大家校准在 Astra 上使用哪种推理力度，请了解 GPT-6 Astra 在低（low）设置下的表现优于 GPT-5.6 Sol 的高（high）设置。”

[Artificial Analysis](https://artificialanalysis.ai/models/gpt-6-astra-low) 目前给 Astra-low 在其智能指数（Intelligence Index）上打出了 49 分，略高于 [Sol-high 的 48 分](https://artificialanalysis.ai/models/gpt-5-6-sol-high)。Astra-low 的响应速度也快得多，首个 Token 的生成时间为 2.53 秒，而 Sol-high 为 11.87 秒。

> “为了让大家校准在 Astra 上使用哪种推理力度，请了解 GPT-6 Astra 在低（low）设置下的表现优于 GPT-5.6 Sol 的高（high）设置。”

## 推理力度改变成本

Astra 的价格为 [每百万输入 Token 10 美元，每百万输出 Token 50 美元](https://openai.com/index/gpt-6-astra/)，而 Sol 的现行价格分别为 4 美元和 20 美元。将推理拨盘从“高”调到“低”并不会改变这些费率，但它可能会改变在任务最终完成之前所做的工作量，这也是 [OpenAI 在其迁移指南中明确提出](https://developers.openai.com/api/docs/guides/latest-model)的一个论点。该公司表示，Astra 可以在使用大幅减少输出 Token 的同时产生更强的结果。

OpenAI 以自己的基准测试作为证明。该公司在 [Terminal-Bench 4.0](https://openai.com/index/gpt-6-astra/) 中发现了同样的模式，Astra 得分为 57.9%，而 Sol 为 37.3%，但每个任务的成本仍降低了约 9%。在 GPQA Diamond 基准测试中，差距甚至更大：Astra 以 94.9% 对 94.6% 的成绩小幅领先 Sol，估计成本降低了 37%。

现实世界的工作负载会有所不同，但结果表明，仅凭每 Token 定价并不能告诉开发者模型实际运行的成本是多少——这是一个 OpenAI [已经在探索基于结果定价](https://thenewstack.io/openai-outcome-based-pricing/)的理念。

## 更少的 Token，更廉价的任务

开发者 [Shinpr](https://dev.to/shinpr/switching-from-gpt-56-sol-to-gpt-6-astra-start-with-medium-effort-25ao) 在相同的代码库上进行了对比，分别使用了 Sol-high 和几种 Astra 推理级别，涵盖分析、实现和审查。

Astra-medium 在时间和成本上表现更好，仅通过 80 次请求就完成了实现，不到 Sol-high 所需 238 次请求的三分之一，且处理了 1110 万个输入 Token，而不是 3780 万个。在所有三个阶段结束时，Astra-medium 运行耗时约 51 分钟，估计成本为 25.67 美元；而 Sol-high 运行耗时约 75 分钟，成本为 31.79 美元。

将 Astra 的推理调高并没有帮助，因为那次运行耗时延长至 77 分钟，成本高达 37.23 美元，而且 Shinpr 表示其审查遗漏了一个 medium 设置能够捕获的启动错误。

一个开发者的测试不能说明 medium 设置就是适合所有工作负载的选择，但它确实表明，在这里支付更多的推理费用并不值得。此外，这种模式并非随处适用。ARC Prize 的测试结果几乎走向了相反的方向。

> 将 Astra 的推理调高并没有帮助，因为那次运行耗时延长至 77 分钟，成本高达 37.23 美元，而且 Shinpr 表示其审查遗漏了一个 medium 设置能够捕获的启动错误。

## 更多的推理，更低的账单

[ARC Prize 对 Astra 的评估](https://arcprize.org/blog/astra)展示了等式的另一面。更多的推理不仅提高了 Astra 在 ARC-AGI-3 上的得分；在某些情况下，它还降低了成本。

在 ARC Prize 的标准评估工具中，Astra 在低推理设置下得分为 17.5%，中（medium）为 38.6%，高（high）为 54.8%，最大（max）为 62.7%。[Astra 还在高和最大之间有一个 xhigh 设置](https://thenewstack.io/astra-arc-agi-benchmark/)。但最昂贵的运行并不是使用推理力度最高的那些。ARC Prize 在低推理设置下花费了 38,166 美元，中推理设置下花费 48,090 美元，高推理设置下花费 40,705 美元。最大（max）设置仅为 26,098 美元。

在 max 设置下，Astra 在每次决策中使用了更多的计算资源，但解决环境问题所需的动作更少。这种权衡足以降低整体成本，这在智能体中是可能发生的。虽然较低的推理看起来更便宜，但错误的转向很快意味着更多的工具调用或一次又一次的尝试，这在前期推理上花费的成本比事后修复错误要多得多。

> 虽然较低的推理看起来更便宜，但错误的转向很快意味着更多的工具调用或一次又一次的尝试，这在前期推理上花费的成本比事后修复错误要多得多。

## 无缓存损失的动态推理

这两种极端情况开发者不必在整个工作流程中二选一，这要归功于 Astra 引入的 [configuration_update](https://developers.openai.com/api/docs/guides/latest-model) 机制，该机制允许应用程序在响应之间更改推理力度，而无需更改原始请求级别的配置。

日常工作可以保持在低推理级别，而失败的测试、意外的工具响应或困难的调试问题可以在下一轮触发更高的推理级别。一旦问题解决，智能体可以调回原来的级别。

这也解释了为什么 Shinpr 和 ARC Prize 得到了如此不同的结果。Shinpr 发现额外的推理增加了时间和成本而没有改善结果，而 ARC Prize 发现更多的推理有时减少了动作数量，从而降低了总账单。

目前，`configuration_update` 仅适用于标准、单智能体请求中的 Astra。但是，不要纠结于 Astra 2.5 倍的 Token 价格。如果一个昂贵的模型能在更少的调用次数内完成工作，并且减少修正错误的尝试，它通常反而是运行成本更低的选择。