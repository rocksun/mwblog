# 一睹 Kubernetes v1.30

**作者：**Amit Dsouza、Frederick Kautz、Kristin Martin、Abigail McCarthy、Natali Vlatko

## 快速浏览：Kubernetes v1.30 中令人兴奋的变更

新年伊始，Kubernetes 也迎来了新版本。我们已完成了一半的发布周期，在 v1.30 中有许多有趣且令人兴奋的增强功能。从 alpha 中的全新功能，到已确立的功能升级到稳定版，再到期待已久的改进，此版本中总有值得大家关注的内容！

在正式发布之前，让我们先睹为快，看看我们在这个周期中最期待的增强功能！

## Kubernetes v1.30 的重大变更

### 动态资源分配的结构化参数 ([KEP-4381](https://kep.k8s.io/4381))

[动态资源分配](/docs/concepts/scheduling-eviction/dynamic-resource-allocation/) 已在 v1.26 中作为 alpha 功能添加到 Kubernetes 中。它定义了请求访问第三方资源的传统设备插件 API 的替代方案。根据设计，动态资源分配使用对 Kubernetes 核心完全不透明的资源参数。这种方法对集群自动扩缩器 (CA) 或任何需要为一组 Pod（例如作业调度程序）做出决策的高级控制器构成了问题。它无法模拟随着时间推移分配或取消分配声明的效果。只有第三方 DRA 驱动程序才有可用于执行此操作的信息。

动态资源分配的结构化参数是对原始实现的扩展，它通过构建一个框架来支持降低这些声明参数的不透明性，从而解决了此问题。驱动程序可以管理资源并使用 Kubernetes 预先定义的特定“结构化模型”对其进行描述，而不是自己处理所有声明参数的语义。这将允许了解此“结构化模型”的组件在不将它们外包给某些第三方控制器的情况下对这些资源做出决策。例如，调度程序可以在不与动态资源分配驱动程序进行反复通信的情况下快速分配声明。为本版本所做的工作集中于定义启用不同“结构化模型”和实现“命名资源”模型所需的框架。此模型允许列出各个资源实例，并且与传统的设备插件 API 相比，增加了通过属性单独选择这些实例的能力。

### 节点内存交换支持 ([KEP-2400](https://kep.k8s.io/2400))

在 Kubernetes v1.30 中，Linux 节点上的内存交换支持对其工作方式进行了重大更改 - 重点在于提高系统稳定性。在以前的 Kubernetes 版本中，NodeSwap 特性门默认处于禁用状态，并且在启用时，它使用 UnlimitedSwap 行为作为默认行为。为了实现更好的稳定性，UnlimitedSwap 行为（可能会损害节点稳定性）将在 v1.30 中被移除。

对 Linux 节点上交换的更新的、仍处于测试阶段的支持将默认可用。但是，默认行为将是将节点设置为 NoSwap（而不是 UnlimitedSwap）模式。在 NoSwap 模式下，kubelet 支持在交换空间处于活动状态的节点上运行，但 Pod 不会使用任何页面文件。您仍需要为 kubelet 设置 --fail-swap-on=false，才能在该节点上运行。

然而，重大更改是另一种模式：LimitedSwap。在此模式下，kubelet 实际上使用该节点上的页面文件，并允许 Pod 将其部分虚拟内存分页出去。容器（及其父 Pod）无法访问超出其内存限制的交换，但系统仍可以在可用时使用交换空间。

Kubernetes 的节点特殊兴趣小组 (SIG Node) 还会根据最终用户、贡献者和更广泛的 Kubernetes 社区的反馈，更新文档，帮助您了解如何使用经过修改的实现。

阅读之前的 [博客文章](/blog/2023/08/24/swap-linux-beta/) 或 [节点交换文档](/docs/concepts/architecture/nodes/#swap-memory) 以了解有关 Kubernetes 中 Linux 节点交换支持的更多详细信息。

### 在 Pod 中支持用户命名空间 ([KEP-127](https://kep.k8s.io/127))

[用户命名空间](/docs/concepts/workloads/pods/user-namespaces) 是一项仅限 Linux 的功能，它可以更好地隔离 Pod，以防止或减轻多个评级为高/严重级别的 CVE，包括 2024 年 1 月发布的 [CVE-2024-21626](https://github.com/opencontainers/runc/security/advisories/GHSA-xr7r-f8xq-vfvv)。在 Kubernetes 1.30 中，对用户命名空间的支持正在迁移到测试阶段，现在支持带或不带卷、自定义 UID/GID 范围等的 Pod！

### 结构化授权配置 ([KEP-3221](https://kep.k8s.io/3221))

对 [结构化授权配置](/docs/reference/access-authn-authz/authorization/#configuring-the-api-server-using-an-authorization-config-file).) 的支持正在迁移到测试阶段，并且将默认启用。此功能支持创建
**多 webhook 授权链**

使用明确定义的参数验证特定顺序中的请求，并允许精细控制（例如，在失败时明确拒绝）。配置文件方法甚至允许您指定 [CEL](/docs/reference/using-api/cel/) 规则，以便在将请求分派到 webhook 之前对其进行预筛选，从而帮助您防止不必要的调用。API 服务器还会在修改配置文件时自动重新加载授权器链。

您必须使用 `--authorization-config` 命令行参数指定该授权配置的路径。如果您想继续使用命令行标记而不是配置文件，它们将继续按原样工作。要获得新的授权 webhook 功能（如多 webhook、失败策略和预筛选规则）的访问权限，请切换到将选项放入 `--authorization-config` 文件中。从 Kubernetes 1.30 开始，配置文件格式为 beta 级，并且由于默认情况下启用了功能闸门，因此只需要指定 `--authorization-config`。[授权文档](/docs/reference/access-authn-authz/authorization/#configuring-the-api-server-using-an-authorization-config-file) 中提供了包含所有可能值的示例配置。

有关更多详细信息，请阅读 [授权文档](/docs/reference/access-authn-authz/authorization/#configuring-the-api-server-using-an-authorization-config-file)。

### 基于容器资源的 Pod 自动伸缩（[KEP-1610](https://kep.k8s.io/1610)）

基于 `ContainerResource` 指标的水平 Pod 自动伸缩将在 v1.30 中升级到稳定版。

水平 Pod 自动伸缩的此新行为允许您根据各个容器的资源使用情况配置自动伸缩，而不是 Pod 上的聚合资源使用情况。有关更多详细信息，请参阅我们的 [上一篇文章](2023/05/02/hpa-container-resource-metric/)，或阅读 [容器资源指标](/docs/tasks/run-application/horizontal-pod-autoscale/#container-resource-metrics)。

### 用于准入控制的 CEL（[KEP-3488](https://kep.k8s.io/3488)）

在 Kubernetes 中集成用于准入控制的通用表达式语言 (CEL) 引入了一种更动态、更具表现力的方式来评估准入请求。此功能允许定义和直接通过 Kubernetes API 强制执行复杂、细粒度的策略，从而增强安全性并提高治理能力，同时不影响性能或灵活性。

CEL 添加到 Kubernetes 准入控制使集群管理员能够制定复杂规则，这些规则可以根据集群的所需状态和策略评估 API 请求的内容，而无需诉诸基于 Webhook 的访问控制器。这种级别的控制对于维护集群操作的完整性、安全性和效率至关重要，使 Kubernetes 环境更强大，并能适应各种用例和要求。有关将 CEL 用于准入控制的更多信息，请参阅 [API 文档](/docs/reference/access-authn-authz/validating-admission-policy/)，了解 ValidatingAdmissionPolicy。

我们希望您和我们一样对这个版本感到兴奋。在几周内留意官方发布博客，了解更多亮点！