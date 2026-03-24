<!--
title: Exton Linux ExLight：轻量亦能让你眼前一亮！
cover: https://cdn.thenewstack.io/media/2026/03/16091dcc-bekeen-co-tmjvp6tcyri-unsplash-1.jpg
summary: ExLight是基于Debian 13的轻量级Linux发行版，采用Enlightenment桌面环境。它兼具高效、简洁与现代感，运行流畅，即使在旧硬件上表现出色。虽预装应用精简，但可通过多种包管理器扩展。作者强烈推荐尝试。
-->

ExLight是基于Debian 13的轻量级Linux发行版，采用Enlightenment桌面环境。它兼具高效、简洁与现代感，运行流畅，即使在旧硬件上表现出色。虽预装应用精简，但可通过多种包管理器扩展。作者强烈推荐尝试。

> 译自：[Exton Linux's light version will "enlighten" you](https://thenewstack.io/exton-linuxs-light-version-will-enlighten-you/)
> 
> 作者：Jack Wallen

我使用 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 已经非常非常久了。我使用 Linux 的历史可以追溯到内核版本 2.0 时代和像 [AfterStep](http://www.afterstep.org/) 这样的窗口管理器。事实上，AfterStep 是我在 Linux 上使用的第一个窗口管理器，它让我看到了这个开源操作系统是多么灵活和出色。

在 AfterStep 之后不久，我发现了 [Enlightenment](https://www.enlightenment.org/)，它同样很酷，但定制起来稍微容易一些。当然，Enlightenment（通常简称为“E”）没有那些花哨的透明度定制，但它本身就有很多“花哨”之处。

Enlightenment 快速、稳定且有趣。

使用 Enlightenment 几年后，我最终迁移到了 [Ubuntu](https://thenewstack.io/ubuntu-unity-25-04-brings-back-ubuntus-biggest-miss/) 及其 UI，但每隔一段时间，我都会尝试一下 Enlightenment，哪怕只是为了追忆。

多亏了那些美好的回忆，每当我看到一个提供 Enlightenment 桌面的 Linux 发行版时，我都会情不自禁地下载一个 ISO，将其作为虚拟机运行起来，看看究竟如何。

[Exton Linux 的 ExLight](https://exlight.exton.net/) 版本就是如此，它包含了 Enlightenment 0.27.1 桌面环境、Refracta Snapshot（用于创建基于 Debian Trixie 的您自己的系统）以及 Calamares 3.3.14-1 安装程序框架。

我相当确定会在这个发行版中发现什么，我没有看错。ExLight 以各种正确的方式给我留下了深刻印象。

但它会是您通往 Linux 启蒙之路的最佳选择吗？让我们深入了解一下。

## ExLight 是什么

ExLight 是一个基于 Debian 13（又名“Trixie”）的 Linux 发行版，因此它使用 APT 包管理器并可以访问大量的应用程序仓库。ExLight 表现出色（即使在旧硬件上也是如此），并且足够稳定，适合日常使用。

ExLight 的默认桌面还包含了足够的视觉效果，使其拥有更现代的外观和感觉，同时还提供了一些我最喜欢的老派功能。正是这种新旧结合（在我看来）使 ExLight 独一无二。

## 一切都关乎效率

正如我所暗示的，Enlightenment 关乎效率和简洁。

对于那些从未使用过 Enlightenment 的人来说，您可能会发现桌面看起来有些熟悉（**图 1**）。

![](https://cdn.thenewstack.io/media/2026/03/48016ea6-exlight1-1024x634.jpg)

**图 1：** 默认的 ExLight 桌面让我想大喊一声，“Eeeeagle！”

如您所见，屏幕底部有一个面板，其中包含常见元素：最左侧的“开始”菜单、最右侧的系统托盘以及中间的应用程序启动器。

您还会注意到四个图标，它们使用的图像与桌面上的相同。这些图标被称为“寻呼机”（Pager），允许您在虚拟桌面之间切换。您会在当前活动的桌面下方看到一条绿线。

还有一个隐藏在显眼位置的 Enlightenment 功能，它使得使用这个窗口管理器（以及由此设计的 ExLight）比许多其他桌面更高效。如果您在桌面的任何空白处左键单击，您将看到桌面菜单，它与“开始”菜单相同，只是可以从桌面上的任何空白区域访问（**图 2**）。

![](https://cdn.thenewstack.io/media/2026/03/4558d1cb-exlight2-1024x630.jpg)

**图 2：** 我记得第一次体验桌面菜单时，意识到它比传统菜单效率高得多。

另一个让桌面如此高效的隐藏功能是“遮蔽”窗口的能力。这意味着您可以双击窗口标题栏，窗口就会“卷起”，这样您就只能看到标题栏。您可以在桌面上拥有任意数量的遮蔽窗口，并根据需要“取消遮蔽”它们。

## 预装应用程序

就预装应用程序而言，您可能会觉得 ExLight 在这方面有点“轻量”。您会发现 Firefox、Leafpad（记事本）、PCMan 文件管理器、Refracta Snapshot、GParted、Enlightenment 文件管理器、LXTerminal、XTerm、mpv（电影播放器）、SMPlayer（媒体播放器）、FileZilla（FTP 客户端）、GIMP 以及一些实用程序。

尽管应用程序列表精简，但还有 Synaptic 包管理器（**图 3**），它是一个用于安装应用程序的 GUI 前端。

![](https://cdn.thenewstack.io/media/2026/03/2baa3bd0-exlight4-1024x676.jpg)

**图 3：** Synaptic 可能看起来有点老派，但它用起来非常棒。

您会发现 ExLight 缺少两大通用包管理器中的一个：Flatpak 和 Snap。当然，您可以使用以下命令安装其中任何一个：

* *sudo apt-get install snapd -y*
* *sudo apt-get install flatpak -y*

我强烈建议安装其中一个工具，因为它们能让您访问许多其他应用程序（甚至是专有选项）。没有 Flatpak 或 Snap，您会错过像 Slack 和 Spotify 这样的应用程序。

如果您使用 Flatpak，您还需要将 Flathub 设置为仓库，这可以通过以下命令完成：

*flatpak remote-add –if-not-exists flathub* [*https://flathub.org/repo/flathub.flatpakrepo*](https://flathub.org/repo/flathub.flatpakrepo)

## 性能

请记住，这个发行版的名称中包含“light”一词，这表明它是一个轻量级的 Linux 版本。它在旧硬件上运行快速，在新机器上更是会让您惊叹不已。我使用 Ollama AI 应用程序进行了常规测试（安装，拉取 llama3.2，并询问两个不同的问题）。

我在这个测试中总是问的第一个问题是“什么是 Linux？” 答案很快就出来了，这不足为奇。有时，在不太活跃的发行版上，响应开始出现之前会有延迟；但 ExLight 则不然。

下一个查询更复杂：

“编写一个 Python GUI 应用程序，接受用户输入的年龄、性别、电子邮件、电话和最喜欢的 Linux 发行版，并将其附加到名为 input.txt 的文件中。”

毫不意外，响应也和第一个问题一样迅速。换句话说，ExLight 以优异的成绩通过了我的 Ollama 本地 AI 测试。

## ExLight 适合您吗？

如果您喜欢在最新 Debian 版本之上体验老式 Linux 桌面的想法，那么选择 ExLight 绝对没错。尽管预装的开发工具不多，但您会在 Synaptic、Flatpak 和 Snap 中找到大量工具来满足或超出您的需求。

我使用 ExLight 的时光非常愉快，我强烈建议您 [下载一个 ISO](https://sourceforge.net/projects/exlight/)，并将其作为虚拟机运行或安装在备用机器上。

尝试一下这个令人印象深刻的发行版，您不会后悔的。