
<!--
title: CachyOS 是一个面向（几乎）所有人的 Arch Linux 发行版
cover: https://cdn.thenewstack.io/media/2024/12/fc5cdb8e-cachyoshero.jpg
-->

如果你想尝试一个能提升你技能的操作系统，CachyOS 是个不错的选择。

> 译自 [CachyOS Is an Arch Linux Distribution for (Almost) Everyone](https://thenewstack.io/cachyos-is-an-arch-linux-distribution-for-almost-everyone/)，作者 Jack Wallen。

Arch Linux 因其对普通用户而言过于具有挑战性而臭名昭著，这很可惜，因为它也是一个任何人都能从中受益的极其稳定的发行版。[Arch Linux](https://archlinux.org/)最具挑战性的方面之一是安装过程，这需要对 Linux（以及一般操作系统）的工作原理有扎实的理解。对于那些不了解[Linux 基础知识](https://thenewstack.io/learning-linux-start-here/)的人来说，Arch 不是一个好选择。

幸运的是，有很多用户友好的 Arch Linux 版本，所有这些版本都使安装过程成为一项点击即可完成的事务。其中一个发行版叫做[CachyOS](https://cachyos.org/)。根据官方网站，“我们的发行版提供无缝的安装过程和一系列定制选项，以个性化您的计算体验。无论您是初学者还是经验丰富的用户，CachyOS 都能提供优化的性能，同时保持其简洁性。”

在安装过程的早期，您可以选择桌面环境（图 1）。

![](https://cdn.thenewstack.io/media/2024/11/d0ba0549-cachyinstall.jpg)

*图 1：您可以为您的 CachyOS 选择几种桌面环境。*

对于新用户，我建议选择 Plasma 桌面、Budgie、Cinnamon 或 Mate。

有 Linux 经验的用户会对任何选项都感到满意。如果您想要最高效的桌面，也许 i3 或[Hyprland 平铺窗口管理器](https://www.youtube.com/watch?v=wgajzUIZNh8) 是最佳选择。我选择使用 Cosmic，因为我预测它将成为我未来的发行版。如果您不熟悉它，Cosmic 是 System76 开发的桌面环境。目前，Cosmic 仍处于 alpha 阶段，但我发现它非常稳定。即便如此，我不建议您将 Cosmic 作为首选——至少在其正式发布之前不要这样做。

我实际上（并且令人愉快地）惊讶地发现 CachyOS 在其选项列表中包含了 Cosmic，并且很乐意尝试一下。

它没有让我失望。

## CachyOS 的特别之处是什么？

显而易见的答案是它使 Arch Linux 更容易被更多用户访问。CachyOS 与市场上被认为最用户友好的那些发行版一样易于使用（想想[Linux Mint](https://thenewstack.io/tutorial-install-linux-mint-on-a-windows-laptop-using-a-usb-stick/) 和[Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)）。当然，这取决于您选择的桌面，但如果您选择了合适的桌面，您会发现 CachyOS 使用起来非常愉快。

登录后首先看到的是欢迎工具，其中包括对自述文件、发行说明、论坛、软件、应用程序/调整、安装应用程序等的快速访问。您可以将其视为一个“第一步”工具，以帮助您了解各种功能。在我看来，每个发行版都应该包含一个欢迎应用程序。

对于[Linux 新手](https://thenewstack.io/learning-linux-start-here/)，您想要采取的前两步将是欢迎应用程序中的应用程序/调整和安装应用程序选项。应用程序/调整部分提供诸如*profile-sync-daemon enable*、*system-oomd enable*、*bpftune* enabled 和 Bluetooth enabled 等调整。修复部分包括系统更新、重新安装所有软件包、刷新密钥环、删除数据库锁、清除软件包缓存、删除孤儿文件、安装游戏软件包、安装 Snapper 支持、排名镜像、更改 DNS 服务器和安装 SpoofDPI 等选项。

从**欢迎 > 应用程序/调整**，还有 CachyOS 内核管理器，它允许您从几个不同的内核中进行选择，例如强化内核、实时内核等等。默认安装的内核是 6.11.7-1。

至于预安装的软件，您会发现选择相当有限。当然，这也取决于您选择的桌面。使用 Cosmic 选项，有 Vim（一个强大的文本编辑器）、Cosmic 终端（一个终端应用程序）、Catchy 浏览器（网络浏览器）、Meld（一个差异工具）、Btrfs Assistant（一个用于调整 Btrfs 文件系统的工具）等等。
Octopi是Pacman软件包管理器的前端，它让我想起了Synaptic，虽然它看起来并非是最现代化的前端，但它非常有效且易于使用。（图2）在Octopi中，您可以搜索要安装的应用程序，右键单击它，从弹出菜单中选择“安装”，然后单击绿色复选标记继续。系统会提示您确认安装，然后要求您输入用户密码。完成此操作后，安装将开始并完成。

![](https://cdn.thenewstack.io/media/2024/11/63a5e313-cachyoctopi.jpg)

*图2：对于任何使用过Synaptic的人来说，Octopi软件包管理器应该很熟悉。*

安装完成后，软件将可在桌面菜单中使用。

Octopi并非唯一的安装程序应用程序。还有CachyOS软件包安装程序（图3），它实际上比Octopi更易于使用。使用CachyOS软件包安装程序，您可以选择要安装的软件包，单击“安装”并输入您的用户密码。

![](https://cdn.thenewstack.io/media/2024/11/d4ad9358-cachypackage.jpg)

*图3： CachyOS软件包安装程序。*

如果您是Linux新手，我建议您使用CachyOS软件包安装程序，因为它更简单易用。

只是为了好玩，我使用了CachyOS内核管理器并安装了*linux-cachyos-rt-bore*，它基于不同的调度程序和其他一些性能改进，看看它的效果如何。新的内核安装完成后，我重新启动并发现性能略有提高，考虑到该操作系统开箱即用的性能，这已经说明了一些问题。它并不完美，因为我确实注意到在移动光标时出现了一些“卡顿”，几乎就像操作系统短暂暂停一样。

为了缓解这个问题，我将分配给虚拟机的RAM增加到6GB（从我通常给虚拟机分配的3GB增加）。此更改并没有解决问题，因此我选择安装不同的内核，这次是6.10 extra/linux-rt（实时）内核。值得庆幸的是，CachyOS内核管理器使这变得非常容易。该内核解决了问题，CachyOS又恢复了流畅运行。当然，您的实际情况可能会有所不同，具体取决于您使用的硬件。

## CachyOS适合您吗？

通常，我不建议新手用户使用基于Arch的Linux发行版，CachyOS也属于同一类别。但这是否意味着每个新手用户都应该避免使用此发行版？不。如果您喜欢冒险，并且想要一个能够提升您技能的操作系统，那么CachyOS是一个不错的选择。如果您想要最适合Linux经验很少的用户的东西，我建议您坚持使用Ubuntu、Linux Mint或ZorinOS。

但是，如果您想体验轻松上手Arch Linux的途径——并且喜欢在操作系统安装过程中能够从几个不同的桌面环境中进行选择的想法——那么CachyOS是一个不错的选择。在我的测试期间，我非常享受使用COSMIC桌面（它很快将成为我的System76 Thelio桌面机器上的默认桌面），并且相信它将成为Linux市场上最热门的桌面之一。

如果您有兴趣测试CachyOS，请[下载ISO镜像](https://cachyos.org)，将其刻录到可启动的USB驱动器（使用[uNetBootin](https://unetbootin.github.io/)之类的工具），然后试用一下。我很确信您会喜欢您所看到的。
