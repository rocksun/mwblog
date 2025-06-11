# 创建用于 Linux 安装的可引导 USB 驱动器

![用于 Linux 安装的可引导 USB 驱动器的特色图片](https://cdn.thenewstack.io/media/2025/06/40998da4-faruk-tokluoglu-fhiny0onkuu-unsplash-1024x683.jpg)

我几乎[每天](https://thenewstack.io/learn-linux-file-permissions-the-easy-way-and-the-hard-way-too/)都在谈论 [Linux](https://thenewstack.io/learning-linux-start-here/)，并且[已经谈论了几十年](https://thenewstack.io/beyond-ubuntu-other-linux-distributions-you-should-try/)。但是，当你沉浸在某件事中时，很容易忘记并非每个人都以相同的速度乘坐同一列火车。

例如，当我在[撰写评论](https://thenewstack.io/kde-neon-is-the-linux-distribution-with-the-dynamic-desktop/) [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)时，我理所当然地认为大家知道我说“将 ISO 刻录到闪存驱动器”是什么意思。

并非所有人都知道这意味着什么。

今天，我将纠正这一点。我将解释它的含义并向你展示它是如何完成的。

首先，这到底是什么意思？

## 刻录 ISO

很容易误解将 ISO 刻录到闪存驱动器的概念。 早在过去，当你将某些内容复制到外部介质时，通常涉及将音乐刻录到可写 CD。 ISO 镜像是一个光盘的精确数字副本。（“ISO”指的是 [ISO 9660](https://www.lenovo.com/us/en/glossary/iso-image/) 文件格式，有趣的是，它不是一个首字母缩写词，因为它源自希腊语单词“isos”（ίσος），意思是“相等”。）

刻录 ISO 不仅仅是将文件复制到闪存驱动器。 如果你将镜像直接复制到 USB 驱动器并尝试从中启动，则什么也不会发生。

这就是关键：你将 ISO 刻录到 USB 闪存驱动器，使其可启动。 当你刻录 ISO 镜像时，该过程会覆盖驱动器上的所有数据，并创建一个可启动的结构，其中包括结构化的文件系统和引导加载程序。 当你使用该 USB 驱动器启动计算机时，引导加载程序会接管并将你带到 Linux 的实时实例中。 此时，你可以尝试或安装它。

所以，是的，刻录 ISO 比复制文件要复杂得多。 幸运的是，它并不像你想象的那么难。

让我来向你展示。 我将解释如何从 Linux、macOS 和 Windows 中刻录 ISO。

## Linux

我最喜欢的刻录 ISO 镜像的工具是 [Popsicle](https://github.com/pop-os/popsicle)，它包含在 [Pop!_OS](https://thenewstack.io/pop_os-one-of-the-best-linux-distros-for-creators-of-all-types/) 中。 有很多用于刻录 ISO 的 GUI 应用程序，它们都非常用户友好。 但是，我将向你展示如何使用命令行来完成它。

Gasp！ 别担心，这并不难。

假设你已经下载了一个 ISO 镜像。 例如，你可以下载 [Ubuntu Budgie ISO](https://ubuntubudgie.org/downloads/)。 将该文件保存在内部存储（保存在 *~/Downloads* 中）后，打开一个终端窗口并导航到包含该文件的目录。

接下来，插入一个 USB 驱动器（确保它至少为 8GB，以确保安全）并确保它当前未挂载。 为此，使用以下命令找到驱动器的名称：

```bash
lsblk
```

假设你的驱动器的名称是 */dev/sdb*。 然后，你可以使用以下命令刻录镜像：

```bash
sudo dd if=/home/USER/Downloads/ubuntu-budgie-XXX.iso of=/dev/sdb bs=4M status=progress
```

上面的“XXX”应替换为相应的版本号。
按 Enter 键，该过程将开始。 完成后，你可以移除 USB 驱动器并使用它在任何需要的机器上安装 Linux。

## macOS 和 Windows

对于 macOS 和 Windows，我强烈建议使用 [balenaEtcher](https://www.balena.io/etcher) 工具来完成此过程。 此工具使刻录 ISO 镜像变得非常简单。

使用 balenaEtcher，你可以选择要刻录的 ISO，选择目标，然后“刷写”它（**图 1**）。

![screenshot](https://cdn.thenewstack.io/media/2025/05/f88dbd84-etcher.jpg)

图 1：balenaEtcher 工具使刻录 ISO 镜像变得非常容易。

刻录完成后，你可以关闭该应用程序，安全地移除 USB 驱动器并使用它在任何需要此开源操作系统的机器上安装 Linux。

## 其他选项

当然，还有很多其他选项可用于将 ISO 镜像刻录到闪存驱动器。 以下是可能的选项列表。

**适用于光盘（CD、DVD、蓝光）**——请注意，其中一些也支持刻录到 USB 闪存驱动器：
[ImgBurn](https://www.imgburn.com/): 使用此应用程序，您可以刻录 ISO、BIN 和 NRG 镜像。该应用程序适用于所有版本的 Windows。

[PowerISO](https://www.poweriso.com/): 另一款支持多种光盘格式甚至允许编辑 ISO 文件的应用程序。此应用程序的免费版本对 ISO 文件的大小有限制，因此如果要刻录更大的镜像，您可能需要购买付费版本。

[Active@ ISO Burner](https://www.lsoft.net/iso-burner/): 此应用程序还包括命令行自动化，并且仅适用于 Windows。

[Free ISO Burner](https://www.freeisoburner.com/): 一个简单的 UI，支持各种光盘，但应尽量避免使用它，因为它与您可能不需要的软件捆绑在一起。

[AnyBurn](https://www.anyburn.com/): 一个基本的 ISO 刻录机，适用于 Windows 7 及更高版本的所有版本。

[WinISO](https://winiso.com/): 此应用程序允许刻录、编辑和转换 ISO 文件。如果选择此方法，您需要使用付费版本，因为免费版本受到限制。

[InfraRecorder](http://infrarecorder.org/): 此应用程序是开源的、可移植的，并且可以处理基本的镜像刻录。

**适用于 USB 闪存驱动器**:

[Rufus](https://rufus.ie/): 用于刻录 ISO 镜像的更广泛使用的工具之一。

[AnyBurn](https://www.anyburn.com/): 也适用于 USB 驱动器。

[UNetbootin](https://unetbootin.github.io/): 最早的 ISO 刻录应用程序之一，它适用于 Linux、macOS 和 Windows

**内置工具**:

- 一些 Linux 发行版包括内置的 ISO 刻录应用程序（例如 Pop!_OS Popsicle）。
- 在 Windows 10/11 中刻录 ISO：右键单击 ISO 镜像，选择“显示更多选项”，然后选择“刻录光盘镜像”。

现在你明白了。您现在知道刻录 ISO 镜像的含义以及实现它所需的工具。

尽情享受吧！

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。