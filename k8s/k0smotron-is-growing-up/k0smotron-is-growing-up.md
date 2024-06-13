
<!--
title: k0smotron 正在成长
cover: https://www.mirantis.com/images/mirantis-logo-1200x630.png
-->

k0smotron 1.0 宣布推出通用可用性，并提供新的企业功能，包括在任何基础设施上远程部署整个集群、提高控制平面高可用性以及启用就地更新。为 Kubernetes 多集群部署提供更无缝、更简单的操作。

> 译自 [k0smotron is Growing Up | Mirantis](https://www.mirantis.com)，作者 Jussi Nummelin。

使用 Kubernetes 的组织面临着定义、配置、扩展和生命周期管理集群的挑战。许多组织需要在多种基础设施（私有云、公有云、裸机等）上执行这些操作。

平台团队需要找到定义 k8s 集群和相关服务的方法，以便运营人员和开发人员可以按需部署这些服务。平台团队和架构师需要找到指定具有新颖占用空间的部署的方法（传统或托管控制平面、本地或远程工作程序），以满足现代混合、边缘和其他用例的要求。

k0smotron（去年推出，11 月宣布）为这些多集群/混合挑战提供了一个开源的 Kubernetes 原生解决方案。它与 Kubernetes ClusterAPI 协同工作，以便在您选择的公有云、私有云、托管或非托管裸机或其任意组合上启用声明性基础设施配置。k0smotron 帮助您配置、部署和生命周期管理跨所有这些基础设施的 k0s Kubernetes 子集群：您可以安装任意数量的 CAPI 提供程序来提供支持。（[了解有关 ClusterAPI 的更多信息](https://www.mirantis.com/blog/how-to-use-cluster-api)）

但还有更多内容。通过利用 k0s Kubernetes 的独特优势（如控制平面/工作程序网络分离），k0smotron 1.0 可以更轻松地配置混合、边缘甚至更复杂的用例的奇特集群占用空间：

- 云中的控制平面，客户场所的高能工作程序节点
- 公有云“母舰”集群上的容器化控制平面，防火墙后面的远端边缘工作程序
- 具有完全移动工作程序的物联网

k0smotron 可以执行所有这些操作，而 k0s 有助于保持网络相当简单。

## 用 Kubernetes 铺平世界

通过将平台管理所需的一切内容置于 Kubernetes API 和声明性配置之后，k0smotron 提供了 Kubernetes 原生多集群 GitOps 所需的内容，并让您更接近于使用 Kubernetes 在 Kubernetes 基底下“铺平”基础设施世界。

借助 k0smotron 1.0（与 Helm 结合使用，以便在子集群上高效安装应用程序和服务），平台工程师可以将完整的解决方案堆栈打包到一组受版本控制的 YAML 文件中：组成软件开发团队所需的一切（即基础设施、集群、已安装的服务和应用程序），以涵盖广泛的用例，例如：

- 整个 SaaS 服务点配置
- 具有端点架构的完整边缘应用程序
- 多服务移动网络平台和服务

现在所有这些都可以轻松部署并实现自我维护。

平台工程师的一个显而易见的优势：简单性。使用 k0smotron，您无需安装、维护、更新和管理大量不同的部署工具（以及它们自己的 YAML 或其他配置代码库）。

k0smotron 在宏观趋势方面也具有意义：

- 首先，Kubernetes 无疑是所有事物的未来平台。它目前是我们运行复杂现代应用程序的最佳工具。它为我们所需的所有更高阶服务（如无服务器、PaaS 和功能即服务等）提供核心平台。因此，使用它来铺平基础设施可以简化我们的生活，甚至让我们以新的方式思考基础设施——我们甚至可以将公有云视为商品实用程序。（还记得我们所有人都以这种方式思考“云”并想象一个未来，在这个未来中，计算/存储/网络 provider 将在不锁定我们或向我们收取大量资金的情况下争夺我们的工作负载吗？这是最初的目标。）
- 其次，Kubernetes 擅长此项工作。它是一个标准化机器，用于查看描述所需状态的声明性文件，然后（直接或通过标准中间件）将现实融合到该状态。这就是为什么现代配置自动化工具都基本以这种方式工作的原因。

将<所有内容>置于 Kubernetes API 之后（并确保这是完全开源和标准化的）赋予了我们超能力：

- 描述和实现深度解决方案堆栈的一种方法
- 注入和实现可观察性的一种方法
- DevSecOps 的一个集成点
- 也许最重要的是，AIOps 的一个集成点。

## 实际客户测试

k0smotron 已被 Mirantis 的主要客户使用了一段时间，我们非常感谢他们的帮助和热情。今天，我们宣布 k0smotron 1.0 正式发布，并提供企业支持。k0smotron 1.0 有一些令人兴奋的新功能，使其成为一个更加完善的解决方案。k0smotron 1.0 不再仅仅是一个“托管控制平面管理器”，而是一个真正的多集群/混合管理解决方案。

k0smotron 1.0 中的新功能包括：

## 远程机器支持

k0smotron RemoteMachine 现在是 Kubernetes ClusterAPI 的一个成熟的基础设施 Provider（请参阅 [provider 列表](https://cluster-api.sigs.k8s.io/providers/)），通过 SSH 启用远程机器的配置。k0smotron 现在可以使用 RemoteMachine（例如）构建和生命周期管理具有托管或传统控制平面的分布式或单片 k0s 集群。

优点：对非托管裸机进行便捷操作，在数据中心和边缘开启用例。例如，您可以在公有云中的母舰集群上使用 k0s 托管控制平面构建一个集群，在边缘位置或客户场所的裸机 Linux 机器上使用远程工作器。

k0smotron + CAPI 提供商（包括 RemoteMachine）还可以充当高级基础设施提供商，与非 k0s 管控平面提供商一起工作。因此，从原则上讲，您现在可以使用 k0smotron RemoteMachine 部署 k3s 或 MicroK8s（或许多其他）集群风格。k0smotron RemoteMachine 还可以支持自定义 SSH 连接器，因此，如果您的基础设施要求您使用 Teleport，例如，您就可以[自定义该 provider ](https://docs.k0smotron.io/stable/capi-remotemachine-teleport/)以运行在 Teleport 所需的基础设施授权下的供应。

## 控制平面扩展和更新

传统的 k0s 集群可以通过利用 Autopilot 运算符自动且无中断地更新自身（控制器和工作器）。然而，k0smotron 的早期版本并未完全支持此范例，因为 k0smotron 没有办法向集群内 Autopilot 发出信号，以更新托管子集群控制平面。**现在，对于在虚拟机中运行的子集群，k0smotron 1.0 与子集群的 Autopilot 集成，以更新整个集群（控制器和工作器）——使用逐节点策略，使集群保持可用。**

优点：以标准化方式轻松扩展多个基础设施平台上的子集群。

## 外部 etcd 支持控制平面 HA

为了增强托管控制平面的高可用性 (HA)（在 pod 中运行 k0s 控制平面），**k0smotron 1.0 现在将在托管控制平面组件的单独 pod（和有状态集）中部署 etcd。** 以前，运行高可用托管控制平面（即部署到不同故障域的多个容器化控制器）具有挑战性，因为当 etcd（实际上是每个控制平面的组成部分）被纵向扩展时，可能会出现脑裂场景。通过新的更新，etcd 独立于其他 HCP 组件（在单独的一组 pod 中）进行管理，使其能够独立扩展。etcd 还可以进行快照和还原，从而实现强大的完整集群升级和状态恢复。

*注意：这涉及到 0.9.5 之前的 k0smotron 版本的重大更改——请参阅* [此注释](https://docs.k0smotron.io/stable/upgrade-0.9.5-to-1.0/) *了解更多信息和简单的解决方法。*

优点：自由扩展的托管控制平面——因此您可以平衡冗余可用性和利用率。

## Clusterctl 支持

最后，k0smotron 1.0 添加了通过 ClusterAPI 的 clusterctl CLI 安装 k0smotron 的支持。用户可以直接通过 clusterctl 安装和管理 k0smotron，而不是单独安装——实际上，这使得将 ClusterAPI 设置用于基础设施管理变成一个完整的多集群解决方案变得更加容易。简单：

```
clusterctl init --bootstrap k0sproject-k0smotron \ --control-plane k0sproject-k0smotron \ --infrastructure k0sproject-k0smotron
```

优点：更简单的设置。通过一个命令从零到“完整的多集群管理器”。

## ClusterClass 支持

以前，为 ClusterAPI 定义一个完整的 Kubernetes 集群及其基础设施需要相当长且复杂的 YAML 文件——有时超过 500 行。**ClusterClass——现在是 ClusterAPI 中的一个 alpha 功能——允许您标准化基础设施定义，然后在几行代码中引用它（带有变体）。** k0smotron 1.0 中支持此功能——简化文件，使其更具可读性和可管理性，支持开发可重用配置，并简化自动化。

优点：提高了可重用性，使代码更易于阅读。错误潜入的可能性更小。

## 立即试用 k0smotron！

k0smotron 1.0 现在是一个完整的多集群管理器——托管控制平面不再是全部（尽管它们非常酷且有用）。

同样令人兴奋的是，k0smotron 现在将获得 Mirantis 的全球全面支持——因此，希望探索解决方案或使用案例的企业可以借助 Mirantis 深厚的客户成功工程团队以及 Team k0s 本身的专业知识，大规模地使用 k0smotron。支持将分为三层：

- LabCare - 8 x 5（周一至周五）工作时间支持。适用于非生产工作负载
- Opscare - 24/7 支持，对关键问题提供 30 分钟响应时间 SLA。适用于企业生产环境
- Opscare Plus - 全托管主动支持，可用性 >99.9%

请注意，对 k0smotron 的支持包括对 k0s 的支持——零摩擦、零依赖、CNCF 验证的 Kubernetes。
