<!--
title: Bash 5.3迎来重大改进——教你如何测试
cover: https://cdn.thenewstack.io/media/2025/07/58ed64e4-bash.png
summary: GNU基金会发布了Bash 5.3，包含命令替换、GLOBSORT变量等新功能。可通过源代码安装，但建议在非生产环境进行。
-->

GNU基金会发布了Bash 5.3，包含命令替换、GLOBSORT变量等新功能。可通过源代码安装，但建议在非生产环境进行。

> 译自：[Bash 5.3 Has Some Big Improvements — Here's How You Can Test It](https://thenewstack.io/bash-53-has-some-big-improvements-heres-how-you-can-test-it/)
> 
> 作者：Jack Wallen

GNU 基金会宣布，Bash（版本 5.3）命令行解释器的最新公开发布版现已推出，距离之前的稳定版本已经过去了三年之久。

新版本的 Bash 包含一些有趣的新功能，将吸引所有类型的用户。首先，让我们来谈谈 Bash 中的新功能，然后我将向您展示如何在您选择的 Linux 发行版上安装最新版本（从源代码安装）。

## 什么是 Bash？

首先，让我们来谈谈 Bash。这个软件到底是什么？

Bash 是最常用的 [Linux](https://thenewstack.io/learning-linux-start-here/) shell。

但是什么是 shell 呢？

在 Linux 中，shell 充当命令解释器。[如果没有 shell](https://thenewstack.io/jeffrey-snover-remembers-the-fight-to-launch-powershell/)，您将无法在 Linux 中运行命令。当您在 Linux 中运行命令时，Bash 会理解这些命令，然后成功执行它们。当然，按照典型的 Linux 风格，有几个 shell 可供选择。有 bash、csh、Bourne、KornShell (ksh)、T Shell (tcsh)、Z Shell、Debian Almquist Shell (dash) 等等。

Bash 是大多数 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/)上的默认 shell，因为它最容易使用、高度可配置，并且包含您在 shell 中需要的所有功能。应该注意的是，为您选择的发行版安装新的 shell 并不总是一个简单的体验，但这是完全有可能的。

例如，如果您想在 Ubuntu 上安装 fish shell，您首先需要[运行以下命令](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)：

```
sudo apt-get update && sudo apt-get install fish -y
```

然后，您可以使用以下命令启动 fish shell：

```
fish
```

您还可以使用 Change Shell 命令将 fish 设置为默认 shell：

```
sudo chsh -s /usr/bin/fish
```

您的默认 shell 现在是 fish。

但我们正在讨论 Bash，所以让我们回到正题。

## Bash 的新功能是什么？

5.3 版本增加了一些重要的新功能，其中最重要的是一种新的命令替换形式，它在当前 shell 上下文中执行命令。根据官方的更新日志，“实现了两种形式：一种读取命令替换的输出，另一种期望在命令替换完成时在 REPLY shell 变量中找到结果。”

两者的区别在于管道字符的添加，如下所示：

```
${ command; }
${ | command; }
```

第一个捕获命令的输出而不派生它，第二个在当前 shell 中运行命令并将结果留在 REPLY 中。

对于那些不熟悉 REPLY 的人来说，它是一个默认变量，用于存储来自 read 命令的响应，而没有指定任何变量。它允许您访问用户提供的输入，而无需为其定义单独的变量。

然后是新的 GLOBSORT shell 变量，它决定了 shell 如何对路径名完成的结果进行排序。

其他新增功能包括：

* compgen 内置命令现在有一个选项，可以将生成的补全放入指定的 shell 变量中（而不是标准输出）。
* read 内置命令新增了一个 -E 选项，该选项使用带有默认 bash 补全（包括可编程补全）的 readline。
* source 内置命令新增了一个 `-p PATH` 选项，该选项强制使用 PATH 参数，而不是使用 $PATH 来搜索文件。

## 如何安装 Bash 5.3

在撰写本文时，Bash 5.3 仍处于候选发布状态，因此还需要一段时间才能进入标准存储库。但是，如果您渴望测试新功能，您可以从源代码安装它。方法如下。

第一步是下载源代码。您可以使用 wget 下载它：

```
wget http://ftp.gnu.org/gnu/bash/bash-5.3.tar.gz
```

使用以下命令解压文件：

```
tar -xvzf bash-5.3.tar.gz
```

使用以下命令安装必要的依赖项（以便您可以从源代码安装）：

```
sudo apt-get install build-essential -y
```

使用以下命令进入 bash 文件夹：

```
cd bash-5.3
```

使用以下命令配置构建：

```
./configure
```

接下来，您必须使用以下命令编译代码：

```
make
```

上面的命令可能需要一些时间才能运行，因此请允许它完成。

使用以下命令运行安装：

```
sudo make install
```

使用以下命令确保 bash 是您的默认 shell：

```
sudo chsh -s /usr/local/bin/bash
```

此时，您应该已经安装了 Bash 5.3。您可以使用以下命令验证安装：

```
bash --version
```

您应该在顶部附近看到列出的 5.3.0 版本。

在我看来，我不会在生产机器上安装 5.3，因为，你永远不知道会发生什么。如果您真的很好奇（或者想了解新版本的最新信息），我建议您在备用（非生产）机器或虚拟机 (VM) 中安装最新的公开发布版本。您当然不希望破坏生产机器上的 shell，因为这样做的后果可能是灾难性的（也就是说，您无法再运行命令……天哪！）。

享受新的 Bash 味道吧。