<!--
title: Bluefin Linux：ChromeOS 的极简，Linux 的极致强大
cover: https://cdn.thenewstack.io/media/2026/02/efeaad1d-the-new-york-public-library-bi8r36kz4uq-unsplash.jpg
summary: Bluefin Linux 结合 ChromeOS 简洁与 Linux 强大，基于不可变架构，支持容器化。提供开发者模式及定制GNOME桌面，兼具高安全性、灵活性和易用性，满足普通用户与开发者需求。
-->

Bluefin Linux 结合 ChromeOS 简洁与 Linux 强大，基于不可变架构，支持容器化。提供开发者模式及定制GNOME桌面，兼具高安全性、灵活性和易用性，满足普通用户与开发者需求。

> 译自：[Bluefin Linux: ChromeOS simplicity meets Linux power](https://thenewstack.io/bluefin-linux-chromeos-simplicity-meets-linux-power/)
> 
> 作者：Jack Wallen

想象一下，你能够使用一个像 ChromeOS 一样简单，同时又像 [Linux 操作系统](https://thenewstack.io/introduction-to-linux-operating-system/) 一样强大的操作系统。

你会用它来做什么？

也许更容易的问题是，“你有什么是 *不能* 做的？”

随着 Linux 的普及率持续上升，专门为可靠性、性能和可持续性而创建的发行版是这个开源操作系统成功的关键，而 [Bluefin Linux](https://projectbluefin.io) 正是其典范。

如果你是 Linux 新手，可以直接使用 Bluefin。如果你是开发者，可以启用开发者模式，这会将你的电脑变成一个功能强大的工作站，拥有以容器为中心的工作流。在开发者模式下，你将获得 [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/)、[Homebrew](https://thenewstack.io/install-homebrew-on-macos-for-more-dev-tool-options/)、[Kubernetes](http://Kubernetes) 支持、[Podman Desktop](https://thenewstack.io/install-and-use-podman-desktop-gui-to-manage-containers/)、[JetBrains](https://thenewstack.io/jetbrains-ceo-on-how-developers-become-leaders/) 的 IDE 等更多功能。

Bluefin 可以轻易地被称为一个能满足所有人的发行版。

根据 Bluefin 的新闻稿，“通过将云原生模式引入桌面，我们希望激发人们对桌面计算的兴趣，同时迎合下一代开源贡献者。Bluefin 旨在成为你最依赖的工具。当前的 Linux 桌面未能实现这一目标，但我们相信已有的可以被重塑。让我们做得更好。”

可以将 Bluefin 视为一个既能吸引新用户，又能满足经验丰富的用户和开发者的 Linux 发行版。

## 什么是 Bluefin？

Bluefin 基于 Fedora Silverblue，它是“Universal Blue”项目的一部分。Bluefin 是一个以容器为中心、不可变的 Linux 发行版，旨在将云原生技术引入桌面。

这个描述中最重要的部分是“不可变”。

### 什么是“不可变”？

不可变 Linux 发行版以只读方式挂载操作系统的核心。通过这样做，操作系统享有更高的安全性，因为核心系统无法被修改。

至于哪些内容无法修改，列表如下：

*   /usr
*   /bin
*   /sbin
*   /lib
*   /lib64
*   /boot
*   /etc

可写目录包括：

你可以在 [为什么企业应该在桌面上采用不可变 Linux](https://thenewstack.io/why-enterprise-businesses-should-adopt-immutable-linux-for-the-desktop/) 中阅读更多关于不可变 Linux 的信息。

本质上，不可变 Linux 是操作系统的未来，因为它具有指数级的安全性提升。

让我们回到 Bluefin。

## 桌面

Bluefin 使用了定制版的 GNOME，其中包括 Dash To Dock 和其他几个 GNOME Shell 扩展，使桌面环境对新的 Linux 用户来说更加简单。

Bluefin 也大量依赖 Flatpak 应用程序，甚至包含了 Bazaar 应用商店（它专门为通用包管理器而创建）。

Bluefin 不仅调整了 GNOME 使其更用户友好，而且它也相当美观。看看工作区概览（**图1**），你就能了解这个发行版有多么漂亮。

![](https://cdn.thenewstack.io/media/2026/02/24e7989d-bluefinoverview.jpg)

***图1：** Bluefin 对 GNOME 工作区概览的演绎。*

## 开发者模式

默认情况下，Bluefin Linux 以标准用户模式运行。你会注意到在安装过程中，你没有选择用户模式或开发者模式的选项。

别担心，切换一点也不难。

要从用户模式切换到开发者模式，打开一个终端窗口并输入命令：

```
ujust devmode
```

之后，使用以下命令重启系统：

```
sudo systemctl reboot
```

同样重要的是，如果你没有使用 Bluefin 的 LTS 版本，你也需要运行以下命令：

```
ujust dx-group
```

如果你好奇，开发者模式会做以下事情：

*   为 Docker 和 containerd 等工具启用预配置环境。
*   与 Homebrew 集成。
*   在保持不可变性的同时，通过 devcontainers 和 Distrobox 等工具提供强大的容器化开发环境。通过这样做，Bluefin 将开发工具与主机操作系统分离。

这个过程需要几分钟来重新基于系统（**图2**），但完成后，你就可以将工作提升到新的水平。

![](https://cdn.thenewstack.io/media/2026/02/6894884c-bluefinerebase.jpg)

***图2：** 将 Bluefin 重新基于到开发者模式。*

## 关于可用性？

我测试了 Bluefin 的用户模式和开发者模式，印象深刻。这个 Linux 发行版设计精良，使用这个开源操作系统是一种享受。虽然我没有深入研究开发者模式，但我试用了 Podman Desktop，发现它非常容易。在入职过程中，你甚至可以指示它自动添加 Kubernetes 支持（**图3**）。

![](https://cdn.thenewstack.io/media/2026/02/08ebc4f8-bluefinpodman.jpg)

***图3：** 在开发者模式下向 Bluefin Linux 添加 kubectl 非常简单。*

Podman Desktop 包含以下功能：

*   仪表盘
*   容器管理
*   Pod 管理
*   镜像
*   卷
*   网络
*   Kubernetes
*   扩展

我在开发者模式下没有找到安装 VS Code。然而，开发者工具箱（**图4**）提供了各种转换器（例如 JSON > YAML、时间戳格式、数字基数、CRON 解析器和反向 CRON）、编码器、格式化器和精简器、生成器以及文本工具。

![](https://cdn.thenewstack.io/media/2026/02/1772d9b5-bluefindevtoolbox.jpg)

***图4：** 开发者工具箱非常方便。*

## 结论

对我来说，Bluefin 最好的地方在于它的灵活性。只需几个命令，你就可以将系统从标准用户重新基于为开发者用户。同时，你获得了不可变性带来的增强安全性，以及一个对任何人来说都足够易用的定制 GNOME 桌面。

如果你的兴趣被激发了，你应该下载 Bluefin 的 ISO，并将其作为虚拟机运行或安装在裸机上；无论哪种方式，我确信你都会印象深刻。