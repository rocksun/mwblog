# Hadolint：命令行下的 Dockerfile 代码检查工具

Hadolint 是一个命令行工具，帮助您确保您的 Dockerfile 遵循最佳实践，并将您的 Dockerfile 解析为抽象语法树（AST）。


翻译自 [Hadolint: Lint Dockerfiles from the Command Line](https://thenewstack.io/hadolint-lint-dockerfiles-from-the-command-line/) 。

![](https://cdn.thenewstack.io/media/2023/07/1ee55405-pedro-candeias-t1zapd0khfq-unsplash-1024x683.jpg)

关于容器的一个小秘密是，它并不总是像您期望的那样容易使用。举个例子，您是否曾经手工编写过 Dockerfile ，结果运行失败？这可能会非常令人沮丧。从 YAML 缩进、使用不适当的镜像、错误地使用标签，到错误的卷映射... 有许多问题可能导致 Dockerfile 运行失败。

这就是为什么您需要[代码检查工具](https://thenewstack.io/four-ways-to-enhance-your-dockerfiles/)。

不，我并不是在谈论衣服干燥机里积聚的灰尘。我谈论的是自动检查代码的程序错误和风格错误。

幸运的是，代码检查不是手动完成的，因为那不仅会非常耗时，而且可能会导致错误叠加。这就像作家编辑自己的作品一样... 大多数情况下，他们无法发现每一个错误。开发人员也是如此。有时候您需要新的一双眼睛，或者一个专门为此目的创建的工具。

![](https://cdn.thenewstack.io/media/2023/07/fecd3b35-68747470733a2f2f6861646f6c696e742e6769746875622e696f2f6861646f6c696e742f696d672f6361745f636f6e7461696e65722e706e67.png)
*Hadolint 吉祥物*

有很多可用的工具，其中一些是付费服务，允许您上传 Dockerfile （以及其他代码片段）进行代码检查。也有桌面应用程序可供使用进行代码检查。如果您喜欢使用命令行，有很多选项可供选择，其中之一就是 Hadolint 。

Hadolint是一个命令行工具，帮助您确保您的 Dockerfile 遵循最佳实践，并将您的 Dockerfile 解析为抽象语法树（AST），然后利用 ShellCheck （另一个脚本分析工具）运行预定义的一组规则对代码进行代码检查。

让我们了解如何使用 Hadolint 来确保您的 Dockerfile 遵循最佳实践，并且没有隐藏的问题。我将在 Ubuntu Server 22.04 上进行演示，但 Hadolint 也适用于 Linux 、 macOS 和 Windows 。

幸运的是，Hadolint不仅可用于本地运行。如果您已经安装了Docker，可以对您的Dockerfile运行Hadolint容器。我也将向您展示如何进行这样的操作。

首先，我们来看本地安装的方法。

## 如何安装 Hadolint

登录到您的Ubuntu Server实例，首先安装ShellCheck：

```bash
sudo apt-get install shellcheck -y
```

一旦安装完成，使用以下命令下载 Hadolint：

```bash
wget https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64
```

注意：请确保查看 [Hadolint 下载页面](https://github.com/hadolint/hadolint/releases)，以确保您下载的是最新版本。

下载完成后，将文件（同时更改文件名）移动到$PATH中的目录，例如：

```bash
sudo mv hadolint-Linux-x86_64 /usr/local/bin/hadolint
```

接下来，赋予该文件可执行权限：

```bash
sudo chmod +x /usr/local/bin/hadolint
```

您可以通过以下命令验证是否安装成功：

```bash
hadolint --help
```

如果看到帮助页面打印出来，您就可以开始使用了。


## 本地检查您的 Dockerfile


为了测试目的，我使用了一个我之前保存的旧 Dockerfile 。使用以下命令创建文件：

```bash
nano Dockerfile
```

将以下内容粘贴到该文件中：

```Dockerfile
#
# Base the image on the latest version of Ubuntu
FROM ubuntu:latest
#
# Identify yourself as the image maintainer (where EMAIL is your email address)
LABEL maintainer="YOUR_EMAIL"
#
# Update apt and update Ubuntu
RUN apt-get update && apt-get upgrade -y
#
# Install NGINX
RUN apt-get install nginx -y
#
# Expose port 80 (or whatever port you need)
EXPOSE 80
#
# Start NGINX within the Container
CMD ["nginx", "-g", "daemon off;"]

```

保存并关闭文件。

现在，我们可以使用 Hadolint 对文件进行代码检查：

```bash
hadolint Dockerfile
```

输出应该类似于以下内容：

```log
Dockerfile:3 DL3007 warning: Using the latest is prone to errors if the image will ever update. Pin the version explicitly to a release tag
Dockerfile:9 DL3009 info: Delete the apt-get lists after installing something
Dockerfile:12 DL3015 info: Avoid additional packages by specifying --no-install-recommends
Dockerfile:12 DL3008 warning: Pin versions in apt get install. Instead of apt-get install <package> use apt-get install <package>=<version>
```


根据输出内容对您的 Dockerfile 进行修改。一旦修改完成，重新运行代码检查，希望问题都已解决。

## 使用 Hadolint Docker 容器对您的 Dockerfile 进行代码检查

如果您不想在本地安装 Hadolint ，您可以使用容器化版本的工具对本地存储的 Dockerfile 进行检查。当然，这需要先安装 Docker 。如果您尚未安装 Docker ，请按以下步骤在 Ubuntu Linux 上安装它：

1. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/1. share/keyrings/docker-archive-keyring.gpg
1. echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] 1. https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/1. apt/sources.list.d/docker.list > /dev/null
1. sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release curl 1. git -y
1. sudo apt-get update
1. sudo apt-get install docker-ce docker-ce-cli containerd.io -y
1. sudo usermod -aG docker $USER
1. 退出并重新登录。

安装了 Docker 之后，您可以使用 Hadolint Docker 容器轻松对 Dockerfile 进行代码检查：

![](https://cdn.thenewstack.io/media/2023/07/2b8771ac-hadolint-lint.png)

如果您之前使用相同的Dockerfile（未做任何更改），您应该会看到相同的输出。

这就是您如何通过命令行轻松进行 Dockerfile 代码检查。要了解有关如何使用 Hadolint 的更多信息，请查阅帮助信息（使用 `Hadolint --help` 命令）以查看可用的不同选项。但是对于基本的 Dockerfile 代码检查，直接使用 Hadolint 命令就可以完美解决。