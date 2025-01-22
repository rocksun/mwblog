# Linux 内核 6.13 增强安全、性能和驱动程序更新

![Linux 内核 6.13 增强安全、性能和驱动程序更新的特色图片](https://cdn.thenewstack.io/media/2025/01/89696443-getty-images-cobtu8xq11c-unsplash-1024x768.jpg)

又到了新的[Linux 内核](https://thenewstack.io/learning-linux-start-here/)发布的时候了！自从[Linux 内核 6.12 发布](https://thenewstack.io/linux-kernel-6-12-is-official-real-time-app-support-better-scheduling/)以来已经过去几个月了，但是新的 6.13 内核的等待现在结束了。[Linus Torvalds](https://thenewstack.io/linus-torvalds-c-vs-rust-debate-has-religious-undertones/)于 2025 年 1 月 19 日向 Linux 社区发布了最新版本。

新版本实现了额外的功能和硬件支持，以提供更高的灵活性和安全性以及性能，特别是对于使用企业级系统的系统管理员和开发人员。更改包括更新的驱动程序、虚拟化改进、额外的架构支持等等。

## 什么是 Linux 内核候选版本？

请注意，新的[Linux](https://thenewstack.io/introduction-to-linux-operating-system) 内核在最终发布之前会经历一系列候选版本 (RC) 阶段。这些阶段为贡献者提供了最终确定代码更新的机会。RC 阶段通常大约为两个月，但时间会根据开发人员解决问题速度而有所不同。

在此阶段不会添加新的功能；只允许修复。Linux 内核 RC 版本从 1 开始递增。例如，在此 RC 阶段，新的 6.13 内核于 2024 年 12 月 2 日以 6.13rc1 开始。

本文总结了 Linux 内核 6.13 中的关键功能，以便您可以决定多快更新您的系统。

## 更新的安全功能

内核 6.13 包括在称为领域的受保护执行环境中运行 Linux 虚拟机 (VM) 的支持，这些领域位于[Arm 机密计算架构](https://www.arm.com/architecture/security-features/arm-confidential-compute-architecture) (Arm CCA) 下。此平台支持从（潜在的）不受信任的执行环境（包括主机操作系统和虚拟化管理程序）中进行[工作负载隔离](https://thenewstack.io/confidential-computing-makes-inroads-to-the-cloud/)。隔离在硬件级别使用受限的地址空间进行。

此增强功能是 2021 年 Armv9-A 版本的一项功能，该版本支持工作站、手机、平板电脑、物联网设备等。它提供安全、AI 和高性能计算功能。具体来说，Arm CCA 引入了称为“领域”的隔离安全状态。Linux 6.13 内核正是利用了这些领域。

新内核还增加了对 64 位 Arm 处理器影子堆栈安全功能的支持，该功能保护用户空间应用程序并提高性能。

最后，内核更新的延迟抢占模型应该通过简化配置选项来提高性能。此更改适用于 x86、RISC-V 和 LoongArch 架构。

## 文件系统更新

对各种 Linux 文件系统的重大改进增加了文件管理的安全性和稳定性。更改包括以下内容：

**XFS**: 添加了原子写入支持，以在断电的情况下保护数据。**ext4**: 添加了原子写入支持，以在断电的情况下保护数据，以及各种代码清理和修复。**Btrfs**: 提高了性能能力。**FUSE**: 添加了配置更新以提高稳定性。

闪存友好型文件系统 (F2FS) 针对闪存存储设备进行了优化，以保持其寿命和性能。它是在内核 3.8 中引入 Linux 的。使用内核 6.13，F2FS 接收设备别名，使用户能够更有效地管理空间。这对于现代固态设备 (SSD) 至关重要。

此外，6.13 内核完全删除了 ReiserFS，结束了其在 Linux 平台上的支持。

## 树莓派视频改进

新的内核也没有忽略[树莓派平台](https://thenewstack.io/the-new-2gb-raspberry-pi-5-another-option-for-linux-sysadmins/)，它为 Broadcom V3D 处理器提供了一个新的内核驱动程序，该驱动程序支持 1MB 的“超级页面”和 64KB 的“大页面”。期待这个驱动程序带来更好的图形性能，继续树莓派在现代计算中的相关性和发展。

## 额外的驱动程序支持

更新的内核包括对特定处理器、图形处理器、音频和网络芯片的额外支持。诸如戴尔的 WMAX 热接口之类的工具为来自不同供应商的笔记本电脑添加了新的管理功能。
越来越多的外围设备受益于不断发展的Linux驱动程序，包括Apple的妙控触控板2（USB-C版）、游戏鼠标和耳机。每个内核版本都会为Linux添加更多驱动程序，使其能够跟上持续推动外围设备发展的巨大硬件增长。

## 还有什么？

其他功能涵盖的领域太多，无法完整记录，但在网络、存储、内存利用率和各种处理器架构方面都存在新的功能。以下一些更新值得关注：

**网络**: 侧重于每个网络命名空间锁的性能改进和功能。
**LoongArch**: 对实时计算和其他杂项更新的支持。
**SD超大容量 (SDUC)**: 支持将来在SD卡上实现128TB存储。
**WireGuard VPN**: 支持用于VPN连接上的网络密集型工作负载的大型TCP GSO。
**SELinux**: 通过对特定网络链路实施策略来提高性能的改进。

另一个新功能是对iPhone/iPad A7到A11芯片的基本支持，这使得未来在较旧的Apple硬件上运行Linux的开发和功能成为可能。另一个面向Apple的功能是某些Mac平台上的ACPI背光功能。

最后，内核6.13继续将[Rust](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/)集成到内核开发过程中，并使用就地模块。这是一项从内核6.12开始的持续工作。预计在接下来的几个内核版本中将会有更多基于Rust的开发功能。

## 总结

虽然内核6.13并非革命性的变化，但它代表了6.x内核系列的持续增长和成熟。这些进步保持了Linux在云服务和服务器平台上的主导地位。客户端设备可能无法体验到相同的好处（树莓派除外），但服务器端的改进是受欢迎的。

预计2025年2月2日将看到内核6.14的第一个候选版本，最终版本很可能在3月底发布。

如果您无法等待您最喜欢的发行版在其下一个版本中包含这个新内核，您可以从[Linus Torvalds自己的Git仓库](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/snapshot/linux-6.13.tar.gz)或[kernel.org](https://www.kernel.org/)下载它。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)