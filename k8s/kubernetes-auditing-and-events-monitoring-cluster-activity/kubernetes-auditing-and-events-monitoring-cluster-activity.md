<!--
title: Kubernetes审计与事件：全面监控集群活动
cover: https://cdn.thenewstack.io/media/2025/12/e5089d49-circuitboard.jpg
summary: Kubernetes日志涵盖容器、集群及应用。容器日志依赖标准输出，集群日志需审计功能。kubernetes_events插件捕获API事件，需安全凭证和RBAC。审计数据应作参考。
-->

Kubernetes日志涵盖容器、集群及应用。容器日志依赖标准输出，集群日志需审计功能。kubernetes_events插件捕获API事件，需安全凭证和RBAC。审计数据应作参考。

> 译自：[Kubernetes Auditing and Events: Monitoring Cluster Activity](https://thenewstack.io/kubernetes-auditing-and-events-monitoring-cluster-activity/)
> 
> 作者：Phil Wilkins

***编者按：**本文摘自 Manning 出版书籍《[Fluent Bit 与 Kubernetes](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)》的第 4 章，该书是一本关于日志、指标和追踪的指南，旨在实现更高效的遥测。本章重点介绍如何使用日志捕获 Kubernetes 应用程序中的事件，以衡量活动、行为和上下文。可在此处[下载](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)完整书籍。*

Kubernetes 从多个角度审视日志和[日志记录](https://thenewstack.io/using-logging-frameworks-for-application-development/)：记录、衡量和追踪容器正在做什么，[更广泛的 Kubernetes 集群正在做什么](https://thenewstack.io/observability-is-a-multicluster-app-developers-best-friend/)（尽管容器和集群可以视为一体），以及容器内的应用程序正在做什么。因此，我们需要考虑如何捕获这些形式的[事件](https://thenewstack.io/understanding-log-events-why-context-is-key/)。

## 理解 Kubernetes 对日志记录的立场

就 Kubernetes 而言，容器运行的应用程序的日志记录是容器运行时的责任。通常，容器会处理标准输出和标准错误。

除了使用[标准输出和标准错误](https://chronosphere.io/learn/dynamic-log-routing-on-kubernetes-labels-fluent-bit/)外，大多数容器运行时都采用了日志驱动（logging driver）的概念，它允许以不同的方式处理捕获到的应用程序日志。除了通常使用日志驱动模型实现标准输出和标准错误之外，其他实现之间的一致性很低。

仅仅处理容器正在做的事情并不能解决集群层面的日志记录问题，例如记录整个集群发生的事情、Pod 的驱逐以及节点的启动和停止。

同样，Kubernetes 不规定特定的解决方案，但提倡在 Sidecar 配置中使用日志代理，或让日志代理在每个节点上运行（作为 DaemonSet 的一部分）。

Kubernetes 有自己的日志库，称为 [klog](https://github.com/kubernetes/klog)，最近已转向采用 [logr](https://github.com/go-logr/logr)。Logr 在日志接口和日志内容输出之间有更强的解耦，因此 logr 可用于创建 klog 和其他输出。

## Kubernetes 审计

除了了解 Kubernetes 生态系统内应用程序的运行情况之外，我们还应该对 Kubernetes 进行审计。

例如，我们可能想找出是谁或什么指令 Kubernetes 驱逐了一个容器。Kubernetes 通过审计功能解决了这种情况，我们可以将其配置为使用 Webhook 与日志后端通信，或将事件以 [JSON Lines 格式](https://jsonlines.org)写入日志文件。

我们不应将此审计与 [Fluent Bit](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd/) 作为插件源所支持的事件功能混淆，正如我们稍后将看到的。通过正确的审计配置，我们可以使用 Fluent Bit 收集此类数据。（有关配置 Kubernetes 审计的更多信息，请参阅 <https://mng.bz/znZA>。）

## Kubernetes 事件输入

Kubernetes 通过其 API 服务器向任何请求者暴露其活动和事件。通过 Kubernetes 事件插件（称为 `kubernetes_events`），我们可以捕获这些事件并将它们放入日志事件管道。您会发现许多属性与 `tail` 插件和基于网络的插件具有相同或相似的名称和用途。

该插件使用 SQLite 数据库，就像我们可以使用 `tail` 一样（由 `db` 属性标识），以避免事件意外地重复进入管道；每次调用 API 服务器时，我们都会获得相同的事件。

由于该过程基于轮询，因此我们有属性来定义秒数或纳秒数（`interval_sec` 或 `interval_nsec` 属性）。

我们需要注意，由于 SQLite 的工作方式限制，我们只能运行一个活动的 Fluent Bit 实例来运行此插件。这种限制并非灾难性的；我们可以依靠 Kubernetes 来监控容器的健康状况。

然而，一个大型集群会有很多事件，因此单个 Fluent Bit 实例需要[足够的资源来跟上 Kubernetes](https://chronosphere.io/learn/kubernetes-cloud-native-app-challenges/)。如果多个 Fluent Bit 实例开始检索事件数据，我们将看到事件重复。

在连接 Kubernetes API 收集事件数据方面，此插件与 Kubernetes 过滤器插件具有一组共同的属性，用于定义服务器 URL、证书位置、TLS 检查、token 和 token 生存时间 (TTL)（`Kube_URL`、`Kube_CA_File`、`Kube_CA_Path`、`tls.debug`、`tls.verify`、`Kube_Token_File`、`Kube_Token_TTL`）。

请参见以下列表：

[![](https://cdn.thenewstack.io/media/2025/12/d40db03d-image2.png)](https://cdn.thenewstack.io/media/2025/12/d40db03d-image2.png)

[![](https://cdn.thenewstack.io/media/2025/12/eeec38da-image1.png)](https://cdn.thenewstack.io/media/2025/12/eeec38da-image1.png)

此插件的配置带来了挑战，特别是：安全地向 Fluent Bit 暴露 Kubernetes token 和证书。假设此 Fluent Bit 部署发生在 [Kubernetes Pod](https://chronosphere.io/learn/what-is-a-kubernetes-pod/) 内，克服此挑战的一个好方法是将文件存储为 Kubernetes Secrets，然后在 Pod 规范中定义一个映射到 Secret 的挂载点。

数据被安全地保存，但我们可以将值映射到任何需要该值的容器。在 Pod 内部，文件被视为正常文件。最好不要通过环境变量提供凭证，因为它们在容器的生命周期内是固定的。因此，如果凭证轮换，配置将失败。

我们应该[谨慎解释 Kubernetes 事件数据](https://chronosphere.io/learn/logging-best-practices/)。正如文档所说，“[事件](https://kubernetes.io/docs/reference/kubernetes-api/cluster-resources/event-v1/)应被视为信息性、尽力而为的补充数据。”

|  |
| --- |
| **注意：** 对于 Kubernetes 过滤器、kubernetes\_events 插件或任何其他直接与 Kubernetes API 交互的方式，必须配置基于角色的访问控制 (RBAC)，以便用于运行这些容器的服务账户拥有从 API 服务器请求数据所需的权限。 |

配置的示例可在 <https://mng.bz/KDGO> 找到。Jay Vyas 和 Chris Love 的“Core Kubernetes”等书籍是了解 RBAC 如何工作的良好指南。

*您刚刚阅读了 Manning 出版书籍《Fluent Bit 与 Kubernetes》的摘录。要了解更多关于 Fluent Bit 和 Kubernetes 的信息，包括 Kubernetes 生态系统的不同部分，请[下载完整书籍](https://chronosphere.io/resource/fluent-bit-with-kubernetes-manning/)。*

## 常见问题

**Kubernetes 审计的目的是什么？** Kubernetes 中的审计使管理员能够跟踪集群中发生了哪些操作、何时发生以及由谁发起，通过配置日志后端或 JSON Lines 文件记录事件，帮助确保安全性和合规性。

**如何配置 Kubernetes 以捕获审计日志？**

Kubernetes 审计日志的设置方法是在 API 服务器上配置审计策略，并指定审计事件应发送到何处，通常是 Webhook 或日志文件；配置必须提供安全的凭证管理，理想情况下是使用挂载到 [Pod](https://chronosphere.io/learn/kubernetes-pod-vs-container/) 中的 Kubernetes Secrets，而不是环境变量。

**Kubernetes 审计日志条目中包含哪些关键字段？**

Kubernetes 审计日志条目包括时间戳、审计 ID、请求阶段、用户信息、动词（执行的操作）、受影响的资源、命名空间、源 IP 和请求统一资源标识符 (URI) 等字段。这些详细信息有助于管理员追踪集群内的活动并诊断安全事件。

**组织应如何保护和解释 Kubernetes 审计数据？**

用于审计日志收集的凭证（例如 token 和证书）应安全地存储为 Secret，并通过 Pod 规范挂载，而不是设置为环境变量，以在凭证轮换期间保持安全。审计事件应被视为信息性、补充数据，而不是用于计费或主要合规性分析。

阅读更多关于 Fluent Bit 的信息：

- [What Is Fluent Bit?](https://thenewstack.io/fluent-bit-core-concepts/)
- [Fluent Bit, a Specialized Event Capture and Distribution Tool](https://thenewstack.io/fluent-bit-a-specialized-event-capture-and-distribution-tool/)
- [How Are OpenTelemetry and Fluent Bit Related?](https://thenewstack.io/how-are-opentelemetry-and-fluent-bit-related/)
- [What Are the Differences Between OTel, Fluent Bit and Fluentd?](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd/)
- [How To Deploy Fluent Bit in a Kubernetes-Native Way](https://thenewstack.io/how-to-deploy-fluent-bit-in-a-kubernetes-native-way/)