微软在周二的 [Build 2026](https://news.microsoft.com/build-2026/) 开发者大会上指出，企业级人工智能（AI）最难的部分已不再是模型，而是数据上下文（data context）。该公司正寄希望于 [Microsoft Fabric](https://thenewstack.io/microsoft-fabric-goes-all-in-on-real-time-data-intelligence/) 来解决这一难题。

此次发布涵盖三个领域：全新的数据库平台、GPU加速的[数据仓库](https://thenewstack.io/data-warehouses-are-terrible-application-backends/)，以及已正式发布的语义和本体层（semantic and ontology layer）—— 每一项都旨在解决同一个底层问题：即智能体（Agent）每次启动都要从零开始，对组织的运作方式缺乏统一、共享的理解。

[Amir Netz](https://www.linkedin.com/in/amirnetz/)，Microsoft Fabric 的首席技术官（CTO），向 *The New Stack* 表示：“我们在日常生活中使用的 AI 与在企业中使用的 AI 之间存在着本质的区别。”

“区别在于，你希望 AI 能够像公司的员工一样 —— 作为一个了解机器如何运转、目标是什么的内部人员，而不是一个置身事外的陌生人。”

Netz 作为在微软工作了 30 年的老将，曾将大部分时间投入到 [Power BI](https://thenewstack.io/power-bi-gets-low-code-datamart-feature/) 和 Fabric 上。他将整个平台定位在所谓的“上下文层”（context layer）—— 这是智能体在企业内部进行可靠推理和采取适当行动所需的组织记忆。

## 适用于 AI 级工作负载的新数据库

最重大的基础设施发布是 [Azure HorizonDB](https://azure.microsoft.com/en-us/products/horizondb)，这是一款现已进入公共预览版的完全托管、与 [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) 兼容的数据库。微软长期以来一直是 PostgreSQL 的贡献者，但 HorizonDB 代表了完全不同量级的规模：弹性存储高达 128 TB，计算规模可达 3,072 个 vCore，并且在应对高需求事务性工作负载时，可实现亚毫秒级的多分区提交延迟。

该数据库还附带了专为 AI 应用构建的功能 —— [向量搜索](https://thenewstack.io/vector-search-is-reaching-its-limit-heres-what-comes-next/)、集成式 AI 模型管理，以及与 [Microsoft Foundry](https://azure.microsoft.com/en-us/products/ai-foundry) 和 Fabric 的直接连接。其核心理念是，开发人员在构建基于智能体的应用时，无需将事务数据、搜索和 AI 系统等多个独立的系统硬凑在一起。

纳斯达克（NASDAQ）软件工程总监 [Mohsin Shafqat](https://www.linkedin.com/in/mohsin-s-0453a17b/) 在一份声明中表示：“HorizonDB 的亮眼之处在于它与我们对该问题的思考方式高度契合。它无需拼凑多个组件，而是将事务数据、向量搜索和 AI 功能带入到单一平台中，这在不强制重新设计架构的前提下简化了整体架构。”

## GPU 加速引入数据仓库

微软还正在将 GPU 加速引入 Fabric 数据仓库（Fabric Data Warehouse），该功能将于 2026 年 7 月进入早期访问预览版。公司表示已将 NVIDIA 加速计算直接整合到数据仓库层，无需重写查询。在 2026 年 5 月进行的内部基准测试中，微软声称在 64 用户并发的情况下，其性能比三个未公开名称的云数据仓库竞争对手快出多达 7 倍。

其底层研究荣获了 [ACM SIGMOD 2026](https://www.linkedin.com/company/acm-sigmod-2026/posts/?feedView=all) 的最佳工业论文奖（Best Industry Paper）。

Netz 对这一性能数据进行了背景解读：“在数据仓库领域，如果一年能获得 10% 的提升，你就该开香槟庆祝了。而通过 GPU 加速，我们看到了 5 倍到 100 倍的飞跃。”

处于预览阶段的客户已经报告了切实的收益。UNC Health 表示其查询速度提升了高达 5 倍，这使团队能够减少在性能管理上花费的时间，而将更多精力放在产生业务洞察上。

NVIDIA 超大规模与高性能计算（HPC）副总裁 [Ian Buck](https://www.linkedin.com/in/ian-buck-19201315/) 指出，在企业数据上进行推理的 AI 智能体需要支持大量并发用户的低延迟性能，而这正是 GPU 加速非常契合的工作负载特征。

## Fabric IQ 迎来 GA（正式发布），贯穿整个智能体生态系统

微软专为企业智能体打造的语义与本体层 [Fabric IQ](https://www.microsoft.com/en-us/microsoft-fabric/features/iq) 现已正式发布。它构建在 Power BI 的语义模型之上（Netz 指出目前约有 50 万家组织在使用该模型），并为其扩展了操作上下文：业务实体、关系、规则、来自 Fabric 实时智能（Fabric Real-Time Intelligence）的实时信号，以及允许智能体采取的行动。

能够持续监控实时数据并根据预定义业务逻辑采取行动的操作智能体（Operations agents）现在也已正式发布。Fabric IQ 内的本体预计将在未来几个月内达到一般可用性（GA）。

微软正将 Fabric IQ 广泛整合到其智能体生态系统中。它现在可以作为 Microsoft Foundry 中的知识源进行访问，作为第一方 MCP 工具与 Microsoft Agent 365 集成，并扩展到了 Microsoft 365 Copilot（包括 Cowork 和 Copilot Chat）中，从而使智能体能够立足于受控的 Power BI 报告和语义模型中。Fabric 智能体技能（Agent Skills for Fabric）还将同样的语义上下文带入到 GitHub Copilot CLI 中，让开发人员能够直接在终端中查询报告和语义模型。

另外两项功能也即将迎来正式发布：用于构建业务实体和系统之间关系模型的 Fabric 图谱（graph in Fabric），以及将于本月晚些时候推出的 Fabric 规划（planning in Fabric）。规划功能尤其值得关注，因为其输出可以写回到 Fabric 中，从而让智能体拥有涵盖 OneLake 历史数据、实时信号以及前瞻性预测的闭环业务视图。

Netz 用时间跨度来描述这种结合效果：“我们拥有了过去，也拥有了现在。唯一缺失的是未来 —— 即应该发生什么。现在，本体终于能够真正涵盖所有的时态了。”

## 平台的故事

微软在 Build 2026 上更广泛的卖点在于，Fabric 既可以作为企业级 AI 的数据基础，又可以作为其部署目标 —— 这是一个能够处理操作型和分析型工作负载的统一平台。Netz 将其与 [Snowflake](https://thenewstack.io/snowflake-streamlines-data-analysis-for-enterprise-ai/) 和 [Databricks](https://thenewstack.io/databricks-brings-data-pipeline-service-to-ga/) 进行了对比，他认为后两者主要偏向分析。

微软的论点是，构建和运行应用程序的智能体需要一个能同时处理这两者的单一平台，并在其上叠加共享的上下文。

Fabric 中全新的数据库中心（Database Hub）目前处于私有预览阶段，它将支持对微软数据库产品组合（HorizonDB、Azure Database for PostgreSQL、Azure Cosmos DB）进行集中管理，并将数据镜像到 OneLake。Azure Cosmos DB 也在 Build 大会上发布了新消息：其 Linux 模拟器（Linux Emulator）现已正式发布，包括语义重排和智能体内存工具包在内的全新 AI 功能也正处于预览阶段。选择 Cosmos DB 作为其主要操作型数据库的 OpenAI 被作为标杆客户提及。

同样在 Build 大会上发布的还有：[Rayfin：一款全新的开源 SDK 和 CLI](https://thenewstack.io/microsoft-build-2026-rayfin-replit-vibe-coding/)，它能让开发人员和编码智能体构建企业级应用后端并直接部署到 Fabric 中，此外，通过与 Replit 的合作，将基于氛围编程（vibe-coded）的应用带入到该平台中。