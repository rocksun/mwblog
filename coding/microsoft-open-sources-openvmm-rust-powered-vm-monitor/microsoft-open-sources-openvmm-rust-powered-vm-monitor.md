
<!--
title: 微软开源 OpenVMM，一款基于 Rust 的虚拟机监控器
cover: https://cdn.thenewstack.io/media/2024/10/c0437f19-pawel-czerwinski-4vkaa4ovycm-unsplash.jpg
-->

继微软最近发布了 OpenHCL（一种机密虚拟机旁虚拟化程序）之后，该公司现在又发布了 OpenVMM，这是一个用 Rust 编写的 VMM。

> 译自 [Microsoft Open Sources OpenVMM Rust-Powered VM Monitor](https://thenewstack.io/microsoft-open-sources-openvmm-rust-powered-vm-monitor/)，作者 Steven J Vaughan-Nichols。

虚拟机监控器 (VMM) 领域又添新成员：[OpenVMM](https://github.com/microsoft/openvmm)。这款全新的开源、跨平台、模块化 VMM 代表着微软对[开源技术](https://thenewstack.io/open-source/) 和安全高效的虚拟化解决方案的承诺迈出了重要一步。

当然，VMM 并不罕见。Hyper-V、QEMU 和 VirtualBox 都是耳熟能详的例子。OpenVMM 的独特之处在于它使用 Rust 语言编写。这一点至关重要，因为正如[Joe Stocker](https://mvp.microsoft.com/en-US/mvp/profile/f9cb9fdd-37e8-ea11-a814-000d3a8dfe0d)，微软安全公司[Patriot Consulting](http://www.PatriotConsultingTech.com) 的 CEO 在 Twitter 上写道，“[Rust 比 C 或 C++ 更安全](https://x.com/ITguySoCal/status/1847101065268744345)，因为它的所有权模型和借用检查器在编译时强制执行严格的内存安全和并发保证，从而防止常见的漏洞，例如空指针解引用、缓冲区溢出和数据竞争。”

OpenVMM 旨在运行在各种操作系统上，展现了微软对跨平台兼容性的承诺。该项目在 GitHub 上以[MIT 许可证](https://opensource.org/license/mit) 发布，支持多种架构和虚拟化 API，使其成为开发人员和系统管理员的通用且强大的工具。

OpenVMM 主要作为[OpenHCL，微软新的开源旁虚拟化](https://thenewstack.io/microsoft-open-sources-openhcl-a-linux-based-paravisor/) 的一部分而开发，用于机密计算虚拟机。OpenVMM 支持具有分配设备的虚拟操作系统客户机，并提供设备转换支持。此外，它允许用户共享机密和非机密架构和客户机。在这两种情况下，VMM 都提供针对每个需求量身定制的相同服务。根据微软的 Caroline Perez-Vargas [在博客文章中](https://techcommunity.microsoft.com/t5/windows-os-platform-blog/openhcl-the-new-open-source-paravisor/ba-p/4273172) 的说法，“这避免了机密和非机密虚拟机之间的碎片化虚拟化解决方案，朝着弥合机密虚拟机的功能差距迈进。”

然而，需要注意的是，OpenVMM 仍处于早期阶段。微软坦诚地承认了该项目当前的局限性，并表示它尚未准备好投入生产使用。该公司将其描述为“更像是一个用于实现新 OpenVMM 功能的开发平台，而不是一个现成的应用程序。”

## 早期阶段

具体来说，“[在传统主机环境中运行 OpenVMM 的体验并没有太多‘打磨’](https://github.com/microsoft/openvmm/blob/main/Guide/src/user_guide/openvmm.md#disclaimer)，尤其是‘令人愉快的’。这种缺乏打磨体现在几个方面，包括但不限于：

- 无组织且文档很少的管理接口（例如，CLI、ttrpc/grpc）
- 未优化的设备后端性能（例如，存储、网络、图形）
- 意外缺少的设备功能（例如，传统 IDE 驱动器、PS/2 鼠标功能）
- 没有任何 API 或功能集稳定性保证。

简而言之，您可以在 Azure 中以及与 OpenHCL 合作的情况下使用 OpenVMM，而不会遇到太多麻烦。但是，对于任何其他用途，您将几乎完全依靠自己。

尽管如此，OpenVMM 可能会成为[虚拟化生态系统](https://thenewstack.io/how-one-small-startup-is-changing-the-virtualization-landscape/) 中的重要角色。但毫无疑问：我们正处于将 OpenVMM 打造成一个普遍有用的管理程序的早期阶段。对于同时运行机密和普通 VM 工作负载的特定用例，OpenVMM 值得您关注。
