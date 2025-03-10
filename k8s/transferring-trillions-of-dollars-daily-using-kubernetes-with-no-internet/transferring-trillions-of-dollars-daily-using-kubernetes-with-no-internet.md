
<!--
title: 每天使用没有互联网的Kubernetes转移数万亿美元
cover: https://cdn.thenewstack.io/media/2025/03/6aa585bc-disconnected-kubernetes-swift.jpg
-->

SWIFT 通过 Kubernetes 集群管理的零权限方法，保障了他们网络上数百万笔日常交易的安全。

> 译自：[Transferring Trillions of Dollars Daily Using Kubernetes With No Internet](https://thenewstack.io/transferring-trillions-of-dollars-daily-using-kubernetes-with-no-internet/)
> 
> 作者：Alex Handy

有很多[架构图](https://roadmap.sh/software-design-architecture)描述了部署在传统企业中的[基于云的架构](https://thenewstack.io/3-key-practices-for-perfecting-cloud-native-architecture/)。但是，如果您运营的金融市场基础设施每天处理价值数万亿美元的交易，该怎么办？如何在几乎没有互联网访问的情况下安全地大规模管理和运营环境？如果集群内部的用户无法以任何方式访问该集群的底层基础设施，只能通过他们正在使用的应用程序访问，该怎么办？如果该架构仍然必须完全更新和修补，以跟上潜在的安全威胁，该怎么办？

这是一个复杂的挑战，特别是考虑到集群无法连接到互联网。然而，这些正是 [Swift](https://www.swift.com/) 旨在处理的约束。当一家银行向另一家银行转账时，交易通过 Swift 网络进行通信。银行之间相互持有账户，并根据交易请求调整余额。

这些请求是 SWIFT 消息，它们完全与互联网隔离。那么，如何在高度安全的离线环境中管理大量的集群呢？

## 无接触

Swift 的容器平台产品负责人 Otmane Benali 表示，他的团队使用 GitOps 在全球部署了数百个完全与互联网断开连接的 Kubernetes 集群。他在 2024 年 11 月在 KubeCon North America 之前的 [OpenShift Commons](https://commons.openshift.org/) [演讲](https://www.youtube.com/watch?v=wI6pmgznbd8) 中描述了该架构。

“我们是在一个断开连接的环境中运行，这意味着用户无法访问互联网。我们只有两台可以访问互联网的主机：我们的 [Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) (RHEL) 主机和 Nexus 容器注册表。在 RHEL 主机上，我们运行一个来自 Red Hat 的名为 oc-mirror 的实用程序来下载镜像。然后，这些镜像存储在本地容器注册表中，”Benali 解释说。

Benali 说：“镜像列表被上传到 git。[当我们有新的 OpenShift 版本或 Operator 时]，我们在实验室环境中测试它们，一旦我们满意，我们就将其提升到开发、质量保证和生产环境。在提升之前，我们使用 Red Hat Advanced Cluster Security for Kubernetes 扫描镜像，并使用 [Podman](https://thenewstack.io/use-podman-to-create-and-work-with-virtual-machines/) 的签名进行身份验证，然后使用 Skopeo 复制镜像。”

Swift 的高级企业架构师 Praveen Siddu 说：“一旦镜像被提升，我们不会就此止步。我们要确保镜像已下载并缓存在特定环境的所有地理位置中，以便镜像在 pod 使用之前已在容器注册表中可用。缓存镜像列表被上传到对象存储。对象存储是集中式的，因此我们可以清楚地了解所有环境，并且我们确信镜像在实际开始使用之前已经提升到该环境。”

## 多国、多集群

这意味着即使没有互联网访问，也有很大的动力来保持安全和更新。Swift 通过使用 git 作为其事实来源，并以集中、可复制的方式管理 [Kubernetes](https://thenewstack.io/kubernetes/) 集群部署来实现这一点。

Benali 说：“我们使用 [GitOps 模型](https://www.redhat.com/en/topics/devops/what-is-gitops)，并使用 [Red Hat Advanced Cluster Management for Kubernetes](https://www.redhat.com/en/technologies/management/advanced-cluster-management) 来更快地构建集群。我们还引入了集群舰队管理，以大规模管理集群并保持它们在同一版本上的一致性。零权限实施帮助我们满足了法规要求以及安全要求。最后，我们实现了显着的成本节约，并将上市时间缩短了几个数量级。”

Siddu 详细阐述了 Swift 使用的多集群架构。他说团队拥有 Hub 集群和 App 集群。“它们都是 Red Hat OpenShift 集群。Hub 集群和 App 集群之间唯一的区别是 App 集群运行应用程序工作负载；Hub 集群只运行 Red Hat Advanced Cluster Management 和 Red Hat GitOps，”Siddu 说。“Red Hat Advanced Cluster Management 是一个非常灵活的工具。它使我们能够同时构建多个集群，因为每个集群都在其自己的命名空间中运行，并且是容器化的。”

由于 git 是所有这些集群构建背后的事实来源，Siddu 说最终只有 [Argo CD](https://argo-cd.readthedocs.io/en/stable/) 才能更改集群；不会对任何集群进行手动更新。

“如果 Argo 是唯一对集群进行更改的实体，”Siddu 说，“这意味着如果我们必须升级一个集群，如果我们必须升级 10 个集群，那么工作量是相同的，对吧？因为我们所要做的就是将配置推送到 git。一旦我们将新更新推送到 git 存储库，我们的工作就停止了；Argo CD 会完成其余的部署工作。”

Swift 已经能够将每个集群的集群部署和测试时间缩短到 90 分钟以内。

这包括一些内置的保障措施。“其中一项保障措施，”Siddu 说，“是所有已在此新版本中的集群都必须处于健康状态。如果其中任何一个不处于健康状态，[the rollout] 就会停止。然后，如果一切都处于健康状态，它将继续处理下一个集群，为其准备配置，Argo CD 会完成将其应用于目标集群的其余工作。完成后，它会给集群一些稳定期，然后继续处理下一个集群。”

所有这些工作使 Swift 能够应对每天面临的困难的安全和监管要求。拥有一个清晰的系统来跟踪谁在何时何地做了什么至关重要。

“谁在哪个集群上执行了哪个操作以及何时执行的列表，”Siddu 说，“实际上是由在同一命名空间中运行的另一个部署检索的，然后将其上传到对象存储。因此，我们可以清楚地跟踪谁在哪个集群上执行了哪个操作。”

Benali 说，这使 Swift 团队能够在全球范围内快速部署数百个 Kubernetes 集群，并通过 Swift 的舰队管理系统进行部署。他们还可以控制升级和更新发生的时间，这样他们就不会意外地传播意外的错误。这使 Swift 能够降低成本并提高开发人员的速度，同时还能保证客户交易的安全。
