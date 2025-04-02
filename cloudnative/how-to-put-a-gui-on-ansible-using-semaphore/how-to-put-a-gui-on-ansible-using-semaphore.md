
<!--
title: 如何使用Semaphore在Ansible上添加GUI
cover: https://cdn.thenewstack.io/media/2023/04/f647832c-semaphore.jpg
summary: 告别命令行！用 Semaphore 为 Ansible 穿上 GUI 外衣，轻松玩转 IT 自动化。一键安装 MariaDB，配置 `systemd`，通过 Web UI 管理 `playbook`、`inventory`。更有 Ansible 常见问题解答，助你快速上手云原生自动化运维！
-->

告别命令行！用 Semaphore 为 Ansible 穿上 GUI 外衣，轻松玩转 IT 自动化。一键安装 MariaDB，配置 `systemd`，通过 Web UI 管理 `playbook`、`inventory`。更有 Ansible 常见问题解答，助你快速上手云原生自动化运维！

> 译自：[How to Put a GUI on Ansible, Using Semaphore](https://thenewstack.io/how-to-put-a-gui-on-ansible-using-semaphore/)
> 
> 作者：Jack Wallen

Ansible 非常适合自动化日常 IT 任务，但有些人可能会因命令行而感到受阻。本文介绍如何安装 Semaphore 图形用户界面。

[Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的开源 Ansible 是一个开源 IT 自动化平台，[使用 Python 编写](https://thenewstack.io/what-is-python/)，可以配置系统、部署软件和编排高级工作流程。默认情况下，Ansible 是一个命令行工具，但使用起来并不十分复杂。
但是，有些人更喜欢使用图形用户界面 (GUI) 来提高平台的使用效率。值得庆幸的是，有一个名为 Semaphore 的 GUI，可以帮助大型环境和组织更轻松地使用 Ansible。

我想带您了解安装 Semaphore 的过程。我将在 Ubuntu Linux（版本 22.04）上进行演示，因此您需要确保已安装并运行 Ansible。为此，请首先按照[本教程](https://thenewstack.io/install-ansible-on-ubuntu-server-to-automate-linux-server-deployments/)进行操作。完成这些操作后，您就可以安装 Semaphore 了。

## 你需要的

显然，您需要在 Ubuntu 上启动并运行 Ansible。您还需要一个具有 `sudo` 权限的用户。就是这样。让我们开始安装。

## 安装 Semaphore

虽然您可以使用 Snap 轻松安装 Semaphore，但我们将采用不同的方式，以便确保该平台可以从 LAN 上的任何位置访问。

首先要做的是安装数据库服务器。我们将使用 MariaDB。要在 Ubuntu 上安装 MariaDB，您必须使用以下命令添加存储库：

```bash
curl -LsS https://downloads.mariadb.com/MariaDB/mariadb_repo_setup | sudo bash -s --
```

该命令完成后，使用以下命令安装服务器和客户端：

```bash
sudo apt install mariadb-server mariadb-client
```

安装 MariaDB 后，使用以下命令保护它：

```bash
sudo mariadb-secure-installation
```

对第一个问题回答 n，对其余问题回答 y。系统还会提示您创建并验证 root 用户密码。
安装数据库后，就可以添加 Semaphore 了。我们首先使用以下命令为版本设置一个变量：

```bash
VER=$(curl -s https://api.github.com/repos/ansible-semaphore/semaphore/releases/latest|grep tag_name | cut -d '"' -f 4|sed 's/v//g')
```

我们现在可以使用该变量通过以下命令下载正确的版本：

```bash
wget https://github.com/ansible-semaphore/semaphore/releases/download/v${VER}/semaphore_${VER}_linux_amd64.deb
```

使用以下命令安装 Semaphore：

```bash
sudo apt install ./semaphore_${VER}_linux_amd64.deb
```

砰！Semaphore 已安装并准备好进行配置。

## 配置 Semaphore

您不能只编辑配置文件，因为尚不存在任何配置文件。要生成配置文件，请运行 semaphore，使其提示您配置所有内容。该命令是：

```bash
sudo semaphore setup
```

配置的第一部分如下所示：

```
Hello! You will now be guided through a setup to:
 
1. Set up configuration for a MySQL/MariaDB database
2. Set up a path for your playbooks (auto-created)
3. Run database Migrations
4. Set up initial semaphore user &amp; password
 
What database to use:
 
1 - MySQL
2 - BoltDB
3 - PostgreSQL
(default 1):
```

确保为您的数据库选择 MySQL，然后进行相应的配置。您可以接受所有内容的默认设置，但您必须键入您之前创建的 MariaDB root 用户密码。
当您进入 Hostname 部分（看起来像 db Hostname (default 127.0.0.1:3306):）时，请确保以以下形式键入它：

```bash
http://SERVER:3000
```

其中 SERVER 是您的托管服务器的 IP 地址。
在提示的末尾附近，系统还会要求您为 Web UI 创建一个新的管理员用户。

## 创建 Systemd 文件

接下来，我们需要创建一个 systemd 文件，以便可以控制 Semaphore 服务。使用以下命令创建文件：

```bash
sudo nano /etc/systemd/system/semaphore.service
```

在该文件中，粘贴以下内容：

```
[Unit]
Description=Semaphore Ansible UI
Documentation=https://github.com/ansible-semaphore/semaphore
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
ExecReload=/bin/kill -HUP $MAINPID
ExecStart=/usr/bin/semaphore server --config /etc/semaphore/config.json
SyslogIdentifier=semaphore
Restart=always

[Install]
WantedBy=multi-user.target
```

保存并关闭文件。
使用以下命令重新加载 systemd 守护程序：

```bash
sudo systemctl daemon-reload
```

使用以下命令启动并启用 Semaphore 服务：

```bash
sudo systemctl enable --now semaphore
```

## 访问 Semaphore Web UI
服务运行并接受连接后，打开连接到同一 LAN 的计算机上的 Web 浏览器，然后将其指向 `http://SERVER:3000`（其中 SERVER 是托管服务器的 IP 地址）。您将看到 Semaphore 登录提示（图 1）。

![Semaphore 登录屏幕](https://cdn.thenewstack.io/media/2023/04/25f1c5c5-semaphore1.jpg)

*图 1：Semaphore 登录屏幕。*

然后，系统将提示您创建您的第一个项目（图 2），因此为其命名并配置可选的 Telegram Chat ID 和最大并行任务数。完成这些操作后，单击“创建”。

![创建新项目](https://cdn.thenewstack.io/media/2023/04/8fdd8abb-semaphore2.jpg)

*图 2：在 Semaphore 中创建一个新项目。*

从项目页面（图 3）开始，您可以添加清单（Ansible 将管理的机器）、环境变量、密钥存储、存储库、任务模板和团队成员。请务必创建您的第一个密钥存储、清单和 playbook 存储库（您仍然必须手动创建 playbook — 我在本文顶部链接的文章中对此过程进行了描述）。

![Semaphore 项目](https://cdn.thenewstack.io/media/2023/04/d8ff0ef1-semaphore3.jpg)

*图 3：您的第一个 Semaphore 项目已准备就绪。*

恭喜，至此，Ansible 应该更容易管理了。

## Ansible 自动化平台常见问题解答

**问：什么是 Ansible？**

答：Ansible 是一个开源 IT 自动化平台，可以配置系统、部署软件和编排高级工作流程。

**问：如何开始使用 Ansible？**

答：要开始使用 Ansible，您需要在 LAN 中的服务器上安装它。您可以从 Ansible 官方网站下载最新版本，也可以使用 pip 等 Python 包管理器。

**问：什么是 Ansible 中的清单文件？**

答：清单文件列出了由 Ansible 管理的所有主机。它用于指定应将哪些机器包含在 playbook 或 playbook 集合中。

**问：如何在 Ansible 中创建一个新的 playbook？**

答：要创建一个新的 playbook，您需要编写一个包含必要配置的 YAML 文件。该文件将包括任务、主机和定义自动化过程的其他设置。

**问：Ansible playbook 中的“运行一次”和“无限重复”有什么区别？**

答：在 Ansible playbook 中，“运行一次”意味着 playbook 将仅在每个主机上执行一次，而“无限重复”允许您将任务设置为无限期重复，直到它失败或成功。

**问：我可以在多个操作系统上使用 Ansible 吗？**

答：是的！Ansible 支持许多不同的操作系统，包括 Linux、macOS 和 Windows。您还可以在本地和远程主机上使用 Ansible。

**问：如何在 Ansible 环境中管理用户权限？**

答：在一个安全的 Ansible 环境中，您应该确保用户拥有运行 playbook 或访问清单文件所需的最低权限。这有助于防止未经授权访问您的基础设施。

**问：Ansible 中的 Bolt 是什么？**

答：Bolt 是一个命令行界面，用于在不编写 playbook 文件的情况下运行 plays。它允许您使用简单的语法执行特定任务，从而可以轻松地自动化重复性任务。

**问：我可以将 Ansible 与其他工具和服务集成吗？**

答：是的！Ansible 可以很好地与许多第三方工具和服务集成，例如 AWS EC2、Docker、Kubernetes 和 Jenkins。您还可以使用自定义插件来扩展其功能。

**问：如何解决 Ansible playbook 中的问题？**

答：要解决 Ansible playbook 的问题，您需要检查日志（通常存储在 logs 目录中）中是否有任何错误消息或警告。