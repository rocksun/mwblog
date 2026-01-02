<!--
title: MocaccinoOS：更易用的Gentoo Linux
cover: https://cdn.thenewstack.io/media/2025/07/58fb1d75-mocaccinohero-2.jpg
summary: MocaccinoOS是基于Gentoo的极简Linux元发行版。它通过Calamares简化安装，采用容器化设计、原子升级，并使用Luet包管理器。适合寻求稳定、轻量级系统的Linux爱好者和开发者。
-->

MocaccinoOS是基于Gentoo的极简Linux元发行版。它通过Calamares简化安装，采用容器化设计、原子升级，并使用Luet包管理器。适合寻求稳定、轻量级系统的Linux爱好者和开发者。

> 译自：[MocaccinoOS Is a More User-Friendly Version of Gentoo Linux](https://thenewstack.io/mocaccinoos-is-a-more-user-friendly-version-of-gentoo-linux/)
> 
> 作者：Jack Wallen

Gentoo 曾是每个用户都渴望构建的 Linux 发行版，以便将其作为荣誉的徽章。

过去，[Gentoo Linux](https://www.gentoo.org/get-started/about/) 仅适用于那些具备高超 [Linux 技能](https://thenewstack.io/introduction-to-linux-operating-system) 的用户。唯一更具挑战性的发行版是 [Linux From Scratch](https://www.linuxfromscratch.org/lfs/)（它本质上是构建你自己的发行版）。

Gentoo 是一个你需要从源代码编译所有内容（包括操作系统）的发行版。安装这个发行版是一项巨大的挑战，需要很长时间才能完成，而且要完美地完成。

我安装过几次 Gentoo，每次都想：“这是我最后一次尝试了。”

但是，正如所有 [Linux](https://thenewstack.io/learning-linux-start-here/) 的情况一样，Gentoo 的演变带来了一些变化和一些分支，它们旨在使开源操作系统的安装变得简单得多。其中一个发行版就是 MocaccinoOS。这个操作系统的标语是：“MocaccinoOS 是面向 21 世纪的极简 Linux 元发行版！”

MocaccinoOS 的主要特性包括：

* 专注于极简主义、小巧的体积和易用性。
* 原生（纯净）上游内核。
* 提供两种版本：Mocaccino Micro 使用基于容器的静态包管理器 Luet；Mocaccino Desktop 曾是 Gentoo 的 Sabyon 分支。
* 它是一个元发行版，这意味着它可以用于引导其他操作系统。
* 它是云优先的，这意味着它包含对最重要的云技术的支持。
* 提供 GNOME、KDE Plasma、MATE 和 Xfce 版本。

在我看来，MocaccinoOS 最重要的一个方面是它使用了 Calamares 安装程序（图 1），这是一个用户友好的图形安装程序，完全是点击式操作。最重要的是，你还会得到一个 GUI 包管理器（取决于你使用的版本），用于安装应用程序和更新软件。MocaccinoOS 还包含了 [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)，这意味着在 GUI 中内置的 Flathub 支持的帮助下，你可以安装 Slack 和 Spotify 等专有应用程序。

[![截图](https://cdn.thenewstack.io/media/2025/07/8d91420a-mocaccinoinstall.jpg)](https://cdn.thenewstack.io/media/2025/07/8d91420a-mocaccinoinstall.jpg) 

*图 1：MocaccinoOS 的安装与任何 Linux 发行版一样简单。*

但是，如果你打算使用 Gentoo，为什么要选择一个用户友好的版本呢？Gentoo 的全部意义不就是展示你的技能吗？

因为 MocaccinoOS 具有创新性。这样想：[MocaccinoOS](https://www.mocaccino.org/docs/) 完全是关于基于容器的软件，它采用不可变设计，使用原子升级并提供用户友好的版本。对于任何将可靠性和稳定性放在操作系统考虑因素首位的人来说，MocaccinoOS 都难以抗拒。

当然，应用程序的安装可能需要更长的时间，但最终结果绝对值得。

MocaccinoOS 一个非常重要的特点是它将系统组件容器化，这意味着更快、更可靠的更新，更简洁的回滚和更好的应用程序隔离。

最终结果是一个闪电般快速、高度稳定的 Linux 操作系统，它将为你提供出色的服务。

我快速安装了 MocaccinoOS（从没想过我会对一个基于 Gentoo 的操作系统说这样的话）。我选择的版本包含了 [KDE Plasma](https://thenewstack.io/linux-desktop-what-makes-kde-plasma-so-appealing/) 桌面环境，我喜欢这个发行版竟然默认使用了浅色主题！我厌倦了每个 Linux 发行版都默认使用深色主题。这个 KDE Plasma 版本甚至默认启用了浮动面板，并加入了恰到好处的透明度，使 UI 看起来现代而简洁。

## Luet 工具

Luet 是一个静态的 Golang 包管理器，它使用 SAT 和 RL 方法解决依赖问题。事实上，Luet 让升级这个基于 Gentoo 的操作系统变得非常容易，只需一个命令：

```
sudo luet upgrade -y
```

Luet 快速且用户友好（图 2）。

[![命令行进度条](https://cdn.thenewstack.io/media/2025/07/ecbdfe9e-mocaccinoluet.jpg)](https://cdn.thenewstack.io/media/2025/07/ecbdfe9e-mocaccinoluet.jpg)

*图 2：Luet 和 apt 或 dnf 一样易于使用。*

当 MocaccinoOS 还是 Sabyon 时，开发人员意识到原始的包管理器 (Entropy) 存在问题，这些问题是：

* 没有简单的可重现构建路径。
* 缺少分歧的软件包。
* 缺少原生的分布式编译。
* 构建服务器不灵活，一次只能容纳一个用户。
* 需要特定的基础设施知识和工具。
* 无法跟踪构建服务器上的更改。

这些问题促成了 Luet 的创建，它抽象了容器层，使一切变得更加简单和可靠。

MocaccinoOS 已经存在了一段时间，所以它有足够的时间成熟，并且它确实成熟了。我对这个发行版的稳定性（以及易用性）印象深刻。

## 内置软件

开箱即用，你不会发现大量预装软件。在 KDE Plasma 版本中，你将获得一套 Qt 开发工具、KolourPaint、Okular、Firefox、KDE Connect、VLC 媒体播放器、Phonon 音视频播放器以及常见的实用工具集。好消息是，你所需要做的就是启动 Discover 来安装你需要的任何应用程序（图 3）。

[![截图](https://cdn.thenewstack.io/media/2025/07/459c6785-mocaccinoldiscover.jpg)](https://cdn.thenewstack.io/media/2025/07/459c6785-mocaccinoldiscover.jpg)

*图 3：在 MocaccinoOS 上使用 Discover 与任何发行版一样简单。*

搜索你想要的软件，然后点击“从 Flathub 安装”来添加应用程序。

## MocaccinoOS 适合谁？

如果这是 Gentoo，我会说它只适合拥有大量 Linux 经验的用户。然而，鉴于开发人员竭尽全力简化了 Gentoo，我会说这个发行版非常适合 Linux 爱好者、开发人员、工程师、重视安全的用户以及任何寻求轻量级、可靠操作系统的用户。但是，如果你是 Linux 的新手，我建议你在深入了解 MocaccinoOS 之前，最好先对 Linux 的工作原理有一个基本的了解。

如果我成功引起了你的兴趣，请前往官方网站，[下载 ISO 镜像](https://github.com/mocaccinoOS/mocaccino/releases)，将其刻录到 USB 驱动器上，并将其安装到备用机器（或作为虚拟机）上。我想你会对这次体验感到满意。