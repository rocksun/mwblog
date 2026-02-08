<!--
title: Kubernetes 1.35 新特性：赋能日常运维变革
cover: https://cdn.thenewstack.io/media/2026/01/17ff642d-kuberenetes-1.35.jpg
summary: Kubernetes 1.35发布五项GA功能，包括Pod资源原地更新、细粒度辅助组控制、PreferSameNode流量分发、结构化认证配置和OCI镜像卷，旨在提升集群的可靠性、效率和安全性，优化运维。
-->

Kubernetes 1.35发布五项GA功能，包括Pod资源原地更新、细粒度辅助组控制、PreferSameNode流量分发、结构化认证配置和OCI镜像卷，旨在提升集群的可靠性、效率和安全性，优化运维。

> 译自：[Kubernetes 1.35 features that change Day 2 operations](https://thenewstack.io/kubernetes-1-35-features-that-change-day-2-operations/)
> 
> 作者：Janakiram MSV

Kubernetes 作为容器化应用和微服务最受欢迎的编排平台，持续发展和成熟。Kubernetes 1.35，[最新版本](https://thenewstack.io/kubernetes-1-35-timbernetes-introduces-vertical-scaling/)于2025年12月中旬发布，提供了多项现已普遍可用的增强功能。这些功能为在 Kubernetes 集群上运行的工作负载带来了可靠性和效率。

本文重点介绍 Kubernetes 1.35 中普遍可用的五项主要增强功能。

## Pod 资源原地更新

[Pod 资源原地更新](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/)是最新 Kubernetes 版本中备受瞩目的 GA 功能。在以前的版本中，修改容器的 CPU、内存请求和限制会强制 Pod 重启，从而中断有状态工作负载和长时间运行的进程。通过 Pod 资源原地垂直扩缩功能，您可以无缝调整正在运行的 Pod 容器的资源大小，而无需终止 Pod。

实现此功能类似于操作现有 Pod 的规范。通过使用 `kubectl patch` 或 `kubectl edit`，您可以直接更改 CPU 和内存请求。当操作 deployments 和 StatefulSets 等控制器时，可以更改并应用 spec 以使其持久化。请记住，此功能仅限于 CPU 和内存，不包括临时存储等其他资源，这些资源仍然会强制 Pod 重启。

此功能对 Pod 垂直自动扩缩具有重要影响。当与 [垂直 Pod 自动扩缩](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/) (VPA) 集成时，Pod 可以根据来自 Metrics Server 或 Prometheus 等源的实时指标进行垂直扩缩。它对于管理有状态服务特别有用，在这些服务中，重启会触发数据重新平衡或故障转移。对于 AI 和机器学习 (ML) 工作负载，它有助于保留内存缓存和模型检查点，最大限度地减少训练、微调和推理期间的干扰。

DevOps 专业人员应了解此功能的潜在局限性。在扩缩 Pod 的 CPU 或内存分配之前，主机节点必须有足够的可用资源。过度承诺资源可能导致内存不足 (OOM) 错误或 Pod 驱逐。使用 `kubectl describe pod` 等命令检查扩缩状态，并将其与 Cluster Autoscaler 结合使用以进行主动节点供应。

## 细粒度辅助组控制

共享 Kubernetes 集群中的安全性取决于文件访问的组权限的有效管理。新的 [辅助组策略](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#supplementalgroupspolicy) 字段现已 GA，它提供了对如何将辅助 Unix 组分配给 Pod 中单个容器的精确控制。

以前，Pod 中的所有容器都从 Pod 的顶级 [安全上下文](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) 继承相同的辅助组集。这可能导致在同一 Pod 中有多个容器的配置中出现过度宽松的访问。新方法提供了多种选项，例如合并来自所有容器的组，或应用严格模式，该模式仅使用每个容器明确指定的组，从而防止意外继承。

DevOps 和 DevSecOps 工程师可以在 Pod 的安全上下文中配置此功能，选择策略类型，然后根据需要为每个容器定义组。这种方法确保单个容器只接收其指定的组，从而强制执行强大的安全性和隔离性。

对于多租户集群，这降低了使用 POSIX 访问控制列表通过持久卷声明 (PVC) 访问共享卷的风险。它允许依赖基于组权限的传统应用程序与其他工作负载安全地运行，而无需授予违反最小权限原则的广泛访问权限。这在金融服务和医疗保健等高度受监管的行业中特别有用，在这些行业中必须维护详细的审计跟踪以符合合规性要求。

将此功能与 Pod Security Admission 结合使用，可以实现全面的安全框架。DevSecOps 团队可以通过 [Open Policy Agent](https://www.openpolicyagent.org/) (OPA) 或 [Kyverno](https://kyverno.io/) 等策略执行工具审计现有 Pod，以强制执行严格模式。通过缩小潜在的攻击面，此功能有助于满足 [互联网安全中心](https://www.cisecurity.org/benchmark/kubernetes) (CIS) 对 Kubernetes 的基准要求。

## PreferSameNode 流量分发

网络效率在高吞吐量集群中至关重要，服务流量分发字段中 [PreferSameNode](https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-distribution) 选项的 GA 有效解决了这一问题。此策略指示 kube-proxy 或 Cilium 等 Extended Berkeley Packet Filter (eBPF) 替代方案等组件优先选择与请求 Pod 位于同一节点上的端点，仅在必要时才回退到跨节点端点。

[DevOps 工程师](https://www.thenewstack.io/DevOps) 可以通过将服务规范中的流量分发字段设置为 PreferSameNode 来启用它。这确保了在整个集群内部流量中强制执行节点本地性，从而减少网络跳数和延迟。

借鉴拓扑感知概念，它最大限度地减少了延迟，非常适合具有“多话”微服务（其中发生频繁的集群内通信）的架构，例如 API 网关或消息队列。在 [Istio](https://istio.io/) 等基于 Sidecar 的模式中，它减少了整体网络开销，从而实现更快的响应时间。具有节点本地缓存（例如 Redis 实例）的应用程序可以看到跨节点流量减少，这可以降低云环境中的数据传输成本。

实际测量表明，节点本地流量路径的延迟显著降低，尤其是在延迟敏感的服务中。DevOps 团队可以通过简单的测试（例如从 Pod 内部运行 curl 命令测量响应时间）或使用基于 eBPF 的可观测性工具进行更深入的洞察来验证这些收益。该功能适用于所有服务类型，包括无头服务，但建议监控不均匀工作负载中的负载不平衡——将其与 Horizontal Pod Autoscaler 集成以实现均衡扩缩。

## 结构化认证配置

在 Kubernetes 中配置认证高度依赖于一组分散的 kube-apiserver 标志，这些标志容易出错且难以在版本控制中跟踪。[结构化认证配置](https://kubernetes.io/docs/reference/access-authn-authz/authentication/) 的 GA 通过专用的 Authentication 配置类型引入了一个声明式、版本化的 API，将所有设置整合到一个单一、可管理的 YAML 文件中。

此文件通过 API 服务器上的特定标志引用，包含各种认证方法的设置，包括客户端证书颁发机构、webhooks、OIDC 提供商和匿名访问，所有这些都采用统一结构。

对于集群管理员，这一转变支持 GitOps 工作流，尤其是在将集群启动到 [CAPI](https://cluster-api.sigs.k8s.io/) 时。通过将配置存储在 Git 仓库中，可以通过拉取请求审查更改，并使用 Flux 和 Argo CD 等工具应用。使用标准的 kubectl 命令检查当前设置变得更简单。它还通过利用保持兼容性的版本化 API 来简化版本升级。

在企业环境中，这降低了可能使集群面临未经授权访问的错误配置的可能性。它补充了基于角色的访问控制 (RBAC)，以实现更精细的权限管理。建议在预演集群中测试新配置，以防止运营中断。

## OCI 镜像卷

[OCI 镜像卷](https://kubernetes.io/docs/tasks/configure-pod-container/image-volumes/) 现已达到 GA 稳定状态，它允许将符合 OCI 标准的容器镜像作为只读卷挂载到 Pod 中。这利用了现有的容器注册表，但将镜像纯粹视为数据仓库而不是可执行容器。尽管此功能尚未完全 GA，但它已稳定并在 Kubernetes 1.35 集群中默认启用。

Pod 规范现在支持添加一个卷，该卷通过注册表路径和拉取策略引用镜像。Kubernetes 拉取镜像层并将其挂载到容器内的指定路径，提供对镜像中文件的只读访问。

这种方法将大型或频繁更新的数据与应用程序镜像分离，使后者保持轻量。这在 AI 和 ML 场景中特别有用，例如可以独立版本化和拉取来自 Hugging Face 等仓库的模型。同样，它简化了在 CI/CD 流水线中分发 Web 应用程序的内容包或共享实用程序，允许通过熟悉的标签机制在不同命名空间中重用。

优点包括更快的镜像构建、更少的存储冗余和简化的版本控制。只读特性通过防止修改来增强安全性。管理员应确保拉取密钥的一致处理并监控注册表使用限制。用于容器镜像创建的工具可以促进这些数据镜像的构建。

## 结论

Kubernetes 1.35 的 GA 功能使管理员能够构建 [更具弹性、更高效的集群](https://thenewstack.io/kubernetes-get-the-most-from-dynamic-resource-allocation/)。首先，设置一个运行最新版本 Kubernetes 的测试环境，并在非生产环境中测试这些功能。

在本系列的后续部分中，我将深入探讨每个功能，包括分步指南和教程。敬请期待！