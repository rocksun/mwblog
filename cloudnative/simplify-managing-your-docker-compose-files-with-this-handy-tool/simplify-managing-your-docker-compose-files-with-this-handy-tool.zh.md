[Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) 的 `run` 命令是运行 [容器](https://thenewstack.io/introduction-to-containers/) 的绝佳入门方式。它简单、快捷且相当容易学习。

但它也有一些局限性。一方面，这些 `run` 命令会变得非常长，仅仅在终端窗口中查看它们就可能是一个真正的挑战。此外，在运行这些命令之前编辑它们也更困难。你可能想修改端口，这意味着你需要使用键盘上的箭头键一个字符一个字符地导航回去，直到可以更改默认端口的精确位置。

尽管你可能从 *docker run* 开始，但你最终会不可避免地迁移到 *docker-compose*。使用 *docker-compose*，你可以从文件中构建容器，因此更容易创建。更好的是，你可以使用 Docker Compose .yaml 文件构建高度复杂的容器。

但是，有些人并不太喜欢通过终端窗口进行操作。除非你像我一样，已经使用 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) CLI（命令行界面）数十年，否则你可能属于这一类人。

你该怎么办？

你可以尝试一个基于 Web 的工具来管理你的 *docker-compose* 文件。其中一个工具就是 [Dockge](https://github.com/louislam/dockge)。

根据该项目的 GitHub 仓库，Dockge 是一个“易于使用且响应迅速的自托管 Docker compose.yaml 堆栈式管理器”。

听起来很有趣，对吧？

我试用了一下，看看它有多容易使用，结果印象深刻。

让我们安装 Dockge，看看它是如何工作的。

## 你需要什么

对于 Dockge，你需要一个支持 Docker 的操作系统和一个具有管理员权限的用户。我将使用 Ubuntu Server 24.04 进行演示。如果你使用不同的操作系统，你只需要修改 Docker 安装说明。如果已经安装了 Docker，你可以跳到“部署 Dockge”部分。

## 安装 Docker 和 Docker Compose

### 安装 Docker

以下是安装 Docker 的步骤：

1. **安装官方 Docker GPG 密钥**

第一步是添加官方 Docker GPG 密钥，这可以通过以下命令完成：

sudo apt-get update  
sudo apt-get install ca-certificates curl  
sudo install -m 0755 -d /etc/apt/keyrings  
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc  
sudo chmod a+r /etc/apt/keyrings/docker.asc

2. **添加官方 Docker 仓库**

使用以下命令添加官方 Docker 仓库：

```

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc]
https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

3. **安装 Docker**

在安装软件之前，使用以下命令更新 apt：

```

sudo apt-get update
```

现在，你可以使用以下命令安装 Docker 和其他组件：

```

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

4. **将你的用户添加到 Docker 用户组**

现在你必须将你的用户添加到 docker 用户组。如果不这样做，你将不得不以管理员权限运行容器，这可能会导致严重的安全问题。为此，请使用以下命令将你的用户添加到 docker 用户组：

```

sudo usermod -aG docker $USER
```

最后，注销并重新登录以使更改生效。

## 部署 Dockge

尽管我们可以使用 Docker `run` 命令部署 Dockge，但这会让人感觉像是打脸；所以，我们将使用 `docker-compose` 命令部署 Dockge。然而，在此之前，还有几个步骤。

首先，使用以下命令创建存储 Dockge 堆栈信息/文件的必要目录：

```

mkdir -p /opt/stacks /opt/dockge
```

使用以下命令进入 Dockge 目录：

```

cd /opt/dockge
```

开发者提供了一个预配置的 yaml 文件供下载，所以你无需自己创建。使用以下命令下载该 `compose.yaml` 文件：

```

curl https://raw.githubusercontent.com/louislam/dockge/master/compose.yaml --output compose.yaml
```

你可能需要打开文件进行编辑，以防你想更改某些内容（例如默认端口 – 5001）。

在将该 yaml 文件配置为你想要的样子后，使用以下命令启动 Dockge：

```

docker compose up -d
```

注意：如果你使用 V1 版本的 docker-compose 或 Podman，命令将是：

```

docker-compose up -d
```

给 Dockge 一分钟时间来启动。

## 访问 Dockge

一旦 Dockge 运行起来，打开一个网络浏览器并指向 http://SERVER:5001（其中 SERVER 是托管服务器的 IP 地址）。如果你更改了默认外部端口，请务必在 URL 中也进行更改。

你将看到帐户设置页面（**图 1**）。

![](https://cdn.thenewstack.io/media/2026/02/1629e45c-screenshot-2026-02-16-at-7.21.09-am.png)

**图 1：** 不用担心，你的信息是本地保存的，因此不会发送遥测数据。

填写必要信息并点击“创建”。

现在你应该会看到 Dockge 主页面（**图 2**）。

![](https://cdn.thenewstack.io/media/2026/02/2915f71f-screenshot-2026-02-16-at-7.39.07-am-scaled.png)

**图 2：** Dockge 主页面简洁易懂。

如果你已经有一个或两个堆栈正在运行，如果你点击其中一个，Dockge 会报告它不是由 Dockge 管理的，所以你无法对它们进行任何操作。

要开始构建一个新的堆栈（明白了吗？），点击“Compose”并开始填写字段。这个工具非常容易上手。你甚至可以在构建页面内将变量添加到 .env 文件中。

你可以添加容器以及网络。默认情况下，你可能会注意到“卷（volumes）”选项不可用。它确实存在，只是有点隐藏。点击“删除”旁边的“编辑”按钮，你就会看到“卷（volumes）”选项（**图 3**）。

![](https://cdn.thenewstack.io/media/2026/02/48d8d9db-screenshot-2026-02-16-at-7.31.11-am.png)

**图 3：** 你 *可以* 使用 Dockge 添加卷。

完成后，点击保存，你将看到完整的 Docker Compose 文件（**图 4**）。

![](https://cdn.thenewstack.io/media/2026/02/beac18be-screenshot-2026-02-16-at-7.32.34-am.png)

**图 4：** 我们的第一个 Docker Compose 文件已准备就绪。

现在你可以通过点击顶部的相关按钮来启动、编辑或更新堆栈。

如你所见，熟悉 Docker Compose 文件并不像想象中那么具有挑战性。