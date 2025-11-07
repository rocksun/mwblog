<!--
title: 重塑PostgreSQL：赋能下一代应用
cover: https://cdn.thenewstack.io/media/2025/11/079a5804-reinventingpostgresqlnextgenerationapps.jpg
summary: PostgreSQL凭借开源治理、可靠性和适应现代分布式应用（如AI、边缘和Kubernetes）的优势，成为Oracle、SAP等昂贵方案的战略替代，且具备低总拥有成本。
-->

PostgreSQL凭借开源治理、可靠性和适应现代分布式应用（如AI、边缘和Kubernetes）的优势，成为Oracle、SAP等昂贵方案的战略替代，且具备低总拥有成本。

> 译自：[Reinventing PostgreSQL for the Next Generation of Apps](https://thenewstack.io/reinventing-postgresql-for-the-next-generation-of-apps/)
> 
> 作者：Chris J. Preimesberger

企业不会随意更新数据库。当延迟成为业务负担时，当全球正常运行时间不容妥协时，当许可压力变得难以忍受时，以及当开发人员需要比采购周期允许的更快地行动时，他们才会这样做。如今，这些因素越来越多地推动组织选择 [PostgreSQL](https://roadmap.sh/postgresql-dba) 作为 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) 和 [SAP](https://www.sap.com/index.html?utm_content=inline+mention) 等昂贵现有方案的替代品。

在与开源Postgres供应商 [pgEdge](https://www.pgedge.com/?utm_content=inline+mention) 的工程副总裁、PostgreSQL社区的长期领导者 Dave Page 交流时，一个信息很明确：这一趋势并不仅仅是为了选择“更便宜”的数据库。它关乎可靠性、控制力以及运行现代工作负载的能力：无论是AI驱动的、边缘分布式的，还是 [Kubernetes](https://thenewstack.io/kubernetes/)-编排的，且没有供应商锁定或基础设施的死胡同。

## 开源PostgreSQL的优势

Page自1990年代末以来一直在PostgreSQL生态系统工作。对他来说，其最大的差异化优势并非某个单一功能，而是PostgreSQL的治理模式。Page表示：“PostgreSQL背后没有一个公司。”

> [Postgres] 不是小众开源；它是主流企业技术，拥有庞大的人才储备和技能管道。

在数据库许可审计、强制升级和封闭生态系统让CIO们感到沮丧的当下，这种独立性显得尤为重要。pgEdge 秉持这一原则；该公司最近将其所有终端用户工具在 [PostgreSQL许可](https://www.postgresql.org/about/licence/) 下开源——这是一种宽松的许可，没有锁定，并提供完整的源代码。

PostgreSQL已经拥有全球最大的开发者社区之一，拥有数百万次 [Docker](https://www.docker.com/?utm_content=inline+mention) 拉取量和广泛采用的工具，例如 pgAdmin。这不是小众开源；它是主流企业技术，拥有庞大的人才储备和技能管道。

怀疑论者理所当然地会问，开源是否会增加运维负担。但事实恰恰相反，像 pgEdge 这样的开源扩展允许开发者最大化 PostgreSQL 在特定用例中的效用，例如确保高可用性、服务边缘网络或跨多个云和区域部署。

Page表示：“pgEdge 将Postgres投入分布式使用——无需DIY脚本。CNPG [CloudNativePG] 自动化了升级、备份和PITR [时间点恢复]。Kubernetes资源调优提高了硬件效率。迁移是增量的，而非推倒重来。”

Page表示，凭借自动化和支持的成熟度，开源路径的总拥有成本趋势在企业规模上决定性地胜过专有数据库许可模式。

## 为什么现代应用需要边缘原生数据库

现代应用不再仅仅运行在集中式数据中心。它们运行在边缘，靠近用户、设备和事件，以最小化延迟并保持响应性。Page直截了当地说：让你的数据库运行在你的应用运行的地方。

这使得选择像 pgEdge 这样支持跨地理分布式集群的 [多主](https://www.pgedge.com/solutions/benefit/multi-master) PostgreSQL 解决方案变得尤为重要。他解释说：“借助这些工具，每个区域都可以以极低的延迟进行本地读写，而异步复制则保持全球范围数据的一致性。如果一个区域离线，流量可以转移到其他地方；当它恢复时，它会自动重新同步并重新加入。”

Page表示，重要的是，pgEdge 没有分叉 PostgreSQL。

他说：“它建立在Postgres的逻辑复制传承之上，并为其多区域、多写入生产拓扑进行增强，同时保留了兼容性和生态系统的一致性。其结果是真正对边缘友好的Postgres，适用于全球实时应用——从零售、物联网 [Internet of Things] 到金融和互联医疗。”

## 使用Kubernetes原生工具自动化PostgreSQL

企业团队希望数据库自动化能够匹配他们的 Kubernetes 投资，而受人尊敬的开源 Postgres 运算符 [CNPG](https://cloudnative-pg.io/) 正是为此而来。凭借 Helm charts 和强化镜像，pgEdge 使团队能够在单节点、主从高可用集群以及完整的多主、多区域 [分布式Postgres](https://www.pgedge.com/products/what-is-distributed-postgres) 中部署 [Kubernetes上的Postgres](https://www.pgedge.com/products/postgres-kubernetes)。

每个边缘站点都可以运行自己的 Kubernetes 集群，并带有一个本地 Postgres 节点。CNPG 处理备份、PITR、滚动更新，甚至主要版本升级，这在历史上是 Postgres 最复杂的任务之一。Page说：“对于平台团队来说，这感觉像是Postgres的控制平面，而不是需要照看的脚本。”

这正是 Postgres 胜过那些拥有单一供应商控制台和专业服务依赖的专有数据库的地方。相反，你获得的是与 GitOps 和站点可靠性工程（SRE）工作流对齐的、由操作员驱动的云原生生命周期自动化。

## 随着业务增长扩展您的数据库架构

很少有组织一开始就采用多区域架构，但当业务增长需要扩展时，你希望有一个平稳的演进：从单节点或主从架构开始；根据需要添加更多区域；并在准备好时启用多主复制。相同的 Postgres 堆栈支撑着每个阶段。Page表示，无需迁移到专有集群、避免架构陷阱或为全球扩展支付吞吐量税。这使得团队的扩展更加直接，并为企业节省了成本。

> 本地读写性能加上全局数据一致性正是边缘原生AI所需要的，尤其是在实时上下文或本地决策至关重要时。

pgEdge 提供两种容器构建：Minimal，包含核心 Postgres 加多主复制；以及 Full，包含 PostGIS 和 [pgvector](https://thenewstack.io/postgres-is-now-a-vector-database-too/) 等关键扩展。

这种组合涵盖了两个日益增长的企业需求：地理空间智能（物流、电信、公共部门）和通过 pgvector 进行嵌入的AI检索工作流。在同一系统中运行向量和关系数据消除了运维开销，并避免了额外搭建专有AI数据库的需求。

## 高性能Postgres

出于性能、隐私和成本考虑，AI推理越来越多地在边缘运行。Page证实 pgEdge 有客户将AI应用和模型与分布式 Postgres 一起运行。本地读写性能加上全局数据一致性正是边缘原生AI所需要的，尤其是在实时上下文或本地决策至关重要时。

这种部署模式预示着一个新兴趋势：AI堆栈以分布式Postgres为核心，而不是独立的向量引擎或专有插件。

Page表示，更多与AI相关的增强功能正在开发中，并指出 pgEdge 的策略是推出生产就绪的功能，而不是炒作驱动的实验。

pgEdge 支持在私有云、受监管的虚拟私有云（VPC）环境以及完全气隙部署中运营的客户。由于其平台是开源的，安全团队可以审计代码和运维组件。受监管的行业不再需要依赖供应商提供特殊的“离线”版本，因为 pgEdge 在设计上就能在任何地方运行。

## SQL兼容性与庞大的人才库

PostgreSQL 对 [SQL](https://roadmap.sh/sql) 和 [ACID](https://thenewstack.io/can-nosql-databases-be-acid-compliant/) 的忠实遵循保证了它是一个重要的迁移推动者。团队可以更顺畅地将工作负载从 Oracle 和 SAP 迁移出来，而不是跳到 NoSQL 或“新 SQL”专有系统。

雇佣PostgreSQL人才也很容易。Page指出，虽然活跃贡献者代表了社区核心，但其用户群体庞大——涵盖金融、电信、软件即服务（SaaS）、制造业和公共部门。这意味着企业人员配置和长期支持的稳定性。

实际上，pgEdge 用户正在利用该技术栈标准化分布式系统文档；自动生成带有覆盖目标的测试；支持边缘站点的迭代重构；以及在 OLTP 工作负载旁边驱动向量搜索。这些都是现代应用的现实：持续迭代、AI驱动的功能、分布式部署足迹和运维一致性。

## 分布式PostgreSQL的战略优势

PostgreSQL 加 pgEdge 不仅仅是一种经济选择。Page表示，对于需要 [多区域、多主可靠性](https://www.pgedge.com/landing-pages/multi-master-whitepaper)；Kubernetes原生运维；pgvector等AI就绪扩展；随处部署（云、混合、边缘或气隙）；以及摆脱供应商锁定和惩罚性许可的企业来说，这是一条战略性的现代化道路。

对于架构师而言，它将PostgreSQL转变为一个全球分布式、云原生的数据控制平面。对于首席财务官而言，它改变了数据库的成本曲线。他说，对于开发人员而言，它保留了他们熟悉和信任的工具链和SQL模型。

最重要的是，它为企业节省了时间——不再浪费在审计、版本陷阱、手动故障转移或延迟排查上。

免费开始使用 pgEdge，并在准备好时添加支持。访问 [开始页面](https://www.pgedge.com/get-started) 了解更多。