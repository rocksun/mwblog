在即将发布的Steam Machine的推动下，[Linux](https://thenewstack.io/learning-linux-start-here/)上的游戏体验最近得到了巨大提升。Steam Machine是一款由Arch Linux驱动的[紧凑型游戏机](https://www.pcgamer.com/hardware/gaming-pcs/steam-machine-specs-availability/)。

然而，这并不意味着你必须等待新设备发布。为什么？因为已经有几款专为游戏而设计的Linux发行版。其中一个发行版叫做[Bazzite](https://bazzite.gg/)。

根据官方宣传材料，“Bazzite让桌面PC、掌机、平板电脑和家庭影院PC上的游戏和日常使用更加流畅和简单。”

你的第一个问题可能是，“Bazzite有什么不同之处？”这份列表可能不长，但其结果却非常显著。Bazzite在标准Linux发行版的基础上增加了以下内容：

*   预装Steam、Proton、Proton+、Lutris和Protontricks。
*   HDR和VRR支持。
*   改进的CPU调度器。
*   多个社区开发的工具和定制功能，以简化游戏体验。
*   支持多种游戏控制器（Xbox、Wii、Switch、PS3/4/5等）。
*   AMD和Intel的最新NVIDIA和Mesa驱动程序。
*   支持额外的Wi-Fi和显示硬件。
*   Waydroid用于Android应用支持。
*   包含Homebrew。

你可以在[这里](https://docs.bazzite.gg/Gaming/Hardware_compatibility_for_gaming/)查看完整的游戏硬件兼容性列表。

Bazzite不仅适用于台式机和笔记本电脑，还适用于掌机和平板电脑。由于你将使用Steam，因此可以访问你的整个Steam库。

Bazzite也是一个基于镜像的操作系统，这意味着如果更新导致问题，你可以轻松回滚到之前正常工作的镜像。而且，由于Bazzite是一个不可变发行版，它也高度安全。整个核心系统以只读模式挂载，因此这些文件无法被修改。

Bazzite基于Fedora Kinoite构建，并使用KDE Plasma或GNOME桌面环境。

所有这些结合在一起，创建了一个几乎可以运行任何东西的Linux发行版。

我安装了[GNOME](https://thenewstack.io/what-makes-gnome-so-appealing/)版本的Bazzite，看看它的实际表现。

## 在Linux上玩游戏

既然Bazzite被宣传为游戏发行版，我想我应该做的第一件事就是看看它在Steam游戏上的表现。我打开了应用程序（无需安装任何东西），登录了我的账户，并启动了我库中的一款游戏。

我以前也做过这些操作，发现一些Linux发行版的结果好坏参半。然而，Steam与Bazzite无缝协作，这让我一点也不惊讶。几分钟内，Albion Online就运行起来了。它不是地球上最受欢迎的游戏，但它是我倾向于用来测试Linux上Steam的游戏。

像往常一样，下载游戏并开始玩需要一些时间。总的来说，大约五分钟后我就开始测试游戏了（图1）。

[![游戏截图。](https://cdn.thenewstack.io/media/2025/11/e1a86c37-albion.jpg)](https://cdn.thenewstack.io/media/2025/11/e1a86c37-albion.jpg)

图1：使用Steam在Bazzite上玩游戏大大简化。

我一直明白的一件事是，在PC上使用Steam并不像使用专用游戏机那么容易。游戏必须下载，必须预留空间等等。但是一旦你在Bazzite上开始玩游戏，它的运行效果就和在游戏机上一样好。事实上，我从未在Linux上体验过如此无缝的游戏体验。它运行得非常好。

画面出色，声音很棒，游戏流畅。当然，游戏运行得好不好取决于游戏本身和硬件。当然，加载时间可能会慢，但玩起来很稳定。

你还可以使用Lutris作为在Bazzite上玩游戏的更简单途径。Lutris的一个注意事项是，你必须下载GOG文件才能安装这些游戏，而且许多GOG文件都有相应的价格。但是，嘿，在这个世界上，付费玩游戏是常态。

## 超越游戏

是的，Bazzite可能以游戏为导向，但这并不意味着它不能用于其他目的。虽然该发行版没有附带太多生产力工具，但它使用了[Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)和Bazaar应用商店，这意味着你可以安装大量应用程序。只需点击几下，你就可以安装所需的任何东西（例如办公套件、IDE、浏览器以及介于两者之间的所有内容——图2）。

[![截图](https://cdn.thenewstack.io/media/2025/11/c1068130-bazzitebazaar.jpg)](https://cdn.thenewstack.io/media/2025/11/c1068130-bazzitebazaar.jpg)

图2：Bazaar应用商店非常易于使用。

我发现Bazzite对于生产力和创造力来说都是一个坚如磐石的发行版。

然后是Btrfs助手（图3），你可以在其中管理Btrfs快照，如果发生问题，这些快照可以用于回滚。

[![截图](https://cdn.thenewstack.io/media/2025/11/cac56082-bazzitebtrfs.jpg)](https://cdn.thenewstack.io/media/2025/11/cac56082-bazzitebtrfs.jpg)

图3：这个工具应该被认为是必用的。

Btrfs助手确实需要一点学习曲线，但一旦你掌握了窍门，你就能像专业人士一样快速创建和管理快照。

## 用于容器化发行版的Distroshelf

Bazzite中包含的另一个出色应用程序是Distroshelf，它允许你以与GNOME Boxes相同的方式快速启动Linux发行版的[容器化](https://thenewstack.io/containers/)版本。你所要做的就是下载一个基础镜像，然后让Distroshelf安装它（图4）。启动虚拟机确实需要一些时间，但这仅仅是因为所需文件下载量很大。除此之外，它使用起来非常简单。

[![截图](https://cdn.thenewstack.io/media/2025/11/e2e79e23-distroshelf.jpg)](https://cdn.thenewstack.io/media/2025/11/e2e79e23-distroshelf.jpg)

图4：Distroshelf是在Bazzite中运行虚拟机的好方法。

总而言之，我发现Bazzite是一个非常稳定且有趣的发行版。我建议你[下载ISO](https://bazzite.gg/#)并在虚拟机或备用系统上运行它。我完全相信你会像我一样享受这种体验。