[返回到扩展容器指南](/community/guides/scaling-docker/)

# 从 Podman 到 Kubernetes：实用集成指南

Podman 是一款轻量级容器引擎，它为管理镜像和容器提供了易于使用的命令行界面。它通常用作 [Docker 的替代品](/community/guides/scaling-docker/podman-vs-docker/)，因为它与 Docker CLI 完全兼容，不包括 Docker Swarm 命令。

但是，Podman 的功能超出了 Docker 兼容性，其中之一就是 Kubernetes 集成（解析和生成 Kubernetes 清单的能力）。此功能提供了额外的便利性和灵活性，使您能够轻松地在 Kubernetes 集群中部署和管理 Podman 工作负载，或将现有工作负载从 Kubernetes 集群无缝传输到 Podman 安装。

本指南旨在演示如何集成 Podman 和 Kubernetes，以高效且实用的方式利用这两种技术的优势。在深入探讨涉及 Kubernetes 的更高级主题和场景之前，我们将对 Pod 进行基本介绍。

在本文结束时，您将清楚地了解如何将 Podman 和 Kubernetes 结合使用，以优化您的容器管理工作流并最大化部署效率。

让我们从 Pod 的概述以及它们在 Podman 中的使用方式开始。

[](/logs?utm_content=upsell&utm_medium=guides&utm_source=community&utm_term=podman-to-kubernetes)

## 先决条件

- 良好的 Linux 命令行技能。
- 具有 Podman 和 Kubernetes 的基本经验。
- 系统上安装了 [Podman 的最新版本](https://podman.io/docs/installation)。
- （可选）系统上安装了 [Docker Engine](https://docs.docker.com/engine/)，用于运行 [minikube](https://minikube.sigs.k8s.io/) 示例。

## 了解 Pod

如您所知，并非所有容器引擎都存在 Pod 的概念。例如，Docker 不支持 Pod。因此，许多工程师不知道 Pod 及其用例，而是更愿意使用单个容器。然而，随着 Kubernetes 的日益普及，许多用户了解和将 Pod 集成到其容器化工作流中已变得至关重要。

在 Kubernetes 中，Pod 表示最小的、最简单的可部署对象，由一个或多个容器组成，这些容器作为一个内聚单元进行管理。Pod 中的容器可以共享网络和存储等资源，同时维护单独的文件系统和进程命名空间，从而确保更严格的安全性和更好的稳定性。

Podman 通过允许用户将容器组织到 Pod 中来符合这一概念。虽然 Kubernetes 和 Podman 的实现有所不同，但将容器作为统一实体进行管理的核心思想保持一致，使 Podman Pod 能够执行类似的任务。

要创建一个新的 Pod，请执行：

```
podman pod create my-first-pod
```

这会输出一个 SHA-256 哈希，唯一标识系统上的 Pod：

```
e22b6a695bd8e808cadd2c39490951aba29c971c7be83eacc643b11a0bdc4ec7
```

您可以发出以下命令以进一步确认 Pod 已成功创建：

```
podman pod ls
```

它会产生类似的输出：

```
POD ID 名称状态创建于基础架构 ID 容器数
e22b6a695bd8 my-first-pod 已创建 23 秒前 131ee0bcd059 1
```

让我们检查每一列：

- POD ID 显示新创建的 Pod 的唯一标识符。仔细检查后，您会注意到它的值对应于 podman pod create 命令生成的 SHA-256 哈希的前 12 个字符。您可以在后续命令和操作中使用此 ID 来区分此 Pod。
- 名称表示新创建的 Pod 的名称。大多数 podman 命令允许您通过名称或 ID 互换引用 Pod。
- 状态表示新创建的 Pod 的状态，可以是以下状态之一：已创建、正在运行、已停止、已退出或已死亡。在这种情况下，状态为已创建，这意味着已创建 Pod 定义，但当前没有容器进程在内部主动运行。
- 创建于仅表示 Pod 创建于多久之前。
- 基础架构 ID 很有趣。它显示了创建 Pod 时使用的基础架构容器的标识符（在本例中为 131ee0bcd059）。基础架构容器允许 Pod 中运行的容器共享各种 Linux 命名空间。默认情况下，Podman 以允许其容器共享 net、uts 和 ipc 命名空间的方式编排 Pod。这允许 Pod 中的容器相互通信并重新使用某些资源。
## 容器数

显示附加到 Pod 的容器数。Pod 始终默认附加 1 个容器（基础设施容器），即使其进程不会自动启动，如您稍后将看到的。

要检查现有容器，请键入：

```
podman container ps -a
```

输出显示您刚刚创建的 Pod 的基础设施容器：

| 容器 ID | 镜像 | 命令 | 创建状态 | 端口 | 名称 |
|---|---|---|---|---|---|
| 131ee0bcd059 | localhost/podman-pause:4.3.1-0 | | 51 秒前已创建 | | e22b6a695bd8-infra |

**注意**

* 容器 ID 如何匹配创建的 Pod 的基础设施 ID，以及容器名称的前 12 个字符 `e22b6a695bd8-infra` 如何匹配 Pod ID。这些关系始终成立，并且可以非常轻松地识别系统上每个 Pod 的基础设施容器，在该系统上可能同时运行多个 Pod。
* 当您创建一个新的空 Pod 时，基础设施容器已准备好启动，但实际上并未启动任何进程。因此，容器最初显示为 `已创建`，而不是 `正在运行`，并且 `-a` 标志对于 `podman container ps` 命令显示它而言是必需的。
* 此时，也未为 Pod 容器建立任何命名空间。键入以下命令进行验证：

```
lsns -T
```

您将看到类似的输出：

| NS 类型 | NPROCS | PID | 用户 | 命令 |
|---|---|---|---|---|
| 用户 | 4 | 98786 | marin | /lib/systemd/systemd --user |
| ├─时间 | 5 | 98786 | marin | /lib/systemd/systemd --user |
| ├─cgroup | 5 | 98786 | marin | /lib/systemd/systemd --user |
| ├─pid | 5 | 98786 | marin | /lib/systemd/systemd --user |
| ├─uts | 5 | 98786 | marin | /lib/systemd/systemd --user |
| ├─ipc | 5 | 98786 | marin | /lib/systemd/systemd --user |
| ├─net | 5 | 98786 | marin | /lib/systemd/systemd --user |
| ├─mnt | 4 | 98786 | marin | /lib/systemd/systemd --user |
| ├─mnt | 0 | root | | |
| └─用户 | 1 | 99106 | marin | catatonit -P |
| └─mnt | 1 | 99106 | marin | catatonit -P |

`/lib/systemd/systemd --user` 行显示当您登录到给定 Linux 机器上的用户帐户时启动的服务管理器使用的命名空间。另一方面，`catatonit -P` 行显示 Podman 在您以无根模式与之交互时维护的全局暂停进程所持有的命名空间。我们不会深入探讨这些命名空间最初存在的原因，但了解它们的存在以及这是您在新的 Pod 执行任何实际工作之前通常会观察到的标准 `lsns` 输出非常重要。

让我们向新创建的 Pod 添加一个容器，看看会发生什么。对于此实验，我们将使用 Docker Hub 中的 [hashicorp/http-echo](https://hub.docker.com/r/hashicorp/http-echo) 镜像（http-echo 是一个小型内存内 Web 服务器，通常用于测试目的）：

```
podman run -d --pod my-first-pod docker.io/hashicorp/http-echo:1.0.0
```

再次列出容器：

```
podman container ps
```

这一次，基础设施容器和 `http-echo` 容器似乎都 `正在运行`：

| 容器 ID | 镜像 | 命令 | 创建状态 | 端口 | 名称 |
|---|---|---|---|---|---|
| 131ee0bcd059 | localhost/podman-pause:4.3.1-0 | | 6 分钟前 | | e22b6a695bd8-infra |
| c57f4d354eb4 | docker.io/hashicorp/http-echo:1.0.0 | | 22 秒前 | | gallant_wescoff |

Pod 也被列为 `正在运行`：

```
podman pod ps
```

| Pod ID | 名称 | 状态 | 创建 | 基础设施 ID | 容器数 |
|---|---|---|---|---|---|
| e22b6a695bd8 | my-first-pod | 正在运行 | 7 分钟前 | 131ee0bcd059 | 2 |

如果您再次执行 `lsns`，您会注意到一些更改：

```
lsns -T
```

| NS 类型 | NPROCS | PID | 用户 | 命令 |
|---|---|---|---|---|
| 用户 | 4 | 98786 | marin | /lib/systemd/systemd --user |
| ├─时间 | 10 | 98786 | marin | /lib/systemd/systemd --user |
| ├─cgroup | 8 | 98786 | marin | /lib/systemd/systemd --user |
| ├─pid | 8 | 98786 | marin | /lib/systemd/systemd --user |
| ├─uts | 8 | 98786 | marin | /lib/systemd/systemd --user |
| ├─ipc | 8 | 98786 | marin | /lib/systemd/systemd --user |
| ├─net | 8 | 98786 | marin | /lib/systemd/systemd --user |
| ├─mnt | 4 | 98786 | marin | /lib/systemd/systemd --user |
| ├─mnt | 0 | root | | |
| └─用户 | 6 | 99106 | marin | catatonit -P |
| ├─mnt | 3 | 99106 | marin | catatonit -P |
| ├─net | 2 | 100589 | marin | /catatonit -P |
| ├─mnt | 1 | 100589 | marin | /catatonit -P |
| ├─mnt | 1 | 100584 | marin | /usr/bin/slirp4netns --disable-host-loopback --mtu=65520 --enable-sandbox --enable-seccomp --enable-ipv6 -c -e 3 -r 4 --netns-type=path /run/user/1000/netns/netns-844a415e-435c-39aa-9962-b04eaf69e806 tap0 |
| ├─uts | 2 | 100589 | marin | /catatonit -P |
| ├─ipc | 2 | 100589 | marin | /catatonit -P |
| ├─pid | 1 | 100589 | marin | /catatonit -P |
| ├─cgroup | 1 | 100589 | marin | /catatonit -P |
| ├─mnt | 1 | 100594 | 165531 | /http-echo |
| ├─pid | 1 | 100594 | 165531 | /http-echo |
| └─cgroup | 1 | 100594 | 165531 | /http-echo |

`/catatonit -P` 进程 (PID：100589) 是基础设施容器的主进程。如您所见，它在与 `net`、`mnt`、`utc`、`ipc`、`pid` 和 `cgroup` 命名空间完全不同的命名空间内运行
**根命名空间（如**
**systemd** 进程所示）。

**/http-echo**
进程本身在单独的
**mnt**、
**pid** 和
**cgroup** 命名空间中运行，但与
基础设施容器中的 **catatonit** 进程共享其
**net**、
**uts** 和
**ipc** 命名空间。

这可能一开始并不完全明显，因此为了确认这一点，您还可以运行：

```
lsns -T -p $(pgrep http-echo)
```

输出很明确：

```
NS TYPE NPROCS PID USER COMMAND
4026531837 user 4 98786 marin /lib/systemd/systemd --user
├─4026531834 time 10 98786 marin /lib/systemd/systemd --user
└─4026532337 user 6 99106 marin catatonit -P
├─4026532340 net 2 100589 marin /catatonit -P
├─4026532403 uts 2 100589 marin /catatonit -P
├─4026532404 ipc 2 100589 marin /catatonit -P
├─4026532407 mnt 1 100594 165531 /http-echo
├─4026532408 pid 1 100594 165531 /http-echo
└─4026532409 cgroup 1 100594 165531 /http-echo
```

- **net**、
**uts** 和
**ipc** 命名空间与基础设施容器所持有的命名空间相同。
- **user** 命名空间与 rootless Podman 维护的全局暂停进程所持有的命名空间相同。
- **time** 命名空间是根
**time** 命名空间。
- **mnt**、
**pid** 和
**cgroup** 命名空间对于
**http-echo** 容器是唯一的，将其与 pod 中的其他容器隔离。

这巩固了 pod 本质上是一组能够共享命名空间的容器这一理念。

正如我之前所说，pod 还允许您将容器作为一个内聚单元进行管理。要实际了解这一点，请键入：

```
podman pod stop my-first-pod
```

```
e22b6a695bd8e808cadd2c39490951aba29c971c7be83eacc643b11a0bdc4ec7
```

此命令将停止 pod 及其所有关联容器。要确认这一点，请键入：

```
podman container ps -a
```

您将看到两个容器都已停止：

```
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
131ee0bcd059 localhost/podman-pause:4.3.1-0 25 minutes ago Exited (0) 22 seconds ago e22b6a695bd8-infra
c57f4d354eb4 docker.io/hashicorp/http-echo:1.0.0 19 minutes ago Exited (2) 22 seconds ago gallant_wescoff
```

pod 本身也已停止：

```
podman pod ls
```

```
POD ID NAME STATUS CREATED INFRA ID # OF CONTAINERS
e22b6a695bd8 my-first-pod Exited 28 minutes ago 131ee0bcd059 2
```

当您不再需要 pod 时，可以通过键入以下内容将其完全删除：

```
podman pod rm my-first-pod
```

```
e22b6a695bd8e808cadd2c39490951aba29c971c7be83eacc643b11a0bdc4ec7
```

这不仅会删除 pod，还会删除其所有关联容器。

您可以通过重复
**podman pod ls** 和
**podman container ps -a** 命令来验证此操作是否成功。您将看到您的系统上既没有 pod 也没有容器：

```
podman pod ls
```

```
POD ID NAME STATUS CREATED INFRA ID # OF CONTAINERS
```

```
podman container ps -a
```

```
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
```

至此，您已经掌握了使用 Podman pod 的基础知识。现在，让我们通过一个实际示例来探索它们的实际用途。

## 探索辅助容器

Pod 通常用于向应用程序添加辅助容器。辅助容器基本上为主要应用程序容器提供额外的功能和支持。这支持诸如配置管理、日志传输、基于角色的访问控制等用例。

为了更好地理解这一点，让我们探索一个实际的日志传输示例，其中 Web 服务器记录传入的 HTTP 请求，而日志传输器将它们转发到外部服务进行索引。在此场景中，应用程序 pod 将包含两个容器：

- 一个
[Caddy](https://caddyserver.com/) 容器，用于通过 HTTP 提供网页。
- 一个
[Vector](https://vector.dev/) 容器，配置为将日志从您的 Web 服务器传输到 [Better Stack](https://betterstack.com/logs)。

通过键入以下内容创建新的 pod：

```
podman pod create --name example --publish 8080:80
```

```
e21066fdb234833ffd3167a1b3bda8f5910df7708176da594a054dd09200fae
```

请注意，与您之前调用
**podman pod create** 相比，该命令看起来略有不同。

首先，您使用
**--name** 选项来指定 pod 的名称。可以通过使用
**--name**
选项或作为最后一个位置参数向
**podman pod create** 命令提供名称。换句话说，命令
**podman pod create --publish 8080:80 example** 也完全有效，并且具有完全相同的作用，但为了清楚起见，在传递
多个命令行选项时使用
**--name** 通常更容易阅读和理解。

不过，最重要的是，您指定了附加命令行选项
**--publish 8080:80**。如您所知，我们已经确定 pod 中的容器默认共享相同的网络命名空间。因此，如果您想接收任何 Web 流量，您需要将端口
8080 暴露给整个 pod 的主机。您不能只针对单个容器执行此操作，因为它与 pod 中的其他容器共享其网络命名空间，并且网络命名空间是在最初创建 pod 时配置的。通过使用
**--publish** 选项，您可以确保到达主机机器上端口
8080 的任何流量都将转发到 pod 内的端口
80，其中
## Caddy 容器

Caddy 容器将监听端口 8080。

通过键入以下内容将 Caddy 添加到 Pod 中：

```
podman create --pod example --name caddy docker.io/library/caddy:2.7.6-alpine
```

在此，通过 `--pod example` 选项，您指定 Podman 将容器附加到名为 `example` 的现有 Pod（您之前创建的 Pod）。您还使用 `--name caddy` 选项为容器指定一个特定名称。最后，`docker.io/library/caddy:2.7.6-alpine` 指定容器应从中创建的确切镜像。

Podman 满足请求并生成以下输出：

```
正在尝试拉取 docker.io/library/caddy:2.7.6-alpine...
获取镜像源签名
复制 blob b7343593237d 完成
复制 blob c926b61bad3b 完成
复制 blob 6fd2155878b9 完成
复制 blob 08886dfc0722 完成
复制 config 657b947906 完成
将清单写入镜像目标
存储签名
7307f130b2951ea8202bbf6d1d6d1a81fbdb66d022d65c26f9c209ee2e664bf2
```

请记住，容器的分配名称不仅适用于特定 Pod，而且是全局保留的。如果您尝试使用相同名称创建另一个容器，您将收到错误，即使它不在同一 Pod 中运行：

```
podman create --name caddy docker.io/library/caddy:2.7.6-alpine
错误：创建容器存储：容器名称“caddy”已被 7307f130b2951ea8202bbf6d1d6d1a81fbdb66d022d65c26f9c209ee2e664bf2 使用。您必须删除该容器才能重新使用该名称：该名称已在使用中
```

现在 Caddy 容器已创建，看看它的实际效果很有趣。运行以下命令：

```
curl localhost:8080
```

令人惊讶的是，事实证明当前无法访问 Web 服务器：

```
curl: (7) 在 0 毫秒后无法连接到 localhost 端口 8080：无法连接到服务器
```

这是为什么？虽然 `podman create` 命令确实创建了容器并将其附加到 `example` Pod，但它实际上并没有启动其主进程。如果您希望在创建容器后立即启动进程，您应该执行 `podman run` 而不是 `podman create`，如下所示：

```
podman run --name caddy docker.io/library/caddy:2.7.6-alpine
```

但是，目前不希望启动进程，因为默认 Caddy 配置不会发出日志，这会让您没有供 Vector 处理的任何数据。您可以通过首先修改默认配置来纠正此问题，然后在容器内启动主 caddy 进程。

创建一个名为 `Caddyfile` 的新文件并粘贴以下内容，以确保生成日志：

```
:80 {
root * /usr/share/caddy
file_server
try_files {path} /index.html
log {
output net localhost:9000 {
dial_timeout 5s
soft_start
}
}
}
```

该 `log` 指令指示 Caddy 开始通过网络套接字发出日志，在 Pod 内监听 `localhost:9000` 处的 TCP 连接。此网络套接字尚不存在，但它将由您接下来设置的 Vector 容器创建。

通过发出以下命令将更新的 `Caddyfile` 复制到 Caddy 容器：

```
podman cp Caddyfile caddy:/etc/caddy/Caddyfile
```

请注意，您如何通过之前指定的名称引用容器（`caddy`）。这比编写以下内容容易得多：

```
podman cp Caddyfile 7307f130b295:/etc/caddy/Caddyfile
```

您几乎已准备好启动主 caddy 进程。但在那之前，让我们快速自定义它将要提供的主页，以便在终端中显示其内容更容易。

创建一个名为 `index.html` 的新文件并粘贴以下内容：

```
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Example</title>
</head>
<body>
<p>This is an example page.</p>
</body>
</html>
```

然后通过发出以下命令将 `index.html` 文件复制到容器：

```
podman cp index.html caddy:/usr/share/caddy/index.html
```

最后，启动 Caddy 容器：

```
podman start caddy
```

再次，您使用之前指定的名称（`caddy`）来标识容器。这就是选择清晰且描述性名称如此重要的原因。

通过键入以下内容确认容器正在运行：

```
podman ps -f name=caddy
```

应出现类似的输出：

```
容器 ID 镜像 命令 创建状态 端口 名称
7307f130b295 docker.io/library/caddy:2.7.6-alpine caddy run --confi... 7 分钟前 运行 大约一分钟前 0.0.0.0:8080->80/tcp caddy
```

再次尝试访问服务器：

```
curl localhost:8080
```

这一次，出现了预期的输出：

```
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="ie=edge">
<title>Example</title>
</head>
<body>
<p>This is an example page.</p>
</body>
</html>
```

很好，Caddy 正常工作，`example` Pod 能够在端口 8080 上接收 HTTP 请求。
## Podman 与 Caddy

将端口 8080 转发到 Caddy 容器（端口 80）进行处理。

您还可以通过 Web 浏览器访问您的服务器。输入 `localhost:8080`，应该会显示类似的网页：

之前，我们提到过在提供初始 Pod 定义后，您无法为特定容器公开其他端口。我们来确认一下。

创建另一个 Pod：

```
podman pod create dummy-pod
```

现在，尝试向该 Pod 添加一个新的 Caddy 容器，尝试将容器的端口 80 发布到主机上的端口 8081：

```
podman create --pod dummy-pod --publish 8081:80 docker.io/library/caddy:2.7.6-alpine
```

您会收到一条错误消息：

```
错误：提供了无效配置：创建 Pod 时必须定义已发布或公开的端口：当与 Pod 共享时，无法配置网络
```

在澄清这一点后，您现在可以开始设置 Vector 容器了。

登录您的 [Better Stack](https://logs.betterstack.com) 帐户并创建一个新数据源：

在显示的表单中，指定 **Podman 教程** 作为名称，**Vector** 作为平台，然后单击 **创建源**：

如果一切顺利，新源将成功创建。复制 **源令牌** 字段下显示的令牌。我们将此令牌称为 `<your_source_token>`，并使用它配置 Vector 以将日志发送到 Better Stack。

现在创建一个名为 `vector.yaml` 的新文件，并粘贴以下内容：

```yaml
sources:
  caddy:
    type: socket
    address: 0.0.0.0:9000
    mode: tcp
sinks:
  better_stack:
    type: "http"
    method: "post"
    inputs: ["caddy"]
    uri: "https://in.logs.betterstack.com/"
    encoding:
      codec: "json"
    auth:
      strategy: "bearer"
      token: "<your_source_token>"
```

此文件将指示在 Vector 容器内运行的主进程在端口 9000 上创建一个新的网络套接字，用于侦听 TCP 连接。Caddy 将连接到此套接字以发出其日志。此外，此配置将告诉 Vector 通过 HTTP 将所有收集的日志转发到 Better Stack。

创建一个新的容器，运行 [官方 Vector 镜像](https://hub.docker.com/r/timberio/vector)，并将其添加到 `example` Pod：

```
podman create --pod example --name vector docker.io/timberio/vector:0.35.0-alpine
```

将配置文件复制到容器：

```
podman cp vector.yaml vector:/etc/vector/vector.yaml
```

最后，启动容器：

```
podman start vector
```

通过输入以下内容验证 Pod 中的所有容器是否正在运行：

```
podman ps --pod
```

您应该看到类似的输出：

```
容器 ID 镜像 命令 创建于 状态 端口 名称 Pod ID Pod 名称
5827494c3cce localhost/podman-pause:4.3.1-0 12 分钟前 3 分钟前启动 0.0.0.0:8080->80/tcp bf97c02c7c07-infra bf97c02c7c07 example
7307f130b295 docker.io/library/caddy:2.7.6-alpine caddy run --confi... 12 分钟前 3 分钟前启动 0.0.0.0:8080->80/tcp caddy bf97c02c7c07 example
cd2daa5962e1 docker.io/timberio/vector:0.35.0-alpine 33 秒前 21 秒前启动 0.0.0.0:8080->80/tcp vector bf97c02c7c07 example
```

现在导航回您的浏览器，并刷新 `localhost:8080` 上的网页几次，或从终端发出几个 `curl localhost:8080` 命令。

```
curl localhost:8080/[1-10]
```

在 Better Stack 中，导航到 **实时尾部**：

您应该会看到从 Caddy 容器收集的一些日志：

您的设置有效。Caddy 和 Vector 容器在同一个网络命名空间中运行，因此它们可以通过 vector 建立的 TCP 套接字进行通信。

要确认网络命名空间相同，请运行：

```
lsns -t net -p $(pgrep caddy)
```

```
NS 类型 NPROCS PID 用户 NETNSID NSFS 命令
4026532340 net 5 166215 marin unassigned rootlessport
```

```
lsns -t net -p $(pgrep vector)
```

```
NS 类型 NPROCS PID 用户 NETNSID NSFS 命令
4026532340 net 5 166215 marin unassigned rootlessport
```

这两个进程在文件描述符为 4026532340 的网络命名空间中运行。

`rootlessport` 命令是一个端口转发器，当在无根模式下运行 Podman 时，它可以促进将流量从主机上的端口 80 转发到 Pod 持有的网络命名空间内的端口 8080。

在完成所有这些操作后，让我们继续探讨如何使用 Podman 生成清单并将其部署到 Kubernetes 集群，以及如何将现有的 Kubernetes 清单部署到本地 Podman 安装中。

确保让您的 `example` Pod 继续运行，因为您将在下一部分中用到它。

## 与 Kubernetes 集成

正如我之前提到的，Podman 没有像 Docker Swarm 这样的工具来管理容器编排。在需要高可用性、可扩展性和容错性的更复杂的部署场景中，并且需要涉及多个主机时，Podman 用户可以利用 Kubernetes 等编排器来处理管理工作负载的复杂性。
## Podman 与 Kubernetes

Podman 旨在通过公开用于将现有工作负载转换为 Kubernetes 可以理解的 YAML 文件（清单）的命令，来简化向 Kubernetes 的过渡。此外，用户可以将现有的 Kubernetes 清单导入 Podman，而 Podman 可以解析并本地运行这些工作负载。

如果您不熟悉 Kubernetes 清单是什么，它是一个描述 Kubernetes 集群所需状态的文件。它包括有关 Pod、卷和 Kubernetes 必须创建和管理的其他资源的信息。

在继续此示例之前，您必须安装 [minikube](https://minikube.sigs.k8s.io/docs/) 才能在本地使用 Kubernetes。如果您不知道 Minikube 是什么，它是一个允许您在本地计算机上运行单节点 Kubernetes 集群的工具。

按照 [官方 Minikube 安装说明](https://minikube.sigs.k8s.io/docs/start/) 进行操作并运行：

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
```

这将下载一个名为 `minikube-linux-amd64` 的二进制文件到您的当前目录。使用以下命令将此文件移动到 `$PATH` 中指定的一个目录：

```
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

这将使您能够从终端中的任何位置运行 `minikube` 命令。

由于 `install` 命令不会移动，而只会将 `minikube-linux-amd64` 文件复制到 `/usr/local/bin` 目录，因此您可以继续通过发出以下命令来删除冗余副本：

```
rm minikube-linux-amd64
```

要确认 `minikube` 已成功安装，请运行：

```
minikube version
```

您应该看到类似的输出：

```
minikube version: v1.32.0
commit: 8220a6eb95f0a4d75f7f2d7b14cef975f050512d
```

由于 [Podman 驱动程序](https://minikube.sigs.k8s.io/docs/drivers/podman/) 对于 Minikube 在撰写本文时仍处于实验阶段，并且这会导致 Minikube 内部出现一些网络和 DNS 解析问题，具体取决于特定的底层设置，对于 Linux 下稳定的 Minikube 体验，您仍然必须使用 Docker。

如果您尚未安装 Docker，通常可以按照 [官方 Docker 安装说明](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) 进行操作。

以下示例假定 Docker Engine 已在您的系统上安装并运行，您可以通过发出以下命令来验证：

```
docker --version
```

您应该看到类似的输出：

```
Docker version 24.0.7, build afdd53b
```

您还需要确保将当前用户添加到 `docker` 组，因此对于针对 Docker 守护程序运行命令不需要 `sudo`：

```
sudo usermod -aG docker $USER && newgrp docker
```

否则，Minikube 将失败，并出现类似的错误：

```
👎 无法选择默认驱动程序。以下是按优先顺序考虑的内容：
▪ docker：不正常：“docker version --format {{.Server.Os}}-{{.Server.Version}}:{{.Server.Platform.Name}}”退出状态 1：尝试连接到 Docker 守护程序套接字时权限被拒绝 unix:///var/run/docker.sock：获取“http://%2Fvar%2Frun%2Fdocker.sock/v1.24/versio
n”：拨号 unix /var/run/docker.sock：连接：权限被拒绝
```

在完成所有这些操作后，继续启动 Minikube：

```
minikube start
```

您应该看到类似的输出：

```
😄 minikube v1.32.0 在 Ubuntu 23.10 (kvm/amd64) 上
✨ 自动选择 docker 驱动程序。其他选择：none、ssh
📌 使用具有 root 权限的 Docker 驱动程序
👍 在集群 minikube 中启动控制平面节点 minikube
🚜 正在提取基础镜像 ...
💾 正在下载 Kubernetes v1.28.3 预加载 ...
> preloaded-images-k8s-v18-v1...: 403.35 MiB / 403.35 MiB 100.00% 36.90 M
> gcr.io/k8s-minikube/kicbase...: 453.88 MiB / 453.90 MiB 100.00% 36.32 M
🔥 正在创建 docker 容器（CPU=2，内存=2200MB） ...
🐳 正在 Docker 24.0.7 上准备 Kubernetes v1.28.3 ...
▪ 正在生成证书和密钥 ...
▪ 正在启动控制平面 ...
▪ 正在配置 RBAC 规则 ...
🔗 正在配置网桥 CNI（容器网络接口） ...
🔎 正在验证 Kubernetes 组件...
▪ 正在使用镜像 gcr.io/k8s-minikube/storage-provisioner:v5
🌟 已启用附加组件：storage-provisioner、default-storageclass
💡 未找到 kubectl。如果您需要它，请尝试：“minikube kubectl -- get pods -A”
🏄 完成！kubectl 现在配置为默认使用“minikube”集群和“default”命名空间
```

在 Minikube 运行时，您可以继续从 Podman 资源生成 Kubernetes 清单。

验证您之前创建的示例 Pod 及其所有容器仍在运行：

```
podman pod ls
POD ID 名称 状态 创建时间 基础设施 ID 容器数
bf97c02c7c07 example 正在运行 7 分钟前 5827494c3cce 3
podman container ps
容器 ID 镜像 命令 创建时间 状态 端口 名称
5827494c3cce localhost/podman-pause:4.3.1-0 8 分钟前 8 分钟前启动 0.0.0.0:8080->80/tcp bf97c02c7c07-infra
7307f130b295 docker.io/library/caddy:2.7.6-alpine caddy run --confi... 8 分钟前 8 分钟前启动 0.0.0.0:8080->80/tcp caddy
```
**[TEXT TO CORRECT]:**

cd2daa5962e1 docker.io/timberio/vector:0.35.0-alpine 8 分钟前 已启动 7 分钟前 0.0.0.0:8080->80/tcp vector

Podman 可以通过 `podman kube generate` 命令轻松地从正在运行的 Pod 中构建 Kubernetes 清单。它希望您提供以下参数：

```
podman kube generate <pod_name> --service -f <output_file>
```

要创建与您的示例 Pod 对应的必要清单，请键入：

```
podman kube generate example --service -f example.yaml
```

在此过程中，您可能会看到以下警告，但由于这些特定注释没有任何重大意义，因此您可以安全地忽略该消息：

```
WARN[0000] 截断注释：“5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140bf”至“5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140b”：Kubernetes 仅允许 63 个字符
WARN[0000] 截断注释：“5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140bf”至“5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140b”：Kubernetes 仅允许 63 个字符
```

在这种情况下，`5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140bf` 是与 Pod 关联的基础设施容器的 SHA-256 ID，它用于填充生成的清单文件中的 `io.kubernetes.cri-o.SandboxID/caddy` 和 `io.kubernetes.cri-o.SandboxID/vector` 注释。这些注释对于将此 Pod 部署到 Kubernetes 没有任何重大作用。

一个 `example.yaml` 文件现在应该出现在您的当前文件夹中：

```
ls -l example.yaml
-rw-r--r-- 1 marin marin 2270 1 月 19 11:21 example.yaml
```

让我们检查一下它的内容：

```
# 保存此文件的内容并使用 kubectl create -f 将其导入 Kubernetes。
#
# 使用 podman-4.3.1 创建
apiVersion: v1
kind: Service
metadata:
creationTimestamp: "2024-01-19T11:21:33Z"
labels:
app: example
name: example
spec:
ports:
- name: "80"
nodePort: 30381
port: 80
targetPort: 80
selector:
app: example
type: NodePort
---
apiVersion: v1
kind: Pod
metadata:
annotations:
io.kubernetes.cri-o.ContainerType/caddy: container
io.kubernetes.cri-o.ContainerType/vector: container
io.kubernetes.cri-o.SandboxID/caddy: 5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140bf
io.kubernetes.cri-o.SandboxID/vector: 5827494c3cce19080da3e0804596c4f46c71c342429d8171bfa45f4188b140bf
io.kubernetes.cri-o.TTY/caddy: "false"
io.kubernetes.cri-o.TTY/vector: "false"
io.podman.annotations.autoremove/caddy: "FALSE"
io.podman.annotations.autoremove/vector: "FALSE"
io.podman.annotations.init/caddy: "FALSE"
io.podman.annotations.init/vector: "FALSE"
io.podman.annotations.privileged/caddy: "FALSE"
io.podman.annotations.privileged/vector: "FALSE"
io.podman.annotations.publish-all/caddy: "FALSE"
io.podman.annotations.publish-all/vector: "FALSE"
creationTimestamp: "2024-01-19T11:21:33Z"
labels:
app: example
name: example
spec:
automountServiceAccountToken: false
containers:
- image: docker.io/library/caddy:2.7.6-alpine
name: caddy
ports:
- containerPort: 80
hostPort: 8080
resources: {}
securityContext:
capabilities:
drop:
- CAP_MKNOD
- CAP_NET_RAW
- CAP_AUDIT_WRITE
- image: docker.io/timberio/vector:0.35.0-alpine
name: vector
resources: {}
securityContext:
capabilities:
drop:
- CAP_MKNOD
- CAP_NET_RAW
- CAP_AUDIT_WRITE
enableServiceLinks: false
hostname: example
restartPolicy: Never
status: {}
```

您现在可以运行以下命令将此清单部署到您的 Kubernetes 集群：

```
minikube kubectl -- create -f example.yaml
```

这将产生类似的输出：

```
> kubectl.sha256: 64 B / 64 B [-------------------------] 100.00% ? p/s 0s
> kubectl: 47.56 MiB / 47.56 MiB [------------] 100.00% 2.42 GiB p/s 200ms
已创建 service/example
已创建 pod/example
```

等待一两分钟，然后键入：

```
minikube kubectl -- get all
```

您应该看到类似的输出：

```
NAME READY STATUS RESTARTS AGE
pod/example 2/2 正在运行 0 7m11s
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
service/example NodePort 10.110.196.168 <none> 80:30381/TCP 7m11s
service/kubernetes ClusterIP 10.96.0.1 <none> 443/TCP 11m
```

这表明 Pod 已启动并在您的本地 Kubernetes 集群中运行。

从输出中，Pod 似乎已准备好通过相应的 NodePort 服务在端口 80 上接受传入的 HTTP 请求。在这种情况下，NodePort 服务基本上将 Pod 正在运行的 Kubernetes 节点的端口 30381 映射到 Pod 中的端口 80。

但是，如果您键入：

```
curl localhost:80
```

您会注意到 Web 服务器不可达：

```
curl: (7) 在 0 毫秒后无法连接到 localhost 端口 80：无法连接到服务器
```

这是因为 minikube 网络与您的主机网络隔离。您可以运行以下命令来确定您可以连接到的 URL：

```
minikube service list
```

这将输出一个类似的表格：

```
|-------------|------------|--------------|---------------------------|
| NAMESPACE | NAME | TARGET PORT | URL |
|-------------|------------|--------------|---------------------------|
```
| default | example | 80/80 | http://192.168.49.2:30381 |
|---|---|---|---|
| default | kubernetes | 无节点端口 | |
| kube-system | kube-dns | 无节点端口 | |

URL 列中列出的地址是能够访问你的 Web 服务器的地址。

重试，在浏览器中打开 http://192.168.49.2:30381 或键入：

```
curl http://192.168.49.2:30381
```

你将看到熟悉的“Caddy, works!”页面：

你的 Pod 现在已在 Kubernetes 上成功运行。你之前通过 podman cp 所做的更改当然在已部署的镜像中缺失，因此 Caddy 默认显示“Caddy, works!”页面，但实际上将应用程序部署到 Kubernetes 所需的只是一条命令。

你可以通过键入以下内容从 Kubernetes 中删除 Pod：

```
podman kube down example.yaml
```

这会产生类似的输出：

```
Pods 已停止：
98e78483cfd2258fa5d82fb77d113b9cbdd39adc33712ea448b4de15800bb4ce
Pods 已删除：
98e78483cfd2258fa5d82fb77d113b9cbdd39adc33712ea448b4de15800bb4ce
```

如你所见，只需几条命令，你便能够生成一个清单，用于在 Kubernetes 上部署你的应用程序。然后，你获取了一个现有的 Kubernetes 清单，并使用 Podman 在本地运行它。这展示了 Podman 在编排你的容器化工作负载方面所能提供的强大功能和灵活性。

## 探索 Podman Desktop

尽管使用 CLI 是与 Podman 交互的常见方式，但更喜欢图形界面的用户还可以选择使用 [Podman Desktop](https://podman-desktop.io/)，这是一个开源工具，为管理容器和镜像以及与 Kubernetes 清单交互提供了一个用户友好的 GUI。

Podman Desktop 旨在抽象底层详细信息，让用户更多地专注于应用程序开发。

安装 Podman Desktop 的常用方法是通过其对应的 [Flatpak](https://flatpak.org/) 包。如果你碰巧没有在你的系统上安装 flatpak，你可以通过运行以下命令来安装它：

```
sudo apt install flatpak
```

然后添加 flathub 存储库，如下所示：

```
flatpak remote-add --if-not-exists --user flathub https://flathub.org/repo/flathub.flatpakrepo
```

你可能需要重新启动会话才能使所有更改生效。完成后，你可以运行以下命令来安装 Podman Desktop：

```
flatpak install --user flathub io.podman_desktop.PodmanDesktop
```

最后，要启动 Podman Desktop，请运行：

```
flatpak run io.podman_desktop.PodmanDesktop
```

很快，Podman Desktop GUI 将出现：

让我们通过在终端中发出以下命令来重新创建我们之前示例中的 Pod：

```
podman pod create --name example --publish 8080:80
podman create --pod example --name caddy docker.io/library/caddy:2.7.6-alpine
podman create --pod example --name vector docker.io/timberio/vector:0.35.0-alpine
```

然后，在 Podman Desktop 中，导航到 **Pods**：

你将看到列出的 example Pod：

不必键入 podman kube generate 从此 Pod 创建 Kubernetes 清单，你可以使用 **生成 Kube** 操作：

将出现一个清单，其中包含与通过运行 podman kube generate example -f example.yaml 获得的内容相同的内容。

不过你可能已经注意到，该清单中缺少 Service 定义。之前，你通过将 --service 标志传递给 podman kube generate 来显式请求它。乍一看，Podman Desktop 似乎不允许你轻松定义 Service。然而，事实并非如此。

返回 **Pods** 屏幕并选择 **部署到 Kubernetes** 操作：

将出现相同的 YAML 定义，但还有一个额外的复选框，允许你定义 Service：

向下滚动一点，你将看到 minikube 被列为 Kubernetes 上下文。这对应于你之前创建的 minikibe 集群：

单击 **部署**，片刻之后，Pod 将部署到你的本地 minikube 集群：

返回终端并发出：

```
minikube service list
```

这会输出：

| NAMESPACE | NAME | TARGET PORT | URL |
|---|---|---|---|
| default | example-8080 | 无节点端口 | |
| default | kubernetes | 无节点端口 | |
| kube-system | kube-dns | 无节点端口 | |

与之前不同，即使创建了服务，也没有可用于连接到 Caddy 的节点端口。这是因为 Podman Desktop 创建了一个类型为 ClusterIP 而不是 NodePort 的服务。

要验证这一点，请发出：

```
minikube kubectl -- get all
```

你将看到 Podman Desktop 创建的 example-8080 服务的类型为 ClusterIP：

```
NAME READY STATUS RESTARTS AGE
pod/example 2/2 Running 0 4m25s
NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE
service/example-8080 ClusterIP 10.105.82.9 <none> 8080/TCP 4m25s
service/kubernetes ClusterIP 10.96.0.1 <none> 443/TCP 6m21s
```

解决此问题的一种可能方法是通过修补服务来更改其类型，以便访问 Caddy：
## 从 Podman 到 Kubernetes：一个实用的集成指南

### 前言

Podman 与 Kubernetes 的集成提供了容器编排的强大且灵活的解决方案。本文将指导你使用 Podman CLI 和 Podman Desktop 在本地环境中管理和部署 Kubernetes Pod。

### 使用 Podman CLI 创建 Kubernetes Pod

1. 安装 Podman 和 kubectl。
2. 创建一个 Kubernetes 清单文件（例如，example.yaml）。
3. 运行 `podman kube play example.yaml` 命令。

### 使用 Podman Desktop 创建 Kubernetes Pod

1. 打开 Podman Desktop 并导航到 Pods 页面。
2. 单击“播放 Kubernetes YAML”按钮。
3. 选择 example.yaml 文件并单击“播放”。

### 访问 Pod 服务

在浏览器中打开 `localhost:8080` 以访问 Pod 的服务。

### 删除 Pod

**使用 Podman CLI：**

```
podman kube down example-8080
```

**使用 Podman Desktop：**

1. 导航到 Pods 页面。
2. 单击 Pod 旁边的“删除”按钮。

### 导入现有 Kubernetes 清单

1. 在 Podman Desktop 中，单击“播放 Kubernetes YAML”按钮。
2. 选择要导入的清单文件。
3. 单击“播放”。

### 结论

Podman 与 Kubernetes 的集成提供了在本地环境中管理和部署容器的强大功能。通过 Podman CLI 和 Podman Desktop，你可以轻松创建、查看和删除 Pod，并访问其面向公众的服务。

### 进一步探索

* [Podman 官方网站](https://podman.io/)
* [Podman 文档](https://podman.io/docs)
* [Podman 社区](https://podman.io/community)

### 作者计划

加入我们的客座写作计划，通过撰写技术指南获得报酬。[为我们撰写](https://betterstack.com/community/write-for-us)！

### 在 Better Stack 的基础上构建

与全世界分享你的项目。[community@betterstack.com](mailto:community@betterstack.com?subject=Better%20Stack%20community%20project&body=) 或 [github.com/betterstack-community/projects](https://github.com/betterstack-community/projects)。