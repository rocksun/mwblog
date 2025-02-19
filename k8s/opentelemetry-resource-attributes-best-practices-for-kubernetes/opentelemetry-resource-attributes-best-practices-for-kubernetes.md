
<!--
title: OpenTelemetry资源属性：Kubernetes最佳实践
cover: ./cover.png
-->

> 译自：[OpenTelemetry resource attributes: Best practices for Kubernetes](https://www.dash0.com/blog/opentelemetry-resource-attributes-best-practices-for-kubernetes)
> 作者：Michele Mancioppi

关于在 Kubernetes 上运行的应用程序拥有出色 OpenTelemetry 资源元数据的全部知识。

[OpenTelemetry 资源](https://www.dash0.com/faq/what-are-opentelemetry-resources) 用于记录遥测数据描述的系统，它们往往是能够从中获得洞察的遥测数据与“仅仅是数据”之间的区别。使用 OpenTelemetry 对服务进行 instrumentation 时，遵守语义约定可确保跨系统的一致、准确和有意义的遥测数据。

各种属性允许您描述 Kubernetes 集群中哪个工作负载正在发出哪些遥测数据。[Kubernetes 资源语义约定](https://opentelemetry.io/docs/specs/semconv/resource/k8s/) 指定了 `k8s.*.uid` 和 `k8s.*.name` 属性对，例如 pod (`k8s.pod.uid` 和 `k8s.pod.name`)，以及所有“更高级别”构造的工作负载（在 Kubernetes 中也称为“资源”，但我们不想混淆这两个术语），例如 deployment (`k8s.deployment.uid` 和 `k8s.deployment.name`)、daemonset (`k8s.daemonset.uid` 和 `k8s.daemonset.name`) 等等。

尽管属性定义明确，但并非所有正确的 Kubernetes 相关元数据都完全可以直接附加到您的遥测数据。

## 一切始于 k8s.pod.uid

在描述来自 Kubernetes 上工作负载的遥测数据的所有资源属性中，`k8s.pod.uid` 绝对是最重要的：通过它，您可以通过将遥测数据通过运行在同一集群内的 OpenTelemetry 收集器的 [k8sattributeprocessor 组件](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/k8sattributesprocessor/README.md) 传输，添加大多数其他 Kubernetes 相关元数据。

`k8sattributeprocessor` 使用从 Kubernetes API 获取的数据“填充”空白，并使用正确的工具，您可以轻松地跨所有类型的聚合过滤和分组遥测数据。`k8sattributeprocessor` 的存在实际上填补了遥测元数据中的一个非常重要的空白：在您的容器内运行的 OpenTelemetry SDK 几乎无法访问有关 *为什么* 它们周围的 pod 正在运行的元数据。除非您专门将其添加到 pod 中（例如，使用环境变量），否则它们将不知道哪个 daemonset 调度了 pod，或者哪个 deployment 的哪个 replicaset。

事实上，如果没有您的额外帮助，例如通过环境变量（自己设置值，或通过 Kubernetes 的 [Downward API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/) 将 pod uid、pod 名称和命名空间名称添加到环境中），容器中的 OpenTelemetry SDK 几乎只能知道 pod uid（尽管涉及到解析 [cgroup](https://en.wikipedia.org/wiki/Cgroups) 元数据的非常深奥的技巧，例如，请参见 Dash0 的 OpenTelemetry for Node.js 发行版中的此 [资源检测器](https://github.com/dash0hq/opentelemetry-js-distribution/blob/main/src/detectors/node/opentelemetry-resource-detector-kubernetes-pod/index.ts)）和 pod 名称（通过网络主机名）。不幸的是，在撰写本文时，OpenTelemetry SDK 甚至没有一致地实现这些功能（例如，参见 [此问题](https://github.com/open-telemetry/opentelemetry-python-contrib/issues/1474)）。

因此，请确保通过 Downward API 和“[相关的环境变量](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/)”在您的 Kubernetes 清单文件中正确可靠地设置 `k8s.pod.uid`：

```yaml
env:
  - name: K8S_POD_UID
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.uid
  - name: OTEL_RESOURCE_ATTRIBUTES
    value: k8s.pod.uid=$(K8S_POD_UID), ...
```

*Kubernetes pod spec 模板代码片段，展示如何将 Downward API 与 OTEL_RESOURCE_ATTRIBUTES 环境变量一起使用来设置 k8s.pod.uid 资源属性。*

顺便说一句，`k8sattributeprocessor` 能够通过唯一的 pod ip 识别哪个 pod 正在向其发送遥测数据（参见“[关联”配置](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/k8sattributesprocessor/README.md#configuration)）：OpenTelemetry 收集器中的处理器匹配发送遥测数据的 TCP 连接“另一端”的 IP 地址，并且由于 Kubernetes 集群中的每个 pod 都有一个唯一的 IP 地址分配给它，因此它可以弄清楚它来自哪个 pod。*大多数情况下……*

这里有一个需要注意的地方：如果使用服务网格或一些不太常见的网络设置，则基于 IP 地址检测 pod 的方法已知不可靠。（别问我们是怎么知道的。排查这个问题一点也不好玩。）因此，安全第一：确保您的遥测数据已使用 `k8s.pod.uid` 进行注释。
如果您同意通过集群内的 OpenTelemetry Collector 代理遥测数据，则可以使用[类似这样的配置](https://www.otelbin.io/s/249772c6c88ab31e77c168af6131df0248902bbf)来填充本文其余部分中提到的大部分资源属性。

## 很高兴认识你，希望你能猜到 Pod 的名字

Pod UID 在所有工作负载中都是有效的唯一标识。（以及所有 Kubernetes 工作负载，任何地方，任何时间。）但是，长长的随机字符字符串并不是我们人类擅长记忆或在列表中搜索的东西。

因此，与设置 `k8s.pod.uid` 资源属性的方式类似，我们可以设置 `k8s.pod.name`：

```yaml
# pod spec yaml
env:
  - name: K8S_POD_NAME
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.name
  - name: OTEL_RESOURCE_ATTRIBUTES
    value: k8s.pod.name=$(K8S_POD_NAME), ...
```

*Kubernetes pod spec 模板代码片段，展示如何使用 Downward API 和 OTEL_RESOURCE_ATTRIBUTES 环境变量来设置 k8s.pod.name 资源属性。*


## 插曲：为什么它们被称为 Pod？

你知道 Kubernetes pod（即共享本地网络和其他资源，如 CPU 和内存分配以及卷的一个或多个容器）之所以这样命名是因为：

1. “pod” 是鲸鱼群体的统称
2. Docker（Kubernetes 最初的容器运行时）的标志是一只鲸鱼
现在你知道啦！

## 如果您有sidecar，您可能需要k8s.container.name

如果您的 Pod 包含多个容器，您真的需要知道哪个容器出现了问题。通常，Kubernetes 上的应用程序只有一个“主”容器，运行您的应用程序，并且可能有一个或多个“sidecar”（即包含辅助进程的容器，例如日志收集器或服务网格代理）。`k8sattributeprocessor`（参见上一节）无法区分容器（您在同一 Pod 中的所有容器共享相同的 IP 地址和 Pod UID，以及其他内容），因此您应该自己设置 `k8s.container.name`。这可能有点费力，因为您无法像我们对 `k8s.pod.uid` 所做的那样使用 Downward API 以通用方式执行此操作，但最终只需向 `OTEL_RESOURCE_ATTRIBUTES` 添加另一个条目即可：

```yaml
0123
env:
  - name: OTEL_RESOURCE_ATTRIBUTES
    value: k8s.container.name=<my_container_name>, ...
```

*Kubernetes pod spec 模板代码片段，展示如何使用 OTEL_RESOURCE_ATTRIBUTES 环境变量来设置 k8s.container.name 资源属性。确保将其设置为与容器名称相同的 value!*

请注意，`k8s.container.name` 可能冗余：`container.name` 属性应该包含相同的数据，并且大多数 OpenTelemetry SDK 中都有检测器（例如，参见[Node.js](http://nodejs.org/)），它们可以通过解析例如 `cgroup` 元数据来为您收集 `container.name`（[cgroups](https://en.wikipedia.org/wiki/Cgroups) 是容器的基础 Linux 功能之一）。但是，并非总是能够将检测器添加到您的容器化应用程序中，尤其是在您使用来自第三方的 sidecar 时。但是，如果它们支持 `OTEL_RESOURCE_ATTRIBUTES` 环境变量，则可以通过进程环境来填充资源属性中的空白。

## 名称还不够，您需要 UID

与您在大多数应用程序中可能拥有 `frontend` 服务（`service.name=frontend`）一样，该服务很可能由 `frontend` 部署（`k8s.deployment.name=frontend`）提供支持。Kubernetes 中的名称仅对同一 Kubernetes 命名空间内相同类型的资源（例如，部署）唯一。如果您想避免混淆并简化您的数据聚合工作，请不仅设置 `k8s.*.name`，还要设置 `k8s.*.uid`，并使用 UID 进行分组。

阅读上一段后，您可能想知道：

“部署名称在命名空间内是唯一的，命名空间名称在集群内是唯一的。那么，为什么我还需要唯一的标识符呢？”

如果您只在一个集群中部署软件，则此逻辑有效。但这很少见。在开发、测试和各种生产集群（这是一种相当常见的布局类型）之间，大多数组织同时在 *许多* Kubernetes 集群上运行相同的软件。而且，更复杂的是，区分 Kubernetes 集群比预期的要难（参见下一节）。

## 这是哪个集群？

标识符的乐趣还没有结束。现在让我们谈谈一些*实际上不存在*的标识符。具体来说，是特定 Kubernetes 集群的标识符。在大多数 Kubernetes 设置中，它实际上并不存在。换句话说，*Kubernetes 集群没有自己的身份概念*！

你肯定为你的集群命名了，但是你在 Kubernetes 集群管理工具中定义的名称“prod-eu-awesomesauce”更多的是你如何调用 `kubectl` 中的配置文件来连接到该集群，而不是你可以在集群本身内部找到的元数据！（你的经验可能会因具体的设置和 Kubernetes 版本而有所不同；但总的来说，情况就是这样。）因此，你应该使用 OpenTelemetry 收集器的 [resourceprocessor](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/resourceprocessor) 来注入以下值：

`k8s.cluster.name`
如下所示：

```
processors:
  resource:
    attributes:
    - key: k8s.cluster.name
      value: "prod-eu-awesomesauce"
      action: upsert
```

*一段 OpenTelemetry 收集器配置代码片段，用于将 k8s.cluster.name 资源属性添加到所有通过的遥测数据中。*

此外，大多数 Kubernetes `k8s.*.name` 属性都有匹配的 `k8s.*.uid` 属性，`k8s.cluster.name` 也有一个匹配项 `k8s.cluster.uid`。在这种情况下，常见的做法是使用 `kube-system` 命名空间的 uid 作为 `k8s.cluster.uid` 的值，而 `kube-system` 命名空间几乎是你保证会在你见过的每个 Kubernetes 集群中都能找到的唯一命名空间（因为它默认情况下承载控制平面组件）。

## 别忘了节点！

`k8s.node.name` 属性及其使用频率较低的 `k8s.node.uid` 属性在调查由于资源供应不足（同一节点上的 Pod 争夺 CPU 或内存等资源）或 [节点压力驱逐](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/) 造成的性能问题时非常有用。唯一的例外是你在 AWS EKS 上使用 Fargate 运行时，从 Kubernetes 的角度来看，每个 Pod 都运行在专用节点上。

如果你已经设置了 `k8sattributeprocessor`，以便它可以向你的遥测数据添加资源属性，它也可以为你处理 `k8s.node.name`。否则，使用 Kubernetes 的向下 API 和“[依赖环境变量](https://kubernetes.io/docs/tasks/inject-data-application/define-interdependent-environment-variables/)”设置 `k8s.node.name` 属性非常简单：

```yaml
env:
...
  - name: K8S_NODE_NAME
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: spec.nodeName
  - name: OTEL_RESOURCE_ATTRIBUTES
    value: k8s.node.name=$(K8S_NODE_NAME)
```

*Kubernetes Pod规范模板代码片段，展示如何将向下 API 与 OTEL_RESOURCE_ATTRIBUTES 环境变量一起使用来设置 k8s.node.name 资源属性。*

## 结论

资源属性是使你的遥测数据有用的关键要素。在这篇博文中，我们研究了 Kubernetes 的 OpenTelemetry 资源语义约定，以及如何确保始终知道哪个集群的哪个工作负载正在发送错误。

在这篇文章中，我们坚持你的遥测数据应该具有的基本 Kubernetes 元数据。当然，关于 OpenTelemetry 语义约定还有很多话要说，即使只是关于 Kubernetes 上的资源。例如，你将在[Kubernetes 资源语义约定](https://opentelemetry.io/docs/specs/semconv/resource/k8s/)中找到更多指定的资源属性。此外，还有关于[Kubernetes 指标](https://opentelemetry.io/docs/specs/semconv/system/k8s-metrics/)的语义约定，在撰写本文时，这些约定处于实验状态（这意味着：约定未声明稳定，因此它可能仍然会以向后不兼容的方式发生变化），并且基于 OpenTelemetry 收集器知道如何使用各种接收器（如 [k8sclusterreceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/k8sclusterreceiver) 和 [kubeletstatsreceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/receiver/kubeletstatsreceiver) 收集的内容。

顺便说一句，如果你喜欢这篇文章，你可能会喜欢 Ben 的“[十大 OpenTelemetry 收集器组件](https://www.dash0.com/blog/top-10-opentelemetry-collector-components)”博文。它可能会给你提供更多关于如何确保你的资源元数据一流的思路。

如果您想要本文中介绍的资源元数据的全部优势，但又不想为此付出任何努力，不妨试试[Dash0 Operator](https://www.dash0.com/documentation/dash0/dash0-kubernetes-operator)：它是开源的，基于 OpenTelemetry 组件构建，具有明确的观点和类似设备的理念（“它就是能工作™”），并且在底层使用了本文中描述的大多数技术来使您的遥测数据达到最先进的水平，而您无需付出任何努力。