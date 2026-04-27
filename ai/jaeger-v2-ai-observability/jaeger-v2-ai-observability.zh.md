随着软件架构的演进，可观测性工具必须随之改变。当行业向微服务迁移时，分布式追踪成为了必需品。Jaeger 脱颖而出，成为工程师理解这些碎片化系统的核心工具。现在，随着企业将生成式 AI 应用和自主 Agent 集成到生产环境中，追踪需求再次发生变化。映射 AI Agent 的执行路径涉及提示词组装、向量数据库检索以及多次外部工具调用。

> “通过采用[模型上下文协议 (MCP)](https://modelcontextprotocol.io/)、[Agent 客户端协议 (ACP)](https://agentclientprotocol.com/) 和 [Agent-用户交互协议 (AG-UI)](https://ag-ui.com)，该项目正在构建一个工程师与 AI Agent 可以协同工作的环境。”

Jaeger 正在演进以应对这些新的工作负载。这一转型包含两个主要阶段。首先，该项目在 Jaeger v2 中重构了其核心架构，以原生集成 OpenTelemetry。其次，Jaeger 正在向标准数据可视化之外扩展。通过采用[模型上下文协议 (MCP)](https://modelcontextprotocol.io/)、[Agent 客户端协议 (ACP)](https://agentclientprotocol.com/) 和 [Agent-用户交互协议 (AG-UI)](https://ag-ui.com)，该项目正在构建一个工程师与 AI Agent 可以协同工作的环境。这有助于映射 AI 流水线的复杂执行路径，而这些路径往往超出了传统追踪工具的极限。

## 奠定基础：Jaeger v2

管理 AI 工作负载需要高效的[数据收集流水线](https://thenewstack.io/data-pipelines-serve-ai/)。这一需求引导了 CNCF 博客文章[《Jaeger v2 发布：核心集成 OpenTelemetry！》](https://www.cncf.io/blog/2024/11/12/jaeger-v2-released-opentelemetry-in-the-core/)中所详述的架构变革。

Jaeger v2 使用 OpenTelemetry Collector 框架替换了其原始的收集机制。这种方法将指标、日志和追踪整合到一个统一的部署模型中。通过原生摄取 OpenTelemetry 协议 (OTLP)，系统消除了中间翻译步骤，提高了摄取性能。这种 OpenTelemetry 集成为更高级的追踪功能提供了必要的数据基础。

## 人类与 Agent 的协作

基于 Jaeger v2，该项目正在探索团队分析分布式系统的新方法。目标是促进工程师与 AI Agent 在调试过程中的协作。[CNCF LFX 指导计划](https://www.cncf.io/people/mentoring/)和 [Google 编程之夏 (GSoC)](https://summerofcode.withgoogle.com/) 的贡献者们正在积极推动这项工作。

为了支持 AI 集成，Jaeger 正在采用三种开放标准：[模型上下文协议 (MCP)](https://thenewstack.io/model-context-protocol-roadmap-2026/)、Agent 客户端协议 (ACP) 和 Agent-用户交互协议 (AG-UI)。MCP 标准化了 AI 模型如何安全地访问外部数据源。ACP 为用户界面与 AI Agent 及 sidecar 通信提供了一种统一的方法。结合在一起，它们使 Jaeger 能够作为一个交互式工作空间运行。

## 构建后端协议层

技术实现从后端开始。我们正在构建一个 Agent 客户端协议层，作为 Jaeger 前端与外部 AI sidecar 之间的无状态翻译器。设计和概念验证记录在 [Jaeger 后端议题 #8252（在 Jaeger AI 中实现 AG-UI 到 ACP）](https://github.com/jaegertracing/jaeger/issues/8252) 和 [议题 #8295（实现基于 ACP 的 AI 处理器）](https://github.com/jaegertracing/jaeger/issues/8295) 中。

![Jaeger v2 技术实现图解](https://cdn.thenewstack.io/media/2026/04/e1b018fa-1-1024x683.png)

(或

```
mermaid
graph LR
  J_UI["Jaeger UI"]
  AI_A["AI Agent"]
  subgraph JAEGER["Jaeger v2"]
    AGW["Agent Gateway"]
    JMCP["Jaeger MCP"]
  end

  J_UI -- "AG-UI Protocol" --> AGW
  AGW -- "ACP Protocol" --> AI_A
  AGW -- "MCP Protocol" <--> JMCP
```

)

传统上，故障响应者通过手动过滤服务和标签来构建查询。ACP 集成允许后端解析自然语言约束（例如，识别支付服务中延迟超过 2 秒的 500 级错误），并将其转换为确定性的追踪查询。

组织可以将此后端配置为使用云端[大语言模型](https://thenewstack.io/ml-and-llm-adoption-challenged-most-often-by-observability/) (LLM) 进行复杂推理，或使用本地小语言模型 (SLM) 以保证严格的数据隐私。分析的深度取决于所选模型，正如[托管与本地 AI 基础设施的行业分析](https://www.algolia.com/blog/engineering/hosted-vs-local-llm-ai-infrastructure)中所指出的。通过将 AI 限制在协议翻译和查询生成上，该架构最大限度地降低了与开放式聊天机器人相关的幻觉风险。

### 协作式 UI 工作空间

Jaeger 用户界面也在进行更新以支持这一后端逻辑。正如 [Jaeger UI 议题 #3313](https://github.com/jaegertracing/jaeger-ui/issues/3313) 所跟踪的那样，我们正在从旧的 Redux 迁移到现代的 Zustand + React Query。

前端引入了一个由 assistant-ui + AG-UI 驱动的应用内助手。UI 使用流式事件将追踪上下文（如错误日志和键值标签）发送到后端网关。这允许工程师提示助手总结特定 Span 内的失败路径，从而减少在事件发生期间手动检查原始日志行的需求。

### 可视化生成式 AI 执行路径

除了使用 AI 分析标准追踪外，该项目还在增加对追踪 AI 应用本身的支持。

[Jaeger 议题 #8401（GenAI 集成）](https://github.com/jaegertracing/jaeger/issues/8401)中概述了这项工作，重点是可视化快速演进的 OpenTelemetry GenAI 语义约定。OpenTelemetry 社区目前正在起草规范，以标准化这些高度动态工作流的遥测数据。关键计划包括用于跟踪任务、内存和动作的 [生成式 AI Agent 系统（议题 #2664）](https://github.com/open-telemetry/semantic-conventions/issues/2664) 衍生草案，以及用于监控临时代码执行环境的 [AI 沙箱（议题 #3583）](https://github.com/open-telemetry/semantic-conventions/issues/3583) 约定。

> “Jaeger 将在 UI 中映射这些新的标准操作，以提供对 AI 执行路径的清晰可见性，而不会将团队锁定在特定厂商的格式中。”

构建检索增强生成 (RAG) 流水线和自主 Agent 的开发人员需要测量嵌入模型延迟、跟踪外部工具调用并监控 Token 使用情况。Jaeger 将在 UI 中映射这些新的标准操作，以提供对 AI 执行路径的清晰可见性，而不会将团队锁定在特定厂商的格式中。

### 统一可观测性：从本地测试到生产

在测试和生产环境之间保持一致性是一个实际挑战。Jaeger 最初通过“全功能一体化 (all-in-one)”执行文件普及了本地测试。由于 Jaeger v2 构建在 OpenTelemetry Collector 之上，开发人员在本地运行的二进制文件与生产环境中的完全相同。

在测试期间，工程师可以使用本地 SLM 运行 Jaeger v2 容器。这创建了一个私人沙箱，用于测试生成式 AI 追踪或调试 ACP 集成，而不会将数据暴露给外部 API。

在生产环境中，平台团队部署相同的统一二进制文件，通常使用诸如针对 Kubernetes 的 [OpenTelemetry Operator](https://opentelemetry.io/docs/kubernetes/operator/) 之类的工具。然后，组织可以将本地 SLM 替换为更大规模的云端 LLM，以处理生产环境的事件分析。这确保了从开发到部署的追踪配置保持一致。

## 展望未来

追踪需求正在发生变化，以适应 AI 应用的复杂性。通过 Jaeger v2 建立坚实的 OpenTelemetry 基础并集成 MCP 和 ACP 标准，该项目正在调整其核心能力。这条技术路径实现了一种实用的工作流，让工程师和 AI Agent 能够协作诊断分布式系统故障。