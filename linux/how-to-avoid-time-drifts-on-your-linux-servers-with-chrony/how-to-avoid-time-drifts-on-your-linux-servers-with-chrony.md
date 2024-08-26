
<!--
title: 如何在Linux服务器上使用Chrony避免时间漂移
cover: https://cdn.thenewstack.io/media/2024/08/7dc11acd-getty-images-f2pc4k6da84-unsplash-scaled.jpg
-->

你会惊讶于如果 Linux 系统的时间不同步，它可能会遇到多少问题。以下是如何使用 Chrony 来校准 NTP。

> 译自 [How to Avoid Time Drifts on Your Linux Servers with Chrony](https://thenewstack.io/how-to-avoid-time-drifts-on-your-linux-servers-with-chrony/)，作者 Jack Wallen。

我说不清有多少次我在 [Linux 上安装软件包](https://thenewstack.io/how-to-manage-linux-software/) 或下载 [Docker](https://www.docker.com/?utm_content=inline+mention) [镜像](https://thenewstack.io/the-case-for-environment-specific-docker-images/) 时，却收到错误消息，提示无法完成操作。第一次遇到这种情况时，我感到非常沮丧，因为我花了很长时间才解决问题。

结果发现，这一切都与时间有关。

无论是由于配置错误的区域设置还是简单的时间漂移，您都可能遇到类似的情况。也许您部署了 [Docker Swarm](https://thenewstack.io/docker-swarm-a-user-friendly-alternative-to-kubernetes/)，但其中一个节点不再响应或连接。或者，您可能遇到了 MariaDB 数据库复制开始失败的问题。您会惊讶于服务器上的时间错误会导致多少问题。

那么，如何避免这种情况呢？您可以安装一个名为 [Chrony](https://chrony-project.org/) 的简单工具，它可以使您的服务器时间保持同步。Chrony 可以将系统时钟与 NTP 服务器、参考时钟和手动输入同步，还可以充当 NTPv4 服务器和对等体，以保持所有 Linux 服务器上的时间同步。

让我向您展示如何在 Linux 上安装和使用 Chrony。

## 您需要准备什么

要使用 Chrony，您需要一台或多台 Linux 服务器和一个具有 sudo 权限的用户。

在我们开始使用 Chrony 之前，您必须先完成一项任务。

## 设置您的时区

为了确保您的服务器时间正确，Chrony 要求所有服务器都必须配置为正确的时区。如果您的服务器都设置为同一个错误的时区，或者它们设置为不同的时区，那么 Chrony 对您来说将毫无用处。

因此，让我们在您的服务器上设置时区。

此步骤使用 `timedatectl` 命令完成，该命令默认安装在大多数 Linux 服务器上。在执行此操作之前，您需要知道应该设置哪个时区。要查看所有时区的列表，请发出以下命令：

```
timedatectl list-timezones | less
```

滚动浏览该列表，直到找到适合您所在地区的时区。例如，如果您住在肯塔基州路易斯维尔，则正确的时区是 America/Kentucky/Louisville，设置方法如下：

```
sudo timedatectl set-timezone America/Kentucky/Louisville
```

完成此操作后，您可以使用以下命令验证更改：

```
timedatectl
```

确保您在所有服务器（无论是裸机、虚拟机还是容器）上都执行了上述操作。
您现在可以使用 Chrony 了。

## 安装 Chrony

Chrony 可以在大多数发行版的标准存储库中找到，这意味着安装非常简单。例如，在基于 Ubuntu 的发行版上，安装命令为：

```
sudo apt-get install chrony -y
```

如果您使用的是基于 Fedora 的发行版，则命令为：

```
sudo dnf install chrony -y
```

对于基于 Arch 的发行版：

```
sudo pacman -S chrony
```

安装 Chrony 后，请确保使用以下命令启动并启用它：

```
sudo systemctl enable --now chronyd
```

## 启用 Chrony NTP 服务

接下来，您必须使用以下命令启用 Chrony NTP 服务：

```
sudo timedatectl set-ntp yes
```

您将不会收到上述命令的任何输出。
完成此操作后，请使用以下命令检查时间：

```
timedatectl
```

它应该是准确的。不仅如此，您现在还应该看到 NTP 服务被列为活动状态，这意味着 Chrony 正在检查您的时间。

请注意，如果您必须更改机器的时区，则应重新启动以使更改生效。

## 配置 Chrony

您应该不需要对 Chrony 进行任何操作即可使其正常工作。如果您想调查配置，可以使用以下命令打开文件进行编辑：

```
sudo nano /etc/chrony.conf
```

如果找不到该文件，请尝试以下命令：

```
sudo nano /etc/chrony/chrony.conf
```

在文件的顶部，您会发现列出了一个用于保持时间同步的公共服务器。在我的 AlmaLinux 测试服务器上，该行是：

```
pool 2.almalinux.pool.ntp.org iburst
```

如果您愿意，可以随时更改默认池。例如，根据 NTP Pool 项目，您可以对美国使用以下池：

```
server 0.us.pool.ntp.org
server 1.us.pool.ntp.org
server 2.us.pool.ntp.org
server 3.us.pool.ntp.org
```

您还可以查看其他几个选项，但您很可能希望保持原样。

您还可以将 Linux 机器配置为 Chrony NTP 服务器。为此，您必须取消注释（删除前导 `#` 字符）Chrony 配置文件中的以下行：

```
allow 192.168.0.0/16
local stratum 10
```

还要确保将 IP 子网更改为您的 LAN 的子网。保存并关闭文件。接下来，使用以下命令重启 Chrony：

```
sudo systemctl restart chronyd
```

确保允许 NTP 服务通过您的防火墙。例如，在 AlmaLinux 上，这需要以下两个命令：

```
sudo firewall-cmd --add-service=ntp --permanent
sudo firewall-cmd --reload
```

然后，您可以在网络上客户端的 chrony.conf 文件中配置 NTP 服务器。例如，如果您的 NTP 服务器位于 192.168.1.210，则可以在 Chrony 配置文件中添加以下内容：

```
pool 192.168.1.210 iburst maxsources 4
```

此时，您的客户端将与您的服务器保持同步。只要您的服务器与 NTP 池同步，任何使用它作为时间服务器的服务器（或桌面）都将保持同步。

使用这个简单易用的工具避免与时间相关的问题，您将减少烦恼和失眠。
