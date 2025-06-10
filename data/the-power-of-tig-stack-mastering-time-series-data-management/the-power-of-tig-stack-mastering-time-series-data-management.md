
<!--
title: TIG Stack的力量：掌握时间序列数据管理
cover: https://cdn.thenewstack.io/media/2025/06/52013265-time.png
summary: 告别传统数据库！用TIG Stack玩转时序数据：Telegraf负责高效采集，InfluxDB 3 Core实现优化存储检索，Grafana酷炫可视化！快速搭建属于你的时序数据管道，玩转IoT、系统指标，释放数据价值！
-->

告别传统数据库！用TIG Stack玩转时序数据：Telegraf负责高效采集，InfluxDB 3 Core实现优化存储检索，Grafana酷炫可视化！快速搭建属于你的时序数据管道，玩转IoT、系统指标，释放数据价值！

> 译自：[The Power of TIG Stack: Mastering Time Series Data Management](https://thenewstack.io/the-power-of-tig-stack-mastering-time-series-data-management/)
> 
> 作者：Anais Dotis-Georgiou

在当今这个数据驱动的世界中，[时间序列](https://www.influxdata.com/what-is-time-series-data/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns)信息不断地从无数来源涌入：[物联网 (IoT) 设备](https://www.influxdata.com/glossary/iot-devices/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns)、系统指标、金融数据流和用户交互。为了有效地利用这些时序数据，您需要专门为此设计的工具。TIG Stack 应运而生：它是由 Telegraf、InfluxDB 和 [Grafana](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/) 这三个强大的开源工具组成，改变了我们收集、存储、分析和可视化基于时间的数据的方式。

**为什么时间序列很重要**

时间序列数据具有独特的特征，传统的数据库很难高效地处理这些特征。它的顺序性、高写入量以及对基于时间的查询的需求，都需要专门构建的解决方案。而这正是 TIG Stack 所提供的。

**入门指南：您的 TIG Stack 设置指南**

本教程将引导您使用以下工具建立自己的时间序列数据管道：

*   [Telegraf](https://docs.influxdata.com/telegraf/v1/install/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns)，用于高效的数据收集。
*   [InfluxDB 3 Core](https://docs.influxdata.com/influxdb3/core/get-started/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns) 或 3 Enterprise，用于优化的存储和检索。
*   [Grafana](https://grafana.com/oss/grafana/)，用于直观的可视化和仪表盘。

TIG Stack 以 InfluxDB 为中心，InfluxDB 是一个专门构建的[时间序列数据库](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/)管理系统，针对高频时序数据的摄取、存储和检索进行了优化。该系统架构支持高基数时间序列的摄取，并具有可配置的降采样和保留机制。

本教程将使用 InfluxDB 3 Core，这是最新版本，它使用 Apache Arrow 和 DataFusion 重新设计了存储层，用于列式数据处理。该实现通过批量预写日志 (WAL) 操作提高了写入性能，通过矢量化处理增强了查询执行，并通过优化的模式编码和压缩技术降低了内存开销。

Telegraf 充当主要的数据收集代理，实现基于插件的架构，用于从各种来源（包括系统资源、网络设备、API 和消息队列）获取指标。

[Grafana 提供了可视化和告警层](https://thenewstack.io/alerting-with-grafana-and-influxdb-cloud-serverless/)，通过原生数据源插件连接到 InfluxDB，这些插件支持 SQL 和 InfluxQL 查询语言。仪表盘框架通过可配置的面板呈现时间序列数据，而告警引擎则根据定义的阈值评估查询结果。

**先决条件**

在开始之前，请确保您已安装以下组件：

*   **Telegraf:** 通用的数据收集代理
*   **InfluxDB 3 Core:** 时间序列数据库基础
*   **Grafana:** 可视化平台 (对于 MacOS 用户：`brew install grafana` 然后执行`brew services start grafana` 将使 Grafana 在[http://localhost:3000](http://localhost:3000) 上可用。)

或者，您可以使用 Grafana Cloud 作为托管解决方案。

**启动 InfluxDB 3 Core**

安装 InfluxDB 3 Core 后，使用以下命令初始化您的服务器：

`influxdb3 serve --host-id=local01 --object-store file --data-dir ~/.influxdb3`

接下来，创建一个身份验证令牌：

`influxdb3 create token`

您将看到类似于以下的输出：

```
1234 |
Token: apiv3_xxx
Hashed Token: zzz
Start the server with `influxdb3 serve --bearer-token zzz`
HTTP requests require the following header: "Authorization: Bearer apiv3_xxx" |
```

纯文本令牌 (apiv3\_xxx) 将与 Telegraf 一起使用，而哈希版本在配置服务器时提供安全性。这种安全模型可防止身份验证令牌直接暴露在您的配置文件或命令历史记录中。

**配置 Telegraf 进行数据收集**

Telegraf 充当您的数据收集代理，[从各种来源收集指标并将它们转发到 InfluxDB](https://thenewstack.io/cleaning-and-interpreting-time-series-metrics-with-influxdb/)。其基于插件的架构使其非常通用。

为了演示，我们将捕获系统 CPU 指标。创建一个配置文件 (`telegraf.conf`)，其中包含以下设置：

```
123456789101112131415161718 |
```
# 全局配置

```toml
[agent]
  interval = "10s" # 采集间隔
  flush_interval = "10s" # 数据刷新间隔
```

# Input Plugin: CPU Metrics

```toml
[[inputs.cpu]]
  percpu = true # 收集每个CPU的指标
  totalcpu = true # 收集总CPU指标
  collect_cpu_time = false # 不收集CPU时间指标
  report_active = true # 报告活跃CPU百分比
```

# Output Plugin: InfluxDB v2

```toml
[[outputs.influxdb_v2]]
  urls = ["http://127.0.0.1:8181"]
  token = "your plain Token apiv3_xxx"
  organization = ""
  bucket = "cpu"
```

**重要提示：** 使用 InfluxDB 3 Core，您无需指定 Organization ID。

使用以下命令启动 Telegraf：

```bash
telegraf --config /path/to/telegraf.conf --debug
```

成功执行将生成显示数据收集和传输的日志条目：

```
2025-01-09T23:34:02Z I! Loading config: ./telegraf.conf
2025-01-09T23:34:02Z I! Starting Telegraf 1.26.2
2025-01-09T23:34:02Z I! Available plugins: 235 inputs, 9 aggregators, 27 processors, 22 parsers, 57 outputs, 2 secret-stores
2025-01-09T23:34:02Z I! Loaded inputs: cpu
2025-01-09T23:34:02Z I! Loaded aggregators:
2025-01-09T23:34:02Z I! Loaded processors:
2025-01-09T23:34:02Z I! Loaded secretstores:
2025-01-09T23:34:02Z I! Loaded outputs: influxdb_v2
2025-01-09T23:34:02Z I! Tags enabled: host=MacBook-Pro-4.local
2025-01-09T23:34:02Z I! [agent] Config: Interval:10s, Quiet:false, Hostname:"MacBook-Pro-4.local", Flush Interval:10s
2025-01-09T23:34:02Z D! [agent] Initializing plugins
2025-01-09T23:34:02Z D! [agent] Connecting outputs
2025-01-09T23:34:02Z D! [agent] Attempting connection to [outputs.influxdb_v2]
2025-01-09T23:34:02Z D! [agent] Successfully connected to outputs.influxdb_v2
2025-01-09T23:34:02Z D! [agent] Starting service inputs
2025-01-09T23:34:12Z D! [outputs.influxdb_v2] Buffer fullness: 0 / 10000 metrics
2025-01-09T23:34:23Z D! [outputs.influxdb_v2] Wrote batch of 13 metrics in 792.507791ms
```

**验证数据收集**

要确认您的指标已正确存储，请直接查询 InfluxDB：

```sql
influxdb3 query --database=cpu "SELECT * FROM cpu LIMIT 10"
```

**使用 Grafana 可视化**

最后一步是设置 [Grafana](https://docs.influxdata.com/influxdb3/core/visualize-data/grafana/?utm_source=vendor&utm_medium=referral&utm_campaign=2025-05_spnsr-ctn_tig-stack_tns)，将您的原始数据转换为有意义的可视化：

- 访问 Grafana：
[http://localhost:3000](http://localhost:3000) - 导航至 Connections > Data sources > Add new data source
- 搜索并选择“InfluxDB”
- 配置您的连接：
  - 选择 SQL 作为语言类型
  - URL:
[http://localhost:8181](http://localhost:8181)
  - Database: cpu
  - 启用“Insecure Connection”
- 点击“Save & test”以验证连接

现在您可以创建可视化了！导航至 Dashboards > Create Dashboard > Add Visualization，选择您的 InfluxDB 数据源，并使用可视化查询构建器或直接编写 SQL。

示例查询：

```sql
SELECT "cpu", "usage_user", "time" FROM "cpu" WHERE "time" >= $__timeFrom AND "time" <= $__timeTo AND "cpu" = 'cpu0'
```

**后续步骤**

通过 TIG Stack 的运行，您现在拥有一个强大的平台，用于时间序列数据的收集、存储和可视化。一些潜在的应用包括：

- 基础设施或产品监控
- IoT 传感器数据分析
- 应用程序性能跟踪
- 预测分析

Telegraf 输入插件的灵活性、InfluxDB 3 Core 的性能以及 Grafana 的可视化功能为时间序列数据应用提供了无限的可能性。

立即开始探索您的数据！

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)