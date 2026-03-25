Kubernetes 与人工智能的结合已在 llm‑d 中实现，这是一个可复制的 Kubernetes 蓝图，用于在任何云上、任何加速器上部署任何模型的推理堆栈。

周二在阿姆斯特丹举行的 [KubeCon Europe 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) 上，IBM Research、Red Hat 和 Google Cloud 宣布将他们开源的分布式推理框架 [llm‑d](https://llm-d.ai/) 捐赠给 [云原生计算基金会 (CNCF)](https://www.cncf.io/)，作为一个沙盒项目。

此举得到了创始合作者 NVIDIA 和 CoreWeave 以及 AMD、Cisco、Hugging Face、Intel、Lambda 和 Mistral AI 的支持，将 llm‑d 确立为一个社区治理的、可扩展的、供应商中立的大语言模型 (LLM) 推理蓝图。

llm‑d 于 2025 年推出，[旨在使基础模型的规模化服务可预测、可移植且云原生](https://www.redhat.com/en/blog/what-llm-d-and-why-do-we-need-it)。它将 [推理从即兴的、逐模型的挑战转变为一个可复制的、生产级的、基于 Kubernetes 的系统](https://thenewstack.io/kubernetes-glorified-ai-host/)。Llm-d 由 [Neural Magic 创建，该公司于 2025 年被 Red Hat 收购](https://thenewstack.io/red-hats-ai-platform-now-has-an-ai-inference-server/)。IBM Research 杰出工程师 Carlos Costa 在 KubeCon 的主题演讲中表示，IBM 的目标是“使大规模模型服务成为一流的云原生工作负载”。

具体来说，llm-d 是一个开源的 Kubernetes 原生框架，用于将大语言模型 (LLM) 推理作为分布式、生产级工作负载运行。这在实践中意味着：

*   Llm-d 将 LLM 服务转变为一个分布式系统：它将推理分解为预填充（prefill）和解码（decode）阶段（解耦），并在不同的 pod 上运行它们。这意味着你可以独立地扩展和调整每个阶段。
*   它添加了一个 LLM 感知的路由和调度层。这是通过一个网关扩展实现的，该扩展根据 [KV 缓存](https://huggingface.co/blog/not-lain/kv-caching) 状态、pod 负载和硬件特性来路由请求，以提高延迟和吞吐量。
*   最后，它在 Kubernetes 之上提供了一个模块化堆栈，使用 [vLLM](https://vllm.ai/) 作为推理网关，以及相关组件，为您提供一个可重用的蓝图，适用于“任何模型、任何加速器、任何云”。

从概念上讲，vLLM 充当快速推理引擎，而 llm‑d 则提供了一个操作层，允许您通过智能调度、缓存感知路由和针对 LLM 流量而非通用 HTTP 工作负载进行调整的自动扩缩，在 GPU/TPU 集群上运行该引擎。

在新闻发布会上，前 Neural Magic 首席执行官、现任 Red Hat 高级副总裁兼 AI 首席技术官 Brian Stevens 表示：“我们做了很多工作来引入新的加速器。TPU、AMD、Nvidia 以及一大批其他加速器。我们真的希望看到它们有办法融入。因此，就像 Linux 一样，你可以运行任何硬件、任何应用程序，通过 llm-d，任何模型、任何加速器。”

这比旧的推理运行方式更快更便宜。Google Cloud 的早期测试显示，在代码补全等用例中，“[首次生成 token 时间缩短了两倍](https://cloud.google.com/blog/products/ai-machine-learning/enhancing-vllm-for-distributed-inference-with-llm-d)”，从而实现了更灵敏的应用程序。这是因为传统的自动扩缩器、通用 API 和请求路由并未针对依赖高效 KV 缓存管理、预填充/解码编排和异构加速器的有状态推理工作负载而设计。

Llm‑d 正面解决了这些问题。它引入了前缀缓存感知路由和预填充/解码解耦，允许推理阶段独立扩缩。它支持跨 GPU、CPU 和存储层级的层次化缓存卸载，在不超载加速器内存的情况下启用更大的上下文窗口。

其流量和硬件感知自动扩缩器动态适应工作负载模式，而非依赖基本的利用率指标。它还旨在与新兴的 Kubernetes API 协同工作，例如 [Gateway API Inference Extension (GAIE)](https://gateway-api-inference-extension.sigs.k8s.io/) 和 [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/)。这三者共同旨在使分布式推理成为一流的 Kubernetes 工作负载。

该项目的贡献者将 llm‑d 描述为组织从实验转向生产的“一条明亮之路”。Carlos Costa 说：“我们为您测试过。我们对其进行了基准测试。我们经历了痛苦。”该框架提供可重现的基准、经过验证的部署模式，以及与 Nvidia GPU 到 Google TPU 再到 AMD 和 Intel 硬件等主要加速器系列的兼容性。

IBM Research 人工智能平台副总裁 Priya Nagpurkar 在 llm-d 主题演讲中强调，推理现在需要 Kubernetes 为微服务带来的相同操作成熟度。“您需要 Kubernetes 为上一个时代提供的规模、分布式和可靠性，同时要认识到这是一种非常不同的工作负载。”

通过将 llm‑d 贡献给 CNCF，IBM 及其合作伙伴正在押注 AI 推理很快将像 Prometheus 或 Envoy 一样，成为云原生堆栈的基础。

IBM 认为此次捐赠对于分布式推理的部署和管理标准化至关重要。Carlos Costa 说：“CNCF 正在成为 AI 基础设施的家园。在这里，通用模式、API 和治理汇聚一堂，以便每个人都可以在相同的‘剧本’上进行构建。”

展望未来，llm-d 的下一个开发周期将重点关注扩展 llm‑d 在多模态工作负载、Hugging Face [多 LoRA](https://huggingface.co/blog/multi-lora-serving) 优化方面的能力，以及与 vLLM 的更深入集成。具体来说，[Mistral AI](https://mistral.ai/) 已经贡献代码，以推动解耦服务方面的开放标准。

IBM Research 将继续探索推理和训练的交叉点，包括强化学习和自优化 AI 基础设施。正如 Carlos Costa 所说，“创建一个共同的基础堆栈可以让生态系统专注于推动 AI 发展，而不是重复构建基础。”CNCF 作为其新家，llm‑d 有望成为云原生 AI 时代的基石。