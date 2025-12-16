<!--
title: 英伟达重磅发布：新一代Nemotron模型
cover: https://cdn.thenewstack.io/media/2025/12/ac9a49ad-img_0477-edit-scaled.jpg
summary: 英伟达推出Nemotron系列AI模型，包括Nano、Super、Ultra，旨在驱动AI代理。Nano已上线，采用MoE技术，性能优异且开源。
-->

英伟达推出Nemotron系列AI模型，包括Nano、Super、Ultra，旨在驱动AI代理。Nano已上线，采用MoE技术，性能优异且开源。

> 译自：[Nvidia's Launches the Next Generation of Its Nemotron Models](https://thenewstack.io/nvidias-launches-the-next-generation-of-its-nemotron-models/)
> 
> 作者：Frederic Lardinois

Nvidia 今天推出了其 Nemotron 系列的最新开源 AI 模型，旨在为 AI 代理提供动力：[Nemotron 系列](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)包括 Nemotron 3 Nano、Super 和 Ultra。Nvidia 首次不仅发布了模型，还发布了价值三万亿个 token 的预训练数据和 1800 万个样本的后训练数据。得益于 Nvidia 现有的训练环境（该公司也为此推出了 10 个新的 gym 环境）以及该公司的开源强化学习库，开发者将能够轻松地获取这些模型并针对其自身用例进行训练。

Nano 模型现已推出，Super 和 Ultra 模型预计将于 2026 年上半年推出。

### Nemotron 3 模型家族

至于模型本身，这是 Nemotron 家族中第一个采用[专家混合 (MoE)](https://www.ibm.com/think/topics/mixture-of-experts) 技术的产品，该技术通过在任何给定时间只激活参数的一个子集，从而将模型大小与计算成本解耦。这反过来意味着这些新模型显著加快，Nvidia 认为，300 亿参数的 Nemotron 3 Nano 模型（由于采用 MoE 技术，其中 30 亿参数处于活跃状态）的性能比同等的 Nemotron 2 Nano 模型高出 4 倍。它生成答案所需的推理 token 也减少了 60%，这将进一步降低使用该模型的成本。它也是少数提供 100 万 token 上下文窗口的开源模型之一。

Nvidia 表示 Nano 模型尤其适用于特定任务，现已在 HuggingFace 上提供。

Nemotron 3 Super 模型是一个 1000 亿参数的模型，拥有 100 亿个活跃参数，专为多代理应用设计。Nemotron 3 Ultra 模型拥有 5000 亿个参数和 500 亿个活跃参数，虽然这将使其成为这些新模型中最智能的，并非常适合更复杂的应用，但其运行成本也将最高。

[![](https://cdn.thenewstack.io/media/2025/12/0e6ceaf2-nemotron-3-press-release-image.png)](https://cdn.thenewstack.io/media/2025/12/0e6ceaf2-nemotron-3-press-release-image.png)

*图片来源：Nvidia。*

Nvidia 在禁令发布之前没有向媒体提供详细的基准测试数据，该公司迄今为止只表示：“Artificial Analysis 是一个对 AI 进行基准测试的独立组织，它将该模型评为同等规模模型中最开放、最高效且具有领先准确性的模型。”

您可以从下面的 Artificial Analysis 图表中获取更多关于 Nano 模型表现的信息，该图表将 Nemotron 3 Nano 置于与 OpenAI 的 GPT-OSS-20B (高)、Qwen 3 30B 和 Qwen 3 VL 32B 大致相同的水平，但每秒 token 输出速度要高得多。ServiceNow 的 Apriel Thinking 模型速度显著较慢，但在 Artificial Analysis 的智能指数中略高于 Nano 模型。

[![](https://cdn.thenewstack.io/media/2025/12/35414510-artificial-analysis-intelligence-vs.-output-speed-scaled.png)](https://cdn.thenewstack.io/media/2025/12/35414510-artificial-analysis-intelligence-vs.-output-speed-scaled.png)

*根据 Artificial Analysis 的 Nvidia Nemotron 3 Nano 基准测试。图片来源：Nvidia。*

## 可用性

鉴于这些新模型的开源性质和许可，开发者如果拥有所需的硬件，可以将其作为 Nvidia NIM 微服务自行运行，但它们也将通过商业提供商和其他平台提供，包括 [Amazon](https://aws.amazon.com/?utm_content=inline+mention) Bedrock (无服务器) 等公共云，并很快在 Google Cloud、Coreweave、Nebius、Nscale 和 Yotta 上提供。

Baseten、Deepinfra、Fireworks、FriendliAI、OpenRouter 和 Together AI 等推理服务也将提供它，以及 [Couchbase](https://www.couchbase.com/products/capella?utm_content=inline+mention)、DataRobot、H2O.ai、JFrog、Lambda 和 UiPath 等平台。

### Nvidia 为何构建自己的模型

尽管 Nvidia 以创建绝大多数大型语言模型所依赖的硬件加速器而闻名，但该公司构建自己模型的旅程始于 2019 年的 [Megatron-LM 模型](https://nv-adlr.github.io/MegatronLM)。第一个以 Nemotron 品牌推出的模型于 2024 年发布，是一个基于 Meta 的 Llama 3.1 的推理模型。自那时起，Nvidia 发布了许多不同规模且针对特定用例进行调整的 Nemotron 模型，所有这些模型都具有相对宽松的许可，允许 [ServiceNow 等公司](https://thenewstack.io/servicenow-launches-a-control-tower-for-agents/)根据自己的用例调整这些模型。

在今天发布会前的新闻发布会上，当被问及 Nvidia 为何要构建自己的模型以及该公司是否正试图成为前沿模型构建者时，Nvidia 企业级生成式 AI 副总裁 Kari Briski 指出，部分原因是希望在训练和模型推理方面将公司自己的硬件推向极限。

她解释说：“我不需要说‘它是否在竞争？’它是为我们自己构建的，我们把它提供给生态系统，让他们信任并在其之上进行开发。”

Briski 认为，这也是 Nvidia 对围绕其模型——以及普遍意义上的模型创建——构建开放生态系统感兴趣的原因。“如果我们相信生成式 AI 和大型语言模型是——我们确实相信——未来的开发平台，那么我会将这些 LLM 视为一个库。我们如何处理库？我们把它们发布出去供 [开发者] 检查代码，这样你就能理解它，你就能在其之上进行构建，我们就能修复 bug，我们就能改进它，然后把它再次发布出去。所以我们发布得越多，开发者参与度就越高。”