<!--
title: Linux 6.18：全新长期支持版内核全解析
cover: https://cdn.thenewstack.io/media/2025/11/36476e17-talos-linux-2.jpg
summary: Linux 6.18发布为新的LTS版，支持至2027年。官方LTS因维护者倦怠缩短为两年，但企业发行版提供更长支持。6.18改进了内存和网络，并加强了硬件兼容性，但移除了Bcachefs。
-->

Linux 6.18发布为新的LTS版，支持至2027年。官方LTS因维护者倦怠缩短为两年，但企业发行版提供更长支持。6.18改进了内存和网络，并加强了硬件兼容性，但移除了Bcachefs。

> 译自：[Linux 6.18: All About the New Long-Term Support Linux Kernel](https://thenewstack.io/linux-6-18-all-about-the-new-long-term-support-linux-kernel/)
> 
> 作者：Steven J. Vaughan-Nichols

[Linus Torvalds](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/) 对 Linux 内核 6.18 版本发布前最后几天的进展并不满意。这位 Linux 内核创建者在 11 月 30 日的 Linux 内核邮件列表中写道：“[如果发布前最后一周的错误修复噪音能少一点，我会更开心](https://lkml.org/lkml/2025/11/30/341)。”

不过，他补充说：“虽然修复工作比我预期的要多，但并没有让我觉得需要更多时间来完善。所以 6.18 已经打上标签并发布了。”

现在 6.18 版本已经完全成熟，它包含了哪些“成分”？对于 Linux 内核来说，“长期支持”到底意味着什么？

| **内核版本** | **2025 年 12 月状态** | **上游计划的生命周期结束 (EOL)** | **备注** |
| --- | --- | --- | --- |
| 6.18 | 新的 LTS | 2027 年 12 月 | 于 2025 年 12 月初指定为 LTS；第六个活跃的 LTS 分支。 |
| 6.12 | LTS | 2026 年 12 月 | 也被选为民用基础设施平台 (CIP)；[超长期支持内核，最长可达 10 年支持](https://www.zdnet.com/article/super-long-term-stable-linux-kernel-arrives/)。 |
| 6.6 | LTS | 2026 年 12 月 | 于 2023 年末标记为 LTS；广泛用作稳定的企业/桌面基础。 |
| 6.1 | LTS | 2027 年 12 月 | 被多个发行版和嵌入式供应商使用的长生命周期分支。 |
| 5.15 | LTS | 2026 年 12 月 | 常见于企业发行版和长期硬件支持堆栈。 |
| 5.10 | LTS | 2026 年 12 月 | 较旧的 LTS，仍在维护并广泛部署（例如 Debian 11，一些嵌入式系统）。 |

曾几何时，Linux 内核的长期支持版本能获得六年的长期支持（LTS）。现在情况不再如此。在 2023 年，[内核开发者将 LTS 缩短到两年](https://www.zdnet.com/article/long-term-support-for-linux-kernel-to-be-cut-as-maintenance-remains-under-strain/)。

为什么？因为 Linux 代码维护者一直[处于倦怠状态](https://thenewstack.io/how-to-recognize-recover-from-and-prevent-burnout/)。这是一项艰苦的工作。而且，正如 Linux 内核文件系统开发者兼维护者 Josef Bacik 在 2022 年 Linux 存储 | 文件系统 | MM & BPF 峰会上的演讲中提到的，“[维护者们正在倦怠，因为维护者无法扩展](https://www.bilibili.com/video/BV1c14y1b7et/)。”雪上加霜的是，他们也[很少为维护工作获得报酬](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)。

因此，我们只获得了两年的“官方”LTS——最新版本 6.18 的计时从 12 月 3 日开始，当时稳定的 Linux 内核维护者 [Greg Kroah-Hartman](https://www.linkedin.com/in/greg-kroah-hartman) [宣布它正式成为最新的 LTS 版本](https://git.kernel.org/pub/scm/docs/kernel/website.git/commit/?id=b9ea3472ee1d973f4c27d075c7e4445afa7ade89)。此版本也意味着 LTS Linux 5.4 不再获得支持。

## 企业级 Linux 发行版的更长支持周期

等等？你说什么？你和你的客户需要比两年长得多的支持时间？那么，根据你用于生产的发行版，你很幸运。许多顶级企业级 Linux 发行商为他们的付费客户提供远更长的支持周期。

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 为其 [Red Hat Enterprise Linux (RHEL)](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) 内核维护自己的版本，支持 [该发行版 10 年以上的生命周期](https://access.redhat.com/support/policy/updates/errata)。Red Hat 通过将安全修复和选定功能回溯到固定的内核版本来实现这一点，即使上游已经放弃了该分支。RHEL 还为较旧的版本提供[扩展生命周期/扩展生命周期支持 (ELS)](https://www.redhat.com/en/resources/els-datasheet) 附加组件，其中包括超出标准维护的内核安全更新。

[AlmaLinux](https://almalinux.org/ja/) 和 [Rocky Linux](https://rockylinux.org/ja-JP) 等 RHEL 兼容发行版通过自己的重建跟踪 RHEL 的 LTS 内核，有效地将内核维护时间线与相应的 RHEL 版本保持一致，从而延长了用户的内核维护周期。

[OpenELA](https://openela.org/) 是由 [Oracle](https://www.oracle.com/developer?utm_content=inline+mention)、[SUSE](https://www.suse.com/ja-jp/) 和 [CIQ/Rocky Linux](https://ciq.com/products/rocky-linux) 支持的 RHEL 兼容 Linux 发行版，也[通过 RHEL 代码树支持旧内核](https://thenewstack.io/openela-liberates-red-hat-enterprise-linux-source-code/)。此外，[OpenELA 明确介入维护了前 LTS Linux 4.14](https://www.zdnet.com/article/linux-4-14s-long-term-support-will-live-on-after-all-thanks-to-this-alliance/) 直到 2024 年 12 月。尽管如此，OpenELA [在 2025 年仍在发布 Linux 4.14 代码](https://github.com/openela/kernel-lts/releases)。

[Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) 也[在 Amazon Linux 2.0 上支持 4.14](https://docs.aws.amazon.com/ja_jp/AL2/latest/relnotes/relnotes-20250818.html) 直到 2025 年 10 月底，并支持其他已废弃的 5.10 内核直到 2026 年 6 月 20 日。

SUSE 维护着生命周期长的 [SUSE Linux Enterprise Server (SLES)](https://www.suse.com/ja-jp/products/server/) 内核，与 Red Hat 类似，并提供扩展支持选项。从 SLES 16 及其 Linux 6.12 内核开始，[SUSE 现在提供 16 年的支持](https://www.zdnet.com/article/suse-enterprise-linux-16-is-here-and-its-killer-feature-is-digital-sovereignty/)。

最后，[Canonical](https://canonical.com/) 通过附加支持包，[为 Ubuntu 的 LTS 内核提供长达 15 年的维护](https://thenewstack.io/canonical-extends-ubuntu-linux-support-for-up-to-15-years/)。[Canonical 还为 4.14 和其他过时的内核提供 LTS](https://ubuntu.com/kernel)。例如，该公司仍然支持已有 11 年半历史的 Ubuntu 14.04 发行版。

为什么应该使用官方的 LTS 内核或其商业支持的同类版本？这很简单。正如 Kroah-Hartman 在 2020 年欧洲开源峰会“专家问答”采访中说的那样，[它们为开发者提供了一个稳定的应用程序二进制接口（ABI）](https://www.zdnet.com/article/linux-5-10-will-be-the-next-long-term-support-linux-kernel/)。他还说，它还提供[持续的安全补丁流](https://www.zdnet.com/article/kernel-security-now-linuxs-unique-method-for-securing-code/)。这比停留在旧的非 LTS 内核或尝试自行挑选修复方案要安全得多。

## Linux 6.18 有哪些新功能？

6.18 的核心是对 [slab 内存分配器进行了重大升级，以“sheaves”的形式](https://lwn.net/Articles/1010667/)。这是一种每 CPU 缓存机制，可以减少竞争并加速内存分配和释放操作。该版本还包括改进的交换行为和其他虚拟机 (VM) 调整，以提高内存压力下的性能，尤其是在繁忙的服务器和桌面上。

最明显和最具争议的变化之一是，实验性的 [Bcachefs 文件系统](https://bcachefs.org/) 被从主线内核中移除。Bcachefs 是一种通用的 Linux 文件系统。它专为需要强大数据完整性和高级存储功能的系统而设计。实际上，它旨在承担与 [Btrfs](https://btrfs.readthedocs.io/en/latest/Introduction.html) 或 [ZFS](https://zfsonlinux.org/) 许多相同的角色：充足的本地存储、多磁盘阵列以及结合 SSD 和 HDD 以实现性能和容量的设置。

Bcachefs 被踢出内核，很大程度上是因为其维护者 [Kent Overstreet](https://www.linkedin.com/in/kent-overstreet-8a281123/) [与包括 Torvalds 在内的内核维护者就补丁时机、审查实践和公共沟通方面发生了冲突](https://lwn.net/Articles/1035736/)。在个人争论的背后，还有一个技术问题：内核维护者表示，Bcachefs 代码修复通常来得太晚，这与内核在发布候选阶段寻求稳定的偏好相冲突。

Torvalds 和其他维护者认为，那种经常需要后期修改的代码还不属于上游，尤其是对于文件系统这样关键的组件。Bcachefs 现在作为 [动态内核模块支持 (DKMS)](https://wiki.archlinux.org/title/Dynamic_Kernel_Module_Support) 模块发布，并在内核树之外进行维护。希望支持 Bcachefs 的发行版必须构建并发布该外部模块。

在网络方面，Linux 6.18 在 TCP 中添加了对 [精确显式拥塞通知 (AccECN)](https://datatracker.ietf.org/doc/draft-ietf-tcpm-accurate-ecn/) 的支持。这实现了更细粒度的拥塞反馈，并可能在负载下获得更好的吞吐量。内核还引入了 PSP 加密的 TCP 连接，这种方法在某些环境中提供硬件友好的卸载特性，作为传统 IPsec 或 TLS 的替代方案。

安全强化仍在继续，支持加密签名的 [BPF](https://thenewstack.io/what-is-ebpf/) 程序。这使得运行时验证的扩展 Berkeley 数据包过滤器 (eBPF) 有效负载成为可能，并改进了安全子系统和多 LSM 配置。

一个值得注意的基础设施变化是能够使用类似文件句柄的对象管理进程命名空间，其精神类似于 [pidfds](https://lpc.events/event/4/contributions/289/404/pidfds.pdf)。这应该会使容器运行时和低级工具更加健壮和抗竞态条件。

此外，[Rust 逐步集成到内核中仍在继续](https://thenewstack.io/rust-linux-and-cloud-native-computing/)，包括支持 Rust Binder 驱动程序。这是 [Google](https://cloud.google.com/?utm_content=inline+mention) 主导的 [Android Binder](https://source.android.com/docs/core/architecture/ipc/binder-overview?hl=ja) 驱动程序的 Rust 重写。这个重要的进程间通信 (IPC) 系统使 Android 设备上的两个进程能够相互通信。

与大多数内核版本一样，6.18 包含大量新的和更新的跨架构驱动程序，包括 x86_64、ARM、RISC-V 等。它还——令人惊喜的是——改进了对最新 GPU、SoC 和存储控制器的支持。它还附带了对流行手持游戏 PC（如 Asus ROG Ally 和 Lenovo Legion Go 2）的修复和增强，以及对笔记本电脑和嵌入式板的更好电源管理和设备树覆盖。

对于最终用户来说，这意味着在跟踪新 LTS 系列的即将发布的发行版上，开箱即用的硬件支持将更好。

对于 Linux 桌面用户——我和 [Jack Wallen](https://thenewstack.io/author/jack-wallen/) 向你们致意——Linux 6.18 的主要好处将是更快、更可扩展的内存分配、改进的网络效率和更广泛的硬件支持，特别是在现代 GPU 和更新的基于 ARM 的系统上。

服务器运营商和云提供商在评估 6.18 作为长期平台时，可能会专注于混合存储的 dm-pcache、新的 TCP 功能和签名的 BPF 基础设施。凭借延伸到 2027 年的支持，并且没有单一的“杀手级”功能，Linux 6.18 将自己定位为一个保守但基础性的版本，许多发行版将在未来几年内以此为标准。