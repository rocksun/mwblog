使用 [Docker 容器](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/) 更具挑战性的方面之一是故障排除。除非你是这方面的行家，否则仅仅是找出 *从何处* 开始故障排除之旅就可能是一次令人头疼的经历。

当然，你可以从命令行进行故障排除，但当你处理大量容器时，这并不实用。毕竟，你不想最终 24/7 工作，对吧？

我不这么认为。

考虑到这一点，你能做些什么来让 Docker 的故障排除更容易一些呢？你能做的最重要的事情是查看日志。不幸的是，这又是另一项会挑战你的 [Docker](https://thenewstack.io/docker-launches-hardened-images-intensifying-secure-container-market/) 任务。

幸运的是，有像 [Dozzle](https://dozzle.dev) 这样的工具。

Dozzle 是一个由 Docker-OSS 赞助的开源项目，它作为 Docker 容器的基于网络的日志查看器。Dozzle 具有实时监控、独立和多主机部署、支持带有过滤和搜索功能的文本/JSON/多行日志、交互式终端以及用户友好的 UI。

Dozzle 实际上非常易于部署，使其成为查看 Docker 日志的绝佳选择。

我将向你展示如何在单个主机上部署这个易于使用的 Docker 日志查看工具。你所需要做的就是一台支持 Docker 的机器。你将在包含要监控的容器的机器上部署 Dozzle。

让我们开始吧。

## 安装 Docker

为了不跳过步骤，我想首先向你展示如何安装 Docker。如果你的 Docker 已经运行，请跳到下面的“部署 Dozzle”部分。我将在 [Ubuntu Server](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 24.04 上演示。如果你使用不同的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 发行版，你需要更改安装过程。

### 1. 添加必要的 GPG 密钥

你必须做的第一件事是添加官方 Docker GPG 密钥，这样你才能实际安装软件。执行此操作的命令如下：

```
for p in $(ls /etc/apt/sources.list.d); do sudo rm /etc/apt/sources.list.d/$p; done && sudo apt update
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

### 2. 添加官方 Docker 仓库

接下来，我们需要添加官方 Docker 仓库，这样我们的包管理器就知道在哪里可以找到该软件，操作如下：

```
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```

### 3. 安装 Docker 及其他组件

现在是时候安装 Docker 和其他一些组件了。使用以下命令执行此操作：

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```

### 4. 将你的用户添加到 Docker 组

为了能够在不需要管理员权限的情况下运行 Docker 容器，请使用以下命令将你的用户添加到 Docker 组：
  
注销并重新登录以使更改生效。

```
sudo usermod -aG docker $USER
```

## 部署 Dozzle

现在是时候部署 Dozzle 了。为此，请发出以下命令：
  
请注意端口配置。如果你确定端口 8080 未被占用，则可以使用 8080:8080。在我的情况下，8080 已被占用，所以我不得不使用 8082:8080 进行部署。

```
docker run --name dozzle -d --volume /var/run/docker.sock:/var/run/docker.sock -p 8080:8080 dozzle/dozzle:latest
```

如果你不确定哪些端口正在使用中，你可以发出以下命令：
  

```
sudo ss -ltn 'sport = :8080'
```

如果你看到 8080 列出，你需要使用不同的端口。

几秒钟后，打开网络浏览器并将其指向 http://SERVER:PORT（其中 SERVER 是托管服务器的 IP 地址，PORT 是你用于 Dozzle 的端口）。你将看到 Dozzle 仪表板（**图 1**）。

![](https://cdn.thenewstack.io/media/2026/01/dab88f44-screenshot-2026-01-21-at-1.34.23-pm-scaled.png)

**图 1：** Dozzle 仪表板非常容易理解。

在左侧边栏中，你应该看到你的主机。点击它，将显示每个已部署的容器（**图 2**）。

![](https://cdn.thenewstack.io/media/2026/01/2ac5a146-screenshot-2026-01-21-at-1.05.03-pm-scaled.png)

**图 2：** 我的主机上运行着多个容器。

## 使用 Dozzle 查看日志

在侧边栏中找到你遇到问题的容器并点击它；你将看到该容器收集到的所有日志（**图 3**）。

![](https://cdn.thenewstack.io/media/2026/01/df06f4de-screenshot-2026-01-21-at-1.40.17-pm-scaled.png)

**图 3：** 我的 Open Notebook 容器运行良好，但检查日志仍然是好的。

仔细查看日志，看看是否发现任何异常。如果容器已退出或遇到问题，你应该在这里找到一些有助于你确定问题的信息。

需要记住的一点是，Dozzle 是一个单功能工具——它用于查看日志文件。你无法在此处管理容器，因此如果容器停止或不健康，你将不得不回到命令行进行管理，或者使用像 [Docker Desktop](https://thenewstack.io/docker-desktop-the-easiest-way-to-debug-docker-containers/)、[Rancher](https://thenewstack.io/suse-upgrades-its-rancher-kubernetes-management-family/) 或 [Portainer](https://thenewstack.io/catching-up-with-the-founder-and-ceo-of-portainer/) 这样的工具。

Dozzle 是一个如此易于部署和使用的系统，因此将其添加到你的 Docker 工具包中是理所当然的。试一试，看看你是否觉得它无价。