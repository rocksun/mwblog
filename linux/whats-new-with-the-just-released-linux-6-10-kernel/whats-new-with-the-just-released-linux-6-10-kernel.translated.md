# 新发布的 Linux 6.10 内核有哪些新功能

![新发布的 Linux 6.10 内核的特色图片](https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux-1024x682.jpg)

最新的 Linux 内核 6.10 已经发布。

[Linus Torvalds](https://thenewstack.io/linus-torvalds-on-security-ai-open-source-and-trust/) 对 [Linux 6.10 发布](https://lkml.org/lkml/2024/7/14/250) 前的最后几天并不满意。不过最终，“它也没有吵闹到需要额外发布 rc [候选版本]”。所以，我们现在有了最新的 Linux 内核，可以开始工作了。

这个 2024 年年中内核升级带来了许多令人兴奋的功能和改进，这些功能和改进增强了各种平台的性能、安全性和硬件支持。

Linux 6.10 中最突出的新增功能之一是新的 [Panthor 图形直接渲染管理器 (DRM) 驱动程序](https://www.collabora.com/news-and-blog/news-and-events/release-the-panthor.html)。这段延迟的代码应该在 6.9 Linux 内核中发布，它支持更新的 Arm Mali 图形处理器。这一发展对于围绕 [基于 Arm 的架构](https://thenewstack.io/arm-eyes-ai-with-its-latest-neoverse-cores-and-subsystems/) 构建的下一代设备来说尤其重要。它将提高它们的图形性能和兼容性。

该内核还包括针对 Intel 用户的几个图形增强功能。最重要的是为 Intel 即将推出的 [Xe2 图形](https://www.anandtech.com/show/21425/intel-lunar-lake-architecture-deep-dive-lion-cove-xe2-and-npu4/6) 做了更多准备。

此版本还针对具有错误固件的 Intel Core 混合系统进行了重大性能修复。有多重要？非常重要。在使用 Intel Core i5 13500H 处理器并使用最早的合格虚拟截止日期优先 (EEVDF) 调度程序的系统上，用户不得不忍受高达 [50% 的性能下降](https://www.phoronix.com/news/Linux-6.10-rc6-PM-Intel-Core)。

[AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention) 也已包含在内，为更小的 Ryzen APU 提供了更好的 ROCm/AMDKFD 支持，并为即将推出的 Zen 5 架构添加了新功能。

在更高层面上，6.10 版本还支持 Intel Arrow Lake-H 处理器、联想 Thinkbook 13x Gen 4、联想 Thinkbook 16P Gen 5 和联想 Thinkbook 13X 笔记本电脑，以及华硕 ROG 2024 笔记本电脑。这些电脑以前可以在 Linux 上运行，但它们的 Cirrus CS35L41 音频放大器存在问题。

Linux 6.10 还带来了显著的性能和 [安全改进](https://thenewstack.io/design-system-can-update-greg-kroah-hartman-linux-security/)。用户可以期待在现代 Intel 和 AMD CPU 上实现更快的 AES-XTS 磁盘和文件加密，以及增强的 IO_uring 零拷贝性能。这个最新的内核还引入了 [MSEAL](https://lwn.net/Articles/954936/)。这可以保护给定的虚拟内存范围免受修改，例如更改其权限位。它还实现了可信平台模块 (TPM) 总线加密和完整性保护。

硬件支持已扩展，内核现在支持各种新设备。其中包括华硕 ROG Raikiri Pro 控制器、2024 年 LG 笔记本电脑型号，以及与华硕 ROG 2024 笔记本电脑的改进兼容性。

Linux 6.10 为开发人员和系统管理员提供了几个新功能。Rust 爱好者将对 [RISC-V 架构的 Rust 语言支持](https://thenewstack.io/rust-in-the-linux-kernel/) 最为兴奋。内核中的 Rust 支持也已更新到该语言的最新版本：[Rust 1.78.0](https://blog.rust-lang.org/2024/05/02/Rust-1.78.0.html)。

Linux 6.10 的发布标志着 Linux 内核持续演进的又一个里程碑。随着社区开始采用这个新版本，现在注意力转向了 Linux 6.11 的开发，它的合并窗口已经打开。Linux 内核开发人员的工作永远不会结束！

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)