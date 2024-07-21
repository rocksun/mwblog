
<!--
title: 选择Linux安装平台
cover: https://cdn.thenewstack.io/media/2024/07/afc234cd-martyn-de-jong-1bizoitnk-0-unsplash.jpg
-->

您已经选择了 Linux 发行版，并准备开始安装过程，但您需要确定您的硬件选项。以下是从哪里开始。

> 译自 [Linux: Choose an Installation Platform](https://thenewstack.io/linux-choose-an-installation-platform/)，作者 Damon M Garn。

[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) 文章。在本系列文章中，我们还介绍了[如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/)，Linux 内核如何[与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)以及如何[管理系统服务](https://thenewstack.io/linux-skills-manage-system-services/)、[存储](https://thenewstack.io/how-to-manage-linux-storage/)、[文件权限](https://thenewstack.io/linux-how-file-permissions-work/)和[用户和组权限](https://thenewstack.io/linux-user-and-group-management/)。

您已经选择了一个 Linux 发行版，并准备开始安装过程，但您需要弄清楚您的硬件选项。您是否需要购买一台新电脑？您可以使用旧系统吗？虚拟化是怎么回事？容器是一个选择吗？

本文不提供技术配置。相反，它讨论了在您追求职业发展、编程或技术认证时，用于试验 Linux 的安装选项。它提供了有关哪些硬件是必需的以及如何使用现有资源的想法。我还从不花太多钱在解决方案上的角度来介绍这些信息。

本系列中的相关文章讨论了选择一个或多个发行版以及实际的安装过程。

## 使用硬件平台

术语“裸机”是指没有操作系统或应用程序（尽管通常存在固件）的计算机硬件。计算机通常有四个主要子系统：处理器、内存、存储和网络。在裸机硬件上，这些组件已安装并准备就绪，但不存在任何软件来利用它们。

在裸机设备上安装 Linux 意味着在没有其他操作系统或您打算保留的应用程序的计算机上安装它。这可能是一台您刚组装的新电脑，或者是一台您打算覆盖其操作系统、应用程序和数据的旧设备。

Linux 在硬件要求方面非常灵活。大多数 Linux 发行版可以使用比 Windows 和 macOS 操作系统少得多的 RAM 和硬盘空间。一些发行版甚至专门针对在更旧的硬件平台上运行良好而设计。由于存在如此多的发行版，并且它们的功能差异很大，因此很难确定一组特定的最低和推荐硬件要求。最好在每个发行版的基础上检查这些建议。

以下是一些示例建议：

- [Ubuntu 硬件规格](https://ubuntu.com/download/desktop#system-requirements)：2 GHz 双核 CPU、4 GB 内存、25 GB 驱动器空间。
- [Fedora 硬件规格](https://docs.fedoraproject.org/en-US/fedora/latest/release-notes/hardware_overview/)：2 GHz 双核 CPU、2 GB 内存、15 GB 驱动器空间。

对于当今的系统来说，这些要求相当轻。您可能会发现，您壁橱或地下室里积满灰尘的旧电脑非常适合运行 Linux，即使它不再能有效地与其他操作系统一起使用。

### 选择 Linux 专用硬件

如果您选择购买硬件，请务必寻找与 Linux 兼容的系统。例如，[Ubuntu 认证了特定硬件](https://ubuntu.com/certified) 用于其发行版。一些主要制造商，如戴尔，在某些系统上提供 Linux 作为预装操作系统选择。

其他供应商专门从事 Linux。考虑 [System76](https://system76.com/) 的笔记本电脑、工作站、迷你电脑和服务器产品线，这些产品线使用他们自己的 Pop!_OS 或 Ubuntu 22.04 LTS。[Tuxedo Computers](https://www.tuxedocomputers.com/index.php) 还提供使用 Tuxedo OS Linux 和 Ubuntu 的 Linux 专用电脑。还有许多其他选择。

但是，Linux 有一套非常强大的驱动程序，并且与当今大多数标准和现代硬件兼容。我不会犹豫在几乎任何我遇到的电脑上安装这个操作系统。

## 什么是虚拟化？

虚拟化软件采用与裸机安装截然不同的方法。此解决方案从裸机硬件设备和现有操作系统（如 Linux、Windows 或 macOS）开始。您将像安装网页浏览器或 PDF 阅读器一样在计算机上安装虚拟化软件。此软件允许您创建虚拟计算机，您可以在其上安装各种操作系统，包括 Linux。

虚拟化软件将您的计算机的进程、内存、存储和网络功能划分为“虚拟机”，并允许在这些虚拟机上安装操作系统。
虚拟化是一个奇怪的概念。让我们通过检查“虚拟机”这两个词来分解它。“虚拟”这个词意味着假装或模拟。在这种情况下，处理器、内存、存储和网络功能正在被模拟。“机器”这个词表明它们被模拟得好像它们是一台真正的计算机。本质上，您是在您的常规计算机和操作系统软件中创建一台假装的计算机。

![](https://cdn.thenewstack.io/media/2024/05/9ba0a520-ubuntu-vm.png)

*图 1：在 Parallels 虚拟化软件中运行的 Ubuntu 22.04 虚拟机的处理器和内存规格。*

因为这台虚拟机看起来和运行起来像一台真正的计算机，所以您可以在它上面安装一个操作系统，这样您就可以像使用任何其他计算机一样使用它。

### 虚拟化示例

考虑以下示例：假设我有一台 Apple MacBook Pro 笔记本电脑。这个物理设备包含一个 Apple Sonoma macOS 的安装。我可以使用这台笔记本电脑和安装在其上的程序来编写文档、浏览网页、管理电子邮件和编辑图像。换句话说，这是一台基本的日常使用计算机。

但是，如果我决定学习一些 [Python 编程](https://thenewstack.io/python/) 呢？我可以毫无问题地使用 macOS 来做到这一点，但将我的编程实验隔离可能很有用，这样如果出现问题，我就不会破坏我用于业务的计算机。我可以在我的 Mac 上安装 Parallels 等虚拟化软件，然后创建一个虚拟机，从我的物理计算机借用处理器、内存、存储和网络。然后，我会在该虚拟机上安装 Fedora Linux 发行版。Fedora 会将此 VM 视为一台真正的计算机。然后，我可以将任何 Python 工具和资源添加到 Fedora VM 中，并使用它来处理我的编程项目。

![](https://cdn.thenewstack.io/media/2024/05/4f39987e-vm-on-mac.png)

*图 2：正在运行 Ubuntu VM 的 MacBook Pro 上的 Parallels 虚拟化应用程序。*

## 比较裸机和虚拟化

裸机和虚拟化方法各有优缺点，不过我要说虚拟化确实是一个非常强大的解决方案。

**裸机的优点：**

- 硬件控制

**裸机的缺点：**

- 更贵
- 空间
- 功耗
- 冷却
- 噪音

**虚拟化的优点：**

- 节省成本
- 空间、冷却和噪音降低
- 使用一台计算机运行多个操作系统

**虚拟化的缺点：**

- 包括学习曲线，尽管基本部署很简单
- 软件可能很贵
- 会给主机计算机的资源带来压力

如今大多数计算机都足够强大，可以同时运行主机操作系统和至少几个 VM。这足以让您尝试几个不同的 Linux 发行版，找到您喜欢的那个。我经常在我的 Mac 笔记本电脑上同时运行 Fedora 和 Ubuntu Linux VM，没有任何性能下降，而且我毫不犹豫地同时运行两个或三个以上的 VM。强大的服务器可以同时托管许多生产 VM。

### 虚拟化软件选项

您有很多虚拟化软件选项。两个主要限制是与您的主机操作系统（Windows、macOS 或 Linux）的兼容性和成本。以下列表显示了最常见的选项。

- [VMware Workstation Pro](https://www.vmware.com/products/workstation-pro.html)：在 Windows 和 Linux 主机系统上运行 Windows 和 Linux VM。VMware 提供了一些不同的购买选项，但 Workstation Pro 的价格为 199 美元。
- [Parallels](https://www.parallels.com/)：在 Apple macOS 主机系统上运行 Windows 和 Linux VM。Parallels 提供标准版或专业版订阅。专业版订阅起价为 95.99 美元/年。
- [Microsoft Hyper-V](https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-enabling-hyper-v-for-use-on-windows-11/ba-p/3745905)：如果您有 Windows 11，您可以添加 Microsoft 的 Hyper-V 虚拟化软件来运行 Windows 和 Linux VM。Hyper-V 本身没有成本，但您必须拥有 Windows 11 专业版或企业版的许可副本。
- [Oracle VirtualBox](https://www.virtualbox.org/)：VirtualBox 在 Windows、Linux 和 macOS 主机上运行，并支持 Windows 和 Linux VM。它是免费的开源软件。VirtualBox 是一个强大的选项，对于大多数用户来说都是一个不错的选择。
- [Gnome Boxes](https://apps.gnome.org/Boxes/)：Boxes 在 Linux 主机上运行，并支持各种 Linux 和 Windows 操作系统。它是 Linux 系统的免费开源产品。

请注意，定价和规格信息在撰写本文时是当前的。

![](https://cdn.thenewstack.io/media/2024/05/5fabc633-control-center.png)

*图 3：Parallels 控制中心显示两个已安装的虚拟机。*

## 考虑使用 Raspberry Pi

另一个有趣的选项是 [Raspberry Pi](https://www.raspberrypi.com/) 平台。Raspberry Pi 是一款体积小巧的单板计算机，在如此小的体积内却拥有惊人的性能。您可以在其上安装 [专为 Raspberry Pi 设计的 Linux 发行版](https://www.raspberrypi.com/software/)，以运行各种应用程序，使用物联网工具或流式传输多媒体。这些设备体积小巧、灵活且价格实惠。它们最初的设计目的是让孩子们对编程和计算感兴趣。Ubuntu 甚至有一个 [Pi 版本](https://ubuntu.com/download/raspberry-pi) 的发行版。

对于那些想要深入了解 Linux 的人来说，Raspberry Pi 是一个不错的选择。

![](https://cdn.thenewstack.io/media/2024/05/d1bb3a6b-rpi-rotated.jpg)

*图4：树莓派3型B电脑。*

## 容器怎么样？

[容器](https://www.docker.com/resources/what-container/) 是一种更新的虚拟化形式，如今备受关注。您可能想知道在容器中使用 Linux 来学习操作系统。这当然是可以的，但这个过程比传统的虚拟机更复杂，而且操作起来并不容易。

与虚拟机一样，容器需要在您的普通计算机上运行主机软件（容器引擎）。但是，容器实际上是为应用程序而不是操作系统层设计的计算环境。

虽然我强烈建议您 [尽可能多地学习有关容器的知识](https://thenewstack.io/containers/how-to-deploy-a-container-with-docker/)，但我认为您会发现比将 Linux 容器化更有效的方式来使用 Linux 操作系统。

## 总结
学习新操作系统的最关键部分是动手实践。如果您准备每天使用 Linux，您需要一种方法来练习命令、安装软件、配置安全等。您可以通过在物理计算机系统上安装 Linux 或在现有计算机上创建虚拟机来获得这种经验。这两种选择都有各自的优势，但虚拟化通常更便宜、更简单。此外，如果您在 IT 行业工作，您还需要熟悉虚拟化。最后，虚拟机使您更容易尝试各种可用的 Linux 发行版。我建议从 [Ubuntu](https://ubuntu.com/desktop)、[Fedora](https://fedoraproject.org/workstation/)、[Rocky](https://rockylinux.org/) 或 [Mint](https://www.linuxmint.com/) 开始。
