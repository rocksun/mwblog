# Oreon Project：更友善的企业 Linux 发行版

![Oreon Project：更友善的企业 Linux 发行版 的特色图片](https://cdn.thenewstack.io/media/2025/02/c3b1cdcb-oreonhero-1024x643.jpg)

你是否曾好奇，为什么更多的人不使用 [AlmaLinux](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/)、[CentOS Stream](https://thenewstack.io/back-to-the-future-a-look-at-centos-streams/) 或 [Rocky Linux](https://thenewstack.io/ciq-unveils-a-version-of-rocky-linux-for-the-enterprise/) 这样的发行版作为桌面操作系统？毕竟，这些发行版非常稳定且安全。这听起来不像是一个理想的桌面操作系统的配置吗？

不。

好吧，是的，听起来确实像……但这并不意味着人们会这样使用它。为什么？复杂。我并不是说这些企业级操作系统很复杂，因为它们并不复杂——至少对于需要可靠服务器操作系统的经验丰富的 Linux 用户来说不是。

但对于桌面用户来说，像 CentOS Stream 这样的系统是不可想象的。是的，你当然可以把它用作桌面操作系统，但当你要做额外的工作才能让它更好地为你服务时，你为什么要这样做呢？

这就是 [Oreon Project](https://oreonproject.org/oreon-10/) 发挥作用的地方。

Oreon Project 的主要目标是使企业 Linux 更适合作为桌面（或笔记本电脑）操作系统。为此，开发人员专注于默认情况下提供最佳用户体验。

Oreon 最大的惊喜之一是，它的首席开发人员 Brandon Lester 是一名高中生，他管理着一个小团队来实现 Oreon。他做得非常出色。

## 一种新型的企业 Linux

当我开始安装操作系统时，我意识到 Oreon 完全不同。我非常了解基于 Fedora 的安装程序；它易于使用且非常稳定。但是，Linux 新手可能会被安装操作系统的步骤吓倒。

幸运的是，Oreon 采用了一种更像 Ubuntu 的安装向导方法（**图 1**），这大大提高了安装的用户友好性。

![安装截图。](https://cdn.thenewstack.io/media/2025/02/af2d0230-oreoninstall.jpg)

图 1：Oreon 的安装是一个点击式的过程，任何人都应该立即熟悉。

Oreon 安装程序只需要点击四次鼠标，因此你可以确定任何人都可以安装此操作系统。

## 预装的应用程序和 Flatpak 支持

Oreon 附带 KDE Plasma 桌面和最少的应用程序。幸运的是，你可以从 Discover 应用商店安装你需要的任何东西，并且为了安全起见，添加了 Flatpak，还有更多的应用程序可供安装。唯一的缺点是 Discover 没有内置 Flatpak 支持。幸运的是，有一个非常简单的解决方法。如果你打开 Discover 并单击“设置”，你会在右上角附近找到一个“添加 Flathub”按钮（**图 2**）。

![KDE Discover 应用的截图。](https://cdn.thenewstack.io/media/2025/02/1afc55a4-oreondiscover.jpg)

图 2：KDE 的 Discover 应用可以轻松添加 Flatpak 支持。

单击“添加 Flathub”，你会发现可用于安装的软件已大大增加。

Oreon 还做了哪些工作来简化其使用？

## SELinux

当我想起 [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux)（现在由 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 维护为开源）时，我看到管理员们围坐在桌面上，试图弄清楚如何告诉 SELinux 允许某些东西工作。我使用过 SELinux，并且了解它有多么令人生畏。

更正一下——它有多么*难*以使用。

Oreon 附带了一个方便的 SELinux GUI，名为 SELinux Alert Browser。如果某个事件或进程触发了 SELinux，你可以使用 Alert Browser 查看正在发生的事情，然后决定进行故障排除、通知、忽略或删除（**图 3**）。

![SELinux 可视化界面。](https://cdn.thenewstack.io/media/2025/02/34312d92-oreonselinux.jpg)

图 3：借助此 GUI，SELinux 更易于管理。

该应用程序的故障排除功能非常出色，甚至为你提供了帮助解决问题的选项（从“故障排除”部分中）。

但是，是什么真正使 Oreon 与其他企业级发行版区分开来，以及你为什么要将其用作桌面操作系统？

以下是使 Oreon 与竞争对手区分开来的主要卖点，作为一个桌面操作系统：
**用户友好**: Oreon 的设计宗旨是欢迎所有技能水平的 Linux 用户，并使其易于使用。无论您是 Linux 新手还是经验丰富的用户，您都应该可以轻松地让这个操作系统为您服务。

**长期支持 (LTS)**: Oreon Lime R2 的生命周期为八年，这意味着它将获得支持直到 2032 年。

**软件仓库**: Oreon 预装了必要的软件仓库，如 Docker、EPEL、RPM Fusion 和 Flatpak。

**轻量级性能**: Oreon 确保您获得流畅的性能，即使安装在较旧的硬件上也是如此，使其适合于恢复老化的机器。

**游戏功能**: Oreon 团队已经移植了一个可用的 WINE 版本（支持 WINE 32 位和 64 位应用程序），并实施了其他修复，因此它可以流畅地运行基于 Proton/WINE 的游戏。Oreon 还支持游戏启动器，如 Lutris、Steam 和 Bottles。请注意，您确实需要手动安装这些软件包。

当然，像现在很多 Linux 发行版一样，Oreon 默认情况下也带有一个深色主题。但由于这是 KDE Plasma，您可以快速配置它以满足您对浅色主题的所有渴望（**图 4**）。

![](https://cdn.thenewstack.io/media/2025/02/c3b1cdcb-oreonhero.jpg)

图 4：我花了不到两分钟的时间就让 KDE Plasma 看起来完全符合我的要求。

## Oreon 最适合谁？

我认为 Oreon 的目标是成为企业桌面的 AlmaLinux/Rocky Linux/CentOS，并且该团队已经为此做了一个很好的开端。这并不是说 Oreon 不适用于任何桌面，但鉴于该操作系统基于 AlmaLinux，因此将其作为面向企业用户的桌面操作系统是完全合理的。

从我的测试来看，我会说 Oreon 最适合那些想要一个坚如磐石的桌面操作系统，并且在公司内部或在家工作的人。或者，如果您喜欢基于企业级操作系统的 Linux 发行版，并且还加入了游戏功能，那么 Oreon 也是一个非常不错的选择。

如果您对 Oreon 的产品感兴趣，请访问官方网站，[下载 ISO](https://oreonproject.org/download/)，然后将其刻录到 USB 驱动器或使用它启动虚拟机，以了解这个新的 Linux 发行版。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，即可观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)