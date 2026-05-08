<!--
title: Redis和ClickHouse遇到瓶颈后，ScyllaDB助力Sprig读取延迟降低4倍
cover: https://cdn.thenewstack.io/media/2026/05/b987245c-alghozy-uk8p08no3k8-unsplash-scaled.jpg
summary: Sprig在面临150亿访客和万亿级事件的挑战时，先后遭遇了Postgres、Redis及ClickHouse的性能瓶颈。最终通过迁移至ScyllaDB Cloud，成功将读取延迟降低4倍，显著提升了扩展性并降低了成本。
-->

Sprig在面临150亿访客和万亿级事件的挑战时，先后遭遇了Postgres、Redis及ClickHouse的性能瓶颈。最终通过迁移至ScyllaDB Cloud，成功将读取延迟降低4倍，显著提升了扩展性并降低了成本。

> 译自：[ScyllaDB cut Sprig's read latency 4X after Redis and ClickHouse hit a wall](https://thenewstack.io/sprig-postgres-scylladb-migration/)
> 
> 作者：Cynthia Dunlop

“只管用 Postgres”是初创公司寻找产品市场契合点（PMF）时的逻辑路径。但 AI 驱动的产品研究平台 Sprig 达到这一契合点的速度远超预期。随之而来的海量数据（来自 150 亿访客的超过 1.3 万亿个事件和 750 亿个属性）使 Postgres 达到极限的速度也远超预期。

在 3 月份的 Monster Scale 峰会上，Sprig 的资深主任工程师 [Brendan Cox](https://www.linkedin.com/in/justnoise/) 介绍了完整的历程：为什么他们看似简单的平台会如此快地触及数据库限制，他们尝试过的各种方法，以及他们的小型工程团队如何攻克这些挑战。您可以观看完整演讲，或阅读下文的精华摘要。

## Sprig 表面简洁背后的复杂性

从表面上看，Sprig 的核心产品相对直观。客户在他们的移动应用或网站中安装 Sprig SDK，以跟踪用户行为和属性。当用户的行为符合设定标准时，Sprig 就会触发有针对性的产品内调查。由于这些调查收集了大量反馈，Sprig 随后使用 AI 处理并为产品研究人员报告研究结果。

在底层，需要一个高速数据引擎来实时评估所有这些用户行为。“我们构建的系统实际上与分析、广告技术或推荐系统有很多共同点，”Brendan 解释道。“也就是说，它是一个低延迟、计算密集且数据密集型的系统，每秒必须做出多达数千次的决策。”

对于一家小型初创公司来说，Sprig 管理的数据量惊人。在任何给定时间内，该平台都在多个设备上跟踪 **150 亿独立访客**。为了了解这些访客，后端维护着 **750 亿个用户属性** 和 **200 亿个不同的事件计数器**，至今（截至 2026 年 2 月）已[处理了超过 1.3 万亿个事件](https://thenewstack.io/how-event-processing-builds-business-speed-and-agility/)。

![解释 Sprig 是什么的信息图。](https://cdn.thenewstack.io/media/2026/05/a07f7f91-1-1024x576.png)

Sprig 的后端系统每秒处理 20,000-40,000 个事件和属性。对于每个传入的事件，系统必须评估复杂的触发标准，并在几毫秒内决定是否显示调查。

## 第一阶段：只管用 Postgres

起初，Sprig 遵循经典的初创公司剧本：他们在 [PostgreSQL](https://thenewstack.io/postgres-ai-ground-truth/) 上构建了初始系统（他们选择了 Amazon Aurora 版本）。正如 Brendan 所说：“这正是每家初创公司*应该*开始的地方。基本上，只需做简单的事情并找到产品市场契合点”。

Sprig 发现产品市场契合点的速度惊人。然而，随着越来越多的重磅客户加入系统，他们触及了 Postgres 的极限。Brendan 表示：“我们的写入吞吐量很高，这使 Aurora 中的单个写入实例达到饱和。我们也达到了当时 AWS 能够提供给我们的读取实例数量上限和最大实例规格。这对我们公司来说非常昂贵。我们绝对有必要尽快离开这个系统，转向新的系统。”

## 第二阶段：增加 ClickHouse 和 Redis

因此，团队提出了一种新方法。他们决定只在 Postgres 上保留访客数据，然后将“事件和属性”流量卸载到完全不同的设置中：位于 Redis 直写式缓存之后的 ClickHouse 数据库。

访客数据存储在一个大型的、未分区的 Postgres 表中（他们需要跨多列查询，这需要多个索引）。每个 SDK 调用都必须检索一条访客记录，这每秒向 Postgres 实例触发 30,000-50,000 次请求。

然而，事件和属性具有更高的吞吐量和容量。他们根据以往的成功经验选择了 ClickHouse 来处理这些数据。但是，由于 ClickHouse 并不适合高吞吐量的点查询，他们在它前面放置了 Redis 作为直写式缓存。

Redis 提供了处理传入事件和属性请求所需的完整工作集。它处理了大部分请求流量，而 ClickHouse 则作为记录系统运行在其后。ClickHouse 每秒吸收 40,000 – 50,000 次插入，同时处理较为适中的每秒 2,000 – 6,000 次读取。

![描述 ClickHouse 和 Redis 的信息图](https://cdn.thenewstack.io/media/2026/05/b8c4190f-2-1024x576.png)

然而，即使是那样的读取量也高于 ClickHouse 作为分析数据库的初衷。因此，团队进行了各种优化和配置调整。具体来说，他们对访客 ID 进行哈希处理，以确保查找只命中单个分区，并将 ClickHouse 的 granule 大小缩小到标准 8,200 行以下，以最小化磁盘 I/O。他们还严格最小化了线程数；通过将最大线程设置为 1 并使用 `pread` 文件系统读取方法，他们防止了线程在繁重的查找过程中不断进行上下文切换和争抢 CPU。

## Postgres + Redis + Clickhouse 的不足之处

尽管进行了这些读取优化，扩展写入仍然是一个挑战。在 Postgres 方面，在单个未分区的表中存储 150 亿行数据变得越来越成问题。工作集不再能装入内存，导致频繁的磁盘读取和飙升的 AWS IOPS 成本。

尾部延迟已经在恶化（P99 约为 50ms）。而且由于 Postgres 运行在共享环境中，即使是一个低效查询或缺失索引也会进一步降低性能。

与此同时，ClickHouse + Redis 的设置也显示出压力迹象。尽管进行了广泛的优化，P90 和 P99 延迟仍然很高（P99 约为 50ms），并且系统在访问模式切换、批处理任务或工作负载变化时会经历周期性的性能下降（brownouts）。

除此之外，增长预测预计写入吞吐量将增加 3-5 倍。

真正的警钟敲响是在他们与 AWS Postgres 专家会面试图解决问题时。“这可能是我见过的最大的未分区 Postgres 表，”一位 AWS 专家告诉 Sprig 团队。

> “这可能是我见过的最大的未分区 Postgres 表。”

这并不完全是他们想听到的。“我们知道我们飞得很高，但我们没意识到我们比任何人都飞得高，也不知道我们离太阳有多近，”Brendan 回忆道。“我们不知道这一切什么时候会崩溃。”

## 寻找合适的数据库匹配

为了在一切崩溃前找到更好的方法，团队对四个选项进行了系统评估：

* **DynamoDB：** 因成本被否决。在 Sprig 的事件和属性量级下，DynamoDB 的读/写容量单位定价将是望而却步的。团队之前经历过的痛苦的写入可靠性问题也将其排除在外。
* **DataStax Astra：** 在基准测试显示更高的延迟和不确定的扩展行为后被否决。此外，IBM 的收购增加了一层他们不放心的风险。
* **在 Kubernetes 上自托管 Cassandra：** 因两个理由被否决：测试中立即出现的不可接受的尾部延迟，以及由两人团队运行大型基于 Java 的分布式数据库的运维开销。
* **在带有 EBS 卷的 Kubernetes 上自托管 ScyllaDB：** 技术上这是可行的，尽管这不是推荐的配置。但是，团队否决了它，因为他们不想在运维上再管理一个分布式数据库。

![说明所考虑的四个扩展选项的要点](https://cdn.thenewstack.io/media/2026/05/520169c1-3-1024x576.png)

但他们喜欢 ScyllaDB，尤其是它在 Sprig 的规模下表现出的低延迟。Brendan 解释说：“我们 90%-95% 的读取都是缓存的，所以 ScyllaDB 配合快速行缓存非常适合我们的工作负载。”

同样重要的还有：ScyllaDB 提供了原生的、高性能的物化视图。Sprig 需要它们跨多列为庞大的访客表建立索引。虽然 Cassandra 的物化视图“在 Cassandra 社区备受诟病，且不再获得官方正式支持”，但 ScyllaDB 的物化视图在 Sprig 的测试中表现得“坚如磐石”。

决定性因素是全托管的部署模型。“ScyllaDB Cloud 让我们的工程师能够专注于我们的核心竞争力，即构建系统和支持我们的产品，”Brendan 表示。“很棒的是，我们有数据库专家——那些真正构建了该系统的人——来为我们运行数据库。”

## 第三阶段：迁移到 ScyllaDB Cloud

Sprig 现有的架构使迁移变得更加容易：

* **通过 Kafka 连接器进行实时写入。** 所有流入 ClickHouse 的数据都已经通过 Kafka。团队编写了一个 Kafka 连接器，将该数据同步写入 ScyllaDB，让两个系统并行运行。
* **通过批量加载器进行历史数据回填。** 一个自定义的批量加载器从 ClickHouse 提取现有记录并将其写入 ScyllaDB，与 Kafka 连接器并发运行。
* **竞态条件处理。** 由于两条写入路径同时运行，他们需要一个冲突解决策略。他们使用了“最后写入者胜（last-write-wins）”策略，将每条记录上的 updated\_at 字段作为权威时间戳。

![描述迁移到 ScyllaDB cloud 的工作流信息图](https://cdn.thenewstack.io/media/2026/05/83a14e19-4-1024x576.png)

为了增强对迁移的信心，团队构建了一个验证层，同时从 ClickHouse/Redis 集群和 ScyllaDB 进行双重读取。他们比较了两个系统之间的值，并将一致和差异部分通过管道传输到 Prometheus。“我们记录了差异，以帮助我们深入了解数据不一致性，并真正调试问题出在哪里，”Brendan 解释道。

一旦两个系统之间的一致性达到约 99.99%，他们就切换了开关，开始向 ScyllaDB 进行读写。

“这并不令人兴奋……直到我们看了延迟图表。”

![显示 ScyllaDB 和 Redis 的 P99 延迟的图表](https://cdn.thenewstack.io/media/2026/05/1c6491e8-5-1024x576.png)

在解释 ScyllaDB 与 Redis 的延迟结果时，Brendan 说：“对于我们的属性工作负载，我们看到从 ScyllaDB 读取的延迟比 Redis 低约 4 倍。我们从 Redis 读取了相当多的数据，而 ScyllaDB 对此支撑得非常好。总的来说，我们来自 ScyllaDB 的平均延迟约为 500 微秒，我们的 P90 延迟约为 1-2 毫秒。这比我们在 Redis 设置中看到的要好 4-8 倍。”

> “对于我们的属性工作负载，我们看到从 ScyllaDB 读取的延迟比 Redis 低约 4 倍。我们从 Redis 读取了相当多的数据，而 ScyllaDB 对此支撑得非常好。”

除了可预测的低延迟外，警报也变少了，团队不再需要不断地调整数据库。对于不断增长的业务来说，最重要的是，随着新客户和新工作负载的加入，他们可以根据需要轻松地扩展集群。

团队待办事项列表上的下一步：

* 从分层压缩（Leveled Compaction）切换到增量压缩（Incremental Compaction）策略，这提供了更好的写入放大特性，非常适合缓存读取。
* 使用工作负载优先级（Workload Prioritization），确保沉重的周末批处理作业永远不会影响实时的生产读取。
* 将更多表从 Postgres 移动到 ScyllaDB。

Brendan 总结了这个项目：“这次迁移对我们团队来说是一个巨大的成功，不仅在数据库性能方面，在成本效率和可扩展性方面也是如此。它极大地降低了我们基础设施的[运维复杂性](https://thenewstack.io/self-driving-devops-how-stakpak-tackles-infrastructure-complexity/)。”