<!--
title: GLM-5.3 基座未变：编码能力提升的秘密来自哪里？
cover: https://cdn.thenewstack.io/media/2026/06/3b7fe4c3-michael-l5jn-7kemls-unsplash-scaled.jpg
summary: Z.ai发布的GLM-5.3模型并未改变基座，而是通过大规模的后训练扩展，显著提升了在代码编写、Agent任务及网络安全分析方面的表现。该案例证明了优化后训练比单纯堆叠参数更能有效提升模型性能。
-->

Z.ai发布的GLM-5.3模型并未改变基座，而是通过大规模的后训练扩展，显著提升了在代码编写、Agent任务及网络安全分析方面的表现。该案例证明了优化后训练比单纯堆叠参数更能有效提升模型性能。

> 译自：[GLM-5.3 didn’t change the base model — where did its coding gains come from?](https://thenewstack.io/glm-5-3-post-training-coding/)
> 
> 作者：Amanda Caswell

Z.ai 于周五发布了 GLM-5.3，这是一个基于与 GLM-5.2 相同基座模型的编程与 Agent 模型。开发人员现在已经可以通过 Z.ai 的 GLM Coding Plan 使用 Claude Code、Cline、OpenCode 和 Codex 来调用 GLM-5.3。直接 API 访问目前仍显示为“即将推出”，因为 Z.ai 计划在经过两周的强化和安全测试后发布模型权重。

## 后训练发挥了核心作用

Z.ai 大幅扩展了 GLM-5.3 的后训练流程，让模型接触了多出十倍的长跨度任务环境，同时拓宽了其对开发工具和工程工作流的访问权限。

一些训练任务模拟了完整的软件生命周期——从识别 Bug 和起草修复方案，到编写代码、运行测试及交付结果。[根据 Z.ai 的说法](https://docs.z.ai/guides/llm/glm-5)，单个任务的工作量就相当于一位高级工程师几天的劳动量。

> Z.ai 将计算资源集中在模型实际工作的特定环境中。

这使得 GLM-5.3 成为后训练计算扩展的一个引人注目的案例研究。Z.ai 将计算资源集中在模型实际工作的特定环境中。他们并非唯一验证这一假设的实验室——[DeepSeek 最近证明了较小的模型可以通过仅优化后训练而非增加参数规模，就能超越其旗舰产品](https://thenewstack.io/deepseek-v4-flash-open-weights/)。

## 基准测试大幅提升，但仍需谨慎

Z.ai 声称，在其内部的代码基准测试（Code Bench）中，GLM-5.3 的性能比 GLM-5.2 提升了 50%，尽管[供应商自行报告的数字](https://z.ai/blog/glm-5.3)在社区测试发布后的权重之前，仍值得保持常规的怀疑态度。然而，在公开评估中，该模型在 Agent 编码方面展现了显著的提升。GLM-5.3 在 Terminal-Bench 3.0 上飙升至 28.3 分（此前为 4.6 分），DeepSWE v1.1 的分数从 46.2 提高到 66.9，在 Agents’ Last Exam 上也从 23.8 微升至 28.5。DeepSWE 上的 66.9 分使其与 Google 的 [Gemini 3.7 Flash (65%)](https://thenewstack.io/gemini-3-7-flash-agents/) 处于同一水平，但由于测试框架的差异，直接对比的结果应谨慎看待。

## 更长的上下文伴随着不同的努力级别

GLM-5.3 拥有 100 万 token 的上下文窗口和 12.8 万 token 的补全上限，能够容纳庞大的代码库。Claude Code 上的开发人员可以通过 glm-5.3[1m] 模型标签和匹配的 1M-token 压缩窗口来配置更大的窗口。

推理努力级别可在低、高和最大级别之间配置（默认启用最大级别）。虽然建议用于非琐碎的工程任务，但最大推理级别会带来明显的延迟和 token 开销。团队必须评估下游的准确性是否值得增加计算成本。Z.ai 断言该模型优化了延迟、token 效率和准确性之间的权衡，但目前尚未发布正式的每 token API 定价。

> 虽然对于只想使用最新底层模型的开发者来说这很方便，但对于试图在同一计划中针对之前版本进行清晰 A/B 对比的团队来说，这产生了一个盲点。

这种缺失反映了市场围绕 Agent 经济正在进行的重新校准。在 [OpenAI 的激进降价](https://thenewstack.io/gpt-5-6-api-price-cuts/) 和 [Microsoft 引入 token 上限](https://thenewstack.io/microsoft-copilot-token-budgets/) 以缓解失控的自主 Agent 之间，对长跨度 Agent 计算定价仍然是一个不断变化的目标。在 Z.ai 的 Coding Plan 中，使用情况通过积分计量：与 GLM-4.7 相比，GLM-5.3 在输入、缓存输入和输出 token 方面具有更高的基准倍率，抵消因素是 50% 的非高峰期折扣。

有一点迁移上的细节值得注意。根据 Z.ai 的文档，调用 GLM-5.2 或 GLM-5.1 的 Coding Plan 请求会自动重定向到 GLM-5.3。虽然对于只想使用最新底层模型的开发者来说这很方便，但对于试图在同一计划中针对之前版本进行清晰 A/B 对比的团队来说，这产生了一个盲点。请务必仔细检查其 Agent 返回的实际模型 ID。

## 安全性提升在漏洞利用环节遇到瓶颈

Z.ai 将网络安全定位为 GLM-5.3 的一个新兴优势。该模型在 CyberGym 上得分为 84.5%，高于 GLM-5.2 的 77.2%。Z.ai 报告称，这一成绩略高于 Mythos 5 的 83.8% 和 GPT-5.6 Sol 的 83.6%。

但在需要利用其发现的漏洞时，GLM-5.3 的表现并不如意。其 ExploitBench 得分从 24.4% 翻了一番多，达到 54.4%，但仍落后于 Mythos 5（78%）和 GPT-5.6 Sol（76.5%）。这些结果遵循了前沿 AI 实验室中可见的模式：[OpenAI 最近专门构建了一个用于网络安全工作的模型](https://thenewstack.io/openai-gpt56-cyber-daybreak/)，并[因担心其进攻能力在野外可能造成的后果而推迟了另一个模型的发布](https://thenewstack.io/openai-astra-cybersecurity-delay/)。

Z.ai 承认，该模型目前在漏洞利用链的早期阶段（包括审查源代码和验证漏洞）比在完成更深层的进攻性安全任务方面更强。但对于那些高分数的白盒审查结果，请务必保持谨慎。正如你所知，可靠地制作一个漏洞利用程序、证明生产环境中的真实可达性，或在不触发下游回归的情况下修补缺陷，是完全不同的挑战。

> 可靠地制作一个漏洞利用程序、证明生产环境中的真实可达性，或在不触发下游回归的情况下修补缺陷，是完全不同的挑战。

## **两周后发布权重**

GLM-5.3 已经可以通过兼容 Anthropic 和 OpenAI 的端点在 GLM Coding Plan 中进行选择。用户可以将其连接到 Claude Code、Codex 或其他支持自定义模型配置的 Agent。[Z.ai 的模型切换指南](https://docs.z.ai/devpack/latest-model)提供了所需的端点和设置。

更重要的发布计划在两周后。一旦权重可用，开发人员将能够测试基准性能的提升是否能延续到本地部署、不同的推理堆栈以及 Z.ai 未选定的存储库中。这种等待是很熟悉的——[Moonshot 在类似条件下发布了 Kimi K3 的权重](https://thenewstack.io/kimi-k3-open-weights/)，“宣布开放权重”与“你实际能运行的权重”之间的差距已成为开放模型领域的重复模式。