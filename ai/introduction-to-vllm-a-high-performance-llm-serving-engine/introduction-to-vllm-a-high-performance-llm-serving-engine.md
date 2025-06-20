<!--
title: vLLM 简介：一款高性能LLM服务引擎
cover: https://cdn.thenewstack.io/media/2025/06/8e0be2d8-vllm.png
summary: 🚀颠覆认知！高性能 LLM 服务引擎 vLLM 横空出世！🔥创新 PagedAttention 机制，突破内存瓶颈；连续 Batching 加速推理，集成 KServe 和 Kubernetes 实现云原生部署。支持 OpenAI API，兼容 NVIDIA、AMD 等多平台，更有 Docker 镜像一键部署！
-->

🚀颠覆认知！高性能 LLM 服务引擎 vLLM 横空出世！🔥创新 PagedAttention 机制，突破内存瓶颈；连续 Batching 加速推理，集成 KServe 和 Kubernetes 实现云原生部署。支持 OpenAI API，兼容 NVIDIA、AMD 等多平台，更有 Docker 镜像一键部署！

> 译自：[Introduction to vLLM: A High-Performance LLM Serving Engine](https://thenewstack.io/introduction-to-vllm-a-high-performance-llm-serving-engine/)
> 
> 作者：Janakiram MSV

开源的 [vLLM](https://github.com/vllm-project/vllm) 代表了[大型语言模型](https://thenewstack.io/llm/)（LLM）服务技术的一个里程碑，它为开发人员提供了一个快速、灵活且可用于生产的推理引擎。

该库最初由加州大学伯克利分校的 [Sky Computing Lab](https://sky.cs.berkeley.edu/) 开发，现已发展成为一个社区驱动的项目，旨在解决 LLM 应用中内存管理、吞吐量优化和可扩展部署的关键挑战。该库在注意力机制和内存分配方面的创新方法使其成为寻求大规模高效部署 LLM 的组织的领先解决方案。

vLLM 作为 AI 推理生态系统中的一项基础技术，其快速增长得到了主要行业参与者的有力支持，其中最值得注意的是 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)。Red Hat 已将 vLLM [集成](https://www.redhat.com/en/about/press-releases/red-hat-unlocks-generative-ai-any-model-and-any-accelerator-across-hybrid-cloud-red-hat-ai-inference-server)到其基于 OpenShift 的 AI 推理服务器的核心。OpenShift 和 vLLM 之间的集成通过 OpenShift AI 的模型服务平台实现，该平台利用 [KServe](https://github.com/kserve/kserve) 来大规模部署和管理 AI 模型。

由 Google 和 Red Hat 最近推出的开源项目 [llm-d](https://llm-d.ai/) 由 vLLM 的高效推理引擎提供支持，从而能够大规模地进行分布式、Kubernetes 原生的 LLM 服务。

## 核心架构和主要特性

### PagedAttention 机制

vLLM 性能优势的基石在于其 [PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html) 算法，该算法从根本上重新构想了在推理期间如何管理键值 (KV) 缓存内存。与分配连续内存块的传统方法不同，PagedAttention 将 KV 缓存划分为固定大小的块，这些块可以存储在非连续的内存位置中。这种设计灵感来自操作系统虚拟内存技术，可实现高效的内存共享并显着减少碎片。

PagedAttention 系统维护块表，该表将每个请求的逻辑 KV 块映射到物理内存块，从而在内存分配方面提供灵活性，同时确保最佳的 GPU 利用率。在处理序列时，该算法使用分块方法计算注意力分数，将键和值向量分成固定大小的块，以实现高效的内存管理和计算。这种方法允许 vLLM 处理动态序列长度，而不会产生与传统填充技术相关的内存浪费。

### 连续批处理和动态调度

vLLM 实现了连续批处理，也称为动态批处理或迭代级调度，它在单个生成步骤的粒度上运行，而不是在整个序列的粒度上运行。这种方法消除了静态批处理系统中固有的队首阻塞问题，在这种系统中，快速完成的请求必须等待较慢的请求完成。该系统维护一个请求队列，并在每次前向传递时动态地组成批次，并在容量允许时将新请求添加到当前正在运行的批次中。

连续批处理机制提供了几个关键优势，包括通过持续的 [GPU 利用率](https://thenewstack.io/developers-can-now-uber-gpus-with-nvidias-lepton-platform/) 提高吞吐量，由于请求会立即处理而减少平均延迟，以及通过最大限度地减少空闲时间来提高资源利用率。当序列完成生成时，它们的资源会立即释放，并在下一个处理步骤中可用于新请求。

### 高级优化特性

vLLM 结合了多种优化技术，可增强各种部署场景（包括 CPU 和 GPU）的性能。该系统支持各种量化方法，包括 GPTQ、AWQ、INT4、INT8 和 FP8，从而可以在资源受限的环境中进行高效部署。[推测解码](https://x.com/karpathy/status/1697318534555336961) 功能允许系统主动生成潜在的未来令牌，从而减少交互式应用程序中的延迟。

该库实现了分块预填充功能，该功能通过将长输入序列分解为可管理的块来有效地处理它们。此功能对于需要广泛上下文窗口或文档处理功能的应用程序特别有价值。此外，vLLM 通过集成 FlashAttention 和 FlashInfer 来支持优化的 CUDA 内核，从而为硬件提供特定的优化以实现最佳性能。
## 模型兼容性和支持

### 支持的模型架构

vLLM 通过与 Hugging Face [Transformers](https://huggingface.co/docs/transformers/en/index) 的无缝集成，提供了对流行模型架构的广泛兼容性。该系统支持各种任务的生成模型和池化模型，用户可以通过命令行参数指定任务。对于本地不支持的模型，vLLM 通过其 Transformers 后端提供兼容性，从而可以在获得官方支持之前使用自定义模型。

该库保持对基于解码器的语言模型的广泛支持，并不断开发视觉语言模型功能。通过完善的 API 可以促进自定义模型集成，这些 API 允许开发人员扩展 vLLM 的功能以适应专门的架构。该系统会自动检测兼容的模型，并且可以在需要时强制使用特定的实现。

### 硬件平台支持

vLLM 的硬件兼容性涵盖多个供应商和架构，支持 NVIDIA GPU、AMD CPU 和 GPU、Intel CPU、Gaudi 加速器、IBM Power CPU、TPU 以及 AWS Trainium 和 Inferentia 加速器。量化兼容性矩阵展示了跨硬件平台的全面支持，尽管某些方法针对特定的 GPU 世代进行了优化。

NVIDIA GPU 支持范围从较旧的 Volta 架构到最新的 Hopper 系统，不同的量化方法针对特定的计算能力进行了优化。AMD GPU 支持包括与现代 RDNA 架构的兼容性，而 Intel GPU 支持为不同的部署环境提供了选择。这种广泛的硬件兼容性使组织能够利用现有基础设施，同时保持最佳的性能特征。

## 部署选项和集成

### 基于容器的部署

vLLM 通过 Docker Hub 上提供的[官方容器镜像](https://hub.docker.com/u/vllm)，提供全面的 [Docker 支持](https://thenewstack.io/containers-in-the-age-of-ai-a-chat-with-new-docker-president-mark-cavage/)。主要的容器镜像 vllm/vllm-openai 提供了一个完整的 OpenAI 兼容服务器环境，可以跨各种容器编排平台进行部署。容器部署通过 [NVIDIA Container Runtime](https://developer.nvidia.com/container-runtime) 支持 GPU 加速，并为张量并行操作提供适当的共享内存配置。

对于需要特定依赖项或配置的组织，支持自定义容器构建。可以使用额外的层扩展 Docker 镜像，以满足专门的需求，例如音频处理功能或 transformers 的开发版本。容器部署简化了从开发环境到生产环境的迁移过程，同时保持了跨不同部署目标的一致性。

### Kubernetes 和生产编排

通过全面的 YAML 配置和 Helm charts，完全支持 [Kubernetes 部署](https://thenewstack.io/kubernetes/)。部署过程需要 NVIDIA [Kubernetes Device Plugin](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/k8s-device-plugin) 用于 GPU 资源管理，并需要适当的持久卷配置用于模型缓存。vLLM 的 Kubernetes 集成通过副本管理支持水平扩展，并通过标准 Kubernetes 网络支持服务发现。
vLLM 生产堆栈提供企业级部署功能，包括上游兼容性、通过 Helm charts 简化的部署以及通过 [Grafana dashboards](https://thenewstack.io/grafana-11-no-need-to-create-promql-queries-for-prometheus/) 集成的**可观测性**。这种面向生产的方法包括多模型支持、模型感知路由、快速引导和 KV 缓存卸载功能等功能。该生产堆栈专为 LLM 工作负载而设计，并针对高性能场景进行了优化。

### API 兼容性和集成

vLLM 提供了一个 OpenAI 兼容的 HTTP 服务器，该服务器实现了标准的 completions 和 chat API，从而可以与现有应用程序无缝集成。该服务器支持所有主要的 OpenAI API 端点，包括 completions、chat completions、embeddings 和音频转录，以及用于分词、池化和评分的附加自定义端点。超出 OpenAI 规范的额外参数可以通过 extra_body 参数传递，以增强功能。
API 服务器支持流式响应，用于实时应用程序，具有逐个令牌的输出生成，从而增强了交互式场景中的用户体验。身份验证通过 API 密钥处理，并且可以使用各种特定于模型的参数来配置服务器，包括生成配置和采样参数。与流行的 HTTP 客户端和官方 OpenAI Python 库的集成非常简单且有据可查。

vLLM 已成为 LLM 推理领域的一项变革性技术，为开发人员提供了部署大规模高性能语言模型所需的工具。其创新的 PagedAttention 机制和连续批处理功能解决了内存管理和吞吐量优化方面的根本挑战。全面的硬件支持、灵活的部署选项和 OpenAI 兼容的 API 使 vLLM 成为希望实施生产级 LLM 服务的组织的理想选择。

该库的积极开发和社区驱动的方法确保了持续的创新和适应快速发展的 AI 领域中出现的需求。凭借其经过验证的性能优势和强大的功能集，vLLM 代表了开发人员构建下一代 AI 驱动应用程序的战略投资。

在本系列的下一部分中，我将深入探讨 vLLM 的核心功能和推理管道。敬请关注。