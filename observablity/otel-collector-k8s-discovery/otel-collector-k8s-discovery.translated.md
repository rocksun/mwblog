# 基于 Kubernetes 注解的 OpenTelemetry Collector 服务发现

在容器和[Kubernetes](https://kubernetes.io/)的世界中，可观测性至关重要。用户需要随时了解其工作负载的状态。换句话说，他们需要对移动对象进行可观测性监控。

这就是[OpenTelemetry Collector](/docs/collector/)及其[接收器创建器](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.117.0/receiver/receivercreator)组件发挥作用的地方。用户可以采用自助服务的方式设置相当复杂的监控场景，遵循集群级别的最小权限原则。

自助服务方法很棒，但它实际上能实现多少自助服务呢？在这篇博文中，我们将探讨 Collector 的一个新添加的功能，该功能使动态工作负载发现更加容易，为管理员和用户提供无缝的体验。

## 容器和 Pod 的自动发现

在容器和 Pod 上运行的应用程序成为监控系统的移动目标。通过自动发现，监控代理（如 Collector）可以跟踪容器和 Pod 级别的更改并动态调整监控配置。

如今，Collector（特别是接收器创建器）可以提供这样的体验。使用接收器创建器，可观测性用户可以定义依赖于环境条件的配置“模板”。例如，作为可观测性工程师，您可以将 Collector 配置为在集群上部署 NGINX Pod 时启用[NGINX 接收器](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.117.0/receiver/nginxreceiver)。以下配置可以实现此目的：

```yaml
receivers:
  receiver_creator:
    watch_observers: [k8s_observer]
  receivers:
    nginx:
      rule: type == "port" && port == 80 && pod.name matches "(?i)nginx"
      config:
        endpoint: 'http://`endpoint`/nginx_status'
        collection_interval: '15s'
```

当通过 Kubernetes API 发现一个 Pod 公开了端口 `80`（NGINX 的已知端口）并且其名称与 `nginx` 关键字匹配时，将启用之前的配置。

这很好，作为管理可观测性解决方案的 SRE 或平台工程师，您可以依靠它来满足用户对监控 NGINX 工作负载的需求。但是，如果另一个团队想要监控不同类型的负载，例如 Apache 服务器，会发生什么情况？他们需要通知您的团队，您需要使用新的条件配置块更新配置，将其经过拉取请求和审查流程，最后进行部署。此部署需要 Collector 实例重新启动才能使新配置生效。虽然此过程对于某些团队来说可能不是什么大问题，但肯定有改进的空间。

那么，如果作为 Collector 用户，您可以简单地启用自动发现，然后让您的集群用户通过正确地为其 Pod 添加注释来告诉 Collector 如何监控其工作负载呢？这听起来很棒，而且实际上并不是什么新鲜事物。OpenTelemetry 已经通过[Kubernetes 运算符](/docs/platforms/kubernetes/operator/automatic/)支持自动检测，允许用户只需为其 Pod 添加注释即可自动检测其应用程序。此外，这是可观测性行业中的其他监控代理已经支持的功能，用户也熟悉它。

所有这些动力促使 OpenTelemetry 社区([GitHub issue](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/17418))为 Collector 创建了类似的功能。我们很高兴地分享，基于 Kubernetes 注解的自动发现现在已在 Collector 中得到支持([GitHub issue](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/34427))！

## 解决方案

该解决方案建立在[Kubernetes 观察器](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.117.0/extension/observer/k8sobserver)和[接收器创建器](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.117.0/receiver/receivercreator)提供的现有功能之上。

K8s 观察器会通知接收器创建器 K8s 集群中出现的对象，并提供有关这些对象的所有信息。除了 K8s 对象元数据外，观察器还提供有关 Collector 可以连接到的已发现端点的信息。这意味着每个已发现的端点都可能被特定的抓取接收器用来获取指标数据。

每个抓取接收器都有一个默认配置，只有一个必需字段：`endpoint`。鉴于端点信息由 Kubernetes 观察器提供，用户唯一需要明确提供的信息是应该使用哪个接收器/抓取器从已发现的端点抓取数据。
这些信息可以在 Collector 上配置，但如前所述，这很不方便。定义哪个接收器可以用来从特定 Pod 抓取遥测数据的更方便的地方是 Pod 本身。Pod 的注释是放置此类细节的自然位置。鉴于接收器创建者可以访问这些注释，它可以使用接收器的默认配置和已发现的端点来实例化正确的接收器。

以下注释指示接收器创建者，此特定 Pod 运行 NGINX，并且可以使用[NGINX 接收器](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.117.0/receiver/nginxreceiver)从中抓取指标：

```
io.opentelemetry.discovery.metrics/scraper: nginx
```

除此之外，需要使用以下注释显式启用 Pod 上的发现：

```
io.opentelemetry.discovery.metrics/enabled: 'true'
```

在某些情况下，默认接收器的配置不适合连接到特定 Pod。在这种情况下，可以将自定义配置定义为另一个注释的一部分：

```
io.opentelemetry.discovery.metrics/config: |
endpoint: "http://`endpoint`/nginx_status"
collection_interval: '20s'
initial_delay: '20s'
read_buffer_size: '10'
```

需要提到的是，注释中定义的配置不能将接收器创建者指向另一个 Pod。Collector 将拒绝此类配置。

除了指标抓取之外，基于注释的发现还支持使用 filelog 接收器进行日志收集。可以使用以下注释启用特定 Pod 上的日志收集：

```
io.opentelemetry.discovery.logs/enabled: 'true'
```

与指标类似，可以提供以下形式的可选配置：

```
io.opentelemetry.discovery.logs/config: |
max_log_size: "2MiB"
operators:
- type: container
  id: container-parser
- type: regex_parser
  regex: '^(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<sev>[A-Z]*) (?P<msg>.*)$'
```

如果需要更改 filelog 接收器操作符的集合，则必须重新定义完整的列表（包括默认的容器解析器），因为在合并到默认配置结构时，列表配置字段将被完全替换。

必须通过添加以下配置字段在接收器创建者中显式启用发现功能：

```
receivers:
  receiver_creator:
    watch_observers: [k8s_observer]
    discovery:
      enabled: true
```

## 试试看

如果您是 Kubernetes 上的 OpenTelemetry Collector 用户，并且您觉得这个新功能很有趣，请参阅[接收器创建者配置](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.117.0/receiver/receivercreator/README.md#generate-receiver-configurations-from-provided-hints) 部分以了解更多信息。

试试看，并通过[CNCF Slack 工作区](https://slack.cncf.io/)的 `#otel-collector` 频道告诉我们您的想法。