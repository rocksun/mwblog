<!--
title: Nvidia重磅发布Nemotron 3 Super：1200亿参数开源模型，赋能大规模AI系统
cover: https://cdn.thenewstack.io/media/2026/03/219a9810-nemotron-3-super-1920x1080-1.jpg
summary: Nvidia发布1200亿参数开源模型Nemotron 3 Super，专为大规模智能体AI系统设计，以高速性能超越竞品，并已广泛上线。
-->

Nvidia发布1200亿参数开源模型Nemotron 3 Super，专为大规模智能体AI系统设计，以高速性能超越竞品，并已广泛上线。

> 译自：[Nvidia launches Nemotron 3 Super, a 120B open model for large-scale AI systems](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/)
> 
> 作者：Frederic Lardinois

在其下周举行的旗舰GTC大会之前，Nvidia于周三[推出了](https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/)其开源权重[Nemotron 3系列](https://thenewstack.io/nvidias-launches-the-next-generation-of-its-nemotron-models/)的第二个模型：Nemotron 3 Super，这是一个拥有1200亿参数、100万个token上下文窗口的模型，并针对速度和效率进行了优化。

去年12月，Nvidia首次推出了Nemotron 3 Nano，这是一个较小的300亿参数模型，采用了与大型Super模型相同的许多优化技术。但Nemotron 3 Nano更适用于小型目标任务，而Nvidia将Nemotron 3 Super定位为能够“大规模运行复杂智能体AI系统”的模型。

## Nemotron 3 Super的可用性

该新模型现已在[build.nvidia.com](https://build.nvidia.com/)、Perplexity、OpenRouter和Hugging Face上可用。企业还可以通过Google Cloud的Vertex AI、Oracle Cloud Infrastructure以及（即将）Amazon Bedrock和Microsoft Azure，以及Coreweave、Crusoe、Nebius和Together AI等平台访问它。

对于拥有必要硬件的用户，Nvidia也将其作为NIM提供。

由于它目前在[OpenRouter](https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b:free)上免费提供，许多人可能会用他们的[“claws”](https://thenewstack.io/nanoclaw-minimalist-ai-agents/)来尝试它。

与Nano模型一样，Nemotron 3 Super也采用了相同的[混合潜在](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)[专家混合](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)和Mamaba-Transformer架构，这应该有助于它在长时间任务中出色地跟踪上下文，而不会产生过多的内存开销。这种架构还允许模型在推理时调用比以前模型多四倍的专家，且推理成本相同。（欲了解更多信息，请查阅[Nvidia的完整研究论文](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf)。）

![](https://cdn.thenewstack.io/media/2026/03/32ed02d8-image2-2.webp)

*标准MoE与潜在MoE架构的并排比较（图片来源：Nvidia）。*

一个有趣的事实是，该模型是使用来自其他前沿推理模型的合成数据进行训练的，并且Nvidia在此次发布中公开了超过10万亿个token的[预训练](https://huggingface.co/datasets/nvidia/Nemotron-Pretraining-Specialized-v1.1)和[后训练](https://huggingface.co/collections/nvidia/nemotron-post-training-v3)数据集，以及15个用于强化学习和评估配方的训练环境。

这很重要，因为不少企业，[包括ServiceNow](https://thenewstack.io/servicenow-launches-a-control-tower-for-agents/)，都曾使用之前的Nemotron变体来微调自己的模型。Nvidia自己也曾将这些模型作为其部分研究和更专业模型的基础。

## Nemotron 3 Super基准测试

当Nvidia首次宣布Nemotron系列时，Super模型最初预计是一个拥有1000亿参数、100亿活跃参数的模型，但该公司显然扩大了其目标。

这可能也是为了与去年8月发布的[OpenAI的gpt-oss-120B模型](https://thenewstack.io/typescript-5-9-brings-less-friction-more-features/#:~:text=OpenAI%20Releases%20Two%20Open%20Source%20Models)竞争。毕竟，大多数人很可能会将Nemotron 3 Super与这款OpenAI模型进行比较。

![](https://cdn.thenewstack.io/media/2026/03/5b31a1db-super-3-aa-scaled.png)

*图片来源：Artificial Analysis。*

从基准测试来看，Artificial Analysis将该模型的整体智能评分为36分，略高于gpt-oss-120B的33分，但远低于Gemini 3.1 Pro或GPT-5.4等领先模型的57分。

尽管如此，Nemotron 3 Super仍远高于Qwen3 Next 80B等较旧的开源模型，但也落后于Qwen3.5 122B、DeepSeek V3.2和GLM-5等较新的模型（尽管GLM-5是一个显著更大的模型）。

![](https://cdn.thenewstack.io/media/2026/03/a5ab6369-nemotron-3-super-scaled.png)

*Artificial Analysis对Nemotron 3的分析（图片来源：Artificial Analysis）。*

但Nemotron 3 Super的优势在于速度。根据[Artificial Analysis](https://artificialanalysis.ai/models/nvidia-nemotron-3-super-120b-a12b/providers)的数据，它以每秒478个输出token的速度，比以往任何模型都要快。Gpt-oss-120B是第二快的模型，每秒264个输出token，Nvidia指出，它还实现了比Qwen3.5-122B高7.5倍的推理吞吐量。

## Nemotron 3 Ultra在哪？

关于Nemotron 3 Ultra何时发布尚无消息，这是该系列中最大的模型，拥有5000亿参数，Nvidia在去年的原始公告中曾预告过。也许几天后的GTC大会上我们会看到它。