<!--
title: Baserow：开源无代码Airtable替代
cover: https://cdn.thenewstack.io/media/2023/11/08450677-screenshot.2e16d0ba.fill-1920x1006-1-1024x537.png
-->

Airtable数据库无法在Linux上运行让你失望？开源数据库Baserow能满足你。下面让我们了解如何上手Baserow。

> 译自 [Baserow: A No Code， Open Source Alternative to Airtable](https://thenewstack.io/baserow-a-no-code-open-source-alternative-to-airtable/)，作者 Jack Wallen。

前几天，我想在 Linux 上安装 [Airtable](https://www.airtable.com/)，这是一种混合数据库/电子表格服务，非常适合快速构建应用程序。让我非常沮丧的是，这种众所周知的服务没有 Linux 客户端。我该怎么办呢？

由于我使用 Linux 作为我的主要操作系统，我知道一定有替代方案。而且[Docker](https://www.docker.com/?utm_content=inline-mention) 也一定会让以前复杂的安装和设置变得简单。

![](https://cdn.thenewstack.io/media/44de3f9b-baserow.svg)

*Baserow 标志*

所以，我开始寻找那个替代方案。我的旅程引导我到一个叫 [Baserow](https://baserow.io/) 的应用程序。

Baserow 包含我需要的所有 Airtable 类系统的功能，例如用户友好的界面，协作和集成(与应用程序/服务如 [Slack](https://thenewstack.io/developer-guide-a-new-way-to-build-on-the-slack-platform/) 和 Zapier)，以及丰富的高级功能，例如复杂的公式和功能，通过工作流程和 Webhook 实现任务自动化，导入/导出等。

更好的是，通过将 Baserow 部署到您自己的网络上，您可以完全控制数据的隐私和安全性。

如果这听起来像您(或您的团队)可以使用的东西，请继续阅读，了解部署 Baserow 的简单性。

## 您需要什么

要遵循本教程，您需要一个支持 Docker 的服务器操作系统。我将在 Ubuntu Server 22.04 上演示这一点。如果您使用不同的操作系统，则需要更改 Docker 安装过程以匹配您选择的平台。

就是这样。让我们深入研究并进行部署。

## 安装 Docker

因为我喜欢完整地演练整个过程(并不假设您已经安装好了 X/Y/Z 的某个部分并准备好了)，所以让我们首先演练在服务器上安装 Docker 的步骤。

开始吧。

首先，您必须下载并安装所需的 Docker GPG 密钥，可以使用以下命令完成:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

完成后，您必须添加官方 Docker 仓库。添加必要仓库的命令是:

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list &gt; /dev/null
```

在我们安装 Docker 之前，我们必须使用以下命令安装一些简单的依赖项：

```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

接下来，更新 apt: 

```bash
sudo apt-get update
```

现在可以使用以下命令安装 Docker CE(Community Edition)：

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

现在 Docker 已安装，您必须将用户添加到 docker 用户组。如果跳过此步骤，则在使用 Docker 时必须使用 sudo，这可能会导致部署的严重安全问题。要将用户添加到用户组中，请运行命令：

```bash
sudo usermod -aG docker $USER
```

最后，退出并重新登录以使更改生效。

重新登录后，使用以下命令列出 Docker 容器来验证一切是否正常工作:

```bash
docker ps
```

输出中应仅显示：

```bash
CONTAINER ID IMAGE COMMAND CREATEDSTATUSPORTS
```

各列中不应列出任何内容。

您现在已准备好部署 Baserow。

## 使用 Docker 部署 Baserow

Baserow 的部署可以通过一个命令来完成，即：

```bash
docker run -d --name baserow -e BASEROW_PUBLIC_URL=<a href="http://192.168.1.227">http://</a>服务器 -v baserow_data:/baserow/data -p 80:80 --restart unless-stopped baserow/baserow:latest
```

其中服务器是托管服务器的 IP 地址或域名。

如果您以前部署过 Docker 容器，上述命令应该看起来很熟悉。但是，您应该了解的一件事是 BASEROW_PUBLIC_URL 选项。如果不包含该选项，您将无法访问 Baserow。您可以将其设置为托管服务器的 IP 地址或域名。如果您选择域名路线(因此您可以从局域网外访问它)，您需要确保网络硬件将域名指向 Baserow 服务器的 IP。

另外，如果该服务器已经在使用 80 端口，您会想要将 80:80 改为类似 8081:80 的东西。只需确保该对中的第一个端口在您的服务器上可用，否则部署将失败。

## 访问 Baserow

打开网页浏览器，指向 http://SERVER(其中SERVER是托管服务器的 IP 地址或域名)。如果使用了 80 以外的外部端口，请确保将其添加到地址中，例如 http://SERVER:8081。

您将看到 Baserow 注册页面(图 1)。

![](https://cdn.thenewstack.io/media/2023/11/41251e3c-baserow1.jpg)

*图1:在继续之前，您必须创建一个管理员用户。*

单击注册，然后 Baserow 登录窗口将显示。使用新创建的管理员用户凭据登录，Baserow 就准备好提供服务了(图2)。

![](https://cdn.thenewstack.io/media/2023/11/2e44824c-baserow2.jpg)

*图 2。*

恭喜您，您现在拥有一个可以从局域网中的任何位置访问的 Airtable 替代品。希望这个工具能像为我服务的那样为您服务。
