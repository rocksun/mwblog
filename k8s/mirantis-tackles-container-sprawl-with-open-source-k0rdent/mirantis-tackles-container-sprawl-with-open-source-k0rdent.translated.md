# Mirantis 通过开源 k0rdent 解决容器蔓延问题
![Featued image for: Mirantis Tackles Container Sprawl With Open Source k0rdent](https://cdn.thenewstack.io/media/2025/02/717e87c6-kordent-1024x768.png)

我们都在使用云原生应用程序，但没有人觉得管理它们容易。[Kubernetes](https://thenewstack.io/kubernetes/) 确实使我们能够编排它们，但这仍然需要大量工作。为了解决这个问题，领先的开源云原生程序提供商 [Mirantis](https://www.mirantis.com/about/) 推出了 [k0rdent](https://github.com/Mirantis/project-2a-docs)，这是它所谓的开源分布式容器管理环境 (DCME) 中的第一个。

K0rdent 旨在应对日益增长的[容器蔓延](https://thenewstack.io/containers/)挑战。它通过为跨各种环境（包括本地、公共云和边缘位置）管理云原生应用程序提供单一控制点来实现这一点。

## 单一管理平台
嗯，我会称之为单一管理平台，但我自己觉得这个术语已经不再流行。随便你怎么称呼它，k0rdent 为应对 Kubernetes 复杂性的组织提供了几个优势。这些是：

- 统一管理：该平台能够轻松创建定制的内部开发者平台 (IDP)，从而简化跨各种基础设施的 Kubernetes 集群的管理。
- 可组合的架构：平台工程师可以根据其特定要求定制 k0rdent，利用标准化部署模板进行快速实施。
- 多云支持：k0rdent 已经在主要的云平台上进行了测试，包括 AWS EC2、AWS EKS、Azure Compute、Azure AKS 以及 vSphere 和 OpenStack 等本地解决方案。
- 声明式自动化：该平台通过声明式自动化、集中式策略执行和针对现代工作负载优化的生产就绪模板来简化维护。
- 开源优势：通过利用开源 Cluster API，k0rdent 允许在任何地方创建和部署 Kubernetes 集群，从而提高灵活性并避免供应商锁定。

将它们放在一起，根据 Miranti 首席技术官 [Shaun O’Meara](https://www.linkedin.com/in/shaun-omeara/) 在一篇博客文章中的说法，你得到的不仅仅是一个帮助你管理基础设施和服务的程序，而且是“关于提[供一个统一的、可扩展的、策略驱动的平台，可以处理现代分布式工作负载](https://www.mirantis.com/blog/announcing-k0rdent-a-new-era-of-kubernetes-native-distributed-container-management/)——而不会迫使团队陷入供应商锁定或运营瓶颈。”

在我看来，这是一个胜利。

Mirantis 开源战略和技术副总裁 [Randy Bias](https://ph.linkedin.com/in/randybias) 在一份声明中解释说：“[k0rdent 旨在创建定制的内部开发者平台，由 Kubernetes 提供支持](https://www.businesswire.com/news/home/20250206532790/en/Mirantis-Launches-Open-Source-Project-for-Platform-Engineering-that-Accelerates-Innovation-for-Modern-Distributed-Workloads)，这有助于在任何地方的任何基础设施上进行大规模应用程序管理，同时提供选择、加速创新并加强合规性。”

## 多云环境
那么，为什么 Mirantis 要将此作为开源项目来做呢？k0rdent 背后的故事始于我们在技术领域看到的更广泛的趋势——跨多云环境部署和管理现代分布式工作负载的日益复杂性以及人工智能的兴起。作为一家在云原生生态系统中拥有深厚根基的开源公司，Mirantis 占据了这些转变的前排位置。

早些时候，Mirantis 构建了一个强大的 Kubernetes 多集群管理程序，[Kubeadm-dind-cluster (KDC)](https://github.com/kubernetes-retired/kubeadm-dind-cluster)，它可以处理从裸机到公共云的一切。然而，它采用了一种非常主观的方法，不容易提供现代平台工程师构建 IDP 以满足苛刻的云原生工作负载所需的灵活性和可组合性。认识到这些限制，Mirantis 采取了一种全新的方法。

## 容器控制平面
这就是 Mirantis 产生 k0rdent 想法的地方。Mirantis 希望创建一个开源的分布式容器管理环境，消除在复杂的多云环境中部署各种分布式应用程序的障碍。

Mirantis 声称，k0rdent 构建在 Kubernetes 之上，作为一个多云控制平面，超越了基础设施——它提供了平台工程师交付可扩展、可重复和安全环境所需的高级抽象、模板化工作流程和自动化。
随着 Kubernetes 的采用持续增长，像 k0rdent 这样的解决方案有望在帮助企业管理分布式容器环境的复杂性方面发挥关键作用。凭借其对简化、定制和开源原则的关注，k0rdent 代表了在解决管理 Kubernetes 驱动的云原生部署的巨大挑战方面向前迈出的重要一步。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。