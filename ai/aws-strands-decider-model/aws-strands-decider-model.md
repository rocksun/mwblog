<!--
title: AWS推出对标TypeSafe Jev决策模型的本地化方案
cover: https://cdn.thenewstack.io/media/2026/04/85f256ca-img_3509-scaled.jpg
summary: AWS推出了Strands Decider 2B决策模型，这是一个基于Qwen3.5-2B的本地可下载模型，旨在帮助开发者进行智能体请求路由、工具选择及输出评估，提供更快速的决策和置信度评分。
-->

AWS推出了Strands Decider 2B决策模型，这是一个基于Qwen3.5-2B的本地可下载模型，旨在帮助开发者进行智能体请求路由、工具选择及输出评估，提供更快速的决策和置信度评分。

> 译自：[AWS launches a local answer to TypeSafe's Jev decision model](https://thenewstack.io/aws-strands-decider-model/)
> 
> 作者：Frederic Lardinois

**AWS于周四推出了 Strands Decider 2B**，这是其对诸如 [Jev](https://thenewstack.io/typesafe-jev-system-one/)、[Kev](https://github.com/jaredpalmer/kev)、[imajev](https://huggingface.co/mohit67890/imajev-4b)、[Laya](https://huggingface.co/convaiinnovations/laya) 等决策模型的本土化回应。

TypeSafe 的 Jev 在几周前掀起了当前决策模型的热潮，各大 AI 厂商现在也纷纷推出了自己的版本。

例如，OpenAI 在周二推出了 [Decisions API](https://thenewstack.io/openai-decision-api-luna/) 的限量预览版。但这是一个托管 API，其 Luna 模型专注于具有预定义答案的问题，而 AWS 则发布了一个[可下载的模型](https://github.com/strands-labs/strands-decider)，以及用于训练该模型的数据和脚本。

## Strands Decider 是如何工作的

决策模型将自由格式的文本生成替换为了从开发者提供的选项中进行选择或返回数值分数。这使得它们在路由自然语言请求、选择工具、评估输出以及检查建议的操作时非常有用，同时将对话和更复杂的工作留给生成式模型。

Strands Decider 使用 [Qwen3.5-2B](https://huggingface.co/Qwen) 作为其语言理解基础模型，AWS 称之为“躯干（torso）”。然后，该团队移除了生成文本的语言模型头部，并将其替换为一个用于对所提供答案选项进行评分的指针头部（pointer head）。

![](https://cdn.thenewstack.io/media/2026/10/a2b83828-image-3.png)

*图片来源：AWS*

该头部拥有刚过一百万的参数，其主干网络则使用了秩为 16 的 [LoRA](https://arxiv.org/abs/2106.09685)（低秩适应）适配器。

限制答案空间可以防止模型凭空捏造未提供的选项，但这并不意味着它总是能给出正确答案。不过，这是一个微小的权衡，因为 LLM 也并非总是正确的。作为回报，开发者可以获得更快的决策速度以及可用于辅助决策的置信度分数。

## 在智能体行动前进行检查

在 AWS 的示例中（使用该公司开源的 [Strands 智能体框架](https://thenewstack.io/aws-launches-its-take-on-an-open-source-ai-agents-sdk/)构建），用户询问天气但没有说明地点，智能体便会猜测一个城市并提议调用天气工具。

在该工具运行之前，Decider 会检查参数值是否基于对话内容，以及智能体是否有足够的信息继续执行。随后，应用程序会将智能体引导回去，询问用户指的是哪个城市。

接着，该检查会通过 Strands 的干预系统运行，该系统允许开发者选择是继续执行工具调用、拒绝调用、请求人工确认，还是向智能体返回反馈。

在此演示中，Decider 在本地运行，而智能体则通过 [Amazon Bedrock](https://aws.amazon.com/bedrock/) 调用其生成式模型。AWS 表示，它也正在开发决策模型集成库。

## 基于开源的 Qwen 模型构建

与 Kev 类似，Strands Decider 建立在开源的 Qwen 模型之上，这表明当前的许多实验在很大程度上多么依赖于开放权重。Kev 已经支持本地部署和微调，并且随着附带的[训练数据和脚本](https://huggingface.co/StrandsAgents)，AWS 的发布让开发者能够检查其构建配方并将其适配到他们自己的任务中。

> 与 Kev 类似，Strands Decider 建立在开源的 Qwen 模型之上，这表明当前的许多实验在很大程度上多么依赖于开放权重。

AWS 表示，它专注于平衡准确性、校准性和延迟。这里的校准性是指模型的置信度分数与它实际正确频率的贴合程度。

在 [JevBench](https://github.com/fstandhartinger/jevbench) 的公开测试集上，AWS 表示 Strands Decider 在参数量约为 20 亿的公开模型中排名第二，在所有提供完整训练配方的公开模型中排名第一。

![](https://cdn.thenewstack.io/media/2026/10/ad1ad06a-image-2.png)

*图片来源：AWS*

AWS 还指出，Strands Decider 2B 正确回答了 JevBench 简单层级中的每一个问题，这正是它为常规智能体决策所量身打造的能力。

AWS 报告称，在 Nvidia RTX 3090 上，决策时间不到 100 毫秒，随着任务增长，响应时间也会增加。该公司表示，在 M3 MacBook 上，处理小型任务的中位数时间约为 150 毫秒。

AWS 现在发布的模型是该架构的第二个主要迭代版本。该公司表示，早期的头部设计表现明显更差。AWS 还将所有早期的迭代版本都保留在了[代码仓库](https://github.com/strands-labs/strands-decider)中，以便开发者能够追踪模型的演进过程。

![](https://cdn.thenewstack.io/media/2026/10/17940bf8-image.png)

*图片来源：AWS*

Strands Decider 最初孵化于 Strands Labs，这是 AWS 专门用于探索智能体 AI 实验性方法的实验室，于今年早些时候成立。在此之前，该公司还发布了 [Strands Harness](https://thenewstack.io/aws-strands-harness-agent/)，它打包了运行长生命周期智能体所需的工具和支持机制。

## 会推出托管版的 Decider 吗？

有一点拭目以待的是，AWS 是否也会在其云端提供该模型（或其未来版本）的托管版本。混合场景非常适合进行实验和在本地运行，但要将基于此模型构建的应用程序投入生产，开发者同样希望看到托管版本。