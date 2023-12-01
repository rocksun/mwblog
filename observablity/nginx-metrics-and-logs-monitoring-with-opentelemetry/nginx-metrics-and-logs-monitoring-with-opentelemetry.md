<!--
title: 使用OpenTelemetry监控Nginx指标和日志
cover: https://signoz.io/assets/images/nginx-metrics-logs-otel-cover-5a6bfe5736f7a85aebcb51d133abc8c3.webp
 -->

Nginx 指标和日志的监控对于确保 Nginx 的性能符合预期以及快速识别和解决问题至关重要。在本教程中，您将安装 OpenTelemetry Collector 来收集 Nginx 指标和日志，然后将收集的数据发送到 SigNoz 进行监控和可视化分析。

> 译自 SigNoz 官方博客的 [Nginx Metrics and Logs Monitoring with OpenTelemetry](https://signoz.io/blog/nginx-metrics-and-logs-monitoring-with-opentelemetry)，作者 Abhishek Kothari 。

本教程涵盖的内容：

- NGINX 简介
- OpenTelemetry 简介
- OpenTelemetry Collector 如何收集数据？
- 前提条件
- 设置 SigNoz
- 设置 OpenTelemetry Collector
- 使用 Signoz 仪表板监控
- 参考:OpenTelemetry Collector 收集的 NGINX 指标
- 总结
- 扩展阅读

如果你想直接跳到实现，请从这个前提条件部分开始。

对于每秒服务数千个请求的大规模 Web 应用程序，拥有多个后端服务器是必要的。这些后端服务器最终通过负载均衡服务器接收流量，该服务器根据需要处理请求分发。这种类型的服务器称为反向代理服务器。在本文中，我们将学习监控最流行的反向代理服务器之一——NGINX。

## NGINX 简介

NGINX 是当今使用最广泛的开源反向代理服务器之一。它广泛用于托管静态前端作为 Web 服务器以及通过充当负载均衡器将流量路由到多个后端服务器。在其核心，NGINX 是用 C++ 编写的，设计上非常模块化。NGINX 允许你添加即插即用模块以获取增强功能，如安全和监控。尽管 NGINX 的初始设置非常简单，但它有一些复杂的参数需要调整，以便为高流量网站实现最佳配置。这使从 NGINX 获取和观测指标变得必要。

## OpenTelemetry 简介

OpenTelemetry 是一组 API、SDK、库和集成，旨在标准化遥测数据(日志、指标和跟踪)的生成、收集和管理。它由云原生计算基金会支持，是可观测性领域领先的开源项目。

您使用 OpenTelemetry 收集的数据与供应商无关，可以以多种格式导出。遥测数据在观测分布式系统状态方面至关重要。随着微服务和多语言架构的出现，需要一个全局标准。OpenTelemetry 旨在填补这一空白，到目前为止，它在这方面做得很好。

在本教程中，您将使用 OpenTelemetry Collector 收集 PostgreSQL 指标以进行性能监控。

### 什么是 OpenTelemetry Collector？

OpenTelemetry Collector 是 OpenTelemetry 提供的独立服务。它可以用作具有大量灵活配置的遥测处理系统，以收集和管理遥测数据。

它可以理解不同的数据格式，并将其发送到不同的后端，这使它成为构建可观测性解决方案的通用工具。

[阅读我们关于 OpenTelemetry Collector 的完整指南](https://signoz.io/blog/opentelemetry-collector-complete-guide/)

## OpenTelemetry Collector 如何收集数据？

receiver是数据进入 OpenTelemetry Collector 的方式。receiver通过 YAML 的 top-level `receivers` 标记进行配置。配置至少必须有一个启用的 receiver 才被视为有效。

这是一个 otlp receiver 的示例:

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:
```

OTLP receiver可以通过 gRPC 或 HTTP 使用 OTLP 格式接收数据。您可以通过 YAML 文件启用高级配置。

这是一个 `otlp` receiver的示例配置。

```yaml
receivers:
  otlp:
    protocols:
      http:
        endpoint: "localhost:4318"
        cors:
          allowed_origins:
            - http://test.com
            # Origins 可以使用 * 通配符，使用 * 匹配任何 origin。
            - https://*.example.com
          allowed_headers:
            - Example-Header
          max_age: 7200
```

您可以[在此](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/otlpreceiver/README.md)了解有关高级配置的更多详细信息。

配置receiver后，必须启用它。receiver通过服务部分中的pipeline启用。pipeline由一组receiver、processor和exporter组成。

以下是pipeline配置示例:

```yaml
service:
  pipelines:
    metrics:
      receivers: [otlp， prometheus]
      exporters: [otlp， prometheus]
    traces:
      receivers: [otlp， jaeger]
      processors: [batch]
      exporters: [otlp， zipkin]
```

现在您已经理解 OpenTelemetry collector 如何收集数据，让我们看看如何收集 Nginx 指标和日志。

## 前提条件

如果您计划监控本地 NGINX 设置，则本教程假设您已在 NGINX 所在的主机上安装 OpenTelemetry collector。如果您正在寻找监控远程 NGINX 设置，则需要打开网络端口以允许 OpenTelemetry collector 访问指标。

### 准备 NGINX

为了本教程的目的，我们将假设以下情况：

- 在设置 OpenTelemetry collector 时，NGINX 安装在同一主机上。
- 已启用 NGINX 日志并存储在路径 `/var/log/nginx/access.log` 中。

您可以使用此[参考](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source)文档在服务器上安装 NGINX。

安装完成后，我们可以配置 NGINX 以包含显示服务器统计信息的端点。为此，请在服务器块顶部添加以下块:

```conf
http {

server {

location /status {
  stub_status on;
}

...
...
 # your configuration

}

}
```

如果这是 NGINX 的新安装，您可以将此块添加到 default.conf 中。添加后，运行命令 `sudo nginx -t` 以验证更改。如果测试成功，您可以重新启动 NGINX 服务。现在，打开 `http://your-domain/status` URL(如果在本地测试，请将域使用 `[localhost](http://localhost)`)。您会看到类似下图的输出。

![](https://signoz.io/img/blog/2023/12/nginx_status_page.webp)

*NGINX 状态页面*

您的 NGINX 服务器现已准备好提供指标。

## 设置 SigNoz

您需要一个后端来发送收集的数据以进行监控和可视化。[SigNoz](https://signoz.io/) 是一种 OpenTelemetry 原生 APM，非常适合可视化 OpenTelemetry 数据。

SigNoz 云是运行 SigNoz 的最简单方法。您可以[在此](https://signoz.io/teams/)注册一个免费帐户，并获得 30 天的免费无限制使用。

您也可以自己安装和自托管 SigNoz。有关安装自托管 SigNoz 的[文档](https://signoz.io/docs/install/)。

## 设置 OpenTelemetry Collector

### 步骤 1 - 下载 OpenTelemetry Collector

从 OpenTelemetry Collector 发布页面下载适合您的 Linux 或 macOS 发行版的二进制包。我们正在使用撰写本教程时可用的最新版本。

对于 MACOS (arm64):

```bash
curl --proto '=https' --tlsv1.2 -fOL https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v0.90.0/otelcol-contrib_0.90.0_darwin_arm64.tar.gz
```

### 步骤 2 - 提取包

创建一个名为 `otelcol-contrib` 的新目录，然后使用以下命令将归档内容提取到新创建的目录中:

```bash
mkdir otelcol-contrib && tar xvzf otelcol-contrib_0.90.0_darwin_arm64.tar -C otelcol-contrib
```

### 步骤 3 - 设置配置文件

在本教程中，我们将监控 NGINX 的指标并可视化其访问日志。让我们在 otelcol-contrib 文件夹中创建一个 config.yaml。这将使用 NGINX receiver 为指标和文件日志 receiver 为日志配置 Collector。

**注意:**

配置文件应在您解压 `otel-collector-contrib` 二进制文件所在的同一目录中创建。如果您已全局安装了二进制文件，则可以在任意路径上创建。

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: localhost:4317
      http:
        endpoint: localhost:4318
  nginx:
    endpoint: "http://localhost:80/status"
    collection_interval: 10s
  filelog:
    include:
      - /var/log/nginx/*.log
processors:
  batch:
    send_batch_size: 1000
    timeout: 10s
  attributes:
    actions:
      - key: app
        value: nginx
        action: insert
exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    # 将 {region} 替换为您的区域
    tls:
      insecure: false
    headers:
      "signoz-access-token": "{your-signoz-token}"
      # 从 https://{your-signoz-url}/settings/ingestion-settings 获取
logging:
  verbosity: detailed
service:
  telemetry:
    metrics:
      address: localhost:8888
    pipelines:
      metrics:
        receivers: [otlp， nginx]
        processors: [batch]
        exporters: [otlp]
      logs:
        receivers: [filelog]
        processors: [attributes]
        exporters: [otlp]
```

您需要在上述文件中用选择的区域(对于 Signoz 云)和从 Signoz 云 → 设置 → 摄入设置中获取的令牌替换区域和 signoz-token。

![](https://signoz.io/img/blog/common/ingestion-key-details.webp)

*您可以在 SigNoz 仪表板中找到摄入详细信息*

上述配置非常简单——每当您想要监控其他 Nginx 实例时，您需要更改 `nginxreceiver` 的 `endpoint` URL。但是，对于日志，OpenTelemetry collector 需要在日志文件所在的同一主机上运行。您还可以通过添加多个 receiver 来监控多个 NGINX 服务器，如下所示：

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: localhost:4317
      http:
        endpoint: localhost:4318
  nginx:
    endpoint: "http://localhost:80/status"
    collection_interval: 10s
  nginx/2:
    endpoint: "http://<remote-nginx>:80/status"
    collection_interval: 10s
  filelog:
    include:
      - /var/log/nginx/*.log
processors:
  batch:
    send_batch_size: 1000
    timeout: 10s
  attributes/remotenginx:
    actions:
      - key: endpoint
        value: <remote-endpoint>
        action: insert
  attributes/localnginx:
    actions:
      - key: endpoint
        value: <local-endpoint>
        action: insert
  attributes:
    actions:
      - key: app
        value: nginx
        action: insert
exporters:
  otlp:
    endpoint: "ingest.{region}.signoz.cloud:443"
    # 将 {region} 替换为您的区域
    tls:
      insecure: false
    headers:
      "signoz-access-token": "{your-signoz-token}"
      # 从 https://{your-signoz-url}/settings/ingestion-settings 获取
logging:
  verbosity: detailed
service:
  telemetry:
    metrics:
      address: localhost:8888
    pipelines:
      metrics:
        receivers: [otlp， nginx]
        processors: [attributes/localnginx， batch]
        exporters: [otlp]
      metrics/2:
        receivers: [otlp， nginx/2]
        processors: [attributes/remotenginx， batch]
        exporters: [otlp]
      logs:
        receivers: [filelog]
        processors: [attributes]
        exporters: [otlp]
```

### 步骤 4 - 运行 collector 服务

每个 Collector 版本都包含一个可以运行的 otelcol 可执行文件。既然我们已经完成了配置，现在可以使用以下命令运行 collector 服务。

从 otelcol-contrib 运行以下命令:

```bash
./otelcol-contrib --config ./config.yaml
```

如果要在后台运行 -

```bash
./otelcol-contrib --config ./config.yaml &> otelcol-output.log & echo "$\!" > otel-pid
```

### 步骤 5 - 调试输出

如果你想查看刚刚为后台进程设置的日志输出，可以使用以下命令：

```bash
tail -f -n 50 otelcol-output.log
```

其中，`tail 50` 将提供文件 `otelcol-output.log` 的最后50行日志。

你可以使用以下命令停止 collector 服务：

```bash
kill "$(< otel-pid)"
```

大约在30秒内，你应该能够在你的 Signoz Cloud UI 上看到指标。

## 使用 Signoz 仪表板监控

完成上述设置后，你将能够在 SigNoz 仪表板中访问这些指标。你可以转到仪表板标签并尝试添加一个新的面板。你可以在[这里](https://signoz.io/docs/userguide/manage-dashboards-and-panels/)了解如何在 SigNoz 中创建仪表板。

![](https://signoz.io/img/blog/2023/12/nginx_metrics.webp)

*由 OpenTelemetry collector 收集的 NGINX 指标*

你可以使用 SigNoz 中的[查询构建器](https://signoz.io/docs/userguide/create-a-custom-query/#sample-examples-to-create-custom-query)轻松创建图表。以下是将新面板添加到仪表板的[步骤](https://signoz.io/docs/userguide/manage-panels/#steps-to-add-a-panel-to-a-dashboard)。

![](https://signoz.io/img/blog/2023/12/nginx_dashboard_panel.webp)

*创建用于平均连接接受的仪表板面板*

你可以围绕发出的各种指标构建一个完整的仪表板。以下是使用收集的指标构建的示例仪表板。

![](https://signoz.io/img/blog/2023/12/nginx_dashboard_panel2.webp)

*示例仪表板*

你还可以在任何指标上创建警报。了解如何在[这里](https://signoz.io/docs/userguide/alerts-management/)创建警报。

![](https://signoz.io/img/blog/2023/12/nginx_create_alerts.webp)

### 可视化 NGINX 日志

为了可视化由 OpenTelemetry 收集器发送的日志，请转到 Signoz → Logs → Logs Explorer。在日志资源管理器中，你可以使用标签 `app=nginx` 进行日志过滤，如下图所示：

![](https://signoz.io/img/blog/2023/12/nginx_logs.webp)

*在这个界面中，你可以轻松可视化日志的数量以及实际的日志行。*

## 参考：由 OpenTelemetry 收集的 NGINX 指标

| 指标名称                     | 描述                              | 类型  |
| ---------------------------- | --------------------------------- | ----- |
| nginx_requests               | 收到的请求数总计                  | 总和  |
| nginx_connections_accepted  | 接受的连接总数                    | 总和  |
| nginx_connections_current    | 当前活动连接总数                  | 总和  |
| nginx_connections_handled    | 成功处理的连接总数                | 总和  |

## 结论

在本教程中，你安装了一个 OpenTelemetry 收集器，用于收集 Nginx 指标和日志，并将收集的数据发送到 SigNoz 进行监控和警报。

访问我们的[完整指南](https://signoz.io/blog/opentelemetry-collector-complete-guide/)，了解有关 OpenTelemetry 收集器的更多信息。OpenTelemetry 悄悄地成为开源可观测性的世界标准，通过使用它，你可以获得统一的遥测信号标准、没有供应商锁定等优势。

SigNoz 是一个开源的 [OpenTelemetry-native APM](https://signoz.io/blog/opentelemetry-apm/)，可用作满足所有可观测性需求的单一后端。

## 进一步阅读

[OpenTelemetry Collector 的完整指南](https://signoz.io/blog/opentelemetry-collector-complete-guide/)

[一个 OpenTelemetry-native APM](https://signoz.io/blog/opentelemetry-apm/)