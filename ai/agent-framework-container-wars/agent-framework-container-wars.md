<!--
title: 科技巨头为何免费送AI智能体框架？
cover: https://cdn.thenewstack.io/media/2026/02/4f46a825-tri-wiranto-o1bzted0cpo-unsplash-scaled.jpg
summary: 大厂免费提供AI智能体框架，实为变现底层服务。独立框架受冲击，未来价值在上下文工程、评估可观测性、安全和互操作协议。建议押注协议，而非框架。
-->

大厂免费提供AI智能体框架，实为变现底层服务。独立框架受冲击，未来价值在上下文工程、评估可观测性、安全和互操作协议。建议押注协议，而非框架。

> 译自：[The reason big tech is giving away AI agent frameworks](https://thenewstack.io/agent-framework-container-wars/)
> 
> 作者：Janakiram MSV

作为一名曾亲身经历容器编排大战的人，我正在目睹AI智能体框架上演同样的一幕。只不过这次的“演员”不同，赌注也高得多，但剧情几乎如出一辙。

2015年，如果你想编排容器，你有大量选择。[Docker Swarm](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/)、Apache Mesos、Hashicorp Nomad，当然还有早期形式的[Kubernetes](https://thenewstack.io/kubernetes/)。每个都有真正的技术优势。聪明人热情地为自己的选择争论不休。我记得坐在会议厅里，看着供应商们为他们的编排器为何是最佳选择提出令人信服的理由。

到2018年，Kubernetes已经吸收了整个生态系统。这并非因为它在所有维度上都技术领先，而是因为它拥有最深厚的超大规模云厂商支持，通过[CNCF](https://thenewstack.io/cto-chris-aniszczyk-on-the-cncf-push-for-ai-interoperability/)拥有最强的社区引力，并成为了容器世界中所有构建的默认基础。

如今，我看到开发者面临着同样令人眼花缭乱的智能体框架选择：LangGraph、CrewAI、[Google ADK](https://thenewstack.io/what-is-googles-agent-development-kit-an-architectural-tour/)、[AWS Strands](https://thenewstack.io/aws-launches-its-take-on-an-open-source-ai-agents-sdk/)、Microsoft Agent Framework、[OpenAI Agents SDK](https://thenewstack.io/introduction-to-the-openai-agents-sdk-and-responses-api/)、Mastra、Pydantic AI和Agno。我花时间研究了其中大部分，我可以告诉你每个都有真正有用的东西。

但真正重要的不是功能。而是你选择框架*之后*，谁来控制发生的一切。

## 免费框架，付费运行时

大多数框架比较文章都忽略了这一点。它们在一张表格中列出功能让你选择。这就像2015年通过列出哪些容器编排器支持健康检查来比较它们一样。它错过了背后正在进行的游戏。

超大规模云厂商并没有在框架功能上竞争。他们正在免费提供框架，将其作为通往其付费推理和部署运行时的入口。

> 超大规模云厂商没有在框架功能上竞争。他们正在免费提供框架，将其作为通往其付费推理和部署运行时的入口。

AWS 将 [Strands](https://strandsagents.com/latest/) 作为开源项目发布。它刻意设计得很精简。包含三个组件：模型、工具和提示。Strands 团队在解释原因时非常坦诚。他们[表示](https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/)，他们之前的框架库“开始阻碍我们充分利用更新的LLM的能力”。但关键在于，Strands 是与 [Amazon Bedrock AgentCore](https://aws.com/bedrock/agentcore/) 协同设计的。

Strands 与 Amazon [Bedrock AgentCore 紧密集成，用于生产部署，并已支持](https://thenewstack.io/aws-unveils-bedrock-agentcore-to-scale-ai-agents-from-prototype-to-production/) Amazon Q Developer、AWS Glue 和 VPC Reachability Analyzer 中的智能体功能。Strands SDK 本身是开源的，不收取许可费，而 Bedrock 和 Bedrock AgentCore 则是按量计费的 AWS 服务。

Google ADK 遵循相同的策略。它在 GitHub 上开源，原生支持多智能体，拥有真正令人印象深刻的上下文工程架构。Google 的工程团队[将](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/)上下文视为“对更丰富的有状态系统的编译视图”。这是严肃的系统工程。但 ADK 针对 Gemini 进行了优化，并附带了到 Vertex AI、BigQuery 和 AlloyDB 的原生连接器。框架是免费的。Vertex AI 则不是。

> “这是将 GKE、EKS、AKS 的策略应用到智能体上：免费提供编排器，从底层基础设施中获利。”

Microsoft Agent Framework 插入 [Microsoft Foundry](https://ai.azure.com/)，并通过 [Entra Agent ID](https://www.microsoft.com/en-in/security/business/identity-access/microsoft-entra-agent-id) 提供智能体身份管理。OpenAI 的 [Agents SDK](https://openai.github.io/openai-agents-python/) 甚至更精简。三个基本要素：Agents、Handoffs、Guardrails。其赌注很简单。如果框架足够易用，你就永远不会离开 OpenAI API。

这是将 GKE、EKS、AKS 的策略应用到智能体上：免费提供编排器，从底层基础设施中获利。

然后是独立厂商。[LangGraph](https://www.langchain.com/langgraph) 以超过80,000个GitHub星标和最大的生态系统领跑。 [CrewAI](https://www.crewai.com/) 因快速原型开发而受欢迎。[Mastra](https://mastra.ai/) 面向 TypeScript 开发者。[PydanticAI](https://ai.pydantic.dev/) 吸引了追求类型安全的 Python 开发者。这些都与模型无关、厂商中立，并且真正有用。

但它们都面临着我十年前目睹 Docker Swarm 和 Mesos 曾面临的同样生存问题。在一个超大规模云厂商正在从上方商品化的层级上，你是否能建立可持续的业务？

## 更智能的模型，更轻薄的框架

这就是智能体框架的故事与容器大战不同之处，而且这种不同对独立厂商并不有利。

在容器编排时代，底层技术（容器）在自我编排方面没有显著提升。你总是需要一个调度器。编排层是持久的。

而对于智能体框架，情况却恰恰相反。模型本身在编排方面越来越好。AWS 的 Strands 团队明确表示：“我们意识到不再需要如此复杂的编排来构建智能体，因为模型现在拥有原生的工具使用和推理能力。”以前需要数月才能投入生产的，现在通过模型驱动的方法只需数天。

当 [GPT-3.5 处于最先进水平时](https://thenewstack.io/donald-knuth-asked-chatgpt-20-questions-what-did-we-learn/)，LangGraph 基于图的编排是必不可少的。模型无法在没有明确控制流的情况下可靠地链接工具调用。如今，随着 Claude Sonnet 4.6、Gemini 3 Pro 和拥有1000万令牌上下文窗口的 Llama 4 Scout 的出现，模型能够独立处理规划、工具选择和自我纠正。随着每一代模型的更新，对繁重框架编排的需求都在减少。

这意味着独立框架正面临两面夹击。超大规模云厂商的运行时将部署和可观测性层商品化。更优质的模型则从底层将编排逻辑商品化。框架层正在变得越来越薄。

## 价值的真正所在

如果框架层变薄，那么真正的价值去向何处？根据我的经验，使用这些工具构建时，四个领域至关重要。

**上下文工程**正在成为生产级智能体的真正差异化因素。重要的不是你如何编排工具调用，而是你如何管理模型所“看到”的一切。Google ADK 的[分层上下文架构](https://developers.googleblog.com/architecting-efficient-context-aware-multi-agent-framework-for-production/)在这方面处于领先地位。Manus 团队[重建](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)了他们的智能体框架四次，才正确地实现了上下文管理。现在，真正的工程难题就在这里。

**评估和可观测性**是 LangChain 真正的护城河所在，不在于链抽象，而在于 [LangSmith](https://smith.langchain.com/)。[Langfuse](https://langfuse.com/)、[Braintrust](https://www.braintrust.dev/) 和 [Ragas](https://www.ragas.io/) 也在这个领域进行建设。AWS 在 1.0 版本中发布了 Strands Evals。无法衡量就无法改进智能体，而生产级智能体需要持续的评估管道。

**智能体安全**是无人预料到的新兴类别。Gravitee 最近的一份报告发现，88% 的组织经历了确认或疑似的智能体安全事件。只有14%的组织对其智能体群拥有完整的安全批准。微软[本周发布](https://www.microsoft.com/en-us/security/blog/2026/02/10/80-of-fortune-500-use-active-ai-agents-observability-governance-and-security-shape-the-new-frontier/)称，80% 的财富500强公司拥有活跃的 AI 智能体。然而，大多数组织仍然将智能体视为人类用户账户的延伸，而不是需要自身身份和访问控制的独立实体。这个安全层是与框架无关的，这意味着拥有它的人将获得跨框架的优势。

**互操作性协议**可能是最重要的转变。[MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) 正在成为工具集成的通用标准。[A2A](https://a2a-protocol.org/latest/) 处理智能体间的通信。Google 的 ADK 和 Amazon 的 Strands 都支持这两种协议。如果 MCP 和 A2A 发展成为行业标准，那么其上方的框架就会变成一个更薄的商品化层。这正是 [Kubernetes 标准化容器编排](https://thenewstack.io/the-impact-of-containerization-on-apm-strategies/)时所发生的情况，而各个发行版则在其之上竞争。

## 类比失效之处

现在，我必须诚实地指出我自己的类比的局限性。容器编排大战产生了一个明确的赢家，因为容器是一种同质的抽象。容器就是容器。工作负载根据定义是可移植的。

智能体则不然。一个编码智能体、一个客户服务智能体和一个数据分析智能体，它们在运行时要求、工具链、评估需求和上下文模式上存在根本性差异。这种异构性表明，基于智能体的市场框架可能不会整合为一个 Kubernetes 式的单一赢家。

> “智能体的Kubernetes”可能根本不是一个框架。它可能是协议层。

我认为实际情况会是一个碎片化但分层的堆栈。对于已致力于特定云的团队来说，超大规模云厂商的 SDK 将会胜出，因为框架与运行时的协同设计是真正的工程优势。LangGraph 将保持其作为需要图级控制和可审计性的复杂工作流解决方案的地位。像 Strands 和 OpenAI 这样轻量级的模型驱动 SDK，对于 LLM 自身处理编排的智能体来说效果很好。而协议，MCP 和 A2A，将成为底层的统一基础，就像 TCP/IP 统一了网络，而无需每个人都使用相同的操作系统一样。

“智能体的Kubernetes”可能根本不是一个框架。它可能是协议层。

## 选择协议，而非框架

如果今天我给一个平台工程团队提供建议（我确实在做），我会这样说。

首先，押注协议，而不是框架。从第一天起就围绕 MCP 设计你的工具集成。采用 A2A 进行智能体间的通信。这是你对冲框架更迭的对冲，而框架更迭一定会发生。

其次，独立于你的框架选择，投资于评估和可观测性。这一层会比任何框架都持久。选择适用于所有框架的工具，而不是将你锁定在某个框架内的工具。

第三，如果你已经深入某个超大规模云厂商，就使用他们的 SDK。Strands 与 Bedrock 或 ADK 与 Vertex 之间的协同设计是真正的工程优势。不要对抗这种引力。不值得为此付出代价。

容器大战告诉我们，生态系统而非功能，才能赢得基础设施之战。智能体框架的洗牌将告诉我们，当工作负载本身像运行它们的智能一样多样化时，这个教训是否仍然成立。