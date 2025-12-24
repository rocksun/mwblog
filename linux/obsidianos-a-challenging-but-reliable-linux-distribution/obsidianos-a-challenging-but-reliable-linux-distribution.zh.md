在我们深入了解 ObsidianOS 之前，让我们先谈谈 A/B 分区。它对 ObsidianOS 的一切都至关重要。

## 什么是 A/B 分区？

A/B 分区是一种实现无缝软件更新的方法。本质上，它能确保你始终拥有一个可工作的系统，尽管这个发行版不是不可变的。

以下是 A/B 分区的工作原理：

你的设备有两个“插槽”——我们称之为 A 和 B。

当你在运行插槽 A 时，插槽 B 在后台接收新的更新（这样你就不会受到干扰）。

当更新完成时，你重启并选择使用插槽 B。你登录到插槽 B，然后整个过程再次发生，只是这次后台更新会发送到插槽 A。

这种更新过程始终确保你不会遇到桌上或膝盖上的设备变砖的情况。你将始终有一个可启动的工作分区，这意味着你可以放心你的电脑将始终正常工作。

在标准的 [Linux 文件系统](https://thenewstack.io/8-linux-desktop-distributions-to-try/) 上使用 A/B 分区有点罕见。这种系统最常使用 [Btrfs](https://btrfs.readthedocs.io/en/latest/) 写时复制文件系统，因为它允许简单的回滚。在一个具有更可靠文件系统的系统上实现 A/B 分区是一个巨大的胜利。

话虽如此，让我们来了解更多关于 ObsidianOS 的信息。

## ObsidianOS 是怎样的

首先，你可以下载一个包含极简桌面、KDE Plasma 或 COSMIC 的 ISO。我决定选择 KDE Plasma 版本，看看开发者对其做了什么。

在测试时，我通常会为相关的操作系统使用 [VirtualBox 虚拟机](https://thenewstack.io/linux-how-to-run-virtualbox-vms-from-the-command-line/)。为了让 ObsidianOS 启动，我必须在“设置”窗口中启用 UEFI。解决这个问题后，我登录到 Live 桌面（用户名 user，空密码），并开始了安装过程。

安装程序有点不稳定，有些文本无法读取（这导致我不得不猜测几次），然后它崩溃了。我第二次运行安装程序。再次，安装失败了，所以我重启了虚拟机，再试一次。

第三次也没有成功，所以我选择了最小化选项，它使用基于文本的安装程序（图 1）。

![](https://cdn.thenewstack.io/media/2025/12/5fc58e22-obsidian1.jpg)

图 1：使用 ObsidianOS 基于文本的安装程序。

结果发现，我在使用 GUI 时回答了一个错误的问题（因为弹出窗口不可读）。当提示“将插槽‘a’卸载到插槽‘b’”时，接受默认的 N 而不是 Y。这样做，安装就会顺利进行。

然而，如果你选择这条路线，你最终会得到一个纯文本的系统。最重要的是，安装没有给你创建新用户的选项。

[Linux 发行版](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/) 的安装不应该这么难。永远不应该。

然后我不得不安装 sudo 和 nano。首先，我以用户 root 身份（无密码）登录到基于控制台的系统。使用以下命令创建新用户：

```
useradd -m USERNAME
```

其中 USERNAME 是你要添加的用户。

使用以下命令为该用户设置密码：

```
passwd USER
```

然后，我运行：

```
pacman -S sudo nano
```

使用以下命令打开 sudoers 文件：

```
EDITOR=nano visudo
```

在该文件中，添加以下内容：

```
USERNAME ALL=(ALL) ALL
```

其中 USERNAME 是你之前添加的用户名。

保存并关闭文件。

使用以下命令更新所有内容：

```
pacman -Syu
```

我没有安装 KDE Plasma，而是选择了 GNOME，因为它安装起来更简单。可以通过以下命令完成：

```
pacman -S xorg
```

接下来，安装 GNOME：

```
pacman -S gnome
```

完成后，使用以下命令启用登录管理器：

```
sudo systemctl enable --now gdm.service
```

当登录窗口出现时，输入你的用户名和密码，GNOME 就可以使用了（图 2）。

![Screenshot.](https://cdn.thenewstack.io/media/2025/12/39825f1c-obsidian2.jpg)

图 2：终于，我有了桌面。

一旦进入桌面，你就可以使用 pacman 或 [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) 安装应用程序。

## ObsidianOS 控制中心

还记得我提到的 A/B 分区吗？这就是有趣的地方。从应用程序概览中打开 ObsidianOS 控制中心。在“插槽”选项卡（图 3）中，你可以切换当前的活动插槽，或者在下次启动时切换一次。一旦你切换了插槽，它将在下次启动时生效。

![screenshot](https://cdn.thenewstack.io/media/2025/12/4fc8fecf-obsidian3.jpg)

图 3：使用便捷的 GUI 管理 A/B 分区。

但是，在此之前，你应该下载一个更新。为此，点击“系统更新”选项卡，然后点击“下载更新”（图 4）。

![Ssccreenshot.](https://cdn.thenewstack.io/media/2025/12/f10da50c-obsidianupdates.jpg)

图 4：请务必为下载选择插槽 a 或 b。如果你正在使用插槽 a，请将更新下载到目标插槽 b。

完成更新后，回到“插槽”选项卡进行切换。

## ObsidianOS 适合谁？

这是一个棘手的问题，但我认为答案是：ObsidianOS 适合那些想要一个始终能正常工作的操作系统的用户。但这也就意味着 ObsidianOS 最适合那些拥有丰富 Linux 经验的用户。

如果你是 Linux 新手，并且选择 ObsidianOS 作为你的第一个发行版，你将会发现自己陷入一片混乱。

然而，对于那些拥有丰富 Linux 技能的人来说，ObsidianOS 绝对是一种享受。

如果你对此感兴趣，请 [下载 ObsidianOS 的 ISO](https://files.obsidianos.xyz/)，然后将其作为虚拟机或在备用电脑上试用。