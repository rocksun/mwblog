<!--
title: Groundcover 瞄准多步工作流，填补 AI 智能体监控的可见性空白
cover: https://cdn.thenewstack.io/media/2026/04/0954b76d-rifky-nur-setyadi-vxelfrt6l04-unsplash-scaled.jpg
summary: Groundcover 扩展其 AI 可观测性服务，利用 eBPF 技术在无需埋点的情况下，深度监控多步智能体工作流。该方案通过关联内核级数据与基础设施状态，解决了传统工具难以追踪动态 AI 决策及成本归因的难题。
-->

Groundcover 扩展其 AI 可观测性服务，利用 eBPF 技术在无需埋点的情况下，深度监控多步智能体工作流。该方案通过关联内核级数据与基础设施状态，解决了传统工具难以追踪动态 AI 决策及成本归因的难题。

> 译自：[Groundcover eyes visibility gap in agentic AI monitoring by targeting multi-step workflows](https://thenewstack.io/groundcover-ai-observability-agents/)
> 
> 作者：Adrian Bridgwater

云监控专家 [Groundcover 本周三宣布扩展其 AI 可观测性服务](https://www.groundcover.com/)。此举标志着该公司增加了对智能体 AI（agentic AI）系统的原生支持，并全面兼容 [Google Vertex AI](https://thenewstack.io/googles-vertex-ai-platform-gets-freejacked/)——这家云巨头用于构建和训练机器学习模型的平台。

为了让组织清晰地洞察智能体功能如何做出决策，Groundcover 将其技术定位为一扇窗口，通过它可以看到组织的应用资产如何在不同模型中以及整个考虑过程中使用 AI，包括成本、[延迟](https://thenewstack.io/why-latency-is-quietly-breaking-enterprise-ai-at-scale/)、提示词使用、智能体行为和工具执行。简单来说，软件工程团队可以追踪每一次大语言模型（LLM）的交互。

Groundcover 采用 BYOC（[自带云](https://thenewstack.io/saas-is-broken-why-bring-your-own-cloud-byoc-is-the-future/)）模式提供服务，在组织的本地云中运行，因此所有数据都在客户的基础设施和环境中进行处理。

## 一种全新的可见性鸿沟

随着各组织现在将大语言模型集成到生产系统中，他们正遇到一种全新的可见性鸿沟。

Groundcover 产品副总裁 [Orr Benjamin](https://www.linkedin.com/in/orr-benjamin/) 告诉 *The New Stack*，传统的监控工具是为确定性软件设计的，而不是为由动态提示词驱动输出的系统设计的。

“当你从传统服务转向多步智能体工作流时，[日志、指标和短链路追踪](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/)这些经典的可观测性支柱开始失效，”Benjamin 表示。“团队面对的不再是请求从一个服务连接到另一个服务时的 20 跳[微服务追踪](https://aws.amazon.com/what-is/distributed-tracing/)，而可能是一个长达两小时的会话和 5 万次工具调用，因此核心挑战变成了如何以用户关心的方式重建并总结实际发生的情况。”

> “当你从传统服务转向多步智能体工作流时，日志、指标和短链路追踪这些经典的可观测性支柱开始失效。” —— Groundcover 产品副总裁 Orr Benjamin。

由于这些挑战，Groundcover 表示，他们看到许多团队难以理解 AI 驱动的功能在现实环境中的表现，包括哪些输入驱动了输出、响应如何变化以及使用如何影响成本。这种可见性的缺乏使得确保可靠性、优化性能以及扩展 AI 驱动的应用变得困难。

## 无需埋点

自从 2025 年 8 月推出 [LLM 可观测性](https://www.groundcover.com/ai-observability/llm-observability)以来，Groundcover 已在其客户群的生产 AI 环境中运行，通过其专利的 [eBPF 传感器](https://thenewstack.io/what-is-ebpf/)自动捕获 LLM 交互。这是一种轻量级数据采集代理，在内核层“监听”所有服务器事件，在使用前无需进行“埋点”（即通过编码实现）。因为不需要埋点，所有数据都保留在客户的云端。

Groundcover 的这次发布旨在解决该公司所说的现实生产部署中暴露的下一个未解难题：对多步智能体系统的可见性。

“因为 Groundcover 通过 eBPF 在内核层（应用层之下）捕获数据，它看到的是智能体实际在做什么，而不是应用程序报告发生了什么。如果一个编码智能体可以在应用层注入追踪信息或操纵日志，那么你的可观测性就只能和智能体本身一样诚实，”Benjamin 说道。

他解释说，这一点至关重要，尤其是随着智能体变得更加自主。由于基础设施上下文是与 AI 行为一并捕获的，这意味着如果智能体询问：“为什么我的成本激增？”，系统可以提供一个基于完整数据上下文的答案，显示 LLM Token 成本激增是因为底层的 [Kubernetes 节点内存不足](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)，导致服务受限并推高了重试次数。

在 Groundcover 的新功能方面，AI 可观测性现在可以呈现完整的智能体执行追踪。这意味着每一次模型调用、每一次[工具调用](https://www.ibm.com/think/topics/tool-calling)（及其参数，即管理与外部工具、API 或系统交互的结构化参数）以及连接它们的推理路径。可配置的关注级别让工程师能够在合适的维度工作，从供应商级别的聚合数据一直到单个 Span 的细节。

## Span 级别的 Token 追踪

准确的成本归因包括提示词缓存。Token 成本在 Span 级别（当特定的 Token 序列代表一个独特的实体或短语时）进行跟踪，并考虑了现代 LLM API 的完整定价复杂性，正确区分常规输入 Token、缓存创建 Token 和缓存读取 Token。团队可以查看各个智能体的运行情况以及会话的实际成本。

如上所述，系统也提供了对 Google Vertex AI 的支持，这意味着 Groundcover 的自动捕获现在扩展到了在 Google Cloud 托管 AI 基础设施上构建的团队，所有可观测性数据都保留在客户自己的环境中，且无需任何埋点。

> “一个看起来像是 AI 问题的 Token 使用激增，实际上可能是因为 Kubernetes 节点内存不足导致重试。”

Benjamin 强调了这些进展，并表示该公司的平台已经处理了数据从受监控环境移动到托管后端的方式，即它的设计旨在保持数据封闭，与传统架构相比，降低了 95% 以上的网络成本，同时确保数据永远不会传输给第三方。他说，这是一种刻意的架构选择，使 Groundcover 的多云支持名副其实，而非虚有其表。

该公司再次提醒我们，Groundcover 支持 AWS、GCP 和 Azure，因为它是真正的 BYOC，无论这个“C”（云）是什么。

由于 eBPF 传感器在内核层捕获一切，无论应用程序调用哪个 LLM 供应商，Groundcover 都能在不触碰代码的情况下，提供对推理路径、Token 使用和响应质量的可观测性。这种将 LLM 行为与基础设施遥测数据相连接的答案，只有当两者存在于同一个平台、同一时间线、使用同一查询语言时才可能实现……而这正是 Groundcover 认为它已为多步智能体工作流时代提供了全面可观测性的基石。