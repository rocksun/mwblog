在今天于纽约举行的峰会上，[AWS](https://aws.amazon.com/?utm_content=inline+mention) 宣布了一系列以人工智能为中心的服务更新，但最重要的消息无疑是 Amazon Bedrock AgentCore，这是一个新的平台（目前处于预览阶段），它汇集了开发者将 AI Agent 投入生产并大规模应用所需的所有服务，并且可以使用任何框架和模型。

在某种程度上，Bedrock AgentCore 是 [Bedrock Agents](https://aws.amazon.com/bedrock/agents/) 的演变。但是，Bedrock Agents 旨在让任何人都能快速构建 Agent，而 AgentCore 则是一个更全面的解决方案，它源于人们意识到将 Agent 投入生产仍然过于困难。AWS 认为，如今，许多客户仍在构建自己的工具，或者使用现有工具，但尚不清楚这些工具的可扩展性如何。AgentCore 背后的核心思想是为企业提供他们在 AWS 上习以为常的那种可扩展性、可靠性和安全性，但用于构建具有非常具体的需求和挑战的 Agentic 系统。

AgentCore 结合了一个用于安全地部署和扩展 Agent 的运行时、一个用于存储和检索 Agent 记忆的记忆系统，以及一个构建在 OAuth 之上的身份服务，允许 AI Agent 通过预先授权访问 AWS 服务和第三方工具。

运行时的一个有趣功能是，单个 Agent 可以运行长达八个小时，并且所有运行时都经过检查点处理，这意味着应该可以很容易地从任何中断或故障中恢复。

[![](https://cdn.thenewstack.io/media/2025/07/60b816ef-aws_ai_stack_6_2025.png)](https://cdn.thenewstack.io/media/2025/07/60b816ef-aws_ai_stack_6_2025.png)

在今天的 Bedrock AgentCore 发布之后，AWS AI 堆栈。图片来源：AWS。

开发者可以使用记忆功能来为他们的 Agent 提供短期和长期记忆 —— 并且该记忆可以在 Agent 之间共享，也可以用于同一 Agent 的不同 Agent 会话（但可能是另一个底层模型）。

整个系统与模型、框架和协议无关。开发者可以使用在 Amazon Bedrock 或其本地笔记本电脑上运行的模型。想要使用自己的模型的企业也可以这样做，AWS 强调这些模型是隔离运行的，并受到 [AWS 的 Nitro 虚拟化系统](https://aws.amazon.com/ec2/nitro/) 的保护。

Bedrock AgentCore 还包括 AgentCore Gateway，用于将任何资源转换为与模型上下文协议 (MCP) 兼容的工具（例如 API、AWS Lambda 函数等），以及一个代码解释器，允许 Agent 安全地编写和执行 JavaScript、TypeScript 和 Python 代码。

正如 AWS 指出的那样，编写和执行代码的能力不仅对编码 Agent 有用。此代码解释器允许 Agent 在此沙盒环境中执行任何类型的代码，Agent 也可以从中访问文件和互联网，以引入额外的库或数据。

对于那些需要能够使用 Web 浏览器的应用程序，可以使用 AgentCore Browser Tool，这是一个基于云的浏览器运行时，允许 Agent 从隔离的虚拟机 (VM) 中与网站进行交互。正如 AWS 在今天发布前的简报中强调的那样，Browser Tool 也与模型无关（与大多数浏览器使用 Agent 不同）。

如今，Agent 的可观测性是一个越来越受关注的领域，因此 AgentCore 也包含一个可观测性工具也就不足为奇了，该工具旨在为开发者提供 Agent 行为、其推理、工具使用情况等的端到端视图。借助这些数据，开发者可以诊断性能问题、故障并审计 Agent 的输出。所有这些数据都以 [OpenTelemetry](https://thenewstack.io/the-modern-observability-roundtable-ai-rising-costs-and-opentelemetry/) 格式发出。

视频