任何好的家庭园丁都知道，健康的植物会长大超出其花盆。

一些人发现，Kubernetes 作业也是如此。它们正在变得太大，超出了它们所运行的节点。

Kubernetes 开源编排平台的最新版本引入了 Pod 资源的就地更新。

此功能（在 [KEP #1287](https://kep.k8s.io/1287) 中描述）允许用户动态调整 CPU 和内存资源，而无需重新启动 Pod 或容器。

总体而言，Kubernetes v1.35 版本（代号“Timbernetes”）引入了 60 项增强功能。

在这些增强功能中，有 17 项已达到稳定状态（包括垂直扩展），这意味着它们已完全达到生产就绪水平。

另有 19 项已进入 Beta 阶段，值得测试，还有 22 项是已进入 Alpha 测试阶段的全新技术。

此版本中也有一些值得注意的[弃用和移除](https://deploy-preview-53498--kubernetes-io-main-staging.netlify.app/blog/2025/12/17/kubernetes-v1-35-release/#deprecations-and-removals)。

## 新功能：垂直扩展

Kubernetes 工作负载一直都是水平可扩展的，只要它们是无状态的（不保存任何独特数据）。

可以启动更多节点并添加容器化应用程序的额外相同副本，前提是应用程序的设计允许轻松添加更多副本以增加容量。

然而，近年来，K8s 运维人员一直呼吁进行就地升级，以提高应用程序正在运行的现有节点的内存和/或 CPU 容量——同时保持应用程序的运行。

这种扩展对于有状态工作负载来说有点棘手，因为在被升级的节点中包含一些数据或独特的业务逻辑。

以前，就地升级需要创建一个新的 Pod，然后将工作负载迁移过去，这可能会导致服务中断。

这项新功能允许用户调整 CPU 和内存资源，而无需重新启动 Pod 或容器。

## Kubernetes 1.35 中的其他新功能

此版本中其他值得注意的新功能包括：

*   **KYAML** (Beta)：Kubernetes 一直可以通过 YAML 人类可读格式进行配置，这常常令[希望](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/)使用不那么繁琐、更容易理解的语言的运维人员感到困扰。KYAML 是 YAML 的一个子集，针对 Kubernetes 进行了优化，不仅使运维人员更易于使用，也为 kubectl 等 Kubernetes 工具提供了更强的表达能力。 ([KEP #5295](https://kep.k8s.io/5295))。
*   **协同调度** (Alpha)：大型、相互依赖的 AI 工作负载将从中受益：这是一种“全有或全无”的调度策略，它将确保只有当集群拥有足够的资源同时容纳整个定义的 Pod 组时，才对其进行调度。 ([KEP #4671](https://kep.k8s.io/4671))。
*   **作业暂停时可变容器资源** (Alpha)：到目前为止，如果作业因内存不足错误或 CPU 不足而失败，用户必须删除该作业并创建一个新作业，从而丢失执行历史记录和状态。Kubernetes v1.35 引入了在暂停状态下更新作业资源请求和限制的功能。 ([KEP #5440](https://kep.k8s.io/5440))。

此版本还包括一些值得注意的弃用。一个主要的弃用是长期使用的 Ingress NGINX 退役，转而支持 [Gateway API](https://gateway-api.sigs.k8s.io/)，这让运维人员[争相](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/)进行更新。

此外，对 Linux 控制组 (cgroup v1) 的支持也将结束，因为权限[现在由](https://thenewstack.io/linux-cgroups-v2-brings-rootless-containers-superior-memory-management/) cgroup v2 管理。

有关所有新功能和弃用的完整详细信息，请查阅 Kubernetes v1.35 [发行说明](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md)。

## 种一棵树

Kubernetes 的每个版本都会有一个新的徽标，通常由发布负责人设计。这次，它由 Kubernetes 工程师 [Drew Hagen](https://www.linkedin.com/in/drew-hagen/) 完成，他是 v1.35 版本的团队发布经理。

他告诉 TNS：“徽标的标准很高，我希望能设计出既有趣又具有象征意义的东西。”

他选择了一棵树作为主图像，以“展示 Kubernetes 社区的韧性”。

他说：“维护者和贡献者都有日常工作，有家庭，其中一些人是为此志愿奉献的。但他们从世界各地汇聚在一起，为[最大的开源项目](https://thenewstack.io/kubernetes/)之一做出贡献。”

Kubernetes v1.35 可在 [GitHub](https://github.com/kubernetes/kubernetes/releases/tag/v1.35.0) 或 [Kubernetes 下载页面](https://deploy-preview-53498--kubernetes-io-main-staging.netlify.app/releases/download/)上下载。