# Nvidia 如何使用 KubeVirt 扩展其云服务

![Featued image for: How Nvidia Scaled Its Cloud Services With KubeVirt](https://cdn.thenewstack.io/media/2024/10/531145bb-nvidia-kubevirt-1024x576.jpg)

2013 年，Nvidia 决定让用户能够在顶级硬件上玩顶级游戏，而无需花费 3000 美元购买游戏 PC。该公司构建了 GeForce NOW，这是一项在线服务，使世界各地的玩家都能使用云端超高速 GPU 支持的游戏 PC。

GeForce NOW 的普及程度不断提高，目前拥有 2500 万订阅用户。有了这么多用户，这项服务不会很快消失，但 Nvidia 的原始架构却面临着考验。虽然 Nvidia 在几乎所有情况下都偏爱下一代 IT，但 GeForce NOW 是使用虚拟机 (VM) 构建的，而不是 Linux 容器，这给服务的扩展计划带来了问题。

扩展此类服务是 [Kubernetes](https://thenewstack.io/kubernetes/) 编排的容器的最佳用例。但是，如果原始游戏平台是基于 VM 构建的，而 VM 更僵化，不太适合快速扩展和缩减，该怎么办？

[KubeVirt](https://kubevirt.io/) 应运而生，这是一个开源平台，用于在本地或云中 [运行容器和虚拟化工作负载](https://thenewstack.io/virtualization-and-containers-better-together/)。

[Nvidia 是基于高端硬件构建的](https://thenewstack.io/nvidias-hardware-roadmap-and-its-impact-on-developers/) 用于游戏。那么 Nvidia 如何使用容器和 VM 构建在线游戏平台呢？
首先，一些背景信息。

## 什么是 KubeVirt？

KubeVirt 提供了一个统一的共享平台，开发人员和管理员可以在其中构建、修改和部署容器和 VM 中的应用程序。KubeVirt 允许使用与管理 Kubernetes 相同的软件来管理 VM，无论您使用 [Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) 还是自己动手 (DIY)。

![KubeVirt 架构](https://cdn.thenewstack.io/media/2024/10/327082ae-kubevirt-architecture-simple-1024x448.png)
来源：[KubeVirt](https://kubevirt.io/user-guide/architecture/)

KubeVirt 将虚拟机放置在 Linux 容器中。因此，您可以像管理平台上的其他基于容器的资产一样管理 VM。KubeVirt 包括对 VM 快照、实时迁移、内存热插拔、非一致内存访问 (NUMA)、[巨页](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/performance_tuning_guide/s-memory-transhuge)、虚拟网络和存储的支持。您可以在大规模处理虚拟机时获得所有预期的 VM 功能，但可以通过与用于 Kubernetes 的相同工具进行管理。

## Nvidia 如何扩展 KubeVirt

Nvidia 必须满足数千名游戏玩家的需求，他们期望的游戏体验等同于台式机上的 PC，而不是云端。

在 2024 年巴黎 KubeCon 上，来自 Nvidia 的 [Ryan Hallisey](https://www.linkedin.com/in/ryan-hallisey-b680b279/) 和 [Alay Patel](https://www.linkedin.com/in/alaypatel07/) [展示了一些 KubeVirt 的基准测试](https://www.youtube.com/watch?v=pCgLYXevN3Y)。这对搭档强调了社区如何大幅提高 KubeVirt 的性能，并展示了他们的基准测试工具。Hallisey 说，该团队希望转向更基于微服务的方案。“我们如何在不完全放弃投资的情况下做到这一点？这就是我们考虑采用 KubeVirt 的地方。下一代 GeForce NOW 基础设施基于 KubeVirt 和 Kubernetes。”

## 在 KubeVirt 上管理和自动化 VM 基础设施

KubeVirt 是 Kubernetes 平台中 VM 的托管层，其他工具提供自动化和管理。[Ansible](https://kubevirt.io/2023/Managing-KubeVirt-VMs-with-Ansible.html) 是一个出色的 KubeVirt 自动化工具，[GitOps](https://kubevirt.io/user-guide/cluster_admin/gitops/) 也是如此，它在 Git 存储库中维护集群的状态。

KubeVirt 是一个可行的选择，可以承担当前在其他 VM 平台上的工作负载。您可以使用开源项目 [Konveyor forklift](https://github.com/kubev2v/forklift.github.io/blob/main/index.md) 将它们迁移到 KubeVirt，正如 [此视频所示](https://www.youtube.com/watch?v=RnoIP3QjHww)。
一旦您启动并运行，平台的开源社区内将会有很多活动。在 2024 年 6 月的 DevConf 上，[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 [Lee Yarwood](https://www.linkedin.com/in/leeyarwood/) 探讨了 KubeVirt 中 [VM 创建现状](https://www.youtube.com/watch?v=HqupumX5Zys)。在 2023 年的 Cloud Native Rejekts 上，Cloudera 的 [Shane Kumpf](https://www.linkedin.com/in/shane-kumpf-024aa222/) 展示了该公司如何使用 KubeVirt [转向超融合基础设施](https://www.youtube.com/watch?v=kMyAkoiXXrg)。[加入社区](https://kubevirt.io/community/) 并与其他用户互动。

## 结论

KubeVirt 可扩展到数千个用户，为由一组工具管理的 VM 和容器提供并排平台。将容器和 VM 的控制平面和管理相结合，减轻了开发人员和系统管理员的负担。

将您的工作负载从另一个虚拟化平台迁移到 KubeVirt 可以从 Konveyor 开始，然后由其他工具自动执行和管理。KubeVirt 是一种可行的替代虚拟化平台，提供标准的 VM 功能、合作伙伴生态系统和扩展性能。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。