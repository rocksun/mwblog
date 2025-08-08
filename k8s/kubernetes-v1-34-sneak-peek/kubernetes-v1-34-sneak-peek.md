

# Kubernetes v1.34 预览

> 译自：[Kubernetes v1.34 Sneak Peek](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/)
>
> 作者：Agustina Barbetta, Alejandro Josue Leon Bellido, Graziano Casto, Melony Qin, Dipesh Rawat

Kubernetes v1.34 预计将于 2025 年 8 月底发布，此版本不包含任何移除或弃用，但包含大量增强功能，例如 DRA 稳定、用于镜像拉取认证的 ServiceAccount 令牌、Deployment 的 Pod 替换策略、kubelet 和 API Server 的生产就绪追踪等。此外，KYAML 将作为 kubectl 的新输出格式引入，并支持 HPA 可配置容差以进行细粒度的自动扩缩控制。

请注意，此信息反映了 v1.34 开发的当前状态，并且在发布之前可能会发生变化。以下是我们在本周期中最兴奋的一些功能！

## Kubernetes v1.34 的精选增强功能

以下列表重点介绍了一些可能包含在 v1.34 版本中的值得注意的增强功能，
但并非所有计划更改的详尽列表。
这不是承诺，发布内容可能会发生变化。

### DRA 的核心功能趋于稳定

[动态资源分配](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) (DRA) 提供了一种灵活的方式来对 Kubernetes 集群中的 GPU 或自定义硬件等设备进行分类、请求和使用。

自 v1.30 版本以来，DRA 一直基于使用 Kubernetes 核心不透明的*结构化参数*来声明设备。
相关的增强提案 [KEP-4381](https://kep.k8s.io/4381) 从存储卷的动态配置中汲取了灵感。
具有结构化参数的 DRA 依赖于一组支持的 API Kind：ResourceClaim、DeviceClass、ResourceClaimTemplate 以及 `resource.k8s.io` 下的 ResourceSlice API 类型，同时使用新的 `resourceClaims` 字段扩展 Pod 的 `.spec`。

DRA 的核心目标是在 Kubernetes v1.34 中升级到稳定版。

使用 DRA，设备驱动程序和集群管理员定义可供使用的设备类。
工作负载可以从设备请求中的设备类中声明设备。
Kubernetes 将匹配的设备分配给特定的声明，并将相应的 Pod 放置在可以访问已分配设备的节点上。
该框架提供灵活的设备过滤（使用 CEL）、集中的设备分类和简化的 Pod 请求等优点。

一旦此功能升级，`resource.k8s.io/v1` API 将默认可用。

### 用于镜像拉取认证的 ServiceAccount 令牌

用于 `kubelet` 凭证提供程序的 [ServiceAccount](/docs/concepts/security/service-accounts/) 令牌集成很可能达到 Beta 版，并在 Kubernetes v1.34 中默认启用。
这允许 `kubelet` 在从需要身份验证的注册表中拉取容器镜像时使用这些令牌。

该支持已经以 Alpha 版形式存在，并作为 [KEP-4412](https://kep.k8s.io/4412) 的一部分进行跟踪。

现有的 Alpha 集成允许 `kubelet` 使用短期的、自动轮换的 ServiceAccount 令牌（遵循符合 OIDC 的语义）来验证容器镜像注册表的身份。

每个令牌的范围都限定为一个关联的 Pod；整个机制取代了对长期存在的镜像拉取密钥的需求。

采用这种新方法可以降低安全风险，支持工作负载级别的身份，并有助于减少运营开销。
它使镜像拉取身份验证更接近现代的、具有身份感知的良好实践。

### Deployment 的 Pod 替换策略

在更改 [Deployment](/docs/concepts/workloads/controllers/deployment/) 后，终止的 Pod 可能会保持运行相当长的时间，并可能消耗额外的资源。

作为 [KEP-3973](https://kep.k8s.io/3973) 的一部分，`.spec.podReplacementPolicy` 字段将作为 Alpha 版引入到 Deployment 中。

如果你的集群启用了该功能，你将能够选择以下两种策略之一：

`TerminationStarted`
:   一旦旧的 Pod 开始终止，就创建新的 Pod，从而以可能更高的资源消耗为代价加快推出速度。

`TerminationComplete`
:   等待旧的 Pod 完全终止后再创建新的 Pod，从而导致推出速度较慢，但确保了受控的资源消耗。

此功能允许你选择在更新或扩缩期间何时创建新的 Pod，从而使 Deployment 行为更可预测。
这在资源限制严格的集群中或终止周期长的工作负载中工作时很有用。

预计它将作为 Alpha 功能提供，并且可以使用 API 服务器和 kube-controller-manager 中的 `DeploymentPodReplacementPolicy` 和 `DeploymentReplicaSetTerminatingReplicas` 功能门启用。

### 用于 `kubelet` 和 API Server 的生产就绪的追踪

为了解决通过关联断开连接的日志来调试节点级别问题的长期挑战，[KEP-2831](https://kep.k8s.io/2831) 提供了对 `kubelet` 的深入、上下文相关的见解。

此功能使用与供应商无关的 OpenTelemetry 标准来检测关键的 `kubelet` 操作，尤其是其与容器运行时接口 (CRI) 的 gRPC 调用。

它允许运营商可视化事件的整个生命周期（例如：Pod 启动），以查明延迟和错误的来源。它最强大的方面是追踪上下文的传播；`kubelet` 将追踪 ID 与其对容器运行时的请求一起传递，从而使运行时能够链接其自身的 span。

此工作由一个平行的增强功能 [KEP-647](https://kep.k8s.io/647) 补充，该功能将相同的追踪功能引入 Kubernetes API 服务器。

这些增强功能共同提供了更统一的端到端事件视图，简化了从控制平面到节点查明延迟和错误的过程。
这些功能已经通过官方 Kubernetes 发布过程成熟。

[KEP-2831](https://kep.k8s.io/2831) 作为 Alpha 功能在 v1.25 中引入，而 [KEP-647](https://kep.k8s.io/647) 在 v1.22 中作为 Alpha 功能首次亮相。这两个增强功能在 v1.27 版本中一起晋升为 Beta 版。

展望未来，Kubelet 追踪 ([KEP-2831](https://kep.k8s.io/2831)) 和 API Server 追踪 ([KEP-647](https://kep.k8s.io/647)) 现在都计划在即将发布的 v1.34 版本中升级到稳定版。

### 服务的 `PreferSameZone` 和 `PreferSameNode` 流量分配

Kubernetes [Service](/docs/concepts/services-networking/service/) 中的 `spec.trafficDistribution` 字段允许用户表达流量应如何路由到 Service 端点的偏好。

[KEP-3015](https://kep.k8s.io/3015) 弃用了 `PreferClose` 并引入了两个附加值：`PreferSameZone` 和 `PreferSameNode`。
`PreferSameZone` 相当于当前的 `PreferClose`。
`PreferSameNode` 优先将流量发送到与客户端位于同一节点上的端点。

此功能已在 v1.33 中引入，位于 `PreferSameTrafficDistribution` 功能门之后。
它计划在 v1.34 中升级到 Beta 版，其功能门默认启用。

### 支持 KYAML：YAML 的 Kubernetes 方言

KYAML 旨在成为一种更安全且不那么模糊的 YAML 子集，并且是专门为 Kubernetes 设计的。无论你使用哪个版本的 Kubernetes，你都可以使用 KYAML 来编写清单和/或 Helm chart。
你可以编写 KYAML 并将其作为输入传递给**任何**版本的 `kubectl`，因为所有 KYAML 文件也都是有效的 YAML。
对于 kubectl v1.34，我们预计你也可以从 `kubectl` 请求 KYAML 输出（如 `kubectl get -o kyaml …`）。
如果你愿意，你仍然可以请求 JSON 或 YAML 格式的输出。

KYAML 解决了 YAML 和 JSON 的特定挑战。
YAML 的重要空格需要仔细注意缩进和嵌套，而其可选的字符串引号可能会导致意外的类型强制转换（例如：["The Norway Bug"](https://hitchdev.com/strictyaml/why/implicit-typing-removed/))。
同时，JSON 缺少注释支持，并且对尾随逗号和带引号的键有严格的要求。

[KEP-5295](https://kep.k8s.io/5295) 引入了 KYAML，它试图通过以下方式解决最重要的问题：

* 始终用双引号引起来值字符串
* 除非键可能不明确，否则不引用键
* 始终对映射（关联数组）使用 `{}`
* 始终对列表使用 `[]`

这听起来很像 JSON，因为它就是！但与 JSON 不同，KYAML 支持注释，允许尾随逗号，并且不需要带引号的键。

我们希望看到 KYAML 作为 `kubectl` v1.34 的一种新的输出格式引入。
与所有这些功能一样，这些更改都不是 100% 确定的；请关注此空间！

作为一种格式，KYAML 现在并将始终是 **YAML 的严格子集**，确保任何兼容的 YAML 解析器都可以解析 KYAML 文档。
Kubernetes 不要求你提供专门格式化为 KYAML 的输入，并且我们没有计划更改这一点。

### 使用 HPA 可配置容差进行细粒度的自动扩缩控制

[KEP-4951](https://kep.k8s.io/4951) 引入了一项新功能，允许用户在每个 HPA 的基础上配置自动扩缩容差，
从而覆盖默认的集群范围内的 10% 容差设置，该设置通常对于不同的工作负载来说过于粗粒度。
该增强功能在 HPA 的 `spec.behavior.scaleUp` 和 `spec.behavior.scaleDown` 部分添加了一个可选的 `tolerance` 字段，
从而可以为扩容和缩容操作设置不同的容差值，
这尤其有价值，因为扩容响应通常比处理流量激增的缩容速度更关键。

此功能在 Kubernetes v1.33 中以 Alpha 版发布，位于 `HPAConfigurableTolerance` 功能门之后，预计将在 v1.34 中升级到 Beta 版。
此改进有助于解决大规模部署中的扩缩挑战，在这种情况下，对于缩容，
10% 的容差可能意味着留下数百个不必要的 Pod 运行。
使用新的、更灵活的方法将能够针对响应式和保守的扩缩行为进行特定于工作负载的优化。

## 想要了解更多？

新的功能和弃用也会在 Kubernetes 版本说明中公布。
我们将在 [Kubernetes v1.34](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md) 的变更日志中正式宣布该版本的新增功能。

Kubernetes v1.34 版本计划于 **2025 年 8 月 27 日星期三** 发布。请继续关注更新！

## 参与其中

参与 Kubernetes 的最简单方法是加入与你的兴趣相符的众多[特别兴趣小组](https://github.com/kubernetes/community/blob/master/sig-list.md) (SIG) 之一。
有什么想向 Kubernetes 社区广播的内容吗？在我们的每周[社区会议](https://github.com/kubernetes/community/tree/master/communication)上以及通过以下渠道分享你的声音。
感谢你的持续反馈和支持。
