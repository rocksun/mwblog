[Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 在过去几年中，在终端用户和开发者中都逐渐受到欢迎。这有很多原因，例如Windows 10的终结、易用性、灵活性、可靠性、游戏以及……开发。

没错，Linux是一个出色的开发平台。它不仅拥有你所需的所有工具，而且这些工具通常都是免费、开源且易于安装的。除此之外，你还有 [Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/)、Podman、 [Kubernetes](https://thenewstack.io/kubernetes/)、虚拟机（VMs）等等。

一般来说，列出最适合终端用户的Linux发行版很容易，但谈到开发时，你肯定会听到各种各样的意见。大多数情况下，这些意见更多地围绕着某个特定开发者使用的发行版，而不是“无论我用什么，这都是适合这项工作的正确工具”。

我已将这份列表精简为五个不同的发行版。我承认我首选的发行版就在这份列表上，但我向你保证，即使我没有使用它十年，我仍然会推荐它。

请记住，几乎任何Linux发行版都可以变成开发机器。安装合适的工具链，添加你喜欢的语言和IDE，混合一个容器运行时引擎，你就可以开始工作了。

但我想重点介绍我认为市场上最好的发行版。

准备好了吗？

开始吧。

## 1. Debian

[Debian](https://www.debian.org/) 被称为“所有发行版之母”是有原因的。Debian是Ubuntu的基础，而大量的发行版又基于Ubuntu。没有Debian，就没有Ubuntu。此外，Debian是最坚如磐石的操作系统之一，这绝不夸张。其原因在于Debian采用保守的发布周期、经过严格审查的应用程序以及快速/安全的更新。

除了稳定性，你还可以通过Debian仓库安装大量的软件，获得强大且用户友好的软件包管理器以及多架构支持。开发者还可以选择他们想要使用的分支，从稳定版、测试版或前沿版。Debian也很快，高度可定制，有不同的桌面环境可供选择。Debian还拥有非常庞大的用户群，这意味着你可以轻松找到任何问题的支持。

最后，Debian非常安全。Debian与基于Ubuntu的发行版不同的一点是，它不会为标准账户启用sudo权限。如果你需要做一些需要管理员权限的事情，你需要使用老方法，切换到root用户。当然，如果你愿意，你可以将你的标准用户添加到sudo组中，以获得更友好的体验。

## 2. Fedora

对许多人来说，[Fedora](https://www.fedoraproject.org/) 是开发的首选。主要原因之一是Fedora是一个专注于新技术的平台，通常比其他发行版更早地采用新软件。Fedora是首批切换到Wayland、使用 [Btrfs](https://en.wikipedia.org/wiki/Btrfs)，并且总是在其他任何发行版发布之前享受到最新版 [GNOME](https://thenewstack.io/what-makes-gnome-so-appealing/) 的发行版之一。由于它附带了新版本的软件，你可以放心，你的工具链应用程序（例如 [GCC](https://thenewstack.io/rust-support-is-being-built-into-the-gnu-gcc-compiler/)）和语言（如 [Python](https://thenewstack.io/what-is-python/)）都将是可用的最新版本。因此，你开箱即用时需要安装或升级的软件会更少。你也不必添加非官方仓库来访问最新版本。Fedora还包括面向开发者的工具，例如编译器和IDE，以及用于创建可重现开发环境的toolbox命令。Fedora还附带了GNOME Boxes应用程序。这款应用程序使得启动虚拟环境变得非常容易，而无需处理VirtualBox或其他VM工具的麻烦。尽管Fedora倾向于“前沿”，但它仍然非常可预测、可靠和稳定。最后，Fedora拥有一个非常大的社区，因此寻找支持绝不是挑战。

## 3. Pop!\_OS

没错，[Pop!\_OS](https://system76.com/pop/?srsltid=AfmBOooG-OYmDfh-ZGheSpaRf4tXaNvvFTnR7phBtIgqhZ8qnL2N00UL) 是我首选的发行版。现在System76推出了 [COSMIC桌面](https://system76.com/cosmic?srsltid=AfmBOooh91B6mMGg_aGi2oBAsL5GRdwSI6CCbr2yPTFL7M840sUGdACd)，它变得更好了。关于COSMIC，你首先会注意到它快得令人难以置信。这是因为桌面环境是用Rust编写的，Rust是一种快速的语言。除了速度，Pop!\_OS实际上是专为创作者打造的。另一个让Pop!\_OS超越许多其他发行版的特性是能够随时启用或禁用平铺窗口管理。如果你需要一个更高效的桌面环境，就启用平铺功能。如果不需要，就关闭它。

Pop!\_OS登上此列表的另一个非常重要的原因是，System76为NVIDIA和AMD GPU提供了ISO镜像。通过选择正确的ISO，你无需担心为你选择的GPU安装驱动程序。安装了适当的NVIDIA驱动程序后，你将在机器学习（ML）和人工智能（AI）开发方面拥有更轻松的体验。Pop!\_OS使用APT软件包管理器，因此你将受益于各种各样的软件。最重要的是，你还可以使用Flatpak获取更多选择。最后，Pop!\_OS开箱即用提供全盘加密，这意味着如果你的系统或驱动器被盗或丢失，你无需担心它会被访问。

## 4. openSUSE

首先，[openSUSE](https://www.opensuse.org/) 有两个不同的版本：Tumbleweed和Leap。Tumbleweed是一个滚动发布发行版，这意味着你将始终拥有最新最好的软件。openSUSE与其他滚动发布发行版之间的区别在于，开发团队使用openQA测试框架来确保更高的稳定性水平，这是你在其他滚动发布版上找不到的。或者，如果你更喜欢长期支持，可以选择Leap版本。你还将获得一些构建者专用的工具，例如Open Build Service（一个强大、基于网络的工具，用于简化软件构建和分发过程）、YaST（一个强大而全面的管理工具，允许开发者一键安装所有必要的-devel软件包）以及Btrfs文件系统（包含快照功能，使回滚到以前的状态变得容易）。openSUSE也开箱即用，非常适合通过Docker、Podman和Kubernetes进行容器化。

## 5. Linux Mint

如果你问任何开发者为什么选择 [Linux Mint](https://linuxmint.com/)，答案很简单：因为它太容易使用了。这种用户友好性意味着能够零问题地启动和运行操作系统，并获得尽可能简单可靠的用户体验。Linux Mint也受益于Ubuntu的基础，因此即使安装所有必要的构建组件，也只需一个命令即可完成：*sudo apt-get install build-essential -y*。这个软件包安装了一整套必需的工具和库，这些工具和库是编译和从源代码构建软件所必需的。你将获得C和C++编译器、GNU Make、标准C和C++库的头文件、dpkg-devel等等。Linux Mint还默认使用Cinnamon桌面，它即刻熟悉、快速且稳定。在开发者环境中，你还需要什么呢？