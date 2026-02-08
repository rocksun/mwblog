自1997年以来，我一直在使用 [Linux](https://thenewstack.io/learning-linux-start-here/)。随着90年代接近尾声，涌现出如此多的 [新发行版](https://thenewstack.io/8-linux-desktop-distributions-to-try/)，令人眼花缭乱。

我记得我的一些最爱，其中之一就是Mandrake Linux。我记得在一次Linux大会上遇到Mandrake的开发者，觉得他们酷毙了。那些女士和先生们知道如何狂欢，我经常加入他们。

但Mandrake不仅仅是关于享受时光。Mandrake碰巧也是我记忆中首批出色地让Linux大众化的发行版之一；它易于使用、可靠且有趣。

正如生活之道，所有美好的事物都必将走向终结，Mandrake也 [销声匿迹](https://www.abortretry.fail/p/the-history-of-linux-mandrake)，再也无人提及。

但它真的消失了吗？

此后不久，一个基于Mandrake的新发行版诞生了。那个发行版就是Mandriva。

你猜怎么着？

Mandriva并没有持续太久。

好消息是，另一个发行版从废墟中诞生，并且至今仍在。我所说的发行版就是 [Mageia](https://www.mageia.org/en/)。

Mageia的口号是“为人们打造出色的工具”。

我已经有一段时间没有试用Mageia了，所以我非常兴奋能测试一下这个分支。

[![截图](https://cdn.thenewstack.io/media/2026/01/55eda0d9-mageiahero.jpg)](https://cdn.thenewstack.io/media/2026/01/55eda0d9-mageiahero.jpg)

## Mageia Live版本

像许多Linux版本一样，Mageia作为一个Live发行版发布，这意味着你可以从RAM启动并运行它。此外，你可以点击桌面上的“安装到硬盘”图标，并通过GUI安装程序进行操作。

Mageia的安装程序不像 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 那样简单。你需要回答比平时更多的问题。在某些情况下，这些提示有点误导。例如，你最终会被问是否要下载某个升级，但安装程序会警告你必须重启才能升级。不要那样做。只需让安装程序继续。安装完成后再重启。

安装时间比一般的Linux发行版稍长（大约10分钟左右），但完成后，你就可以重启并开始使用了。安装时间较长的原因之一是Mageia在安装时也会进行升级，这意味着你第一次登录时无需立即运行升级。

## 初次印象

正如我前面提到的，我有一段时间没有尝试Mageia了。我选择了 [KDE Plasma](https://thenewstack.io/linux-desktop-what-makes-kde-plasma-so-appealing/) 选项（还有GNOME和Xfce）。

当我第一次登录时，我知道会看到什么。毕竟，这是KDE Plasma，我非常熟悉。令我惊讶的一件事是默认主题。我已经习惯了发行版默认使用深色主题，但Mageia选择了较浅的配色，这正合我意。

接下来是欢迎应用，它向我承诺了更新、安装、配置等更多功能。我总是很高兴看到欢迎应用，因为我认为它们是Linux新手的必备品，而Mageia的欢迎应用和任何其他欢迎应用一样好用。

令我印象深刻的一点是“安装软件”选项卡，你可以在其中选择RPMDrake或Dnfdragora（图1）。Dnfdragora是基于之前的rpmdragora的前端，而rpmdragora最初是rpmdrake。

是的，这有点令人困惑。

[![截图](https://cdn.thenewstack.io/media/2026/01/f5c4718d-mageiawelcom.jpg)](https://cdn.thenewstack.io/media/2026/01/f5c4718d-mageiawelcom.jpg)

图1：不要让这种混淆把你弄糊涂。

事情是这样的。如果你点击RPMDrake，它会打开软件管理GUI，你可以在那里安装应用程序。如果你点击dnfdragor，它会安装dnfdragora，这是一个不同的软件管理GUI。我安装了这两个，看看它们有什么不同（图2）。

[![截图](https://cdn.thenewstack.io/media/2026/01/e9fb495a-softwaremanagement.jpg)](https://cdn.thenewstack.io/media/2026/01/e9fb495a-softwaremanagement.jpg)

图2：RPMDrake在左边。

在我看来，我发现RPMDrake是两者中更好的一个。区别很简单：rpmdrake主要用于基于Mandriva的系统，而dnfdragora专为Fedora和其他基于DNF的发行版设计。使用Mageia，你可以同时使用两者。

特别。

但等等，还有第三个选项。如果你点击“应用程序”（从欢迎应用），你可以快速安装一些常用应用（图3）。

[![截图。](https://cdn.thenewstack.io/media/2026/01/3ba9df31-mageiaapps.jpg)](https://cdn.thenewstack.io/media/2026/01/3ba9df31-mageiaapps.jpg)

图3：安装选项层出不穷。

## 预装应用

说到应用程序，你会得到常用的软件集合，例如LibreOffice、“K Suite”工具集（Kontact、Calendar、Kmail等）、Emacs、Firefox等。你还会在桌面菜单中找到“文档”部分，可以访问Live安装程序手册和Mageia控制中心手册。

说到这里……

Mageia控制中心（图4）是Mageia系统设置应用程序的一种扩展，面向管理员。你会发现硬件、网络、网络共享、锁定磁盘、安全、启动等选项。我将MCC比作openSUSE的YaST（即将被淘汰）。

[![截图。](https://cdn.thenewstack.io/media/2026/01/95ad55ef-mcc.jpg)](https://cdn.thenewstack.io/media/2026/01/95ad55ef-mcc.jpg)

图4：Mageia控制中心是高级用户的设置应用程序。

## 结论

Mageia是一个杰出的Linux发行版，它会让你想起你刚开始这段旅程时使用的Linux。然而，不要被迷惑；这是一个拥有所有现代功能和优点的现代发行版。

如果你正在寻找一个新的Linux发行版来尝试，我强烈建议你试用Mageia。将其部署为虚拟机（VM）进行测试，如果你喜欢它，可以将其安装在备用系统上。

从 [Mageia官方下载页面](https://www.mageia.org/en/downloads/) 下载ISO。