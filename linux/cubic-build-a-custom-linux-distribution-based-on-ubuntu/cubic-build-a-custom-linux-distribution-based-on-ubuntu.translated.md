# Cubic：构建基于 Ubuntu 的自定义 Linux 发行版

![Cubic：构建基于 Ubuntu 的自定义 Linux 发行版的特色图片](https://cdn.thenewstack.io/media/2025/03/b72ba278-karographix-photography-f7rp5ed74be-unsplash-cubic-1024x668.jpg)

您是否曾经想构建自己的自定义 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)? 您可能需要一个包含特定应用程序、文件和自定义设置的特定发行版，这样您就可以将其安装在您的企业或家庭网络中的任意数量的机器上。

这听起来可能是一项具有挑战性的任务，但 Ubuntu（和[基于 Ubuntu 的发行版](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/)）有一个 GUI 工具，可以使这项任务变得更加容易。

该应用程序称为 [Cubic](https://github.com/PJ-Singh-001/Cubic)。

Cubic 可以轻松地浏览 ISO 自定义步骤（借助 GUI 和集成的虚拟命令行环境）来自定义 Linux 文件系统。使用 Cubic，您可以创建新的发行版或自定义现有的发行版。

Cubic 可用于 Ubuntu 18.04.5 及更高版本或 Debian 11 Bullseye 及更高版本。使用 Cubic，您可以自定义以下实时 ISO 镜像：

- 来自 14.04 及更高版本的所有 Ubuntu 版本。
- 大多数基于 Ubuntu 的发行版。
- 许多 Debian 版本（在 Debian 11 Bullseye 及更高版本上测试过）。
- 许多基于 Debian 的发行版。

如何使用 Cubic？让我来向您展示。

## 您需要什么

为了使此方法有效，您需要一个正在运行的基于 Ubuntu 的发行版实例、充足的本地存储（或连接的 USB 驱动器）以及具有 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)的用户。您还需要下载要自定义的发行版的 ISO 镜像。请注意，某些发行版与 Cubic 的兼容性不佳。在我的测试中，我从 [elementaryOS 镜像](https://thenewstack.io/elementary-os-a-linux-distro-easy-to-use-and-easy-on-the-eyes/) 和 Debian 创建了 ISO。最终结果是 elementaryOS 的 ISO 镜像无法启动，而基于 Debian 的镜像可以正常工作，因此您的结果可能会有所不同。

就是这样。让我们开始工作吧。

## 安装 Cubic

您要做的第一件事是安装 Cubic。为此，请登录到您的基于 Ubuntu 的发行版，打开一个终端应用程序，然后首先使用以下命令添加必要的存储库：

```
sudo apt-add-repository ppa:cubic-wizard/release
```

使用以下命令更新 apt：

```
sudo apt-get update
```

最后，使用以下命令安装 Cubic：

```
sudo apt-get install --no-install-recommends cubic -y
```

安装该应用程序后，您可以从桌面菜单中打开它。

## 使用 Cubic

首次打开 Cubic 时，您需要通过单击下拉列表右侧的小文件夹图标来选择一个项目目录（**图 1**）。

![Cubic 启动页面。](https://cdn.thenewstack.io/media/2025/03/826d7394-cubic1.jpg)

图 1：Cubic 主窗口设计精良且易于使用。

选择项目目录后，单击“下一步”。

在结果窗口（**图 2**）中，您必须首先选择要使用的原始 ISO 镜像。单击与“文件名”关联的文件夹图标，然后找到您下载的 ISO。这将自动填写大部分其他信息。如果某些内容无法自动填写，则您无法手动填写，因此它将保持空白。

![Cubic 屏幕截图。](https://cdn.thenewstack.io/media/2025/03/38377506-cubic2.jpg)

图 2：选择 ISO 后，所有内容都应自动填充。

单击“下一步”。

然后，Cubic 将分析磁盘镜像，将文件从原始镜像复制到项目文件夹，并提取未压缩的 Linux 文件系统。完成后，单击“自定义”，这将使您进入基于终端的虚拟环境（**图 3**）。

![Cubic 屏幕截图。](https://cdn.thenewstack.io/media/2025/03/51e1bde3-cubic3.jpg)

图 3：Cubic 虚拟环境是您自定义发行版的地方。

您现在可以使用您将用于自定义的命令行。是的，这意味着您需要使用命令行。您可以使用 apt 或 flatpak 包管理器来安装（或删除）发行版所需的任何内容。例如，您可能想要安装 LibreOffice、GIMP、Slack、Snapd 以及您需要的任何应用程序，如下所示：

```
apt-get install libreoffice gimp snapd
```

您不能做的一件事是使用 [Flatpak](https://thenewstack.io/linux-an-intro-to-the-flatpak-universal-package-manager/) 或 [Snap](https://thenewstack.io/an-introduction-to-the-snap-universal-package-manager/) 安装应用程序，因为它们无法连接到系统总线。
您甚至可以更换内核，例如，更换为实时或 HWE 内核，以获得更好的硬件识别和更少的延迟，或者启用 zRAM 以获得更好的性能。

也许您想使用以下命令为 ISO 创建特定用户：

```
adduser USERNAME
```

其中 USERNAME 是要添加的用户的名称。
从虚拟终端可以执行的任务令人印象深刻。您可以在[官方 Cubic Terminal Page Wiki](https://github.com/PJ-Singh-001/Cubic/wiki/Terminal-Page)上阅读更多相关信息。

完成自定义后，单击“下一步”。虚拟环境将关闭，然后 Cubic 将进入一个页面，您可以在该页面上删除任何应用程序以缩小其创建的 ISO 的大小。您可以浏览列表（**图 4**）并选择您不需要的任何应用程序。

![Screenshot.](https://cdn.thenewstack.io/media/2025/03/59b5c7d7-cubic4.jpg)

图 4：Cubic 应用程序删除页面。

确保不要选择系统运行所依赖的任何内容。为此，您只想删除面向用户的应用程序。

完成该操作后，单击“下一步”。在出现的窗口（**图 5**）中，您可以选择要使用的内核。

![Screenshot.](https://cdn.thenewstack.io/media/2025/03/9bcbd50f-cubic5.jpg)

图 5：我建议您在此处坚持使用默认设置。

单击“下一步”，然后在出现的窗口（**图 6**）中，选择您的压缩级别，然后单击“生成”。

![Screenshot.](https://cdn.thenewstack.io/media/2025/03/17f5136f-cubic6.jpg)

图 6：如果您想要更小的 ISO 镜像，请使用 zstd 或 xz 压缩。

现在…我们等待。此过程可能需要一些时间（具体取决于原始 ISO 和您所做的自定义）。生成完成后，单击“完成”。

生成完成后，您将收到摘要，然后可以单击“关闭”。您新的自定义 ISO 镜像将在您在过程开始时选择的项目目录中找到。您可以将该镜像刻录到 USB 驱动器或与其他人共享，然后他们可以随意安装该发行版。

朋友们，这就是您如何创建基于 Ubuntu 或 Debian 的自定义 Linux 发行版的方法。尽情享受这个很棒的工具吧。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)