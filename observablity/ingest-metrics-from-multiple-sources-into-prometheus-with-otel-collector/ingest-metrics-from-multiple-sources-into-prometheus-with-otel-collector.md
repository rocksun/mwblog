<!--
title: 使用 OTel Collector 将来自多个来源的指标提取到 Prometheus 中
cover: https://cdn.thenewstack.io/media/2025/05/3844a465-ingest-metrics-multiple-sources-prometheus-otelccollector.jpg
summary: 用`OTel Collector`搞定异构监控！统一`OTLP`、`StatsD`、`Prometheus exporters`等多源指标，通过`receiver`、`processor`标准化数据，再用`remote write exporter`推送到`Prometheus`，云原生可观测性起飞！
-->

用`OTel Collector`搞定异构监控！统一`OTLP`、`StatsD`、`Prometheus exporters`等多源指标，通过`receiver`、`processor`标准化数据，再用`remote write exporter`推送到`Prometheus`，云原生可观测性起飞！

> 译自：[Ingest Metrics from Multiple Sources into Prometheus with OTel Collector](https://thenewstack.io/ingest-metrics-from-multiple-sources-into-prometheus-with-otel-collector/)
> 
> 作者：Sharad Regoti

在企业发展的早期，[监控](https://thenewstack.io/whats-the-difference-between-observability-and-monitoring/)可能只是事后才考虑的事情。 后来，随着系统的发展，不同的团队在项目需求的驱动下，采用了各种工具。 后端团队采用了 [StatsD](https://github.com/statsd/statsd)，因为它很简单，可以将指标导入 [Graphite](https://graphiteapp.org/)。 基础设施工程师依赖于 syslog 或 [Nagios](https://www.nagios.org/) 检查。

后来，随着容器化的普及，另一个部门采用了 [Prometheus](https://prometheus.io/) 来监控微服务。快进到今天，最新的应用程序正在使用 [OpenTelemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 工具进行构建，并通过 [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/) 发送指标数据。

这种监控的无序扩张变得难以为继。跨系统关联问题非常复杂，管理不同的系统和配置会耗尽资源。因此，需要进行标准化和整合，但删除现有的工具通常是不切实际的。如何在不增加*更多复杂性*的情况下，将这些不同的指标来源（StatsD、Prometheus exporters 和 OTLP）桥接到一个中央 Prometheus 系统中？

[OTel Collector](https://thenewstack.io/how-adobe-uses-opentelemetry-collector/) 应运而生。它充当一个强大的、与供应商无关的**聚合层**和**协议转换器**。我们将向您展示如何使用 OTel Collector 作为中央枢纽，无缝地从这些不同的来源提取指标，一致地处理它们，并将它们发送到 Prometheus，从而简化您的架构，并为统一的可观测性铺平道路。

## 前提条件

我们将使用 [Docker](https://www.docker.com/?utm_content=inline+mention) 和 Docker compose：[使用容器](https://roadmap.sh/docker) 来运行 Prometheus、OTel Collector 和示例指标源。有关安装，请参阅本 [指南](https://docs.docker.com/desktop/setup/install/mac-install/)。

**Prometheus 的基本理解：** 熟悉 Prometheus 的概念，如抓取、指标格式和 Remote Write 会很有帮助。查看 [Prometheus 入门研讨会](https://o11y-workshops.gitlab.io/workshop-prometheus/) 以获取介绍。

**OTel Collector 的基本理解：** 了解接收器、处理器、导出器和 [pipelines](https://thenewstack.io/the-case-for-telemetry-pipelines) 很有用。如果您是新手，请查看 [官方 OTel Collector 文档](https://opentelemetry.io/docs/collector/configuration/)。

## 异构监控环境的问题

异构监控环境在不断发展的组织中很常见，您的环境是新旧技术的混合体。

这是一个场景：

- **新服务：** 您最新的微服务正在使用 OpenTelemetry 软件开发工具包 (SDK) 构建，使用 OTLP 发出指标，并使用一些中介将其发送到 Prometheus。
- **基础设施工具：** 您有现有的工具或基础设施组件（例如使用 node-exporter 或 mysqld-exporter 等 exporters 的数据库或代理），它们以 Prometheus 格式在特定的 HTTP 端点上公开指标。
- **StatsD 发射器：** 较旧的服务或特定工具正在使用 StatsD 协议通过用户数据报协议 (UDP) 将指标发送到 Graphite。

虽然每个组件都可能以*某种方式*被监控，但这种异构性会产生运营摩擦。如果没有中央聚合层，您将面临以下几个挑战：

*   Prometheus 需要为每个 exporter 和应用程序配置抓取。管理大量且动态的这些目标可能会变得具有挑战性。
*   [复杂的 Prometheus 配置：](https://o11y-workshops.gitlab.io/workshop-prometheus/#/9)
*   **多条摄取路径：** OTLP 数据可能需要专用的 OTLP-to-Prometheus 桥接或特定的接收器配置，具体取决于 Prometheus 是否直接支持它们。相比之下，每个基础设施工具（例如，MySQL、[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention)）都需要自己的 exporter。
*   **不一致的元数据：** 来自不同来源的指标可能缺少标准识别标签（例如环境、集群或应用程序组），这使得关联数据和创建统一的仪表板变得困难。
*   **维护开销：** 管理多个代理（例如 statsd_exporter，可能还有其他代理）和复杂的 Prometheus 抓取配置会增加运营负担。
该图说明了多个路径和所需的潜在系统，以及直接加在 Prometheus 上的配置负担。

![监控异构环境的复杂性，根据以上说明进行图解](https://cdn.thenewstack.io/media/2025/05/49155f0d-heterogenous-monitoring-architecture.png)

*来源: Chronosphere*

## OTel Collector 解决方案：统一的采集点

[OpenTelemetry Collector](https://docs.chronosphere.io/ingest/metrics-traces/otel/otel-ingest?utm_source=TNS&utm_medium=sponsored+content) 充当遥测数据的“瑞士军刀”。通过将其部署在指标源和 Prometheus 之间，您可以简化架构。

以下是它在我们的场景中的工作方式：

**接收器：** Collector 配置了多个接收器：

*   OTLP 接收器：侦听来自新服务的 OTLP 指标（gRPC 和/或 HTTP）。
*   Prometheus 接收器：主动抓取旧版 Prometheus 导出器的 /metrics 端点。
*   Statsd 接收器：侦听 UDP 端口上的 StatsD 指标。

**处理器：** Collector 可以处理流经它的指标。一个关键用例是使用资源处理器等处理器添加标准元数据，以确保发送到 Prometheus 的所有指标都具有一致的标签（例如，environment=”production”，k8s_cluster=”main”）。

**导出器：** 然后，Collector 使用以下一种（或两种）方法将统一的处理后的指标导出到 Prometheus：

*   **Prometheus Remote Write exporter**：将指标直接推送到 Prometheus 的 remote write 端点。这使 Collector 与 Prometheus 的抓取周期分离。
*   **Prometheus exporter**：在 Collector 本身*上*公开一个*新的*/metrics 端点。此端点包含来自所有已配置接收器的聚合指标。然后，您可以配置 Prometheus 以*仅从 Collector 抓取这单个端点*。

这种方法将处理 Collector 中各种来源的复杂性集中化，从而使 Prometheus 可以专注于其核心优势：存储、查询 (PromQL) 和警报。

下图显示了 Collector 如何充当中心枢纽，从而简化了 Prometheus 的连接和配置。

![OTel Collector 充当 Prometheus 的中心枢纽](https://cdn.thenewstack.io/media/2025/05/7af3cc50-otel-collector-central-hub.png)

来源: Chronosphere

## 使用 OpenTelemetry Collector 统一指标

![OTel Collector 集中了来自各种来源（例如 MySQL、OTLP、Apache Airflow）的指标采集。](https://cdn.thenewstack.io/media/2025/05/ee329da0-unify-metrics-otel.png)

*来源: Chronosphere*

该图演示了 [OpenTelemetry Collector](https://docs.chronosphere.io/ingest/logs/otel-logs-oem?utm_source=TNS&utm_medium=sponsored+content) 如何集中来自各种来源的指标采集。

左侧是一些示例，例如发送 OTLP 的现代应用程序、提供其特定指标的 MySQL 数据库以及发出 StatsD 数据的 [Apache Airflow](https://thenewstack.io/apache-airflow-3-0-from-data-pipelines-to-ai-inference/)。每种不同的数据类型都流入 [OTel Collector](https://docs.chronosphere.io/ingest/metrics-traces/otel?utm_source=TNS&utm_medium=sponsored+content) 中相应的专用接收器（分别为 OTLP、MySQL 和 StatsD 接收器）。

然后，这些指标通过通用处理器进行处理，这些处理器可以通过添加一致的资源属性（例如环境标签）并批量处理它们以提高效率来规范化数据。

最后，单个导出器（例如本示例中使用的 `prometheusremotewrite` exporter）将这些指标传输到您的中心 Prometheus 实例，从而大大简化了整体监控管道。

让我们使用 Docker Compose 将其转换为一个可用的设置。

### 配置 Fluent Bit 的说明

**1. 创建您的目录。**

打开您的终端并创建一个名为 `otel-test` 的目录：

```
mkdir otel-test && cd otel-test
```

**2. 创建一个 Docker 网络。**

运行命令：

```
docker network create opentelemetry-demo
```

#### **3. 设置 MySQL。**

创建一个名为 `mysql.yml` 的文件，其中包含以下内容：

```yaml
services:
  mysql:
    image: mysql:8.0
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_USER: otel
      MYSQL_PASSWORD: otelpass
      MYSQL_DATABASE: otel
    ports:
      - "3306:3306"
    networks:
      - opentelemetry-demo

networks:
  opentelemetry-demo:
    external: true
```

**4. 设置 Apache Airflow。**

创建一个名为 `airflow.yml` 的文件，其中包含以下内容：

```yaml
services:
  airflow:
    image: apache/airflow:2.8.1-python3.10
    container_name: airflow
    environment:
      - AIRFLOW__METRICS__STATSD_ON=True
      - AIRFLOW__METRICS__STATSD_HOST=otel-collector
      - AIRFLOW__METRICS__STATSD_PORT=8125
      - AIRFLOW__CORE__EXECUTOR=SequentialExecutor
      - AIRFLOW__CORE__LOAD_EXAMPLES=False
    command: bash -c "airflow db init && airflow standalone"
    networks:
      - opentelemetry-demo

networks:
  opentelemetry-demo:
    external: true
```

**5. 设置 OpenTelemetry instrumentation 的应用程序。**
在你的终端中执行以下命令。这将创建两个文件：`.env` 和 `otel-demo.yml`。此设置使用了一个精简版的 [otel-demo](https://github.com/open-telemetry/opentelemetry-demo) 仓库。

```
wget https://gist.githubusercontent.com/sharadregoti/6223a08ad3f52c7eee1b688aaff68c42/raw/d87e4dd0911bf0af45b33e9b3a0566d335d70efa/.env
```

**6. 设置 Prometheus。**
执行以下命令，在 `prometheus` 目录下创建 Prometheus 配置文件：

```
mkdir prometheus && cd prometheus && touch prometheus.yml
```

将以下内容复制到配置文件中：

```yaml
global:
  scrape_interval:     15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']
```

导航到上一级目录（`prometheus` 目录之外），并创建一个名为 `prometheus-compose.yml` 的文件，内容如下：

```yaml
services:
  prometheus:
    image: prom/prometheus:v2.53.4 # Use a recent version
    container_name: prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--web.enable-lifecycle' # Allows config reload
      - '--web.enable-remote-write-receiver' # Crucial for receiving remote write data
    volumes:
      - ./prometheus:/etc/prometheus
      - prometheus_data:/prometheus # Optional: Persist data
    ports:
      - "9090:9090"
    networks:
      - opentelemetry-demo

volumes:
  prometheus_data: {}

networks:
  opentelemetry-demo:
    external: true
```

**7. 配置和设置 OpenTelemetry Collector。**
执行以下命令，在 `otel-collector` 目录下创建 OTEL 配置文件：

```
mkdir otel-collector && cd otel-collector && touch otel-collector-config.yaml
```

将以下内容复制到配置文件中：

```yaml
receivers:
  # 1. OTLP Receiver (for gRPC and HTTP)
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

  # 2. Prometheus Receiver (to scrape existing exporters)
  prometheus:
    config:
      scrape_configs:
        - job_name: 'legacy-node-exporter'
          scrape_interval: 10s
          static_configs:
            - targets: ['node-exporter:9100']
          metric_relabel_configs:
            - source_labels: [__address__]
              target_label: collector_scraped_target

  # 3. StatsD Receiver
  statsd:
    endpoint: 0.0.0.0:8125 # Listen on UDP port 8125
    aggregation_interval: 10s # Aggregate stats over 10s before flushing
  mysql:
    endpoint: mysql:3306
    username: otel
    password: otelpass
    database: otel
    collection_interval: 10s
    initial_delay: 1s
    statement_events:
      digest_text_limit: 120
    time_limit: 24h
    limit: 250

processors:
  # Standard processors
  memory_limiter:
    check_interval: 1s
    limit_percentage: 75
    spike_limit_percentage: 25
  batch:
    send_batch_size: 8192
    timeout: 1s

  # Add common attributes/labels to all metrics passing through
  resource:
    attributes:
      - key: environment
        value: "development"
        action: insert # Add if not present
      - key: collector.instance.id
        value: "otel-collector-01"
        action: insert

exporters:
  # 1. Prometheus Remote Write Exporter
  # Pushes metrics TO Prometheus's remote write endpoint
  prometheusremotewrite:
    endpoint: "http://prometheus:9090/api/v1/write" # URL of Prometheus remote write endpoint
    resource_to_telemetry_conversion:
      enabled: true

service:
  pipelines:
    metrics:
      receivers: [otlp, prometheus, statsd, mysql]
      processors: [memory_limiter, resource, batch]
      exporters: [prometheusremotewrite]
```

导航到上一级目录（`otel-collector` 目录之外），并创建一个名为 `otel-collector.yml` 的文件，内容如下：

```yaml
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:0.123.0 # Use contrib for more receivers/exporters
    container_name: otel-collector
    command: ["--config=/etc/otelcol-contrib/otel-collector-config.yaml"]
    volumes:
      - ./otel-collector:/etc/otelcol-contrib
    ports:
      # Receivers
      - "4317:4317"   # OTLP gRPC receiver
      - "4318:4318"   # OTLP HTTP receiver
      - "8125:8125/udp" # StatsD receiver
      # Exporters
      - "8889:8889"   # Prometheus exporter (for Prometheus to scrape the collector)
      # Optional: Expose Collector's own metrics
      - "8888:8888"
    networks:
      - opentelemetry-demo

networks:
  opentelemetry-demo:
    external: true
```

**8. 运行所有服务。**
执行此命令：

```
docker compose \
  -f mysql.yml \
  -f airflow.yml \
  -f otel-demo.yml \
  -f prometheus-compose.yml \
  -f otel-collector.yml up -d
```

这将需要几分钟时间；请等待命令完成。
**9. 在 Prometheus 中观察输出。**
使用此 URL 在浏览器中打开 Prometheus：`http://localhost:9090/graph`，并在控制台中运行以下命令：

```
{environment="development"}
```

您应该看到类似于下图的输出。
![Prometheus output](https://cdn.thenewstack.io/media/2025/05/561bdd36-prometheus-output.png)
来源: Chronosphere
要查看更多结果，请尝试以下 Prometheus 查询。

```
12345 |
# To view "airflow" statsd metricsairflow# To view "mysql" metricsmysql |
```

**10. 清理。**

执行以下命令以删除所有容器：

```
123456 |
docker compose \ -f mysql.yml \ -f airflow.yml \ -f otel-demo.yml \ -f prometheus-compose.yml \ -f otel-collector.yml down && docker network rm opentelemetry-demo |
```

## 结论

[OpenTelemetry Collector](https://chronosphere.io/learn/evaluating-an-observability-vendor-why-you-should-try-before-you-buy-with-the-opentelemetry-collector/?utm_source=TNS&utm_medium=sponsored+content) 帮助管理异构环境中的指标。通过充当中央聚合和处理层，它允许您：

- **简化 Prometheus 配置：** 减少 Prometheus 需要管理的抓取目标和专用导出器的数量。
- **统一不同的指标源：** 通过单个组件提取 OTLP、Prometheus 格式的指标和 StatsD（以及接收器支持的许多其他格式）。
- **确保一致性：** 使用处理器应用标准标签和转换，以确保所有指标上的标准化元数据。
- **提供灵活性：** 在通过 Prometheus Remote Write 推送指标或公开单个聚合抓取端点以供 Prometheus 拉取之间进行选择。

无论您是将应用程序迁移到 OpenTelemetry、集成遗留系统，还是只是处理复杂的指标源组合，OTel Collector 都提供了一个强大的解决方案来弥合可观测性堆栈中的差距。