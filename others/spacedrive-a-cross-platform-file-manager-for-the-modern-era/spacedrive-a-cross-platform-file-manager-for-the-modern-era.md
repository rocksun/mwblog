
<!--
title: Spacedrive：现代的跨平台文件管理器
cover: https://cdn.thenewstack.io/media/2024/10/bce0f837-spacedrive.jpg
-->

这款跨平台文件管理器，适用于 Linux 和 Mac，一旦解决了一些问题，就展现出了巨大的潜力。

> 译自 [Spacedrive, A Cross Platform File Manager for the Modern Era](https://thenewstack.io/spacedrive-a-cross-platform-file-manager-for-the-modern-era/)，作者 Jack Wallen。

文件管理器经常被忽视，但它应该是每个操作系统的关键组件。使用文件管理器，您可以保存和组织文件、共享文件、查找和打开文件、连接到网络共享等等。如果没有文件管理器，高效地使用您的操作系统将非常具有挑战性，这就是它们如此重要的原因。

但并非所有文件管理器都是一样的。一些文件管理器比其他文件管理器具有更多功能，一些文件管理器采用现代美学设计，大多数文件管理器仅限于特定操作系统。例如，您在 macOS 上有 Finder，在 Windows 上有 Explorer，在 GNOME 桌面上有 Files（又名 Nautilus），在 Plasma 桌面上有 Dolphin。在该列表中，只有在不同的桌面上安装 Files 或 Dolphin 是可能的，但即使那样，您也安装了许多您可能不需要的其他组件和依赖项。

这就是当我读到一个现代的跨平台文件管理器时，我感到非常兴奋的原因。

您知道，我同时使用 [Linux](https://thenewstack.io/learning-linux-start-here/) 和 macOS。Linux 是我的桌面操作系统，而 macOS 是我用于笔记本电脑以及视频编辑的操作系统。有时我希望我可以在 Linux 上使用 Finder 或在 macOS 上使用 Files。但随着 Spacedrive 的发布，我不必再担心这个问题了。为什么？因为 Spacedrive 是一个现代的、功能齐全的文件管理器，可以在 Linux、macOS 和 Windows 上安装。虽然 Spacedrive 仍处于 alpha 阶段，但完整版本即将发布。

根据 [Spacedrive 网站](https://www.spacedrive.com/)，“Spacedrive 是一个跨平台文件管理器。它将您的设备连接在一起，帮助您从任何地方组织文件。”

大多数文件管理器允许您通过 Samba 等方式连接到远程共享，而 Spacedrive 采用了一种完全不同的方法。Spacedrive 将自动检测网络上的其他实例，或者您可以手动输入它们。连接后，您可以轻松地将文件发送到网络上另一个 Spacedrive 实例（只要接收机上的用户接受传入文件 - 稍后会详细介绍）。

![](https://cdn.thenewstack.io/media/2024/10/82415c38-1-1024x501.webp)

Spacedrive 的另一个与众不同之处在于它使用虚拟分布式文件系统 (VDFS) 作为去中心化数据库来模拟文件系统。借助此功能，Spacedrive 会索引硬件文件系统以创建主数据库，该数据库与网络上其他 Spacedrive 实例同步（实时）。

Spacedrive 的当前功能集（请记住，它处于 alpha 阶段）包括：

- 库：这允许您将相关文件夹集合在一起以方便访问。
- 位置：您可以将文件夹添加到侧边栏以快速访问。
- 标签
- 概述
- 最近
- 收藏夹

我一直提到 Spacedrive 仍处于 alpha 阶段开发。这样做的原因是它非常明确地定义了 alpha 软件是什么：尚未准备好供一般使用。我曾多次遇到 Spacedrive 崩溃，看到它丢失网络位置或拒绝添加新的 Spacedrive 节点，以及在操作系统之间遇到不一致。例如，Spacedrop 功能（允许您轻松地将文件从一台机器发送到另一台机器）在 macOS 机器之间运行良好，但从 Linux 到 macOS 仍然有点问题。但当一切正常时，Spacedrive 确实非同凡响。

让我向您展示我的意思。我将演示 Spacedrive 在两台不同的 macOS 机器之间进行的简单工作流程。

在我们开始之前，请确保从 [官方 Spacedrive 网站](https://www.spacedrive.com/) 下载适合您操作系统的 Spacedrive 安装程序。您会找到适用于 Linux（目前仅提供 .deb 文件）、macOS Apple Silicon、macOS Intel 和 Windows 的安装程序。还有一个 Docker 版本，有迹象表明它很快就会出现在 Android 上，还有一个网页版本。

请确保在至少两台机器 [在您的网络上](https://thenewstack.io/networking/) 安装 Spacedrive，以便您可以测试节点功能。

## 添加新节点

您要做的第一件事是向 Spacedrive 添加一个新节点。为此，请打开文件管理器，然后单击窗口左下角的齿轮图标。在“设置”中，单击左侧边栏中的“网络”，然后找到底部的“节点”部分，您应该会看到网络上发现的另一个 Spacedrive 实例。如果该实例没有自动出现，您可以手动输入另一个实例的 IP 地址（不需要端口）。然后，单击“提交”。

如果您看到列出了自动检测到的节点，请单击“连接”（图 1）以建立连接。

![-](https://cdn.thenewstack.io/media/2024/10/72ddbd06-spacedrive_settings.jpg)

*图 1：我的 MacBook Pro 上的 Spacedrive 自动发现了我的 iMac 上的实例。*

我 MacBook 上的 Spacedrive 没有自动找到 Linux 实例，所以我必须手动添加它。

添加节点后，它应该出现在左侧边栏的“Peers”下。如果单击该实例，您将看到一个小窗口，上面写着您可以将文件拖放到该窗口中以将其发送到连接的机器（图 2）。

![-](https://cdn.thenewstack.io/media/2024/10/21f40665-spacedrive_network.jpg)

*图 2：Spacedrive 中新添加的 Peer。*

猜猜怎么了？这不太好使。原因是，如果您离开窗口去寻找要发送的文件，窗口就会消失。此外（至少目前），您无法打开第二个 Spacedrive 窗口，这将允许您将文件拖放到传输窗口中。

幸运的是，还有其他方法可以共享文件。以下是方法：

- 使用 Spacedrop：单击左侧边栏中“Local”下的任何条目，然后单击 Spacedrop 图标（看起来像一个微小的土星状星球）。选择要将文件发送到的设备，找到并选择文件（出现提示时），然后发送。接收者必须按下“接受”以接受传入的文件，然后决定将其保存到哪里。
- 使用上下文菜单：如果您导航到 Spacedrive 中的文件夹，您可以右键单击文件并选择“共享”>“Spacedrop”>“节点”（其中“节点”是接收机器的名称）。
以上两种方法每次都能正常工作。

## 库

库是 Spacedrive 的另一个重要功能，因为它允许您将不同的文件夹收集到一个相关的主题集合中。例如，您可能正在处理项目 X，并且有几个与该项目相关的文件夹。您可以像这样创建一个新的库：

1. 单击 Spacedrive 窗口左上角的下拉菜单。
2. 选择“新建库”。
3. 为库命名。
4. 单击“添加位置”（位于左侧边栏的“位置”下）。
5. 找到并选择与项目相关的文件夹。
6. 出现提示时，单击“添加”。
7. 继续添加更多位置，直到与项目相关的每个文件夹都已添加。

我喜欢库的一点是，您可以创建任意数量的库并添加所有必要的位置，当您在库之间切换时，只会显示您添加的位置，这使得它成为一个非常高效的文件管理器。

虽然 Spacedrive 还没有准备好用于一般用途，但它显示出作为文件管理器的巨大潜力，我很容易就能看到它成为我使用的每个操作系统的默认选择。我强烈建议您安装这个跨平台文件管理器，看看它到底有什么特别之处。
