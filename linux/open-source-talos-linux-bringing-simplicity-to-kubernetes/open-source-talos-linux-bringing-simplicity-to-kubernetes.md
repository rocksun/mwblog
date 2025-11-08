
<!--
title: 开源Talos Linux：重塑Kubernetes的简洁之道
cover: https://cdn.thenewstack.io/media/2025/11/36476e17-talos-linux-2.jpg
summary: Talos Linux为私有/边缘云提供极简、安全的Kubernetes管理，降低成本。它无SSH/root、不可变，SNCF和SGX成功应用，Omni SaaS实现自动化。
-->

Talos Linux为私有/边缘云提供极简、安全的Kubernetes管理，降低成本。它无SSH/root、不可变，SNCF和SGX成功应用，Omni SaaS实现自动化。

> 译自：[Open Source Talos Linux: Bringing Simplicity to Kubernetes](https://thenewstack.io/open-source-talos-linux-bringing-simplicity-to-kubernetes/)
> 
> 作者：B. Cameron Gain

**披露：** Sidero Labs 支付了作者前往 TalosCon 的差旅和住宿费用。

过去几年，由于成本飙升和数据主权等一系列驱动因素，[公共云](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/)向本地和私有云基础设施发生了巨大转变。这反过来又对 Kubernetes 管理产生了重大影响。

[Sidero Labs](https://www.siderolabs.com/?utm_content=inline+mention) 的 [Talos Linux](https://github.com/siderolabs/talos) 为管理异构 Kubernetes 及其他部署所带来的高成本和复杂性提供了一个令人耳目一新的替代方案。

在许多方面，它与 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 Linux OpenShift、SUSE Rancher 和其他 Kubernetes 发行版背道而驰。在所有这些发行版中，Kubernetes 都安装并运行在通用操作系统之上。

Sidero Labs 及其开源 [Talos Linux](https://thenewstack.io/set-up-talos-linux-on-your-machine/) 认为，整个基础不仅没有必要，反而是一种负担，特别是对于私有云和边缘用例而言。

“如果你的目标是运行容器中的工作负载，并且你选择 Kubernetes 作为这些工作负载的编排器，那么在主机操作系统上你不需要太多东西，”Sidero Labs 工程负责人 Andrey Smirnov 在该公司十月中旬于阿姆斯特丹举行的 TalosCon 活动上告诉我。

“你的工作负载自带所有东西。它们已经在容器里了……所以它们不应该与主机过多交互。”

## 通过极简主义实现安全

Smirnov 表示，Talos 的核心思想是使主机最小化和安全。

他说：“我们既可以通过使其最小化，也可以通过实施更容易实现的最佳安全实践来提高系统的安全性。”

Smirnov 说，Sidero 正在剥离数十年来关于多用户系统的[类 Unix 思维](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/)：“你根本没有用户。你运行的只有你的工作负载和容器……以及 Kubernetes。”

他补充说，这种极简主义实现了“最佳安全实践”，例如“只读的不可变根文件系统。一些 Linux 发行版可以做到这一点，或接近这一点，但这有点难。” 但对于 Talos，“我们拥有整个技术栈。所以对我们来说，这很简单。我们只是把它设为只读，句号。”

Smirnov 指出，虽然 Kubernetes 是当前的标准，但其架构是灵活的：“理论上，我们也可以使用 Nomad 之类的东西。”

法国铁路运营商 SNCF 云原生平台团队负责人 Thomas Comtet 概述了这在实践中的意义。在成功将该组织 70% 的应用程序迁移到公共云后，他的团队还有 30% 的应用程序必须保留在私有数据中心。

在使用 [OpenStack](https://thenewstack.io/openstack-flamingo-reduces-technical-debt-boosts-performance/) 构建 SNCF 新的私有云平台时，该团队试图复制他们在 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 和 Azure 上使用的托管服务的效率。

Comtet 在 TalosCon 期间告诉我，SNCF 团队在公共云上管理 Kubernetes 服务，并积累了使用 [Bottlerocket](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/) 的经验，Bottlerocket 是一种基于 Linux 的开源容器操作系统。

他说：“我们非常清楚如何将 Bottlerocket 与 EKS 配合使用，或者将 Azure Linux 与 AKS 集群配合使用。”“这非常非常高效。事实上，我们非常喜欢它，我们想重现相同的体验。”

因此，他阐述道：“我们选择 Talos 主要是因为它能够与 Bottlerocket 竞争。作为平台团队，我们希望在数据中心拥有相同的体验，并且我们以更低的成本实现了这一点。”

## 案例研究：新加坡交易所与 Talos

对于新加坡交易所 (SGX) 而言，Talos 的主要吸引力在于其提供的控制级别。

当该组织开始规划其 Red Hat OpenShift 部署的生命周期结束时，可用的选项要么成本高昂，要么过于复杂，要么与 SGX 的基础设施策略不符。但其团队发现了 Talos Linux，并迅速开展了一项概念验证，这将重塑该组织的平台战略。

“对我们来说，Talos 是有意义的，”SGX FX Group 平台工程负责人 Rushan Ratha 在 TalosCon 期间告诉我。“它极其轻量级，并且符合我们的安全模型。对我来说，一次安全审计……[意味着要问]谁能访问所有这些机器？”

“嗯，现在不再是这样了。你没有 SSH 访问权限，也没有 root 用户。一切都以这种方式严格控制。”

Ratha 说，该团队在“不到 24 小时”内就从 Red Hat OpenShift 切换到了 Talos Linux。

## Omni SaaS 的创建

在创建 Talos 之后，Sidero 面临的下一个问题是如何在更大范围内实现基础设施自动化。Sidero Labs 最初尝试了 [Cluster API](https://thenewstack.io/is-cluster-api-really-the-future-of-kubernetes-deployment/)，但它引发了一些设计问题。

Smirnov 说：“每当你更改某些东西时，Cluster API 就会说它想要替换那台机器。”“这在云端效果很好，但在裸机上，那就是一场灾难。”

Talos 在开发时考虑了相反的方法：“原地更改，原地升级，一切都在原地。”

Sidero 随后尝试了 Terraform，但喜忧参半。Smirnov 说：“这好得多，但我们仍然面临这种更高级别编排的问题，例如 Kubernetes 升级。”“编码这种编排很痛苦。”

这种完整循环促成了 Sidero Labs 的 Omni 的创建，这是一款软件即服务 (SaaS) 产品。Smirnov 说：“Omni 最初的想法完全相反。不是自动配置，而是‘带上你的 Talos’这个模型。”

“用户可以将 Talos 镜像放在任何地方，即使是在一个不知名的云上，它也会连接到 Omni，然后你就可以管理了。这种方法更适用于裸机，因为裸机的库存实际上是静态的。”

在 [Omni](https://www.siderolabs.com/omni-signup/) 创建之后，用户要求具备动态配置能力，例如突发到云端并临时扩展到 AWS 的能力。这促使 Sidero 为 Proxmox、裸机、[VMware](https://www.vmware.com/?utm_content=inline+mention) 和 AWS 等环境实现了基础设施提供商。

Smirnov 说：“对于私有数据中心，裸机基础设施提供商可以处理机器的 PXE 启动、发现它们、擦除磁盘和使用 PMI。”“这个提供商可以在数据中心运行，但连接到你的 SaaS 产品 Omni。”

他说，用户也可以在本地运行 Omni，“但 Omni 成为了中央管理场所。”

Kubernetes 的兴起伴随着对其复杂性的担忧。向本地或私有云的转变加剧了这些担忧。Sidero 凭借其极简主义、安全至上的 Talos Linux 和 Omni 方法，提出了强有力的论据。但最终的评判来自于 SNCF 和 SGX 等组织的实际部署。