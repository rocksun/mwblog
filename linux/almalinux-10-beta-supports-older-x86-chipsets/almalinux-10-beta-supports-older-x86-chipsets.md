
<!--
title: AlmaLinux 10 Beta版支持较旧的x86芯片组
cover: https://cdn.thenewstack.io/media/2025/01/8cb805c6-alma10.jpg
-->

AlmaLinux 10自带新的sudo系统角色，用于简化配置管理，以及Sequoia PGP工具，用于更高级的加密。

> 译自 [AlmaLinux 10 Beta Supports Older x86 Chipsets](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/)，作者 Jack Wallen。

曾经，追踪[Red Hat Enterprise Linux](https://www.openshift.com/try?utm_content=inline+mention) 的克隆版本相当容易。但后来情况变得有点棘手，导致了一些混乱。以当前 AlmaLinux 的状态为例。

有一个常规版本，可以作为 Red Hat Enterprise [Linux](https://thenewstack.io/introduction-to-linux-operating-system) 的直接替代品。然后是[Kitten](https://thenewstack.io/almalinux-kitten-offers-preview-of-distros-next-release/)，它是 AlmaLinux 的[CentOS Stream](https://thenewstack.io/almalinux-makes-in-place-upgradeseasier-for-centos-users/)（即 RHEL 的上游）克隆版本。大多数企业都不想费心使用 Kitten，因为他们需要可用于生产环境的操作系统。另一方面，开发人员应该考虑将 Kitten 作为他们的首选平台。

如果你想让一切清晰明了，记住这一点：AlmaLinux Kitten 不使用 Beta 版本，因为它只是 CentOS Stream 的重新构建版本。然而，AlmaLinux 10 使用 Beta 版本。但是，为什么基于另一个操作系统的操作系统还需要 Beta 版本呢？从本质上讲，AlmaLinux 团队并非试图创建 RHEL 代码的精确副本，而是创建 RHEL 提供的*体验*的逐一功能克隆。

这有很大的区别。

## 较旧的芯片组

由于 AlmaLinux 处理新版本的方式，开发团队能够进行更改。他们所做的更重要的更改之一是通过支持方式实现的。当 Red Hat[迁移到 x86-64-v3 芯片微架构](https://developers.redhat.com/articles/2024/01/02/exploring-x86-64-v3-red-hat-enterprise-linux-10)时，它停止了对先前版本的支持。另一方面，AlmaLinux 不仅限于支持 v3，还继续支持 v2（因此，使用较旧硬件的用户不会像 Windows 10 用户尝试迁移到 Windows 11 时那样陷入同样的陷阱）。

根据 AlmaLinux 的变更日志，“在 AlmaLinux OS 10 中，我们将遵循 Red Hat 的决定，默认情况下交付经过 x86-64-v3 优化的二进制文件，但我们还将仅为较旧的硬件提供额外的 x86-64-v2 架构。所有 RHEL 10 的第三方软件包都将面向 x86-64-v3，而 AlmaLinux OS 10 的 x86-64-v2 版本仅适用于使用默认操作系统软件包集就足够或用户能够自己为 x86-64-v2 架构重新构建任何其他所需软件包的工作负载。”

还有其他与 RHEL 的偏差，例如默认情况下重新启用帧指针，重新启用服务器和客户端应用程序的 SPICE 支持，Firefox 和 Thunderbird 作为常规 RPM 软件包（而不是 Flatpak）发布，以及修改了几个设备驱动程序以重新添加 PCI ID。

对于那些不是开发人员的人来说，标准的 AlmaLinux 版本是最佳选择，并且有很多更新，例如 Python 3.12、Ruby 3.3、Node.js 22、Perl 5.40、PHP 8.3、Git 2.45、Apache 2.4.62、NGINX 1.26、Varnish Cache 7.4、Squid 6.10、MariaDB 10.11、MySQL 8.4、GCC 14.2、glibc 2.39、binutils 2.41、GDB 14.2、Grafana 10.2.6、Rust Toolset 1.79.0、Go Toolset 1.22 等等。

## Linux 安全性

就安全性而言，AlmaLinux 10 通过对后量子密码学的支持为操作系统带来了一个关键变化。这样做可以确保操作系统能够抵御量子计算机更复杂的加密能力，以解决目前可能并非首要关注的问题，但随着量子计算机变得越来越容易获得，该平台将做好准备。新版本还包含对 SELinux 的一些重要更新，例如对策略模块、工具和实用程序的升级，这些工具和实用程序使您可以更精细地控制安全配置。策略将更容易维护，并且执行更加一致。

还有一个新的[sudo 系统角色](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)，用于简化管理员的配置管理，以及添加 Sequoia PGP 工具 (sq 和 sqv) 以实现更高级别的加密。

我将 AlmaLinux 10 Beta 作为虚拟机安装以查看其性能，并且毫不意外地发现它几乎完美无瑕。我使用 RHEL 克隆版本时总是做的第一件事是启用 Cockpit (*sudo systemctl enable cockpit.socket*) 以查看情况，一切看起来都非常熟悉。

对于那些喜欢带有 GUI 的服务器的用户，AlmaLinux 附带 GNOME 47.alpha，并且仅包含最少的用户界面应用程序（Firefox、GNOME Software、GNOME 文本编辑器、计算器、Tour、相机、时钟、系统监视器、设置、GNOME 终端、磁盘、图像查看器、字体管理器，但仅此而已。你找不到通常的 GNOME 应用程序，例如天气和地图，你也不会在应用程序概述中找到任何媒体播放器。
记住，这是一个服务器操作系统，所以这并不奇怪。

我遇到的唯一一个AlmaLinux 10 beta 的问题是 mcelog 服务无法启动。这是什么？Mcelog 是用于记录硬件向内核报告的机器检查错误的用户空间后端服务。根据服务日志，发生这种情况是因为我的 CPU 不受支持（AMD Ryzen）。解决方法很简单：

在 Cockpit 服务选项卡中禁用 mcelog，然后启用 rasdaemon：

```bash
sudo systemctl enable --now rasdaemon
```

错误消失。

除此之外，以及性能的显著提升，使用 AlmaLinux 10 beta 与使用之前的任何版本一样流畅和轻松。这并不是说你应该在生产环境中使用 AlmaLinux 10 beta。恰恰相反。但我强烈建议您下载测试版，并在正式发布之前开始熟悉新的安全增强功能。你肯定不想花时间去学习新的后量子密码学或新的 sudo 系统角色。

如果您有兴趣试用 AlmaLinux 10 beta，您可以[从官方下载页面下载 ISO 镜像](https://repo.almalinux.org/almalinux/10.0-beta/isos/)。
