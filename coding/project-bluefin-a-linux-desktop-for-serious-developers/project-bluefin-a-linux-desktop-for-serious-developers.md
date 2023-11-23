<!--
title:  专业开发者定制的Linux桌面系统
cover: https://cdn.thenewstack.io/media/2023/11/52f1a3ea-bluefin-1024x636.png
-->

如果您想要一个基于Fedora稳定内核，采用Ubuntu桌面风格，为开发者专门定制的Linux桌面系统，那Bluefin正符合您的期待。

> 译自 [Project Bluefin: A Linux Desktop for Serious Developers](https://thenewstack.io/project-bluefin-a-linux-desktop-for-serious-developers/)，作者 Steven J. Vaughan-Nichols ，别名 sjvn，自从 CP/M-80 是前沿的 PC 操作系统，300bps 是快速的互联网连接，WordStar 是最先进的文字处理器，我们就一直喜欢它，他就一直在写有关技术和技术业务的文章。

像许多玩编程的人，更重要的是，那些真正从事这项工作的人一样，我使用 Linux 桌面。好吧，我不能比 [Bluefin](https://github.com/ublue-os/bluefin) 的创造者 Jorge Castro 来得更好，他是一位顶级开源和 Linux 社区经理，"Bluefin 是 GitHub 中一群云原生极客自动化整个交付流水线创建的 [Fedora Silverblue 的自定义镜像](https://www.ypsidanger.com/announcing-project-bluefin/)。我们想要一个可靠的桌面体验，可以运行所有的东西，但我们又太懒惰无法维护任何东西。"

我喜欢它！

逐一分析，[Fedora Silverblue](https://fedoraproject.org/silverblue/) 是一种使用 GNOME 接口的不可变桌面 Linux。在此基础上，Castro 和他的伙计们想要一个更像 Ubuntu 的桌面。

[Bluefin](https://projectbluefin.io/) 有三个目标:  

- 对终端用户来说，提供一个像 Chromebook 一样可靠的系统，几乎零维护，具有 Ubuntu 和 Fedora 融合在一起的功能
- 对开发人员来说，通过启用易于使用来提供最好的云原生开发人员体验，这包括专门的带有[行业领先工具](https://landscape.cncf.io/card-mode?sort=stars)的 bluefin-dx 和 bluefin-dx-nvidia 镜像。
- 为玩家提供一流的 [Flathub](https://flathub.org/en) 游戏体验

Project Bluefin，现在处于测试阶段，不仅仅是另一个 Linux 发行版。它是增强版的 Fedora Silverblue，经过打磨，提供了更可靠和免维护的桌面体验。该项目经过定制，面向那些觉得传统 Linux 桌面不够可靠的人，在默认 Fedora 镜像的基础上提供了干净的原子层。这意味着如果需要，用户始终可以恢复到股票镜像。  

不喜欢 Ubuntu 的方法？没问题。正如 Casto 写的那样，"您可以根据需要切换用户空间。默认情况下，它是 Bluefin/Ubuntu，但我一直在享受 Bluefin/Alpine 的速度和小巧。在某些时候，我也会迁移到使用 [Wolfi 镜像](https://github.com/wolfi-dev?ref=ypsidanger.com)。换句话说，“使用任何你想要的，或者坚持 Fedora 股票镜像。我们有意不规定开发人员的工作流程；任何对你有效的都行。[Homebrew](https://brew.sh/) 是我首选的路线，我推荐给那些迁移到 Bluefin DX 的人。"

该项目已经通过 GitHub 上的交付流水线完全自动化，确保更新是自动和透明的。它拥有内置驱动程序和运行 Flathub 应用程序包的能力。这为您提供了浏览器的选择，并且带有内置的容器运行时，您可以在其上运行几乎任何 Linux 工作负载。  

## 面向开发者

对于开发者来说，Project Bluefin 是一个宝库。它内置了 [Podman](https://thenewstack.io/check-out-podman-red-hats-daemon-less-docker-alternative/) 容器运行时，并包含 [distrobox](https://github.com/89luca89/distrobox) 用于交互式体验，允许用户为日常任务选择任何发行版镜像。另外，开发人员镜像 bluefin-dx 配备了 [Visual Studio Code](https://code.visualstudio.com/) with [devcontainers](https://devcontainers.github.io/)、[devbox with Fleek for nix](https://getfleek.dev/)、[devpod](https://devpod.sh/)、homebrew 和 [Docker](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/)。无论您的开发需要是什么，Bluefin 都可以满足。  

该项目还解决了开源贡献的可持续性问题。它是使用常见的工具如 Containerfiles with [Python/Shell](https://thenewstack.io/how-python-is-evolving/) 构建的，使其可以为许多贡献者所接受。治理和程序都很重要，欢迎贡献，特别是那些具有云原生知识的人。

## Bluefin 社区

Project Bluefin 不仅仅是关于技术；它关乎社区和可持续性。该项目的图像以恐龙为特色，这是对开源生态系统中所需演化和适应能力的点头。Bluefin 背后的团队小心确保从贡献角度来看，该项目很轻量，完全自动化了大部分维护工作，从而允许开发人员专注于创新而不是维护。

随着该项目于 2024 年春季推出公测版，团队专注于优化安装体验和解决次要问题。开发人员有信心，未来几个月的安装过程会有显着改善。

Project Bluefin 代表着新一代 Linux 桌面用户和开发者的新起点，旨在加速云原生技术的消费，并作为软件工程和开发的可靠平台。

对于那些对 Linux 桌面和云原生开发未来感兴趣的人来说，Project Bluefin 是值得关注的发行版。该项目的测试阶段是对社区的邀请，加入并为可能成为 Linux 桌面最先进的状态做出贡献。

我认识 Castro 好多年了，也了解他对 Linux 桌面的热情。他对 Bluefin 的梦想是，“如果我们可以使用 Linux 桌面直接引入人们进入云原生怎么样？”

他能成功吗?试一试，加入社区。我想你会印象深刻的。

