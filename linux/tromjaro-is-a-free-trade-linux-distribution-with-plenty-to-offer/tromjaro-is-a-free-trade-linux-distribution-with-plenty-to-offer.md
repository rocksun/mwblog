<!--
title: Tromjaro：功能丰富、自由贸易的Linux发行版
cover: https://cdn.thenewstack.io/media/2026/03/252e699f-razvan-vezeteu-kl8rphbr1xs-unsplash-1.jpg
summary: Tromjaro是一款基于Manjaro的自由贸易Linux发行版，强调隐私保护，预装丰富软件，提供桌面布局和内核管理。功能强大但对Linux新手可能过于复杂，适合有一定经验的用户。
-->

Tromjaro是一款基于Manjaro的自由贸易Linux发行版，强调隐私保护，预装丰富软件，提供桌面布局和内核管理。功能强大但对Linux新手可能过于复杂，适合有一定经验的用户。

> 译自：[Tromjaro is a free-trade Linux distribution with plenty to offer](https://thenewstack.io/tromjaro-is-a-free-trade-linux-distribution-with-plenty-to-offer/)
> 
> 作者：Jack Wallen

想象一下，拥有一个不会追踪你、向你推送广告、也不会强制你进行“免费”试用的操作系统。

听起来像 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/)，不是吗？

确实如此，因为这正是大多数 Linux 发行版所追求（并实现）的目标。

但有些发行版通过“自由贸易”将这个理念推向了更深层次。自由贸易意味着什么？首先，它意味着开发者不向你索取任何东西，因此不会收集任何数据，也不收取费用。

本质上，它核心是 [FOSS](https://thenewstack.io/what-can-enterprise-open-source-really-do-for-you/)（自由开源软件），所以当开发者说他们不向你索取任何东西时，你可以信任他们。

[Tromjaro](https://www.tromjaro.com/) 基于 [Manjaro](https://manjaro.org/)，但它加入了许多原始版本所没有的功能。

例如，Tromjaro 使用了定制版的 [Firefox](https://thenewstack.io/how-mozillas-ai-strategy-disconnects-from-its-browser-heritage/)（使其成为自由贸易版本），因此它无法收集数据、进行追踪或地域限制，甚至还添加了工具，让你可以从任何网站下载视频、音频文件和照片。

除了这些功能，Tromjaro 的 Firefox 版本还增加了：

*   Privacy Badger – 学习阻止追踪器。
*   uBlock Origin – 内容拦截器。
*   SponsorBlock – 让你跳过 YouTube 视频赞助商。
*   LibRedirect – 将网站重定向到隐私友好的前端。
*   Sci-Hub X Now – 解锁科学论文。
*   Wayback Machine – 让你快速访问 Wayback Machine。
*   KeePassXC – 密码管理器的插件。
*   Enable Right Click & Copy – 强制启用右键点击和复制。

Manjaro 也使得录制屏幕、发送文件、通信、控制远程机器、关注 RSS 源、阻止网页内容、添加网页应用以及使用自由贸易的 [RiseupVPN](https://riseup.net/en/vpn) 变得容易。

此外还有其他功能，其中一个让我非常兴奋。这个功能叫做 HUD。这个出色的附加功能最初是在 [Ubuntu](https://thenewstack.io/ubuntu-unity-25-04-brings-back-ubuntus-biggest-miss/) 中提供的，当时 Unity 是其默认桌面。HUD 的理念是，你将焦点放在一个特定的应用程序上（通过点击它），按下热键，它就会为该应用程序弹出一个菜单搜索工具。搜索你想要的菜单项并按 Enter 键。

例如，你可能想在 LibreOffice 中居中文本。你可以打开 HUD，搜索“居中”，然后选择正确的选项。这可以避免你在冗长的菜单中搜索你想要的功能。

现在，在你对这个功能感到过于兴奋之前，请了解两件事：并非所有应用程序都支持 HUD，而且我无法让它正常工作。遗憾的是，我尝试了所有方法（甚至各种应用程序），但都无济于事。

## Tromjaro 有何特别之处？

我总是问自己一个问题：一个特定的 [Linux 发行版](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/) 与竞争对手相比有何不同之处？

Tromjaro 希望成为一个能保证不收集任何信息的发行版。这很重要，但许多发行版也能做出同样的声明。

然而，Tromjaro 的一个突出之处是它包含一个桌面布局切换器（**图 1**）。Tromjaro 的默认桌面是 Xfce，它提供了六种不同的布局：Windows风格、MX风格、Unity风格、macOS风格、GNOME风格和TOPX风格。

![](https://cdn.thenewstack.io/media/2026/03/dee5e54d-tromjarolayout.jpg)

***图 1：** Tromjaro Xfce 布局切换器。*

这与你在 Zorin OS 中看到的非常相似，只不过 Zorin OS 你可以付费激活另外四种布局。Tromjaro 不提供这个选项。当然，它是 Xfce，所以你可以尽情定制。

Tromjaro 另一个使其脱颖而出的方面是它包含的预装软件数量庞大。考虑到 ISO 镜像的大小接近 6 GB，这一点应该很明显。打开 Xfce 桌面菜单（**图 2**），你会发现开发者确实非常认真地囊括了所有可能的功能。

![](https://cdn.thenewstack.io/media/2026/03/2b5c5f5a-tromjaromenu.jpg)

***图 2：** Tromjaro Xfce 桌面菜单显示了大量预装应用程序。*

此外，如果你打开“设置”应用，你会看到比你所需更多的选项。

在“设置”应用中，你会找到一个标有“驱动程序、内核、语言、时间、日期、用户、账户、键盘布局”的选项。这就是 Manjaro 设置管理器，其中一个最重要的工具是内核管理器（**图 3**），你可以在其中从当前内核切换到列表中包含 Linux 6.19.2-1 到 5.10.250-1 的任何内核。

![](https://cdn.thenewstack.io/media/2026/03/b1158ab9-tromjarokernel.jpg)

***图 3：** Linux 内核管理器是那些喜欢确保拥有最新内核的人的重要工具。*

开箱即用时，Tromjaro 搭载的是 6.12.73-1 内核。我决定测试内核管理器并安装 6.19.2-1，看看效果如何。

新内核安装完成后，我重启了系统，果然，6.19 内核已激活。

说到安装软件，Tromjaro 包含了 pacman 的图形用户界面前端 Pamac（**图 4**）。这是一个重要的补充，因为如果你是 Linux 新手，你不会想深入终端去安装应用程序。

![](https://cdn.thenewstack.io/media/2026/03/32d1a1ed-tromjaropamac.jpg)

***图 4：** 这个 GUI 让安装软件变得容易得多。*

## Tromjaro 适合谁？

即使有了 Pamac GUI，我愿意向任何用户推荐 Tromjaro 吗？不。请记住，Tromjaro 基于 Manjaro，而 Manjaro 又基于 Arch，Arch 并非最用户友好的发行版。

大多数人同意这种观点的原因有两方面。首先是 Arch Linux 的滚动发布特性，许多人认为滚动发布发行版不如标准发布稳定。在我处理 Linux 的这些年里，我从未发现滚动发布发行版不稳定。第二个原因是 *pacman* 包管理器。尽管我发现 *pacman* 并不比 apt 或 dnf 更有挑战性，但新用户绝不应该被推荐使用需要命令行操作的 Linux 发行版。

然而，Tromjaro 通过包含 Pamac 避免了这个问题。

即使有了 Pamac GUI，我也不会向任何 Linux 新手推荐这个发行版。很大一部分原因是它使用了 Xfce 桌面。尽管 Xfce 桌面并不难操作，但它为新用户提供了太多自定义选项。如果你从未接触过 Linux，并且深入 Xfce 设置管理器（**图 5**），你会发现大量可配置的选项。

![](https://cdn.thenewstack.io/media/2026/03/34bccf43-tromjaroxfcesettings.jpg)

***图 5：** Xfce 设置应用对新用户来说可能有点令人应接不暇。*

我一点也不反对 Xfce，但考虑到你可以进行大量的定制，对于一个不知道自己在做什么的人来说，“破坏”桌面并非难事。仅此一点，我通常不向 Linux 新手推荐 Xfce。

如果你至少具备中等水平的 Linux 技能，Tromjaro 是一个很棒的 Linux 发行版，可以很好地为你服务。无论你只是一个网页浏览者、内容创作者还是开发者，Tromjaro 都会是你的下一个桌面发行版的一个绝佳选择。

从官方网站 [下载 Tromjaro 的 ISO](https://www.tromjaro.com/download/) 并安装，看看这个 Linux 版本表现如何。