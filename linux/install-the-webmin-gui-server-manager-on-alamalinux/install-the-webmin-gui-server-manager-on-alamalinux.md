
<!--
title: 在 AlamaLinux 上安装 Webmin GUI 服务器管理器
cover: https://cdn.thenewstack.io/media/2024/07/d7904a3a-webadmin-dashboard.png
-->

仍然不习惯使用 Linux 命令行？试试 Webmin，它是一个图形界面，可以帮助您管理和配置 Linux 服务器。

> 译自 [Install the Webmin GUI Server Manager on AlamaLinux](https://thenewstack.io/install-the-webmin-gui-server-manager-on-alamalinux/)，作者 Jack Wallen。

如果您是 [Linux](https://www.thenewstack.io/Linux) 新手，您可能不想从 [命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 执行所有操作。

虽然 CLI 提供了强大的功能和灵活性，但对于那些没有在终端窗口中管理过服务器的人来说，它可能有点让人不知所措。对于那些从 Windows Server 迁移到 Linux 的人来说尤其如此。

幸运的是，有很多工具可用于此目的。开箱即用，您始终可以为 [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/) 启用 [Cockpit GUI](https://cockpit-project.org/)，但该界面在可添加的第三方模块方面有点有限。

还有 [Webmin](https://webmin.com/)，它已经存在很长时间了。我记得，当我第一次开始使用 Linux 作为服务器操作系统时，Webmin 很快就成为了我的好朋友。有了这个强大的 GUI 应用程序，我不再觉得我的大脑要因为学习如此多的命令而爆炸了。

Webmin 为我提供了完成工作所需的所有功能，同时我学习了管理服务器所需的命令行工具的来龙去脉。

但即使 CLI 现在对我来说已经成为第二天性，有时我仍然更喜欢使用 GUI 来完成任务。例如，如果我有许多服务器要管理，或者如果我只需要快速完成一项复杂的任务。

开箱即用，Webmin 包含模块来帮助您管理：

- Bacula 备份
- 启动和关闭
- 密码管理
- 磁盘和网络文件系统
- 磁盘配额
- 文件系统备份
- 日志文件轮换
- MIME 类型程序
- PAM 身份验证
- 正在运行的进程
- 计划命令
- 计划的 cron 作业
- 软件包更新
- 软件包
- 系统文档
- 系统日志
- 用户和组
- 服务器（如 SSH）
- HTTP 隧道
- Perl 模块
- 受保护的 Web 目录
- 防火墙
- Kerberos5
- NIS 客户端和服务器
- TCP 包装器
- Linux RAID
- 本地磁盘上的分区
- 集群

如果这还不够，还有一个网站可以搜索 [第三方模块](https://www.webmin.com/cgi-bin/search_third.cgi?modules=1)，这些模块可以极大地扩展 Webmin 的功能集。

我想带您逐步了解在 AlmaLinux 上安装 Webmin 的步骤。

## 您需要什么

要安装 Webmin，您需要一个正在运行的 AlmaLinux 实例和一个具有 sudo 权限的用户。您还需要访问 root 用户以进行初始 Webmin 登录。仅此而已。让我们来做一些 GUI 魔法吧。

## 更新 AlmaLinux

在开始安装之前，最好先升级 AlmaLinux。需要注意的是，如果在此过程中升级了内核，则需要重新启动机器才能使更改生效。

要升级 AlmaLinux，登录到您的服务器，打开一个终端窗口并发出以下命令：

```
sudo dnf update -y
```

升级完成后，如果需要，请重新启动。

## 添加必要的存储库

由于 Webmin 在标准存储库中找不到，因此您必须为 dnf 创建一个新条目。使用以下命令创建文件：

```
sudo nano /etc/yum.repos.d/webmin.repo
```

在该文件中，粘贴以下内容：

```
[Webmin]
name=Webmin
mirrorlist=https://download.webmin.com/download/yum/mirrorlist
enabled=1
gpgkey=http://www.webmin.com/jcameron-key.asc
```

使用键盘组合 Ctrl+x 保存并关闭文件。运行另一个更新命令，以便 dnf 了解新的存储库（*sudo dnf update*）。

## 安装 Webmin

下一步是安装 Webmin 管理器，这可以通过以下命令完成：

```
sudo dnf install webmin -y
```

完成后，Webmin 服务将运行并准备接受连接。但是，您仍然必须打开防火墙，否则您将无法从浏览器访问 GUI。要永久打开所需的端口，请发出以下命令：

```
sudo firewall-cmd --add-port=10000/tcp --permanent
```

然后，您必须使用以下命令重新加载防火墙：

```
sudo firewall-cmd --reload
```

## 登录 Webmin

Webmin 运行后，打开与托管服务器位于同一网络上的 Web 浏览器，并将其指向 *http://SERVER:10000*（其中 SERVER 是托管服务器的 IP 地址）。

您将看到一个登录窗口（图 1）。

![](https://cdn.thenewstack.io/media/2024/06/016817ee-webmin1.jpg)

*图 1：Webmin 登录窗口*

对于您的第一次登录，您必须使用 *root* 帐户，因为您必须添加任何需要从 Webmin 内部访问 GUI 的用户。输入 *root* 作为用户，然后输入 root 用户密码。

登录后，您应该做的第一件事是将任何用户添加到 Webmin，这样 root 用户就不必再使用。为此，请展开侧边栏中的 Webmin 条目，然后单击 Webmin 用户。
您实际上并没有创建新用户，而是将现有用户转换为 Webmin 用户。为此，请单击“创建新的 Webmin 组”（图 2）。

![](https://cdn.thenewstack.io/media/2024/06/ded05a78-webmin2.jpg)

*图 2：Webmin 用户页面是您可以转换现有用户的地方。*

接下来，为新组命名（例如 admin），然后单击“创建”。回到 Webmin 用户页面，单击“将 Unix 用户转换为 Webmin 用户”。在结果页面（图 3）上，您可以选择所有用户或键入要转换的用户列表。

![](https://cdn.thenewstack.io/media/2024/06/7b16b6c1-webmin3.jpg)

*图 3：将 Unix 用户转换为 Webmin 用户*

确保从左侧窗格的 Webmin 组下拉菜单中选择新添加的组，然后单击“立即转换”。转换用户后，您需要返回到新组并选择该组可以访问的 Webmin 模块。为此，请单击“可用的 Webmin 模块”，然后浏览完整列表（图 4），选中该组应具有访问权限的任何/所有模块。

![(https://cdn.thenewstack.io/media/2024/06/50dbf75f-webmin4.jpg)]

*图 4：向新的 Webmin 组添加模块*

完成此操作后，单击“保存”，分配的模块现在可供该组内的用户访问。

您现在可以注销 Webmin 并以标准用户身份登录。

恭喜！您现在拥有 Webmin GUI 的强大功能，可以帮助您管理和配置 AlmaLinux 服务器。
