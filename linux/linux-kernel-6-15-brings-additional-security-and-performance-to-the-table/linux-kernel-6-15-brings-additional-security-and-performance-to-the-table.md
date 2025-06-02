
<!--
title: Linux Kernel 6.15提升虚拟化、GPU和CPU性能
cover: https://cdn.thenewstack.io/media/2025/05/88c31c76-getty-images-qcp7xpdq3q8-unsplash.jpg
summary: Linux Kernel 6.15性能大爆发！虚拟化增强Hyper-V和KVM，CPU支持AMD Zen 6，GPU集成NVIDIA NOVA驱动。内存管理优化巨页初始化，存储提升Btrfs、XFS性能。网络方面改进IPv6，更重要的是，安全补丁缓解Spectre v2漏洞，速升！
-->

Linux Kernel 6.15性能大爆发！虚拟化增强Hyper-V和KVM，CPU支持AMD Zen 6，GPU集成NVIDIA NOVA驱动。内存管理优化巨页初始化，存储提升Btrfs、XFS性能。网络方面改进IPv6，更重要的是，安全补丁缓解Spectre v2漏洞，速升！

> 译自：[Linux Kernel 6.15 Boosts Virtualization, GPU, and CPU Performance](https://thenewstack.io/linux-kernel-6-15-brings-additional-security-and-performance-to-the-table/)
> 
> 作者：Damon M Garn

一个新的内核为 [Linux 社区](https://thenewstack.io/learning-linux-start-here/) 增光添彩！Linux kernel 6.15 现已发布，它提供了通常的大量驱动程序、性能更新和安全缓解措施。管理具有大量 RAM、大量虚拟机或担心 Spectre v2 漏洞的 Linux 服务器的系统管理员将特别高兴于此版本。

使用本文中的详细信息来确定是否需要在 kernel 6.15 发布后更新您的系统。首先，请确保您熟悉 Linux 发布候选系统。

**什么是 Linux Kernel Release Candidates (RC)？**

Linux 依赖于内核更新的滚动计划，该计划之前有多个发布候选版本 (RC)。发布候选版本使贡献者能够完成代码更新并处理最终测试。团队在此阶段不添加任何新功能。这些都在第一个 RC 之前的内核的最终拉取中决定。

通常有七到八个发布候选版本，具体取决于测试结果。该过程通常持续两个月。kernel 6.15rc1 版本发布于 4 月初。

## Kernel 6.15 主要属性

描述新的 Linux 6.15 内核的最佳词语可能是“增强”。增强功能比比皆是，涵盖 CPU、GPU、存储、网络和各种常规改进。当然，安全缓解措施是新内核的重要组成部分。

查看以下增强类别，以了解有关 Linux kernel 6.15 如何提高 Linux 系统的整体功能和能力的更多信息。

### 常规增强

6.15 内核包括各种常规改进。以下是一些：

- 用于 Linux 内核代码的 Rust 编程持续增长。
- 内核调度程序（[从 kernel 6.12 继续](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/)）改进。
- Apple Z2 触摸屏和 Touch Bar 驱动程序，以增加 Apple 硬件支持。
- Apple 键盘背光驱动程序。
- Xpad 游戏控制器驱动程序改进了 Xbox 控制器
- Samsung Galaxy Book 笔记本电脑和二合一设备驱动程序支持。
- Huwei Matebook E Go EC 二合一设备驱动程序支持。

### 虚拟化增强

Microsoft 为在 Hyper-V 上托管 Linux VM 提供了更多改进，包括：

- Microsoft Hyper-V 支持作为根分区运行。
- Microsoft Hyper-V 支持为 Linux VM 脱机 CPU 核心。

另一个有用的改进是 [基于内核的虚拟机](https://thenewstack.io/how-to-develop-on-a-linux-desktop-with-an-easy-to-use-vm/) (KVM) 功能的持续开发。Kernel 6.15 更新并不深刻，但它们包括：

KVM on Intel:

- 在不保持 MMU 锁支持的情况下老化影子页表条目 (SPTE)，从而实现可扩展性和稳定性。
- 嵌套仿真改进，支持 ARM 架构上的 VGICv3。
- 中断处理增强功能提高了整个 VM 生命周期内的可靠性，尤其是在拆卸过程中。

KVM 还在 AMD 处理器上获得了总体性能和稳定性改进。

### CPU 增强

新内核继续利用 CPU 创新来提高效率、能力和安全性。CPU 增强功能包括：

- 用于 x86 架构的引导参数 setcpuid=，以改进虚拟化。
- AMD Zen 6 CPU 核心识别，为下一代 EPYC 和 Ryzen 处理器添加内核识别。
- ARMv9 支持改进
- RISC-V 指令集更新。
- Turbostat CPU 监控功能从 1024 个核心增加到 8192 个核心，以支持更强大的系统。
- LoongArch 支持提高了此架构的稳定性和可靠性，并在 [kernel 6.12](https://thenewstack.io/linux-kernel-6-13-stands-ready-with-security-performance-driver-updates/) 上完成的工作的基础上不断发展。

### 内存增强

内存管理在 kernel 6.15 中受到关注。具体来说，您现在可以控制巨页初始化的并行化，从而大大缩短了分配大量巨页的系统的启动时间。这些页面本身有助于提高内存密集型工作负载的性能。该选项优化了它们在启动时的分配。

将 hugetlb_alloc_threads= 引导参数添加到您的内核命令行以启用此功能。例如，添加值 4 以分配四个线程。您应该会注意到围绕扩展 VM、具有大量内存的服务器或依赖巨页的服务器的最大差异。

### GPU 增强

内核的新增强功能随着 GPU 在现代处理中的日益重要而继续发展。各种当前和未来的增强功能都进入了最新的内核，包括：
- 用于 [NVIDIA GPU](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/) 的 NOVA 开源驱动程序，使用 NVIDIA 的 GSP 固件早期阶段支持。
- Intel Xe 开源驱动程序支持，增加或改进电源管理和共享虚拟内存。它还集成了直接渲染管理器 (DRM) 增强功能，以保持与 Linux 图形堆栈的兼容性。
- AMD RX 9070 系列风扇速度报告改进。（请注意，内核 6.13.5 或更高版本需要支持这些设备的完整功能集。）
- 添加了 Broadcom BCM74110 散热驱动程序，以改进温度控制。
新的内核通过引入标准化的用户空间报告机制，直接关注挂起的 GPU。此功能改进了对应用程序和桌面环境的支持，以提醒用户并响应 GPU 挂起，而与硬件和驱动程序无关。

### 存储和文件系统增强

增加[存储容量](https://thenewstack.io/storage/)始终是系统管理员非常关心的话题。此内核中的存储增强相对较小，但仍然提供有用的功能，针对 Btrfs、XFS、NTFS3 等。改进包括：

- FUSE 下的文件名长度限制从 1024 增加到 4095，远高于其他文件系统（ext4 和 XFS 将名称限制为 255 字节）。
- 通过输入验证和错误处理，ext4 强化了针对模糊（故意损坏）文件系统问题的防御能力。
- 添加了 ext4 的写时复制支持，以提高性能。
- 块大小现在可以大于页面大小，从而实现更灵活的文件系统配置。
- Btrfs 文件系统上的 Zstd 数据压缩快速/实时改进。
- 大型原子写入组件，最终将支持 ext4 和 XFS 下的此功能，从而提高可靠性和性能。

### 网络增强

所有 Linux 内核版本都包含大量的驱动程序更新。各种网络设备驱动程序都出现在 6.15 内核中，包括：

- 网络堆栈中的 IPv6 改进，以支持地址生成和数据包处理。

### 安全缓解措施

新内核解决了有关 Spectre v2 变体和相关系统漏洞的问题。虽然域隔离最初被认为可以缓解 Spectre v2 问题，但某些变体规避了缓解措施，从而引发了其他安全问题。Training Solo 类变体可以利用域内的分支预测器来暴露数据。

Linux kernel 6.15 包含旨在解决 AMD 和 Intel 处理器上的 Training Solo 安全漏洞的补丁。

## 总结

从性能增强到安全缓解再到集成功能，最新的 Linux 内核不断推动操作系统的发展。此内核可能会引起那些关注 Spectre v2 漏洞、运行具有大量 RAM 的系统或需要最新设备驱动程序的人的兴趣。

与往常一样，您可以等待您喜欢的发行版将新内核集成到其更新机制中。如果您急于开始使用其中一些功能，或者想要内核 6.15 中包含的安全/性能优势，请从[Linux 内核档案](https://www.kernel.org/)或 Linus Torvalds 的 [Linux Git 树](https://web.git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git)下载它。