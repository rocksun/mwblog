你怎么屏蔽广告？大多数人会在电脑上安装各种各样的广告拦截软件，或者添加浏览器扩展来完成这项任务。

无论你选择哪种方式，屏蔽广告都可以帮助你的网络浏览器避免加载可能消耗过多系统资源，甚至可能向你的系统注入恶意代码的广告。我曾遇到过单个广告拖慢我的CPU，导致电脑完全停止运行的情况。唯一的解决方法就是强制重启。

在那之后，我一直在想尽一切办法避免再次发生类似情况。起初，我考虑过使用浏览器扩展，但我意识到我必须在我家网络上使用的每台台式机和笔记本电脑上的每个浏览器上都安装扩展。如果你的局域网只连接了几台机器，这当然没问题。但如果你的机器数量更多呢？

你可能需要考虑像 Pi-Hole 这样的应用程序。

[Pi-Hole](https://pi-hole.net/) 是一个流行的开源项目，它提供了一个简单易用的解决方案，用于屏蔽互联网上的广告和跟踪器。Pi-Hole 不以单台计算机为基础工作，而是实现全网络范围的功能。它的名字来源于数学常数圆周率 (π)，它代表圆的周长与直径之比。

它的工作原理很简单：首先，你部署/安装 Pi-Hole，然后配置每台计算机使用 Pi-Hole 作为其 DNS 服务器。就是这样。

Pi-Hole 提供全网络保护、屏蔽应用程序内广告的能力、提高网络性能（因为广告通常会降低速度），以及一个用于统计监控的基于网络的界面。Pi-Hole 还包括一个内置的 DHCP 服务器，以便对你的网络进行更精细的控制。

现在，在我们继续之前，我想提一下。让 Pi-Hole 在你的网络上工作的最佳方法是将你的调制解调器/路由器的 DNS 设置指向 Pi-Hole 服务器。我之所以提到这一点，是因为如果你使用 AT&T Fiber，你无法更改路由器的 DNS 设置。

我曾多次部署和使用 Pi-Hole，每次涉及 AT&T Fiber 时，事情都会变得很棘手。但是，如果你使用的 ISP 允许你更改调制解调器/路由器上的 DNS 地址，那么你应该没问题。

让我们部署 Pi-Hole。

## 安装 Docker

由于我们将 Pi-Hole 部署为 [Docker容器](https://thenewstack.io/docker-containers-that-could-be-essential-for-your-small-business/)，你可能需要先安装 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)。如果你使用的是 macOS 或 Windows，你可以简单地安装 [Docker Desktop](https://www.docker.com/products/docker-desktop/)，它会同时安装必要的 Docker 工具。如果你使用的是 Linux，过程会稍微复杂一些。以下是在 Ubuntu Server 24.04 上的步骤。

第一步是使用以下命令添加所需的 Docker GPG 密钥：

1.  *sudo apt-get update*
2.  *sudo apt-get install ca-certificates curl*
3.  *sudo install -m 0755 -d /etc/apt/keyrings*
4.  *sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc*
5.  *sudo chmod a+r /etc/apt/keyrings/docker.asc*

接下来，使用以下命令添加官方 Docker 存储库：

*echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo “${UBUNTU\_CODENAME:-$VERSION\_CODENAME}”) stable” | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null*

使用以下命令更新并安装 Docker：

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

然后你需要将你的用户添加到 Docker 组（这样你就可以在不使用 sudo 的情况下管理容器，这可能会导致安全问题），使用以下命令：

```
sudo usermod -aG docker $USER
```

注销并重新登录，以便更改生效。

使用以下命令验证你是否可以使用 Docker：

```
docker ps -a
```

你应该看到一个空列表，没有任何错误。

## 部署 Pi-Hole

安装 Docker 后，我们终于可以部署 Pi-Hole 了。有几点需要注意：

你需要确保将任何外部端口（冒号字符左侧的那些）更改为可用的端口。你还需要将 webserver\_api\_password (PASSWORD) 更改为强大且唯一的密码。

考虑到这一点，此操作的 docker run 命令是：

```
docker run --name pihole -p 54:53/tcp -p 54:53/udp -p 8081:80/tcp -p 443:443/tcp -e TZ=America/Kentucky/Louisville -e FTLCONF_webserver_api_password="PASSWORD" -e FTLCONF_dns_listeningMode=all -v ./etc-pihole:/etc/pihole -v ./etc-dnsmasq.d:/etc/dnsmasq.d --cap-add NET_ADMIN -d --restart unless-stopped pihole/pihole:latest
```

你需要给容器一两分钟时间来部署。一旦容器被列为“healthy”（使用命令 *docker ps -a*），你就应该可以使用了。

## 访问 Pi-Hole

你会希望能够访问你的 Pi-Hole 控制面板，这可以通过将连接到你的局域网的浏览器指向 http://SERVER:PORT/admin/ 来完成（其中 SERVER 是主机服务器的 IP 地址，PORT 是你在 docker run 命令中配置的外部端口）。

你将看到一个登录页面，你需要输入你在 docker run 命令中为 *webserver\_api\_password* 配置的密码。

登录后，你将看到 Pi-Hole 控制面板（**图 1**）。

![](https://cdn.thenewstack.io/media/2026/03/73ca6ce1-screenshot-2026-03-16-at-12.13.48-pm.png)

**图 1:** 一个新部署的 Pi-Hole 实例已准备就绪。

## 配置你的机器使用 Pi-Hole

有两种方法可以配置你网络上的计算机使用 Pi-Hole。更复杂的方法是配置每台机器使用 Pi-Hole 服务器地址作为其 DNS 地址。

第二种方法允许你一次性配置 DNS。为此，你必须访问你的 ISP 调制解调器/路由器，然后将路由器的 DNS 配置为使用 Pi-Hole IP 地址。完成此操作后，你需要禁用 ISP 调制解调器/路由器上的 DHCP，并在 Pi-Hole 服务器上启用 DHCP。

要在你的 Pi-Hole 服务器上启用 DHCP，请转到“设置”>“DHCP”（在 Pi-Hole 基于网络的 GUI 中），启用 DHCP 服务器，配置要分发的 IP 地址范围，然后配置与你的调制解调器/路由器关联的路由器/网关地址（**图 2**）。

![](https://cdn.thenewstack.io/media/2026/03/ed63edb2-screenshot-2026-03-16-at-12.17.49-pm.png)

**图 2:** 使用 Pi-Hole 提供 DHCP 地址是更便捷的途径。

然后，你可以重新启动你的机器，或者让它们续订 IP 地址的 DHCP 地址租约，这些机器将开始使用 Pi-Hole 的 DNS 地址，这也意味着它们受到了广告的保护。