# EndeavourOS Neo：Arch Linux 的时尚之路

![EndeavourOS Neo：Arch Linux 的时尚之路特色图片](https://cdn.thenewstack.io/media/2024/12/6c89a5c1-endeavorhero-1024x645.jpg)

Arch Linux 以安装困难而闻名。如果你想要原汁原味的 [Arch Linux](https://archlinux.org/)——它自称是“一个简单轻量级的发行版”——你需要配置一个文本文件或使用脚本，因为大多数现代 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)都没有传统的安装程序。

因此，Arch Linux 很少被经验不足的用户考虑作为选择。

没关系，因为有很多 Arch 主题的变体，它们使安装操作系统变得容易得多，同时仍然保留了 Arch 的核心特性。

其中一个发行版叫做 [EndeavourOS](https://endeavouros.com)。虽然这个 Arch 版本并非最古老的（首次发布在 2019 年 5 月），但它是我获得极其稳定的桌面操作系统的最喜欢的选择之一。

EndeavourOS 的亮点是增加了 Calamares 安装程序，因此你无需再经历过于复杂的基于文本的安装程序。Calamares 是一个点击式安装程序，任何人都可以轻松安装此操作系统。

EndeavourOS 团队进一步定制了 Calamares 安装程序，使其支持在线和离线安装。离线安装无需在安装过程中连接网络。此安装将安装 Xfce 桌面（包含 EndeavourOS 主题）。

至于在线安装程序，你可以从 9 个不同的桌面环境中进行选择，例如 GNOME、Plasma 桌面、Xfce、LXQt、i3 等等。我没有选择通常的 GNOME 或 Plasma 桌面，而是最初选择了 i3 平铺窗口管理器，因为它是一种值得体验的东西。

但是，安装之后，我记起了 i3 的复杂性，因此决定在其最新版本 EndeavourOS Neo 中评测 Plasma 版本。毕竟，这个发行版的理念是使 Arch Linux 对普通用户足够容易，而 i3 达不到这个目标。因此——Plasma 桌面。

在我开始介绍桌面 UI 之前，让我们谈谈 EndeavourOS 附带的内容。默认应用程序列表并不十分广泛，但始终存在应用程序安装程序（可从欢迎工具中轻松访问），它允许你添加各种应用程序。

例如，如果你想安装 [LibreOffice 办公套件](https://thenewstack.io/designing-libreoffice-preparing-images-graphics-editors/)，请转到欢迎应用程序并点击“添加更多应用程序”选项卡。在那里，点击“选择要安装的常用应用程序”，展开“办公”条目，选择 LibreOffice fresh（最新版本）或 still（稳定版本），然后点击“立即安装”（图 1）。

<br>

图 1：安装最新版本的 LibreOffice。

<br>

出现提示时，输入你的用户密码并确认安装。安装完成后，按键盘上的 Enter 键关闭窗口。然后，你可以安装更多应用程序或从桌面菜单打开 LibreOffice。

或者，你也可以始终使用命令行。要安装 LibreOffice Fresh，命令如下：

```bash
sudo pacman -S libreoffice-fresh
```

我还建议安装 Pamac GUI 用于 pacman 包管理器。为此，请打开终端窗口并发出以下命令：

```bash
yay -S pamac-aur
```

使用 yay 而不是 pacman 的原因是 pacman 不支持 AUR 存储库，而 Pamac 就位于 AUR 存储库中。安装 Pamac 后，你可以在桌面菜单中找到它，在那里你可以打开它并随意安装应用程序（图 2）。安装后，你将在位于 *系统 > 添加/删除软件* 的桌面菜单中找到 Pamac。

<br>

图 2：Pamac GUI 比包含的安装程序容易得多。

<br>

我知道使用 Pamac 有悖于 EndeavourOS 的理念（它会让你默认使用命令行），但是一个旨在使 Arch Linux 更容易的发行版应该使最终用户的一切都更容易，而 Pacmac 正是这样做的。

当然，你还会安装 Python3、Firefox、Kate 文本编辑器、Meld（用于“比较”文件）、KDE Connect（用于连接其他设备）和 VLC 媒体播放器以及 Haruna 媒体播放器。

我还建议你安装 Flatpak，以便你可以访问更多应用程序。为此，请发出以下命令：

```bash
sudo pacman -S flatpak
```

安装 Flatpak 后，你可以添加第三方应用程序，例如 Spotify、Slack 等。

## 那些讨厌的深色主题
开箱即用，EndeavourOS 非常偏向于深色主题。我不是很喜欢深色主题，所以我着手切换到浅色主题，这可以通过系统设置 > 颜色和主题来完成，然后选择一个浅色主题。

唯一需要注意的是，只有 Breeze Dark EndeavourOS 主题包含开发团队完成的所有自定义设置。即便如此，这也是 Plasma 桌面，所以它仍然很漂亮。

您也可以点击全局主题窗口右上角的“获取新主题”，这将打开一个新窗口，其中包含大量主题可供选择。其中一些主题相当基础，而另一些主题实际上会为您的桌面配置各种效果。

我最喜欢的主题之一是 Vince 的 Apple MacOS 主题 [White Sur]。使用此主题，您还可以添加顶部栏并将面板配置得更像停靠栏。瞧，您就拥有了一个非常类似 Apple 的桌面（图 3）。

-

图 3：我已经让我的桌面 Mac 化了！

如果您不确定应该使用哪个版本，KDE 的 Plasma 桌面和 Arch 底层相结合，构成了一个非常高性能的系统。凭借 Plasma 桌面中所有配置选项，您可以确保能够完全按照自己的意愿配置桌面。

## 最后…

EndeavourOS 适合谁？好吧，如果您在论坛上阅读太多内容，您可能会倾向于认为它完全是为经验丰富的用户或那些可能没有太多 Linux 经验但想快速上手的用户准备的。但是，只需少量工作，您就可以拥有一个能够完美服务于任何人的 EndeavourOS 版本，无论他们的经验水平如何。

更好的是，EndeavourOS 是一个漂亮的桌面操作系统，对于任何想要体验 Arch Linux 的人来说，这是一个不错的选择。即使默认桌面壁纸上的定义可能会让您认为开发人员期望您付出努力才能使其运行起来，但根据我的经验，这并非完全必要。安装 Pamac 和 Flatpak，然后使用这些工具安装您需要的软件。

EndeavourOS 为您提供了 Arch Linux，而没有 Arch 的所有特性。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以串流收听我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)