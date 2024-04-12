
<!--
title: Cloud Next 2024上Google鼓吹新的Gemini代码辅助工具
cover: https://cdn.thenewstack.io/media/2024/04/babcfbd3-thomas-gcn-overview.jpg
-->

在 Google Cloud Next '24 上，Google 展示了其对所有 AI 事物的持续投入，形式是若干新的开发者工具和新的以 AI 为重点的芯片。

> 译自 [Google Vaunts New Gemini Code Assist Tool at Cloud Next 2024](https://thenewstack.io/google-vaunts-new-gemini-code-assist-tool-at-cloud-next-2024/)，作者 Chris J Preimesberger。

[Google 的 Cloud Next 2024](https://cloud.withgoogle.com/next) 活动将于 4 月 11 日在拉斯维加斯举行，届时将有 30,000 名与会者参加，这意味着从 [Gemini](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/)（Google 的 AI 驱动的聊天机器人）到 GenAI、[DevOps](https://thenewstack.io/devops/) 和安全等所有内容都将有大量以云为重点的新消息。

自 2019 年 [COVID-19](https://thenewstack.io/the-network-impact-of-the-global-covid-19-pandemic/) 席卷全球以来，这是第二次举办线下 Cloud Next 活动。该活动的在线版本已于 2020 年、2021 年和 2022 年举行。[Google Cloud](https://cloud.withgoogle.com?utm_content=inline+mention) 首席执行官 [Thomas Kurian](https://www.linkedin.com/in/thomas-kurian-469b6219/) 及其继任者们登台展示了他们对所有 AI 事物的持续关注，并推出了多款新的开发者工具。其中一款工具 [Gemini 代码辅助](https://cloud.google.com/products/gemini/code-assist?hl=en) 不仅可以找到你一直在寻找的代码，还可以对替代方案提出周到的建议。

在本次展会上备受关注的其他新型 AI 工具和服务包括[适用于 Gmail 的 Duet AI](https://cloud.google.com/products/gemini?hl=en)，这是生成式 AI 在 Google 安全产品线中的扩展，以及其他以企业为重点的更新。

## “重新定义 AI 原生时代的云”

“Google 正在重新定义 AI 原生时代的云体验，”Gartner 副总裁兼首席分析师 [Chirag Dekate](https://www.linkedin.com/in/cdekate/) 告诉 The New Stack。“企业正在踏上某种旅程，以构建未来的 AI 工厂，这些工厂将改变其所有流程，并通过 GenAI 提升为每一位员工赋能。”

Dekate 表示，这种新兴的 AI 原生时代在很多方面都非常适合 Google。

“由于其核心技术、系统、功能和服务都是为了解决无处不在的 AI 而设计的，因此体验现在已成为 Google 众多产品和服务（从 Google 搜索到地图及其他）的原生功能，”Dekate 说。

Dekate 表示，因此，Google 正在其系统和服务组合中创建差异化功能也就不足为奇了，其中包括：

- [AI 超级计算机](https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-tpu-v5p-and-ai-hypercomputer)（一种与同类产品不同的工作负载优化基础设施）；
- 业界最广泛、最深入的[模型目录](https://cloud.google.com/data-catalog/docs/concepts/overview)（支持访问一、三方和企业级开放源代码模型，所有这些模型均在 AI 超级计算机上构建和优化）；
- [适用于 Google Cloud 的 Gemini](https://cloud.google.com/blog/products/ai-machine-learning/gemini-for-google-cloud-is-here)和 [适用于 Workspace 的 Gemini](https://workspace.google.com/) 体验，这些体验具有差异化和聚合基础设施；
- [Gemini 模型](https://ai.google.dev/?gad_source=1&gclid=Cj0KCQjwztOwBhD7ARIsAPDKnkAa7_5-dR9kLoUKJnN_v4HN-TPCZSxKAS4c38F_RID--xTbTaNgaC8aAmQ4EALw_wcB)创新，可激活新的生态系统飞轮；以及
- 代理生态系统，得益于广泛的合作伙伴生态系统集成，将所有 GenAI 创新应用于企业环境中。

首席执行官 Kurian 表示，AI 超级计算机结合了 Google 的 [TPU](https://thenewstack.io/paperspace-co-founders-discuss-tpus-and-cloud-deep-learning/)、[GPU](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/) 和 AI 软件，为训练和服务模型提供了性能和成本优势。“如今，领先的 AI 公司和 Google Cloud 客户，如 Anthropic、[AI21 Labs](https://thenewstack.io/ai21-labs-releases-jurassic-2-its-new-large-language-model/)、Contextual AI、Essential AI 和 [Mistral AI](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/) 正在使用我们的基础设施，”他说。

Kurian 表示，Google 还宣布了 TPU v5p 的普遍可用性，这是用于训练和推理的最新 AI 加速器，其计算能力是前代产品的四倍。

## 新的代码辅助改进

Google 在展会的第一天公布了 AI 驱动的 Gemini 代码辅助工具的重大改进，引起了开发者的广泛关注。

“我认为版本 1.5 中的 Gemini 代码辅助增强功能对于开发者来说是最重要的，”Forrester 首席分析师
[Devin Dickerson](https://www.linkedin.com/in/devin-dickerson-47679225/) 告诉 The New Stack。“多模态输入和对可分析代码行数方面相对较大的输入的支持可能对希望获得更全面且应用程序感知的建议的开发者和开发团队有所帮助。”

**从大局来看，这些进步对云开发人员有多重要？**

Dickerson 说：“我认为代码行数的扩展（根据主题演讲中的公告，为 30K）将代码辅助推向了正确的方向。”“随着这些工具越来越了解更大的代码库集以及系统级和应用程序级问题，价值主张将会增加，尤其是在企业中的应用程序现代化用例。”

Gartner 的 Dekate 表示同意。“除了代码完成之外，Gemini Code Assist 还提供代码生成，从而提高了企业开发人员的生产力、效率和准确性，”他说。“通过与第三方深度集成并支持包括 GitHub 和 [GitLab](https://about.gitlab.com/?utm_content=inline+mention) 在内的更广泛的生态系统，Google Code Assist 在该领域的生态系统集成方面树立了标杆。

“此外，Gemini Code Assist 现在由 Gemini 提供支持，其中更大的上下文大小可提供无与伦比的开发人员体验。每个企业在寻求利用 GenAI 来加速开发人员生产力时都应将 Google Code Assist 列入候选名单。”

## Google Cloud Platform 中的新闻

Google Cloud Next 也是用于引入大量新实例类型和加速器以增强 Google Cloud Platform 的场所。除了新的基于 Arm 的 Axion 定制芯片之外，大多数公告都是关于 AI 加速器的，无论是由 Google 还是 [AI 芯片制造商 NVIDIA](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/) 构建的。似乎企业都在探索在许多系统中使用 AI，一旦他们启动并运行某些内容，他们自然会希望对其进行加速。

NVIDIA 在几周前宣布了其 [Blackwell 平台](https://thenewstack.io/nvidia-gtc-hyperscaler-happiness-and-enterprise-indigestion/)，但 Google 不会很快提供这些机器。对用于 AI 和 HPC 工作负载的高性能 [NVIDIA HGX B200](https://www.nvidia.com/en-us/data-center/hgx/) 和用于 [大型语言模型 (LLM)](https://thenewstack.io/what-is-a-large-language-model/) 训练的 [GB200 NBL72](https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/) 的支持将于 2025 年初推出。周二来自 Google 的一个有趣的事实：GB200 服务器将采用液冷，这说明了它们预计会产生很大的功率和热量。

NVIDIA 表示，其 Blackwell 芯片要到今年的最后一个季度才会公开发布。
