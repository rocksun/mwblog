<!--
title: 使用Atoms管理Linux chroot环境
cover: https://cdn.thenewstack.io/media/2024/02/05c7d01a-atom-1786007_1280-1024x643.jpg
-->

chroot 命令可以创建软件系统的虚拟副本，Atom 这个图形界面工具允许您轻松创建 chroot 环境。

> 译自 [Linux: Manage chroot Environments with Atoms](https://thenewstack.io/linux-manage-chroot-environments-with-atoms/)，作者 Jack Wallen 是 X 代思想与当今讽刺意识的结合。Jack 是一个寻求真理和用量子力学铅笔写字的人，他的声音和灵魂节奏是割裂的。

问任何老派的 [Linux 用户](https://thenewstack.io/linux-hide-your-shell-passwords-with-sshpass/)关于 chroot 环境，他们要么会理解这个工具提供了什么，要么会转身走开，这样你就看不到他们眼中的恐惧。

虽然这可能有点言过其实，但是从命令行创建 chroot 环境确实不是最简单的事。

但是等等... 什么是 chroot 环境？

## 什么是 chroot 环境？

本质上，[chroot](https://man7.org/linux/man-pages/man2/chroot.2.html) 环境创建了软件系统的隔离的、虚拟化的副本，可以用于测试或开发，而不会危害你的[主机操作系统](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)。这些环境是测试任何对生产机器构成任何风险的东西的绝佳选择。

传统上，chroot 环境是通过命令行创建的，这可能有点复杂。幸运的是，有一个图形界面工具可以更轻松地管理 chroot 环境。

该应用程序称为 [Atoms](https://github.com/AtomsDevs/Atoms)，它允许您创建、管理和使用 chroot 环境。Atoms 当前支持以下 Linux 镜像:

- Alpine Linux  
- Ubuntu  
- Fedora  
- Alma Linux  
- Centos
- Debian  
- Gentoo
- OpenSUSE
- RockyLinux

使用 Atoms，您可以轻松选择您要环境使用的发行版(以及版本)镜像。一旦您创建了环境，您就可以访问它，做任何您需要做的事情，然后退出它，知道您在环境中所做的一切都不会危害您的主机操作系统。

可以将 Atoms 视为另一种用户友好的方式来创建虚拟化环境，而不会对您的生产文件系统进行任何更改。

让我展示一下如何安装 Atoms，然后我们将创建第一个 chroot 环境。

## 如何安装 Atoms

要使用 Atoms，您需要一个支持 [Flatpak](https://flatpak.org/) 的 Linux 发行版。您不会在 .deb 或 .rpm 包中找到 Atoms，它也不可通过 Snap 获得。所以，如果您当前的 Linux 操作系统没有安装 Flatpak，您需要先安装它。像 [Fedora 这样的发行版](https://thenewstack.io/fedora-centos-consistency-transparency-open-source/)默认自带 Flatpak。对于基于 Ubuntu 的发行版，您可以使用如下命令安装 Flatpak:

```bash
sudo apt-get install flatpak -y
```

如果您现在才安装 Flatpak，在它可以从 Flathub 安装应用程序之前，您需要对其进行设置。为此，请确保发出以下命令(在安装 Flatpak 后):

```bash
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
```

做完这些后，重新启动系统以使更改生效。

## 安装 Atoms

安装 Atoms 很简单。打开终端窗口并发出以下命令:

```bash
flatpak install flathub pm.mirko.Atoms
```

请确保对所有问题回答 y。安装完成后，您可以登录并注销(以便向您的桌面菜单添加 Atoms 启动器)，或者立即使用以下命令运行 Atoms:

```bash
flatpak run pm.mirko.Atoms
```

首次启动 Atoms 时，您会看到“创建新 Atom”按钮(图1)。

![](https://cdn.thenewstack.io/media/2024/01/4438efab-atoms1.jpg)

*图1:首次运行时 Atoms 应用程序不包含任何 chroot 环境。*

## 创建第一个 chroot 环境(也称为 Atom)

点击“创建新 Atom”，在弹出的窗口中(图2)，您需要为 atom 命名、选择要用作基础镜像的发行版，然后选择所选发行版的版本。您可能会发现，对于某些发行版，您只能选择最新版本。

![](https://cdn.thenewstack.io/media/2024/01/019030a3-atoms2.jpg)

*图2:我正在创建一个名为“New Stack Test”的新的 Atom Chroot，使用 Rocky Linux 的最新版本。*

配置新 Atom 后，点击“创建”，应用程序将开始工作。当进程完成时(这应该不到一分钟)，关闭弹出窗口，您就会看到 atom 被列出。

## 使用新的 Atom

在“仪表盘”选项卡中，点击新 Atom 的条目，您会看到“浏览文件”、“详情”、“绑定”和“破坏性操作”条目(图3)。

![](https://cdn.thenewstack.io/media/2024/01/ad93c43c-atoms2a.jpg)

*图3:我的“New Stack Test” Atom 的 Atom 仪表板。*

如果点击“浏览文件”，它将挂载环境并打开文件管理器，以便您可以浏览文件系统层次结构。然而，真正的工作发生在“控制台”选项卡中。

点击“控制台”选项卡，您将找到自己在环境的 root 提示符下，在这里您可以开始测试、开发等所需的工作(图4)。

![](https://cdn.thenewstack.io/media/2024/01/aeb43a87-atoms3.jpg)

*图4:通过命令行升级 Rocky Linux chroot 环境。*

需要记住的一件事是，chroot 环境与虚拟机或裸机安装并不完全相同。当您安装 Docker、[Podman](https://thenewstack.io/install-and-use-podman-desktop-gui-to-manage-containers/)、Apache2 等应用程序时，会遇到问题。

然而，您可以做的是，从仪表盘中，点击浏览文件，然后使用文件管理器，将源代码/脚本复制粘贴到所需的目录，并从那里工作。使用相同的方法，您可以创建新目录。您也可能会遇到权限问题，因此您需要切换到控制台并像这样添加新用户:

```bash
useradd -m USERNAME
```

其中用户名是要添加的用户名。

然后使用命令为该用户设置密码:

```bash
passwd USERNAME
```

然后可以使用命令切换到该用户:

```bash
su USERNAME
```

此时，您将有权限写入新用户主目录(使用 cd 命令更改)。

完成使用 Atom 后，可以单击仪表盘选项卡左上角的向左箭头。如果不再需要 Atom，请在仪表盘中单击“破坏性操作”，然后单击“销毁 Atom”。

Atoms 是快速创建 chroot 环境的绝佳方式。您可能需要花一些时间来掌握使用它们，但至少最难的部分已经完成。将 chroot 环境(通过 Atom)添加到开发/测试流程中，看看它们是否能让您的生活轻松一些(并减少对生产系统的破坏)。
