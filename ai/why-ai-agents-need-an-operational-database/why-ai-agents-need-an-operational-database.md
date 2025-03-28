
<!--
title: 为什么AI Agent需要一个运营数据库
cover: https://cdn.thenewstack.io/media/2025/02/4041ef62-ai.jpg
-->

一个专门为速度、可扩展性和低延迟而设计的平台，确保 AI 代理能够有效地收集、处理和交付上下文丰富的可观测性结果。

> 译自 [Why AI Agents Need an Operational Database](https://thenewstack.io/why-ai-agents-need-an-operational-database/)，作者 Tim Rottach。

AI Agent 应用程序有望改变员工和客户与计算机系统交互的方式。通过收集数据、推理和执行任务，这些 Agent 将在无数当前用例中自动化人类工作流程——从内部支持机器人到面向客户的复杂服务——遍及各个行业。

有些人正在寻找分析数据库来支持这些 Agent。然而，[AI Agent](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) 本质上是运营性的，很像传统的 Web 应用程序、移动应用程序和 [microservices](https://thenewstack.io/microservices/)。认识到这种区别对于选择正确的数据平台至关重要。

## 什么是 AI Agent，它们如何工作？

与仅限于严格输入和预定义逻辑的传统应用程序不同，AI Agent 与其环境动态交互。它们不断接收和处理来自多个来源的数据，执行实时推理并自主执行任务。它们使用各种工具、功能和系统提示来检索相关数据、提出下一个问题、完善其推理并采取行动。

由于 Agent 依赖于 [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) 或其他高级机器学习技术，因此它们需要实时运行，并且需要支持频繁、低延迟的读取和写入操作的数据基础设施。这就是运营数据库（一种专为即时、持续的交互而设计，而不是延迟的批处理）必不可少的原因。

## 数据源 – 零售示例

零售环境中的典型 AI Agent 可能会使用各种运营数据，结合经典数据和 AI 特定数据。以下是一些示例：

*   **用户个人资料和偏好：** 支持高度个性化的推荐和客户体验。
*   **带有媒体的产品目录：** 允许更丰富的用户体验。
*   **库存数据：** 确保商品有库存且方便履行。
*   **Web 调用和外部 API：** Agent 可以检索其他信息（例如名人关联、上下文评论或市场情绪）以增强推荐。
*   **历史销售数据：** 支持追加销售、交叉销售和预测客户接下来可能购买的商品。
*   **非结构化内容：** 可以集成诸如详细说明产品使用或保养说明的 PDF 之类的文档，以提高 Agent 响应的质量。
*   **向量嵌入：** [语义搜索的必需品](https://thenewstack.io/the-future-of-search-is-vector/) 和检索增强生成 (RAG)，无需重新训练自定义模型即可显着改善 LLM 响应。

Agentic AI 还需要维护有关开发人员创建的工具和功能的信息。此元数据可帮助 Agent 选择要调用哪个功能或数据源，从而不断发展其技能。此外，语义和对话缓存允许 Agent 重用现有上下文，通过最大限度地减少对昂贵的 LLM 端点的重复请求来提高速度并降低成本。

随着提示和工具的发展，系统必须捕获并维护交互历史记录，包括记录、决策和中间推理步骤。对于其他行业，核心运营数据类型可能有所不同（例如，制造业中的传感器读数），但基本原则保持不变：AI Agent 需要能够处理各种数据格式、频繁更新和实时可访问性的强大运营数据库。

## 为什么运营数据库很重要

使用多种不同的技术（一种用于缓存，另一种用于向量搜索，另一种用于事务）会降低性能、阻碍管理并使数据治理复杂化。为了使 AI Agent 能够及时交付结果，所有这些数据交互都必须以最小的延迟发生。

运营数据库擅长高速、高并发的工作负载，这些工作负载需要实时读取和写入。它们通常还提供强大的复制和集群功能，以确保高可用性，这对于必须保持响应的 AI 驱动的应用程序至关重要。

## 结论

AI Agent 将成为现代计算的基石。选择专门为速度、可扩展性和低延迟交互而设计的平台，可确保 AI Agent 可以有效地收集、处理和处理信息，从而为最终用户提供强大、上下文丰富的体验。就其本质而言，它们[生成并依赖于实时数据](https://thenewstack.io/using-real-time-data-to-unify-generative-and-predictive-ai/)，这使得运营数据库成为 AI Agent 的必需品。

Couchbase 推出了 Couchbase AI 服务，用于安全地与 AI 模型交互、整合非结构化数据，并提供开箱即用的语义和对话缓存。Agent Catalog 功能使开发人员能够更轻松地发现、管理和保护代理所需的工具和功能，并与 LangChain 等流行的 AI 框架无缝集成。此外，Couchbase 的多用途数据库无需使用多个单一用途的数据库，从而降低了应用程序开发的复杂性和成本。请点击[此处](https://www.couchbase.com/products/ai-services/)了解更多信息。
