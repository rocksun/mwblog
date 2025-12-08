<!--
title: Tuxedo OS：Ubuntu血脉，KDE Plasma加持，性能一骑绝尘！
cover: https://cdn.thenewstack.io/media/2025/11/5bdc9dd3-tuxedooshero.jpg
summary: Tuxedo OS是基于Ubuntu和KDE Plasma的发行版，安装简便，性能卓越，AI能力突出。预装应用丰富，易于软件管理。是稳定美观的桌面系统之选。
-->

Tuxedo OS是基于Ubuntu和KDE Plasma的发行版，安装简便，性能卓越，AI能力突出。预装应用丰富，易于软件管理。是稳定美观的桌面系统之选。

> 译自：[Tuxedo OS: Ubuntu Base, KDE Plasma, Awesome Performance](https://thenewstack.io/tuxedo-os-ubuntu-base-kde-plasma-awesome-performance/)
> 
> 作者：Jack Wallen

Tuxedo Computers 的使命是让 Linux 普及到大众。它实现这一目标的主要方式是提供出色的笔记本电脑和台式电脑。我测试过该公司生产的几款产品，它们总是令我印象深刻。

但你知道 Tuxedo Computers 也有自己的 Linux 发行版吗？

没错。[Tuxedo OS](https://www.tuxedocomputers.com/en/TUXEDO-OS_1.tuxedo) 基于 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)，并使用 KDE Plasma 作为其桌面环境。尽管 Tuxedo OS 针对 Tuxedo 硬件进行了优化，但它可以在任何现成的系统上运行。我得说：Tuxedo OS 在该公司自己的硬件上运行时非常出色。即便如此，它在其他系统和虚拟机 (VM) 上仍然运行得很好。

为了我的测试/评审目的，我将 Tuxedo OS 作为 [VirtualBox 虚拟机](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/) 安装，分配了 3GB 内存和 2 个 CPU 核心。让我们看看它的表现如何。

## 简易安装过程

Tuxedo OS 的安装与任何 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)一样简单；换句话说，它完全是点击式操作。只需点击几下（并输入我的用户名信息），我在五分钟内就让操作系统运行起来了（Windows，你看到了吗）。

首次登录后，我发现 Tuxedo 对 KDE Plasma 的实现与任何使用相同桌面环境的发行版开箱即用的效果没有显著差异。它界面简洁，易于理解。

我唯一的抱怨是针对许多 Linux 发行版都存在的问题：默认的深色主题。我不明白为什么这么多开发团队选择随 Linux 提供深色主题。

## KDE Plasma 桌面体验和自定义

没关系，因为 KDE Plasma 可以非常轻松地从深色切换到浅色。打开系统设置，前往“颜色和主题”>“全局主题”，然后选择一个浅色选项（图 1）。

![Screenshot](https://cdn.thenewstack.io/media/2025/11/1f25f356-tuxedoos1.jpg)

*图 1：如果你不喜欢任何默认选项，点击“获取新主题”并下载你选择的主题。*

我最喜欢的 KDE Plasma 主题之一是 Se7en Aero；它晶莹剔透，非常漂亮。你可以花几个小时仔细浏览并安装各种 KDE Plasma 主题，尽情享受吧。

当然，KDE Plasma 主题与 Tuxedo OS 本身并没有太大关系，但它们是自定义桌面的一个好方法。

让我们来看看 Tuxedo OS 独有的一些功能。

## Tuxedo 控制中心和 Aquaris 工具

你会在系统托盘中找到一个看起来像带有白色 X 的黑色方块图标。点击它，Tuxedo 控制中心弹出窗口就会出现（图 2）。从这里，你可以选择电源配置文件，启用省电拦截器并打开 Aquaris 控制中心。

![Screenshot](https://cdn.thenewstack.io/media/2025/11/318df86c-tuxedocc.jpg)

*图 2：控制中心弹出窗口让你能够访问多个很酷的功能。*

Aquaris 控制中心让你能够快速访问仪表板（图 3）、配置文件、各种工具、全局配置文件设置等。

![screenshot](https://cdn.thenewstack.io/media/2025/11/245293f8-tuxedoaq.jpg)

*图 3：Aquaris 工具非常实用，尤其是当你使用笔记本电脑时。*

我得说：在官方 Tuxedo 硬件上运行操作系统时，Tuxedo 控制中心的作用更大。

## 预装应用程序和软件管理

Tuxedo OS 包含大量预装应用程序，例如 Firefox、Kate（文本编辑器）、KDE Connect（同步手机和桌面）、Thunderbird、Elisa（本地音乐播放器和在线广播）、Kamoso（网络摄像头软件）、VLC 媒体播放器、LibreOffice（Calc、Draw、Impress、Math 和 Writer）等等。

尽管 [Samba](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/) 没有预装，但如果你打开 Dolphin（默认文件管理器），右键点击一个文件夹，点击“属性”，然后打开“共享”选项卡，你可以一键安装 Samba（图 4）。

![Screenshot](https://cdn.thenewstack.io/media/2025/11/230e1e66-tuxedosamba.jpg)

*图 4：在 Tuxedo OS 上安装 Samba 非常简单。*

Samba 安装完成后，按照其余提示（包括系统重启）操作，你就可以开始在你的局域网中共享文件夹了。你无需接触命令行即可让 Samba 正常运行，并共享你的主目录中的文件夹。

你还会发现 [Flatpak 支持](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) 集成到了 KDE Discover 中，因此你可以轻松安装大量应用程序（包括 Slack 和 Spotify 等专有软件）。

## 卓越的性能和 AI 能力

Tuxedo OS 表现得像个冠军。我为虚拟机分配了刚刚超过 5GB 的内存和 3 个 CPU 核心，没有任何抱怨。当然，一开始我并没有对操作系统进行极端的压力测试。在测试期间，我安装了 [Ollama](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/) 来看看它的表现如何。

安装完成后，我拉取了 llama3.2 大型语言模型 (LLM)。这是一个 2 GB 的模型，拉取大约用了两分钟。一旦准备就绪，我查询了“什么是 Linux？” 我对它的响应速度感到非常惊讶。通常，在纯 CPU 模式下运行 Ollama 可能会很慢，但在 Tuxedo OS 上，Ollama 表现出色。我见过在更强大的硬件上运行反而更慢的情况。我不确定这是否归因于定制的 Tuxedo 内核或其他原因，但它确实令人印象深刻。所以，如果 AI 是你所热爱，那么选择 Tuxedo OS 绝对不会错。

常用应用程序运行流畅快速。操作系统更新迅速，动画也很流畅。

总而言之，我对 Tuxedo OS 的性能没有任何抱怨。

Tuxedo OS 是一个出色的 Linux 发行版，它不需要 Tuxedo 电脑也能运行良好（尽管我建议你尝试他们的硬件）。如果你想要一个性能稳定、界面美观的桌面操作系统，请 [下载 ISO 镜像](https://os.tuxedocomputers.com/)，找一台备用电脑，或者启动一个虚拟机，安装 Tuxedo OS，然后尽情享受吧。