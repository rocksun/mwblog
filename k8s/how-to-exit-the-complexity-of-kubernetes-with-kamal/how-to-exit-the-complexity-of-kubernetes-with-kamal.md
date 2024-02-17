<!--
title: 利用Kamal摆脱Kubernetes的复杂性
cover: https://cdn.thenewstack.io/media/2024/02/bd254e29-ines-a-tgs0thmk4eg-unsplash-1024x683.jpg
-->

我们来介绍一下 Kamal，它是基于 Docker 实现容器部署的 Capistrano。相比于 Kubernetes 或 Docker Swarm，它提供了更简单的替代方案。

> 译自 [How to Exit the Complexity of Kubernetes with Kamal](https://thenewstack.io/how-to-exit-the-complexity-of-kubernetes-with-kamal/)，作者 David Eastman。

最近我写了一篇关于 [Capistrano](https://yylives.cc/2023/10/26/why-capistrano-got-usurped-by-docker-and-then-kubernetes/) 的文章，没想到会再次提及它，因为它是早期应用部署历史的遗迹。我没意识到 Capistrano 是由 37Signals 公司的工程师为他们的主要产品 Basecamp 编写的。这是 David Heinemeier Hansson 的公司。

DHH（他以缩写而闻名）去年宣布出于纯粹的经济原因[离开了云](https://thenewstack.io/merchants-of-complexity-why-37signals-abandoned-the-cloud/)。如果你有能力在自己管理的机架上运行软件（就像以前每个人都不得不做的那样），显然可能比使用亚马逊 AWS 更便宜，特别是如果你有固定的需求。显然，当他们诱使人们加入他们的平台时，云服务提供商看起来比后来价格上涨时更具吸引力。

亚马逊高度创新的服务提供方式仍然是留在云上的一个很好的理由。除此之外，每个组织都必须根据自己的情况[进行权衡](https://world.hey.com/dhh/we-stand-to-save-7m-over-five-years-from-our-cloud-exit-53996caa) —— 云并不适合许多用例。但必须说的是，尽管硬件变得更便宜了，DHH 是一种非常特殊的技术导向型领导者。

本文的其余部分将介绍 Capistrano 的替代品 [Kamal](https://kamal-deploy.org/)。它基本上是通过 [Docker](https://www.docker.com/?utm_content=inline-mention) **用于容器的 Capistrano**。可以说，它是 [Kubernetes 或 Docker Swarm](https://thenewstack.io/kubernetes-vs-docker-swarm-whats-the-difference/) 的一个更简单的选择。Kamal 提供“零停机部署、滚动重启、资源桥接、远程构建以及你在生产环境中使用 Docker 部署和管理 Web 应用所需的一切。” 因此，它通过 ssh 命令部署内容。但它的目标是尽可能对部署目标保持中立。

## Docker 回顾

作为一个快速的记忆回顾，Docker 使用 Dockerfile 构建镜像，并在容器上运行这些镜像 —— 在这些容器上，你的应用程序或其部分以隔离的方式运行：

![Zoom](https://cdn.thenewstack.io/media/2024/02/3ccbe32e-untitled-1024x320.png)

*构建 Docker 镜像*

这是一个示例 Dockerfile:


```Dockerfile
FROM ubuntu:18.04 
# Install nginx and curl 
RUN apt-get update && 
apt-get upgrade -y && 
apt-get install -y nginx curl && 
rm -rf /var/lib/apt/lists/*
```

因此，这个 Dockerfile 使用了已知 Ubuntu 版本的基础镜像，然后运行 Ubuntu 的更新和升级，然后安装 nginx 并进行清理。

我们可能需要记住的另一件事是，Docker Hub 是容器镜像的官方仓库。如果我登录到 hub.docker.com，我仍然可以看到一些旧的镜像 —— 就像在 GitHub 上的仓库一样。

Kamal（是的，又一个[模糊的海事起源名字](https://exploration.marinersmuseum.org/object/kamal/)）使用了 Ruby，这是 37Signals 的内部语言，我偶尔还会涉猎一下。更明确地说，我在这里的第一篇文章是关于 [Sinatra](https://thenewstack.io/ruby-devs-try-sinatra-before-moving-up-to-ruby-on-rails/) 的 —— 你可以用它来搭建一个 Ruby 环境。

在我的 Mac 上启动 [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 后，我会检查一下我的内置 ruby 的版本：

![Zoom](https://cdn.thenewstack.io/media/2024/02/158df979-untitled-1-1024x354.png)

然后我可以安装 kamal gem：

```bash
> gem install kamal
```

然后启动它：

![Zoom](https://cdn.thenewstack.io/media/2024/02/e42ac6d2-untitled-2.png)

我们没有任何需要部署的东西，也没有任何需要部署的地方，所以我们只是看一下 Kamal 是如何看待世界的。但这是来自 37Signals 的，所以你可以想象他们部署一个 **Rails** 应用程序。因此，有关数据库、负载均衡器等方面都有所提及。

`deploy.yml` 文件保存了各种东西的目标位置，而 .env 文件将保存我们可能不会提交到源代码控制的“机密”信息。因此，这个 .env 文件会按名称添加到各种 .ignore 文件中。

让我们首先看一下创建的 deploy 文件。在这个 yaml 模板中，简单的组织层次结构很容易阅读，我们将检查它需要哪些类型的东西：

```yaml
>cat config/deploy.yml 
 
# Name of your application. Used to uniquely configure containers. service: 
my-app 
# Name of the container image. 
image: user/my-app 
 
# Deploy to these servers. 
servers: 
 - 192.168.0.1 
 
# Credentials for your image host. 
registry: 
 # Specify the registry server, if you're not using Docker Hub 
 # server: registry.digitalocean.com / ghcr.io / ... username: 
 my-user 
 
 # Always use an access token rather than real password when possible. 
 password: 
  - KAMAL_REGISTRY_PASSWORD 
 
# Inject ENV variables into containers (secrets come from .env). 
# Remember to run `kamal env push` after making changes! 
# env: 
#  clear: 
#   DB_HOST: 192.168.0.2 
#  secret: 
#   - RAILS_MASTER_KEY
```

因此，您将为您的服务器设定目的地，并指定要部署的镜像名称。镜像可能来自 Docker Hub，这是“镜像主机”，因此您需要存储凭据。请注意，env 变量会以可编辑的方式或明文形式注入到容器中。

在 deploy.yml 的稍后部分，我们看到了更多示例部分：

```yaml
# Use accessory services (secrets come from .env).
# accessories:
#   db:
#     image: mysql:8.0
#     host: 192.168.0.2
#     port: 3306
#     env:
#       clear:
#         MYSQL_ROOT_HOST: '%'
#       secret:
#         - MYSQL_ROOT_PASSWORD
#     files:
#       - config/mysql/production.cnf:/etc/mysql/my.cnf
#       - db/production.sql:/docker-entrypoint-initdb.d/setup.sql
#     directories:
#       - data:/var/lib/mysql
#   redis:
#     image: redis:7.0
#     host: 192.168.0.2
#     port: 6379
#     directories:
#       - data:/data
```

“accessory service”一词指的是长期依赖的服务，比如数据库。它们定义了不同的镜像和主机。例如，[Traefik](https://thenewstack.io/traefik-a-dynamic-reverse-proxy-for-kubernetes-and-microservices/) 反向代理还有额外的设置部分。

.env 文件是您放置适当“密钥”的地方：

```shell
> cat .env

KAMAL_REGISTRY_PASSWORD=change-this
RAILS_MASTER_KEY=another-env
```

这些文件可以用于引用 1Password 或其他集中式存储。如果我们打算使用数据库，上面的内容将缺少 MYSQL 密码。如果您更改了这些内容，需要明确使用 `kamal env push` 将其推送到系统中。实际上，在部署之前，这些内容是必需的。在 DevOps 环境中，不是每个工程师都应该可以访问这些文件，但每个人都需要知道它的作用。

然后，我们使用 `kamal setup` 启动系统。如预期的那样，如果我现在执行此操作，系统会迅速告诉我没有内容可以交流：

![](https://cdn.thenewstack.io/media/2024/02/b1d89ca6-untitled-3-1024x128.png)

那么，Kamal 如何处理所有指定和可用的服务器呢？

连接到服务器后，如果需要，它将安装 Docker 和 curl。然后，登录到镜像注册表，它将在本地构建镜像，然后将其推送到注册表中。接下来，它将从目标服务器中拉取镜像。在推送环境变量之后，它将使用当前版本的应用程序启动一个新容器，并停止旧容器。

如果您对应用程序进行了更改，那么在初始设置之后，`kamal deploy` 将更新您的系统。随后，您可以使用 `kamal redeploy`，它将跳过诸如注册表登录等步骤，因此速度更快。这建立了正常的工作流程。通过保留一些旧的温暖容器镜像，您还可以快速使用有效的镜像目标进行 `kamal rollback`。从这里，DevOps 工程师可以识别出熟悉的模式。

通过向社区提供这个工具，37Signals 不仅指明了一种从云计算中实际退出的方法，还提供了一种轻松更换服务提供商的方法。他们还在摆脱相对复杂的 Kubernetes。在考虑您的计算策略时，如果您的发展方向是这样的，了解有关经济和技术退出方法的工作示例，那将是件好事。