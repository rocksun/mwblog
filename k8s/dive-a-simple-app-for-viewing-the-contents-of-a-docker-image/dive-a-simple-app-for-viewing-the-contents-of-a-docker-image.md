# Dive：查看 Docker 镜像内容的应用

您是否曾经想知道一个 Docker 镜像包含哪些组成部分，而不必首先构建完整的软件材料清单？Dive 提供了这种洞察力。

翻译自 [Dive: A Simple App for Viewing the Contents of a Docker Image](https://thenewstack.io/dive-a-simple-app-for-viewing-the-contents-of-a-docker-image/) 。

![](https://cdn.thenewstack.io/media/2023/09/07dfd75c-dive-demo-ci-1024x610.png)
*功能截图由 Dive 提供*

你是否曾经想过了解一个 Docker 镜像的构成部分，而不必首先构建完整的[软件材料清单](https://thenewstack.io/how-to-create-a-software-bill-of-materials/)？也许你不仅想查看内容，还想找到缩小镜像大小的方法？

为了做到这一点，你需要了解诸如层、层的详细信息、每个层的内容和镜像的详细信息等方面的信息。

听起来是不是很费力呢？

有一个叫做 [Dive](https://github.com/wagoodman/dive) 的应用程序可以帮助你，实际上这个过程非常简单。

Dive包括以下功能：

- 镜像内容分解
- 显示每个层的内容详细信息
- 显示正在检查的镜像的总大小
- 显示镜像中的浪费空间（越小越好）
- 显示镜像的效率得分（越高越好）

这些都是非常重要的信息，特别是对于试图创建尽可能高效和安全的 Docker 镜像的开发人员而言。你肯定不想在镜像的层中包含不必要的应用程序，而 Dive 正是一个很好的工具，可以准确地了解其中的内容。

让我们开始安装 Dive 吧。

![](https://cdn.thenewstack.io/media/2023/09/10db0dd9-dive-demo.gif)

## 安装需求

Dive 可以安装在 Ubuntu、Red Hat Enterprise Linux 和基于 Arch 的发行版上，以及 MacOS 和 Windows 上。我将演示在 Ubuntu 22.04 上的安装过程。如果你使用不同的操作系统，你需要修改 Docker 和 Dive 的安装过程。在 MacOS 上，可以使用 Homebrew 或 MacPorts 安装 Dive，而在 Windows上，可以使用操作系统的[下载安装程序文件安装](https://github.com/wagoodman/dive/releases/latest)。

## 安装 Docker

要使用 Dive 来检查镜像，你首先必须能够使用 Docker 拉取镜像（除非你打算创建自己的 Docker 镜像...这意味着你无论如何都需要安装 Docker）。下面是如何在 Ubuntu 22.04 上安装 Docker 运行时引擎的步骤。

首先，你必须下载并安装官方的 Docker GPG 密钥（以便你可以安装软件）。为此，请登录到你的 Ubuntu 实例，打开一个终端窗口，然后执行以下命令：

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

添加了 GPG 密钥后，现在是时候创建适当的 Docker 存储库了，可以使用以下命令完成：

```
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

现在，存储库已经正确添加，我们将使用以下命令安装一些依赖项：

```
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

在安装 Docker 之前，我们现在必须使用以下命令更新 apt：

```
sudo apt-get update
```

使用以下命令安装 Docker：

```
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

为了允许你的用户使用 Docker（而不必使用 sudo，这可能会带来安全问题），你必须使用以下命令将用户添加到 docker 组中：

```
sudo usermod -aG docker $USER
```

退出并重新登录以使更改生效。

## 安装 Dive

现在是时候安装 Dive 了。在 Ubuntu 上，这也是通过命令行完成的。有三个命令要使用。

第一个命令将最新的 Dive 版本定义为名为 DIVE_VERSION 的环境变量。该命令是：

```
export DIVE_VERSION=$(curl -sL "https://api.github.com/repos/wagoodman/dive/releases/latest" | grep '"tag_name":' | sed -E 's/.*"v([^"]+)".*/\1/')
```

接下来，使用以下命令下载最新版本：

```
curl -OL https://github.com/wagoodman/dive/releases/download/v${DIVE_VERSION}/dive_${DIVE_VERSION}_linux_amd64.deb
```

上述命令将下载一个 .deb 文件到当前工作目录。然后，你可以使用以下命令安装 Dive：

```
sudo apt install ./dive_${DIVE_VERSION}_linux_amd64.deb
```

安装完成后，你就可以测试该应用程序了。

## 使用 Dive

有了 Dive 和 Docker 两者的安装，Dive 不仅可以深入到容器镜像中，还可以拉取镜像。

假设你想要查看最新的 Alpine Docker 镜像。该命令是：

```
dive alpine:latest
```

一旦镜像被拉取，Dive 将显示镜像的内容，显示每个层和其中的内容（图1）。

![](https://cdn.thenewstack.io/media/2023/08/09cd7597-dive1.jpg)
*图1：Dive 工具显示最新的 Alpine 镜像的层。*

Dive 会自动从 Docker Hub 拉取镜像。你可以使用 source 选项定义不同的来源，像这样：

```
dive IMAGE --source SOURCE
```

其中，IMAGE 是你想要拉取的镜像的名称，SOURCE 是存储库的位置。

要退出 Dive，使用 [Ctrl]+[C] 键盘组合键。

假设你想要查看 MongoDB 镜像。使用以下命令完成：

```
dive mongo:latest
```

考虑到这是一个更复杂的镜像，你会发现有多个层。你可以使用光标键在层之间导航。当前选择的层将由一个小紫色方块表示（图2）。

![](https://cdn.thenewstack.io/media/2023/08/0a2c5a62-dive2.jpg)
图2：我们深入到了最新的MongoDB镜像中，并发现了多个层。

如果按 Tab 键，你将移动光标到右窗格，然后可以使用光标键导航到层次结构。

在左下角的窗格中，你将看到浪费空间和镜像效率信息。如果这是一个自定义镜像，而这些详细信息不令人满意，你需要对镜像进行一些工作，重新构建它，然后再次深入其中。

这基本上是使用 Dive 工具查看任何 Docker 镜像内容的基础知识。希望这个命令行应用程序能帮助你构建更高效和安全的镜像（或者至少了解构成你使用的镜像的确切内容）。
