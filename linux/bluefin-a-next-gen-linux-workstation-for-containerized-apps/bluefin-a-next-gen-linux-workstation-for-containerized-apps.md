
<!--
title: Bluefin，下一代用于容器化应用程序的Linux工作站
cover: https://cdn.thenewstack.io/media/2025/01/e437f290-bluefinhero.jpg
-->

Bluefin 旨在向 Linux 用户展示广泛用于云原生计算的工具和应用程序。

> 译自 [Bluefin, a Next-Gen Linux Workstation for Containerized Apps](https://thenewstack.io/bluefin-a-next-gen-linux-workstation-for-containerized-apps/)，作者 Jack Wallen。

Bluefin 是 Fedora Silverblue 的定制版本。

如果您不熟悉 [Silverblue project](https://fedoraproject.org/atomic-desktops/silverblue/)，它是 [Fedora](https://thenewstack.io/fedora-41-offers-zippy-performance/) 的一个变体，它使用不可变的文件系统来实现原子更新和轻松回滚。Silverblue 还使用了 rpm-ostree，它为 [Linux](https://thenewstack.io/learning-linux-start-here/) 提供了持续的版本控制更新。

[rpm-ostree](https://coreos.github.io/rpm-ostree/) 包系统的一个很酷的特性是，它可以重新设置您的安装，因此您可以轻松地在 Silverblue (GNOME)、Kinoite (KDE Plasma)、Sericea (Sway) 和 Bluefin (GNOME 的定制版本) 之间切换。

但我们今天不是来讨论重新设置的。相反，让我们把 [Bluefin](https://projectbluefin.io/) 放在聚光灯下。

Bluefin 使用来自 Flathub 的应用程序，几乎不需要维护，并且包含 GPU 驱动程序，因此您不必手动安装它们。

在您深入了解 Bluefin 之前，请记住以下几点：

- Flatpak 问题当然应该认真对待，因为 Bluefin 的应用程序模型围绕着在 Flathub 中隔离和维护的 [Flatpak apps](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)。如果您使用的应用程序在 Wayland、Pipewire、Flapak 或 Portals 上运行不佳，那么它在 Bluefin 上运行良好的可能性也很小。
- Bluefin 与其说是一个发行版，不如说是 [containerized applications](https://thenewstack.io/red-hat-rethinks-the-linux-distro-for-the-container-age/) 的载体。
- Bluefin 针对大多数用户进行了优化。
- Bluefin 专注于容器，并将“让新的 Linux 用户接触到云原生中使用的工具”。

最后一点是什么意思？本质上，开发人员已将 Bluefin 与云原生生态系统集成在一起。其中大部分都在底层，因为您找不到预先安装的、专门用于连接基于云的服务（如 Google）的应用程序集合。就云原生问题而言，要知道它主要面向开发人员。

但是用户呢？Bluefin 提供了其他发行版没有提供的什么？Bluefin 的基本目标是创建一个尽可能免维护的开源操作系统。对于任何觉得其他 Linux 桌面发行版不够可靠的人来说，Bluefin 凭借其位于默认 Fedora 镜像之上的原子层而获胜。这意味着如果需要，您也可以恢复到默认镜像。

关于底层讨论就到此为止。让我们来谈谈 Bluefin 的外观、工作方式和性能。

## 外观

Bluefin 非常漂亮。从默认壁纸到主题、dock 以及介于两者之间的一切。我想说这是我用过的 GNOME 桌面最好看的一个版本。虽然它仍然是原来的 GNOME，但它得到了以下扩展的提升：

- Blur My Shell
- Dash to Dock
- Apps Menu (已安装但默认未启用)
- Logo Menu
- Search Light (全局搜索)

我是那些既要求高颜值又要求高性能操作系统的 Linux 用户之一，而 Bluefin 轻松地满足了这两个要求。Bluefin 提供了典型 GNOME 桌面的易用性以及 elementary OS 的优雅性。

它与 [any Linux distribution](https://thenewstack.io/choosing-a-linux-distribution/) 一样易于使用，但不会“简化”任何内容。Linux 新手会在 Bluefin 上感到宾至如归，而经验丰富的用户不会觉得他们在使用“玩具”操作系统。

## 应用程序，应用程序，应用程序

开箱即用，您不会在 Bluefin 上找到大量的预安装应用程序。有常见的 GNOME 应用程序集合（例如日历、联系人、天气、地图、计算器、文本编辑器、终端）、Firefox、Thunderbird、Clapper（媒体播放器）、InputLeap（用于在桌面之间共享鼠标和键盘）、Connections（用于远程桌面连接）、Mission Center（系统资源监视器）等等。

这可能看起来有点简陋，但总有 GNOME Software 可用于安装其他应用程序。Bluefin 的 GNOME Software 版本集成了 Flapak，因此您安装的应用程序都将来自 Flathub（图 1）。

![](https://cdn.thenewstack.io/media/2025/01/46012a2e-bluefinsoftware.jpg)

*图 1：GNOME Software 是一个非常用户友好的包管理器 GUI。*

还有一个名为 Warehouse 的小型应用程序，可让您控制复杂的 Flatpak 选项。使用 Warehouse，您可以轻松回滚任何不需要的更新、固定运行时、屏蔽 Flatpak、过滤软件包、排序日期、查看当前应用程序用户数据、清理任何零散数据、拍摄应用程序快照、安装新软件包等等。您安装的任何 Flatpak 应用程序都会出现在 Warehouse 中（图 2），并且可以从 GUI 中轻松管理。

![Warehouse 截图](https://cdn.thenewstack.io/media/2025/01/ae84ef7f-bluefinwarehouse.jpg)

*图 2：Warehouse 对于那些喜欢使用 Flatpak 应用程序的人来说是一大福音。*

使用 Warehouse，您可以快速删除特定应用程序的用户数据、打开应用程序的用户数据文件夹、打开应用程序、卸载应用程序等等。最重要的是，Bluefin 附带 Flatseal，它简化了管理 Flatpak 权限的过程。

您还会发现默认安装了 Brew，或 [Homebrew](https://brew.sh/)。Brew 通常被认为是 macOS 的命令行包管理器，但有了 Linux 版本，您可以安装很多应用程序。例如，您可以使用以下命令安装 tree 应用程序：

```bash
brew install tree
```

请记住，brew 仅用于安装命令行工具。

## Bluefin 适合哪些人？

有些人可能倾向于说 Bluefin 是最适合开发人员或经验丰富的 Linux 用户的发行版，但我认为它对于新用户来说也是一个同样强大的竞争者，因为它非常可靠，而且开箱即用配置良好。Bluefin 是那种您能找到的几乎可以一劳永逸的发行版之一。

对于开发人员，您可以为开发人员模式重新构建 Bluefin，这是一个专用的开发人员镜像，其中包含特定的捆绑工具，例如带有 Docker 的 Visual Studio Code、DevPod、Podman 和 Podman Desktop、性能工具等等。

要启用开发模式，您需要运行两个命令。第一个是：

```bash
ujust devmode
```

运行此命令后，重新启动。
接下来，您需要使用以下命令将您的用户帐户添加到正确的组：

```bash
ujust dx-group
```

注销并重新登录。您现在应该处于 Bluefin 开发模式。
这种 Linux 的实现既坚固又美观（这说明了一些问题）。在对 Bluefin 进行测试后，我得出的结论是：“我可以想象自己将它作为我的默认 Linux 发行版。”

如果您对 Bluefin 产生了兴趣，您可以使用 [网站](https://projectbluefin.io) 的“TRY BLUEFIN”部分下的表格下载 ISO。将 ISO 刻录到可启动的 USB 驱动器，将其插入您的机器，启动并安装。

您不会后悔给这个发行版一个机会。

