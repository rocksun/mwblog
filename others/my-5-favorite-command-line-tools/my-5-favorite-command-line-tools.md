
<!--
title: 我最喜欢的5个命令行工具
cover: https://cdn.thenewstack.io/media/2024/10/28e31613-5favoritecommandlinetools.jpg
-->

将这五个 CLI 工具添加到您的工具箱中，以改进您的软件开发工作流程。

> 译自 [My 5 Favorite Command Line Tools](https://thenewstack.io/my-5-favorite-command-line-tools/)，作者 Pratik Patel。


无论你是 [Linux 命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 的新手，还是已经使用它多年（甚至几十年？），我都想向你展示我最喜欢的五个命令行界面 (CLI) 工具：SDKMAN、eza、ffmpeg、pueue 和 find。读完这篇文章后，你会变得更加高效，并感觉自己像个 CLI 摇滚明星。

打开一个终端，让我们来了解这些工具吧！

## 1. 用于管理 JDK 的 SDKMAN

SDKMAN 代表“软件开发工具包管理器”，它是一个用于管理多个 SDK 并轻松地在它们之间切换的工具。让我们用它来安装和管理 Java 开发工具包 ([JDK](https://thenewstack.io/end-of-the-road-for-javafx-in-jdk-8-keeping-your-apps-alive/))。

要安装它，只需按照 [SDKMAN 安装页面](https://sdkman.io/install/) 上的简单说明操作即可，无论你是在 Linux、MacOS 还是 Windows 上。我将安装免费的 Azul Zulu 构建，它是 Azul 完全免费的 OpenJDK 构建。

你可以通过在命令行中键入以下内容来列出所有可用的 JDK：

```
sdk list java
```

这将产生类似于以下的输出：

![](https://cdn.thenewstack.io/media/2024/10/8199a6b3-sdk_list_java-1024x259.png)

由于 [Java 23 刚刚发布](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/)，让我们安装它吧！使用 SDKMAN 很简单，只需发出以下命令：

```
sdk install java 23-zulu
```

![](https://cdn.thenewstack.io/media/2024/10/36000150-sdk_install-java-1024x487.png)

瞧，你现在已经安装了 Java 23。你可以使用命令 `java -version` 来检查它是否已安装并且是默认构建：

![](https://cdn.thenewstack.io/media/2024/10/06c15ab9-java_-version-1024x150.png)

你可能想要安装旧版本的 Java，这也很容易。例如，你想安装 Java 17？在控制台中输入以下内容：

```
sdk install java 17.0.12-zulu
```

它会询问你是否要将其设置为默认值——这取决于你。你可以通过发出以下命令轻松地在运行时切换版本；它将命令中指定的 JDK 设置为将在该 shell 会话中使用的 JDK：

```
sdk use java 17.0.12-zulu
```

![](https://cdn.thenewstack.io/media/2024/10/47994d51-sdk_use_java-1024x179.png)

## 2. 更好的 ls：eza

`ls` 命令非常适合列出文件，但我更喜欢使用 `eza`，因为它会对输出进行颜色编码，并且了解 [符号链接](https://en.wikipedia.org/wiki/Symbolic_link) 和 [Git](https://roadmap.sh/git-github) 等内容。

例如，你可以指定一个树深度，它将输出到该深度的所有文件：

```
eza -l –TL3
```

![](https://cdn.thenewstack.io/media/2024/10/0ff1df54-eza_-l-1024x395.png)

通常，我想先看到顶部的目录，然后看到目录中的文件。你可以使用 `eza` 来做到这一点：

```
eza -al --group-directories-first
```

![](https://cdn.thenewstack.io/media/2024/10/847ca965-eza_-al-1024x229.png)

我经常使用它，所以我为它创建了一个别名：

```
alias ll="eza -al --group-directories-first"
```

所以现在我只需键入 `ll`，它就会格式化和排序输出，以便我更快地找到东西。

## 3. A/V 瑞士军刀：ffmpeg

`ffmpeg` 工具是一个用于处理音频和视频文件的综合命令。它可以做任何事情：调整视频文件大小、将视频文件的音频输出到 MP3、从不同的视频格式转换，等等。关于 `ffmpeg` 有些很棒的教程和书籍，但我想向你展示一个如何将 1080p 视频文件调整为 480p 的示例。

```
ffmpeg -i ./AltantaTimeLapse.mp4 -vf scale=-1:480 -c:v libx264 -crf 0 -preset veryslow -c:a copy AltantaTimeLapse-480.mp4
```

`scale` 选项告诉 `ffmpeg` 调整大小并保留纵横比（因为我只提供了一个维度：`scale=-1:480`）。它还告诉 ffmpeg 复制音频，因为我不需要更改它。

以下是我的桌面上原始视频文件和缩小后的视频文件，以便你看到区别：

![](https://cdn.thenewstack.io/media/2024/10/be18bea1-ffmpeg-1024x642.png)

如果你想了解更多信息，我推荐这篇深入的 [ffmpeg 教程](https://img.ly/blog/ultimate-guide-to-ffmpeg/)。

## 4. 使用 Pueue 进行多步骤作业处理

`pueue` 命令是“处理队列”的缩写——或者正如其 [网站所说](https://github.com/Nukesor/pueue)，“Pueue 是一个命令行任务管理工具，用于顺序和并行执行长时间运行的任务。”当你不想坐在电脑前运行一系列需要很长时间才能完成的命令时，它是一个非常有用的命令。或者，它也可以作为一种自动执行大量命令的方式，这样你就可以去喝杯咖啡休息一下。

我们刚刚使用 `ffmpeg` 处理了一个视频文件，这将需要一些时间（并且根据视频的长度或分辨率，它可能需要 *很长时间*）。让我们用 `pueue` 来做这些事情，这样我们就不用一直盯着我们的任务了：

1. 处理文件（调整大小）。
2. 使用 `find` 命令将它们移动到一个名为 Finished 的文件夹中。

使用你的系统包管理器安装 `pueue`，然后确保它的守护进程正在运行：

```
pueued –d
```

![](https://cdn.thenewstack.io/media/2024/10/d4f07e79-pueued_-d-1024x115.png)

现在将 `ffmpeg` 命令排队：

```
pueue add -- ffmpeg -i ./AtlantaTimeLapse.mp4 -vf scale=-1:480 -c:v libx264 -crf 0 -preset veryslow -c:a copy AtlantaTimeLapse-480.mp4
```

还要将将文件移动到名为 Finished 的文件夹中的命令排队：

```
pueue add -- find . -type f -name "*480p*" -exec mv {} finished/
```

输入命令 pueue 查看队列中的内容及其状态：

![](https://cdn.thenewstack.io/media/2024/10/4dfb569c-pueue-1024x411.png)

## 5. 不要使用 Hunt 命令；使用 Find 命令

Unix find 命令在您查找文件时是一个可以节省大量时间的强大工具。您甚至可以用它对找到的文件运行一个命令。您可以按类型、名称、属性等等找到文件。我们在上面使用 find 命令来移动已处理的文件：

```bash
find . -type f -name "*480p*" -exec mv {} finished/
```

.表示从这个目录开始查找文件。

让我们来看一下这些选项。

- 仅查找文件（不查找目录）：-type f 
- 在文件名中查找带有 480p 的文件：-name "*480p*" 
- 对找到的文件执行命令：-exec mv {} finished 

exec 标志表示：“对 find 命令找到的每一项执行 mv 命令。”{} 用于替换找到的文件或目录。选项非常多，我推荐使用本教程来入门。

## 结论

我们已经逐步介绍了我在开发软件时日常工作中发现的五个宝贵的命令行工具。我希望您能够在您的工具箱中添加一些新的工具！

**了解更多信息，请注册参加 [All Things Open 2024](https://thenewstack.io/event/all-things-open-2024/)，您可以在那里听到 [Pratik](https://2024.allthingsopen.org/speakers/pratik-patel) 和其他开源专家分享他们的见解和知识。**