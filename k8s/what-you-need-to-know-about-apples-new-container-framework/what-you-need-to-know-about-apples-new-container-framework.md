<!--
title: 关于苹果新容器框架，你需要了解的内容
cover: https://cdn.thenewstack.io/media/2025/06/692d026c-coding.jpg
summary: WWDC 炸裂！Apple推出全新容器框架，macOS迎来原生容器化！每个 Linux 容器跑在轻量级 VM 中，实现硬件级隔离，告别传统命名空间。亚秒级启动，完整 OCI 兼容，Swift 编写，Rosetta 2 支持 x86_64。Hypervisor 隔离成标配？容器安全迎来新范式！
-->

WWDC 炸裂！Apple推出全新容器框架，macOS迎来原生容器化！每个 Linux 容器跑在轻量级 VM 中，实现硬件级隔离，告别传统命名空间。亚秒级启动，完整 OCI 兼容，Swift 编写，Rosetta 2 支持 x86_64。Hypervisor 隔离成标配？容器安全迎来新范式！

> 译自：[What You Need To Know About Apple's New Container Framework](https://thenewstack.io/what-you-need-to-know-about-apples-new-container-framework/)
> 
> 作者：Alex Zenla

在 WWDC 2025 上，Apple [宣布](https://www.apple.com/newsroom/2025/06/apple-supercharges-its-tools-and-technologies-for-developers/)了一项将从根本上改变我们对[容器安全](https://thenewstack.io/open-source-and-container-security-are-fundamentally-broken/)的看法的技术：macOS 26 的容器化框架。虽然主题演讲侧重于 AI 和设计更新，但这项技术公告代表了一种范式转变，验证了我们在容器安全领域多年来一直倡导的理念。

## Apple 实际构建了什么

让我们抛开营销术语：Apple 的容器化框架在各自的轻量级虚拟机 (VM) 中执行每个 Linux 容器，提供硬件级别的隔离，而不是依赖于传统的基于命名空间的容器运行时。这本质上是从头开始实现的、经过优化的、用于 Apple Silicon 的、且[用 Swift 编写](https://thenewstack.io/get-started-with-swift/)的、hypervisor 隔离的容器。

容器化框架提供以下 API：

- **管理开放容器倡议 (OCI) 镜像：** 标准注册表兼容性
- **与远程注册表交互：** 你所期望的拉取/推送工作流程
- **创建和填充 ext4 文件系统：** 真正的 Linux 文件系统
- **与 Netlink 套接字族交互：** 底层网络原语
- **创建优化的 Linux 内核以实现快速启动时间：** 自定义内核构建
- **生成轻量级虚拟机：** 通过 Virtualization.framework 实现硬件隔离
- **管理虚拟机的运行时环境：** 完整的生命周期管理
- **生成并与容器化进程交互：** 进程控制和 I/O
- **使用 Rosetta 2 在 Apple Silicon 上执行 x86_64 进程：** 跨架构转换

技术架构令人印象深刻。容器使用优化的 Linux 内核配置和具有轻量级 init 系统的最小根文件系统，实现了亚秒级的启动时间。每个容器都有自己的 IP 地址，消除了端口转发的复杂性，同时保持了完整的 OCI 兼容性，以便与现有的容器工作流程无缝集成。

## 为什么这件事比你想象的更重要

Apple 进入[容器运行时](https://thenewstack.io/container-security-and-the-importance-of-secure-runtimes/)领域不仅仅是为了在 macOS 上提供 Docker Desktop 的替代方案。它验证了 hypervisor 级别的隔离应该是容器从一开始就应该拥有的安全模型。

传统的容器运行时在所有容器之间共享主机内核，从而通过内核漏洞或容器逃逸漏洞创建潜在的攻击向量。通过将每个容器放置在自己的轻量级 VM 中，Apple 消除了困扰容器安全十多年的共享攻击面。

这里的性能突破不容小觑。从历史上看，像 Kata Containers 这样的基于硬件的容器解决方案带来了显著的开销、性能下降和复杂性。Apple 实现了具有完整 hypervisor 隔离的亚秒级容器启动时间，消除了安全性和开发者生产力之间的传统权衡。

## 开发者体验革命

对于那些在 macOS 上苦苦挣扎于 Docker Desktop 的许可成本、性能问题和 VM 开销的开发者来说，Apple 的容器化框架提供了一个引人注目的原生替代方案。该框架使开发者可以直接在 Mac 上创建、下载或运行 Linux 容器镜像，OCI 兼容性确保了与现有注册表和工作流程的无缝集成。

但真正的革命在于安全模型。开发者现在可以从第一天开始就使用 hypervisor 隔离的容器构建应用程序，而不是在开发过程中接受较弱的基于命名空间的隔离，并希望在生产中获得更好的安全性。

## 行业影响

当 Apple 验证一种技术方法时，整个行业都会注意到。它决定从头开始构建 hypervisor 隔离的容器，而不是为 Kata Containers 等现有项目做出贡献或在 Docker 上构建，这表明它认为这种架构对于容器开发的未来至关重要。

这一公告可能会加速企业在整个行业中采用基于 hypervisor 的容器运行时。注重安全的组织现在有了一条清晰的路径，可以在其整个开发生命周期（而不仅仅是在生产中）实施更强大的隔离模型。
鉴于企业安全需求和合规标准的不断提高，时机显得尤为重要。传统的容器安全在很大程度上依赖于额外的工具、监控和运行时保护，以解决共享内核隔离的根本弱点。而hypervisor级别的隔离从架构层面消除了许多这些顾虑。

## 更广泛的安全生态系统

Apple的框架在容器生态系统中创造了一种有趣的动态。虽然它的解决方案解决了hypervisor隔离容器的开发方面，但企业规模的生产部署需要围绕编排、多租户和性能优化进行不同的考虑。

这为专注于生产的专业解决方案创造了机会，这些解决方案可以保持开发人员现在在本地体验到的相同安全保证。关键是确保开发和生产环境之间的兼容性和工作流程的连续性。

## 未来将如何发展？

Apple的容器化框架不仅仅代表另一种容器运行时选项。它代表了容器安全的发展方向，并验证了在不牺牲性能的情况下优先考虑隔离的方法。

该框架的开源性质也表明了Apple对更广泛的生态系统采用的承诺。Apple旨在提供一个开源框架，该框架利用其Swift编程语言，该语言针对其Apple Silicon芯片进行了优化，并最大限度地降低了安全风险。

对于容器行业而言，此公告标志着一个转折点。Hypervisor隔离容器不再是一种奇异的安全增强功能，它们正成为现代容器部署的预期基线。

问题不在于这种方法是否会成为标准，而在于生态系统将以多快的速度适应。对于优先考虑安全性而不影响开发人员体验的组织而言，这种转变现在就开始了。Apple通过使hypervisor隔离容器可用于开发，从而解决了一半的问题。保持这些安全保证的[生产规模解决方案](https://edera.dev/stories/apple-just-validated-hypervisor-isolated-containers-heres-what-that-means)的机会代表了容器发展的下一阶段。

现在，每个macOS开发人员都可以在其开发工作流程中访问适当的容器隔离。挑战和机遇在于确保相同的安全级别无缝地扩展到生产部署中。