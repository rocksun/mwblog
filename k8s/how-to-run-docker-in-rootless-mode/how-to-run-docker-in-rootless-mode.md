
<!--
title: 如何在Rootless模式下运行Docker
cover: https://cdn.thenewstack.io/media/2022/03/14e8787f-flower-gf47577b05_640.jpg
summary: 告别sudo！无需Root权限也能玩转Docker？本文教你如何在无Root模式下安装Docker，利用用户命名空间隔离权限，保障安全。但需注意端口限制和 cgroup v2 依赖。更有uidmap安装、NGINX测试等干货，更有Podman等替代方案，云原生安全再升级！
-->

告别`sudo`！无需Root权限也能玩转Docker？本文教你如何在无Root模式下安装Docker，利用用户命名空间隔离权限，保障安全。但需注意端口限制和`cgroup v2`依赖。更有`uidmap`安装、`NGINX`测试等干货，更有`Podman`等替代方案，云原生安全再升级！

> 译自：[How to Run Docker in Rootless Mode](https://thenewstack.io/how-to-run-docker-in-rootless-mode/)
> 
> 作者：Jack Wallen

虽然可以在没有 root 权限的情况下部署 [Docker](https://www.docker.io/) 容器，但这并不一定意味着它完全是无 root 的。这是因为堆栈中还有其他组件（例如 runc、containerd 和 dockerd）确实需要 root 权限才能运行。这可能会因权限提升攻击而导致安全问题。

当然，您可以将您的用户添加到 docker 组并在没有 sudo 帮助的情况下运行 docker 部署命令，但这实际上并没有解决问题。还有其他运行 docker 的方法看起来不错，但最终，它们与使用 sudo 权限运行 docker 一样危险。

那么，您该怎么办？您可以始终选择无 root 模式。

## 无 Root 模式的工作原理

实际上，运行无 root Docker 利用了用户命名空间。该子系统提供跨进程的权限隔离和用户身份隔离。自 3.8 版本以来，Linux 内核就提供了此功能，并且可以与 docker 一起使用以映射一系列用户 ID，以便最内层命名空间中的 root 用户映射到父命名空间中的非特权范围。

Docker 已经能够利用用户命名空间功能一段时间了。这是使用 `--userns-remap` 选项完成的。唯一的问题是运行时引擎仍然以 root 身份运行，因此它并没有解决我们的问题。

这就是无 root docker 发挥作用的地方。

## 局限性

### 特权端口访问

不幸的是，无 root 模式并不完美。第一个问题是无 root docker 将无法访问特权端口，即任何低于 1024 的端口。这意味着您需要记住将 [您的容器](https://thenewstack.io/introduction-to-containers/) 暴露给 1024 以上的端口，否则它们将无法运行。

### 容器的资源限制

另一个问题是，只有在使用 cgroup v2 和 systemd 运行时，才支持使用诸如 –cpus、–memory 和 –pids-limit 之类的选项来限制资源。

您可能遇到的其他限制包括：

- 不支持 AppArmor、checkpoint、overlay network 和 SCTP 端口暴露。
- 存储驱动程序支持有限（仅支持 overlay2、fuse-overlayfs 和 vfs 存储驱动程序）。
- 不支持 –net-host。

综上所述，我们如何安装 docker 以便它可以在无 root 模式下运行？实际上非常简单。让我来告诉你怎么做。

我将在我首选的服务器 Ubuntu Server 20.04 上进行演示，但您几乎可以在任何 Linux 发行版上执行此操作。唯一的区别是为唯一依赖项运行的安装命令。

## 安装唯一的依赖项

我们必须做的第一件事是为此设置安装唯一的依赖项。该依赖项是 uidmap，它处理系统的用户命名空间映射。要安装 uidmap，请登录到您的服务器并发出以下命令：

```bash
sudo apt-get install uidmap -y
```

这就是依赖项的全部内容。

## 安装 Docker

接下来，我们安装 Docker。我们不想使用标准存储库中找到的版本，因为它无法在无 root 模式下成功运行。相反，我们需要下载一个特殊的安装脚本，该脚本将安装无 root Docker。

**下载并运行 Docker 无 root 安装程序**

我们可以使用单个命令下载并安装无 root 版本的 docker：

```bash
curl -fsSL https://get.docker.com/rootless | sh
```

**添加必要的变量**

安装完成后，您需要将一对环境变量添加到 .bashrc。使用以下命令打开文件：

```bash
nano ~/.bashrc
```

在该文件中，将以下行添加到末尾：

```bash
export PATH=/home/jack/bin:$PATH
export DOCKER_HOST=unix:///run/user/1000/docker.sock
```

注意：请务必添加您的特定用户 ID。在上面的代码中，我的 ID 是 1000。要查找您的用户 ID，请发出以下命令：

```bash
id
```

您需要添加 *uid=* 后面的数字，如下所示：

```bash
export DOCKER_HOST=unix:///run/user/ID/docker.sock
```

其中 *ID* 是您的用户 ID 号。
保存并关闭文件。

注销并重新登录到服务器（以便更改生效），您就可以测试无 root docker 了。

## 测试无 Root Docker

我们将部署我们值得信赖的 NGINX 容器作为测试。请记住，我们尚未将我们的用户添加到 docker 组。如果这是一个标准的 Docker 安装，那么如果不将我们的用户添加到 docker 组或使用 `sudo` 权限运行部署命令，我们将无法成功部署 NGINX 容器。

**使用 NGINX 测试无 Root Docker**

要测试无 root 模式（以分离模式部署 NGINX），请发出以下命令：

```bash
docker run --name docker-nginx -p 8080:80 -d nginx
```

打开一个 Web 浏览器并将其指向 http://SERVER:8080（其中 SERVER 是您的 Docker 服务器的 IP 地址），您应该会看到 NGINX 欢迎页面。
这个容器的部署未使用 root 用户，因此整个堆栈都没有那些提升的权限。

**使用 Ubuntu 容器测试无根模式**

您甚至可以部署一个完整的 Linux 容器，并通过如下命令访问它的 bash shell：

```bash
docker run -it ubuntu bash
```

所有这些操作都不需要触及 root 权限。

## 结论

显然，这并不是解决 Docker 容器所有安全问题的完美方案。您甚至可能会发现 [Podman](https://thenewstack.io/deploy-a-pod-on-centos-with-podman/) 是一个更好的解决方案，因为它可以在开箱即用的情况下以无根模式运行。但是对于那些已经投资 Docker，但又希望尽可能提高安全性的用户来说，以无根模式运行 Docker 肯定是一个可行的选择。

尝试一下无根 Docker，看看它是否能稍微缓解您的安全难题。

## 无 root 模式常见问题解答

### 1. 什么是 Docker 无根模式？

答：Docker 无根模式允许您在不需要超级用户权限的情况下运行容器，它利用 Linux 内核提供的命名空间和 cgroups。

### 2. 为什么要使用 Docker 无根模式？

以无根模式运行 Docker 提供了以下几个好处：

**安全性**：降低了潜在的安全风险，因为没有进程以提升的权限运行。

**隔离性**：提高了系统隔离性，因为每个容器都在其自己的用户命名空间中运行。

**灵活性**：允许使用非 root 用户，并避免与现有的基于 root 的应用程序发生冲突。

### 4. 我还需要 Dockerd 吗？

答：是的，您仍然需要一个 docker 守护进程 (dockerd)。您可以按如下方式启动它：

```bash
dockerd-rootless-setuptool.sh install –non-suid
```

此命令以无根模式启动 dockerd。

### 5. 如何运行容器？

答：一旦 Docker 无根模式设置完成，您就可以使用标准的 docker 命令来运行容器，例如：

```bash
docker run -it ubuntu bash
```

### 6. 我可以在无根模式下使用 Docker Compose 吗？

答：是的，您可以在无根模式下使用 Docker Compose。只需确保 Docker 和 Docker Compose 都已安装。

### 7. 网络配置如何？

答：在无根模式下，网络设置与 root 模式不同。默认情况下，*dockerd-rootless-setuptool.sh* 使用 SLIRP4NetNS 为网络配置一个用户特定的网络堆栈。可以通过修改 /home/USER/.local/share/docker/rootless 下的配置文件（其中 USER 是您的用户名）来自定义此设置。

### 8. 我可以与主机共享 Docker 卷吗？

答：是的，但是您需要挂载可以从您的用户命名空间访问的卷。例如，您可以这样做：

```bash
docker run -v /host/data:/container/data ubuntu bash
```

请注意，共享卷的某些功能可能在无根模式下未完全支持。

### 9. 我可以访问 docker system prune 和其他命令吗？

答：并非所有命令都可以在无根模式下直接工作。例如，您不能使用 *docker system prune*，因为它需要访问非 root 用户无法访问的主机内核。

您可以通过使用容器化的 Docker 版本来运行这些命令。