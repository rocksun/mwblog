<!--
title: OpenTelemetry 揭秘：Kubernetes 上的跟踪、指标与日志实践
cover: https://cdn.thenewstack.io/media/2025/10/c9f74680-how-otel_works-metrics-logs-traces-kubernetes-scaled.jpg
summary: 本文探讨Kubernetes平台工程，重点介绍OpenTelemetry在分布式系统可观测性中的应用（指标、日志、跟踪），并强调应用安全、OAuth2、SSO身份管理。建议早期将OTel与身份管理融入骨架系统，以提升效率和安全性。
-->

本文探讨Kubernetes平台工程，重点介绍OpenTelemetry在分布式系统可观测性中的应用（指标、日志、跟踪），并强调应用安全、OAuth2、SSO身份管理。建议早期将OTel与身份管理融入骨架系统，以提升效率和安全性。

> 译自：[How OpenTelemetry Works: Tracing, Metrics and Logs on Kubernetes](https://thenewstack.io/how-opentelemetry-works-tracing-metrics-and-logs-on-kubernetes/)
> 
> 作者：Mauricio Salatino

*本节摘自 Manning 出版社的 [Platform Engineering on Kubernetes](https://chronosphere.io/resource/platform-engineering-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS) 一书的第一章，内容包括：介绍 Kubernetes 环境，通过一条命令安装示例会议应用，验证健康状况并学习核心原语——部署 (deployments)、副本集 (ReplicaSets)、服务 (services) 和服务发现 (service discovery)——同时应对零停机、弹性、状态/数据一致性、安全/身份以及理解应用程序行为等实际问题。要阅读完整章节，您可以[下载该书](https://chronosphere.io/resource/platform-engineering-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS)。*

---

分布式系统是复杂的庞然大物，从第一天起就充分理解它们如何工作，可以在问题出现时帮助您节省时间。这促使监控、跟踪和遥测社区努力[开发有助于解释](https://www.youtube.com/watch?v=4iBU7YpG0Dw&utm_source=sponsored-content&utm_id=TNS)系统在任何给定时刻如何工作的解决方案。

[OpenTelemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide) 社区与 Kubernetes 一同发展，现在可以提供您监控服务运行所需的大部分工具。正如[其官网](https://opentelemetry.io/)所述：“您可以使用它来检测、生成、收集和导出遥测数据（指标、日志和跟踪），以便进行分析，从而了解您的软件性能和行为。”

## 指标、日志和跟踪

图 1 显示了一个常见用例，其中服务将[指标、跟踪和日志推送到一个集中位置](https://dev.to/siddhantkcode/the-mechanics-of-distributed-tracing-in-opentelemetry-1ohk)，该位置存储和聚合信息，以便可以在仪表板中显示或供其他工具使用。

[![Fig. 1. Aggregating observability from all services in a single place reduces the cognitive load on the teams responsible for keeping the application up and running.](https://cdn.thenewstack.io/media/2025/10/0d0b88b1-aggregating-observability_fig1.png)](https://cdn.thenewstack.io/media/2025/10/0d0b88b1-aggregating-observability_fig1.png)

*图 1. 将所有服务的可观测性聚合到一处可以减少负责保持应用程序正常运行的团队的认知负担。(来源：《Kubernetes平台工程》)*

## Kubernetes 上的 OpenTelemetry：平台工程师的核心概念

值得注意的是，OpenTelemetry 关注您软件的行为和性能，因为它们会影响您的用户及其用户体验。从行为角度来看，您希望确保应用程序正在执行其应有的功能。因此，您需要了解哪些服务正在调用哪些其他服务或基础设施来执行任务。

使用 Prometheus 和 Grafana 使我们能够查看服务遥测数据并构建特定领域仪表板，以突出显示某些应用程序级别的指标（例如，一段时间内已批准或已拒绝的会议提案数量，如图 2 所示）。

[![Fig. 2. Monitoring telemetry data with Prometheus and Grafana.](https://cdn.thenewstack.io/media/2025/10/40b6f656-monitoring-telemetry_fig2.png)](https://cdn.thenewstack.io/media/2025/10/40b6f656-monitoring-telemetry_fig2.png)

*图 2. 使用 Prometheus 和 Grafana 监控遥测数据。(来源：《Kubernetes平台工程》)*

从性能角度来看，您需要确保服务遵守其服务水平协议 (SLAs)，这意味着它们能够及时响应请求。如果您的某个服务出现异常行为并花费比平时更多的时间，您会希望知道。

## OpenTelemetry 收集器：摄取、处理和导出模式

[对于跟踪](https://chronosphere.io/platform/distributed-tracing/?utm_source=sponsored-content&utm_id=TNS)，您必须修改服务以了解内部操作及其性能。OpenTelemetry 提供大多数语言的即插即用检测库，以将服务指标和跟踪外部化。

图 3 显示了 OpenTelemetry 架构，包括 [OpenTelemetry 收集器](https://docs.chronosphere.io/ingest/metrics-traces/otel/otel-ingest?utm_source=sponsored-content&utm_id=TNS)从每个应用程序代理以及共享基础设施组件接收信息。

[![Fig. 3. OpenTelemetry architecture and library (Source: https://opentelemetry.io/docs/)](https://cdn.thenewstack.io/media/2025/10/4627f7a7-otel-architecture_fig3.png)](https://cdn.thenewstack.io/media/2025/10/4627f7a7-otel-architecture_fig3.png)

*图 3. OpenTelemetry 架构和库。(来源：OpenTelemetry docs.)*

如果您正在创建[一个骨架系统](https://www.youtube.com/watch?v=EY13z1XFVmg&t=2s)，请确保其中内置了 OpenTelemetry。如果您将监控推迟到项目的后期阶段，那就太晚了——事情会出错，找出责任方将花费太多时间。

### 应用程序安全和身份管理

如果您曾经构建过 Web 应用程序，您就会知道提供身份管理（用户账户和用户身份）以及身份验证和授权是一项相当大的工作。破坏任何应用程序（云原生或非云原生）的一种简单方法是执行您不应该执行的操作，例如（使用上面会议提案的例子）删除所有提出的演示文稿，除非您是会议组织者。

### 分布式系统中的身份传播和边缘的 OAuth2

在分布式系统中，身份传播变得具有挑战性，因为授权和用户身份必须跨不同服务传播。在分布式架构中，通常会有一个代表用户生成请求的组件，而不是将所有服务直接暴露给用户进行交互。

在我们的示例中，人们提交演示提案的前端服务就是这个组件。大多数情况下，您可以使用这个面向外部的组件作为外部服务和内部服务之间的屏障。因此，通常会配置前端服务，使其使用 OAuth2 协议连接到授权和身份验证提供商。

下图显示了前端服务与身份管理服务进行交互，身份管理服务负责连接身份提供商（例如 Google、GitHub、您的内部 LDAP 服务器）以验证用户凭据，并提供角色或组成员身份，这些角色或组成员身份定义了用户可以在不同服务中执行和不能执行的操作。前端服务处理登录流程（身份验证和授权），但一旦完成，只有上下文会传播到后端服务。

[![Fig. 4. Identity management: The Role/Group is propagated to the backend services.](https://cdn.thenewstack.io/media/2025/10/661990a1-identity-management_fig4.png)](https://cdn.thenewstack.io/media/2025/10/661990a1-identity-management_fig4.png)

*图 4. 身份管理：角色/组传播到后端服务。(来源：《Kubernetes平台工程》)*

### 隐私、社交登录和 SSO/身份提供商

一个不处理用户或其数据的应用程序非常适合遵守 GDPR 等法规。但您可能希望允许用户使用其社交媒体账户登录应用程序，而无需创建单独的账户。这通常称为社交登录。

一些流行的解决方案，如 [Keycloak](https://www.keycloak.org/) 和 [Zitadel](https://zitadel.com/opensource)，将 [OAuth2 和身份管理](https://blog.gravatar.com/2024/05/10/oauth-2-0-simplified-unraveling-authorization-protocols/)结合在一起。这些开源项目为单点登录 (SSO) 解决方案和高级身份管理提供了一站式服务。如果您不想在基础设施中安装和维护 SSO 和身份管理组件，Zitadel 还提供托管服务供您使用。

跟踪和监控也是如此。在骨架系统中规划用户（包括 SSO 和身份管理）将促使您思考“谁能做什么”的具体细节，从而进一步完善您的用例。

## 了解更多

将 OTel 融入您的 Kubernetes“骨架系统”，您就打下了基础，可以在呼叫器响起之前快速发现问题、验证 SLO 并缩短平均解决时间 (MTTR)。

如果您想要端到端的操作手册，包括部署到 Kubernetes 集群、CI/CD、收集器模式、身份、交付管道和多云基础设施，请[下载完整的 Manning 电子书](https://chronosphere.io/resource/platform-engineering-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS)并继续构建。