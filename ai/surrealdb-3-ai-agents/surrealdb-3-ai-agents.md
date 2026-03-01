<!--
title: 数据库未为代理蔓延而生，SurrealDB破局之道
cover: https://cdn.thenewstack.io/media/2026/02/89745970-surrealdb.png
summary: SurrealDB推出多模型数据库3.0版，旨在解决AI代理带来的“架构蔓延”问题。它在一个引擎内整合事务、记忆、向量和关系数据，简化了AI工作负载。新版本强化了代理内存和向量功能，并引入插件系统，同时采用源代码可用许可模式，平衡开放与商业控制。
-->

SurrealDB推出多模型数据库3.0版，旨在解决AI代理带来的“架构蔓延”问题。它在一个引擎内整合事务、记忆、向量和关系数据，简化了AI工作负载。新版本强化了代理内存和向量功能，并引入插件系统，同时采用源代码可用许可模式，平衡开放与商业控制。

> 译自：[Databases weren’t built for agent sprawl – SurrealDB wants to fix it](https://thenewstack.io/surrealdb-3-ai-agents/)
> 
> 作者：Paul Sawers

AI 代理无法很好地融入企业数据栈的设计方式。典型的代理需要事务状态（例如，刚刚发生了什么）、长期记忆、相似性搜索、关系感知数据以及实时响应数据变化的能力。在大多数组织中，这意味着将关系数据库、向量存储、图引擎和多层中间件拼接在一起，以保持所有内容同步。

> “AI 代理无法很好地融入企业数据栈的设计方式。”

这种架构虽然可行，但伴随着延迟、数据重复和操作开销。随着基于代理的系统投入生产，其复杂性成为一个真正的负担。这就是为什么 [SurrealDB](https://surrealdb.com/) 致力于解决其所谓的“架构蔓延”问题，它使用一个多模型数据库，旨在单一引擎内处理结构化记录、关联数据和 AI 工作负载。

该公司由兄弟 [Jamie Morgan Hitchcock](https://www.linkedin.com/in/jaimemorganhitchcock) 和 [Tobie Morgan Hitchcock](https://www.linkedin.com/in/tobiemorganhitchcock/) 于 2022 年创立，总部位于伦敦，刚刚宣布 [SurrealDB 3.0](https://surrealdb.com/3.0) 全面上市。该版本在其现有的多模型基础上，更侧重于持久代理内存、扩展的向量功能和新的数据库内插件系统。

此外，SurrealDB 上周[宣布](https://surrealdb.com/blog/surrealdb-raises-23m-series-a-extension-to-power-the-ai-native-database-era)已获得 2300 万美元的新一轮融资，使其自成立以来的总融资额达到 4400 万美元。

## 被千百个数据库所困

如果说现代软件栈不缺什么，那就是数据库。[PostgreSQL](https://www.postgresql.org/) 支持大量的结构化事务性工作负载。[MongoDB](https://www.mongodb.com/) 已成为面向文档应用程序的默认选择。[Neo4j](https://neo4j.com/) 在图分析和关联数据领域开辟了利基市场。而 [Redis](https://redis.io/) 则主导着内存缓存和实时性能用例。每个数据库都旨在解决一类特定问题，尽管许多数据库已经扩展了其原有功能。

SurrealDB 并没有将自己定位为这些系统的全面替代品。大型企业已投入多年时间来调整和扩展现有数据库栈，这些平台继续很好地服务于其核心工作负载。相反，SurrealDB 认为 AI 原生系统带来了不同的架构压力。代理通常需要在单个工作流程中实现持久的读写状态、结构化和非结构化数据的低延迟检索以及关系感知上下文。这种组合可能会超出传统数据库的界限。

> “SurrealDB 通过让团队将代理的核心状态、上下文记忆和关联数据模型保存在一个地方，从而降低了复杂性。”

首席执行官 [Tobie Morgan Hitchcock](https://www.linkedin.com/in/tobiemorganhitchcock/) 表示 SurrealDB 专注于 AI 原生公司：

“彻底替换最大的部署将是极其昂贵的，”Tobie Hitchcock 告诉 *The New Stack*。“相反，SurrealDB 旨在服务 AI 原生公司和用例——构建 AI 代理；构建知识图谱；构建实时应用程序；嵌入式和边缘计算。”

Hitchcock 认为，这些工作负载的不同之处在于它们如何结合多种类型的数据访问。传统应用程序可以将事务更新、搜索、分析和关系查询分离到不同的系统中。相比之下，代理通常需要近实时地更新状态、检索相关上下文并对关联数据进行推理。这可能意味着数据需要在多个存储和索引之间复制，以保持一切同步。

“将数据发送到单独索引和存储的传统模式会增加延迟、数据重复并带来重大风险，”Hitchcock 说。

他说，SurrealDB 的解决方案是将这些移动部件整合到一个系统中——将结构化状态、上下文记忆和关联数据保存在一起。

“SurrealDB 通过让团队将代理的核心状态、上下文记忆和关联数据模型保存在一个地方，从而降低了复杂性，”Hitchcock 说。

## 扩展数据库层

虽然 SurrealDB 长期以来一直支持单一引擎内的多种数据模型，但 3.0 版本引入了一个正式的扩展系统，并将更多应用程序逻辑直接引入到数据库层。

[Surrealism](https://surrealdb.com/surrealism) 是一种开源插件框架，允许开发人员将业务逻辑、访问控制和 API 行为定义为版本控制的模块，这些模块在 SurrealDB 内部运行。团队可以打包和共享具有完整事务保证的扩展，而无需仅仅依赖外部服务或绑定到单一部署的存储过程。

实际上，这可能意味着直接在数据库内部生成模拟数据进行测试，暴露 Rust 库中的专用功能（这些功能通常存在于应用程序代码中），或者将领域特定逻辑（如语言处理或财务计算）嵌入到更靠近其操作数据的位置。

除了 Surrealism，SurrealDB 3.0 还为公司的持久代理内存引入了更明确的支持。这意味着结构化记录、嵌入和关系数据可以存储并在同一个数据库实例中一起查询，而无需跨单独系统进行管理。为支持这一点，该版本扩展了向量索引和相似性搜索性能，并允许使用 SurrealQL 查询结构化数据以及图像、音频和文档。

实际上，该数据库旨在让代理在同一个系统中检索语义相似的内容、查询相关记录并更新状态。

## （并非完全）开源因素

值得注意的是，虽然更广泛的 SurrealDB 平台的某些方面是开源的，但核心数据库本身不是，这一举动明确旨在防止第三方将其作为托管数据库服务提供。这反映了数据库生态系统中吸取的一个教训，即云提供商将开源项目商业化为托管服务。

像 [MongoDB](https://techcrunch.com/2018/10/16/mongodb-switches-up-its-open-source-license/) 和 [Redis](https://techcrunch.com/2019/02/21/redis-labs-changes-its-open-source-license-again/) 这样的公司通过转向专有的、源代码可用的[许可模式](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)来回应，以保留对托管服务的控制权。

“因此，SurrealDB 能够提供一个运行 SurrealDB 的托管平台，该平台由其构建者运营，”Hitchcock 说。“这意味着我们能够提供最可靠、安全和最新的端到端体验。”

简而言之，任何人都可以免费运行和自托管 SurrealDB，如果他们想要一个提供专业知识的完全托管版本，则可以付费使用。

这种方法似乎帮助 SurrealDB 赢得了一些令人印象深刻的企业客户标志，如 Nvidia、Tencent、Walmart 和 Verizon 等公司都自豪地展示在公司主页上。然而，该公司拒绝具体说明哪些是付费客户，哪些正在运行自托管版本。

“不幸的是，由于商业机密，我们无法透露哪些标志是我们的付费客户，”Hitchcock 说。“我们拥有健康混合的商业客户和大规模、非商业的企业部署。”