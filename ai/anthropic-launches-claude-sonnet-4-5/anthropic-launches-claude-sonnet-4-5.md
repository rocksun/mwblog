<!--
title: Anthropic 重磅发布 Claude Sonnet 4.5
cover: https://cdn.thenewstack.io/media/2025/09/16ef92f1-sonnet-4.5.png
summary: Anthropic发布Claude Sonnet 4.5，号称最佳编码模型，性能卓越。同时更新Claude Code，发布Agent SDK，并推出“Imagine with Claude”即时软件生成实验。
-->

Anthropic发布Claude Sonnet 4.5，号称最佳编码模型，性能卓越。同时更新Claude Code，发布Agent SDK，并推出“Imagine with Claude”即时软件生成实验。

> 译自：[Anthropic Launches Claude Sonnet 4.5](https://thenewstack.io/anthropic-launches-claude-sonnet-4-5/)
> 
> 作者：Frederic Lardinois

Anthropic 的 Claude Sonnet 和 Opus 大型语言模型长期以来一直是开发人员的最爱。今天，该公司推出了 Claude Sonnet 4.5，这是其主流模型的最新版本，该公司将其描述为“世界上最好的编码模型”。

该公司还发布了 Claude Code 的更新，一个 Claude Agent SDK，允许开发人员使用 Anthropic 自己使用的工具构建代理，以及一个 VS Code 扩展等。

还有一个引人入胜的新实验，“Imagine with Claude”，它使用新模型即时生成软件（但仅对 Claude Max 订阅者开放，且仅限未来五天）。

## Sonnet 4.5

Anthropic 表示，Sonnet 4.5 将更可靠地遵循指令并重构现有代码。在 SWE-Bench Verified 基准测试中，该测试评估模型处理一系列真实世界 GitHub 拉取请求的能力，Sonnet 4.5 得分为 77.2%（并联测试时计算能力可达 82%）。

Anthropic 表示，在某些方面，Sonnet 4.5 现在超越了该公司旗舰模型 Opus 4.1，包括在金融服务行业解决问题。

在 [OSWorld](https://os-world.github.io/) 上，一个测试人工智能模型在真实计算机使用任务中表现的基准，Sonnet 4.5 现在以 61.4% 的成功率位居榜首。这比之前以 43.9% 成功率位居榜首的 Sonnet 4 有了重大飞跃，也击败了之前得分约为 44% 的 Opus 4.1。

![](https://cdn.thenewstack.io/media/2025/09/22812765-claude-for-chrome.png)

*图片来源：Anthropic。*

对于长时间运行的复杂任务，Sonnet 4.5 现在可以自主运行 30 小时，而 Opus 4 只有 7 小时。Anthropic 表示，通过这些模型更新，Sonnet 4.5 现在可以在“全程保持专注和性能”的同时完成这些任务，不过这还需要一些测试来验证其在真实场景中是否属实。

在几乎所有编码基准测试中，Sonnet 4.1 都击败了 OpenAI 的 GPT-5 和 Google 的 Gemini 2.5 Pro 等竞争对手。然而，在视觉推理基准测试中，Anthropic 的模型通常表现稍逊一筹，竞争对手仍保持领先。

[![Anthropic Sonnet 4.5 benchmarks](https://cdn.thenewstack.io/media/2025/09/c5387eac-sonnet_4-5_eval_social.png)](https://cdn.thenewstack.io/media/2025/09/c5387eac-sonnet_4-5_eval_social.png)

*图片来源：Anthropic。*

但更重要的是，Anthropic 赋予了该模型访问多项新功能的能力——类似于其 Claude Code 编码代理所拥有的功能。这些功能包括访问虚拟机和内存，以及更好的上下文管理和多代理支持。

值得一提的是，Anthropic 表示 Sonnet 4.5 是其发布的第一个能够重建 Claude.ai 网页应用程序的模型，这项工作耗时约五个半小时，涉及 3,000 多次工具使用。

Cursor 首席执行官 Michael Truell 表示：“我们看到 Claude Sonnet 4.5 展现了最先进的编码性能，在更长期的任务上有了显著改进。”“这进一步证明了为什么许多使用 Cursor 的开发人员选择 Claude 来解决他们最复杂的问题。”

Sonnet 4.5 的定价将保持不变，输入/输出每百万 token 分别为 3 美元/15 美元，与 Anthropic 之前对 Sonnet 4 的收费相同。

[![Anthropic's Claude code hours of work chart.](https://cdn.thenewstack.io/media/2025/09/7c30c01c-hours_of_work_chart-1.png)](https://cdn.thenewstack.io/media/2025/09/7c30c01c-hours_of_work_chart-1.png)

*图片来源：Anthropic。*

## Claude Code 有哪些新功能？

谈到 Claude Code，Anthropic 的编码代理现在当然也能访问这个新模型，但该公司也推出了不少新功能。例如，Anthropic 表示，Claude Code 目前的年化收入已超过 5 亿美元，过去三个月的使用量增长了 10 倍以上，它正在获得一个原生的 Visual Studio Code 扩展。这将允许开发人员通过内联差异实时查看 Claude Code 所做的更改。

终端中的 Claude Code 也得到了一些更新，状态可见性得到改进，并增加了可搜索的提示历史记录。鉴于您可能经常希望重复使用提示，最后一个功能尤其有用。以前，您要么必须在终端中找到这些提示并复制粘贴，要么将它们保存到终端之外。

新增的功能还有检查点，这使得在 Claude Code 脱离脚本时更容易回滚代码。以前，开发人员必须通过将代码推送到其仓库或（天哪！）进行本地备份来手动完成此操作。

## Claude 代理 SDK

对于那些希望基于与 Claude Code 相同的基础构建代理的开发人员，Anthropic 正在推出 Claude Agent SDK。Anthropic 表示，这个新的 SDK 使用与 Claude Code 相同的底层基础设施，但允许开发人员构建他们想要的任何代理。该 SDK 将包含代理编排、内存和上下文管理、工具使用、权限管理等功能。

![](https://cdn.thenewstack.io/media/2025/09/3d1e5433-claude-agents-sdk.gif)

*图片来源：Anthropic。*

在 API 方面，开发人员获得了一个内存工具，以帮助他们的代理在长时间运行的任务中保持上下文。Anthropic 还增加了一个自动上下文管理功能，该功能将使 Claude 根据需要编辑上下文窗口并删除陈旧数据。

## 即时构建软件：“Imagine with Claude”

“Imagine with Claude”是 Anthropic 在即时生成软件和用户界面方面进行的一项实验。

Anthropic 在今天的新闻稿中解释说：“没有预先确定的功能；没有预先编写的代码。您所看到的是 Claude 实时创建，并根据您的请求进行响应和调整。”“这是一个有趣的演示，展示了 Claude Sonnet 4.5 能做什么——一种通过将强大模型与正确基础设施结合起来，探索可能性的方式。”

Claude 在后台构建这些应用程序时到底发生了什么，目前尚不清楚。Anthropic 尚未提供任何额外细节。

最近几个月，许多人工智能专家一直在讨论这个想法。如果你能在需要时直接使用人工智能来构建所需的软件会怎样？Lovable 等工具在一定程度上已经实现了这一点，但这仍然不是 Anthropic 在这里承诺的那种无缝体验，即构建本质上是一次性使用的软件。

显然，目前这只是一个展示 Sonnet 4.5 功能的实验——而且仅在接下来的五天内对 Anthropic 的 Claude Max 计划用户开放——但它确实展示了该行业在不远的将来可能的发展方向。