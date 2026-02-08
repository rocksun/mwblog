<!--
title: Liya Linux：高性能，无需命令行！
cover: https://cdn.thenewstack.io/media/2026/01/c66a7597-liyahero.jpg
summary: Liya Linux是一款用户友好的Arch发行版，特点是易安装、定制Cinnamon桌面和独特预装应用。它通过图形界面管理软件，性能出色，旨在无需命令行即可让Arch普及化。
-->

Liya Linux是一款用户友好的Arch发行版，特点是易安装、定制Cinnamon桌面和独特预装应用。它通过图形界面管理软件，性能出色，旨在无需命令行即可让Arch普及化。

> 译自：[Liya Linux proves high performance doesn’t require a command line](https://thenewstack.io/liya-linux-proves-high-performance-doesnt-require-a-command-line/)
> 
> 作者：Jack Wallen

任何一个[Linux发行版](https://thenewstack.io/choosing-a-linux-distribution/)声称要[让Linux变得简单](https://thenewstack.io/learning-linux-start-here/)并向大众开放，同时还要将自己打造成家庭计算的新行业标准，这都是一个大胆的举动。

但我喜欢这样。当一个Linux发行版能够做出如此大胆的声明时，这意味着他们正在尝试做一些光荣而重要的事情：让Linux人人可用。

问题在于，许多发行版都提出了这样的主张；虽然有些成功了，但有些也失败了。

那么最大的问题是，[Liya Linux](https://liyalinux.gitlab.io)是否兑现了这一承诺？考虑到这个发行版是基于Arch Linux的，这是一个相当冒险的声明。由于Liya Linux对我来说是新鲜事物（这在如今很少见），我将其作为虚拟机（VM）安装，看看它能提供些什么。

安装一开始，我立刻就知道开发者认真对待了这个承诺。与许多现代Linux发行版一样，Liya Linux提供了用户友好的、点击式安装。

直到我第一次登录，我才得以看到开发者所做的一切。

在我深入探讨之前，重要的是要了解Liya使用了[Btrfs文件系统](https://itsfoss.com/btrfs/)，功能齐全，包含快照，并且默认启用了[Samba共享](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/)，还提供了简洁的应用选择，这可能不如某些发行版那么熟悉，但我发现所有预装应用都是日常用户的可行选择。

甚至在我查看应用选择之前，立刻让我震惊的是Liya骗了我。在我决定尝试这个发行版之前，我特意没有事先阅读相关资料，因为我想获得惊喜。一开始，我确实感到非常惊喜。

当我第一次登录时，我以为我正在使用[KDE Plasma桌面](https://thenewstack.io/linux-desktop-what-makes-kde-plasma-so-appealing/)。这是一个很容易的假设，因为它看起来非常像KDE Plasma（带有一些特定于发行版的调整）。桌面很漂亮，并带有KDE Plasma的典型特征。

我万万没想到，这个桌面实际上是一个定制的[Cinnamon](https://thenewstack.io/what-makes-the-cinnamon-desktop-so-appealing/)。

哇。好吧。我原以为我对Linux桌面了如指掌，能在一百米外就能认出来。它看起来像是定制成KDE Plasma的样子，但当你开始探索时，就会发现你（其实是我）错了。

骗我一次……

话虽如此，这是我第一次看到Cinnamon桌面并心想：“我真的很喜欢它。”我常常觉得Cinnamon太无聊、太老派、太像Windows。这个Cinnamon版本恰到好处地融合了现代感，同时仍保留了标准的桌面隐喻，因此可以吸引各种类型的用户。

然而，只有当你浏览应用程序菜单时，你才会意识到Liya很可能是一个面向大众的基于Arch的发行版。

[Manjaro](https://thenewstack.io/manjaro-is-arch-linux-for-newbies/)，小心了。

## 预装应用

这是真正令人印象深刻的地方。首先，Liya脱离了通常的默认安装，选择了[Brave浏览器](https://brave.com/download/)和[ONLYOFFICE办公套件](https://www.onlyoffice.com/desktop)。虽然这个组合对新用户来说可能不那么熟悉，但两者都非常用户友好。我实际上更喜欢ONLYOFFICE而不是LibreOffice，因为它允许我本地和通过云端工作（甚至可以使用基于局域网的ONLYOFFICE服务器安装）。

除了这两个默认应用之外，你还会得到诸如Celluloid（视频播放器）、一些游戏、Deluges（BitTorrent）、Exaile（管理音频收藏）、Geary（电子邮件）、Newelle（聊天机器人，图1）、Pika Backup、Pinta（图像编辑器）、Pix（照片管理器）、Bleachbit（系统清理器）、Firewall配置GUI、固件安装器、Gestures（手势管理器）等等。

![屏幕截图](https://cdn.thenewstack.io/media/2026/01/10690298-liya2.jpg)

*图1：Newelle是一个新颖的应用，使使用AI变得简单。*

有了Newelle，甚至无需安装或连接大型语言模型（LLM），因为它已全部就绪。

最让我印象深刻的是，Liya的开发者在默认预装应用方面采取了一条非传统的道路，但他们却创建了一个满足所有需求的应用集合。鉴于许多发行版都认为最好的前进道路是传统应用，很高兴看到一个发行版采取不同的方法。

## Liya的性能如何？

Arch和Cinnamon的结合造就了一个快速稳定的桌面操作系统。Liya在性能和可用性方面都轻松地与[Linux Mint](https://thenewstack.io/reasons-to-love-linux-mint/)相媲美。

什么？

如果我以为一个基于Arch的发行版能够达到Linux Mint那样的易用性，那我一定是疯了。毕竟，Arch是现有的最具挑战性的Linux发行版之一。尽管这样说很容易，但当你遇到一个完全点击式、包含出色软件集合并在此之上添加了用户友好型应用商店的Arch版本时，它很容易改变一个人的想法。

一些基于Arch的发行版认为用户更喜欢使用命令行。然而，也有一些发行版完全理解大多数人宁愿避免使用命令行，因此它们包含了用于管理软件的GUI。Manjaro是首批这样做的发行版之一，Liya也追随了它的脚步。

讨论中的图形用户界面（GUI）是Pamac，虽然它可能不是现有的最现代化的应用商店，但对于新用户来说，它比尝试理解pacman要容易得多。你所要做的就是打开应用，搜索你想要安装的软件，然后点击安装新的软件。Liya唯一没有包含的是[Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)，这意味着你会错过一些重要的软件，例如Spotify和Slack。

幸运的是，Flatpak可以通过[Pamac](https://itsfoss.com/install-pamac-arch-linux/)轻松安装。只需打开应用商店，搜索Flatpak，然后点击绿色的安装按钮（图2）。

![屏幕截图](https://cdn.thenewstack.io/media/2026/01/980e5c88-liya1.jpg)

*图2：如今安装Flatpak应该被视为必需。*

## 基于Arch的发行版排名

如果我必须在用户友好的基于Arch的发行版中对Liya进行排名，它可能看起来像这样：

Manjaro、Liya、EndeavourOS、Garuda Linux、Artix Linux和CachyOS。虽然我更喜欢EndeavourOS和Garuda，而不是Liya，但这两个选择主要是基于美学。如果我仅从用户友好的角度考虑，Liya紧随Manjaro之后，并且有朝一日可能轻易地与其一较高下。