<!--
title: 了解一下Debian，所有Linux发行版的“鼻祖”
cover: https://cdn.thenewstack.io/media/2024/05/199b905f-debian.png
summary: Debian被称为“所有Linux发行版的母亲”，以稳定性著称。它提供安全、免费开源的定制化体验，拥有庞大社区和完善文档。Debian有稳定版、测试版和不稳定版，支持GNOME、KDE Plasma等桌面环境，并通过Discover添加Flatpak/Snap支持，适合追求稳定和旧系统支持的用户。
-->

Debian被称为“所有Linux发行版的母亲”，以稳定性著称。它提供安全、免费开源的定制化体验，拥有庞大社区和完善文档。Debian有稳定版、测试版和不稳定版，支持GNOME、KDE Plasma等桌面环境，并通过Discover添加Flatpak/Snap支持，适合追求稳定和旧系统支持的用户。

> 译自：[Check Out Debian, the 'Mother of All Linux Distributions'](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/)
> 
> 作者：Jack Wallen

您多久听到或读到关于基于 [Ubuntu](https://thenewstack.io/cubic-build-a-custom-linux-distribution-based-on-ubuntu/) 的发行版？有 [Kubuntu](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/)、[elementaryOS](https://thenewstack.io/elementary-os-a-linux-distro-easy-to-use-and-easy-on-the-eyes/)、[Zorin OS](https://thenewstack.io/zorin-os-the-perfect-linux-distro-for-migrating-from-windows/)、[Deepin](https://www.deepin.org/index/en)、[Ubuntu Budgie](https://ubuntubudgie.org/)、[KDE neon](https://thenewstack.io/kde-neon-is-the-linux-distribution-with-the-dynamic-desktop/)……这个列表没完没了。

如此多的操作系统开发人员[基于 Ubuntu 构建他们的发行版](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)是有原因的：

- 它很可靠。
- 它对用户友好。
- 它提供了市场上最好的安装程序之一。
- 它很容易定制。
- 它具有一些最好的硬件检测功能。

但是，如果您知道 Ubuntu 反过来又是基于另一个发行版，您会怎么说？

你们大多数人可能会说：“废话”。

## 所有 Linux 发行版的母亲

对于那些试图用一个音节让我感到羞愧的人，您应该知道 Ubuntu 是基于 [Debian](https://www.debian.org/) 的。

Debian 项目成立于 1993 年 8 月，旨在创建真正开放的 Linux 发行版，本着 [Linux 和 GNU](https://thenewstack.io/learning-linux-start-here/) 的精神。“Debian”这个名字是其两位联合创始人 Debra Lynn 和 Ian Murdock 的名字的组合。

Debian 已被称为“所有发行版的母亲”，因为，嗯，Ubuntu。由于如此多的发行版都基于 Ubuntu，并且由于 Ubuntu 是 Debian 的“孩子”，因此将其标记为“母亲”是合理的。

有了所有这些基于 Ubuntu 的发行版，为什么还要费心使用 Debian 呢？毕竟，它不是以预装可能被认为过时的软件而闻名吗？

嗯，是的。但是——相信我，这是一个重要的大*但是*——Debian 的一切都与一件事有关，那就是稳定性。

## 为什么选择 Debian？

除了它提供的坚如磐石的稳定性之外，还有很多理由采用 Debian 作为您的首选 Linux 发行版，包括：

- **安全性**：Debian 不仅关注稳定性。由于其严格的测试过程，Debian 也非常安全。事实上，Debian 开发人员花费的测试时间比其他发行版团队要多得多。
- **免费和开源**：Debian 仅包含免费和开源的软件。
- **大型社区**：Debian 拥有最大和最活跃的开发人员、维护人员和用户社区之一，远远超过任何其他发行版所提供的。
- **可定制性**：由于拥有庞大的软件包存储库，Debian 允许高度的定制。
- **低维护**：由于 Debian 非常稳定，因此几乎不需要维护。
- **文档**：Debian 的文档非常完善。

对于大多数普通用户来说，采用 Debian 的主要原因是您在大多数其他操作系统中找不到的稳定性。在我使用 Debian 的这些年中，我从未遇到过任何问题。现在，这可以对许多 Linux 发行版说，但 Debian 将其提升到了更高的水平。

## 版本

Debian 有三个不同的“版本”：

- **稳定版**：Debian 最新正式发布的发行版，建议日常使用。
- **测试版**：测试版包含尚未被接受到“稳定”版本中的软件包，但正在排队中。使用测试版的主要优点是它包含更新版本的软件。
- **不稳定版**：这是开发最活跃的版本，建议由开发人员和喜欢“走在前沿”的人使用。不建议日常使用此版本。

Debian 不会发布带有特定桌面的特定版本。相反，您可以下载一个 ISO，并在安装过程中，您可以从 GNOME、KDE Plasma、Xfce、MATE、Cinnamon、LXDE 或 LXQt 中进行选择。当然，您也可以在安装操作系统后安装不同的桌面环境，例如 Budgie 或 COSMIC。

为了本次评测的目的，我安装了带有 KDE Plasma 的 Debian。

![桌面截图。](https://cdn.thenewstack.io/media/2025/03/e998b570-debianhero.jpg)

*默认的 Debian KDE Plasma 桌面。*

## Debian 就是 Debian
关于 Debian，我真正敬佩的一点是，它始终如一。当你第一次登录时，你清楚地知道会发生什么。倒不是说 Debian 一成不变；而是它太可靠了，以至于感觉有点静态。即使 KDE Plasma 版本是 5.27.5，它给我的感觉也没有比上次使用 Debian 时更新鲜。这可能是因为我通常在 Debian 上安装 GNOME，所以还是一如既往。

Debian 还附带了常见的开源软件：

- Firefox (ESR)
- LibreOffice
- Akregator (RSS feed reader)
- Dragon Player (video)
- GIMP (image editor)
- JuK (music player)
- KMail (email client)
- Konqueror (web browser)
- Sweeper (system cleaner)

还有 Discover，它允许你安装你可能需要的所有软件。如果你想添加 [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) 或 [Snap](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/) 后端，你可以进入 Discover > 设置并安装必要的软件包（**图 1**）。

![Screenshot](https://cdn.thenewstack.io/media/2025/03/f41f6609-debian1.jpg)

*在 KDE Plasma 的 Discover 中添加 Flatpak 和/或 Snap 支持。*

添加 Flatpak 或 Snap（或两者都添加）的一个好处是，Debian 能够安装更新版本的软件包（只要它们在 Flathub 或 Snapcraft 存储库中可用）。只需确保重新启动 Discover 以使更改生效。

## Debian 适合谁？

简而言之，当稳定性至关重要时，你应该使用 Debian 这个 Linux 发行版。Debian 也非常适合旧系统支持，这意味着它可以轻松地在你的旧硬件上运行。

但是，如果你只是想要一个很少（甚至永远不会）让你失望的操作系统，那么 Debian 是你可以做出的最明智的选择之一。

但是，有一件事你应该了解 Debian：为了提供尽可能高的安全性，开发人员在发布操作系统时，不会自动为标准用户提供 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)。因此，你所做的任何需要管理员权限的更改都必须先使用命令 `su -` 切换到 root 用户后才能完成。你可以使用以下命令将用户添加到 sudo 组：

```bash
usermod -aG sudo USER
```

将上面语句中的“USER”替换为用户名。
完成此操作后，用户需要注销并重新登录才能使更改生效。

如果安全性是你决定选择 Debian 的主要原因，我建议不要将用户添加到 sudo 组——这样，你就可以控制谁拥有系统上的管理员权限。

如果有人问我认为最稳定的操作系统是什么，答案是自动的：Debian。如果有什么可以确定的话，那就是运行 Debian 的机器不会出现故障（至少在软件层面——因为硬件最终总是会发生故障），并且会为你服务很长时间。

如果我对 Debian 引起了你的兴趣，你可以从 [Debian 官方网站](https://www.debian.org/) 下载最新版本。