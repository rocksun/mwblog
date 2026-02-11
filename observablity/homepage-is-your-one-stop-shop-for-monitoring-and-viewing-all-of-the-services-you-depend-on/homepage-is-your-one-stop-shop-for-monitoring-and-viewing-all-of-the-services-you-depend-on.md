<!--
title: Homepage 如何简化你的自托管服务监控
cover: https://cdn.thenewstack.io/media/2026/02/09627ea6-allison-saeng-7icarfsxo2y-unsplash.jpg
summary: 本文介绍了Homepage，一个自托管仪表板，用于集中监控本地服务和Docker容器。它详细讲解了如何通过Docker进行安装和基本配置，旨在简化自托管服务的监控流程。
-->

本文介绍了Homepage，一个自托管仪表板，用于集中监控本地服务和Docker容器。它详细讲解了如何通过Docker进行安装和基本配置，旨在简化自托管服务的监控流程。

> 译自：[How Homepage simplifies monitoring your self-hosted services](https://thenewstack.io/homepage-is-your-one-stop-shop-for-monitoring-and-viewing-all-of-the-services-you-depend-on/)
> 
> 作者：Jack Wallen

渐渐地，我一直在迁移到自托管服务，这样我终于可以摆脱对第三方的依赖了。通过将所有内容保留在[我的局域网](https://thenewstack.io/build-your-own-private-cloud-at-home-with-docker/)内，我享有比继续使用云主机更多的安全性和隐私。

问题是，我最终运行了许多不同的服务，我必须通过不同的IP地址和端口来访问它们。但是，如果我想简单（快速）地查看这些服务的状态，看看统计数据，甚至确认我的[Docker 容器](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)仍然按预期运行呢？我需要为每个服务打开一个浏览器标签页来验证一切是否正常吗？

我可以这样做。

或者，我可以使用一个单一的仪表板，从一个集中位置获取我需要的所有信息。[Homepage](https://gethomepage.dev/)并非旨在取代你使用的所有应用和服务，而是让你更容易地检查这些服务，甚至添加你可能需要/使用的第三方服务的链接。

你无需为每个服务打开一个网页浏览器标签页，只需打开Homepage即可大致了解你的局域网服务/应用中正在发生的事情。

我将向你展示如何部署和配置Homepage，以便你可以简化你的监控工作流程。

![](https://cdn.thenewstack.io/media/2026/02/7382dcff-homepage.jpg)

## 安装

感谢[Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，安装Homepage实际上相当容易。当然，你需要先安装Docker，所以我会先带你完成这个过程。

### 安装Docker

以下是安装Docker的步骤：

1. **添加必要的 GPG 密钥**

在你安装必要的 Docker 存储库之前，你必须首先添加官方的 Docker GPG 密钥。执行此操作的命令是：

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

2. **添加官方 Docker 存储库**

现在，我们可以使用以下命令添加官方 Docker 存储库：

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

3. **安装 Docker**

现在，我们使用以下命令安装必要的软件：

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

4. **将您的用户添加到 Docker 用户组**

为了在不要求管理员权限（这可能导致安全问题）的情况下运行 Docker 容器，请使用以下命令将您的用户添加到 docker 用户组：

```
sudo usermod -aG docker $USER
```

注销并重新登录以使更改生效。

### 安装 Homepage

安装 Docker 后，你现在可以安装 Homepage 了。安装 Homepage 有两种方法：使用 docker-compose 或 docker run。我将向你展示这两种方法。

要使用 docker-compose 安装 Homepage，你必须创建一个 docker-compose.yml 文件。在此之前，我们先使用以下命令在你的主目录中创建一个目录：

```
mkdir -p ~/docker/homepage
```

使用以下命令进入新目录：

```
cd ~/docker/homepage
```

使用以下命令创建 yml 文件：

```
nano docker-compose.yml
```

在该文件中，粘贴以下内容：

```
services:
  homepage:
    image: ghcr.io/gethomepage/homepage:latest
    container_name: homepage
    ports:
      - 3000:3000
    volumes:
      - /path/to/config:/app/config # Make sure your local config directory exists
      - /var/run/docker.sock:/var/run/docker.sock:ro # (optional) For docker integrations
    environment:
      HOMEPAGE_ALLOWED_HOSTS: gethomepage.dev # required, may need port. See gethomepage.dev/installation/#homepage_allowed_hosts
```

在保存此文件之前，你需要进行以下更改：

*   ports – 如果你的托管服务器上已经使用了端口 3000，请将其更改为类似 3001:3000 的端口
*   volumes – 将 /path/to/config 更改为 /home/USER/docker/homepage（其中 USER 是你的用户名）。
*   HOMEPAGE_ALLOWED_HOSTS – 将 gethomepage.dev 更改为你的托管服务器的 IP 地址和端口（例如 http://192.168.1.26:3001）。

保存并关闭文件。然后你可以使用以下命令部署容器：

```
docker-compose up
```

等待一分钟左右，然后你应该能够通过地址 http://SERVER:PORT 从浏览器访问 Homepage（其中 SERVER 是你的托管服务器的 IP 地址，PORT 是用于该服务的外部端口）。

如果你不想使用 Docker Compose，你可以像这样使用 docker run 命令：

```
docker run -p 3000:3000 -e HOMEPAGE_ALLOWED_HOSTS=gethomepage.dev -v /path/to/config:/app/config -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/gethomepage/homepage:latest
```

对上面的命令进行与你在 docker-compose.yml 文件中相同的更改。

## 自定义 Homepage

我不会详细介绍如何自定义 Homepage，因为你会有特定的需求。不过，我会给你一个入门示例。

如果你进入 ~/docker/homepage 目录，你会找到两个特定的文件：

*   services.yml – 用于配置要监控的服务。
*   settings.yml – 用于配置 Homepage 的基本设置。

如果你想自定义 Homepage 的外观和感觉，打开 settings.yml 文件即可。你可以添加自定义背景图片，甚至控制图片的模糊度。例如，你可以像这样更改 Homepage 的名称并添加背景图片（在 settings.yml 中）：

```
title: My Homepage

background:
  image: /images/yourimagehere.jpg
  blur: sm # sm, "", md, xl... see https://tailwindcss.com/docs/backdrop-blur
  saturate: 50 # 0, 50, 100... see https://tailwindcss.com/docs/backdrop-satura>
  brightness: 50 # 0, 50, 75... see https://tailwindcss.com/docs/backdrop-brigh>
  opacity: 50 # 0-100
```

这里有个诀窍。上面，我将图片配置为在我添加到 docker/homepage 的 images 目录中查找。要使用它，我必须在 docker-compose.yml 文件中声明它，像这样：

```
- /home/USER/docker/homepage/config/images:/app/public/images
```

其中 USER 是你的用户名。

服务在 services.yml 文件中配置。假设你的网络上运行着 UptimeKuma，并且你想：

1.  从 Homepage 内添加一个指向它的链接
2.  添加一个快速 ping 测试以了解它是否正在运行

要做到这一点，你可以为 UptimeKuma 添加一个部分：

```
- Up or Down:
    - Example UptimeKuma:
        description: "UptimeKuma"
        icon: si-uptimekuma -#5CDD8B # icons found here https://simpleicons.org/
        href: http://192.168.1.27:3001/dashboard
        ping: https://192.168.1.27
```

你可以添加任意数量的服务。要了解更多关于如何配置服务的信息，请务必查看官方的[Homepage 服务小部件文档](https://gethomepage.dev/widgets/)。