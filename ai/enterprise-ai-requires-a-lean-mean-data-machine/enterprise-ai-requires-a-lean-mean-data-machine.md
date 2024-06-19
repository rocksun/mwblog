
<!--
title: 企业AI需要精益、高效的数据机器
cover: https://cdn.thenewstack.io/media/2024/06/ef898029-artificial-intelligence-7649721_1280.jpg
-->

贵公司如何处理这个问题将决定它是否会随着人工智能的下一个阶段而发展，还是成为过去的一个遗迹。

> 译自 [Enterprise AI Requires a Lean, Mean Data Machine](https://thenewstack.io/enterprise-ai-requires-a-lean-mean-data-machine/)，作者 Bharti Patel。

七年前，[八位 Google 研究人员](https://www.wired.com/story/eight-google-employees-invented-modern-ai-transformers-paper/) 在一场重要的机器学习会议上介绍了 Transformer，将 [AI](https://thenewstack.io/ai/) 推向了进化的新阶段。[Transformer 架构](https://www.techtarget.com/searchenterpriseai/feature/Transformer-neural-networks-are-shaking-up-AI) 是创新的 AI 神经网络，它使当今的大语言模型 (LLM) 和建立在其上的生成式 AI 应用程序成为可能。这项工作建立在许多人的基础之上，包括图灵奖得主 [Geoffrey Hinton](https://www.newyorker.com/magazine/2023/11/20/geoffrey-hinton-profile-ai) 等 AI 巨头和传奇人物 [Fei Fei Li](https://qz.com/1034972/the-data-that-changed-the-direction-of-ai-research-and-possibly-the-world)，后者因坚持认为大数据是释放 AI 力量的核心而受到认可。虽然超大规模计算和学术界的研究仍然像以往一样充满活力，但当今 AI 模型创新的另一个热点是企业本身。

各个垂直领域的企业都明智地评估了 AI 发展史上的这一分水岭时刻，抓住时机以创新方式优化 LLM，并利用它们创造新的价值。但是，到目前为止，该价值在很大程度上仍是[未实现的](https://thenewstack.io/ex-red-hat-ceo-ais-bumpy-road-to-the-enterprise/)。

现在，2024 年过半，为了充分利用 LLM，企业创新者首先必须[了解大量活动部件](https://thenewstack.io/5-key-learnings-about-ai-and-chatgpt-in-the-enterprise/)。拥有合适的底层技术并根据企业的独特需求进行调整，将有助于确保生成式 AI 应用程序能够产生可靠的结果——以及现实世界的价值。

## 数据集、模型和工具

当然，数据是 AI 的燃料，海量的公共数据集为 [LLM](https://thenewstack.io/what-is-a-large-language-model/) 提供动力。但这些公共数据集可能不包含企业创新者试图实现的目标的正确数据。通过它们产生的幻觉和偏差也与企业所需的质量控制相冲突。数据谱系、可追溯性、可解释性、可靠性和安全性对企业用户来说都更为重要。他们必须对数据使用负责，否则会面临代价高昂的诉讼、声誉问题、客户伤害以及对其产品和解决方案的损害。这意味着他们必须确定哪些内部专有数据集应为模型定制和应用程序开发提供支持，这些数据集位于何处，以及如何最好地清理和准备它们以供模型使用。

我们听说最多的 LLM 被认为是基础模型：由 OpenAI、Google、Meta 等公司构建的模型，这些模型在海量互联网数据上进行训练——一些高质量数据，一些质量差到被视为错误信息。基础模型专为大规模并行而构建，可适应各种不同的场景，并且需要重要的防护措施。Meta 的 [Llama 2](https://www.infoworld.com/article/3706470/what-is-llama-2-metas-large-language-model-explained.html)，“一个经过预训练和微调的 LLM 家族，参数规模从 7B 到 70B 不等”，是许多企业的热门起点。它可以通过独特的内部数据集进行微调，并结合知识图谱、向量数据库、用于结构化数据的 SQL 等功能。幸运的是，开源社区中有一项强大的活动可以提供新的优化 LLM。

开源社区在提供用作生成式 AI 生态系统的连接组织的工具方面也变得特别有帮助。[LangChain](https://thenewstack.io/building-gpt-applications-on-open-source-stack-langchain/)，例如，是一个简化基于 AI 的应用程序创建的框架，它有一个专门设计用于优化 LLM 使用的开源 Python 库。此外，Linux 基金会[分支](https://www.datanami.com/2024/04/16/linux-foundation-promotes-open-source-rag-with-opea-launch/)正在为检索增强生成 ( [RAG](https://www.infoworld.com/article/3712227/what-is-rag-more-accurate-and-reliable-llms.html)) 制定开放标准，这对于将企业数据引入预训练的 LLM 和减少幻觉至关重要。企业开发人员可以使用 API 访问许多工具，这是一场范式转变，有助于实现 AI 开发的民主化。

虽然一些企业会有一个纯粹的研究部门来调查开发新算法和 LLM，但大多数企业不会重新发明轮子。微调现有模型并利用不断增长的工具生态系统将成为实现价值的最快速途径。

## 超级计算和弹性数据平面

当前的 AI 时代，尤其是生成式 AI 的蓬勃发展，正在推动计算使用量和 GPU 技术的进步出现惊人的增长。这是由于 [AI 训练和 AI 推理](https://siliconangle.com/2023/02/05/generative-ai-drives-explosion-compute-looming-need-sustainable-ai/) 所需的计算复杂且数量庞大，尽管这些过程消耗计算的方式存在差异。这里不可能不提到 Nvidia GPU，它供应了[大约 90% 的 AI 芯片市场](https://www.popsci.com/technology/nvidia-chip-generative-ai/)，并且随着最近[宣布](https://www.nvidia.com/gtc/keynote/) 的功能强大的 GB200 Grace Blackwell 超级芯片，它可能会继续保持主导地位，该芯片能够进行实时万亿参数推理和训练。

除了这种强大的计算之外，正确的数据集、微调的 LLM 和强大的工具生态系统的结合对于实现企业 AI 创新至关重要。但为这一切提供形式的技术支柱是数据基础设施——能够统一数据生态系统的存储和管理系统。在云计算中奠定基础的数据基础设施现在也成为 AI 存在和增长的基础。

当今的 LLM 需要以前所未见的速度获得数据量、速度和多样性，这会产生复杂性。不可能在高速缓存中存储 LLM 所需的数据类型。对于需要为海量数据集进行扩展的高 IOPS 和高吞吐量存储系统，是 [LLM 所需的](https://www.techtarget.com/searchstorage/news/366537138/Storages-role-in-generative-AI?Offer=abt_pubpro_AI-Insider) 基底，其中需要数百万个节点。借助能够实现闪电般快速读取存储读取时间的超级 GPU，企业必须拥有低延迟、大规模并行系统，该系统可以避免瓶颈并针对此类严格要求进行设计。例如，Hitachi Vantara 的虚拟存储平台 One 提供了一种新的方法来跨块、文件和对象实现数据可见性。需要随时提供不同类型存储来满足不同的模型要求，包括闪存、现场和云中。闪存可以提供更密集的占用空间、聚合性能、可扩展性和效率，以加速 AI 模型和应用程序开发，同时兼顾碳足迹。闪存还可以降低功耗，这对于在可持续的现在和未来获取生成式 AI 的好处至关重要。

最终，数据基础设施提供商可以通过向开发人员提供统一的弹性数据平面和易于部署的设备（以及生成式 AI 构建模块、合适的存储和计算），以最佳方式支持企业 AI 开发人员。统一的弹性数据平面是一台精益机器，可以极高效地处理数据，数据平面节点靠近数据所在位置，可以轻松访问不同的数据源，并提高对数据谱系、质量和安全性的控制。借助设备，模型可以位于顶部并可以持续训练。这种方法将加速企业跨领域的价值生成 AI 应用程序的开发。

## 控制成本和碳足迹

至关重要的是，AI 时代的这些技术基础必须以成本效益和减少碳足迹为目标来构建。我们知道，在世界迫切需要减少碳足迹的时候，训练 LLM 和生成式 AI 在各行业的扩展正在增加我们的碳足迹。我们也知道，首席信息官始终将削减成本列为首要任务。采用混合数据基础设施方法有助于确保企业灵活选择最适合其特定要求且最具成本效益以满足这些需求的方式。

最重要的是，AI 创新者应该明确他们想要实现什么以及实现这一目标所需的模型和数据集，然后根据闪存、固态硬盘和硬盘等硬件要求进行调整。从超大规模计算提供商处租用或使用本地机器可能是有利的。生成式 AI 需要节能、高密度的存储来降低功耗。

具有高自动化水平、弹性数据平面和针对 AI 应用程序构建进行了优化的设备的混合数据中心将以一种社会负责且可持续的方式帮助推动 AI 创新，同时仍然尊重底线。你的企业如何处理这个问题可能会决定它是否会随着 AI 的下一个阶段而发展，还是成为过去的一个遗迹。
