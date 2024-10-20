
<!--
title: OVHcloud 如何提升其 800 个数据库的效率
cover: https://cdn.thenewstack.io/media/2024/10/5291016d-how-ovhcloud-made-its-800-databases-more-efficient-2.jpg
-->

诸如 Grafana 之类的监控工具以及公司内部 SQL 技能的培养大大减少了慢查询并提高了弹性。

> 译自 [How OVHcloud Made Its 800 Databases More Efficient](https://thenewstack.io/how-ovhcloud-made-its-800-databases-more-efficient/)，作者 Robert Kimani。

在法国云服务提供商 [OVHcloud](https://us.ovhcloud.com/)，一个专门的数据库运营小组肩负着一项关键任务：确保构建公司控制平面和数据平面的内部产品团队能够访问弹性、可扩展且高性能的数据库基础设施。

9 月，在伦敦举行的 [SREday](https://sreday.com/2024-london/) 大会上，OVHcloud 数据库和可观测性工程经理 [Wilfried Roset](https://www.linkedin.com/in/wilfriedroset) 讲述了数据库运营团队如何从被动地解决性能问题发展到主动优化数据库集群，从而显著减少慢查询并提高可观测性。

OVHcloud 的数据库运营团队改变了其管理和优化基础设施的方式。从增强可观测性到扩展硬件以及将慢查询减少 50%，该团队成功构建了一个可扩展且可靠的数据库服务，可以满足其内部产品团队的需求。

该团队专注于持续改进、SQL 优化和由 [服务级别目标 (SLO)](https://thenewstack.io/sre-fundamentals-differences-between-sli-vs-slo-vs-sla/) 驱动的性能指标，为面临类似规模挑战的数据库团队提供了蓝图。

## 挑战：对可扩展数据库的需求不断增长

OVHcloud 提供了种类繁多的云服务，开发这些服务的内部产品团队高度依赖数据库运营团队提供的基础设施。

数据库团队的客户不是外部客户，而是负责开发 OVHcloud 服务的内部工程团队。反过来，这些团队需要快速、可靠地访问数据库，才能构建其控制平面和数据处理解决方案。

OVHcloud 的基础设施在 Kubernetes 上运行，拥有 100 多个生产数据库 [集群](https://thenewstack.io/kubernetes-building-blocks-nodes-pods-clusters/)，但可以容纳虚拟机和裸机服务器。这是一个灵活的架构，旨在通过负载均衡器有效地将读取和写入流量路由到每个集群中的专用节点。

然而，挑战在于如何在规模上保持最佳性能，尤其是在服务和客户数量不断增长的情况下。

## 基础设施：弹性、灵活的数据库集群

OVHcloud 目前运行的数据库集群通常由三个节点组成。一个主节点管理写入流量，而其他节点处理只读请求和备份。该架构在 [PostgreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/) 和 [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/) 数据库之间共享，每个节点都设计用于卸载专门的工作负载。

“这种设置非常适合我们，因为它允许产品团队在无需考虑数据库管理的情况下进行操作，”Roset 对 SREday 的观众说。“我们确保基础设施根据需要进行扩展，支持备份并自动平衡负载。”

产品团队受益于适应其需求的数据库系统，该系统可以随着服务的增长而扩展，同时通过高效的负载均衡保持可靠性。

## 需要更好的可观测性

随着需求的增加，数据库团队开始遇到瓶颈。产品团队经常报告性能问题，但由于缺乏 [可观测性](https://thenewstack.io/observability/)，诊断这些问题变得很困难。

“当我们的公共云团队负责人询问为什么他们的控制平面很慢时，我们无法立即给出答案。我们正在通过 SSH 连接到各个服务器并手动跟踪日志，”Roset 说。这种被动的故障排除既耗时又低效。

数据库团队认识到需要一种更加结构化的方法来进行监控，因此实施了一个可观测性堆栈，将来自 PostgreSQL 和 MySQL 的日志提取到 [OpenSearch](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/) 集群中，并集中管理关键指标。

“我们将系统、数据库和负载均衡器指标集成到 [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) 仪表板中，”Roset 补充道。“这使我们能够在一个地方可视化所有内容，从慢查询计数到整体系统运行状况。”

他说，可观测性堆栈使团队能够实时跟踪性能并更快地响应问题。“以前，我们只有在产品团队报告问题后才会知道。现在，我们可以实时查看正在发生的问题，并在问题升级之前解决它们。”

## 升级硬件以提升性能

改进后的可观测性表明，许多性能问题源于硬件不足。随着 OVHcloud 内部数据库工作负载的增长，支持这些工作负载的硬件变得越来越吃紧。

数据库团队成员意识到，他们需要升级基础设施，以便更好地支持对其提出的需求。Roset 说：“我们通过升级到更快的 CPU、添加更多内存、提高磁盘速度和增强所有节点的网络吞吐量来实现垂直扩展。”

这些升级对于解决许多性能瓶颈的根本原因至关重要。然而，仅仅改进硬件是不够的。低效的工作负载，尤其是优化不良的 SQL 查询，仍然会导致性能问题。这促使数据库团队对工作负载优化采取更全面的方法。

## 优化 SQL 查询可将慢查询减少 50%

一个改进领域来自优化 SQL 查询。最初，团队在一个数据库上每周观察到超过 200 万个慢查询。凭借其新的可观测性工具提供的洞察力，团队着手减少这一数字。

Roset 说：“我们将慢查询定义为执行时间超过一秒的查询，但随着我们优化工作负载，我们逐渐将该阈值降低到 250 毫秒。”

为了解决慢查询问题，团队启动了一项持续的查询优化计划，每周分析日志并识别导致最多慢查询的数据库。

Roset 说，每周一他都会在公司范围内发送一份报告，重点介绍前一周执行最慢查询的数据库。“这是一种让每个人都意识到优化不良的查询的影响的方法，”他说。“如果一个团队的数据库一直出现在报告中，他们就知道他们需要采取行动。”

通过提供对特定数据库性能的可见性并向开发人员提供自动反馈，团队能够将超过 1,000 个数据库的慢查询数量从超过 200 万个减少到不到 100 万个。“这是一个巨大的成功。”

## SLO：建立明确的期望

团队成员对优化的追求并没有止步于更好的可观测性和查询性能。他们为其数据库服务实施了 SLO，设定了明确的性能目标，并确保数据库满足其所服务的產品团队的需求。

Roset 说：“我们围绕延迟和可用性定义了 SLO。” “例如，我们的目标是在数据库连接尝试中实现 99.99% 的成功率，并为查询执行设定了特定的延迟目标。”

为了跟踪这些目标，团队使用合成监控代理和修补的 [SQL Exporter](https://github.com/justwatchcom/sql_exporter/pull/121) 来测量查询执行时间，从而为其监控系统提供实时反馈。

这种 SLO 驱动的方法帮助团队保持一致的性能，即使在扩展时也是如此。合成监控系统使数据运营工程师能够在问题影响产品团队之前检测到问题，并确保数据库保持高度可用性。

## 持续改进：展望未来

尽管 OVHcloud 的数据库团队在优化其基础设施和减少慢查询方面取得了重大进展，但它仍在继续寻找改进的方法。

目前正在进行的一项计划是开发分层服务模型，根据工作负载的关键程度提供不同级别的数据库性能。对于最关键的系统（称为“振金集群”），团队提供了最高级别的性能和冗余。

随着 OVHcloud 的不断扩展，数据库团队也在探索将其方法扩展到其他类型数据库的方法，包括键值和列式存储，以确保团队的所有服务都能从相同级别的优化中受益。

“我们已经取得了很大进步，但我们从未停止改进，”Roset 说。“我们一直在寻找优化、扩展和为内部团队提供更好服务的新方法。”
