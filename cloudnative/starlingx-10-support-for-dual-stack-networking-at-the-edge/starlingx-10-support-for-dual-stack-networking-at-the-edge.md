
<!--
title: StarlingX 10：支持边缘双栈网络
cover: https://cdn.thenewstack.io/media/2025/02/9815d818-starling-x-2.jpg
-->

> 译自：[StarlingX 10: Support for Dual-Stack Networking at the Edge](https://thenewstack.io/starlingx-10-support-for-dual-stack-networking-at-the-edge/)
> 
> 作者：Steven J Vaughan-Nichols

StarlingX，这个开源分布式云平台，已正式发布备受期待的10.0版本。

StarlingX 一直以来都是一个优秀的边缘计算云平台，但它在核心网络中也同样有所帮助。

[StarlingX](https://www.starlingx.io/)，这个开源分布式云平台，已正式发布其备受期待的[10.0](https://docs.starlingx.io/releasenotes/index.html)版本，标志着其发展的一个重要里程碑。此更新于周三发布，带来了许多新功能和增强功能，以提高各种应用程序的性能和用户体验，尤其是在[物联网 (IoT)](https://thenewstack.io/the-internet-of-things-on-the-edge/)、5G 和[边缘计算环境](https://thenewstack.io/edge-computing/)中。

StarlingX 10.0 的一个突出特点是其对 IPv4/IPv6 双栈网络的支持。此增强功能允许用户同时运行两种协议，确保在行业从 IPv4 向 IPv6 过渡（许多行业正在进行中）时的兼容性。

虽然 StarlingX 长期以来一直支持 IPv6 网络，但直到现在它还不支持双网络栈。现在，“最新的增强功能现在允许用户在单栈和双栈网络配置之间切换，以允许[使用 IPv4 和 IPv6 地址空间](https://www.starlingx.io/blog/starlingx-release-10/)，”开放基础设施基金会 (Open Infrastructure Foundation) 的社区总监在 StarlingX 博客的一篇文章中写道。

由于 StarlingX 经常被电信公司使用，而它们的 数据中心通常仍然运行 IPv4，而它们的 5G 移动网络依赖于 IPv6，因此这种新的双栈支持是一个宝贵的补充。

## 简化部署的新框架

此最新版本还拥有一个新的统一软件管理框架，该框架简化了平台的部署和管理。用户现在可以通过 REST API 或 CLI 访问的单个界面执行更新和升级，从而简化了单一和分布式云安装的操作。

具体来说，该框架使用[OSTree](https://github.com/ostreedev/ostree)安装新软件，而主机继续在现有文件系统上运行。因此，简单的重启就可以切换到新软件，与以前的方法相比，大大减少了停机时间。它还支持同时部署补丁和更新。简而言之，这是一个纯粹的胜利。

在幕后，StarlingX 10.0 包括对其底层[Linux 内核版本从 5.10 升级到 6.6](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/)。此更改增强了性能并扩展了对更广泛的硬件平台和设备驱动程序的支持。此更新基于最新的长期支持 (LTS) [Yocto Linux 发行版](https://www.yoctoproject.org/)。Yocto 是一个广受好评的可定制嵌入式 Linux。

因此，平台的可扩展性得到了显著提高。它现在可以管理每个系统控制器最多 5000 个远程站点，而之前的版本只有 1000 个。此增强功能对于大规模部署至关重要，使操作大型网络更加容易。

## 增强的 Kubernetes 支持

此版本还随附 [Kubernetes 的 Harbor](https://goharbor.io/) 作为其容器注册表。Harbor 是一个开源注册表。它使用策略和[基于角色的访问控制 (RBAC)](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/)来保护工件。Harbor 还确保映像经过扫描且没有漏洞；它还会对映像进行签名。这使用户能够安全地管理云原生工件，例如容器映像和 Helm 图表。

正如您所料，StarlingX 继续集成各种开源项目的较新版本，包括[Kubernetes](https://roadmap.sh/kubernetes)（最高版本 1.29），确保用户可以访问平台内的最新技术。

改进的 Kubernetes 支持非常重要，因为 StarlingX 依赖于 Kubernetes 服务[NUMA 感知内存管理器](https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/)来防止最坏情况下的内存延迟。当 StarlingX 的核心在高负载下运行时，可能会发生这种内存速度下降。

虽然所有这些都增强了 StarlingX 作为边缘云的地位，但将 StarlingX “归类”为边缘云将是一个错误，负责商业支持该项目的公司的首席技术官说。
“从核心到中心，Boost Mobile ([https://www.boostmobile.com/](https://www.boostmobile.com/)) 网络中的每一块云基础设施，超过 20,000 个站点，都基于 StarlingX”，Miller 告诉 The New Stack。

他不是唯一一个对 StarlingX 的最新变化感到满意的人。“我们很高兴看到 StarlingX 10.0 的发布，”99Cloud ([https://www.99cloud.net/](https://www.99cloud.net/)) 技术总监 Huang Shuquan 在一份声明中说。“此次发布是我们努力提供企业级开源分布式边缘云平台的关键成就。”

那些有兴趣探索新功能或部署 StarlingX 10.0 的人现在可以下载预构建的 [StarlingX 代码库中的 Debian Linux ISO](https://mirror.starlingx.windriver.com/mirror/starlingx/release/10.0.0/debian/monolithic/outputs/iso/)。如果您以前没有使用过 StarlingX，我强烈建议您首先阅读 [项目文档](https://docs.starlingx.io/)。
