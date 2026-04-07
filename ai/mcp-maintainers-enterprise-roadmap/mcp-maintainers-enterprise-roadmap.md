<!--
title: MCP维护者在开发者峰会公布企业安全路线图
cover: https://cdn.thenewstack.io/media/2026/04/60e429de-adam-szabo-0mfhutwlyo8-unsplash-scaled.jpg
summary: MCP维护者在AAIF保障下致力于企业安全、可靠性与治理。MCP是连接AI智能体的快速增长标准，未来将聚焦实用性和最佳实践，与A2A协议互补，而非竞争。
-->

MCP维护者在AAIF保障下致力于企业安全、可靠性与治理。MCP是连接AI智能体的快速增长标准，未来将聚焦实用性和最佳实践，与A2A协议互补，而非竞争。

> 译自：[MCP maintainers from Anthropic, AWS, Microsoft, and OpenAI lay out enterprise security roadmap at Dev Summit](https://thenewstack.io/mcp-maintainers-enterprise-roadmap/)
> 
> 作者：Eric Newcomer

在上周纽约举行的[MCP开发者峰会](https://events.linuxfoundation.org/mcp-dev-summit-north-america/)圆桌会议上，来自Anthropic、AWS、Microsoft和OpenAI的Model Context Protocol (MCP) [维护者](https://www.linuxfoundation.org/blog/open-source-maintainers-what-they-need-and-how-to-support-them)向我们保证，MCP规范在[智能体AI基金会](https://aaif.io/) (AAIF)手中是安全的，并将解决企业对安全性、可靠性和治理的关键需求。

AAIF从12月开始接受MCP、[goose](https://github.com/block/goose)和[AGENTS.md](http://agents.md)的贡献，并迅速发展到170名成员。MCP是最受欢迎的项目，已成为连接AI智能体与数据和应用程序的行业标准。

小组向MCP用户保证，项目自身治理方式变化不大（它仍然是一个自下而上的开源项目）。AAIF为企业用户及其需求提供了一个连接点，这些需求会反馈到协议开发中，以解决在生产环境中使用MCP的顾虑。

“我们看到客户对基金会以及将其作为一个中立平台来开发MCP及相关项目感到兴奋，”AWS高级首席工程师、维护者Claire Liguori表示。“很高兴能与社区在一起，并在整个开发者生态系统中工作，而不仅仅是在我们自己的公司内部。”

他们表示，MCP的广泛采用已发现显著的改进领域，特别是对于需要严格安全性、可扩展性、可靠性和治理的企业应用。

> “MCP是种子。基金会的职责范围远不止MCP……它对新的协议和技术开放，就像早期的云原生计算基金会（CNCF）一样。但MCP本身应该保持狭窄：连接AI到数据源。” — Nick Cooper，OpenAI

“MCP是种子，”OpenAI技术人员、维护者Nick Cooper说。“基金会的职责范围远不止MCP，”他继续说道。“它对新的协议和技术开放，就像早期的[云原生计算基金会](https://www.cncf.io/) (CNCF)一样。但MCP本身应该保持狭窄：连接AI到数据源。身份、可观测性和治理应该作为其他项目引入。”

Cooper补充说，AAIF目前正在征集与智能体AI相关的[新项目提案](https://github.com/aaif/project-proposals)，但我们需要谨慎，确保首批接受的项目设定正确的方向。

“我们在安全和授权方面看到了开放的挑战，我们很高兴AAIF能将行业聚集在一起，讨论正确的解决方案，”Anthropic技术人员、MCP共同创建者、维护者David Soria Para说。

Para补充说，授权是过去一年中MCP规范变化最活跃的部分之一。维护者们正在与Okta及其他方合作改进身份验证。

但Para表示，没有单一协议能解决所有安全挑战——生态系统（网关、注册中心、沙盒、拦截器）必须与协议一同发展。

[RedMonk](https://redmonk.com/)的会议主持人Sephen O’Grady表示，MCP是RedMonk追踪过增长最快的标准。例如，他说Docker花了大约13个月才达到MCP在大约13周内达到的普及程度。

智能体AI领域的另一个提议标准是[智能体间 (A2A) 协议](https://a2a-protocol.org/latest/)，它使得AI智能体能够相互连接。

小组指出，MCP和A2A是相互学习的大型协议，并非直接竞争。未来的融合是可能的但并非确定——“目前方法略有不同，”Para说。“但我们对任何能通过开放标准使行业更容易协作的方式都持开放态度。”

O’Grady提到了一个广受争议的社交媒体帖子，声称“MCP已死”，因为现在有一个具有类似功能的命令行界面（CLI）。

“我们提供API、SDK和CLI，所有这些都是为了与Azure互动，从而提供Microsoft的具体体验，因为我们希望在开发者所在的地方与他们会面，并在他们正在工作的场景中与他们会面，”Microsoft合作软件工程师、维护者Catie McCaffrey说。“对于本地开发场景，让智能体只与Azure CLI或GitHub CLI互动是一个非常棒的用例。”

> “对于本地开发场景，让智能体只与Azure CLI或GitHub CLI互动是一个非常棒的用例……MCP未来的重点必须放在其连接事物的实用性上。只要MCP保留其重要实用性，它就可以发展。”

小组表示，MCP和CLI这两种与智能体互动的方式对于不同的用例都很重要，并提供不同的开发者体验。

“MCP未来的重点必须放在其连接事物的实用性上。只要MCP保留其重要实用性，它就可以发展，”Cooper说。“对我来说，其价值在于使用MCP连接这些不同系统具有真正的实用性。MCP应该增长、发展并专注于此。这就是为什么中立行事并专注于MCP所提供的实用性很重要。”

小组同意MCP客户端需要关注，并且MCP的最佳实践需要更好的文档和沟通。例如，不要仅仅封装500个API端点。那是头号反模式。相反，应将MCP接口设计为智能体的新一类消费者（而不仅仅是另一个开发者）。精心设计的服务器和简单的API封装器之间存在巨大的质量差异。