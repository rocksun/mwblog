# 海蓝Linux：人人皆宜的便捷美观Fedora发行版

![特色图片：海蓝Linux：人人皆宜的便捷美观Fedora发行版](https://cdn.thenewstack.io/media/2025/02/a7303a4a-ultramarinedocky-1024x614.jpg)

我经常说，一个漂亮的桌面环境可以成就或毁掉一个[发行版](https://thenewstack.io/choosing-a-linux-distribution/)。当然，很多人不在乎他们的桌面是什么样子，只要性能好，能提高工作效率就行。

我每天要盯着桌面好几个小时，与其看到乏味的东西，不如看到赏心悦目的东西。幸运的是，有很多Linux桌面环境在优雅方面都能胜过macOS和Windows。

但是，要使Linux发行版真正有用，它也必须易于使用。在数百个可用的发行版中，有一些是我认为适合Linux新手使用的[优秀发行版](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/)。很长一段时间以来，我一直拒绝将[Fedora](https://thenewstack.io/fedora-centos-consistency-transparency-open-source/)添加到该列表中。然而，在过去的几年里，出现了一些（官方和非官方的）衍生版本，将Fedora的用户友好性提升到了新的高度。

其中一个发行版叫做[海蓝Linux](https://ultramarine-linux.org/)。这个基于Fedora的操作系统旨在为Linux新手提供易于使用的体验，同时也提供更高级的功能，以吸引高级用户离开他们当前的桌面。

海蓝Linux在几个方面与标准Fedora不同：

- 它包含一些对桌面的调整和定制，以增强用户体验。
- 添加了存储库以扩展软件数量。
- 自动安装第三方存储库。
- 打磨了流行桌面环境的版本。
- 添加了性能增强功能，例如System76 CPU调度器。
- 自定义壁纸和桌面布局。
- 可选择多个桌面环境（KDE Plasma、GNOME、Budgie等）。
- 添加了工具，例如[Starship提示符](https://starship.rs/)和Pop Launcher。

虽然你不会找到大量的预安装应用程序，但你会得到LibreOffice、Firefox和Rhythmbox等应用程序。由于增加了存储库和在应用商店中内置了[Flatpak支持](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)，因此可以通过GUI安装大量的应用程序。

海蓝是我接触Starship提示符的发行版，我非常喜欢它。如果您不熟悉Starship，它是一个用Rust编写的提示符，具有跨shell兼容性、改进的速度和性能、最小的（但可定制的）设计、丰富的显示信息、动态语法检查等功能以及简单的配置。我喜欢Starship提示符的一点是它有一个非常简洁的界面，任何人都可以使用（图1）。

- 图1：默认的Starship提示符简洁明了。

## 海蓝Linux适合谁？

重要的是要记住，海蓝基于Fedora，这是一个非常适合高级用户的发行版，部分原因是它被认为是一个“前沿发行版”，也因为其频繁的更新和以开发者为中心的关注点。

虽然海蓝仍然保留了这些方面，但它的主要关注点是易用性，并且开发人员为此付出了巨大的努力。如何做到这一点？考虑以下几点：

- 它包含您需要的基本软件以及轻松安装更多软件的方法。
- 包含所有您需要的多媒体编解码器。
- 提供一系列用户友好的桌面环境供您选择。
- 包含flatpak支持。
- 使用实用的默认设置，因此您无需花费太多时间（如果有的话）来调整桌面。
- 更新简单。

这是海蓝Linux最好的方面之一……它适合任何人。如果您以前从未体验过Linux，海蓝是一个不错的起点（只需确保您选择一个用户友好的桌面版本，例如KDE Plasma或Budgie）。如果您已经使用过一些Linux，并且想了解更多，海蓝是一个绝佳的选择，因为它可以让您快速上手，并且不会阻止您使用更高级的功能（例如SELinux）。如果您是高级用户或开发者，海蓝仍然是Fedora，这使其成为一个很棒的开发平台或管理员操作系统。

## Budgie 体验
我选择使用 Budgie 桌面版本的 Ultramarine，部分原因是我非常喜欢它，而且它非常容易定制。Ultramarine 对 Budgie 的诠释非常漂亮，但对我来说太暗了，而且很典型。但这没问题。| 大约两分钟后，我把底部面板改成了 Dock，关闭了暗模式，并移除了桌面图标。这就足够让桌面更符合我的口味了。

-

图 2：稍微调整一下，Budgie 就更符合我的口味了。

我一直是 Budgie 的粉丝，Ultramarine 的版本也没有让我失望。我唯一的问题是无法更改窗口标题栏的主题。鉴于我不喜欢暗色主题，我希望能够在不编辑 CSS 文件的情况下更改它，这不推荐给新用户。还有其他方法可以实现这一点，但没有一个是简单的。为了获得更轻松的主题体验，我建议使用官方的[Ubuntu Budgie 发行版](https://ubuntubudgie.org/blog/)。

## 性能

如果你曾经使用过 Fedora Linux，那么你就会知道它的性能有多好。在过去五年左右的时间里，Fedora 的性能已经赶上了大多数主要的 Linux 发行版，甚至可以与一些轻量级发行版媲美。

应用程序安装和打开速度很快，动画和滚动流畅如丝，感觉非常稳定。

但是，我在 Ultramarine 中遇到一个问题。当我打开 Software 应用时，它通知我最新版本 (41) 可用。根据 Ultramarine 官方网站，最新版本是 40。当我尝试运行升级时，每次都会失败。它表现得好像正在下载更新，下载到大约 26% 时就崩溃了。

我不知道这是否是异常情况，但它也阻止了常规应用程序的更新。我已经多次安装 Ultramarine，从未遇到过这个问题，所以我猜这要么是偶然事件，要么是升级服务器的问题。无论如何，我将继续尝试升级（通过 GUI 和终端），并希望它最终能够成功。

除此之外的一个小故障，Ultramarine 使用起来绝对是一种享受，我想各种类型的用户都会发现这个发行版是从 macOS 或 Windows 迁移过来的一个不错的选择。

如果你对此感兴趣，[下载 Ultramarine Linux 的 ISO 镜像](https://ultramarine-linux.org/download/)，并将其安装为虚拟机或安装在备用桌面上试用一下。你不会后悔的。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。