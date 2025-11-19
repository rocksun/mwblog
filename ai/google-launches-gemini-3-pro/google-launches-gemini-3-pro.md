<!--
title: 谷歌发布Gemini 3 Pro
cover: https://cdn.thenewstack.io/media/2025/11/d2b59466-gemini3-logo.png
summary: Google发布了其基础模型系列最新迭代的Gemini 3 Pro。该模型在多模态推理和编码任务上表现出色，并在多个基准测试中创下纪录。Gemini 3 Pro已在多种Google产品中可用，并将在未来推出Gemini 3 Deep Think变体。
-->

Google发布了其基础模型系列最新迭代的Gemini 3 Pro。该模型在多模态推理和编码任务上表现出色，并在多个基准测试中创下纪录。Gemini 3 Pro已在多种Google产品中可用，并将在未来推出Gemini 3 Deep Think变体。

> 译自：[Google Launches Gemini 3 Pro](https://thenewstack.io/google-launches-gemini-3-pro/)
> 
> 作者：Frederic Lardinois

[Google](https://cloud.google.com/?utm_content=inline+mention) 今日发布了其基础模型系列最新迭代的 Gemini 3 Pro，其他 Gemini 3 变体也将随后推出。Gemini 3 已在包括 Google Search、Gemini App、AI Studio、Vertex AI 以及 Google 的各种智能体开发工具（包括[新推出的 Antigravity](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/)）在内的多种 Google 产品中立即可用。

## 创纪录的基准测试

毫不意外，Google 将 Gemini 3 Pro 描述为有史以来最智能的模型。据 Google 称，该模型将以 1501 分的成绩在 LMArena 排行榜上名列前茅。它在 Humanity’s Last Exam 上也获得了 37.5% 的分数，在 GPQA Diamond 上获得 91.9% 的准确率，GPQA Diamond 是一个提出博士级别科学问题的基准测试，此前 OpenAI 的 GPT-5.1 以 87.6% 的准确率领先。

Google 团队强调的一个领域是 Gemini 3 Pro 在多模态推理任务上的出色表现，该模型在许多此类基准测试上也达到了创纪录的分数。这也意味着它将在视觉推理任务上表现出色，Google 强调的另一个领域是它能够即时创建复杂的动画和模拟。

[![Gemini 2.5 Pro 和 3 在可视化任务上的对比（图片来源：Google）。](https://cdn.thenewstack.io/media/2025/11/92d37f16-google-gemini3-scale.gif)](https://cdn.thenewstack.io/media/2025/11/92d37f16-google-gemini3-scale.gif)

*Gemini 2.5 Pro 和 3 在可视化任务上的对比。（图片来源：Google）*

当然，基准测试并非全部，有时甚至可能具有误导性，但 Google 认为新模型能够为每次交互带来“新水平的深度和细微差别”，而不会诉诸于陈词滥调和其他模型中常见的谄媚行为。然而，只有在日常使用中，模型系列之间的差异才会真正显现出来，因此开发人员和消费者需要几天时间才能真正了解该模型在实际任务中的表现。

## Gemini 3 编码

在编码方面，Google 表示新模型在智能体工作流编码和处理零样本任务方面均优于 Gemini 2.5 Pro。它将可在 Google 自有工具（如 Gemini CLI 和 Android Studio 的 Agent Mode）以及 Cursor、GitHub、JetBrains、Manus 和 Cline 等第三方工具中使用。

Cline 的 AI 负责人 [Nik Pash](https://www.linkedin.com/in/nikpash/) 表示：“Cline 正在使用 Gemini 3 为开发者的 IDE 提供自主代码生成功能。Gemini 3 Pro 能够处理跨越整个代码库的复杂、长周期任务，在多文件重构、调试会话和功能实现过程中保持上下文。它比 Gemini 2.5 Pro 更有效地利用长上下文，并解决了令其他领先模型感到困惑的问题。”

API 访问的费用为每百万输入 token 2 美元，输出 token 12 美元，适用于 20 万 token 或更少的提示。这高于 Gemini 2.5 Pro 每百万输入/输出 token 1.25 美元和 10 美元的价格。

随着此次发布，Google 还发布了一个客户端 bash 工具，允许模型在其智能体工作流中使用 shell 命令，例如导航文件系统。还将有一个用于代码生成和原型设计的托管 bash 工具，但目前，该托管工具仅提供给 Gemini API 的早期访问合作伙伴。

## Deep Think 即将推出

Google 即将推出 Gemini 3 的另一个变体：Gemini 3 Deep Think。此版本将具有增强的推理模型，可能会进一步提升模型的性能。目前，Google 仅将此模型提供给安全测试人员，但很快也将提供给 Google AI Ultra 订阅者（每月付费 250 美元）。

Google Gemini 模型高级总监兼产品负责人 [Tulsee Doshi](https://www.linkedin.com/in/tulsee-doshi/) 在今天发布前的新闻发布会上解释说：“Gemini 3 Deep Think 在 Humanity’s Last Exam 和 GPQA Diamond 等基准测试上的表现超越了 Gemini 3 Pro 已经令人印象深刻的表现。因此，它真正突破了智能的界限，以帮助您解决最复杂的问题。”