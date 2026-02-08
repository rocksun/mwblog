<!--
title: Dockhand免费工具，Docker容器管理轻松搞定
cover: https://cdn.thenewstack.io/media/2026/01/1d93644a-tsd-studio-adj7_snhwpc-unsplash.jpg
summary: Dockhand是一款功能强大、易用的Docker容器管理器，可监控、部署、故障排除容器。适合家庭实验室，比Portainer更轻便。
-->

Dockhand是一款功能强大、易用的Docker容器管理器，可监控、部署、故障排除容器。适合家庭实验室，比Portainer更轻便。

> 译自：[Free Dockhand Tool Simplifies Docker Container Management](https://thenewstack.io/free-dockhand-tool-simplifies-docker-container-management/)
> 
> 作者：Jack Wallen

你是否运行了太多的[Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) [容器](https://thenewstack.io/introduction-to-containers/)？快速检查了一下我的家庭实验室，仅一台服务器就运行着10个[Docker 容器](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)。我如何管理它们，更不用说只是跟踪哪个是哪个了？

我可以部署 [Portainer](https://thenewstack.io/build-and-use-a-custom-image-with-portainer/)，但目前来说那有点大材小用。此外，Portainer 现在更像是一个企业级应用程序，所以在家庭实验室、开发环境或小型企业中使用它并不是那么实用。

这就是像 [Dockhand](https://dockhand.pro/) 这样的应用程序发挥作用的地方。

Dockhand 是一款功能强大、易于使用的容器管理器/监控器，对家庭实验室免费使用，我发现它对于跟踪我的容器来说是不可或缺的。使用 Dockhand，我可以查看日志、访问 shell、查看堆栈、镜像、卷、网络、注册表、活动和计划。我可以停止、暂停、重启、编辑和删除容器，创建健康检查，检查并应用更新等等。

你甚至可以创建和部署容器！

一旦你开始使用 Dockhand，你会想知道没有它你是怎么过来的。事实上，我发现使用 Dockhand 时，我能对 Docker 容器做更多事情。这个应用程序简直简化了一切。

但你如何部署和使用 Dockhand 呢？

很简单，就是这样。

让我来给你展示。

## 部署 Dockhand

不言而喻，你需要一个支持 Docker 的平台。你还需要一些正在运行的容器，我假设你已经有了；否则，你为什么要一个监控它们的平台呢？

在你的宿主平台上部署 Dockhand 就像运行下面这个简单的命令一样：

这段文字包含隐藏或双向 Unicode 字符，其解释或编译方式可能与此处显示的不同。要查看，请在显示隐藏 Unicode 字符的编辑器中打开文件。
[了解更多关于双向 Unicode 字符的信息](https://github.co/hiddenchars)

```bash
docker run -d \
  --name dockhand \
  --restart unless-stopped \
  -p 3000:3000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v dockhand_data:/app/data \
  fnsys/dockhand:latest
```

给容器一点时间启动。几分钟后，打开网络浏览器并指向

[http://SERVER:3000](http://server:3000)

（其中 SERVER 是你的宿主服务器的 IP 地址）。你应该会看到一个空的仪表盘。我们接下来需要做的是配置你的第一个环境。

## 添加环境

我们将首先添加本地环境。为此，从仪表盘中点击“添加环境”（**图 1**）。

[![](https://cdn.thenewstack.io/media/2026/01/395dfa37-dockhand1.jpg)](https://cdn.thenewstack.io/media/2026/01/395dfa37-dockhand1.jpg)

**图 1**：你的 Dockhand 仪表盘让你快速访问你的环境和其他功能。

在弹出的窗口中（**图 2**），你只需为环境命名并点击“添加”即可。

[![](https://cdn.thenewstack.io/media/2026/01/19f5b155-dockhand2.jpg)](https://cdn.thenewstack.io/media/2026/01/19f5b155-dockhand2.jpg)

**图 2**：我们在这里添加一个本地环境。

添加环境后，你应该会在仪表盘中看到它。

## 使用仪表盘

点击侧边栏的仪表盘图标，然后点击你刚刚创建的环境。现在你应该会看到所有正在运行的 Docker 服务列表（**图 3**）。

[![](https://cdn.thenewstack.io/media/2026/01/4ee592be-dockhand3.jpg)](https://cdn.thenewstack.io/media/2026/01/4ee592be-dockhand3.jpg)

**图 3**：我运行着几个容器。

假设你想在这个本地环境中创建一个新容器。为此，点击顶部的“创建”。在弹出的窗口中（**图 4**），输入你想要拉取的镜像名称，然后点击“拉取”。

[![](https://cdn.thenewstack.io/media/2026/01/84785b7f-dockhand4.jpg)](https://cdn.thenewstack.io/media/2026/01/84785b7f-dockhand4.jpg)

**图 4**：如果你还没有拉取镜像，你需要在那里进行。

我将拉取最新的 Vaultwarden 镜像 (vaultwarden/server:latest)。完成之后，Dockhand 会自动切换到“容器”选项卡，你可以在那里开始构建你的新容器（**图 5**）。

[![](https://cdn.thenewstack.io/media/2026/01/f018396f-dockhand5.jpg)](https://cdn.thenewstack.io/media/2026/01/f018396f-dockhand5.jpg)

**图 5**：我们将部署一个 Vaultwarden 容器。

你需要的信息如下：

* 名称：vaultwarden
* 卷映射：宿主路径 – /vw-data/ 和容器路径 – :/data/
* 端口：宿主 – 443 容器 – 443（Vaultwarden 必须使用 SSL）

当然，你需要根据自己的需求填写。此外，还要记住。

当你完成填写容器所需信息后，点击“创建容器”。你的容器应该会显示为正在运行。

真的就是这么简单。

## 容器故障排除

假设你有一个容器出了问题。你能做什么？借助 Dockhand，你可以进行故障排除。

例如，我有一个 [GitLab](https://about.gitlab.com/?utm_content=inline+mention) 容器失败了。要找出发生了什么，从容器列表中点击有问题的容器，你会看到一个“日志”选项卡。点击该选项卡以显示任何已记录的信息（**图 6**）。

[![](https://cdn.thenewstack.io/media/2026/01/fec164ad-dockhand6.jpg)](https://cdn.thenewstack.io/media/2026/01/fec164ad-dockhand6.jpg)

**图 6**：我的 GitLab 容器表现异常。

日志将设置为自动滚动。我发现下载日志文件可以更容易地梳理信息。为此，点击右上角附近的向下箭头（**图 7**）。

[![](https://cdn.thenewstack.io/media/2026/01/cb19ec90-dockhand7.jpg)](https://cdn.thenewstack.io/media/2026/01/cb19ec90-dockhand7.jpg)

**图 7**：我失败的 GitLab 容器的运行日志。

日志将是一个 .txt 文件，你可以在你的机器上打开它并查阅，以排除容器故障。当然，你需要知道如何阅读 Docker 日志文件才能充分利用此功能。

你还可以查看概览选项卡，它会显示任何错误代码。在我的案例中，我看到了退出码 137，这表明容器由于内存不足（OOM）或接收到终止信号而被终止。

越来越接近真相了。

如你所见，Dockhand 非常方便。如果你正在寻找一种轻松管理容器的方法，我强烈推荐你尝试一下这个系统，看看它是否能简化你家庭实验室或小型企业中运行容器的管理。