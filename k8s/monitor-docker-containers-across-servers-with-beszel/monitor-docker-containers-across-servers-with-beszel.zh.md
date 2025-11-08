你的网络上有多少台机器运行 [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) [容器](https://thenewstack.io/introduction-to-containers/)？一台？两台？20台？

那么，这些机器和容器的性能如何？你多久能登录到这些机器并运行必要的命令来找出这些信息？更棒的是，你知道完成这些所需的命令吗？

如果我告诉你，你可以在一台机器上部署一个容器，然后在你需要监控的每台服务器上部署代理呢？如果我告诉你，这一切都可以通过 Docker 完成，而且非常简单呢？最终结果是一个单一的仪表盘，让你能快速访问用于容器部署的那些机器的资源使用情况。

这个容器叫做 [Beszel](https://beszel.dev/)，它能够显示 Docker 统计数据、历史数据和警报功能。

Beszel 的功能集包括：

*   用户友好的网页界面
*   简单配置
*   自动备份支持
*   多用户
*   OAuth 认证
*   API 访问

它部署和使用都足够简单，你会觉得这是个无需思考的选择。

让我向你展示如何部署 Beszel 并连接一个代理，以便你可以跟踪 Docker 服务器的系统资源。

## 你需要什么

你唯一需要的是多台支持 Docker 的机器。我将在 [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 24.04 上演示这一点，因此如果你使用不同的操作系统，你需要修改 Docker 的安装过程。

## 安装 Docker

如果你正在考虑监控运行 Docker 容器的服务器资源，你可能已经安装了 Docker。万一你没有，这里是安装方法（否则，请跳到下一节）。

**1. 使用以下命令添加官方 Docker GPG 密钥：**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get update |
|  | sudo apt-get install ca-certificates curl |
|  | sudo install -m 0755 -d /etc/apt/keyrings |
|  | sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc |
|  | sudo chmod a+r /etc/apt/keyrings/docker.asc |

**2. 使用以下命令添加所需的 Docker 仓库：**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | echo \ |
|  | "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \ |
|  | $(. /etc/os-release && echo "${UBUNTU\_CODENAME:-$VERSION\_CODENAME}") stable" | \ |
|  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null |
|  | sudo apt-get update |

**3. 使用以下命令安装所需的软件：**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y |

**4. 将你的用户添加到 Docker 用户组：**

要以标准用户身份运行 Docker 命令，你需要将该用户添加到 Docker 用户组。这样做是为了你可以无需 `sudo` 权限运行 Docker 命令。使用以下命令将你的用户添加到 Docker 用户组：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo usermod -aG docker $USER |

注销并重新登录，以使更改生效。

## 部署 Beszel

我们现在可以部署 Beszel 中心。为此，我们将使用 `docker run` 命令，如下所示：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker volume create beszel\_data && \ |
|  | docker run -d \ |
|  | --name beszel \ |
|  | --restart=unless-stopped \ |
|  | --volume beszel\_data:/beszel\_data \ |
|  | -p 8090:8090 \ |
|  | henrygd/beszel |

给它一两分钟的时间来启动。时间过后，打开网页浏览器并指向：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

其中 SERVER 是托管服务器的 IP 地址。

你应该会看到一个账户创建页面。完成创建后，登录，你将看到 Beszel 主窗口（图 1）。

[![](https://cdn.thenewstack.io/media/2025/11/da830332-beszel1.jpg)](https://cdn.thenewstack.io/media/2025/11/da830332-beszel1.jpg)

图 1. Beszel 中心现在已准备好接受来自代理的连接。

## 部署代理

在右上角，点击“添加系统”（Add System）。一个弹出窗口将出现（图 2），要求你填写你想要监控的服务器信息。添加一个名称和主机 IP 地址。

[![](https://cdn.thenewstack.io/media/2025/11/d245d003-screenshot-2025-11-07-at-4.14.50%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/11/d245d003-screenshot-2025-11-07-at-4.14.50%E2%80%AFpm.png)

图 2. 填写信息以添加新系统。

接下来，点击“复制 Docker Compose”（Copy Docker compose），它将复制代理部署所需的配置内容。

登录到你要监控的第一台机器，并使用以下命令创建一个新的 `docker-compose.yaml` 文件：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

将复制的内容粘贴到新文件中。内容应该如下所示：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[了解有关双向 Unicode 字符的更多信息](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | services: |
|  | beszel-agent: |
|  | image: henrygd/beszel-agent |
|  | container\_name: beszel-agent |
|  | restart: unless-stopped |
|  | network\_mode: host |
|  | volumes: |
|  | - /var/run/docker.sock:/var/run/docker.sock:ro |
|  | - ./beszel\_agent\_data:/var/lib/beszel-agent |
|  | # monitor other disks / partitions by mounting a folder in /extra-filesystems |
|  | # - /mnt/disk/.beszel:/extra-filesystems/sda1:ro |
|  | environment: |
|  | LISTEN: 45876 |
|  | KEY: 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDkDP8dJ2QSK3Z9jSm3P5X1NhOlgXZI83uMq74npgk4j' |
|  | TOKEN: 7dd3-6d258uY0fn-8a19-1f66bba3c |
|  | HUB\_URL: http://192.168.1.26:8090 |

保存并关闭文件。

使用以下命令部署代理：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

代理将部署，几分钟后，你可以刷新中心的网页，新服务器将列出。

然后，你可以在你需要监控的每台机器上部署代理。

一旦代理出现，你可以查看它们的资源使用情况，还可以点击顶部的容器按钮（看起来像一个小的 3D 矩形）来查看部署在该机器上的每个容器的资源使用情况（图 3）。列表还将显示每个容器的健康状态。

[![](https://cdn.thenewstack.io/media/2025/11/75e50884-beszel2.jpg)](https://cdn.thenewstack.io/media/2025/11/75e50884-beszel2.jpg)

图 3. 你的所有容器都属于我们！

这真是太方便了。

如果你需要密切关注容器的资源使用情况以及健康状态，Beszel 是我发现的最好、免费且易于使用的选择之一。试试 Beszel，看看它是否能让监控这些容器变得更简单。