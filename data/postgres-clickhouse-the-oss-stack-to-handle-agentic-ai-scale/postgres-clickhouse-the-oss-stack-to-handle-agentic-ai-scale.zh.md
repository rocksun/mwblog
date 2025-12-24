Postgres 是引导应用程序的常用选择，因为它广为人知、灵活且可靠。其灵活性意味着它可以在一段时间内处理您交给它的大部分任务。随着应用程序的扩展，Postgres 常常会被其未设计处理的工作负载推向极限。

应用程序达到这些极限的点并未改变，但由于 AI 的发展，达到该点所需的时间已大大缩短。

解决这一问题的一种新兴模式是将 [Postgres](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/) 与 ClickHouse 结合。在这种架构中，[Postgres 继续服务事务性工作负载](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/)，而 [ClickHouse 处理分析](https://thenewstack.io/vector-search-without-the-lock-in-why-devs-like-clickhouse/)。这两个数据库都是开源的，并且已发展出一个生态系统，使它们更紧密地结合在一起。

## 超越 PostgreSQL 的扩展能力

在 AI 时代，过去需要数年才能实现的增长现在在数月内发生。开发人员更快地达到了 Postgres 的极限，因为 AI 驱动的工作负载加速了产品开发、数据创建和分析需求。

这种趋势不仅限于内部仪表盘或离线报告。更多时候，它正在影响面向用户的应用程序。实时仪表盘、推荐系统以及对大型数据集的搜索都依赖于快速的分析查询。一旦这些功能成为用户体验的一部分，[架构就必须支持对大量数据的低延迟访问](https://clickhouse.com/blog/langchain-why-we-choose-clickhouse-to-power-langchain#what-were-the-challenges-you-faced-with-postgres)，而仅靠 Postgres 是不够的。

## Postgres + ClickHouse 如何协同工作

构建同时使用 Postgres 和 ClickHouse 的应用程序通常涉及两个主要挑战。第一个是数据集成，即如何将正确的数据移动到正确的数据库。第二个是应用程序集成，即如何确保应用程序知道对每个操作查询哪个数据库。

### 数据集成

将 ClickHouse 与 PostgreSQL 集成有两种常见模式。

**拆分写入或双写**：应用程序根据具体的用例直接将数据写入 PostgreSQL 和 ClickHouse。拆分写入模式只将数据写入需要的数据库，而双写模式则同时将所有数据发送到两个系统。当数据用途有明确区分时，这种方法效果很好。例如，遥测或用户跟踪事件不太可能需要发送到 Postgres，因为它们可能只用于分析。支持这种模式意味着需要更新应用程序以将数据发送到正确的数据库。

![](https://cdn.thenewstack.io/media/2025/12/c9f2dbcd-image2-981x1024.png)

**变更数据捕获 (CDC)**：所有写入都发生在 PostgreSQL 中，PostgreSQL 仍然是事实的来源。[CDC 过程将插入、更新和删除流式传输到 ClickHouse](https://clickhouse.com/blog/seemplicity-scaled-real-time-security-analytics-with-postgres-cdc-and-clickhouse#hitting-the-postgres-bottleneck-and-why-cdc-matters)，因此分析查询始终反映最新状态，而不会对事务性数据库施加额外负载。这种模式适用于操作分析用例，其中一致性至关重要，但[分析性能仍然是优先事项](https://clickhouse.com/blog/sewerai-sewer-management-at-scale#postgres-to-peerdb-to-clickpipes)。它允许团队在 PostgreSQL 中维护事务保证，同时在 ClickHouse 中独立扩展分析查询。

![](https://cdn.thenewstack.io/media/2025/12/810109d7-image1-1024x907.png)

### 应用程序集成

集成 Postgres 和 ClickHouse 的目标是让每个数据库都用于其最擅长的工作负载。这意味着一些查询将保留在 Postgres 上，而另一些将移动到 ClickHouse。

[许多应用程序将对象关系映射器 (ORMs) 与 Postgres 结合使用](https://clickhouse.com/blog/moosestack-does-olap-need-an-orm)，但这在分析型数据库中不太常见。有一些[像 MooseStack 这样的开源项目](https://clickhouse.com/blog/clickhouse-powered-apis-in-react-app-moosestack)，可以为 [ClickHouse 提供类似 ORM 的体验](https://clickhouse.com/blog/eight-principles-of-great-developer-experience-for-data-infrastructure)。更常见的是，集成使用 [ClickHouse 原生语言客户端](https://clickhouse.com/docs/integrations/javascript)。

集成将从识别将要移动的查询开始，例如任何执行大型聚合查询的查询。这些查询的 API 路由需要更新，以便将 SQL 发送到 ClickHouse。可以使用一种向后兼容的模式，允许在测试期间将这些路由在 Postgres 或 ClickHouse 之间切换。这种模式被 [clickhouse.build](https://clickhouse.com/blog/clickhouse-build-agentic-cli-accelerate-postgres-clickhouse-apps) 使用，它是一个代理式 CLI，可以自动迁移 TypeScript 代码库以使用 Postgres 和 ClickHouse 进行原型开发。

另一种方法是在 Postgres 内部使用外部数据包装器 (FDW)，它允许将查询原样发送到 Postgres 并透明地推送到 ClickHouse。这减少了开始同时使用 Postgres 和 ClickHouse 所需的工作量，尽管可能会牺牲对集成的一些控制。

## 一个开源生态系统

Postgres 和 ClickHouse 生态系统已发展成为一个成熟的技术栈。许多团队现在默认将这两个数据库配对使用，一套成熟的开源和商业工具使得这种架构在生产规模下易于操作。这些工具的重点是明确且有目的的：可靠的 Postgres 复制、快速地将数据摄入 ClickHouse 以及与现有 Postgres 工作流的顺畅集成。

### **PeerDB**

[PeerDB 是一个开源项目](https://www.peerdb.io/)，提供高吞吐量的 PostgreSQL CDC 和到 ClickHouse 的可靠复制。它支持大型更新流、处理模式更改并避免对事务性数据库造成负载。PeerDB 还支持像 [ClickHouse Cloud 的 ClickPipes](https://clickhouse.com/blog/postgres-cdc-connector-clickpipes-ga) 这样的托管服务。

### **PostgreSQL 可扩展性和 FDWs**

PostgreSQL 扩展模型帮助团队将分析工作负载转移到 ClickHouse，而无需更改其应用程序代码。FDWs 通过将外部系统公开为常规 PostgreSQL 表来实现这一点。[Supabase 的 ClickHouse FDW](https://supabase.com/docs/guides/database/extensions/wrappers/clickhouse)、开源的 [clickhouse_fdw](https://github.com/ildus/clickhouse_fdw) 以及类似的扩展允许应用程序继续通过 Postgres 发出熟悉的 SQL，而繁重的分析查询则在 ClickHouse 中运行。这使得应用程序层保持不变，并为随着工作负载增长将分析从 Postgres 转移提供了一条平稳的路径。

### **ORMs 和开发人员工具**

[MooseStack](https://docs.fiveonefour.com/moose#get-started) 等项目表明开发人员工具正在跟上步伐。它们使得在 ORMs 或模式优先开发模式为标准的开发环境中更容易使用 ClickHouse。

总的来说，围绕 Postgres 和 ClickHouse 的生态系统不仅仅是工具的集合。它是一个专注且广受欢迎的技术栈，专为那些超越单一在线事务处理 (OLTP) 数据库需求，并需要快速分析引擎同时不失去熟悉 Postgres 开发工作流的团队而设计。

## 未来

如今，许多应用程序从 Postgres 开始，然后在问题出现后才采用 ClickHouse。随着这一时间线的缩短，在产品生命周期开始时就采用这种架构变得更有意义。开发人员应该能够开箱即用地使用 Postgres + ClickHouse，同时对产品速度的影响最小。

托管服务、托管复制以及工具之间更深层次的集成已经朝着这个方向发展。目标是实现事务和分析系统默认协同工作的无缝体验。

核心原则保持不变：Postgres 和 ClickHouse 不是相互竞争的技术。它们相互补充，共同构成了现代开源数据架构的基础，这种架构灵活、透明且适合生产环境。