# Docker 中运行 OpenTelemetry

翻译自 [Run OpenTelemetry on Docker](https://thenewstack.io/run-opentelemetry-on-docker/) 。 这是为新一代可观测性工具的储备知识。

OpenTelemetry 项目已创建了演示服务，以帮助云原生社区成员更好地理解云原生开发实践。

[OpenTelemetry](https://opentelemetry.io/) 项目提供了供应商中立的集成点，帮助组织获取现代可观测性工具所需的原始材料——"遥测(telemetry)"，并在集成时最小化投入。

但对于那些使用他们喜爱的可观测性工具但并不完全了解它如何帮助他们的人来说，OpenTelemetry 意味着什么？ OpenTelemetry 对于那些对 Kubernetes （过去几年大多数 KubeCon 与会者）和刚开始使用可观测性的人来说可能有什么相关性？

OpenTelemetry 项目创建了 demo 服务，以帮助云原生社区成员更好地理解云原生开发实践，并测试 OpenTelemetry 、 [Kubernetes](https://thenewstack.io/kubernetes/) 、可观测性软件、[Docker](https://thenewstack.io/webassembly/docker-needs-to-get-up-to-speed-for-webassembly/) 等容器环境。

在 DevOps 历史的这个关键时刻，关于开发人员和运维团队可观测性的热度很高，最近，人们开始关注如何通过单一界面将不同的可观测性解决方案结合起来，而在这方面， OpenTelemetry 已经成为一个关键的标准。

## 学习曲线

尽管可观测性和 OpenTelemetry 在概念上很简单，但它们需要一定的学习曲线才能使用。为此， OpenTelemetry 项目发布了一个 demo 版本来帮助用户。项目的创建者表示，这个 demo 版本旨在更好地理解云原生开发实践，并测试 OpenTelemetry、Kubernetes、可观测性软件等等。

[OpenTelemetry Demo v1.0](https://github.com/open-telemetry/opentelemetry-demo/tree/v1.0.0) 已在 GitHub 和 https://opentelemetry.io/blog/2022/announcing-opentelemetry-demo-release/OpenTelemetry 网站上发布。这个演示版帮助学习如何向应用程序添加 instrumentation 来收集指标、日志和跟踪以实现可观测性。对于像 Prometheus 和 Jaeger 这样的开源项目，有详细的说明，用于 Kubernetes 和分布式跟踪。演示还展示了如何使用 Grafana 等工具创建仪表板。演示还扩展到创建故障和使用 OpenTelemetry 数据进行故障排除和修复的场景。演示版专为初学者或中级用户设计，可以在大约五分钟内在 Docker 或 Kubernetes 上设置运行。

OpenTelemetry demo 项目团队传达的目标是：

* 提供一个真实的分布式系统示例，可用于演示 OpenTelemetry 的 instrumentation 和可观测性。
* 为供应商、工具作者和其他人构建一个基础，以扩展和展示他们的 OpenTelemetry 集成。
* 为 OpenTelemetry 贡献者创建一个实际示例，用于测试 API、SDK 和其他组件或增强功能的新版本。

## OpenTelemetry 和 Docker

在本教程中，我们将看看如何在 Docker 环境中运行 OpenTelemetry demo 。让我们开始吧。

先决条件是：

* Docker
* [Docker Compose](https://docs.docker.com/compose/install/#install-compose) v2.0.0
* 4 GB的RAM

需要注意的是，如果你在 Windows 上运行 Docker ，你需要确保已经激活了管理员权限，在 Microsoft PowerShell 中部署 OpenTelemetry demo。

首先克隆存储库：

![](https://cdn.thenewstack.io/media/2023/06/18f49bce-capture-decran-2023-03-22-170646-1024x400.png)

![](https://cdn.thenewstack.io/media/2023/06/0c1aca67-opentelcloned.png)

切换到克隆的文件夹：

![](https://cdn.thenewstack.io/media/2023/06/eb34804a-capture-decran-2023-06-05-165859.png)

运行 Docker Compose（--no-build） 并启动演示：

![](https://cdn.thenewstack.io/media/2023/06/8e4488bf-no-build.png)

如果你使用的是 Windows ，打开 Docker Desktop ，你应该在仪表盘上看到准备就绪的 OpenTelemetry 容器：

![](https://cdn.thenewstack.io/media/2023/06/67b44feb-go-to-docker-1024x249.png)

访问 OpenTelemetry-Demo-Main ，实时查看演示的指标数据：

![](https://cdn.thenewstack.io/media/2023/06/6cbec6f5-start-collecting-data-1024x482.png)

至此为止。现在可以开始享受乐趣了！

在 Docker 上运行演示只是一个开始，当然还有许多可能性可以通过演示来做更多事情，这可能会成为未来教程的主题。

其中包括设置 Astronomy Shop 电子商务演示应用程序，该应用程序被项目维护者描述为云原生开发人员可能负责构建和维护的应用程序示例:

![](https://cdn.thenewstack.io/media/2023/06/72ac8594-opentelemetryappstore.png)

![](https://cdn.thenewstack.io/media/2023/06/0748a597-opentelemetryappstore2.png)

有几个为电子商务应用程序预先构建的仪表盘可用，例如用于 Grafana 的仪表板，用于跟踪每个端点的延迟指标：

![](https://cdn.thenewstack.io/media/2023/06/a088eee2-grafana-dashboard-for-span-metrics-1024x492.png)

## 功能标志

[功能标志](https://thenewstack.io/what-are-the-next-steps-for-feature-flags/)，例如 `recommendationCache` 功能标志，将在代码中引发故障，并可以使用 Grafana 或 Jaeger 的面板进行监控（此处使用 Jaeger ）：

构建镜像并启动容器后，可以访问以下选项之一：

* Webstore: http://localhost:8080/
* Grafana: http://localhost:8080/grafana/
* Feature Flags UI: http://localhost:8080/feature/
* Load Generator UI: http://localhost:8080/loadgen/
* Jaeger UI: http://localhost:8080/jaeger/ui/

## 任重道远

这个 OpenTelemetry demo 项目已经走了很长的路。当然，可能存在一些错误，这也是为什么 GitHub 存在的一部分原因，你可以帮助这个项目变得更好。演示的 [GitHub 页面](https://github.com/open-telemetry/opentelemetry-demo)还提供了一些入门资源。

在将来的教程中，请密切关注如何启动 Astronomy Shop 电子商务演示应用程序，并通过 Grafana 面板查看 OpenTelemetry 提供的所有精彩指标的步骤。