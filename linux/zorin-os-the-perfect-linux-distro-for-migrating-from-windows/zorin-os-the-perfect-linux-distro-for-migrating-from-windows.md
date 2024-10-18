
<!--
title: Zorin OS：适合从Windows系统迁移的完美Linux发行版
cover: https://cdn.thenewstack.io/media/2024/10/12610fee-newstackzorinhero.jpg
-->

无论您是否有 Linux 使用经验，Zorin OS 都可以轻松地从 Windows 或 macOS 迁移。

> 译自 [Zorin OS: The Perfect Linux Distro for Migrating From Windows](https://thenewstack.io/zorin-os-the-perfect-linux-distro-for-migrating-from-windows/)，作者 Jack Wallen。

我从 1997 年就开始使用 Linux 了。这一切都始于我第一次遇到 Windows“蓝屏死机”之后，以及我希望摆脱微软操作系统不断出现的问题的愿望。我的第一个发行版（从当地一家电脑商店购买）是 OpenCaldera 1.0，但我立即遇到了麻烦。首先，用户界面与我习惯的截然不同。而且，我无法让我的内置调制解调器工作。在无知的驱使下，我回到商店，买了一份 [Red Hat 5.0](https://www.openshift.com/try?utm_content=inline+mention)，然后飞奔回家安装了它。

用户界面好多了，但调制解调器仍然无法工作。事实证明，我的电脑使用的是 Linux 无法识别或使用的 Winmodem 之一。在购买了外置的 US Robotics 调制解调器后，一切都好了，我很快意识到 Linux 是我的首选操作系统。

并非每个人都有耐心或能力进行如此复杂的迁移，这就是像 [Zorin OS](https://zorin.com/os/) 这样的 Linux 发行版如此重要的原因。

我对什么才是有效的 [Linux 桌面发行版](https://thenewstack.io/project-bluefin-a-linux-desktop-for-serious-developers/) 有着相当独特的看法，这一切都围绕着用户界面。如果你能创建一个既植根于过去又与未来相连的用户界面，它就可能成功。

我所说的意思是什么？你有一个用户界面，它能让用户立即熟悉，但也提供了一些非常现代化的功能。创建这样的界面，[Microsoft Windows](https://news.microsoft.com/?utm_content=inline+mention) 和 macOS 用户就不会觉得这个发行版像是由一个拥有远远超过我们的技术的先进外星种族创造的。

Zorin OS 就是这样一种发行版，它在过去和未来之间取得了完美的平衡。它是一个足够灵活的操作系统，任何类型的用户都可以轻松地对其进行配置以满足他们的需求。

如果你是 macOS 用户，这里有一个适合你的布局。Windows 用户也是如此。如果你熟悉 Linux，你会发现类似于 KDE Plasma、GNOME、Cinnamon 等的布局。更好的是，Zorin OS 带有一个应用程序（Zorin 外观 - 图 1），它使切换布局变得非常容易，任何人都可以做到。

![](https://cdn.thenewstack.io/media/2024/10/28dcb641-zorinosappearance.jpg)

*图 1：Zorin 外观应用程序极大地简化了自定义 Zorin OS 桌面的过程。*

Zorin OS 基于 Ubuntu，这意味着它从根本上来说是用户友好的、稳定的和可靠的。最新版本（17.2）基于 [Ubuntu 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/)，这是一个长期发布候选版本，将获得标准支持到 2027 年 6 月。

## 17.2 版本的新增功能

17.2 版本不是一个主要版本，所以新功能并不完全令人兴奋。我喜欢把点发布看作是完善主要版本的一种手段，而 Zorin OS 的最新版本正是这样做的。

新增的功能包括：

* 第三方主题安装指南。
* 更强大的“快速查找”工具。
* 内置对 Flatpak、Snap 和 AppImages 的支持。
* 光标自定义。
* 窗口行为（例如窗口放置和标题栏按钮位置）。
* 动态叠加滚动条切换。
* 改进的安全性。
* 更好的硬件支持（支持英特尔和 AMD CPU、NVIDIA GPU、罗技外设、各种游戏手柄，甚至联想键盘）。

正如你所看到的，这个版本没有任何重磅功能，但这并不意味着它是一个你可以忽略的版本或升级。然而，最重要的是，Zorin OS 17.2 仍然是 Zorin OS，这意味着它是一个操作系统所能达到的最坚如磐石的程度。

## 预装应用程序

至于预装的应用程序，你会发现最新版本的应用程序已经准备就绪，包括 LibreOffice（改进了与 Microsoft Office 的兼容性）、Firefox、Remmina（远程桌面查看器）、图像查看器、照片（网络摄像头应用程序）、视频、Rhythmbox（音乐应用程序）、录音机、Evolution（群件 - 类似于 Outlook）、磁盘使用分析器、备份等等。

需要考虑的一点是，Zorin OS 没有预装大量的工具链类型的应用程序。你不会发现 gcc、make 或大量的开发工具已经准备好了。当然，Zorin OS 172. 确实附带了 [Python 3.10.12](https://thenewstack.io/python-under-the-hood/)，但几乎所有 Linux 发行版都包含 Python。如果你是一名开发人员，你可以轻松地安装你需要的必要工具，其中大部分都可以在标准存储库中找到。

例如，你可以安装 GNU 编译器集合（GCC），它包括 C、C++、Objective C、Fortran、Ada、Go 和 D 的编译器。这还会安装 binutils、dpkg-dev、fakeroot 和所有必要的库。使用以下命令安装此软件包：

```
sudo apt-get install build-essential -y
```

因为 Zorin OS 在 GUI 应用商店（恰如其分地命名为“软件”）中加入了 Flatpak 和 Snap 支持，所以您可以安装第三方专有软件，例如 Spotify 和 Slack，而无需使用命令行或添加额外的存储库。您还可以从“软件”中安装多个 IDE，例如 IntelliJ、Eclipse、Arduino IDE、Android Studio 等等。

## Zorin OS 适合谁？

简而言之，Zorin OS 是一个任何人都可以使用的操作系统。无论您是否拥有 Linux 经验，Zorin OS 都可以让您轻松地从 Windows 或 macOS 迁移过来。我只推荐少数几个 Linux 发行版给那些没有任何 Linux 经验的人，而 Zorin OS 就是其中之一。在我看来，Zorin OS 是从 macOS 或 Windows 迁移过来的最佳发行版之一，您无需花费数小时、数天或数周的时间来学习如何与操作系统交互或提高工作效率。

Zorin OS 就是这么棒。

我建议从 Zorin OS Core（免费）开始。如果您喜欢这个版本，可以花 47.99 美元购买专业版，享受六种高级桌面布局、专业级的创意应用程序套件、高级生产力工具和支持。

您可以从 [Zorin OS 官方下载网站](https://zorin.com/os/download/) 下载 Core（基本版）、Education（面向学生的版本）或 Pro（包含所有强大功能的版本）。如果您使用的是 Zorin OS Core，则可以购买专业版许可证，并使用 Zorin OS 升级工具升级到付费版本。

