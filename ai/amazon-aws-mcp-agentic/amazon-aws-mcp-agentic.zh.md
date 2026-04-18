在纽约举行的 MCP 峰会上，《The New Stack》采访了 [Clare Liguori](https://www.linkedin.com/in/clareliguori/)，她是 [AWS](https://aws.amazon.com/) 的高级首席软件工程师，也是开源 [Model Context Protocol 项目](https://modelcontextprotocol.io/community/triggers-events/charter#leadership)的核心维护者。我们讨论了这家超大规模云厂商对 MCP 的贡献、该技术的现状以及未来。

视频

自 [2024 年底发布](https://www.anthropic.com/news/model-context-protocol)以来，模型上下文协议（MCP）已成为连接 AI 智能体与工具、数据的通用方法。MCP 的发起者 Anthropic 在 [2025 年底将 MCP 的控制权移交给了 Linux 基金会](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/)。随着智能体 AI 在企业领域的影响力不断扩大，企业对 MCP 的兴趣已达到狂热程度。毕竟，如果你的 AI 应用无法获取所需的实时事实或工具，它又有什么用呢？

## 亚马逊对 MCP 项目的承诺

Liguori 既是 AWS 的成员又是 MCP 的核心维护者，这意味着她立足于企业和开源这两个世界。据这位开发者介绍，她作为 MCP 维护者的职责包括协助决定哪些内容应加入 MCP 规范（以及哪些不应加入）。她告诉《TNS》，具体而言，她目前正在研究如何将 Web Hooks、事件和通知更好地引入 MCP。

如果这听起来有点像 OpenClaw 的风格，你的直觉是正确的。Liguori 表示，虽然我们曾经习惯于让 AI 智能体处于非常短的“约束”之下，“但我们现在开始看到——特别是随着 OpenClaw 和其他一些正在出现的智能体运行时的出现——那些‘始终在线’、等待事件触发并开始行动的智能体。”

换句话说，MCP 还远未*完工*。

鉴于 AWS 提供托管 MCP 服务，让其顶尖人才加入模型上下文协议项目具有良好的协同效应。事实上，AWS 已为 MCP 做出了多项贡献，包括任务（Tasks）和启发（Elicitations）（分别针对较长的请求时间线和向人类提示者请求更多上下文）。

我们可以预见 AWS 与 MCP 之间会有更多协作。Liguori 表示，这家云服务提供商充当了“MCP 中一些新兴概念的实验场，这些概念仍处于草案规范阶段，我们仍在根据反馈进行调整和优化。但能在某个地方拥有一个让人们真正上手体验的官方实现是非常棒的。”

这就是企业赞助和通过代理参与开源项目（OSS）可以开花结果的地方；赞助资金不仅能让开源基金会维持运转，其平台也有助于推动甚至塑造技术的普及。

## 展望未来

MCP 在智能体技术栈中的作用是显而易见的。AI 智能体需要这种“结缔组织”来将上下文引入 AI 智能体及其底层模型的工作中。但是，那些技术不领先、甚至没有内部开发团队的公司该怎么办呢？

Liguori 指出，亚马逊最近向所有岗位的所有职级开放了其 Kiro AI 开发工具，因为公司原本预计只有工程师才需要使用该服务。事实并非如此。将人们对 AI 驱动开发工具日益增长的兴趣，与像入门门槛较低的 Amazon Quick 这样使用 MCP 的工具结合起来，你就能预见到，未来 AI 将突破技术领域的局限，为即使是最小的业务也带来真正的自动化。