<!--
title: Prometheus和Grafana监控Kubernetes以及未来
cover: ./cover.png
-->

了解使用 Prometheus 和 Grafana 监控 Kubernetes 的优势和挑战，以及他们的潜在继任者。

> 这篇文章已经一年多了，许多情况发生了变化，例如 OpenTelemetry 的发展改变了许多，但是如果还是看 Prometheus 相关的方案，还是可以参考。译自 [Prometheus vs Grafana and Kubernetes， Oh My！ ](https://www.groundcover.com/blog/prometheus-grafana-kubernetes)。作者 Yechezkel Rabinovich 是 groundcover 的 CTO 和创始人。

## 这三者能否经受住时间(或技术创新)的考验？

也许你就是那个将可观测性引入组织的人。您负责设计组织的第一个 Kubernetes 应用程序，并需要一种方法来确定开发、测试和生产集群是否一切正常。您搜索 Reddit、Stack Overflow、Twitter 和所有其他常用的产品信息来源，然后找到了 Prometheus。安装和配置非常快速和简单，很快您就得到了所需要的：简单的 dashboard 和警报，可以在系统需要关注时警告您。完美。

不久，Kubernetes 在您的组织中迅速发展。突然之间，您有 50 个生产集群，每个集群都在生成关于 Kubernetes 和集群内运行的服务的指标。由于其他系统管理员看到了它的价值(免费也有帮助)，Prometheus 的使用量爆炸式增长。所有这些新的 Prometheus 服务器很难管理，但它提供的价值超过了努力，所以您和团队继续前进。

然后业务应用程序也开始向该系统发送指标......您开始担心。

Prometheus 需要越来越多的磁盘空间来接收和存储所有这些数据。服务器经常因 OOM 错误而崩溃，重新启动会导致您丢失重要数据。关键的 dashboard 开始需要越来越长的时间来返回结果。您恳求获取更多内存，并竭力削减非关键指标，以抵御指标海啸。

最后，到了考虑 Prometheus 之后会发生什么的时候了。

## Prometheus 是什么？

公平地说，我们要说的是：Prometheus 系统是一个惊人的指标和监控解决方案。

最初由 SoundCloud 于 2012 年开始构建，Prometheus 已被许多组织采用，并享受强大活跃的开发者社区的支持。当它在 2016 年成为云原生计算基金会托管的第二个项目时，其成功更加凸显。随着从 [Redis](https://www.groundcover.com/blog/redis-cluster-kubernetes) 和 MongoDB 到 Minecraft 和比特币等系统的[大量指标 exporter 库](https://prometheus.io/docs/instrumenting/exporters/)的可用性，Prometheus 和 [Grafana](https://www.groundcover.com/blog/grafana-kubernetes) 成为许多基础设施团队的关键组件。

作为理解其优势和缺点的关键，首先理解 Prometheus 提供的功能非常重要。从本质上讲，有四个关键功能：

- 一个**时间序列数据库**，具有方便识别、查询和分组指标的键值数据模型;
- 一个强大且高度灵活的**查询语言** PromQL;
- 一个拉模式的“**scraper**”，用于检索和存储指标;
- 一个用于自定义通知的**警报器**组件;

该系统的架构很简单、直接:

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a5341fb58f0ea05eee_LGXtXjiQd_38rFSshFioTzL4JBXZL2ZTWHCspWLPsWnjfpg3h9E6WrHxZz10t29T6mumzdQKn14c8t1YVjooJh6AMEG0omwhliuLo2jisYdYt7dTptfR3-vV8BRU-Ja7PSfP-DyWhvG2nTH1MAH9ttVPgH2aIF9-otF9uFLOimwUaFN4VLyGWOiY_XlnzH1oWnA.png)

(来源: https://prometheus.io/docs/introduction/overview/)

Prometheus **服务器**负责从组织计算环境中的基础设施和应用程序中“scraping”指标，将其存储为具有毫秒级时间戳的时间序列数据，并使用称为标签的灵活标记来方便查询。**Alertmanager** 根据您指定的规则提出警报，**Grafana** dashboard 提供可视化功能，以更轻松地理解和监控当前环境状态。 对于无法刮擦指标的情况，**Pushgateway** 允许您将这些指标“推送”到 Prometheus 系统中。

指标可以通过驻留在要监控的系统中(或附近)的 **exporter** 通过 HTTP 发现端点或自定义应用程序代码公开给 Prometheus。Prometheus 社区已经创建了大量[现成的 exporter](https://prometheus.io/docs/instrumenting/exporters/) ，并且为许多语言提供了客户端库，以便在需要时编写自己的 exporter。

那么有什么不好的呢？ 在我们深入研究之前，让我们更 closely 看看许多实现的另一个关键部分：Grafana。

## Grafana 是什么？

Grafana 是一种非常流行的开源时间序列数据可视化工具。 Grafana Labs 是 Grafana 的制造商，在广泛的企业中拥有 2，000 多家客户，截至 2022 年 7 月，Grafana 产品本身在全球范围内拥有 90 多万 active 安装。

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a686678e1080d0f592_RcaRWtKXHLtoxzH1TyVFEV-TrfIBpQG3r2yVwTF8ggxwA-JjXNArSxUkpptgjo0MNX1fRjh7uq0YR16m5fOHPspGNfAj7LmuB67RZA281hBP50sxmN1Jn1NLz2qC_hTipGzaBGKKqfeLsON50lPFAW9F-oNqURrgZWqmFxCC1nKH_YVuPYKZL_x30akf_Fc564k.png)

(来源: https://prometheus.io)

有大量可用的[可视化类型](https://grafana.com/docs/grafana/latest/visualizations/)，包括您所有喜欢的：条形图、直方图、热图、K线图、饼图、地图等等。系统自己的基于插件的可扩展性为您提供了许多额外的面板，可以将其融合到您自己的 Grafana dashboard 中。

将 Grafana 连接到 Prometheus 很简单：使用 Grafana 的“配置”菜单创建一个新的 [Prometheus 数据源](https://grafana.com/docs/grafana/latest/datasources/prometheus/)，指向 Prometheus 实例的网络端点，然后点击“保存并测试”。 一旦数据源可用，您就可以通过指定引用新创建的 Prometheus 数据源中的指标的查询表达式来创建图形和其他可视化。 如果您愿意，您甚至可以使用 [Grafana 的共享 dashboard](https://grafana.com/grafana/dashboards/) 来启动您的工作。

## 使用 Prometheus 和 Grafana 监控 Kubernetes

使用 Prometheus 和 Grafana 来[监控 Kubernetes](https://www.groundcover.com/kubernetes-monitoring) 相当常见，主要有以下几个原因:

- 它是完全免费的！ 其他 Kubernetes 监控解决方案可能有免费层，但大多数会根据数据量、主机数量、用户座位数或其他机制收费。
- 不仅有一个活跃的社区可以提供信息和支持，而且还提供了各种资源，包括 exporter、示例 dashboard 和许多其他资源。这简化了快速建立基本的 Prometheus 和 Grafana 平台。
- 自定义很容易(甚至通过服务发现自动完成更好)

Prometheus 本身可以作为容器化应用程序进行安装，Helm chart 是部署到 Kubernetes 集群的常用机制。kube-prometheus-stack [chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) 安装了 Prometheus、Grafana 和各种其他组件，以便您管理 Prometheus 系统。也提供了独立的 Helm chart 来简化单独的 Prometheus 和 Grafana 安装。

(Prometheus 也在开发 [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator)，这是一种本地部署和管理机制。在撰写本文时，Prometheus Operator 处于 beta 状态。Prometheus Operator 与 Helm chart 和 [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) 的比较包含在 Github 存储库的 README 文件中。)

一旦安装了 Prometheus 和 Grafana，就可以通过 [cAdvisor](https://github.com/google/cadvisor)、kubelet 和 [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) 获取 Kubernetes 指标。[这篇](https://grafana.com/grafana/dashboards/315-kubernetes-cluster-monitoring-via-prometheus/)来自 Grafana 的文章很好地概述了该过程、所需的 Prometheus 配置以及一些示例 dashboard。

## Prometheus 和 Grafana:挑战

尽管 Prometheus 非常有吸引力，但随着可观测性环境的规模不断增大，它存在一些严重的缺陷。

### 单服务器架构

Prometheus 在本质上是一个单服务器系统。随着 Kubernetes 集群数量的增加以及收集的指标数量的增加，Prometheus 服务器上的负载也在增加。在某些时候，您的需求可能会超出单个服务器的能力;然而，Prometheus 的体系结构并不是为横向可扩展而设计的，所以扩展监控意味着更大的 Prometheus 和 Grafana 服务器占用空间。

### 内存利用率和“基数”问题

收集大量数据需要系统内存。Prometheus 在将指标导入数据库方面做得很好，但有两个因素会严重影响 Prometheus 进行此操作所需的内存量:指标的数量和用于标识每个指标的标签的设计。Stack Overflow 和其他地方的讨论对此问题进行了详细描述。如果服务器需要执行大量 PromQL 查询，内存约束可能会加剧。

### 长期数据存储

基准和运营经验表明，在存储时间序列指标时，Prometheus 可以消耗大量磁盘空间。几篇博客文章和社交媒体线程专门讨论此问题(后面会有更多内容)，以及 [VictoriaMetrics](https://victoriametrics.com/)、[Mimir](https://grafana.com/oss/mimir/)、[Promscale](https://www.timescale.com/promscale) 和 [Thanos](https://thanos.io/) 等项目正在努力解决此问题。

### 缺乏“混合可观测性”

由于 Prometheus 和 Grafana 主要是为时间序列数据设计的，因此对于数值指标，它们都工作得很好。集成非数值数据(例如日志和跨度数据通常需要用于故障排除)以及无法轻松关联应用程序或基础架构行为不规则期间的数据，会使诊断更加困难。也就是说，Grafana 和 Prometheus 肯定走在了正确的方向上，并通过 exemplars 和 Grafana 日志数据库 Loki 的引入等功能进入了这种地形。

## 谁将成为 Prometheus 的接班人？

鉴于上述优势和挑战，您是否应该为 Prometheus 的继任者做好准备？有几个您可能想要考虑的新产品。

### Grafana Mimir

[Grafana Mimir](https://grafana.com/oss/mimir/) 是一个开源产品，其使命是成为“...最可扩展、性能最好的开源时间序列数据库 for metrics”。使用 Mimir，您可以继续允许现有的 Prometheus 实例从基础设施和应用程序中抓取指标；但是，与写入 Prometheus 数据库不同，您可以将指标转发到 Mimir。Mimir 的关键优势包括支持 PromQL 查询和 Prometheus 告警、横向扩展和自动集群以及显着改进的长期存储功能。

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a6230d2c35f1816935_r3G1LrXBVjKIXqWXKJgO9mwaVMjK6xe8Fqv6-ZZLhj52is0vJrhzD_pXin_IZ9sR10sbawkzH1D9z_yGRCdt0_1QYf65o5-wnu6ZsYWD7xgEV5NPb-lSQ8RpCHu7fITx_Y4WGH_IUdQdB9uy8To7t3Nkh9luaqODuAVGZeQ9Zzuh5OA2_KXQzD6YlOXSEGo2mWA.png)

(来源:https://grafana.com/oss/mimir/)

Grafana Labs 最近在他们的博客上分享了一些关于 Mimir 可扩展性的有趣信息:

- 我们如何将新的 Prometheus TSDB Grafana Mimir 扩展到 10 亿 active series
- 使用 Grafana Enterprise Metrics 在客户基础设施上将 Grafana Mimir 扩展到 5 亿 active series

## VictoriaMetrics

与 Grafana Mimir 一样，[VictoriaMetrics](https://victoriametrics.com/products/open-source/) 是一个开源解决方案，同时提供自管理版和托管版，它解决了许多相同的挑战。[VictoriaMetrics 的功能列表](https://victoriametrics.com/plans-features/)充满了优点：为了可扩展性进行集群/分片/复制，拉模式与 Prometheus 兼容以简化迁移，并额外支持其他协议(如 InfluxDB 或 OpenTSDB)，以及一个强大的，受 PromQL 启发的查询语言(VictoriaMetrics 在其 VictoriaMetrics Enterprise 版本中也支持 Graphite 查询语言)。

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a86e474e85e920ef1a_MxJ_a5vXTASTgsfpu3_ZvPqJta__G7UBMkjfRf_d4OcjYmiMNc-4qYl8lkrNOguvKTmZtP3GByy-JzhpdX3iM4PcpGoClqfkkL2IWw9L6W859kgGXhAQcyNLB6IsPagaNTIrFjOme6PmL3EQLR7JxLPAw3ZQZFM-H-0JJDMwMV5iO_lUPRsP_u8A_vlU7gPj-rE.png)

(来源:https://victoriametrics.com/products/open-source/)

在 2020 年由 VictoriaMetrics 创始人之一 [Aliaksandr Valialkin](https://twitter.com/valyala) 执行的使用 Prometheus [node_exporter 目标的基准测试](https://valyala.medium.com/prometheus-vs-victoriametrics-benchmark-on-node-exporter-metrics-4ca29c75590f)中，运行在 Google Cloud 上的 VictoriaMetrics 能够使用明显更少的磁盘空间存储指标数据，磁盘峰值也更少、更轻。

即使我们忽略这个项目几乎是由一个人构建和维护的事实，VictoriaMetrics 也不失为一个惊人的工程解决方案。它持续击败时间序列数据库领域的每个基准，并使自己成为未来几年广泛使用的替代方案。就在最近，VictoriaMetrics 在这个[基准测试](https://victoriametrics.com/blog/mimir-benchmark/)中与 Grafana Mimir 进行了比较，这表明了这个技术的伟大程度。

### Promscale

[Promscale](https://www.timescale.com/promscale) 为指标世界带来了一种有趣的方法。除了 Prometheus 远程写入功能和完整的 PromQL 支持之外，Promscale 通过 TimescaleDB 和构建在 PostgreSQL 之上的 Promscale 扩展来实现长期指标存储。这使用户能够利用标准 SQL 来分析系统的行为，包括指标和跟踪数据的相关性。通过 SQL、PromQL 或 Jaeger 的 Grafana 集成让 Prometheus 用户可以继续利用熟悉的可视化功能。

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a68a5b067329bf5b61_vQ1B2u6StzeK8oUbK70CqwxkJJxrEYHxIThSZ0jTcEVAtCJ18JAziK54IsCprhRUCGRyF83-ttBkPHFCH4X2vBfcbQhxYCxjau3pdSFLO_IMppCc7WKUIEJRbk7m6vTBI44txDGpkLs19K7DGSHfdgAhxuXvfKdYfNUVuteScjwXI7Da_JzrhE9y-uOo8RZZZCg.png)

(来源:https://github.com/timescale/promscale)

在 2020 年的一篇博文中，Timescale(Promscale 和 TimescaleDB 的制造商)指出，Promscale 提供了“...横向可扩展到每秒 1000 万指标和 PB 级存储”，以及高基数指标的解决方案和许多其他功能。

## 谁会获得王冠？

浏览社交媒体讨论和关于这个话题的博客文章，以了解维护者和大客户对这个问题的看法很有意思。一些人[看到 Prometheus-Mimir 混合未来的潜力](https://www.reddit.com/r/PrometheusMonitoring/comments/twqbme/will_grafana_mimir_replace_prometheus/):

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a6984ed310798be966_TgfyMhnCaOgeTtNE03csIGhjkTtNTZz-GnaN5dRJMCZg6G8pvZs8gYGnoF69vJIaNkBg9OsVlZgn8QGXZGQooKPZCa5f63-RuYrJg142Rm9caGggOOFJdFwKUFGosYVaV4Fp3whHnLZVedm44OgzIvNYm9yYbBGgYz0GyDkvhVv13IKFik3O9Zb0rOfpU0E-fTQ.png)

其他帖子强化了混合未来的想法，[长期存储需求将由 Thanos 和其他解决方案满足](https://www.reddit.com/r/devops/comments/uhmk77/those_of_you_using_prometheus_as_part_of_your/):

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a786678e746dd0f5a5_BN2c-tMldCW5RnJyZxM8rqP34LcyIK4PxH8Xy0JNPM2kFIBDwayi3JXK5xR_0FQ3f6apqxSG4YlhZdO0cdHDrWGzmnxLC9V3NLxOPz2cVwKWzcKN96Nuji7e8klzyfC6yzQo4tQKC7lHF6tWsw4OyEJ6tauqklDKWsPsdBC0AuKIBBk0WHAnE9U4K4bEATAOZAM.png)

VictoriaMetrics 在几个讨论中突出出现，[这个用户](https://stas.starikevich.com/posts/disk-usage-for-vm-versus-prometheus/)分享了他对该产品磁盘存储特性和查询速度的经验:

![](https://assets-global.website-files.com/626a25d633b1b99aa0e1afa7/631ee4a7a7c4ff32d004a04b_KS1ZX9o6IGHL2G0I9mjm4VF4ZwtuWFph1Noc-aYk3z2nXygbfSw7w_D89yULA1RimhW__eYgiJZum94Qru-VHBinTtZedmrY6clBH5g9eye87Ran8aOABCktbigUqGovo6QoTlUFOMB_WxZsUZStMqptGliAuimM6VClFPdLW2WlWjswAgBcHyHPC34Oecbjm8I.png)

有趣的是，Grafana Labs 本身正在通过新的产品(如 [Loki](https://grafana.com/logs/)(根据 [Loki Github 存储库](https://github.com/grafana/loki)的说法，"类似 Prometheus，但适用于日志")、Traces([完全托管](https://grafana.com/traces/)和[自托管开源版本](https://github.com/grafana/tempo)中都提供的分布式跟踪服务)和 [Grafana Enterprise Metrics](https://grafana.com/products/enterprise/metrics/)(更可扩展的“Prometheus 即服务”功能))成为一家全栈可观测性公司。[Grafana Cloud](https://grafana.com/products/cloud/) 将所有这些功能组合成一个统一的、完全托管的可观测性平台，可与现有的 Prometheus 安装集成。

## 密切关注

Prometheus 和 Grafana 已经非常好地满足了 Kubernetes 可观测性需求(事实上，就总体可观测性而言也是如此)。随着 IT 基础设施的增长，围绕长期存储、查询速度、基数和混合可观测性的新解决方案的需求将越来越明显。这个领域的所有竞争者都在迅速变化和改进，因此无论您是刚刚考虑 Prometheus/Grafana 还是正在运行数百个 Kubernetes 集群，密切关注这个对话都是明智之举。
