模型上下文协议（[MCP](https://modelcontextprotocol.io/)）已[成为](https://thenewstack.io/why-the-model-context-protocol-won/)代理式AI技术栈的关键构建模块之一，它作为模型连接外部工具、文件和业务系统的通用语言。

想要一个AI助手从Google Drive拉取文件、查询公司数据库、检查GitHub问题，或在内部应用程序中触发操作吗？这就是MCP旨在处理的任务。

现在，该项目[新的2026年路线图](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)表明维护者正在关注一个更棘手的问题：在MCP能够经受住真实生产环境的使用之前，需要修复什么？

## 走向共享协议之路

MCP于2024年末首次亮相，当时Anthropic[引入](https://www.anthropic.com/news/model-context-protocol)了该协议，旨在使AI模型能够以更结构化的方式与外部工具和数据源进行交互。

该项目的[开源资质](https://github.com/modelcontextprotocol)帮助它在构建AI助手和代理式应用程序的开发者中获得了关注。团队无需为每个系统编写自定义集成，而是可以[通过MCP服务器](https://thenewstack.io/15-best-practices-for-building-mcp-servers-in-production/)暴露这些服务，让模型使用相同的协议与它们进行交互。

过去一年里，AI公司和开发者平台组成的生态系统日益壮大，并开始增加对MCP的支持。Anthropic[自己的Claude助手](https://code.claude.com/docs/en/mcp)使用它与外部工具交互，而其他供应商——[包括OpenAI](https://community.openai.com/t/introducing-support-for-remote-mcp-servers-image-generation-code-interpreter-and-more-in-the-responses-api/1266973)、[Microsoft](https://developer.microsoft.com/en-us/windows/agentic/)、[Google](https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services)和[Amazon](https://devops.com/aws-adds-mcp-support-to-amazon-q-developer-platform/)——也已采纳该标准。

但随着应用的推广，在更严肃的环境中运行该协议的操作挑战也随之而来。为了解决这些成长烦恼，项目维护者审阅了一系列潜在改进，并确定了四个优先领域，大部分开发工作和快速推进的协议提案将集中于此。

## 让MCP更容易大规模运行

开发者们普遍关注的一个反复出现的问题是MCP如何处理客户端和服务器之间的连接。目前，该协议依赖于长寿命的“有状态”会话，这使得在多个实例或负载均衡器后面部署MCP服务器变得更加困难，因为会话状态通常存储在处理连接的服务器上，而不是在机器之间共享。

这个优先领域被标记为“传输演进和可扩展性”。简单来说，这意味着重新设计MCP处理这些连接的方式，以便部署能够更容易地在分布式基础设施中扩展。

开发者在尝试在多台机器上运行MCP服务器时已经遇到了这个限制。在[一份八月份提出的GitHub问题](https://github.com/modelcontextprotocol/typescript-sdk/issues/892)中，一位尝试使用Redis在多个Pod上构建无状态MCP服务器的开发者报告称，SDK没有提供将客户端会话ID映射到服务器内部事件流的可靠方法。如果没有这种映射，如果请求被路由到不同的服务器实例，会话就无法恢复——这实际上迫使部署依赖于内存状态而不是分布式基础设施。

MCP维护者[后来在一项关于启用无状态或准无状态服务器架构的更广泛跟踪讨论中引用了该问题](https://github.com/modelcontextprotocol/typescript-sdk/issues/1058)。

路线图建议通过两项主要改变来解决这些限制。首先，演进MCP的传输和会话模型，使服务器能够横向扩展而无需在单台机器上维护状态。其次，引入一种服务器可以暴露的标准元数据格式——可能通过*.well-known*端点——这样工具和注册表就可以在不首先建立实时连接的情况下发现MCP服务器的功能。

Anthropic的技术人员兼MCP首席维护者[David Soria Parra](https://www.linkedin.com/in/david-soria-parra-4a78b3a)表示，目标是改进现有传输的工作方式，而不是引入新的传输。

Parra写道：“我们想要明确一点：我们本周期不会增加更多官方传输方式，而是会演进现有传输方式。保持传输方式数量少是基于[MCP设计原则](https://modelcontextprotocol.io/community/design-principles)的审慎决定。”

## 没有任务太小

第二个优先事项涉及“代理通信”，它指的是MCP如何处理由AI代理触发的长时间运行的工作。

目前，该协议允许客户端启动异步任务（Tasks），使代理可以在一个请求中启动工作并在稍后检索结果。但早期的生产使用暴露了这些任务应如何行为的空白——特别是失败作业应如何重试以及已完成结果应保留多长时间。

其中一些问题在[任务（Tasks）功能本身](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1686)的开发过程中浮出水面。在定义任务如何操作的GitHub拉取请求中，AWS软件工程师兼MCP维护者[Luca Chang](https://www.linkedin.com/in/luca-chang/)将这种模式[描述为](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1732)允许代理在一个请求中启动工作并在稍后检索结果。

尽管这种方法使代理更容易运行长时间操作，但它也引发了关于当出现问题时这些作业如何重试以及其结果应保留多长时间的问题。

路线图提出了更清晰的生命周期规则定义，以便MCP系统能够更可靠地管理代理驱动的任务。

Parra还指出，其中一些空白只有在开发者开始在真实的生产环境中实际使用某个功能时才会显现。

他说：“这种迭代只有在某事物部署并在真实世界中测试后才能进行。我们计划对MCP的其他部分采取同样的方法：发布实验版本，收集生产反馈，然后迭代。”

## 减少MCP治理中的瓶颈

治理也坚定地提上了议程。随着MCP在公司和开发者社区中的应用范围扩大，维护者表示项目需要更清晰的决策结构和贡献者路径。

这个“治理成熟”的优先领域主要关注于完善协议变更的提议和审查方式。

最终目标是确保MCP能够持续发展，而无需依赖一小部分核心维护者在生态系统扩展时审查每一项变更。[目前](https://modelcontextprotocol.io/community/sep-guidelines)，每项MCP提案——称为SEP（规范增强提案）——无论涉及哪个领域，都必须由全体核心维护者审查。

Parra说：“那是一个瓶颈。它减缓了那些在其各自领域已经具备评估提案专业知识的工作组的进展。”

## 为企业级应用做准备

最后一个优先事项侧重于路线图所称的“企业级就绪”，对于许多开源基础设施项目来说，随着它们在行业内获得更广泛的应用，这是一个熟悉的阶段。

随着组织开始将MCP集成到内部系统中，它们往往会遇到一套可预测的操作要求——包括审计追踪、与企业身份系统绑定的身份验证、网关控制以及可以在不同环境之间干净迁移的配置。

与其他优先事项不同，这个领域有意地定义得不那么明确。路线图指出，企业级就绪仍然是当前工作计划中规定最少的部分之一，部分原因是维护者希望从亲身遇到这些问题的团队那里获得输入。

例如，目前MCP项目中没有专门的企业工作组。相反，维护者正在鼓励具有企业基础设施经验的贡献者帮助塑造这些工作。

Parra说：“我们希望那些正在经历这些挑战的人来帮助我们定义这项工作。”

## 展望未来

总的来说，这四个优先事项强调了一旦基础设施项目超越其萌芽阶段后，便会显现出来的问题。就MCP而言，这意味着使其协议更容易在多台机器上运行，澄清代理如何管理长时间运行的工作，建立更清晰的治理，并为企业做好准备。

然而，这份清单并非详尽无遗。路线图还强调了几个“展望未来”的领域，包括触发器和事件驱动的更新、新的结果类型以及围绕安全和授权的更深入工作。

尽管这些主题并非官方“优先事项”，但很可能在本周期内通过社区主导的工作组而非维护者直接关注来推进。

Parra写道：“我们专注于有限的项目集，但我们仍希望协议探索能以良好的速度继续进行。”

目前，重点是强化协议的核心——并邀请更广泛的开发者社区来帮助塑造未来。