
<!--
title: Oreon Linux：能否成为真正的红帽企业版替代品？
cover: https://cdn.thenewstack.io/media/2025/09/d5e221f8-oreonhero.jpg
summary: 面向企业用户的Linux桌面发行版包括Red Hat Enterprise Linux Desktop、SUSE Linux Enterprise Desktop和Oreon Linux。Oreon Linux基于AlmaLinux，目标是企业用户，并为游戏进行了优化。
-->

面向企业用户的Linux桌面发行版包括Red Hat Enterprise Linux Desktop、SUSE Linux Enterprise Desktop和Oreon Linux。Oreon Linux基于AlmaLinux，目标是企业用户，并为游戏进行了优化。

> 译自：[Is Oreon Linux a True Red Hat Enterprise Alternative?](https://thenewstack.io/is-oreon-linux-a-true-red-hat-enterprise-alternative/)
> 
> 作者：Jack Wallen

列出所有专为企业用户设计的 Linux 桌面发行版。

我想到了[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) [Enterprise Linux (RHEL) Desktop](https://thenewstack.io/red-hat-enterprise-linux-10-an-ai-driven-quantum-ready-platform/) 和 [SUSE Linux Enterprise Desktop](https://thenewstack.io/suse-displays-enhanced-enterprise-linux-at-susecon/)。

就这些了。

当然，你可以选择一个常规的桌面发行版，比如 [Ubuntu](https://thenewstack.io/ubuntu-25-10-replaces-sudo-with-a-rust-based-equivalent/)，并对其进行强化以供企业使用，但如果已经有专门为你的业务设计的发行版，为什么要这样做呢？

首先是成本。

使用这些[企业就绪的 Linux 发行版](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/)的成本，远高于使用（和调整）一个标准的（和免费的）发行版。同样，你可能不想处理供应商锁定。最重要的是，我使用过这些企业 Linux 桌面，它们往往不如其他发行版那样用户友好。

## 什么是 Oreon Linux？

好消息是，还有其他的选择，其中一个叫做 [Oreon Linux](https://oreonproject.org/)。这个 Linux 发行版的目标是企业组织，但带有一丝简洁。Oreon Linux 附带更友好的默认设置、持续更新，并倾向于 Red Hat Enterprise Linux 的稳定性和安全性。

这个基于 GNOME、企业就绪的 Linux 桌面包括到 2030 年 8 月 20 日的主流支持，以及到 2035 年 6 月 1 日的寿命终止。虽然 Oreon 可能表明它是基于 RHEL 的，但它实际上是基于一个基于 RHEL 的发行版。这个发行版是 [AlmaLinux](https://thenewstack.io/almalinux-10-beta-supports-older-x86-chipsets/)。

Oreon Linux 旨在满足日常用户在日常计算方面的需求。但 Oreon Linux 不仅仅适用于企业。如果你正在寻找一个更安全的家用 Linux 桌面发行版，Oreon 可以帮助你。

## 预装软件的极简主义方法

想象一下，有一个桌面 Linux 发行版，例如 Ubuntu 或 Fedora，它基于企业就绪的 AlmaLinux。这种组合对于家庭和小型企业用户来说可能是一个真正的福音。

Oreon Linux 附带 kernel 6.12.0-55，但限制了包含的软件数量，使其更接近裸机状态。开箱即用，你不会找到办公软件、电子邮件客户端或更多其他内容。你有一个 Web 浏览器 (Firefox)、一个文本编辑器 (GNOME Text Editor) 和一些实用程序。仅此而已。

当然，总是有应用商店，你可以在其中选择数千个要安装的应用程序。Oreon 确实包括 Flatpak，因此有更多的应用程序可以安装；但是，Flatpak 支持并未内置到图形用户界面 (GUI) 应用商店中。幸运的是，这可以通过以下命令轻松解决：

```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

添加 Flathub 存储库后，你应该可以在 GNOME Software 中找到 [Flatpak 应用程序](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)。为什么不将其作为默认行为？

继续。

正如我提到的，没有很多预装的应用程序，包括用于更高级功能配置的 GUI。当然，这是经过设计的。我从很多用户那里听说过，他们采用了 openSUSE 作为桌面，当他们打开 Yet another Setup Tool (YaST) 时，他们睁大了眼睛。YaST 非常强大，最好由新用户自行决定是否使用。

## 使用 Cockpit Web GUI 进行高级配置

好消息是，Oreon Linux 默认启用基于 Web 的 Cockpit GUI，因此你只需将浏览器指向 <http://localhost:9090>，就可以使用比 GNOME 设置更强大的工具（图 1）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/fe201674-oreoncockpit.jpg)](https://cdn.thenewstack.io/media/2025/09/fe201674-oreoncockpit.jpg)

*图 1. 基于 Web 的 Cockpit GUI 是管理 Oreon 安装的出色工具。*

使用 Cockpit，你可以管理日志、存储、网络、帐户、服务、Anaconda、应用程序、SELinux、更新等。

## 关于其 Red Hat Enterprise Linux 连接的真相

与 Oreon Linux 相关的一个棘手问题是。Oreon 项目网站声称它基于 Red Hat Enterprise Linux，但事实并非如此，这种说法可能会给该项目带来麻烦。事实是，Oreon Linux 基于 AlmaLinux，而不是 Red Hat Enterprise Linux。

当然，这引出了一个不同的问题：为什么要这样做？从本质上讲，Oreon Linux 是一个重新命名的 AlmaLinux，添加了一些额外的调整，使其成为一个开箱即用的更可行的桌面发行版。是的，确实如此，但它确实有一些调整，可能会使其对桌面用户更具吸引力。更大的调整之一是包含安装和使用 Wine/Proton 进行游戏所需的依赖项，以及未包含的架构和损坏的软件包。因此，如果你一直梦想使用 AlmaLinux 作为游戏平台，Oreon 可能就是你想要的。

只需打开 GNOME Software 并搜索“proton”。该搜索将显示几个应用程序（例如 ProtonUp-Qt），你可以安装这些应用程序以使在 Linux 上进行游戏更容易（根据应用程序本身）。ProtonUp-Qt 简化了 Steam 的 Proton-GE 和 Lutris 的 Wine-GE 的安装和管理。作为测试，我安装了 ProtonUp-Qt，看看它是否能让设置变得更容易。令我惊讶的是，它确实做到了。

只需选择你的下载目录，添加一个版本并安装（图 2）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/92cef8a1-oreon2.jpg)](https://cdn.thenewstack.io/media/2025/09/92cef8a1-oreon2.jpg)

*图 2. 此应用程序应该可以简化游戏设置。*

Proton 的作用是使在 Linux 上运行 Windows 游戏成为可能（在 Steam 的帮助下）。安装 ProtonUp-Qt 并添加/安装版本后，你就可以在 Steam 中启用 Proton 并运行这些 Windows 游戏 - 无需单独安装 Proton。

这是否足以吸引你使用 Oreon Linux？如果你想要一个基于 AlmaLinux 的桌面操作系统，它可以让游戏变得更容易，这当然是一个选择。但是，就 Linux 上的游戏而言，你最好选择一个专门用于游戏的发行版，例如 [Bazzite](https://bazzite.gg/) 或 [Drauger OS](https://bazzite.gg/)。