
<!--
title: CentOS之后，AlmaLinux和Rocky Linux的差异演进
cover: https://cdn.thenewstack.io/media/2025/06/71926fa7-beth-macdonald-p3rs8j1thi4-unsplash-alma-rocky.jpg
summary: AlmaLinux和Rocky Linux都是为了替代CentOS，但策略和技术方向开始分化。AlmaLinux基于CentOS Stream构建，兼容RHEL，并支持旧硬件。Rocky Linux则力求成为RHEL的精确克隆，CIQ还推出了强化版。选择哪个取决于你的需求。CentOS 7用户应尽快迁移到受支持的Linux发行版。
-->

AlmaLinux和Rocky Linux都是为了替代CentOS，但策略和技术方向开始分化。AlmaLinux基于CentOS Stream构建，兼容RHEL，并支持旧硬件。Rocky Linux则力求成为RHEL的精确克隆，CIQ还推出了强化版。选择哪个取决于你的需求。CentOS 7用户应尽快迁移到受支持的Linux发行版。

> 译自：[How AlmaLinux and Rocky Linux Have Diverged Since CentOS](https://thenewstack.io/how-almalinux-and-rocky-linux-have-diverged-since-centos/)
> 
> 作者：Steven J. Vaughan-Nichols

[AlmaLinux](https://almalinux.org/) 和 [Rocky Linux](https://rockylinux.org/) 的出现，都是为了应对 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) [停止维护 CentOS Linux](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/) 的举措，旨在提供免费、社区驱动、企业级的操作系统，并与 [Red Hat Enterprise Linux (RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)) 兼容。那是过去。现在的情况是，虽然它们的起点相似，但它们的策略、治理和技术方向已经开始分化。

在深入探讨之前，让我们先了解一下它们的起源。[CloudLinux](https://cloudlinux.com/) 是一家专注于 Web 服务器 Linux 的公司，其产品基于 CentOS，[它启动了 AlmaLinux](https://thenewstack.io/jack-aboutboul-how-almalinux-came-to-be-and-why-it-was-needed/)。此后，该发行版转移到了非营利组织 [AlmaLinux OS 基金会](https://almalinux.org/members/)。它的重点是提供一个稳定的、与 RHEL 兼容的应用程序二进制接口 (ABI) 平台。商业支持可以通过 [TuxCare](https://tuxcare.com/) 获得。

[Gregory Kurtzer](https://gmkurtzer.github.io/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 是 CentOS 的联合创始人，他创立了 Rocky Linux，该项目由 [Rocky Enterprise Software Foundation (RESF)](https://www.resf.org/) 管理。这个发行版强调社区驱动的方法，并与 RHEL 实现 1:1 的二进制兼容。如需 Rocky Linux 的支持，您可以联系 Kurtzer 的公司 [CIQ](https://ciq.com/products/rocky-linux/)。

这两个发行版都依赖于 [Red Hat Package Manager (RPM)](https://rpm.org/) 和 [Dandified Yum (DNF)](https://opensource.com/article/18/8/guide-yum-dnf) 包管理器。虽然 Red Hat 最近也采用了 [不可变镜像来代替 RHEL 10 的软件包补丁](https://thenewstack.io/red-hat-enterprise-linux-10-an-ai-driven-quantum-ready-platform/)，但 AlmaLinux 和 Rocky Linux 都没有采用这种方法。

在支持方面，与 Red Hat 一样，它们都为其主要版本提供 10 年的长期支持 —— 5 年的积极支持（功能和错误更新），以及 5 年的安全更新和关键错误修复。例如，这两个发行版新发布的 10 版本将获得积极支持到 2030 年 5 月，安全支持到 2035 年 5 月。

## AlmaLinux 逐渐超越 RHEL

到目前为止，它们听起来非常相似，但你越仔细观察，就会发现越多的差异。例如，AlmaLinux 不再是 RHEL 的严格 1:1 二进制克隆。相反，它是基于 [CentOS Stream 源代码](https://gitlab.com/redhat/centos-stream?utm_source=opensourcewatch.beehiiv.com&utm_medium=referral&utm_campaign=almalinux-boosts-legacy-hardware-support-with-latest-linux-release) 构建的。不过，由于其 ABI RHEL 兼容性，你基本上可以在其上运行所有 RHEL 应用程序。在最低级别上，RHEL 和 AlmaLinux 之间现在存在差异。这会对你造成影响吗？可能不会。

事实上，你们中的许多人会欣赏 AlmaLinux 的一些变化。例如，当 Red Hat [放弃对 x86-64-v2 芯片微架构的支持时](https://developers.redhat.com/articles/2024/01/02/exploring-x86-64-v3-red-hat-enterprise-linux-10)，AlmaLinux 选择 [继续为这种较早的架构提供二进制文件](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/)。这意味着你可以在使用大约 2008 年到 2013 年的 x86-64 处理器的服务器上运行最新的发行版 AlmaLinux 10。

还有许多其他的细微差别。这些包括对 [独立计算环境简单协议 (SPICE)](https://www.spice-space.org/)（虚拟桌面协议）的支持，以及 Firefox 和 Thunderbird，它们作为 RPM 软件包而不是 Flatpak 提供。

此外，[AlmaLinux 9.4](https://opensourcewatch.beehiiv.com/p/almalinux-boosts-legacy-hardware-support-latest-linux-release) 和 10.0 明确地重新引入了对 RHEL 9.4 和 10.0 已经删除的设备驱动程序和硬件的支持。这包括存储控制器、网络适配器和其他对旧服务器和工作站至关重要的组件。

最后但同样重要的是，[AlmaLinux 将根据请求修补常见漏洞和暴露 (CVE)](https://fossforce.com/2024/04/in-a-first-almalinux-patches-a-security-hole-that-remains-unpatched-in-upstream-rhel/)，即使 Red Hat 将它们评为低优先级或中等优先级。

## Rocky Linux 保持信念

另一方面，如果你想要一个真正的 RHEL 克隆，尽可能地镜像 CentOS 的原始模型，那么 Rocky Linux 就是你想要的。如果你的首要任务是稳定性和可预测性，那么这非常棒。

假设安全性对你来说最重要。在这种情况下，CIQ 想要向你介绍 [CIQ 的 Rocky Linux – Hardened](https://ciq.com/products/rocky-linux/hardened/)。此版本通过消除许多潜在的攻击面和常见的利用途径，最大限度地降低了零日漏洞和 CVE 风险。它包括代码级别的强化，可以阻止常用的利用路径，从而降低成功攻击的风险。它还使用 [Linux Kernel Runtime Guard (LKRG](https://lkrg.org/)) 来检测逃避传统安全措施的复杂入侵。其中的所有软件包都经过验证，并通过安全供应链交付，确保操作系统安全交付且始终保持最新。

## 要走的路

那么，你应该选择哪一个呢？这取决于你。两者都是优秀的发行版。

不过，我能说的是，对于成千上万（甚至数百万？）仍然使用 [CentOS 7 的人，尽管它已于 2024 年 6 月 20 日停止支持](https://opensourcewatch.beehiiv.com/p/centos-7s-end-life-sight-ready)，你们必须咬紧牙关并迁移到受支持的 Linux。是的，我知道从 CentOS 升级可能成本高昂且耗时。但我也知道，当（不是如果）一个重大的安全零日漏洞破坏现有的 CentOS 安装时，你将会遇到大麻烦。切换到 AlmaLinux 或 Rocky Linux 的时间是在那一天到来之前，而不是之后。