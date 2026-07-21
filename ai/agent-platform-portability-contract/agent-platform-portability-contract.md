<!--
title: 亚马逊、微软和谷歌在企业智能体架构上正趋于统一
cover: https://cdn.thenewstack.io/media/2026/07/58744e26-eva-wahyuni-kjdretrfc6o-unsplash-1024x853.png
summary: 亚马逊、微软和谷歌在企业智能体平台架构上趋于一致，均整合了运行时、内存、工具网关等组件。这种集成虽然提升了生产效率，但也加剧了云供应商锁定。作者呼吁借鉴Cloud Foundry的经验，建立行业中立的智能体部署标准，以实现真正的可移植性。
-->

亚马逊、微软和谷歌在企业智能体平台架构上趋于一致，均整合了运行时、内存、工具网关等组件。这种集成虽然提升了生产效率，但也加剧了云供应商锁定。作者呼吁借鉴Cloud Foundry的经验，建立行业中立的智能体部署标准，以实现真正的可移植性。

> 译自：[Amazon, Microsoft, and Google are converging on the same enterprise agent architecture](https://thenewstack.io/agent-platform-portability-contract/)
> 
> 作者：Janakiram MSV

**在过去的九个月里**，亚马逊、微软和谷歌各自推出了或重命名了其企业智能体平台。这三家公司都采用了相同的核心架构。运行时、内存、工具网关、身份验证、可观测性和治理功能现在均出现在 [Amazon Bedrock AgentCore](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available)、[Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) 以及 [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) 中，尽管名称略有不同。每家厂商都将这些组件作为生产级智能体的基础。在大约18个月前，这还是零散的库集合，如今正演变为一个独特的平台层。

要了解这一转变可能导向何方，可以参考平台即服务（PaaS）的演进。在2011年至2016年间，开发者使用虚拟机、负载均衡器、消息队列、密钥存储和监控代理来构建应用程序——每个组件都有自己的API和操作模型。[Cloud Foundry](https://thenewstack.io/open-source-platform-engineering-a-decade-of-cloud-foundry/) 和 Heroku 围绕一个应用契约统一了这些碎片。开发者无需过多考虑机器，而可以专注于应用程序。智能体生态系统正接近一个类似的转折点，但它仍然缺乏一个等效的契约——且目前还没有开源项目站出来定义它。

## 生产级智能体仍需的基础设施

想象一下，一个平台团队在本季度将一个客户支持智能体投入生产。他们选择了一个模型提供商，然后是一个框架，最后是一个存储会话状态和长期记忆的地方。他们添加了一个工具网关，以便智能体可以访问工单系统。接着是身份层，这样智能体就可以代表请求者行事，而沙箱则保证生成的代码安全无虞。评估和追踪通常被留到最后考虑，直到有人问起在客户发现问题之前，如何呈现质量回归。

每一个选择单独看起来都很小。但结合在一起时，它们决定了工作负载存活于哪个云平台。会话状态驻留在单个提供商的托管存储中。追踪记录在该提供商的遥测服务中，智能体的身份也源自其目录。一年后想要迁移该智能体，意味着必须重构整个组件，这正是PaaS为应用程序提供可移植形态之前，企业所处的困境。

## Cloud Foundry在失去市场前做对的事情

Cloud Foundry 将应用部署简化为一个单一命令，而平台负责之后的所有事情。[Buildpacks](https://buildpacks.io/) 可以检测语言并生成可运行的制品。服务代理负责配置数据库或消息代理，并将凭据绑定到应用程序环境中。路由、日志记录、自动伸缩和健康检查作为平台行为直接提供，而不是作为提交给运维团队的一串工单。

重要的是契约，而不是实现方式。应用程序声明其所需，且无需关心运行位置。Buildpacks 起源于 2011 年的 Heroku。Pivotal 和 Heroku 于 2018 年 1 月启动了 Cloud Native Buildpacks 项目，并于同年 10 月被 CNCF 接收。一个 PaaS 理念的寿命超过了孕育它的平台本身。

Cloud Foundry 从未成为主导平台。Kubernetes 成功了，Cloud Foundry 社区最终通过 [Korifi](https://www.cloudfoundry.org/technology/korifi/) 在 Kubernetes 之上重建了其抽象层。无论如何，其设计原则得以延续，而 2016 年运行该平台的企业所拥有的可移植性，是今天大多数智能体团队无法企及的。

## 三大云平台中相同的原语

让我剖析这三个平台，因为它们的相似之处被品牌名称掩盖了。

AgentCore 于 2025 年 10 月全面发布，包含七项可组合服务，即运行时、网关、内存、浏览器、代码解释器、身份验证和可观测性。运行时提供八小时的执行窗口，并具有完整的会话隔离。网关连接到现有的 MCP 服务器，将 API 和 Lambda 函数转换为智能体兼容的工具，而可观测性则通过 OpenTelemetry 导出到 CloudWatch。

微软自 2026 年 1 月 1 日起将 Azure AI Foundry 更名为 Microsoft Foundry。Foundry Agent Service 涵盖了相同的内容。微软记录了在会话隔离的托管运行时中运行的托管智能体，并使用 Entra Agent ID 处理身份验证。托管内存跨越会话、用户和程序范围，追踪功能则建立在 OpenTelemetry 之上。

谷歌在 2026 年的 Cloud Next 大会上停用了 Vertex AI 名称，并将该平台整合入 [Gemini Enterprise Agent Platform](https://cloud.stack.io/google-gemini-agent-platform/)。原先的 Agent Engine 变成了 Deployments，而 Memory Bank、Sessions、Agent Registry、Policies 和 Gateways 则位于其旁，构成了一个以智能体为先的信息架构。

这种趋同是理性的行为而非阴谋，因为基础设施公司建立垂直整合的平台，是因为利润存在于集成之中。其后果由客户而非供应商承担。身份验证、遥测和部署全部终止于单一提供商内部，这使得智能体下方的操作层变得难以迁移。最近，我曾在一篇关于谷歌 [Agent Substrate](https://thenewstack.io/kubernetes-ai-agent-runtime/) 的文章中分析过这个问题的运行时方面。

## 智能体平台将继承的契约

任何智能体平台都可以用一个问题来测试：如果 Cloud Foundry 风格的契约是为智能体而不是 Web 应用程序编写的，它会是什么样子？映射关系既具有指导意义，又足够引人入胜。

| PaaS 抽象 | 智能体平台等价物 | 目前可移植性断裂之处 |
| --- | --- | --- |
| 应用程序源码 | 智能体代码、指令和评估套件 | 每个框架定义了自己的打包形状 |
| Buildpack | 框架检测和智能体打包 | SDK 之间缺乏共享的构建契约 |
| 后端服务 | 模型、内存、检索或工具提供商 | 提供商被硬编码进智能体逻辑 |
| 服务绑定 | 工具和数据的认证附件 | 凭据由宿主云发放 |
| 路由器 | 智能体端点、MCP 或 A2A 接口 | 协议存在但缺乏生命周期管理 |
| 日志和指标 | 追踪、工具调用、成本和质量评分 | 生成式 AI 规范仍处于开发中 |
| 发布推广 | 评估、版本控制和渐进式部署 | 评估耦合于单个供应商的工具 |
| 平台策略 | 智能体身份、权限和审批 | 身份绑定于提供商的目录 |

真实的部署会混合这些行，而不是干净地采用它们，且没有团队需要从第一天就拥有全套功能。

### 将智能体打包为一个可部署单元

开发者交付的东西必须是可版本化、可测试且可作为单个制品移动的。代码、指令、工具依赖、内存契约、权限和评估套件必须共同流动，否则就毫无意义。AWS 通过其 [harness](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-is-now-generally-available-go-from-idea-to-production-grade-agent-in-minutes/) 导出路径接近了这一目标。一条命令即可将配置好的 harness 转换为 Strands 代码，AWS 表示该导出保留了模型、提示词、工具、内存布线和容器环境。客户无需重写架构即可轻松从配置转向代码，这是指向单一云平台的正确直觉。

### 绑定能力而非嵌入提供商

[Twelve-Factor App](https://12factor.net/) 教导开发者将数据库和缓存视为通过配置访问的附属资源。模型、内存存储、检索引擎、浏览器和工具网关也应受到同等待遇。一个在应用程序逻辑内部指定模型提供商的智能体，无论平台宣传册如何声称，都已经放弃了可移植性。

### 使运维成为抽象的一部分

PaaS 不仅实现了部署，更通过提供路由、日志记录、自动伸缩和回滚等内置功能证明了其价值。对智能体而言，核心问题大不相同，这正是企业必须询问的问题。平台团队想知道智能体是否完成了任务，以及是否选择了正确的工具。他们还想知道智能体是否超出了其权限，运行成本是多少，以及模型更新后质量是否出现回归。

## 智能体与应用程序的区别

智能体不是带有模型的 Web 应用程序，建立在该假设基础上的平台在生产中会失败。三个差异在此占据了主导地位：智能体的行为是概率性的，因此两个相同的输入可能会产生不同的工具调用；智能体以委派的用户权限行事，这会将权限错误转化为现实世界的副作用，而非仅仅显示错误页面；智能体的依赖项无需部署任何代码即可改变其行为——模型更新或修订后的工具描述会改变智能体的决策。

“Twelve-Factor”原则中进程应是无状态的规则在此并不适用。智能体平台需要临时的执行工作者，以及持久、可检查且可移植的智能体状态。[LangGraph](https://docs.langchain.com/oss/python/langgraph/durable-execution) 已经在开源领域展示了这种组合，包括每一步的检查点、一等公民的人工干预，以及崩溃后的恢复执行。其控制平面是商业化的 LangSmith 产品的一部分，涵盖了部署、评估和可观测性。碎片化出现在单个项目内部。

## 开放协议遗漏了什么

中立平台所需的大多数原语已经存在。[Model Context Protocol](https://modelcontextprotocol.io/) 标准化了智能体访问工具和数据的方式。[A2A](https://a2a-protocol.org/) 涵盖了独立智能体之间的发现和通信。[OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai/) 正在定义智能体跨度、工具调用和 token 使用的生成式 AI 规范，尽管大多数属性仍标记为开发中。OCI 镜像仍然是托管运行时无法承载的任何内容的打包逃生舱。

供应商已经承认中立层的重要性。Linux 基金会于 2025 年 12 月[宣布](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)成立 Agentic AI Foundation。其创始项目包括 Anthropic 的 MCP、Block 的 goose 和 OpenAI 的 AGENTS.md，AWS、谷歌和微软均作为白金会员加入。谷歌还将 A2A 移交给了 Linux 基金会。

协议并不等同于生命周期平台。一个管理智能体如何与工具对话的基金会，并不能说明如何管理智能体的版本，也不能说明如何通过环境推进该智能体，或在评估回归时将其回滚。企业在审查智能体平台时，可以处理三个简单问题。首先是治理：项目是由中立基金会控制，还是由销售托管版本的供应商控制。其次是打包，即相同的智能体制品应该在两个不同的云上运行而无需重写。第三是状态，即内存必须存在于企业可以导出的地方。目前还没有开源项目能同时回答这三个问题。

## 这将走向何方？

Kubernetes 定义了 Pod、部署和服务，这些抽象影响了整个行业对运行软件的看法。等效的智能体抽象尚未固定。无论最终谁拥有智能体控制平面，都不会仅仅拥有部署权。该所有者将定义什么是智能体、它包含哪些组件，以及平台团队被允许替换什么。

总而言之，超大规模云厂商正在构建有效的平台，切实解决了运维问题。但它们也在单个云内部解决了这些问题。如果一个中立项目能够在 Linux 基金会现有的协议之上组装相同的生命周期，企业将重新获得 Buildpacks 和服务代理曾经赋予它们的谈判地位。一个开放的、云中立的智能体平台将使供应商和买家同样受益，因为正是稳定的契约使得云原生生态系统能够超越任何单一提供商而成长。