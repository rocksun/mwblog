# 基础设施监控入门

通过利用监控数据，公司可以确保他们的基础设施在以最佳状态运行的同时降低成本。

![](https://cdn.thenewstack.io/media/2023/09/31a6901d-monitoring-1024x683.jpg)
*图片来自 Shutterstock 的 GaudiLab*

[InfluxData](https://www.influxdata.com/?utm_content=sponsor-disclosure) 赞助了这篇文章。

虽然构建新功能和推出新产品很有趣，但如果你的软件不可靠，这一切都无关紧要。确保应用程序顺利运行的关键部分之一是具有稳健的基础设施监控。在本文中，您将学习以下内容：

* 基础设施监控的不同组成部分。
* 用于基础设施监控的流行工具。
* 如何为应用程序设置监控。

如果您更喜欢视频，也可以查看[这个演示](https://www.youtube.com/watch?v=ESub4SAKouI)，它涵盖了本文中讨论的一些主题。

## 基础设施监控的组件

基础设施监控由现代应用程序所需的各种不同架构组件组成。为了确保软件的可靠性，所有这些组件都需要得到适当的监控。

* **网络监控** - [网络](https://thenewstack.io/networking/)监控侧重于硬件(如路由器和交换机)，涉及跟踪带宽使用、正常运行时间和设备状态等内容。它用于识别瓶颈、停机时间和潜在的低效网络路由。
* **服务器监控** - 服务器监控侧重于监控物理和虚拟服务器实例的性能和运行状况。常见的指标有 CPU、RAM 和磁盘利用率。服务器监控对容量规划很重要。
* **应用程序性能监控(APM)** - APM 侧重于软件，用于跟踪应用程序在从 UI 到数据存储的每一层的执行情况。常见指标有错误率和响应时间。
* **云基础设施监控** - 如其名所示，云监控涉及监控数据库、不同类型的存储和 VM 等云基础设施。其目标是跟踪可用性和性能，以及资源利用率，以防止云硬件的过度或不足配置。

这些不同类型的监控充当了团队查看和管理其基础设施的不同透视。通过利用所有这些数据，公司可以确保其基础设施以最佳状态运行，同时降低成本。

## 基础设施监控工具

选择正确的工具至关重要，以便建立基础设施监控系统。有许多开源和商业选择可用。您还可以选择全服务解决方案，或通过组合专业工具来创建自己的定制解决方案。无论如何，有三个主要问题需要考虑：您将如何收集数据，如何存储数据以及您将对数据做什么。让我们看一下用于完成每一项工作的一些工具。

## 数据收集工具

基础设施监控的最大挑战之一是收集可能来自许多不同源的数据，而这些数据通常没有标准化的协议或 API。这里的关键目标应该是选择一个工具，该工具可以节省您重新发明轮子的时间，不会锁定您，并且是可扩展的，以便随着您的应用程序的变化而扩展或修改数据收集。

### Telegraf

Telegraf 是一个开源服务器代理，非常适合基础设施监控数据收集。Telegraf 解决了上述大多数问题。它拥有 300 多个不同的输入和输出插件，这意味着您可以轻松从新源收集数据，并将该数据输出到最适合您的用例的存储解决方案。

结果是，Telegraf 通过不必编写自定义代码来收集数据并可轻松更改存储输出来防止供应商锁定，为您节省了大量工程资源。在某些用例中，Telegraf [还具有用于数据处理和转换的插件](https://www.influxdata.com/time-series-platform/telegraf/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)，因此它可以通过替换流处理工具来简化架构。

### OpenTelemetry

OpenTelemetry 是一个开源的 SDK 和工具集，可以轻松地从应用程序中收集指标、日志和[跟踪](https://www.influxdata.com/blog/tracing-influxdb-iox/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)。 [OpenTelemetry](https://thenewstack.io/how-adobe-uses-opentelemetry-collector/) 的主要优势在于其供应商中立性，因此您不必担心被昂贵的 APM 工具锁定，这会带来高昂的切换成本。 [OpenTelemetry](https://www.influxdata.com/blog/opentelemetry-tutorial-collect-traces-logs-metrics-influxdb-3-0-jaeger-grafana/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns) 还通过提供使应用程序易于检测数据收集的工具来节省开发人员的时间。

## 数据存储工具

在开始从基础设施中收集数据后，您需要一个地方来存储该数据。 虽然可以将通用数据库用于此数据，但在许多情况下，您会希望寻找一个更专门的数据库，该数据库专门用于处理为基础设施监控收集的[时间序列数据](https://www.influxdata.com/what-is-time-series-data/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)类型。 这里有一些可用的选项：

### InfluxDB

InfluxDB 是一个开源时间序列数据库，用于存储和分析大量时间序列数据。它提供高效的存储和检索功能、可扩展性和实时分析支持。使用 [InfluxDB](https://www.influxdata.com/products/influxdb-overview/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-mointoring_tns)，您可以轻松捕获和存储来自各种源的指标，这使它非常适合监控和分析基础设施的性能和运行状况。

### Prometheus

Prometheus 是一个开源监控和报警工具包，用于收集和存储指标数据。它专门用于监控动态和云原生环境。[Prometheus](https://www.influxdata.com/integration/prometheus-monitoring-tool/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns) 提供了灵活的数据模型和强大的查询语言，这使它非常适合存储基础设施监控数据。通过其内置的报警和可视化功能，Prometheus 使您能够洞察基础设施的性能和可用性。

### Graphite

Graphite 是一个时间序列数据库和可视化工具，侧重于存储和呈现监控数据的图表。它被广泛用于监控和绘制各种指标图表，这使它成为存储基础设施监控数据的合适选择。Graphite 在可视化时间序列数据方面表现突出，允许您创建交互式和可自定义的仪表板来监控基础设施的性能和趋势。它的可扩展架构和广泛的插件生态系统使它成为监控和分析基础设施指标的热门选择。

## 数据分析工具

一旦您的数据存储完毕，就是玩儿的时候了，实际上可以用它来创造价值。这里有一些可以用于分析数据的工具。

### Grafana

Grafana 是一个强大的开源数据可视化和分析工具，允许用户创建、探索和共享交互式仪表板。它通常用于通过连接到各种数据源(如数据库、API 和监控系统)来分析基础设施监控数据。使用 [Grafana](https://www.influxdata.com/grafana/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)，用户可以创建可视化、设置报警并深入了解基础设施指标、日志和跟踪。

### Apache Superset

Apache Superset 是一个现代的企业级业务智能 Web 应用程序，可让用户探索、可视化和分析数据。它提供了一个友好的界面来创建交互式仪表板、图表和报告。当涉及到分析基础设施监控数据时，[Apache Superset](https://www.influxdata.com/integration/apache-superset/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns) 可用于连接到监控系统、数据库或其他数据源，以探索和可视化关键指标、生成报告并洞察基础设施的性能和运行状况。

### Jaeger

Jaeger 是一个开源的端到端分布式跟踪系统，可帮助用户监控和排除复杂的微服务架构问题。它可以通过提供对基础设施不同组件之间交互和依赖关系的详细洞察来分析基础设施监控数据。[Jaeger](https://thenewstack.io/best-practices-for-deploying-jaeger-on-kubernetes-in-production/) 捕获和可视化跟踪，跟踪表示请求在系统中的传播路径，允许用户识别基础设施中的瓶颈、延迟问题和性能优化。

## 基础设施监控教程

现在让我们看一个如何为应用程序实现监控系统的示例。本教程将重点介绍一组称为 [TIG 栈](https://www.influxdata.com/blog/tig-stack-iiot-ot/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)的开源工具：Telegraf、InfluxDB 和 [Grafana](https://www.influxdata.com/blog/getting-started-influxdb-grafana/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)。 TIG栈使开发人员可以轻松构建一个可扩展且长期可扩展的基础设施监控解决方案。

### 架构概述

本教程的示例应用程序是一个聊天应用程序，它由一个根据用户输入返回响应的 AI 模型提供支持。该应用程序具有混合架构，后端托管在 AWS 上，AI 模型在云之外的专用 GPU 上运行。主要挑战是在保证服务可靠性的同时也扩展基础设施，因为用户增长迅速。要做到这一点，需要收集大量数据来实时跟踪资源利用率，用于监控，也用于根据用户增长进行未来容量规划。

### 基础设施监控设置

现在我们来看看如何为此应用程序设置和配置监控。第一步将是配置 Telegraf 以收集我们从基础设施的每一部分所需的数据。我们将利用以下 [Telegraf](https://www.influxdata.com/blog/storing-secrets-telegraf/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns) 插件:

- **SNMP 输入** - SNMP 插件用于收集所需的网络监控指标。
- **CPU、Disk、Nvidia SMI、DiskIO、mem、swap、system 输入** - 这些插件用于收集服务器监控指标。
- **OpenTelemetry 输入** - 使用 OpenTelemetry 收集应用程序性能指标，如日志、指标和跟踪。 
- **AWS Cloudwatch 输入** - AWS CloudWatch 插件可以轻松地从 AWS 收集所有所需的云基础设施指标。
- **[InfluxDB V2 输出](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/influxdb_v2)** - InfluxDB 输出插件将发送所有这些收集的指标到指定的 InfluxDB 实例。

下面是一个针对此设置的 Telegraf 配置 [TOML 文件](https://docs.fileformat.com/programming/toml/#:~:text=TOML%20(Tom's%20Obvious%20Minimal%20Language,parse%20to%20different%20data%20structures.)的示例：

```TOML
[global_tags]
  # dc = "us-east-1" # will tag all metrics with dc=us-east-1
  # rack = "1a" 
  # user = "$USER"
  
[agent]
  interval = "10s"
  round_interval = true
   
  metric_batch_size = 1000
  metric_buffer_limit = 10000
  collection_jitter = "0s"
   
  flush_interval = "10s" 
  flush_jitter = "0s"
  precision = ""
   
  # debug = false
  # quiet = false
  # logtarget = "file"
  # logfile = ""
  # logfile_rotation_interval = "0d"
  # logfile_rotation_max_size = "0MB"
  # logfile_rotation_max_archives = 5
   
  hostname = ""
  omit_hostname = false
  
[[inputs.snmp]]
  agents = ["udp://127.0.0.1:161"].
  timeout = "15s"
   version = 2
   community = "SNMP"
  retries = 1
   
    
  [[inputs.snmp.field]]
    oid = "SNMPv2-MIB::sysUpTime.0"
    name = "uptime" 
    conversion = "float(2)"
   
  [[inputs.snmp.field]]
    oid = "SNMPv2-MIB::sysName.0"
    name = "source"
    is_tag = true
  
[[inputs.cpu]]
  percpu = true
  totalcpu = true
  collect_cpu_time = false
  report_active = false
  
[[inputs.disk]]
  ignore_fs = ["tmpfs"， "devtmpfs"， "devfs"， "iso9660"， "overlay"， "aufs"， "squashfs"]
  
[[inputs.diskio]]
[[inputs.mem]]  
[[inputs.processes]]
[[inputs.swap]]
[[inputs.system]]
[[nvidia-smi]]

[[inputs.opentelemetry]]
service_address = "0.0.0.0:4317"

  timeout = "5s"

 metrics_schema = "prometheus-v2"

  tls_cert = "/etc/telegraf/cert.pem"
   tls_key = "/etc/telegraf/key.pem"

[[inputs.cloudwatch_metric_streams]]

  service_address = ":443" 

[[inputs.cloudwatch]]
  region = "us-east-1"
  
[[outputs.influxdb_v2]]
  urls = ["http://127.0.0.1:8086"]

  ## Token for authentication.  
  token = ""

  ## Organization is the name of the organization you wish to write to.
  organization = ""

  ## Destination bucket to write into. 
  bucket = ""

  ## The value of this tag will be used to determine the bucket.  If this
  ## tag is not set the 'bucket' option is used as the default.
  # bucket_tag = ""

  ## If true， the bucket tag will not be added to the metric.
  # exclude_bucket_tag = false

  ## Timeout for HTTP messages.
  # timeout = "5s"

  ## Additional HTTP headers
  # http_headers = {"X-Special-Header" = "Special-Value"}

  ## HTTP Proxy override， if unset values the standard proxy environment
  ## variables are consulted to determine which proxy， if any， should be used. 
  # http_proxy = "http://corporate.proxy:3128"

```

这个 Telegraf 配置通过收集所有指定的数据并将其发送到 InfluxDB 进行存储，完成了数据收集和数据存储这两个步骤。 让我们过一下您可以用这些数据做些什么。

![](https://cdn.thenewstack.io/media/2023/09/7daf28dd-image2-e1694104722975.png)

### 数据可视化

许多公司的第一个步骤是为他们的基础设施监控系统创建仪表板和数据可视化。这些仪表板可用于从高级报告到工程师实时详细分析监控的一切。这里是一个使用本教程中收集的数据构建的 Grafana 仪表板示例：

![](https://cdn.thenewstack.io/media/2023/09/c8403fdb-image4-e1694104768999.png)

### 报警

虽然仪表板很好，但在大规模下手动跟踪基础设施发生的一切是不可能的。 为了帮助解决这个问题，设置自动化报警是基础设施监控系统的常见功能。 这里有一个关于 Grafana 如何用于为指标设置值阈值并在违反这些阈值时创建自动报警的示例。

![](https://cdn.thenewstack.io/media/2023/09/1e53ef05-image1-e1694104800868.png)

Grafana 与 PagerDuty 和 Slack 等第三方工具集成，以便如果发生故障，通知工程师。 在某些情况下，这样的报警可以完全自动化某些操作，例如如果硬件利用率达到一定水平，自动扩展云容量。

### 预测分析和预测

对许多工程团队来说，[预测分析](https://www.influxdata.com/resources/enabling-predictive-analytics-with-influxDB/?utm_source=vendor&utm_medium=referral&utm_campaign=2023-09_spnsr-ctn_infrastructure-monitoring_tns)和预测可能是最理想的最终目标。 虽然报警是一种响应方法，只有在发生问题后才起作用，但预测分析和预测允许您在问题发生之前采取行动。 创建准确的预测显然说起来容易，做起来难，但如果做的正确，确实具有巨大的好处。
