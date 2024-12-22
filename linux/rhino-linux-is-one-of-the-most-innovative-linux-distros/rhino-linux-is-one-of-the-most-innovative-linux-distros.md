
<!--
title: Rhino Linux是极具创新性的Linux发行版之一
cover: https://cdn.thenewstack.io/media/2024/12/3e57223b-rhinolinuxhero.jpeg
-->

Rhino Linux 是一款华丽的桌面系统，它既能满足新用户的需求，也能满足经验丰富的 Linux 用户的需求，同时也能满足任何希望使用开源桌面进行开发的用户。

> 译自 [Rhino Linux Is One of the Most Innovative Linux Distros](https://thenewstack.io/rhino-linux-is-one-of-the-most-innovative-linux-distros/)，作者 Jack Wallen。

我使用和评测[Linux发行版](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/)已有数十年。我[尝试过所有](https://thenewstack.io/syslinuxos-a-linux-distro-for-system-administrators/)发行版，从[最精简的](https://thenewstack.io/truenas-a-linux-distro-for-low-cost-network-attached-storage/)到功能比大多数用户所需[更丰富的](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)发行版。我评测过一些桌面Linux发行版，它们显然更注重效率而不是美观，也使用过一些更注重外观而不是功能的发行版。

然后，还有一些在可用性和外观上都同样出色的发行版。Rhino Linux就是这样一个发行版。

[Rhino Linux](https://rhinolinux.org)是对Ubuntu的重新设计，但这不仅仅是重新设计Ubuntu桌面。Rhino Linux是一个滚动发布发行版，这意味着它始终是最新的，您无需担心新版本发布后需要安装。只需安装一次Rhino Linux，只要您持续更新，它将始终包含最新的软件和安全补丁。

Rhino Linux还添加了一些其他技巧，使其成为一个引人入胜的桌面发行版。例如，您会发现桌面上有一个方便的搜索栏。点击垂直面板上的“U”，就会出现一个搜索栏。Ulauncher可以用作应用程序启动器、在线搜索工具和目录浏览器。

让我向您展示一些Ulauncher的工作示例。

- 打开搜索栏，输入`~`，然后您可以导航到用户主目录中的目录以查看文件。点击文件即可打开它。
- 输入`g`后跟一个空格来运行Google搜索。输入`so`后跟一个空格来在Stack Overflow上运行搜索。输入`wiki`后跟一个空格来搜索维基百科。
- 输入应用程序的名称，一旦条目出现，点击即可启动它。

Ulauncher是一个强大的搜索工具，可以使查找所需内容变得更加容易。您还可以添加新的搜索快捷方式。例如，假设您想添加DuckDuckGo搜索引擎。打开Ulauncher首选项（图1），转到快捷方式，点击添加快捷方式，并按如下方式配置：

- 名称 – DuckDuckGo
- 关键词 – `ddg`
- 查询或脚本 – `https://duckduckgo.com/%s`

![](https://cdn.thenewstack.io/media/2024/12/b2bc9e01-ulauncher.jpeg)

*图1：您可以根据需要添加任意数量的快捷方式。*

点击保存，然后使用键盘组合Ctrl+Space打开Ulauncher。在搜索栏中，输入`ddg`后跟一个空格和您的搜索字符串。按键盘上的Enter键，您的默认浏览器将打开并显示搜索结果。

说到快速访问，如果您查看Rhino Linux桌面的顶部，您会看到一行文件夹位置（文件、文档、音乐、图片、视频）。如果您点击任何这些条目，则该目录中包含的文件将显示出来。点击一个条目即可打开相应的文件。

Rhino Linux桌面是Xfce，但它配置了独特的（且美观的）布局。当然，由于这是Xfce，您可以进行无限的调整。这种定制的桌面体验称为Unicorn，它与传统的Xfce桌面一样快，但外观更现代。

但是Rhino Linux不仅仅是漂亮的外观。这个开源操作系统还包括与Pacstall一起使用的AUR（Arch用户存储库），Pacstall是Ubuntu上使用的命令行，因此它可以使用那些原本不可用的存储库。

Pacstall的工作方式与官方的Arch包管理器pacman非常相似。例如，如果您想从AUR安装VS Codium（VS Code的开源版本）。可以使用以下命令：

```bash
pacstall -I vscodium-deb
```

您可以使用以下命令查看AUR中是否有可用的应用程序：

```bash
pacstall -S vscodium
```

上述命令将列出所有可用的安装选项。

需要注意的是，第一次登录时，您会看到一个设置向导，允许您添加对Flatpak、Nix、Snap和AppImage的支持。我建议您至少启用这些通用包管理器中的一个，方法是将On/Off滑块点击到On位置，然后点击下一步（图2）。

![](https://cdn.thenewstack.io/media/2024/12/6f8ad6e1-rhinosetup.jpeg)

*图2：在Rhino Linux中启用通用包管理器。*

启用Flatpak后，您还可以启用Flatpak Beta Channel以及Flatseal（用于管理Flatpak权限）。

之后，您可以启用各种容器技术（图3），例如Docker、Podman、Distrobox、Apptainer、QEUM和VirtualBox。

![](https://cdn.thenewstack.io/media/2024/12/08c58845-rhinosetup2.jpeg)

*图3：向Rhino Linux添加容器支持。*

最终屏幕允许您启用Nala、GitHub CLI、Apport和Redshit。完成此操作后，单击“下一步”，输入您的用户密码（出现提示时），所有操作都将完成。

我必须说，升级后我遇到一个问题，最终不得不重新安装操作系统。即使经过几分钟的故障排除，我也无法弄清楚发生了什么。没关系，因为Rhino Linux的安装非常简单。只需点击几下，安装就开始了。完成后，我重新登录并重新开始。这是通过虚拟机进行测试的优点之一。我本可以在升级之前创建快照，但我习惯了Linux升级不会出现问题。

尽管出现了一个小问题（在第二次安装中我没有遇到），但我发现Rhino Linux是一个令人着迷且优秀的Linux发行版，几乎任何用户都会喜欢。

如果这个Linux发行版听起来很适合您，我建议您立即下载ISO并安装它。相信我，您不会后悔这个决定的。Rhino Linux是一个华丽的桌面，既能满足新用户，也能满足拥有大量Linux技能的用户，以及任何希望使用开源桌面进行开发的用户。
