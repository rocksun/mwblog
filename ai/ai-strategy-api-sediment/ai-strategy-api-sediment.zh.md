“API格局一团糟，很少有人理解它，”API行业资深人士兼[Naftiko](https://naftiko.io)创始人Kin Lane告诉《The New Stack》。

有时感觉我们就像[生活在一个XKCD漫画中](https://xkcd.com/927/)。

![一幅名为“标准如何增殖：(参见：空调充电器、字符编码、即时消息等)”的三格漫画](https://cdn.thenewstack.io/media/2026/02/0331e67d-standards.png)

*xkcd.com*

组织通常不会在新思想出现时将旧系统从一个规范迁移到另一个。相反，它们会随着时间的推移积累多层集成标准，每个时代都留下了过于昂贵或有风险而无法挖掘的系统。“我接到一家大型企业一位20年资深员工的电话，他说，‘我们仍然有[EDI](https://www.edibasics.com/edi-vs-api/)和[WSDLs](https://en.wikipedia.org/wiki/Web_Services_Description_Language)，很多[Swagger](https://swagger.io)和[OpenAPI](https://www.openapis.org)。我们正在尝试做更多[Async API](https://www.asyncapi.com/en)。[MCP](https://modelcontextprotocol.io/docs/getting-started/intro)正在兴起，我们正在关注[Agent Skills](https://agentskills.io/home)，但我们有一个全球性业务需要运行，它必须稳定。’”

正是看到了这种API沉淀的反复模式，促使Lane创立了Naftiko。
API规范的演变和分化

> “组织……随着时间的推移积累多层集成标准，每个时代都留下了过于昂贵或有风险而无法挖掘的系统。”

Lane认为，相互竞争的标准是供应商“跑马圈地”的结果，竞争性供应商利用规范来施加影响。我并不反对他的假设，但我想补充一点，不同的标准也反映了它们开发的时间。

Web服务描述语言 (WSDL) 出现在2000年代的企业SOA运动中，作为Web服务的正式契约语言。它由W3C管理，但受IBM、Microsoft和Oracle的严重影响，技术上是开放的，但反映了企业中间件的需求，使用冗长的XML模式定义操作、消息和绑定。

在2010年代，REST API取代了SOAP，更轻量级的规范出现了：

*   **Swagger**，最初由[Tony Tam](https://www.linkedin.com/in/tonytam/)为他的创业公司Wordnik创建，作为字典API，成为HTTP/REST API的主导标准。与SOAP和WSDL相比，它达到了更好的平衡——足够机器可读以便于工具使用，也足够人类可读以便于文档编写。它专注于同步请求-响应模式。在Tam的创业公司被[SmartBear](https://smartbear.com/)收购后，Swagger被移交给Linux基金会并更名为OpenAPI。
*   **API Blueprint**，由Apiary创建，倡导基于Markdown的可读性。它优雅、人性化，并获得了早期关注，但在2017年[Oracle收购Apiary](https://www.oracle.com/corporate/pressrelease/oracle-buys-apiary-011917.html#:~:text=Creates%20the%20Most%20Comprehensive%20API,lifecycle%20and%20deliver%20integrated%20applications.%E2%80%9D)后，随着Oracle将其整合到其API平台云服务中，开发转向了维护模式。由于缺乏基金会治理，竞争对手没有动力投资工具，社区也随之萎缩。
*   **RAML (RESTful API建模语言)**，由MuleSoft支持，强调模块化和重用，这对于拥有数百个API的大型企业至关重要。“我认为RAML比Swagger是一个更好的规范，”Lane告诉我，“但MuleSoft的人在社区中对其他人表现得非常糟糕，以至于没有人想使用它。”[Salesforce于2018年以65亿美元收购了MuleSoft](https://investor.salesforce.com/news/news-details/2018/Salesforce-Signs-Definitive-Agreement-to-Acquire-MuleSoft/default.aspx)，RAML成为MuleSoft Anypoint平台的一个功能，而不是共享基础设施。

随着事件驱动架构、消息队列、WebSockets和流媒体等异步架构模式在2010年代后期流行起来，OpenAPI的请求-响应模型不再适用。作为OpenAPI的姊妹规范，[AsyncAPI](https://www.asyncapi.com/en)（也属于Linux基金会）借鉴了OpenAPI的结构，并将其适配于发布/订阅、流媒体和异步消息模式。

进入2010年代，[Smithy](https://smithy.io) (AWS) 和TypeSpec (Microsoft) 标志着向协议无关的API建模的转变。它们不是直接描述HTTP端点，而是抽象地建模服务，然后生成OpenAPI、代码或特定协议的实现。这反映了云提供商需要保持类型安全，同时从单一定义支持多种协议（HTTP、gRPC、专有协议）。

Smithy为AWS的服务定义提供支持。TypeSpec源于Microsoft在Azure API方面的经验，并强调基于TypeScript的语法，以提高开发人员的广泛可访问性。Smithy和TypeSpec都是开源的，但两者都没有OpenAPI/AsyncAPI意义上的真正开放治理。AWS根据内部AWS需求推动Smithy的路线图。TypeSpec最近进入了Linux基金会的一个工作组，但Microsoft仍然是主要贡献者。没有开放治理——没有多供应商指导委员会，也没有要求竞争性云提供商达成共识。

这很重要，因为Smithy和TypeSpec反映了它们创建者的架构假设：多区域云服务、多语言微服务、自动生成的客户端。它们针对的是AWS和Azure遇到的问题，而不一定是企业或初创公司面临的问题。缺乏多样化的治理，它们就有可能成为解决供应商特定问题的复杂工具。

Smithy和TypeSpec的SDK重点揭示了另一点：这些规范假设开发人员通过生成的代码来消费API。它们并未针对LLM供应商希望构成下一波API消费者的自主代理进行优化。因此，大型LLM模型提供商正在创建并推动新的标准：

*   **MCP（模型上下文协议，Anthropic/开放社区）**定义了AI模型如何发现和调用工具/API。MCP不是描述API是什么，而是概述API*为代理做什么*——强调自然语言描述、参数语义和状态管理。它已获得快速早期采用，但也因[安全风险](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls)和[上下文窗口膨胀](https://thenewstack.io/how-to-reduce-mcp-token-bloat/)而受到批评。
*   **A2A（代理到代理）**最初由Google于2025年4月推出。这个开放协议专为多代理系统设计，允许来自不同提供商的AI代理或使用不同AI代理框架构建的代理之间进行互操作。
*   **Agent Skills (Anthropic)** 将能力与针对LLM理解优化的语义描述打包在一起——为AI理解而非人类阅读编写的文档。

虽然OpenAPI和AsyncAPI是战略资源，但MCP和A2A更具策略性。“MCP和A2A都非常具有事务性、令人兴奋，并且正值当下，”Lane说。“如果你不小心，它们也很可能泄露你所有的价值和数据。你必须非常谨慎地在新领域中进行交易。”

## 治理鸿沟：API治理与AI访问

问题是如何弥合单个团队的战术需求与整个企业的战略需求之间的鸿沟。“我在Postman经常看到这种情况。拖拉机公司John Deere会来找我们说，‘我们的首席信息官、首席技术官办公室和卓越中心，在整个组织中管理SOAP、WSDLs、open API和AsynchAPI。现在我们有团队使用Postman Collections运行测试和自动化，但他们不了解全局。我们需要Postman来为我们调和这两个世界。’”

API经济见证了开发人员设计API，将其视为产品，对其进行速率限制，并了解谁在使用它们以及他们用它们做什么。“然而，MCP想要规避所有这些，”Lane说。“它想要直接访问你的数据和文件，所以它正在抛弃我们文件系统和数据库前十年的设计工作，转而让代理直接访问，而没有多少审计或治理。”

除了浪费巨大的潜在价值，糟糕的数据治理在内部部署LLM时也带来了重大挑战。组织可能会无意中跨部门泄露敏感信息。这些数据之前可能在技术上是可访问的，但需要手动搜索Google Drive或文件共享才能找到。

当LLM获得这些信息存储库的访问权限时，它们可以更容易地发现和共享敏感数据，从而有效地普及了访问权限，这可能违反了预期的访问控制。这是[Nicolleta Curtis](https://www.linkedin.com/in/nicoletta-curtis-4ab48515?originalSubdomain=uk)在一次[对《LeadDev》的采访](https://leaddev.com/technical-direction/if-95-of-generative-ai-pilots-fail-whats-going-wrong)中向我强调的一点。“即使是OneDrive和SharePoint等基本服务，我们也发现了被过度共享或具有开放权限的文档，”她告诉我。

组织通常以两种方式之一应对这一挑战：他们要么低估数据暴露风险的严重性，要么低估了适当缓解措施将给其安全团队带来的操作负担。事后实施适当的访问控制和数据边界需要付出巨大努力。

在拥有遗留系统的大型企业中，追溯性地收紧权限通常会破坏现有的工作流和集成。这会在组织内部造成摩擦，因为团队突然失去对他们历来依赖的信息的访问权限，导致生产力受影响以及对新控制措施的内部抵制。

在[本系列的第一篇文章](https://thenewstack.io/map-your-api-landscape-to-prevent-agentic-ai-disaster/)中，Lane描述了他如何在Bloomberg建立API治理的经验，其中包括：

*   通过抓取GitHub和Confluence以获取API证据（WSDLs、XSDs、Swaggers、OpenAPI规范）来绘制现有格局
*   将所有内容标准化为OpenAPI 3.1以获得完整记录
*   识别不同业务线中的团队边界、领域和所有权

使用这种结合OpenAPI等既定标准的全面API映射和治理方法，为合规性、安全性以及个人身份信息 (PII) 管理提供了最佳基础。对于较新/较小的组织，Lane建议跳过“包袱”，直接采用Agent Skills或MCP等新方法。

无论您偏爱哪种方法，我们都同意您应该抵制采取技术优先方法而忽视业务成果的诱惑。