
<!--
title: 高效LLM推理的六大框架
cover: https://cdn.thenewstack.io/media/2025/09/9e8f0a3a-milad-fakurian-e8ufcyxz514-unsplash.jpg
summary: 文章概述了多种 LLM 推理框架，包括 vLLM、Hugging Face TGI、SGLang、NVIDIA Dynamo、AIBrix 和 llm-d。它们在性能、可扩展性、编排和对不同部署场景的适用性方面各有优势，满足了低延迟、高吞吐量和异构硬件部署的需求。
-->

文章概述了多种 LLM 推理框架，包括 vLLM、Hugging Face TGI、SGLang、NVIDIA Dynamo、AIBrix 和 llm-d。它们在性能、可扩展性、编排和对不同部署场景的适用性方面各有优势，满足了低延迟、高吞吐量和异构硬件部署的需求。

> 译自：[Six Frameworks for Efficient LLM Inferencing](https://thenewstack.io/six-frameworks-for-efficient-llm-inferencing/)
> 
> 作者：Janakiram MSV

大型语言模型 ([LLM](https://thenewstack.io/llm/)) 推理技术发展迅速，这得益于对低延迟、高吞吐量以及跨异构硬件灵活部署的需求。

因此，涌现出各种各样的框架，每个框架都为扩展、性能和操作控制提供独特的优化。

从 vLLM 的内存高效的 PagedAttention 和连续批处理，到 Hugging Face TGI 的生产就绪的编排，再到 NVIDIA Dynamo 的解耦服务架构，生态系统现在涵盖了像 SGLang 这样的研究友好型平台、像 llm-d 这样的 Kubernetes 原生堆栈以及像 AIBrix 这样的面向企业的控制平面。本文将详细探讨这些框架，重点介绍它们的设计选择、技术创新以及对各种真实部署场景的适用性。

## vLLM：通过 PagedAttention 优化推理

[vLLM](https://docs.vllm.ai/en/latest/) 是一个高度优化的 LLM 推理引擎，最初在加州大学伯克利分校创建，现在由一个全球社区开发。该框架的核心是 [PagedAttention](https://arxiv.org/abs/2309.06180) 机制，它可以更高效、更精细地管理 transformer 注意力所需的键值缓存内存。这使得 vLLM 在处理具有长上下文窗口和大批量的工作负载时具有优势。另一项创新，[连续批处理](https://www.anyscale.com/blog/continuous-batching-llm-inference)，通过动态插入和移除批处理中的请求来保持 GPU 繁忙。其他功能包括通过语法约束的有限状态机进行引导解码、用于处理冗长提示的块预填充、前缀缓存共享、推测解码以及涵盖 NVIDIA、AMD、Intel 甚至新兴加速器平台的硬件支持。该引擎公开了一个与 OpenAI 兼容的 API，与 [Hugging Face 模型](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 无缝集成，并支持具有张量、管道和专家并行性的多 GPU、多节点部署。vLLM 通常被选择用于最大化服务器吞吐量和延迟至关重要的生产环境。

## Hugging Face TGI：企业就绪的推理服务

Hugging Face [Text Generation Inference](https://huggingface.co/docs/text-generation-inference/en/index) (TGI) 是使用 Hugging Face 模型生态系统的企业首选的服务平台。TGI 旨在有效地跨多个 GPU 和节点扩展 LLM 推理。主要功能包括智能批处理、量化支持（INT4、INT8、FP8）、GPU 加速和多模型编排。TGI 既可以作为独立服务运行，也可以与云部署工具集成，以实现强大的监控和自动缩放。它的 API 与 Hugging Face 和生产 REST 端点兼容，并提供用于可观测性和日志记录的丰富工具包。最近的版本侧重于跨 GPU 集群的高效分片、自回归令牌调度和高级量化，以最大限度地减少延迟并最大限度地提高吞吐量。TGI 在具有多样化模型需求以及高容量、多租户生产聊天或内容生成工作负载的组织中尤其受欢迎。

## SGLang：用于复杂 LLM 工作流程的可编程控制

[SGLang](https://docs.sglang.ai/) 将高级速度与对 LLM 运行时流程的可编程控制结合在一起。SGLang 专为研究人员和生产团队设计，提供了一种专用的脚本语言，用于链接操作和管理模型逻辑。[RadixAttention](https://arxiv.org/pdf/2312.07104) 是一项核心技术，它支持具有相似前缀的序列的缓存重用，这在代理和多模态应用中是一个显着的优势。后端运行时可以利用连续批处理、张量和管道并行性、推测解码和强大的多模型编排。SGLang 擅长处理多步骤推理任务或将 LLM 与其他 AI 工具链集成，包括视觉和检索模型。通过其结构化的脚本前端和运行时优化，SGLang 使开发人员能够对动态、复杂的 LLM 部署进行细粒度控制。

## NVIDIA Dynamo：用于超大规模性能的解耦服务

[NVIDIA Dynamo](https://www.nvidia.com/en-in/ai/dynamo/) 是一种最先进的分布式推理框架，它利用了 NVIDIA 在高性能计算和生成式 AI (GenAI) 方面的专业知识。Dynamo 围绕解耦服务构建，它将 LLM 请求的预填充和解码阶段分开。这种分离支持动态 GPU 分配，并在处理数千个并发客户端时实现更高的利用率。Dynamo 使用 Rust 进行编排，使用 Python 进行可扩展性编写，并且可以使用多个后端，包括 vLLM、[TensorRT-LLM](https://docs.nvidia.com/tensorrt-llm/index.html) 和自定义引擎。Dynamo 的主要技术进步是用于加速互连的 [NIXL 库](https://github.com/ai-dynamo/nixl)、动态 GPU 到请求的路由、高级缓存卸载和模块化插件支持。Dynamo 专为超低延迟、弹性和跨数据中心集群的快速扩展是优先事项的环境而设计。它已在寻求无与伦比的弹性的超大规模提供商和大型企业中获得认可。

## AIBrix：云原生编排和控制

[AIBrix](https://aibrix.readthedocs.io/latest/) 用作云原生、研究友好型 LLM 服务的编排和控制平面。AIBrix 本地构建于 Kubernetes 之上，协调动态调度、模型策略实施、自动缩放、LoRA 管理和开源后端（如 vLLM）的插件注册。混合粒度编排允许推理请求通过使用 [Kubernetes](https://thenewstack.io/kubernetes/) 和 [Ray](https://thenewstack.io/amazon-to-save-millions-moving-from-apache-spark-to-ray/) 的混合调度在多节点集群中传播。其分布式 KV 缓存可实现高效的内存使用和高可靠性，而高级路由和服务级别目标 (SLO) 驱动的优化即使在高负载下也能确保快速公平的服务。该框架还配备了管理多模态和多适配器部署的功能，支持微调、LoRA 更新和经济高效的资源放置。企业和研究团队因其策略驱动的工作流程、企业管理功能以及对开放 API 和适配器的完全支持而青睐 AIBrix。

## llm-d：Kubernetes 原生分布式服务

[llm-d](https://llm-d.ai/) 面向 Kubernetes 原生分布式 LLM 服务，建立在与 vLLM 的深度集成之上，并为研究和生产团队提供可扩展、可观测的推理堆栈。它引入了一个推理网关，用于处理快速请求路由、自动缩放和精细的资源管理。解耦服务将预填充和解码分开以降低延迟，而池化的 KV 缓存管理可改善内存占用。llm-d 架构强调操作遥测和透明部署，支持高可用性模式和与 OpenAI 兼容的端点。作为云原生平台，llm-d 在 Kubernetes 下管理的多 GPU NVIDIA 集群上运行效率最高，从而简化了 LLM 工作负载的部署和监控，以用于持续的研究、开发和商业部署。

这些框架反映了 LLM 服务朝着更高吞吐量、更低延迟、可编程编排和无缝扩展的演进。vLLM 和 Hugging Face TGI 因其速度和生态系统兼容性而被广泛用于生产。SGLang 被选择用于高级代理应用程序和多模态任务。NVIDIA Dynamo 通过数据中心级弹性和后端灵活性推动了边缘发展。AIBrix 为企业和研究工作流程提供编排和策略控制。llm-d 结合了 Kubernetes 原生扩展和强大的可观测性，用于持续的云实验和生产部署。

随着 LLM 工作负载的增长，这些解决方案将继续在性能、灵活性和可靠性方面设定新标准。