<!--
title: Ironwood：谷歌在AI芯片大战中对抗英伟达的答案
cover: https://cdn.thenewstack.io/media/2025/04/e9f2b7df-osarugue-igbinoba-t354dnfdjkq-unsplash.jpg
summary: 谷歌发布第七代AI芯片Ironwood (TPU7)，单Pod算力超42.5 exaflops，剑指Nvidia！专为Gemini推理优化，能效翻倍，HBM高达192GB。支持FP8/FP4数据类型，集成Vertex AI、JAX/PyTorch等，打造AI超级计算机，云原生应用迎来新选择！
-->

谷歌发布第七代AI芯片Ironwood (TPU7)，单Pod算力超42.5 exaflops，剑指Nvidia！专为Gemini推理优化，能效翻倍，HBM高达192GB。支持FP8/FP4数据类型，集成Vertex AI、JAX/PyTorch等，打造AI超级计算机，云原生应用迎来新选择！

> 译自：[Ironwood: Google's Answer to Nvidia in the AI Chip Wars](https://thenewstack.io/ironwood-googles-answer-to-nvidia-in-the-ai-chip-wars/)
> 
> 作者：Agam Shah

撇开[幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)不谈，过去的客户抱怨[谷歌的 Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)速度慢，尤其是在较大的上下文和 token 计数的情况下。

为了解决这个问题，该公司宣布正在构建一些迄今为止[最快的计算机](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/)，使用其名为 Ironwood 的新型 AI 芯片，即第七代 [TPU](https://thenewstack.io/ai-hardware-and-open-models-headed-in-the-linux-direction/)，该芯片在 [Google Cloud Next](https://cloud.withgoogle.com/next/25) 上发布。

每个服务器，[Google](https://cloud.google.com/?utm_content=inline+mention) 称之为“pod”，将互连 9,216 个 Ironwood 芯片，这些芯片可以联合作为一个大型芯片运行。一个 pod 可以提供 42.5 exaflops 的 AI 性能。

“世界排名第一的超级计算机 El Capitan 每个 pod 支持 1.7 exaflops。Ironwood 提供的计算能力是其 24 倍以上，”Google 机器学习、系统和云 AI 副总裁兼总经理 Amin Vahdat 在新闻发布会上说。

9,216 个 Ironwood 芯片中的每一个都提供 4,614 teraflops 的 FP8 性能，并通过 Google 的专有技术连接在一起。

Google 在一份新闻稿中表示，互连的芯片采用液体冷却，“跨越近 10 兆瓦”。

这需要大量的能量，但这是 Google 锁定可靠 AI 性能的唯一方法。

## Google 需要 Ironwood

Google 组织世界的数字信息，并通过搜索和现在的 AI 将其呈现给用户。

Ironwood 芯片将定义 Google 通过 Gemini 呈现信息的速度。

对 AI 的需求正在压倒数据中心，而像 Ironwood 这样更快的芯片可以满足需求。Ironwood 是 Google 自 2015 年以来发布的 AI 芯片系列的第七个版本。

Vahdat 说：“作为一个行业，在过去的八年中，我们看到对训练和服务模型的需求同比增长了 10 倍。这是一个 1 亿的因子。”

该芯片旨在运行在 Google Cloud 基础设施中运行的 Gemini 工作负载。它不会在现货市场出售。

Ironwood 比去年发布的第六代 TPU（称为 Trillium）更快、更节能。

Vahdat 说：“Ironwood TPU 的能效是我们第六代 TPU Trillium 的两倍。”

每个 Ironwood TPU 都有 192GB 的 HBM 内存，是 Trillium 上 32GB HBM（高带宽内存）内存的六倍。

片上 HBM 容量比 AI 芯片速度更重要。更高的内存有助于芯片保留和处理更快的 AI 处理所需的大量数据。

![](https://cdn.thenewstack.io/media/2025/04/e5bdda24-screenshotironwood-1-1-1024x505.png)

## 竞争

Google 的 Ironwood 来得正是时候。其他专有 AI 模型在竞争芯片上运行。

Nvidia [上个月宣布](https://thenewstack.io/nvidia-unveils-next-gen-rubin-and-feynman-architectures-pushing-ai-power-limits/)了其最新的 Blackwell Ultra 芯片和下一代 Rubin 和 Feynman GPU。这些芯片为 OpenAI 最新的 AI 模型提供动力。

Amazon 将在今年交付其 Trainium3 AI 芯片。Anthropic 的 Claude 模型针对 Trainium2 芯片进行了优化。

Microsoft 目前使用 Nvidia GPU，但已部署了自己的 AI 加速器，称为 [Maia](https://thenewstack.io/why-microsoft-has-to-save-openai/)，用于推理工作负载。

## 专为推理而构建

Vahdat 说，Ironwood（Google 也称为 TPU7）是第一个为推理和强大思考而构建的 TPU。

在早期，AI 芯片是为训练而构建的。但 AI 现在完全是关于推理，具有更智能的模型，例如 OpenAI o1 和 DeepSeek R1，它们可以在提供答案之前进行推理和思考。

Vahdat 说：“这不再是关于输入到模型中的数据，而是模型在训练后可以对数据做什么。”

Nvidia CEO Jensen Huang 上个月表示，与非推理模型相比，推理模型将推动计算需求增长 100 倍以上。

Ironwood TPU 仅用于服务 Gemini，目前为 2.5 版本。Nvidia 的 GPU 更通用，可以运行除 Gemini 之外的几乎任何模型。

Vahdat 说：“TPU 的发布建立在致力于为我们的客户提供 AI 硬件可选性的承诺之上，包括我们广泛的基于 Nvidia GPU 的产品。”

对更快芯片的需求正压倒像 Google、OpenAI 和 Microsoft 这样的公司。因此，GPU 制造商 Nvidia 和 AMD 也在每年推出新的 AI 芯片。而以前，芯片的发布周期为一年半到两年。

## 可用性

Ironwood TPU 将提供两种配置：TPU7 和 TPU7x。一位 Google 女发言人告诉 The New Stack，这些技术名称将会在 Google 客户的控制台、文档和账单中显示。

Google 没有宣布 Ironwood 在 Google Cloud 中的具体可用日期。

但可以肯定的是，Ironwood TPU 将是最昂贵的，而像 Trillium (TPU6) 或 TPU v5 产品等较旧的 TPU 的价格将会下降。客户可以选择这些芯片来满足他们的 AI 工作负载。

“有些人可能需要 Ironwood 的高级推理能力，而另一些人可能更喜欢 TPU v5e 的经济高效的训练，”这位 Google 女发言人说。

## 数据类型

上面反映的 Ironwood 峰值性能数字是针对 FP8 数据类型的，FP8 是推理的首选数据类型。

“Ironwood 还支持 FP4，客户可以通过它以较低的精度额外提高数据移动和电源效率，”这位女发言人说。

Nvidia 上个月在 GTC 上分享的 GPU 性能基准测试是基于 FP4 数据类型的。与 FP8 相比，FP4 等较低精度的数据类型通常会产生不太准确的响应，但功耗效率要高得多。

Ironwood 还支持需要高精度数据类型的训练工作负载。

这位 Google 女发言人说，训练工作负载“受益于 Ironwood 实现的大规模并行处理和高效的内存访问”。

## Google 的堆栈

Google 的全球数据中心基础设施分为“[AI 超级计算机](https://cloud.google.com/solutions/ai-hypercomputer?hl=zh-cn)”，其中包含 AI 芯片、存储、网络和内存。

Ironwood 为 AI 超级计算机提供了更多的能力。

开发人员可以进入超级计算机并定义他们需要的芯片类型，例如 GPU、TPU 或 CPU。选择取决于问题。

超级计算机软件层包括 Vertex AI，它托管 Gemini、Llama、Gemma 和其他 AI 模型。

开发人员可以选择 AI 框架和参考实现——例如 JAX 或 [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) ——以及编排软件，例如 [GKE](https://thenewstack.io/run-a-google-kubernetes-engine-cluster-for-under-25-month/) 或 [Slurm](https://thenewstack.io/kubernetes-evolution-from-microservices-to-batch-processing-powerhouse/)。

在 Google Cloud Next 上宣布的一个新层将 AI 代理作为参与或响应查询的一种方式。Gemini 2.5 是一个推理模型。

Google 通过服务级别合同保证 Google Cloud 中 AI 服务的可用性和交付。