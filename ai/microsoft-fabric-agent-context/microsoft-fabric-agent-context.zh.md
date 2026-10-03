**微软正在将 Fabric**（其集成数据平台）打造成企业智能体了解公司运作方式的阵地，无论是了解上个季度的财务状况，还是工厂车间当前正在发生的事情。

周二，在西班牙巴塞罗那举行的 FabCon 和 SQLCon 数据大会上，微软阐述了其愿景的下一步，即构成 Fabric 的产品如何简化所有这些信息收集过程。

例如，微软介绍了 Fabric 内部的上下文层 [**Fabric IQ**](https://learn.microsoft.com/en-us/fabric/iq/overview) 如何默认向 Microsoft 365 Copilot 提供数据。外部智能体可以通过 MCP 对其进行查询。Power BI 很快将能够把相同的定义转化为应用。而向其中添加业务规则的本体论（Ontologies）也进一步推进到了预览阶段。

![](https://cdn.thenewstack.io/media/2026/09/af4a4c3c-img_5653-1024x768.jpg)

*图片来源：The New Stack*

正如微软 [Fabric](https://www.microsoft.com/en-us/microsoft-fabric) 首席技术官 [Amir Netz](https://www.linkedin.com/in/amirnetz/) 在主题演讲后的新闻发布会上所说：“智能体是一种非常非常奇怪的生物，我总是喜欢说它就像电影《初恋50次》（*50 First Dates*）里的德鲁·巴里摩尔（Drew Barrymore）。每次它们睁开眼睛，就会忘记之前发生的一切。

“它们不知道自己身处何方，所以我们要做的第一件事就是告诉它们身在何处。你现在为微软工作。你现在为富国银行工作。你现在为阿联酋航空工作。”

> “智能体是一种非常非常奇怪的生物，我总是喜欢说它就像电影《初恋50次》（*50 First Dates*）里的德鲁·巴里摩尔（Drew Barrymore）。每次它们睁开眼睛，就会忘记之前发生的一切。”

客户往往是通过艰难的方式发现这一点的。负责 Fabric IQ 的公司副总裁 [Yitzhak Kesselman](https://www.linkedin.com/in/yitzhak-kesselman/) 告诉 *The New Stack*，企业统一了数据，在其上运行模型，然后查看结果。

“在这一旅程中处于更先进阶段的客户会为他们的智能体制定自己的评估标准，”他说道，并补充说他们所看到的结果有时并非他们所期望的。“然后[客户]会明白：‘好吧，现在我需要为我的智能体创建上下文了。’”

Kesselman 表示，他去年会见了 320 多家公司，这种压力的来源是业务部门，他们会要求“‘展示这些智能体的价值’，”他说，“‘看看使用前后的对比。’”

微软 [Azure Data](https://azure.microsoft.com/en-us/products/data-factory) 执行副总裁 [Arun Ulag](https://www.linkedin.com/in/arunulag/) 在主题演讲中表示，编码智能体之所以能够工作，是因为它们拥有“代码、代码库、更改历史记录、规范和测试”。但他辩称，在编码之外，大多数企业没有任何与之相提并论的东西。

Fabric IQ 是微软所谓的 Microsoft IQ 的四个组成部分之一（毕竟这是微软，其中总会涉及许多不同的名称和产品）。

Work IQ 涵盖电子邮件、Teams 和 SharePoint。Foundry IQ 涵盖文档和手册。Web IQ 涵盖公共互联网。

Ulag 表示，Fabric IQ “专注于你的业务状态以及你的业务实际是如何运行的。”他在其[公告博客文章](https://azure.microsoft.com/en-us/blog/fabcon-and-sqlcon-2026-in-barcelona-building-the-data-foundation-for-microsoft-copilot-and-agents/)中将其描述为结合了“来自 OneLake 的统一数据、来自 Power BI 语义模型的受信任指标，以及来自本体论和实时情报的运营上下文。”

## 导入数据

“每个人都想直接跃升至 AI，但随后他们意识到，‘哦，我需要为此准备数据，’”Kesselman 说道。“他们需要来自业务应用程序的数据、结构化数据。他们需要拥有实时数据。”

Fabric 的存储层 [OneLake](https://learn.microsoft.com/en-us/fabric/onelake/onelake-overview) 是这一切的核心，为了让系统提供上下文，企业必须将他们使用的所有第一方和第三方服务的数据输入其中。

Fabric 的快捷方式和镜像功能（将外部源连接或复制到 OneLake 中）是免费的，Netz 表示，OneLake 下管理的存储量正以每年 300% 的速度增长。

## 2026 年巴塞罗那 FabCon 和 SQLCon 本周新品

周二，[该公司宣布](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/fabcon-and-sqlcon-barcelona-2026-what%E2%80%99s-new-in-microsoft-onelake-and-its-rapidly/5369146)与 Salesforce Data Cloud 360 实现双向集成、Google BigQuery 镜像功能全面上市（GA）、直接针对 OneLake 运行该引擎的 ClickHouse 工作负载，以及预计在未来几周内在 Fabric 中推出的 dbt Fusion 引擎。

然而，单纯复制数据并不能满足安全团队的要求。在未来几周内进入公开预览阶段的镜像安全角色（Mirrored security roles）将权限与数据一同引入。例如，在 Snowflake 中定义的访问权限角色将以相同的成员和相同的表权限出现在 Fabric 中。

正如微软的 [Shireen Bahadur](https://linkedin.com/in/shireen-bahadur) 在主题演讲中演示该功能时所说：“我们不仅仅是在复制安全规则。我们实际上在积极执行并维护这些角色。”

> “我们不仅仅是在复制安全规则。我们实际上在积极执行并维护这些角色。”

OneLake 并不是单行道。企业还可以将数据提取出来并在其他工具中使用。

毕竟，OneLake 数据是以开放格式存储的并且具有开放 API，Netz 在台上表示任何能够读取它们的引擎都可以使用它。“如果你想用我们帮助人们免费获取的数据去使用我们竞争对手的工具，请便。我对此并不高兴，但请便吧，”他说。

现处于预览阶段的 IQ 共享（IQ sharing）允许一个组织在不进行复制且带有过期时间的情况下，与另一个租户共享受治理的表、文件、Markdown 智能体指令和 RDF 本体论。这是 Fabric 用户一直以来所期盼的，主题演讲中的这一宣布赢得了在场的数千名数据专业人士的阵阵掌声。

## 过去、现在与未来

“不仅是我们过去拥有的东西，不仅是现在正在发生的事情。我们还希望智能体能够理解我们希望未来发生什么，”Netz 在主题演讲中说道。

过去是语义模型。语义模型是每个 Power BI 报告之下的层，它定义了诸如收入之类的指标是如何计算的、实体如何关联以及哪些表提供了数字。Netz 表示，Power BI 用户已经创建了 2200 万个语义模型，Ulag 称它们为“Fabric IQ 的核心”。

现在是[实时情报](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/trusted-ai-starts-with-microsoft-fabric-real-time-intelligence-and-iq/5369528)（Real-time intelligence），即 Fabric 的流处理和事件堆栈，该堆栈也由 Kesselman 负责。他回忆起那天在巴黎有两位 CIO 对他说过同样的话。“‘没有实时情报就没有 AI；’没有实时情报就没有 AI，”他说。“如果你没有流式数据……没有新鲜的数据，你运行 LLM 时所依据的数据就会是几个小时或几天前的。”

> “‘没有实时情报就没有 AI；’没有实时情报就没有 AI。”

不过，单纯的一个信号是不够的：“你希望获取现在得到的信号……现在发生的事件，并从历史角度去看看，好吧，这是否是一个异常情况？”Kesselman 说道。这就是为什么主题演讲展示了批处理复制作业和事件流相互提供数据，以便智能体能够对照通常发生的情况来判断刚刚发生了什么。

未来是 [Fabric Planning](https://learn.microsoft.com/en-us/fabric/iq/plan/overview)，该功能于 7 月份正式全面上市，并在本周获得了性能和功能更新。这是微软用于预算、预测和目标的工具，关注的是企业想要实现的数字，而不是已经记录下来的数字。

计划是 Fabric 的一个项目，就像湖仓（lakehouse）或笔记本（notebook）一样，它从报告所使用的相同语义模型中借用其度量标准，因此收入在预测中与在仪表盘中的含义完全相同。在演示中，对输入的更改在包含约 1300 万个单元格的模型中层层传递。

让这些起作用的是[本体论](https://learn.microsoft.com/en-us/fabric/iq/ontology/overview)（Ontologies）：对业务处理的事物、它们如何关联以及处理规则的正式描述。Netz 在台上称它们为“语义模型加加”，在后来的新闻发布会上，他用一家航空公司来解释这个“加”。

“如果你是一家航空公司，你有飞机、你有飞行员、你有地勤人员、你有机场、你有行李，”他说。这些就是实体。

他表示，它们之间的关系“远不止是数据关系”。“不仅仅是说，‘哦，我在飞行员和飞机之间找到了外键和主键匹配’，它还可能是策略关系。根据资质，哪个飞行员可以驾驶哪架飞机，或者根据过去 24 小时的休息时间，该飞行员现在是否被允许驾驶这架飞机？”

但本体论不仅定义名词，它们还定义动词。“我可以将一架飞机停飞。我可以改道飞机。我可以为飞机指派登机口。”

创建这些本体论可能会非常耗时，因为它们必须将公司可能用于同一事物的各种术语映射到单个实体。但由于它们对该项目以及允许智能体对数据进行推理至关重要，微软构建了一个自动生成它们的工具。

## 付诸实践

截至周二，Microsoft 365 Copilot Chat 中的 Fabric IQ 以及 [Cowork](https://www.microsoft.com/en-us/microsoft-365/blog/2026/03/30/copilot-cowork-now-available-in-frontier/)（微软基于 Anthropic Claude Cowork 背后的技术构建的用于委派多步骤任务的模式）已全面上市。它能够从 Power BI 语义模型和报告中回答业务问题；它对 Fabric 和 Power BI 客户默认开启，微软表示它不消耗额外的 AI Token。

![](https://cdn.thenewstack.io/media/2026/09/7060ea0d-img_5661-1024x768.jpg)

*图片来源：The New Stack*

但商业用户不仅仅想与这些模型进行聊天。在这个氛围编程的时代，他们还希望生成使用所有这些数据的应用程序。

Power BI Desktop 在未来几周内将迎来预览版的[应用创建体验](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/power-bi%E2%80%99s-next-chapter-the-evolution-of-business-intelligence/5369131)。用户从语义模型开始，描述应用，然后让 Copilot 生成并将其发布到 Fabric 中。

正如 Ulag 所写，与报告不同，这些应用“可以接受输入、回写数据、保存共享状态并支持运营工作流。”

它们是构建在 [Rayfin](https://community.fabric.microsoft.com/blog/fbc_fabricupdatesblogs/introducing-rayfin-a-new-ai-first-way-to-build-deploy-and-govern-application-bac/5191676)（微软在 Build 大会上推出的开源 SDK）之上的 Fabric 应用。Power BI Pro 和每用户高级版（Premium Per User）客户可以免费获得它们，每个应用最高可享受 1GB 的 Fabric 数据库。

Netz 在发布会上确认这两者“没有核心区别”，Ulag 补充道：“创建出来的就是一个 Fabric app，对吧？就是这样。”

对于 Copilot 外部的智能体，[Fabric IQ MCP](https://learn.microsoft.com/en-us/fabric/iq/connectors/fabric-iq-mcp) 现已全面上市，包含六个只读工具，用于查找语义模型和报告、读取其架构（schemas）并对它们运行 DAX 查询。

本体论 MCP 工具目前处于预览阶段，公开了本体论定义和查询。目前同样处于预览阶段的 Fabric 数据智能体现在可以使用本体论作为其上下文源。并且该上下文通过同一层延伸到了 Microsoft Foundry、Copilot Studio 和 GitHub Copilot。

开发人员可以使用他们自己的工具来驱动新的数据工程智能体。

该智能体构建在[微软于 1 月份收购的 Osmos 技术](https://blogs.microsoft.com/blog/2026/01/05/microsoft-announces-acquisition-of-osmos-to-accelerate-autonomous-data-engineering-in-fabric/)之上，能够承担诸如迁移和 ETL 等长期运行的工作，并且可以从 GitHub Copilot、VS Code、Codex 和 Claude Code 中启动和引导。

Netz 在台上表示，前沿模型将编写这些代码，“并且它不会失败”，但你并不知道结果是否正确。

## 每个人现在都有了一个上下文层

今年，Databricks 推出了 [Genie Ontology](https://www.databricks.com/blog/whats-new-unity-catalog-data-ai-summit-2026)，Snowflake 推出了 [Horizon Context Layer](https://www.constellationr.com/insights/news/snowflake-summit-2026-context-custom-model-training-iceberg-v3)，Google 推出了 [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction)，Salesforce 推出了无头（headless）Data 360，并将其描述为上下文服务。Databricks 首席执行官 Ali Ghodsi 在 6 月份的自家会议上总结这一观点时指出，AI 面临的是上下文问题，而不是智能问题。

微软的版本在 Microsoft 365 Copilot 内部默认开启，并以 2200 万个语义模型为起点。微软本周还表示，它将为 Snowflake 发起的供应商中立语义元数据标准 [Apache Ossie](https://ossie.apache.org/) 做出贡献，并希望将 Power BI 的公式语言 DAX 识别为 Ossie 查询语言。

当微软在 6 月份的 Build 大会上[提出上下文论点时](https://thenewstack.io/microsoft-build-2026-data-fabric-horizondb-ai-agents/)，让智能体根据该上下文采取行动的各个部分大多还处于路线图阶段。现在，问答功能已经全面上市，而行动功能也已进入预览阶段。

当被问及当用户不再是运行仪表盘的单个人，而是一群智能体时，Fabric 如何应对，Kesselman 指出了可观测性。

“Fabric 真正让你可以拥有这种圣杯般的组合，既有系统数据、智能体如何运行的数据，也有业务数据，”他说，因此公司可以检查智能体是否做了它应该做的事情以及这给业务带来了什么影响。“在接下来的几个月里，这一领域还会有更多内容推出。”