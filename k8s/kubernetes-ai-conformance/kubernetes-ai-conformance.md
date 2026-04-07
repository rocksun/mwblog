<!--
title: Google 推出 Kubernetes AI 一致性计划，赋能集群机器学习
cover: https://nerds.xyz/wp-content/uploads/2026/04/kubernetes-ai-conformance-google-ai-kubernetes.png
summary: 谷歌推出 Kubernetes AI 一致性计划，确保集群能更好地支持 AI 工作负载，解决资源分配、调度、扩缩和可观测性等关键难题。
-->

谷歌推出 Kubernetes AI 一致性计划，确保集群能更好地支持 AI 工作负载，解决资源分配、调度、扩缩和可观测性等关键难题。

> 译自：[Google launches Kubernetes AI Conformance program to prepare clusters for machine learning](https://nerds.xyz/2026/04/kubernetes-ai-conformance/)
> 
> 作者：Brian Fagioli

人工智能工作负载正在*爆发式增长*，而为其提供支持的基础设施也开始感受到压力。这一现实似乎正在推动 Google 和更广泛的 Kubernetes 社区采取新举措，他们刚刚[公布](https://opensource.googleblog.com/2026/04/kubernetes-goes-ai-first-unpacking-the-new-ai-conformance-program.html)了一项名为“认证 Kubernetes AI 一致性计划”。

这个想法非常直接。Kubernetes 已经有一个认证系统，可以确保平台在不同供应商之间行为一致。新的 AI 一致性层增加了专门针对机器学习和 AI 工作负载的额外要求。换句话说，如果公司要在 Kubernetes 集群上运行大规模模型和推理管道，生态系统需要一个通用标准来确保事情确实按照开发人员的预期运行。

传统的 Kubernetes 环境最初是为云应用程序设计的。例如无状态 Web 服务、微服务和可扩展的后端系统。AI 工作负载则完全不同。训练模型或提供推理通常涉及专用硬件、大量的网络需求以及与典型应用程序行为不同的数据管道。

这正是这项新认证工作发挥作用的地方。

AI 一致性计划本质上是在现有 Kubernetes 认证测试之上建立的。任何想要获得“AI 就绪”徽章的平台都必须首先通过常规的 Kubernetes 检查，然后满足针对 AI 工作负载的额外要求。

这项工作正在开源社区中开展，并有多个公司参与。来自 Google 的工程师以及与 Microsoft 和 Red Hat 相关的贡献者都参与其中。目标是创建一个适用于整个行业的东西，而不是将 AI 基础设施锁定在某个特定的云提供商。

最大的变化之一围绕着动态资源分配（Dynamic Resource Allocation，简称 DRA）。开发人员可以根据特定属性（例如内存大小或硬件功能）请求加速器，而不是请求通用 GPU。对于部署模型的数据科学家来说，这种额外的控制级别可以带来真正的改变。

调度是该计划试图解决的另一个痛点。大型分布式训练作业经常遇到令人沮丧的情况，即某些容器启动了，而其他容器却在等待资源。这浪费了昂贵的 GPU 时间。AI 一致性指南提倡一种“全有或全无”的调度模型，因此作业只有在所有资源都准备好之后才会开始。

自动扩缩也得到了调整。通常 Kubernetes 会根据 CPU 或内存使用情况进行扩缩。AI 工作负载更关心加速器活动。在新计划下，集群需要支持根据 GPU 或 TPU 利用率等指标进行扩缩。

可观测性是这难题的另一部分。大规模运行 AI 需要了解与加速器相关的性能指标。新的规范规则推动平台公开标准化指标，以便团队可以更轻松地跟踪推理延迟、吞吐量和硬件健康状况。

主要的托管 Kubernetes 平台已经与这项工作保持一致。Google Kubernetes Engine 和 Azure Kubernetes Service 等服务有望支持认证所需的功能。

对于今天正在构建 AI 基础设施的人来说，这听起来可能像是大量的管道工作。但现实很简单。AI 工作负载正在成为现代基础设施的正常组成部分。如果 Kubernetes 想继续成为云原生计算的默认平台，它就必须顺利处理这些工作负载。

Kubernetes 社区计划在 2026 年全年扩展 AI 一致性计划，包括自动化认证测试以及对推理模式和安全性的额外要求。

从长远来看，希望 AI 就绪性能够简单地成为 Kubernetes 本身的一部分，而不是组织必须自行设计的东西。