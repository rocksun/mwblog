# Docker 基础：如何使用 Dockerfiles

![Featued image for: Docker Basics: How to Use Dockerfiles](https://cdn.thenewstack.io/media/2019/06/76845160-child-1864718_640.jpg)

[Esi Grünhagen](https://pixabay.com/users/FeeLoona-694250/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1864718) 来自 [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1864718).

## 理解 Dockerfiles：构建与应用

Dockerfile 是一个脚本，可以自动创建 Docker 镜像，这对于构建容器至关重要。关键部分包括指定基础镜像 (FROM)、执行命令 (RUN)、复制文件 (COPY)、暴露端口和设置环境变量。利用 Dockerfiles 可以提高镜像创建的效率、可重用性和标准化。

要构建 Dockerfile，请创建一个目录并定义特定的关键字，如 FROM、RUN 和 MAINTAINER。例如，用于更新 Ubuntu 镜像的基本 Dockerfile 涉及更新软件包和安装 build-essential 的命令。

创建 Dockerfile 后，使用命令 *docker build -t “NAME:Dockerfile,”*（其中 NAME 是您要使用的名称）构建镜像。此过程能够有效地管理容器的多个变体，从而简化从单个镜像的部署。

## 概述

Dockerfile 是一个文本文件，其中包含用于在 Docker 中构建和配置镜像的指令。它用于自动执行从头开始创建容器的过程，使用各种层来构建最终镜像。Dockerfile 通常包含以下部分：

**From**: 此行指定您的新镜像将构建在其之上的基础镜像。
**Run or Command**: 这些行在构建过程中运行命令，例如安装依赖项或设置环境变量。
**Copy**: 此指令将文件从当前目录复制到容器中的特定位置。
**Exposed port**: 此行指定在创建镜像并在容器中运行时将暴露哪些端口。
**Environment variables**: 这些行设置您的应用程序要使用的环境变量。

使用 Dockerfile 有几个好处，包括高效的镜像创建、可重用性、可移植性、标准化、更快的构建过程和更好的测试。

在本文中，您将学习 Dockerfile 的基础知识、如何构建 Dockerfile、如何从 Dockerfile 构建 Docker 镜像以及如何使用 Dockerfile 部署容器。

通过使用 [Docker](https://www.docker.com/?utm_content=inline+mention) 镜像，不仅可以一个接一个地部署容器，而且非常容易。从注册表（例如 [Docker Hub](https://hub.docker.com/)）中提取镜像后，可以使用单个 [docker command](https://thenewstack.io/how-to-use-the-docker-exec-command/) 部署每个容器。但是，如果您发现自己必须从同一镜像部署大量容器（每个容器用于不同的目的）会发生什么？突然之间，[这些容器的管理](https://thenewstack.io/deploy-portainer-for-easier-container-management/)可能会变得有点麻烦。
例如，假设您下载最新的 [Ubuntu image](https://thenewstack.io/an-introduction-to-ubuntus-uncomplicated-firewall/) 用于开发。在使用该容器进行开发之前，您需要对镜像进行一些修改（例如升级 [软件并添加手头工作所需的必要开发包](https://thenewstack.io/surprise-software-testing-is-every-developers-job-now/)）。

为此，您可以根据需要手动编辑每个镜像（为主题的每个必要变体创建一个新镜像），或者您可以为每个变体构建一个 Dockerfile。构建好 Dockerfile 基础知识后，您可以快速 [构建相同的镜像](https://thenewstack.io/3-best-practices-for-image-building-and-scanning/) 一遍又一遍，而无需花费时间手动完成。精心设计的 Dockerfile 可以为您节省大量时间和精力。

我想向您介绍如何使用 Dockerfile 的过程。我将通过使用最新的 Ubuntu 镜像、更新和升级该镜像，然后安装 build-essential 软件包来进行演示。这将是一个相当基本的 Dockerfile，但您可以轻松地在此基础上进行构建。

**Dockerfile 基础知识**

在我们构建 Dockerfile 之前，您需要了解构成该文件的内容。这将是一个名为 Dockerfile 的文本文件，其中包含特定的关键字，用于指示如何构建特定的镜像。您可以在文件中使用的特定关键字包括：
**ADD** 将主机上的源文件复制到容器文件系统的目标位置。**CMD** 可用于在容器内执行特定命令。**ENTRYPOINT** 设置一个默认应用程序，每次使用该镜像创建容器时都会使用该程序。**ENV** 设置环境变量。**EXPOSE** 关联一个特定的端口，以实现容器与外部世界之间的网络连接。**FROM** 定义用于启动构建过程的基础镜像。**MAINTAINER** 定义镜像创建者的全名和电子邮件地址。**RUN** 是 Dockerfile 的核心执行指令，也称为 run Dockerfile 命令。**USER** 设置运行容器的 UID（或用户名）。**VOLUME** 用于启用从容器到主机上目录的访问。**WORKDIR** 设置使用 CMD 定义的命令要执行的路径。**LABEL** 允许您向 Docker 镜像添加标签。
并非所有关键字都是 Dockerfile 运行所必需的。例如，我们的示例将仅使用 FROM、MAINTAINER 和 RUN。

**构建 Dockerfile**

在创建基本 Dockerfile 之前，我们需要创建一个新的工作目录。我们将使用以下命令创建 **dockerbuild** 目录：

```bash
mkdir ~/dockerbuild
```

使用以下命令进入新创建的目录：

```bash
cd ~/dockerbuild
```

现在，我们将编写我们的 Dockerfile。使用以下命令创建新文件：

```bash
nano Dockerfile
```

在该文件中，粘贴以下内容以运行 Dockerfile：

```dockerfile
FROM ubuntu:latest
MAINTAINER NAME EMAIL
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential
```

NAME 是您的全名，EMAIL 是您的电子邮件地址。
保存并关闭该文件。

**构建您的 Docker 镜像**

完成基本 Dockerfile 后，您现在可以从该文件构建镜像。发出以下命令（从 *~/dockerbuild* 目录中）：

```bash
docker build -t "NAME:Dockerfile" .
```

其中 NAME 是要创建的新镜像的名称，重要的是要注意 NAME 必须全部小写，否则构建将失败。
例如，假设您要为 Web 开发、应用程序开发和安全开发创建镜像。您可以发出以下命令：

```bash
docker build -t "appdev:Dockerfile" .
docker build -t "webdev:Dockerfile" .
docker build -t "secdev:Dockerfile" .
```

这将开始下载 ubuntu:latest 镜像并根据 Dockerfile 构建镜像的过程（**图 1**）：
![](https://cdn.thenewstack.io/media/2024/02/847f61a1-dockerfiles-1.jpg)
图 1：镜像已构建。

构建完成后，发出以下命令：

```bash
docker images
```

您应该看到所有新构建的镜像，现在可以使用了（**图 2**）：
![](https://cdn.thenewstack.io/media/2024/02/e8247536-dockerfile-02.jpg)
图 2：新创建的镜像已准备好部署。

**如何在 Rocky Linux 上运行 Dockerfile**

假设您想使用 [Rocky Linux](https://thenewstack.io/start-developing-with-rocky-linux-as-a-docker-container/) 创建一个镜像，该镜像更新拉取的 Rocky Linux 镜像并安装 Web 服务器。为此，我们首先使用以下命令创建一个新目录：

```bash
mkdir ~/rockylinux
```

使用以下命令进入该目录：

```bash
cd ~/rockylinux
```

使用以下命令创建新的 Dockerfile：

```bash
nano Dockerfile
```

将以下内容粘贴到该文件中以运行 Dockerfile 命令：

```dockerfile
FROM rockylinux:9
MAINTAINER NAME EMAIL
RUN dnf makecache
RUN dnf upgrade -y
RUN dnf install -y httpd
```

其中 NAME 是您的姓名，EMAIL 是您的电子邮件地址。
保存并关闭文件。使用以下命令构建镜像：

```bash
docker build -t “webdev_rockylinux:Dockerfile” .
```

根据需要升级的内容多少，此特定构建将比 Ubuntu 镜像花费更长的时间。构建完成后，发出命令 *docker images* 以查看您新构建的（基于 CentOS 的）镜像已准备就绪（**图 3**）：
![](https://cdn.thenewstack.io/media/2024/02/65fe0164-dockerfile-3.jpg)
图 3：Rocky Linux 镜像可用于部署。

**Docker 镜像构建变得简单**

这就是使用 Dockerfile 构建 Docker 镜像的全部内容。与提交对拉取镜像的更改相比，这是一种更有效和标准的创建新镜像的方法。一旦您熟练掌握如何使用 Dockerfile，您可以创建的镜像类型就没有限制。

*（编者注：此帖子已更新。它最初于 2019 年 6 月 19 日发布。）*
**常见问题解答：使用 Dockerfile**
**1. 什么是 Dockerfile？**
Dockerfile 是一个文本文件，其中包含一系列关于如何构建 Docker 镜像的指令。它定义了将在容器内运行的环境和应用程序。

**2. Dockerfile 中使用的基本命令有哪些？**
以下是您可能会遇到的一些基本命令：
**FROM**: 指定新镜像的基础镜像。

**RUN**: 在当前镜像顶层的新层中执行命令，并提交结果。

**COPY**: 将文件或目录从主机文件系统复制到镜像中。

**CMD**: 为正在执行的容器提供默认值，例如要运行的命令。

**ENTRYPOINT**: 配置容器以作为可执行文件运行。

**3. 如何从 Dockerfile 构建镜像？**

要构建镜像，请导航到包含 Dockerfile 的目录，并在终端中运行以下命令：

```
docker build -t your-image-name .
```

**4. CMD 和 ENTRYPOINT 之间有什么区别？**

- CMD: 为容器设置默认命令和/或参数。 可以在运行容器时覆盖它。
- ENTRYPOINT: 配置容器以作为可执行文件运行。 它不会被命令行参数覆盖。

**5. 如何优化我的 Dockerfile？**

要优化您的 Dockerfile，请考虑以下提示：

- 尽量减少层数：尽可能使用 `&&` 组合命令。
- 明智地排序您的命令：将更改频率较低的命令放在顶部，以利用缓存。
- 使用 `.dockerignore`: 排除镜像中不需要的文件和目录，以减小大小。

**6. 什么是多阶段构建？**

多阶段构建允许您在 Dockerfile 中使用多个 `FROM` 语句，这对于将构建环境与运行时环境分离非常有用，有助于显着减小最终镜像大小。

**7. 如何从我的镜像运行容器？**

构建镜像后，您可以使用以下命令运行容器：

```
docker run -d IMAGE
```

其中 IMAGE 是要使用的镜像的名称。

**8. 在哪里可以找到有关 Dockerfile 的更多信息？**

有关更多详细信息，您可以参考 [官方 Docker 文档](https://docs.docker.com/reference/dockerfile/)，其中提供了有关 Dockerfile 及其用法的丰富资源。

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)