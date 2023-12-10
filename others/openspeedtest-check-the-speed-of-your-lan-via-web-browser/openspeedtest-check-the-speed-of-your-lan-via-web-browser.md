<!--
title:浏览器OpenSpeedTest检测局域网速率
cover: https://cdn.thenewstack.io/media/2023/12/e85bed58-denny-muller-pulu3axfjtq-unsplash-1024x683.jpg
-->

OpenSpeedTest可轻松测试局域网基础速率，检测局域网是否正常通信响应。

> 译自 [OpenSpeedTest: Check the Speed of your LAN via Web Browser](https://thenewstack.io/openspeedtest-check-the-speed-of-your-lan-via-web-browser/)，作者 Jack Wallen 就是当 X 代思维与当今讽刺融合时所发生的事情。Jack 是一个寻求真理和词语的写手，他用量子力学笔和不协调的声音与灵魂节拍写着字。虽然他驻扎在...
阅读更多来自 Jack Wallen 的文章。


想象你正在开发一个内部网络上的应用程序，这个应用程序需要一定的网络速度才能正常运行。你可以打开网页浏览器，指向市场上众多的网络速度测试之一，但我相信你知道这会做什么......它测试你与外部世界的连接。

如果你想测试 LAN 本身的速度怎么办？[Speedtest.net](https://www.speedtest.net/) 并没有多大帮助，尤其是当你正在开发一个只在 LAN 上运行的应用程序或者你计划推出到全球的应用程序，而它目前还在 alpha 开发阶段。掌握网络速度可以是一个方便的故障排除工具。

这就是 [OpenSpeedTest](https://github.com/openspeedtest/Speed-Test) 的用武之地。

OpenSpeedTest 是一个免费的开源 HTML5 网络性能估计工具，它不需要任何客户端软件或插件即可运行。一旦部署，该工具可以从标准的现代网页浏览器访问。更棒的是，OpenSpeedTest 可以与 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 一起部署。它使用 [NGINX](https://thenewstack.io/microservices-architectures-release-7-nginx-plus-googles-spdy-protocol/) 和 [Alpine Linux](https://thenewstack.io/alpine-linux-heart-docker/) 的组合来最大限度地减少 [Docker 服务器](https://thenewstack.io/deploy-a-docker-swarm-on-rocky-linux/)上的资源消耗。

你可以运行有或没有 [Let's Encrypt](https://letsencrypt.org/) SSL(自动证书更新)的 OpenSpeedTest。我将向你展示这两种方法。

![](https://cdn.thenewstack.io/media/2023/11/d6a18288-10g-s.gif)

## 你需要什么

要使用 OpenSpeedTest，你需要一台服务器来托管容器和一个具有 sudo 权限的用户。我将在 Ubuntu Server 22.04 上演示此操作，因此如果你使用不同的操作系统，则需要更改 Docker 安装说明(但没有更多)。

就是这样，让我们开始吧。

## 安装 Docker

由于我不会遗漏任何内容，让我首先向你展示如何在 Ubuntu Server 上安装 Docker。

首先要处理的事情是下载并安装所需的 Docker GPG 密钥。使用以下命令执行此操作:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

该命令完成后，使用以下命令添加官方 Docker 仓库:

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

使用以下命令安装所需的依赖项:

```bash
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y
```

在运行 Docker 安装之前，你必须先使用以下命令更新 apt:

```bash
sudo apt-get update
```

现在是时候安装 Docker 社区版、CLI 工具和 containerd 了，命令是:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
```

为了避免以 sudo(或管理员)权限运行 Docker，这可能会导致严重的安全问题，你必须使用以下命令将用户添加到 docker 组:

```bash
sudo usermod -aG docker $USER
```

为了使更改生效，退出然后重新登录到你的服务器。

你可以通过发出以下命令来验证一切是否正常:

```bash
docker ps
```

输出中你应该只看到:


```bash
CONTAINER ID IMAGECOMMAND CREATEDSTATUSPORTS
```

太好了!你已经准备好部署容器了。

## 部署 OpenSpeedTest

首先，我将向你展示如何在没有 Let's Encrypt 的情况下部署 OpenSpeedTest。为此，你只需发出以下命令:

```bash
docker run --restart=unless-stopped --name openspeedtest -d -p 3000:3000 -p 3001:3001 openspeedtest/latest
```

给容器足够的时间进行部署(几分钟就可以了)。部署完成后，打开你 LAN 上的网页浏览器，指向 http://SERVER:3000(其中 SERVER 是托管服务器的 IP 地址)。你应该会看到 OpenSpeedTest 界面，在那里你可以点击“开始”(图 1)来运行速度测试。


![](https://cdn.thenewstack.io/media/2023/11/99f62812-ost1.jpg)

*图 1:OpenSpeedTest 已准备好测试你的网络速度。*

你也可以使用 HTTPS(所以你的流量被加密)通过地址 https://SERVER:3001 访问(其中 SERVER 是托管服务器的 IP 地址)。


## 部署包括 Let's Encrypt 支持的 OpenSpeedTest

如果你更喜欢使用免费的 Let's Encrypt SSL 支持部署容器，那么你需要以下内容:

- 一个面向公众的 IPv4 或 IPv6 地址。
- 解析到托管服务器 IP 地址的域名。
- 一个电子邮件 ID。

完成这些准备工作后，使用 Let's Encrypt SSL 支持部署 OpenSpeedTest 的命令是:

```bash
docker run -e ENABLE_LETSENCRYPT=True -e DOMAIN_NAME=yourdomain -e USER_EMAIL=youremail --restart=unless-stopped --name openspeedtest -d -p 80:3000 -p 443:3001 openspeedtest/latest
```

其中 yourdomain 是指向托管服务器的域名，youremail 是你要用作 ID 的电子邮件地址。

当容器成功部署后，在网页浏览器中指向 https://SERVER:443(其中 SERVER 是托管服务器的域名)。你应该会看到与上述相同的页面(图 1 中所示)。

这就是部署自己的 LAN 速度测试工具的全部内容。使用 OpenSpeedTest，你可以轻松测试 LAN 的速度，这可以大大帮助调试你正在构建的应用程序和服务的任何问题。

即使你没有忙着构建应用程序或服务，该工具也可用于测试基本的 LAN 网络速度或帮助你调试以查看 LAN 是否正常响应。


