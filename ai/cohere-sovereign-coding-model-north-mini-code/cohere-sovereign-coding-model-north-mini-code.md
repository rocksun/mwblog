<!--
title: Cohere 将主权 AI 概念带向开发者：发布首款代码模型 North Mini Code
cover: https://cdn.thenewstack.io/media/2026/06/60ec81c1-rizki-ardia-6pkdqrnh7ls-unsplash-scaled.jpg
summary: Cohere 推出首款开源代码模型 North Mini Code，旨在满足开发者对模型自主权与数据隐私的需求。该模型采用 30B 参数 MoE 架构，支持本地私有化部署，旨在通过赋予开发者对基础设施的掌控权，应对 AI 模型开发的集权化问题。
-->

Cohere 推出首款开源代码模型 North Mini Code，旨在满足开发者对模型自主权与数据隐私的需求。该模型采用 30B 参数 MoE 架构，支持本地私有化部署，旨在通过赋予开发者对基础设施的掌控权，应对 AI 模型开发的集权化问题。

> 译自：[Cohere sold sovereign AI to enterprises, now it's targeting developers with its first coding model](https://thenewstack.io/cohere-sovereign-coding-model-north-mini-code/)
> 
> 作者：Paul Sawers

加拿大基础模型公司 [Cohere](https://cohere.com/) 在 [过去几年中](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/) 一直向银行、政府和医疗服务提供商兜售一个特定的理念：AI 应该在客户自己的基础设施上运行，处于客户的控制之下，且数据绝不会离开安全边界。

Cohere 的推销在受监管行业中非常受用。现在，该公司正将这一理念带给不同的受众——推出了 [North Mini Code](https://cohere.com/blog/north-mini-code)，这是其首款代码模型，并 [从一开始就以 Apache 2.0 许可证发布](https://huggingface.co/CohereLabs/North-Mini-Code-1.0)。

## 模型访问即基础设施

Cohere 长期以来向企业客户主张的“主权”论点，从根本上讲， [关于所有权](https://thenewstack.io/frontier-ai-models-now-becoming-available-for-takeout/)。受监管的行业有严格的要求：数据不能离开特定的边界，在敏感基础设施上运行的智能层必须是组织能够控制的东西。这一要求塑造了 Cohere 构建产品的方式——可以在任何地方部署，可以在私有基础设施上运行。

根据 Cohere 联合创始人 Nick Frosst 的说法，改变的是提出这些相同问题的人。

“我们现在从开发者那里也听到了类似的担忧，” Frosst 告诉 *The New Stack*。“他们开始将模型访问视为基础设施，而基础设施应该是你拥有并控制的东西。这是主权的延伸。”

> “[开发者] 开始将模型访问视为基础设施，而基础设施应该是你拥有并控制的东西。”

North Mini Code 正是对这一需求作出的直接回应。它是一个 300 亿参数的混合专家（MoE）模型，实际激活参数仅为 30 亿，专为智能体编码任务而设计：这是 Claude Code 和 Cursor 等编码智能体所构建的那种多步骤、使用工具的工作。

Cohere 表示，它可以在单块 Nvidia H100 GPU 上运行，这使得无需大规模多 GPU 部署即可进行自托管成为可能。不想自己管理基础设施的开发者可以通过 API 访问它。

“我们希望为开发者提供一个功能强大、快速、权重开放的模型，他们可以按自己的意愿在本地运行，并适应他们的计算环境，” Frosst 说。

> “我们希望为开发者提供一个功能强大、快速、权重开放的模型，他们可以按自己的意愿在本地运行，并适应他们的计算环境。”

Cohere 声称，在 [Artificial Analysis Coding Index](https://artificialanalysis.ai/models/north-mini-code) 上，其表现优于阿里巴巴的 [Qwen3](https://qwen-3.com/en) 和 Google 的 [Gemma 4](https://thenewstack.io/google-gemma-local-ai/) 等同类权重开放模型（得分 33.4），并表示在相同硬件上，其输出吞吐量比 [Mistral 的 Devstral Small](https://ollama.com/library/devstral-small-2) 2 高出 2.8 倍。

Cohere 自己的基准测试显示，North Mini Code 在终端和代码生成任务中处于领先地位，但在整个评估套件中的结果喜忧参半，如其图表所示，Qwen 3.6 在 SWE-Bench Verified 和 LiveCodeBench v6 上表现更佳。这些比较基于 Cohere 的内部测试，仅供参考。

![North Mini Code 在智能体软件工程和终端任务中的表现，以及与同等规模领先开源模型的复杂代码生成基准测试对比。](https://cdn.thenewstack.io/media/2026/06/df37238d-06e7b98d2b53bf7ca8b7dfa53d758991a031c2e5-3140x2400-1-1024x783.avif)

*North Mini Code 在智能体软件工程和终端任务中的表现，以及与同等规模领先开源模型的复杂代码生成基准测试对比。* (**来源：Cohere**)

## 日益壮大的阵营

Cohere 的时机使其跻身于越来越多的国际公司行列，这些公司已将权重开放的代码模型作为一种有意的产品选择。[Mistral](https://mistral.ai/)，这家 [总部位于巴黎的 AI 公司](https://thenewstack.io/mistral-vibe-cloud-agents/)，于 2025 年 5 月 [推出了 Devstral](https://mistral.ai/news/devstral/) —— 这是其首款专用的智能体编码模型，同样使用 Apache 2.0 许可证，并于 12 月 [推出了 Devstral 2](https://mistral.ai/news/devstral-2-vibe-cli/)。[JetBrains](https://www.jetbrains.com/)，这家捷克开发者工具公司，最近 [开源了其第二代代码模型 Mellum2](https://thenewstack.io/jetbrains-mellum2-open-source-coding-model/)。

重点各不相同。Mistral 明确将权重开放与 AI 主权以及在私有基础设施上部署模型的能力联系起来，而 JetBrains 则专注于延迟、成本和部署灵活性。在实践中，这两种方法都让开发者和企业对模型在哪里运行以及如何操作拥有了更多控制权。

## 掌控基础设施

人们对前沿模型权重开放替代方案的渴望显而易见。AI 智能体平台 Lindy [最近宣布已将](https://thenewstack.io/lindy-deepseek-anthropic-switch/) 100% 的推理流量从 Anthropic 转移到中国的 DeepSeek，称此举将为公司节省数百万美元，同时实际上提高了其核心用例的性能。Lindy 的首席执行官 Flo Crivello 回应了关于通过中国开发模型路由的明显问题：该公司使用 Atlas Cloud，这是一个基于美国的推理提供商，在美方领土上托管 DeepSeek。DeepSeek 的权重开放性质使这一切成为可能——该模型可以由任何提供商、在任何司法管辖区进行托管。

这正是 Frosst 所指出的动态。权重开放为开发者提供了专有 API 所不具备的可选性：能够选择模型在哪里运行、由谁操作以及在什么条款下操作。对于那些推理账单已经增长到超过工资支出的公司——正如 Crivello [指出](https://x.com/Altimor/status/2044108104816832576) Lindy 的情况一样——这些都是具有实际商业后果的决策。

Cohere 的 [Command 系列](https://cohere.com/command) —— 其专为智能体、多语言和多模态任务构建的旗舰企业模型系列 —— 此前曾以更严格的许可证作为权重开放模型发布。随着 Command A+ 的发布，[该公司在 5 月转向了 Apache 2.0](https://cohere.com/blog/command-a-plus)，使得关于使用和再分发的法律条款明显更加宽松。

> “开源开发集中在少数几个司法管辖区，运行关键基础设施的组织没有可靠的替代方案。”

Frosst 将 Cohere 多年来主张的企业主权论点与 North Mini Code 背后的思考直接联系起来。他说，开源代码模型是对 Cohere 在企业 AI 中看到的相同集中化问题的回应——只是现在在开发者层面上演。

“开源开发集中在少数几个司法管辖区，运行关键基础设施的组织没有可靠的替代方案，” Frosst 说。“North Mini Code 将这种思考延伸到了开发者层面。随着编码智能体成为软件工程运行的基础设施，谁控制了这些系统，谁就控制了它们如何工作、如何演进以及它们针对什么进行优化。我们认为开发者和企业应该拥有控制权。”