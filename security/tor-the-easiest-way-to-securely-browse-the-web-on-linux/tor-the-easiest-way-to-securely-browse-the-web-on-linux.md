<!--
title: Tor：Linux 匿名上网终极指南，简单到飞起！
cover: https://cdn.thenewstack.io/media/2025/09/aa454b96-tor.png
summary: 网络安全与隐私至关重要。Tor浏览器提供匿名浏览，Tor Launcher简化Linux安装和使用，实现自动连接及身份重置，保障用户数据安全。
-->

网络安全与隐私至关重要。Tor浏览器提供匿名浏览，Tor Launcher简化Linux安装和使用，实现自动连接及身份重置，保障用户数据安全。

> 译自：[Tor: The Easiest Way to Securely Browse the Web on Linux](https://thenewstack.io/tor-the-easiest-way-to-securely-browse-the-web-on-linux/)
> 
> 作者：Jack Wallen

除非你一直与世隔绝，否则安全和隐私是两个非常热门的话题。这有很好的理由：因为每个人似乎都在觊觎你的数据和/或信息。公司想为你建立指纹（以便他们能更好地创建定向广告），而不良分子则想获取任何可能帮助他们劫持你的身份或窃取你的银行账户信息的资料。

没人希望那样。

如今这种情况如此猖獗的部分原因是浏览器不安全。大多数[现代网络浏览器](https://thenewstack.io/the-cautionary-tale-of-the-browser-wars-and-why-business-transformations-often-fail/)可能会让你的生活变得更容易一些（尤其是在代理选项出现之后），但在此过程中，它们也降低了安全性。只有少数浏览器能在用户友好性和安全性之间取得完美平衡。例如，你可以使用Brave，它在这两个方面做得相当不错。然而，即便如此，你仍然可能面临隐私或安全问题。

除此之外，大多数其他浏览器远没有那么安全。

那么，当你在这信息高速公路上浏览时想要达到最高的安全性，你该怎么办呢（请原谅我这异想天开的标题转折）？

你转向Tor。

## 什么是Tor？

对于那些已经知道Tor是什么的人，可以随意跳到下一节。对于不熟悉这个浏览器的人，请继续阅读。

Tor是一个特殊的网络浏览器，它使用[Tor网络](https://www.torproject.org/about/history/)（也称为洋葱网络）。

什么？

Tor网络是一个由志愿者运营的开源全球覆盖网络，它确保匿名通信和在线隐私。Tor网络通过“洋葱路由”（因此得名）工作，它将数据多层加密，并在数据到达目的地之前，通过至少三个随机的转发器（又称节点）的电路发送。当数据到达一个节点时，它会解密数据的一层以识别路径中的下一个节点，在此过程中，它永远不知道原始IP地址或最终目的地是什么。通过这样做，你的数据是真正的匿名。

而数据包的匿名性应该成为目标。

你可能认为这听起来太复杂而无法使用，但实际上并非如此。我记得当我第一次开始使用Tor浏览器时，它比使用标准浏览器要复杂得多，也慢得多。如今，这个工具要容易和快速得多。

但这并不意味着你应该简单地安装基本的Tor浏览器然后直接使用。在[Linux](https://thenewstack.io/learning-linux-start-here/)上，有一种更简单的方法来解决这个问题，它被称为Tor Launcher。

## 什么是Tor Launcher？

Tor Launcher（或Tor Browser Launcher）是一个用户友好的工具，它使安装和使用Tor浏览器变得相当容易，这意味着你无需费力就能让你的数据匿名化或加密。使用Tor Launcher，你可以获得：

*   适用于你的语言和系统架构的最新版Tor浏览器。
*   Tor浏览器的自动更新。
*   Tor浏览器GnuPG签名的验证。
*   AppArmour配置文件，确保Tor遭受破坏的后果不会像可能的那样严重。
*   在你的桌面菜单中有一个Tor浏览器启动器。
*   当你打开Tor浏览器时，会有一个有趣的调制解调器声音（可选）。

你可能想知道为什么开发者包含了调制解调器声音。嗯，如果说Tor浏览器有什么是用户抱怨的，那就是速度。由于Tor浏览器的工作方式，它明显比其他浏览器慢。正因为如此，开发者添加了可选的调制解调器声音，作为对拨号上网时代的回归。

那真是有趣的时光。

任何时候我需要在Linux上安装Tor浏览器，我总是使用Tor Launcher，仅仅因为它让一切都变得更简单。

## 如何安装Tor Launcher

好消息是Tor Launcher有一个[Flatpak安装程序](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/)，因此任何使用Flatpak应用程序的发行版都可以使用它。由于大多数Linux发行版都支持Flatpak，你可以确定Tor Launcher的安装会很简单。

有多简单？我来给你演示。

你需要做的第一件事是确保你的发行版支持Flatpak。为此，打开你的发行版的软件中心并搜索Flatpak。如果你看到通用包管理器的条目，就安装它。如果你在发行版的应用商店中找不到它，你总是可以使用以下命令之一来安装它：

```
Debian-based distributions: sudo apt-get install flatpak -y
Fedora-based distributions: sudo dns install flatpak -y
Arch-based distributions: sudo pacman -S flatpak -y
```

安装完成后，重启你的系统，以便Flatpak全局可用。

安装好Flatpak后，现在是时候添加Tor Launcher了。

为此，输入命令：

```
flatpak install flathub org.torproject.torbrowser-launcher
```

如果安装后，你在桌面菜单中找不到Tor浏览器条目，你需要注销并重新登录，以便更改生效。

现在你已经安装了Tor Launcher，并准备好使用。

## 使用Tor Launcher

当你打开Tor Launcher时，它会自动打开Tor浏览器并建立与Tor网络的连接（图1）。通过这样做，你无需担心在打开Tor浏览器后还要记住连接到Tor网络。本质上，Tor Launcher为你完成了一切。

[![截图](https://cdn.thenewstack.io/media/2025/09/0d461f33-torlauncher.jpg)](https://cdn.thenewstack.io/media/2025/09/0d461f33-torlauncher.jpg)

*图1. Tor浏览器已打开并自动连接到Tor网络。*

在任何时候，你也可以在Tor浏览器中重置你的身份。本质上，这会关闭所有标签页和窗口，清除所有私人信息（如cookie和浏览历史记录），并为连接建立新的Tor电路。通过重置你的身份，你无需担心你的Tor会话会将之前会话的任何浏览活动与当前活动关联起来。

要重置你的身份，你只需点击地址栏右侧的小扫帚图标（图2）。

[![截图](https://cdn.thenewstack.io/media/2025/09/5135306a-torlauncher2.jpg)](https://cdn.thenewstack.io/media/2025/09/5135306a-torlauncher2.jpg)

*图2. 重置你的Tor浏览器身份。*

既然你已经掌握了如何在Linux上使用Tor Launcher运行Tor浏览器，你会发现体验要容易得多（但仍然很慢）。