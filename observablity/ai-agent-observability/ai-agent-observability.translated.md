# AI Agent 可观测性 - 不断演进的标准和最佳实践

## 2025: AI Agent 年

AI Agent 正在成为 2025 年人工智能领域的下一个重大飞跃。从自主工作流到智能决策，AI Agent 将为各行各业的众多应用提供动力。然而，随着这种演变，对 AI Agent 可观测性的关键需求也随之而来，尤其是在扩展这些 Agent 以满足企业需求时。如果没有适当的监控、追踪和日志记录机制，诊断问题、提高效率以及确保 AI Agent 驱动的应用程序的可靠性将充满挑战。

### 什么是 AI Agent

AI Agent 是一种应用程序，它结合使用 LLM 功能、连接外部世界的工具和高级推理来实现所需的最终目标或状态；或者，Agent 也可以被视为系统，其中 LLM 动态地指导自己的流程和工具使用，从而保持对完成任务方式的控制。

*图片来源*:
[Google AI Agent Whitepaper](https://www.kaggle.com/whitepaper-agents).

有关 AI Agent 的更多信息，请参阅：

[Google: What is an AI agent?](https://cloud.google.com/discover/what-are-ai-agents)
[IBM: What are AI agents?](https://www.ibm.com/think/topics/ai-agents)
[MicroSoft: AI agents — what they are, and how they’ll change the way we work](https://news.microsoft.com/source/features/ai/ai-agents-what-they-are-and-how-theyll-change-the-way-we-work/)
[AWS: What are AI Agents?](https://aws.amazon.com/what-is/ai-agents/)
[Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents)

### 可观测性及其他

通常，来自应用程序的遥测数据用于监控和排除故障。在 AI Agent 的情况下，鉴于其非确定性性质，遥测数据还用作反馈循环，通过将其用作评估工具的输入，从而不断学习并提高 Agent 的质量。

鉴于 GenAI 的可观测性和评估工具来自不同的供应商，因此围绕 Agent 应用程序生成的遥测数据的形状建立标准非常重要，以避免因供应商或框架特定格式而导致的锁定。

## AI Agent 可观测性的现状

随着 AI Agent 生态系统不断成熟，对标准化和强大的可观测性的需求变得越来越明显。虽然某些框架提供内置的检测，但其他框架则依赖于与可观测性工具的集成。这种分散的局面突显了
[GenAI observability project](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md)
和 OpenTelemetry 新兴的语义约定的重要性，这些约定旨在统一遥测数据的收集和报告方式。

### 了解 AI Agent 应用程序与 AI Agent 框架

区分 **AI Agent 应用程序** 和 **AI Agent 框架** 至关重要：

**AI Agent 应用程序** 是指自主执行特定任务的各个 AI 驱动的实体。**AI Agent 框架** 提供必要的 инфраструктуру 来开发、管理和部署 AI Agent，通常比从头开始构建 Agent 的方式更简化。 示例包括：[IBM Bee AI](https://github.com/i-am-bee),[IBM wxFlow](https://github.com/IBM/wxflows/),[CrewAI](https://www.crewai.com/),[AutoGen](https://microsoft.github.io/autogen/dev/),[Semantic Kernel](https://github.com/microsoft/semantic-kernel),[LangGraph](https://www.langchain.com/langgraph),[PydanticAI](https://ai.pydantic.dev/) 等。

![AI agent application vs AI agent framework](/blog/2025/ai-agent-observability/agent-agent-framework.png)

### 建立标准化的语义约定

今天，OpenTelemetry 中的
[GenAI observability project](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md)
正在积极致力于定义语义约定，以标准化 AI Agent 可观测性。这项工作主要由以下因素驱动：
**Agent application semantic convention (代理应用语义约定)** – 一个 AI 代理应用语义约定草案已经建立并最终确定，作为 [OpenTelemetry semantic conventions repository](https://github.com/open-telemetry/semantic-conventions/issues/1732) 讨论的一部分。最初的 AI 代理语义约定基于 [Google’s AI agent white paper](https://www.kaggle.com/whitepaper-agents)，为定义可观测性标准提供了一个基础框架。展望未来，我们将继续完善和加强这一初始约定，使其更加健壮和全面。

**Agent framework semantic convention (代理框架语义约定)** – 现在，重点已经转移到为所有 AI 代理框架定义一个通用的语义约定。这项工作正在 [this OpenTelemetry issue](https://github.com/open-telemetry/semantic-conventions/issues/1530) 中讨论，旨在为 IBM Bee Stack, IBM wxFlow, CrewAI, AutoGen, LangGraph 等框架建立一个标准化的方法。此外，不同的 AI 代理框架将能够定义他们自己的 Framework Vendor Specific Semantic Convention (框架供应商特定语义约定)，同时遵守通用标准。

通过建立这些约定，我们确保 AI 代理框架可以报告标准化的指标、追踪和日志，从而更容易集成可观测性解决方案，并比较不同框架的性能。

注意：实验性的约定已经存在于 OpenTelemetry 的模型中，位于 [GenAI semantic convention](/docs/specs/semconv/gen-ai/)。

### Instrumentation approaches (检测方法)

为了使一个系统具有可观测性，必须对其进行检测：也就是说，来自系统组件的代码必须 [emit traces, metrics, and logs](/docs/concepts/instrumentation/)。

不同的 AI 代理框架在实现可观测性方面有不同的方法，主要分为两种选择：

#### Option 1: Baked-in instrumentation (内置检测)

第一种选择是实现内置检测，使用 OpenTelemetry 语义约定来发送遥测数据。这意味着可观测性是一个原生功能，允许用户无缝地跟踪代理性能、任务执行和资源利用率。一些 AI 代理框架，如 CrewAI，遵循这种模式。

作为代理框架的开发者，以下是这种内置检测的一些优点和缺点：

- 优点
  - 您可以承担维护遥测检测的开销，使其保持最新。
  - 简化了不熟悉 OpenTelemetry 配置的用户的采用。
  - 在发布当天保持新功能的秘密，同时为它们提供检测。
- 缺点
  - 对于不需要可观测性功能的用户来说，会增加框架的臃肿。
  - 如果框架的 OpenTelemetry 依赖滞后于上游更新，则存在版本锁定的风险。
  - 对于喜欢自定义检测的高级用户来说，灵活性较差。
  - 您可能无法从熟悉当前语义约定的 OTel 贡献者那里获得反馈/审查。
  - 您的检测可能滞后于最佳实践/约定（不仅仅是 OTel 库依赖的版本）。
- 如果您考虑这种方法，以下是一些需要遵循的最佳实践：
  - 提供一个配置设置，让用户可以轻松地启用或禁用从您的框架的内置检测中收集遥测数据。
  - 提前规划用户想要使用的其他外部检测包，并避免冲突。
  - 如果您选择这条路，请考虑在 [OpenTelemetry registry](/ecosystem/registry/) 中列出您的代理框架。
- 作为代理应用程序的开发者，如果...，您可能希望选择一个具有内置检测的代理框架
  - 您的代理应用程序代码中对外部包的依赖性最小。
  - 无需手动设置即可实现开箱即用的可观测性。

#### Option 2: Instrumentation via OpenTelemetry (通过 OpenTelemetry 进行检测)

此选项是将 OpenTelemetry 检测库发布到某些 GitHub 存储库。这些检测库可以导入到代理中，并配置为按照 OpenTelemetry 语义约定发送遥测数据。

对于使用 OpenTelemetry 发布检测，有两种选择：

- Option 1: External instrumentation in your own repository/package, like [Traceloop OpenTelemetry Instrumentation](https://github.com/traceloop/openllmetry/tree/main/packages), [Langtrace OpenTelemetry Instrumentation](https://github.com/Scale3-Labs/langtrace-python-sdk/tree/main/src/langtrace_python_sdk/instrumentation) etc.
- Option 2: External instrumentation in OpenTelemetry owned repository, like [instrumentation-genai](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation-genai) etc.

这两种选择都很好，但长远目标是将代码托管在 OpenTelemetry 拥有的存储库中，就像 Traceloop 试图 [donate the instrumentation code](https://github.com/open-telemetry/community/issues/2571) 现在捐赠给 OpenTelemetry。

作为代理框架的开发者，以下是使用 OpenTelemetry 进行检测的一些优点和缺点：
## 优点

- 将可观测性与核心框架分离，减少臃肿。
- 利用 OpenTelemetry 社区驱动的维护来进行工具更新。
- 允许用户混合和匹配 contrib 库，以满足其特定需求（例如，云提供商、LLM 供应商）。
- 更有可能利用围绕语义约定和零代码工具的最佳实践

## 缺点

- 如果用户依赖不兼容或过时的 contrib 包（包括安装时和运行时），则存在碎片化的风险。
- 当 OpenTelemetry 审查队列中存在过多的 PR 时，开发速度会减慢。

## 这种方法的最佳实践：

- 确保与流行的 OpenTelemetry contrib 库（例如，LLM 供应商、向量数据库）兼容。
- 提供关于推荐的 contrib 包和配置示例的清晰文档。
- 避免重复发明轮子；与现有的 OpenTelemetry 标准保持一致。
- 作为代理应用程序的开发人员，如果满足以下条件，您可能希望选择具有内置工具的代理框架……
- 您需要对遥测源和目标进行细粒度控制。
- 您的用例需要将可观测性与小众或自定义工具集成。

**注意：** 无论采用何种方法，所有 AI 代理框架都必须采用 AI 代理框架语义约定，以确保可观测性数据中的互操作性和一致性。

## AI 代理可观测性的未来

展望未来，AI 代理可观测性将继续发展，具体包括：

- **更强大的语义约定**，以涵盖边缘情况和新兴的 AI 代理框架。
- **统一的 AI 代理框架语义约定**，以确保不同框架之间的互操作性，同时允许供应商特定的扩展。
- **不断改进 AI 代理语义约定**，以完善初始标准并应对 AI 代理发展过程中的新挑战。
- **改进的工具**，用于监控、调试和优化 AI 代理。
- **与 AI 模型可观测性更紧密的集成**，以提供对 AI 驱动应用程序的端到端可见性。

## OpenTelemetry 的 GenAI SIG 的作用

[OpenTelemetry 中的 GenAI 特别兴趣小组 (SIG)](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md) 正在积极定义 [GenAI 语义约定](/docs/specs/semconv/gen-ai/)，涵盖以下关键领域：

- LLM 或模型语义约定
- VectorDB 语义约定
- AI 代理语义约定（更广泛的 GenAI 语义约定中的一个关键组成部分）

除了约定之外，SIG 还扩大了其范围，以提供对 Python 和其他语言的代理和模型的工具覆盖。随着 AI 代理变得越来越复杂，可观测性将在确保其可靠性、效率和可信度方面发挥根本作用。建立 AI 代理可观测性的标准化方法需要协作，我们邀请更广泛的 AI 社区做出贡献。

我们期待与不同的 AI 代理框架社区合作，以建立最佳实践并共同完善这些标准。您的见解和贡献将有助于塑造 AI 可观测性的未来，从而培养一个更加透明和有效的 AI 生态系统。

不要错过这个帮助塑造 GenAI 可观测性行业标准的未来机会！请在 [CNCF Slack](https://slack.cncf.io) `#otel-genai-instrumentation-wg` 频道上加入我们，或参加 [GenAI SIG 会议](https://github.com/open-telemetry/community/blob/main/projects/gen-ai.md#meeting-times)。