CrunchBang 是一个基于 Debian 的[Linux 发行版](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/)，它以其极简主义和在硬核用户中的流行而闻名。[CrunchBang](https://crunchbang.org/about/) 最终停产，但催生了 CrunchBang++，甚至是我最喜欢的 BunsenLabs Linux。

CrunchBang 还有一个衍生版，名为 ArchBang。正如你所猜测的，这个版本基于 Arch Linux，但保留了 Openbox 窗口管理器以保持轻量级的速度。

ArchBang 曾一度淡出，但后来以 GreenBang 的名义复活。

这有点令人困惑，因为如果你搜索 GreenBang，你会跳转到 ArchBang 网站，该网站仍然将这个发行版称为 ArchBang。如果你去 Distrowatch 搜索 GreenBang，你会得到一个名为 GreenBang 的列表，它也指向 ArchBang 网站。

这是怎么回事？

嗯，在 2025 年 7 月，ArchBang 更名为 GreenBang。开发者声称存在来自 [Arch Linux](https://thenewstack.io/arch-ultimate-edition-a-feature-rich-beautiful-desktop-os/) 关于商标法的法律担忧。无论事实是否如此，至少我们知道为什么名称发生了变化。我们不知道的是为什么网站没有更新。

话虽如此……

[GreenBang](https://archbang.org/)！它是什么？

在我继续之前，让我们谈谈最初的名称。CrunchBang 以 Linux bash 脚本中使用的前两个字符 #! 命名。如果你曾写过 Linux bash 脚本，你会知道第一行通常是：

```
#!/bin/bash
```

这也被称为“shebang”。我一直称之为“crunch bang”：“crunch” 代表 `#`，“bang” 代表 `!`。

现在我们已经了解了背景，让我们来谈谈 GreenBang。

## GreenBang 是什么？

正如我所说，GreenBang 是一个基于 Arch Linux 的[Linux 发行版](https://thenewstack.io/learning-linux-start-here/)，它放弃了 Openbox 窗口管理器，转而使用 [Labwc](https://labwc.github.io)。如果你从未听说过 Labwc，它是一个轻量级、高度可定制的 X Window System 窗口管理器。Labwc 提供了与 Openbox 相同的极简主义桌面方法，因此它获得了与 Openbox 相同的速度和广泛配置，这意味着用户可以对其进行调整以完美适应他们的需求，打造一个完全独特的 UI。

Labwc 不是一个完整的桌面环境（如 [KDE Plasma](https://thenewstack.io/linux-desktop-what-makes-kde-plasma-so-appealing/) 或 [GNOME](https://thenewstack.io/what-makes-gnome-so-appealing/)），这意味着它不享受这些桌面环境中的深度集成。但同时，Labwc 让你完全控制外观、键盘快捷键和应用程序启动。Labwc 提供了桌面环境无法比拟的速度（即使在老旧硬件上），并且它尽可能地极简。

Openbox 和 Labwc 之间最大的区别是 Openbox 仅限于 X Windows，而 Labwc 获得了对 Wayland 的支持。

在 Labwc 桌面上，你会发现一个底部面板，除此之外不多。如果你在桌面上的任意位置左键单击，你会发现一个极简菜单，允许你访问已安装的应用程序和一些其他选项（如设置）。

单击“应用程序”条目，你会发现预装应用程序少得可怜。事实上，你可能会因此想知道这个操作系统在没有应用程序的情况下有什么用，尤其是在没有图形应用程序商店的情况下。

嗯，总有命令行，任何喜欢使用基于 Arch 的 Linux 发行版的用户都完全清楚，在这种发行版中，命令行通常是必需的。例如，如果你想安装 LibreOffice，打开终端应用程序并执行以下命令：

```
sudo pacman -Sy libreoffice\
```

你也可以安装 pamac 图形界面，这需要以下步骤：

1.  更新发行版：`sudo pacman -Syu`
2.  安装必要的依赖项：`sudo pacman -S --needed base-devel git`
3.  克隆 yay 仓库：`git clone https://aur.archlinux.org/yay.git`
4.  进入新创建的目录：`cd yay`
5.  构建软件包：`makepkg -si`
6.  安装 pamac：`yay -S pamac-aur`

我知道，这很多。如果你是 Arch 用户，你很可能会坚持使用命令行来安装应用程序，尤其考虑到 GreenBang 的核心卖点是其速度。你当然不想用一个华丽的图形界面来降低速度。

或者，如果你想避免命令行，就继续 pamac 安装。我要说的是：在测试 pamac 图形界面后，我发现它拒绝在 Wayland 上运行，并报错：“Lost connection to Wayland compositor”（与 Wayland 混成器失去连接）。

相反，我决定安装 Octopi，它是 Manjaro 的图形应用程序管理器。这个安装（`yay -S octopi`）需要一些时间，因为有很多依赖项需要安装，但最终，你将拥有一个方便的图形界面来安装应用程序（图 1）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/12/3f780b41-greenbangoctopi.jpg)](https://cdn.thenewstack.io/media/2025/12/3f780b41-greenbangoctopi.jpg)

图 1：Octopi 应用程序管理器图形界面。

## 安装

GreenBang 的安装是一个命令行操作。这不难，但你确实需要确保按照所提供的顺序完成所有操作（图 2）。

[![Screenshot](https://cdn.thenewstack.io/media/2025/12/a80c1dcd-greenbanginstall.jpg)](https://cdn.thenewstack.io/media/2025/12/a80c1dcd-greenbanginstall.jpg)

图 2：从桌面左键菜单启动安装程序。

键入 1，然后选择你想要使用的分区工具（我建议使用 gparted）。完成此操作后，逐一完成安装的其余部分。完成后，系统会提示你键入 d（表示完成），然后重启系统。

## 自定义

自定义 Labwc 完全是通过编辑文本文件进行的。如果你打开终端窗口，使用以下命令进入 .config/labwc 目录：

```
cd ~/.config/labwc
```

在该目录中，你会找到四个文件：

*   autostart：配置启动时运行的内容。
*   environment：配置默认键盘布局。
*   menu.xml：配置桌面菜单。
*   rc.xml：这是主配置文件。

有大量的配置选项可用于自定义你的桌面。要了解更多信息，我建议你查看[Labwc 官方文档](https://labwc.github.io/labwc-config.5.html)。

## GreenBang 适合谁？

这是一个难以回答的问题，但我认为我已经找到了答案。GreenBang 是一个很棒的发行版，适合那些不仅想要一个闪电般快速、极简的基于 Arch 的 Linux 发行版，而且渴望回到 Linux 的“美好旧时光”的人，那时命令行是必需品，而窗口管理器风靡一时。

如果这听起来像你，那么 GreenBang 将是一次真正的享受。

GreenBang 和 Labwc 让我想起了我早年使用 Linux 的日子，这立刻让我的脸上露出了笑容。

试试 GreenBang，看看它是否能用那些老派的 Linux 感觉温暖你的心。