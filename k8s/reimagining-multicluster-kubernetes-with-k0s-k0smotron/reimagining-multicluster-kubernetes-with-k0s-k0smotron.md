<!--
title:k0s/k0smotron：重新想象多集群 Kubernetes
cover: https://cdn.thenewstack.io/media/2023/11/c597fd88-k0smotron-copy-1024x576.png
-->

k0s 是高度灵活的 Kubernetes，允许您根据使用场景需要，便捷配置和部署控制平面与工作节点。

> 译自 [Reimagining Multicluster Kubernetes with k0s/k0smotron](https://thenewstack.io/reimagining-multicluster-kubernetes-with-k0s-k0smotron/)，作者 Jussi Nummelin 是一位在 IT 和软件领域有 20 多年经验的技术老将。他目前是 Mirantis 的高级首席工程师，领导 k0s Kubernetes 发行版的开发工作。Jussi 很早就接受了容器技术，将 Docker 0.6 部署到生产环境。自那时起......

Kubernetes 有着非常复杂的名声。从某种意义上说，这是不可避免的：跨多个基础设施和功能配置的容器编排是很复杂的事情，涉及许多潜在的依赖关系。

从本质上讲，Kubernetes 很简单：从集群内部看，世界就像一堆[“只有它们需要的复杂程度”的抽象概念](https://thenewstack.io/why-kubernetes-operators-will-unleash-your-developers-by-reducing-complexity/)，Kubernetes 以可靠、可预测的方式对其进行操作。

当然，这正是 Kubernetes 的目的：用一个新的、统一的、单一的[开源平台](https://thenewstack.io/isovalent-open-sources-tetragon-ebpf-based-observability-platform/)和自动化标准取代过去对数据中心和云平台的概念：一种人们可以用来“铺平基础设施世界”的东西，实现真正的工作负载可移植性、敏捷性和高效率规模化运维。

这导致了两年前开源 [k0s 项目](https://k0sproject.io/)的引入，该项目最初由 [Docker](https://www.docker.com/？utm_content=inline-mention) 和 Kontena 的团队组成，后来被 Mirantis 联合起来，专注于服务这两个相关目标。

**简单性**：创建一个得到[云原生计算基金会](https://cncf.io/？utm_content=inline-mention)验证的、敏捷的、易于定制的发行版，快速地消耗上游的基础部分(安全补丁在 3 天内完成，次要版本在几天内完成，完整版本更新在几周内完成，都经过测试)。以一种让它几乎可以在任何环境中运行的方式进行打包(任何 CPU、任何常见的 Linux、作为进程或在容器中、在物联网节点、笔记本电脑、服务器上，扩展到数据中心中的数千个节点)，并在操作上尽可能地具备完整的功能和易于使用。

k0s 可以在任何地方用一个命令进行部署，并自带自己的 CLI 和 kubectl——其他开源部署和操作工具可以从同一来源下载，例如 k0sctl 或 Lens Desktop。

**铺平基础设施世界的能力**：Kubernetes 既是一个平台，也是一个[随时可扩展的自动化系统](https://thenewstack.io/automate-the-boring-stuff-with-kubernetes/)——这是为了在其他事情中操作自己而构建的。

k0s 通过使用 YAML 或 JSON 声明式地配置事物、在必要时创建自定义抽象并使用 kubectl 或其他自动化来应用和管理它们，以 Kubernetes 原生的方式解决 [Kubernetes 运维挑战](https://thenewstack.io/three-common-kubernetes-challenges-and-how-to-solve-them/)。

自最初版本以来，k0s 已快速发展，发布了:

- 一个自动管理用户设置计划中的安全更新的 [Autopilot](https://docs.k0sproject.io/head/autopilot/) k0s operator;
- 一个具有提供程序和扩展的 [Kubernetes Cluster API(CAPI)](https://thenewstack.io/commoditizing-kubernetes-with-the-cluster-api/) operator，允许您使用 ClusterAPI 作为集群操作的 Kubernetes 原生载体;
- 支持 [Konnectivity](https://github.com/k0sproject/k0s/blob/main/docs/networking.md%23controller-worker-communication)——一种在被动防火墙隔离的情况下，Kubernetes 工作节点和控制平面之间进行安全双向通信的协议，因此可以实现更完整的(和“开箱即用”简单的)控制平面/工作节点分离，而无需大量的网络配置。

然后 k0s(及其不断增长的 operator 群)正在成为我们认为大多数 Kubernetes 用户所需要的：一个普通的、功能齐全的、[可配置的 Kubernetes，可以在任何地方运行](https://thenewstack.io/5-best-practices-for-configuring-kubernetes-pods-running-in-production/)，进行自我更新，并且可以(越来越自动地)管理基础设施——所有这些都是符合 Kubernetes 最佳实践的 Kubernetes 原生方式。

此外，k0s 的灵活性非常强，允许您根据使用情况将控制平面和工作节点配置和放置在任何有意义的位置。

简而言之，k0s 是“完整简单的 Kubernetes，正常工作”。这是开源软件，您可以用它来铺平基础设施世界。

## K0smotron

[K0smotron](https://k0smotron.io/)，刚刚作为开源软件推出，是下一步：它的 operator(可在任何 CNCF 验证的 Kubernetes 上运行)使您可以使用 Kubernetes 原生方法在 Kubernetes 集群上托管、扩展和生命周期管理容器化的 k0s 控制平面，然后从任何地方配置和连接工作节点到这些虚拟控制平面。

K0smotron 正在构建，以解决那些希望以高效和敏捷的方式利用 Kubernetes 的组织现在面临的重大[挑战](https://thenewstack.io/how-to-solve-kubernetes-persistent-storage-challenges/)——几乎不需要平台工程或特殊技能，并且运营开销很低。

如今，这些用例中有一些已经无处不在——基本上每个人都有这个问题:

**问题：我如何为开发人员、团队和项目提供和维护大量不同规模的 Kubernetes 环境？我如何使个人(“我需要一个测试集群!”)和团队(“我想轻松执行蓝绿应用部署!”)自助使用 Kubernetes？**

满足这一挑战的传统方法开始于一系列重要的、技术要求高的大决策，随着组织规模的增加，这些决策变得更加困难。您应该在虚拟机上托管 Kubernetes 集群还是裸机上？公有云还是私有云(或者两者都有)？自制开源还是专有 IaaS 云解决方案？

然后，主要基于这些选择，您将需要平台工程和深度自动化技能 —— 用于管理底层虚拟基础设施(如果您使用云)、设置集群、扩展集群、随着时间的推移保持集群的安全/策略管理/合规性以及更新集群(可能围绕运行的应用程序)。

所有这些意味着需要大量知识、要维护的复杂自动化代码以及需要制定和跟进的许多新程序。 

**有了 k0s/k0smotron 生活会更美好** —— 相比之下，k0s 允许您在任何基础设施上建立一个强大的 [Kubernetes 主机集群](https://thenewstack.io/microsoft-azure-stop-and-start-kubernetes-clusters-like-pausing-a-video/)(使用 k0sctl，多节点集群可以在几分钟内用一个命令构建)，安装 k0smotron operator(一个命令)，然后:

- 在一个简单、可读的 YAML 文件中定义一个控制平面；
- 用一个命令应用它；
- 用一个命令派生[托管控制平面](https://thenewstack.io/hosted-control-planes-bring-extra-power-and-more-cost-control/)的工作节点加入密钥；
- 在任何地方安装工作节点 —— 每个只需要三个命令：安装，安全地提供密钥和启动，将它们加入到控制平面。

该过程非常快速、非常可靠，并且因为它需要很少的交互，所以使用您现在使用的任何工具都非常容易自动化。

k0smotron 子集群[控制平面是 Kubernetes 应用程序](https://thenewstack.io/how-kubernetes-is-becoming-the-universal-control-plane-for-distributed-applications/)，因此 Kubernetes 会做所有标准操作来保持它们正常运行和健康，没有单点故障。

- k0s 子集群通过 Autopilot operator 实现自我更新和自我修复，它在执行像先更新[控制平面节点](https://thenewstack.io/how-many-nodes-for-your-kubernetes-control-plane/)然后更新工作节点以及在出现问题时回滚等操作时非常智能。所以子集群基本上不需要运维开销。
- k0s 主机集群也可以使用 Autopilot 进行自我更新。一旦您设置了所需的配置，整个系统在很大程度上可以自我维护，无需人工干预。
- 它也是自扩展的。可以使用 CAPI operator 动态扩展和缩减 k0s 主机集群，以驱动底层[云基础架构或供应/取消供应裸机](https://thenewstack.io/containerization-in-public-clouds-or-on-bare-metal-think-again/)(使用 k0sctl 衍生代码库)。
- 如果需要的话，k0s 子集群也可以跨主机自扩展，并且如果需要更多物理或虚拟容量，甚至可以请求主机自扩展。而且 k0smotron 也可以通过主机的 CAPI operator 说话来提供节点作为工作节点。所以解决方案操作的每个方面都是通过 Kubernetes 原生方式执行和控制的。

k0smotron 的其他用例更加微妙。例如:

**问题：我如何使用多集群 Kubernetes 来高效地集中管理大量运行工作负载的分布式物联网设备网络？**

同样，传统的解决方案相当痛苦。首先，您解决多集群管理的挑战(见上文)，但有一些额外的问题。首先，公有云 Kubernetes 不支持远程工作节点，大多数企业平台在开箱即用方面难以提供此功能，所以您可能会被迫自行开发(复杂、耗时、许多未知)。

然后，您要解决设置、更新和维护数千甚至数万个工作节点的挑战——可能在无线或其他不稳定网络链接的另一端。如果“远程设置工作节点”有任何复杂之处，您的自动化在扩展和可靠工作方面将面临[挑战](https://thenewstack.io/how-to-move-past-elasticsearchs-scaling-challenges/)。

即使您能够在实地搭建工作节点——如果没有强大的控制平面/工作节点分离，大多数 Kubernetes 集群模型在这些情况下都无法良好运行。

有了 k0s/k0smotron，这些问题基本上会消失。 K0s 可以在近乎任何东西上运行(我们已经测试了只有单个 ARM7 CPU 和 512MB RAM 的情况)，并且维护控制平面/工作节点分离(包括恢复/重新连接等)。

Konnectivity 可以处理跨哑防火墙和[ NAT](https://en.wikipedia.org/wiki/Network_address_translation) 的工作节点到控制平面链接。Autopilot operator 使主机集群、子集群控制平面及其分布式工作节点保持更新。CAPI operator [管理主机集群的基础设施](https://thenewstack.io/kubecon-eu-red-hat-expands-openshift-to-the-edge-with-advanced-cluster-management/)，并有潜力供应物联网节点。

您构建该应用程序“基础架构”层 [MVP](https://en.wikipedia.org/wiki/Model-view-presenter) 的投资涉及编写一些相当简单的自动化，以大规模运行简单、可靠的程序，并对用户友好。

## Mirantis 全面支持

k0s 和 k0smotron 的构建是为了简化 Kubernetes 并普及这样一个强大的想法，即 Kubernetes 可以并且应该作为基础设施上的一个在很大程度上自治的抽象层运行。

两者都经过 CNCF 验证，并及时更新以跟上 kubernetes.io 和 CNCF 生态系统创新，并由 [Mirantis](https://www.mirantis.com/?utm_content=inline-mention) 进行安全验证和完整测试。k0s/k0smotron 为组织提供了一条干净、安全的路线，通过该路线可以消耗上游创新，以最小的成本和风险，灵活地在任何地方利用多集群 Kubernetes。

它们也得到了 [k0s 团队和 Mirantis Opscare 的全面支持](https://thenewstack.io/lens-an-open-source-kubernetes-ide-grows-with-mirantis-support/)，直到 Mirantis 专业服务和/或 Opscare 提供的“零运维”状态。此外:Mirantis 全球范围内的云原生平台专家团队定制和管理您的解决方案，让您可以 100% 专注于推动业务增长的创新。

我们鼓励您尝试开源 k0s 和 k0smotron。我们的新博客“[k0smotron 入门](https://www.mirantis.com/blog/getting-started-with-k0smotron)”可以让您轻松上手。

