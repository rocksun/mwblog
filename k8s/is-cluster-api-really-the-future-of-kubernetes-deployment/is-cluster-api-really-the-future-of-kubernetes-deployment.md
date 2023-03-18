# Cluster API 真的是 Kubernetes 部署的未来吗？

翻译自 [Is Cluster API Really the Future of Kubernetes Deployment?](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/) 。

每个人都喜欢 Cluster API。但有些情况下它并不是最好的解决方案。来看看 Omni，Sidero Labs 新的基于裸金属和边缘部署的 Kubernetes SaaS 。

在 Sidero Labs ，我们非常喜欢 [Cluster API](https://github.com/kubernetes-sigs/cluster-api)（CAPI）。我们已经围绕它构建了许多东西，包括[多个](https://github.com/siderolabs/sidero) [CAPI](https://github.com/siderolabs/cluster-api-control-plane-provider-talos) [ Provider ](https://github.com/siderolabs/cluster-api-bootstrap-provider-talos)，不用提还有每天多次使用 CAPI测试 Talos Linux 。我们是 CAPI 的粉丝。但在这篇文章中，我们将讨论我们认为存在问题的地方，以及为什么我们选择不在我们的新 SaaS 产品 Omni 中使用 CAPI 来在裸机和边缘上部署 Kubernetes 。

首先，什么是 Cluster API ？根据文档，“ Cluster API 是 Kubernetes 的一个子项目，旨在提供声明性 API 和工具，以简化多个 Kubernetes 集群的配置、升级和运维。”这基本上意味着 Cluster API 为人们提供了一种创建和管理 Kubernetes 集群的方式，类似于他们在 Kubernetes 中管理应用工作负载的方式。这为那些已经成为Kubernetes专家的人提供了一个非常好的体验，以便他们可以用自己喜欢的方式管理事物。

有所有[云提供商](https://github.com/orgs/kubernetes-sigs/repositories?q=cluster-api-provider&type=all&language=&sort=)的 Cluster API Provider 、VMware 的 Cluster API Provider ，以及针对裸机的 Cluster API Provider —— [Sidero Metal](https://sidero.dev/) 是我们自己的针对裸机的 CAPI 提供商，可以对服务器进行全面管理（在需要时开关机，将它们添加到集群中，删除和擦除机器等）。根据 CAPI 文档，“可以在各种基础设施环境中实现一致和可重复的集群部署。”

听起来不错，那么问题在哪里呢？

## CAPI 的问题

我们很幸运在 Sidero Labs 拥有一群热情的用户。我们有大量企业大规模运行 Talos Linux，其集群中有数十万个核。我们也有很多中小型企业运行着几个只有几个节点的小型集群，还有许多用户在运行家庭实验室。这些不同的用例导致人们对像 CAPI 这样的东西的胃口呈双峰分布。那些将数百个裸机集群作为内部服务运行的团队喜欢 CAPI 提供的功能。小团队则没有那么热衷。以下是一些原因。

* CAPI 需要一个专用的“管理平面”。这意味着您需要一个 Kubernetes 集群来管理您的 Kubernetes 集群。对于硬件有限的人，只想运行一两个集群，专门为此目的分配另一个集群和节点是浪费和昂贵的。
* 这很难。在许多方面，必须深入了解 Cluster API 和特定提供程序提供的原语。这些原语因所选的提供程序而异，这可能会导致普通用户在尝试了解其管理平面和预配系统时感到困惑。对于完全不了解 Kubernetes 的团队来说，这更加令人困惑。试图理解 pod 、 deployment 等已经够难了，还需要额外的思维负担。
* CAPI 对于裸金属或边缘部署来说存在一些假设不太适用。在 CAPI 的世界中，升级过程是“启动一个带有新配置的新节点，然后关闭旧节点”。这对于单节点集群的边缘用例根本行不通，对于需要复制大量数据的集群节点，如果关闭节点，则也不起作用（考虑一个带有大量 Ceph 存储在本地连接的磁盘上的裸机节点）。如果没有备用服务器用于滚动升级，也不起作用——而留下每个类别的昂贵服务器空闲，以及管理平面服务器，则会带来沉重的负担（如果在云提供商中运行集群，则不存在此问题）。
* 故障排除很困难。由于 Cluster API 的模块化，很难确定出问题的地方。许多集群创建的编排都取决于各种资源的状态，以及这些资源是否已完成配置，以便下一个提供者拥有足够的信息来提供其资源。与上述观点相关的是，您必须深入了解 CAPI 本身和基础设施/引导/控制平面提供者之间的集成，才能知道在哪里查找故障日志。 

所有这些都导致我们建议普通用户不要使用 CAPI，尽管我们开发了一个 CAPI 提供者，除非他们要部署具有数百台服务器的许多集群。

## 进入 Omni

我们大约九个月前开始构建 Omni。 Omni 的目标是提供绝对顺畅的体验，用于创建 Kubernetes 集群并随时间管理它们。这包括一整套惊人的功能，例如轻松加入节点、处理升级、与企业身份验证提供程序集成的集群用户管理等。正如人们可能怀疑的那样，我们进行了许多关于如何架构该系统以及是否要基于 Cluster API 的讨论。最终决定是，不，我们不会使用 CAPI。上述问题是其中一些原因，加上 Omni 的一些其他目标，CAPI无法满足这些目标：

* 对于我们的一些用户来说，要求使用专用的“管理平面”是不可行的。我们有使用本地设备的用户，他们希望提供完全断网和简单的方式来部署、管理和升级集群，我们希望通过 Omni 来实现这一点。我指的是在沙漠地区运输一整个机架并希望它能正常工作的级别的断网。对于这些用户，要求额外的硬件来运行一个HA管理平面集群是资源的巨大浪费，或者在某些情况下根本不可能，因为他们已经有一整个机架的服务器。
* 再加上操作这些设备的人甚至不知道 Kubernetes 是什么。我们需要最简单的体系结构来启动 Omni 及其管理的集群。要求使用 CAPI 的 Kubernetes 集群、一堆提供程序、 Omni 本身，然后尝试在现场启用引导和故障排除基本上是行不通的。从要求中移除 Cluster API 允许我们将 Omni 作为单个 Go 二进制文件进行交付，这使得管理变得简单明了。（是的，Omni是一个SaaS，但您可以轻松地自己运行它。）
* Omni 通过 Kubespan 支持真正的混合 Kubernetes 集群。我们在内部使用它，效果非常好。我们通过在 Azure 中低成本托管控制平面节点，而在 Equinix Metal 中使用强大的裸机节点，每月节省大约 $1500 。这种能力非常强大，允许您从任何地方（任何云、VMware、裸机）添加节点到集群中（但要小心如何标记这些节点并调度它们）。然而，在 Cluster API 中，没有任何提供者是以这样一种方式编写的，即可以在单个集群中混合使用提供者。
* Omni 的目标之一是使边缘 Kubernetes 变得简单 - 大部分使用 Omni 的人都在用它来实现这一点。使用 Cluster API 没有好的方法来进行边缘部署。没有真正的方法允许在边缘进行预启动执行环境（PXE）引导：这些节点需要遵循“签到”流程。在Omni中的工作方式是，节点从公司的 Omni 账户下载的镜像引导。该镜像被预先配置为形成一条点对点 Wireguard 连接返回到 Omni 账户。因此，只要机器启动，它就会显示为 Omni 中的未分配机器，并允许用户将机器连接到现有集群或使用它创建一个新集群。这实际上并不符合 Cluster API 的供应流程，我们认为我们想出的与 Cluster API 一起使用的任何解决方案都会有点“hacky”，并且无法提供我们想要的简单性。
* 最后，Cluster API 将限制一些 Talos Linux 的功能。一个很好的例子是升级 Kubernetes 和 Talos Linux 本身。我们为这两者都提供非常好的 API，允许就地升级并在升级执行过程中提供良好的就绪检查。在 CAPI 之外构建允许我们利用我们已经拥有的升级 API，并避免 CAPI 强加的滚动更新限制。

因此，所有这些都是为了说明，在考虑我们的设计目标时，Cluster API 并不适合 Omni 。

## 未来

有人可能会问：“这对 Sidero Metal 有什么影响？”回答是：完全没有影响！ Sidero 实验室仍然是 CAPI 社区的一部分，我们所有的提供者都将继续得到维护和改进。虽然我们认为 CAPI 存在一些限制，正如您可以从上面的观点中看到的那样，但对于特定的用例，如大规模提供许多集群而无需混合集群， CAPI 仍然是一个不错的选择。对于这些用户，我们将继续建议他们使用和享受 CAPI 。

但是对于 Omni，我们将继续在没有 CAPI 的情况下构建它，因为这会为更多用户带来更好的体验。实际上，我们预计 Omni 很快将成为一个更好的体验，即使对于运行数百个集群和服务器的用户也是如此。 Omni 可以轻松混合来自任何平台的工作程序（不像 CAPI）；它是（像 CAPI 一样）基于声明性的驱动；它带来了 SaaS 的简单性，并且很快将支持 IPMI 以用于裸金属，所有这些都包含在一个优雅的 UI（和API） 中。这是一个绝对棒的平台，将简化几乎所有用户的生活。同时鼓励他们不要过于担心操作集群，只需运行他们的工作负载即可！

如果您想了解更多有关 Omni 或 CAPI 的信息，欢迎参加我们 3 月 21 日的免费虚拟用户会议 [TalosCon](https://www.siderolabs.com/taloscon/) 。诺基亚将讨论如何使用 CAPI、 Talos Linux 和 Sidero Metal “将私有云托管的 Kubernetes 服务扩展到10万+核心”。我们还将举行几场有关 Omni 和边缘 Kubernetes 的演讲。

希望在那里见到您！