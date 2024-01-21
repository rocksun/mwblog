<!--
title: 解码PostgreSQL监控
cover: ./cover.png
-->

对 PostgreSQL 的性能问题进行监控至关重要。PostgreSQL 是一个强大的开源关系数据库系统，以其健壮性、可扩展性和对可扩展性和标准符合性的强调而脱颖而出。在本 PostgreSQL 监控指南中，我们将介绍应监控的关键 PostgreSQL 指标、PostgreSQL 监控的最佳实践以及一些可以设置 PostgreSQL 监控的工具。

> 译自 [Decoding PostgreSQL Monitoring | 101 Guide](https://signoz.io/blog/postgresql-monitoring)。作者 Deepam Kapur 。

## 什么是 PostgreSQL？

PostgreSQL 是一个开源的关系数据库管理系统。PostgreSQL 项目起源于 1986 年的加州大学。它最初被命名为 Postgres，并最终在 1996 年更名为 PostgreSQL，以突出其对 SQL 查询语言的支持。

PostgreSQL 由于其存储和扩展复杂数据工作负载的能力而被广泛采用。从技术上讲，它是一个对象关系数据库，允许创建自定义数据类型并支持高级功能，如继承和多态性。

它支持完全 ACID compliant 的事务，并实现了一个称为多版本并发控制的独特功能。这使得多个事务可以同时运行，而不会造成交通拥堵或需要锁定。

它还提供了各种扩展，如用于地理空间数据的 PostGIS(用于 Uber 等应用程序)，用于数据分片和分发的 Citus，以及用于 AI 应用程序的 PG 嵌入。

监控 PostgreSQL 数据库很重要，以确保数据库能够有效地完成其工作。

## PostgreSQL 监控的关键指标

监控 PostgreSQL 可以跟踪查询性能、资源利用率、可用性等。让我们看一下应该监控的 PostgreSQL 的重要指标。

### 查询吞吐量和延迟指标

如果您的查询执行时间比应该的时间长，那么您使用什么类型的机器或数据库都无关紧要。因此，如果随着表或数据库的大小，查询延迟指数增长，则始终跟踪查询延迟。

考虑图书馆的类比: 每个查询都是一个信息请求。为了理解这种互动的步伐，让我们使用以下 SQL 查询计算平均延迟:

```sql
SELECT query, mean_exec_time
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 5
```

此查询根据平均执行时间获取前 5 个查询，提供潜在瓶颈的见解。您还可以根据要求从 `pg_stat_statements` 表中查看其他指标，如调用次数或最小和最大执行次数。

分析这些数据有助于识别可能导致性能问题的查询，从而进行有针对性的优化工作。

### 磁盘利用率和 I/O 操作

PostgreSQL 负责管理数据在磁盘上的存储方式以及在需要时如何检索数据。这个过程通常对终端用户不可见，但对数据库性能至关重要。

磁盘利用率和 I/O 操作是 PostgreSQL 性能的关键方面。磁盘利用率是指数据库使用的磁盘空间量。I/O 操作涉及读取或写入磁盘存储。两者都很重要，因为它们可能显着影响数据库的速度和效率。高磁盘利用率或低效的 I/O 操作会拖慢数据库。

您可以使用下面的查询定期监控 PostgreSQL 数据库中不同对象使用的磁盘空间量:

```sql
SELECT object_type, object_name, schema_name, size FROM
(SELECT
    'Table' AS object_type,
    relname AS object_name,
    schemaname AS schema_name,
    pg_total_relation_size(relid) as size_bytes,
    pg_size_pretty(pg_total_relation_size(relid)) AS size
FROM
    pg_catalog.pg_statio_user_tables
UNION
SELECT
    'Index' AS object_type,
    indexrelname AS object_name,
    schemaname AS schema_name,
    pg_total_relation_size(indexrelid) as size_bytes,
    pg_size_pretty(pg_total_relation_size(indexrelid)) AS size
FROM
    pg_catalog.pg_stat_all_indexes
) as data
ORDER BY
    size_bytes DESC
```

该查询使用名为 pg_size_pretty 的函数计算每个表和索引的大小(以字节(size_bytes)和人类可读格式(size)表示)。

查询中正在发生的事情:

- 查询的第一部分选择数据库中的所有用户表(`pg_statio_user_tables`)，获取它们的名称、模式和大小。
- 第二部分对所有索引(`pg_stat_all_indexes`)执行相同的操作。
- 然后这些结果被组合并按字节大小(`size_bytes`)排序，最大的对象首先出现。

下面是您可以用上述查询获得的示例输出。

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-table.webp)

*该查询列出了 PostgreSQL 数据库中的表和索引，显示了它们的类型、名称、模式名称和大小*

如果您正在使用 PostgreSQL 并希望检查是否有任何可能影响数据库性能的额外索引，则可以使用一个简单的查询。这将向您显示数据库中所有索引的列表:

```sql
SELECT * FROM pg_catalog.pg_stat_all_indexes
```

您将获得类似下面的输出:

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-index.webp)

*检查 PostgreSQL 数据库中的所有索引*

`idx_scan` 列告诉您每个索引被使用的次数。如果数字很高，则索引可能有助于查询更快地运行。但是如果数字很低或者为零，则该索引可能不是非常有用，甚至可能会拖慢数据库。通过识别这些索引，您可以决定是保留它们还是删除它们以提高数据库的效率。

### 连接健康状况和池化

连接健康和池化是优化 PostgreSQL 环境的关键组成部分。想象一个繁忙的鸡尾酒会。健康的连接就像顺畅的谈话。让我们 visualize 这个概念:

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-pooling.webp)

*PostgreSQL 中的连接池*

您可以直接在应用程序代码中实现连接池。在单体应用程序的情况下，您可以创建一个可以跨整个应用程序使用的共享连接池。

您可以通过使用第三方工具(如 PgBouncer)有效地管理连接池，而无需将其集成到应用程序代码中。PgBouncer 是一个 PostgreSQL 连接池工具。您可以配置 PgBouncer 来平衡连接负载并提高 PostgreSQL 数据库性能。

任何目标应用程序都可以连接到它，就像它是一个 PostgreSQL 服务器一样，PgBouncer 将创建一个连接到实际服务器的连接，或者它将重用其现有连接之一。

您可以利用 PgBouncer 管理控制台来监控许多重要指标。一旦连接，您就可以使用 SHOW STATS 命令提供各种指标，这些指标有助于监控和了解连接池的性能和行为。

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-stats.webp)

*PgBouncer 的 Show Stats 输出*

您可以通过 `SHOW STATS` 命令访问的一些关键 PostgreSQL 指标如下:

1. **总请求数(total_xact_count)**: 已处理的 SQL 事务(或会话)总数。
2. **总查询数(total_query_count)**: 已执行的 SQL 查询总数。
3. **已接收数据(total_received)**: 从客户端接收的数据总量，通常以字节为单位。
4. **已发送数据(total_sent)**: 发送给客户端的数据总量，也通常以字节为单位。
5. **总查询时间(total_query_time)**: 执行查询所花费的总时间。这通常以微秒为单位，并提供了数据库负载和查询效率的概况。
6. **平均事务持续时间(avg_xact_time)**: 事务的平均持续时间。这有助于了解数据库处理事务的性能。
7. **平均查询持续时间(avg_query)**: 与平均事务持续时间类似，此指标显示执行查询的平均所需时间。
8. **总事务数(total_xact_count)**: 已处理的事务总数。
9. **总查询数(total_query_count)**: 执行的查询总数。
10. **活动服务器连接数(active_server_conns)**: 到 PostgreSQL 服务器的活动连接数。
11. **最大服务器连接数(max_server_conns)**: 到 PostgreSQL 服务器的最大连接数。

在这些和 PgBouncer 的相关命令中，总计数字自 `process start` 后开始计数。平均值每 `stats_period` 个你在配置中配置的被更新一次。

### 了解锁和死锁

在 PostgreSQL 中，锁和死锁在维护数据完整性方面发挥着关键作用。锁是一种机制，可防止多个事务同时访问相同的资源以避免冲突并确保一致性。当两个或多个事务被阻塞时，每个事务都在等待其他事务释放锁，从而导致停滞，这就是死锁。可视化这个场景:

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-deadlock.webp)

*PostgreSQL 中的锁和死锁*

为了监控 PostgreSQL 的锁和死锁，您可以使用内置以及第三方工具。

- `pg_locks`: 这是一个 PostgreSQL 系统视图，提供有关数据库中所有当前锁的信息。它显示诸如锁的类型、持有锁的进程的进程 ID(PID)以及正在锁定的特定数据库资源(如表、行等)的详细信息。
- `pg_stat_activity`: 此视图通过提供每个进程的额外上下文(如其所连接的数据库)来补充 `pg_locks`。使用 PID 通过 `pg_locks` 连接 `pg_stat_activity` 允许您看到不仅锁，还有哪个数据库和查询涉及其中。

提供的 SQL 查询将 `pg_locks` 与 `pg_stat_activity` 连接在一起，以显示当前锁的全面视图:

```sql
SELECT
    pg_locks.pid,
    pg_stat_activity.datname,
    pg_locks.mode,
    pg_locks.relation,
    pg_locks.page,
    pg_locks.tuple
FROM
    pg_locks
JOIN
    pg_stat_activity ON pg_locks.pid = pg_stat_activity.pid
```

这里是一个示例输出可能的样子:

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-sample-output.webp)

*pg_locks 和 pg_stat_activity 查询的示例输出*

监控锁和死锁涉及定期针对 `pg_locks` 和 `pg_stat_activity` 运行查询以识别任何潜在问题。通过关注这些视图，您可以主动解决锁定方案并采取纠正措施以确保数据库平稳运行。

这些查询可以作为定期监控任务的一部分进行调度，以及时检测和解决 PostgreSQL 数据库中的任何与锁相关的问题。

您也可以使用手动工具，如 PGAdmin 来管理正在发生的事情，但在生产环境中，手动工具可能不起作用。您可以使用 [SigNoz](https://signoz.io/) 等工具进行监控，这可以帮助您可视化和监控 PostgreSQL 指标。您还可以在重要指标上设置警报。

现在您对需要监控的关键 PostgreSQL 指标有了一些了解，让我们介绍一下 PostgreSQL 监控的最佳实践。

## PostgreSQL 监控最佳实践

### 建立 PostgreSQL 性能基线

建立性能基线对于了解 PostgreSQL 数据库在典型操作条件下的正常行为至关重要。

这个过程涉及:

- **确定关键性能指标**: 关注查询执行时间、事务率和资源利用率(CPU、内存、磁盘 I/O)等重要指标。这些指标可以了解数据库在常规操作期间的性能。
- **收集和分析历史数据**: 收集足够长时间段的数据以建立准确的基线非常重要。这种历史分析可帮助您识别正常的操作模式和自然波动。为了收集历史数据，您需要类似 SigNoz 这样的工具来随时间存储数据并通过图表和控制面板访问它。
- **使用 `pg_stat_statements` 和 `pg_stat_activity`**: 这些工具对于捕获详细的性能指标至关重要。它们有助于了解典型的工作负载模式并发现任何偏离正常的情况。
- **记录基线值**: 详细记录关键指标的基线值。此文档可作为识别偏差和异常行为的参考点。确保定期更新此文档以反映数据库环境或工作负载中的任何更改。

### 为 PostgreSQL 监控定义阈值

为及时识别 PostgreSQL 监控中的异常条件和潜在问题，定义精确的性能阈值至关重要。这涉及:

- **确定关键指标**: 确定反映数据库正常操作状态的关键指标，如 CPU 使用率、内存消耗和磁盘 I/O。理解这些指标对设置有意义的阈值至关重要。
- **根据基线设置阈值**: 通过参考已建立的性能基线，为每个关键指标建立阈值。这些阈值表示超出可能需要采取行动的可接受性能范围。
- **结合动态阈值**: 考虑实现可以根据不同条件(如时间、预期的工作负载波动或特定操作事件)调整的动态阈值。这种方法使阈值能够更具上下文相关性，并减少误报。
- **定期审查和更新:** 定期审查和调整这些阈值，以与数据库工作负载、系统升级或不断变化的业务需求保持一致。这可确保监控系统保持对数据库当前状态的有效响应。
- **与警报机制集成**: 将这些阈值与警报系统链接，以便在阈值被违反时通知相关团队。这使得及时调查和干预成为可能，最大限度地减少了对数据库性能和可用性的潜在影响。
- **平衡敏感度和实用性**: 设置敏感程度足以检测实际问题但不太紧密的阈值，从而不会生成过多的误报。找到这种平衡对有效的监控至关重要。

### 设置警报和通知

实现一个稳健的警报机制是有效的 PostgreSQL 监控的一个关键组成部分。这确保当性能指标超过定义的阈值时管理员能够及时收到通知。为了优化这个过程:

- **选择警报工具**: 选择与PostgreSQL环境集成良好的最合适的警报工具或框架。流行的选择包括SigNoz、Prometheus、Nagios或PostgreSQL内置的警报功能。选择应基于兼容性、可扩展性和易于集成等因素。
- **定义警报规则:** 创建基于每个关键指标建立阈值的警报规则。这些规则应精确到最小化误报，同时确保没有重大问题被忽略。
- **配置通知渠道**: 设置各种通知渠道以适应不同的偏好和紧急程度。这可能包括电子邮件、Slack消息、短信或与事件管理系统的集成。确保这些渠道可靠并经常测试。
- **实施升级计划**: 制定升级计划，根据问题的严重性定义警报如何路由到相关人员。这可能涉及根据时间或警报性质通知不同的团队成员或角色。
- **测试警报机制**: 定期测试警报系统以确保它按预期工作。这包括测试警报触发器、通知传递和响应时间。
- **记录警报协议**: 保留警报流程的清晰文档，包括警报规则的配置、阈值设置背后的理由和升级程序。此文档对新团队成员的入职培训以及事件响应期间的参考至关重要。
- **平衡警报敏感度**: 努力在警报敏感度之间找到平衡。过于敏感的警报可能导致警报疲劳，而敏感度过低可能会错过关键问题。定期审查和调整警报阈值和规则可以帮助维持这种平衡。

### 定期审计性能优化

定期审计对于维护和增强 PostgreSQL 数据库的运行状况和效率至关重要。这个过程涉及:

- **计划性能审查**: 进行计划的性能审查和审计，以评估数据库的整体健康状况。这包括检查查询性能和系统资源利用率。
- **分析和优化查询**:
  - 利用 `pg_stat_statements` 等工具来识别和分析缓慢的查询。
  - 通过索引改进、重写 SQL 语句或调整数据库配置等方法来优化查询。
- **审查 PostgreSQL 配置**:
  - 持续审查和调整 PostgreSQL 配置，以适应不断发展的工作负载和性能需求。
  - 确保数据库设置经过调优，适合当前的运营要求。
- **评估资源分配**:
  - 定期评估 CPU、内存和磁盘空间等资源的分配情况。
  - 确保数据库拥有必要的资源来有效处理当前和预期的工作负载。
- **记录审计结果**:
  - 详细记录审计结果，包括性能改进和所做的任何更改。
  - 这些文档可作为未来调优和审计的有价值参考。

## PostgreSQL 监控最佳工具

现在您已经了解了 PostgreSQL 的关键指标监控以及 PostgreSQL 监控的最佳实践，让我们看一下 PostgreSQL 监控的最佳工具。

以下是监控 PostgreSQL 数据库的最佳工具列表。

### SigNoz

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-signoz.webp)

*在 SigNoz 中构建 PostgreSQL 监控的自定义控制面板*

SigNoz 是一个开源监控工具，通过 OpenTelemetry 在 PostgreSQL 指标监控方面表现出色。它使用 OpenTelemetry Collector 收集 PostgreSQL 指标，并有效地可视化这些数据。SigNoz 允许用户监控关键数据库指标，全面分析数据库性能。其建立自定义控制面板和警报的能力使其特别适合用于跟踪和管理 PostgreSQL 实例的运行状况和效率。

有关 SigNoz 如何执行 PostgreSQL 监控的更详细探讨，您可以访问他们的指南: [使用 OpenTelemetry 监控 PostgreSQL 指标](https://signoz.io/blog/opentelemetry-postgresql-metrics-monitoring/)。

### pgAnalyze

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-pgAnalyze.webp)

*pgAnalyze 中的 PostgreSQL 监控(来源:pgAnalyze 网站)*

Pganalyze 是一个专为 PostgreSQL 数据库设计的全面监控工具。它深入洞察 PostgreSQL 实例的性能，帮助数据库管理员和开发人员有效地优化和维护数据库系统。

该工具提供性能监控、查询分析、日志洞察等功能。

### pgDash

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-pgDash.webp)

*pgDash 中的 PostgreSQL 监控(来源:pgDash 网站)*

pgDash 是一个全面诊断和监控 PostgreSQL 的解决方案。它提供了核心报告和可视化功能，呈现有关 PostgreSQL 性能的深入数据。

关键功能包括广泛的 SQL 查询信息、时间序列图表和执行计划，扫描潜在问题的诊断以及复制指标的监控。PgDash 还提供有关表、索引、锁和后端的信息，以及团队共享功能。

它支持与 AWS CloudWatch 和 PgBouncer 等系统的集成，并提供警报选项。PgDash 以 SaaS 和自托管格式提供，与 AWS RDS 和 Aurora 兼容。

### Prometheus

Prometheus 是一个开源监控解决方案，它提供了一个多维数据模型，其中时间序列数据由指标名称和键值对标识。它具有强大的查询语言(PromQL)用于详细的数据分析，并支持高效的数据存储，包括内存和本地磁盘。

Prometheus 提供灵活的可视化选项，包括与 Grafana 的集成，并且设计了可靠的操作，每个服务器独立运行。它还基于 PromQL 提供精确的警报，以及用于处理通知的警报管理器。此外，Prometheus 高度可扩展，具有许多客户端库和第三方数据的集成。

### New Relic

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-new-relic.webp)

*New Relic 中的 PostgreSQL 监控(来源: New Relic 网站)*

New Relic 是一个通用的性能监控工具，为监控 PostgreSQL 数据库提供了强大的功能。它提供了数据库性能的详细信息，包括查询分析、吞吐量和响应时间。

使用 New Relic，用户可以跟踪和可视化关键指标，如事务量、错误率和服务响应时间。其警报系统在性能异常或系统问题时通知用户。此外，New Relic 支持与云和内部部署的 PostgreSQL 实例集成，提供数据库运行状况和性能的全面实时视图。

### Datadog

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-datadog.webp)

*Datadog 中的 PostgreSQL 监控(来源:Datadog 网站)*

Datadog 是一个强大的监控工具，为 PostgreSQL 数据库提供了全面的见解。它自动从 PostgreSQL 的统计信息收集器收集数据，使关键指标在自定义控制面板中可见。

Datadog 的集成有助于查询级性能洞察，以优化缓慢的查询。它还支持在应用程序中跟踪 PostgreSQL 查询，以帮助识别瓶颈。这种通用性使 Datadog 既适用于高层次的 PostgreSQL 数据库监控，也适用于详细的性能分析。

### Grafana

![](https://signoz.io/img/blog/2024/01/postgresql-monitoring-grafana.webp)

*Grafana 中的 PostgreSQL 监控(来源:Grafana 网站)*

Grafana 是一个强大的可视化和分析软件，可与 PostgreSQL 无缝集成以进行监控和数据分析。它使用户能够创建交互式实时控制面板来可视化 PostgreSQL 指标和日志。

Grafana 的通用性在于它支持各种数据源，包括 PostgreSQL，这使其可以进行全面的数据库监控。用户可以自定义控制面板以跟踪特定的 PostgreSQL 指标，设置警报并分析长期趋势。这使 Grafana 成为数据库管理员和需要密切关注数据库性能和运行状态的团队的必备工具。

## 总结

在这篇文章中，我们涵盖了有效的 PostgreSQL 监控的所有方面。我们介绍了一些 PostgreSQL 监控的关键指标，介绍了在设置 PostgreSQL 监控时应遵循的最佳实践，然后介绍了您可以用于 PostgreSQL 监控的顶级工具。

一个允许您存储、查询和可视化 PostgreSQL 监控指标的监控工具可以帮助您快速调试性能问题。对于基于分布式架构的现代应用程序，将 PostgreSQL 指标与应用程序基础架构的其余部分相关联非常重要。

SigNoz 是一个全栈开源可观测性工具，可帮助您监控 PostgreSQL 实例，同时为应用程序的其余部分提供监控。它在一个面板中提供指标、日志和跟踪。在使用 SigNoz 进行 PostgreSQL 监控时，您可以将重要指标与跟踪和日志相关联，这可以帮助您快速调试潜在问题。

SigNoz 云是运行 SigNoz 的最简单方式。您可以[在此](https://signoz.io/teams/)注册一个免费帐户，并获得 30 天免费无上限使用。

您也可以自行安装和自托管 SigNoz。查看[文档](https://signoz.io/docs/install/)了解如何安装自托管的 SigNoz。
