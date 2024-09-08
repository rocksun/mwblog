# 学习 Linux？从这里开始

![学习 Linux？从这里开始的特色图片](https://cdn.thenewstack.io/media/2024/09/fa8b210b-zetong-li-my06s-wg_zc-unsplash-1024x682.jpg)

学习 Linux 从未如此简单。现在有大量资源，很多动手实践的机会，以及比以往更友好的发行版。你可能面临的最大挑战是如何制定学习计划。

本文提供了一些关于特定主题领域以及何时学习它们的建议。将其用作学习计划，为工作变动、认证考试或新的开发项目做准备。它与我以及其他人撰写的 [The New Stack](https://www.thenewstack.io/Linux) 上的当前（和未来）文章相对应，这些文章提供了更深入的解释。

## 动手实践至关重要

对于许多新的 IT 人员来说，在 [命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 上工作令人望而生畏。然而，这是一项必要的技能，一旦你习惯了，你会发现它比预期的更容易。命令行管理提供了图形界面所没有的功能，包括：

**脚本**: 命令可以放在系统执行的文本文件中，从而实现复杂的自动化任务，这些任务可以通过单个命令轻松启动。**速度**: 对于熟悉 Bash 的人来说，命令行界面通常比鼠标驱动的交互更快（包括诸如制表符补全和历史记录之类的技巧，以提高效率）。**其他选项**: 图形界面通常只在其菜单中包含标准任务，而命令通常具有许多额外的功能、选项和参数，这些功能、选项和参数可能是必要的，但不太常用。**不需要图形界面**: 与大多数 Windows 和 macOS 安装不同，许多 Linux 服务器不包含图形界面，因为它会增加额外的开销。在这种情况下，命令行管理是主要选项。

[构建一个实验室环境](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)，其中包含两个或三个 Linux 虚拟机，将使学习以下技能变得更容易。没有什么比动手实践更好了！

当你忘记命令选项或子命令时，不要忘记使用手册页。

如今，大多数 Linux 发行版要求用户使用非特权（非 root）用户帐户登录。然后，用户可以使用 [sudo](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) 为特定委托的任务提升权限。避免 root 登录被认为是 Linux 安全最佳实践。

## 学习访问控制方法

管理对文件和文件夹的访问是 Linux 系统管理员的一项关键技能。访问控制从 [用户帐户](https://thenewstack.io/linux-user-and-group-management/) 开始，它建立用户的身份。这些帐户可以被放置在组中，以便于管理。

命令: | 描述: |
------- | -------- |
useradd | 创建用户 |
usermod | 修改用户 |
userdel | 删除用户 |
groupadd | 创建组 |
groupmod | 修改组 |
groupdel | 删除组 |

计算机还维护基本资源，例如 [文件和目录](https://thenewstack.io/linux-file-management/)。管理员和用户创建、修改和删除这些资源。掌握管理文件和目录的各种命令，使你能够高效地使用这些资源。

命令: | 描述: |
------- | -------- |
mkdir | 创建目录 |
touch | 创建文件或更新其时间戳 |
ls | 列出目录的内容 |
cd | 更改到不同的目录 |

一旦系统了解用户的身份以及存在哪些文件资源，它就可以执行访问控制。权限与文件相关联，以指定哪些帐户具有哪些权限。每当用户尝试管理文件时，都会检查此访问列表。

[Linux 权限](https://thenewstack.io/linux-how-file-permissions-work/) 不同于 Windows 访问控制。有三个级别的访问权限（读、写和执行），它们使用诸如
chmod 和
chown 之类的命令应用于三个身份（用户（所有者）、一个组和所有其他人）。Linux 权限比 Windows 权限更易于管理，但不太健壮。诸如访问控制列表 (ACL) 权限之类的功能确实增加了重要的功能。

学习管理用户和权限是 Linux 管理的基础，因此务必掌握这些技能。

![](https://cdn.thenewstack.io/media/2024/07/dbe42982-ls-l.png)

## 管理硬件、服务和进程

Linux 服务器的目的是提供服务。这些服务可能包括文件存储、打印、网站访问、数据库托管等等。在部署服务之前，确定系统是否具有 [硬件容量](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/) 来支持该角色。Linux 包含许多用于报告硬件的内置命令，包括 top、lshw 等等。
现代 Linux 发行版通常依赖于 systemd 来 [管理服务](https://thenewstack.io/linux-skills-manage-system-services/)。您可以使用 systemctl 命令和一系列标准子命令与 systemd 交互。这些命令允许您启动、停止、重启、启用和禁用服务。主要任务通常是重启服务，这对于配置更改或故障排除是必要的。

| 命令： | 描述： |
|---|---|
| systemctl status {service} | 显示服务的当前状态 |
| systemctl stop {service} | 临时停止服务 |
| systemctl start {service} | 临时启动服务 |
| systemctl restart {service} | 配置更改后重启服务 |
| systemctl enable {service} | 使服务在系统启动时启动 |
| systemctl disable {service} | 阻止服务在系统启动时启动 |

![](https://cdn.thenewstack.io/media/2024/07/2f7ee41d-systemctl-status-sshd.png)

进程是正在运行的代码的实例。这些可能是 Linux 本身的一部分，也可能与系统上托管的服务和应用程序相关。系统管理员在性能监控、安全审计、故障排除等过程中 [审查这些进程](https://thenewstack.io/linux-manage-system-processes/)。审查进程可以让管理员了解 Linux 设备上正在发生的事情。

评估硬件和管理服务是 Linux 用户的一项重要技能。如果您正在使用学习计划来组织您的 Linux 学习，请将这些概念和实用程序作为一个单元来学习。

## 选择和部署 Linux 发行版

微软和苹果只销售和维护少量操作系统版本。由于其开源性质，Linux 允许任何人创建 [发行版](https://thenewstack.io/choosing-a-linux-distribution/)，并且它不像闭源操作系统那样严格地执行操作系统版本。结果是，数千个版本的 Linux 可供使用，选择一个通常很困难。

术语 *发行版* 指的是 Linux 内核、各种应用程序和目的的组合。发行版通常专门针对特定角色，例如最终用户工作站、Web 服务器或物联网操作系统。选择发行版意味着找到（或创建）一个与您的目的相匹配的发行版。

![](https://cdn.thenewstack.io/media/2024/07/8b9e7629-distrowatch.png)

您还必须注意 [安装选项](https://thenewstack.io/how-to-install-linux/)。您将在 [裸机硬件或虚拟机](https://thenewstack.io/linux-choose-an-installation-platform/) 上安装 Linux 吗？它将是本地还是基于云的？它将依赖于哪个处理器（英特尔或 ARM）？它需要多少 RAM、存储容量和网络访问？

最后，启动安装过程。大多数现代 Linux 发行版使用安装向导来简化此过程。

培养选择和安装 Linux 发行版的知识，可以帮助您将专门的 Linux 版本部署到用户、服务器、云环境、物联网生态系统等。

## 维护系统

Linux 部署可能存在多年。它是一个极其稳定且寿命长的操作系统，这使得维护成为一个关键问题。除了通常的内核和应用程序更新之外，还要注意 [存储容量](https://thenewstack.io/how-to-manage-linux-storage/)。这似乎是始终被消耗的资源。存储在本地 Linux 工作站或服务器上的文件可能会填满存储空间。高访问时间会让用户感到厌烦，因此请将存储容量保持在合理水平，并在必要时进行升级。

![](https://cdn.thenewstack.io/media/2024/07/e55d9ea0-df-h.png)

日志文件维护系统活动的记录，以便您可以评估性能、安全性和整体运行状况。养成定期检查日志的习惯。将日志文件集中起来，以便更容易地跨多个系统进行归档和分析，这也是一个好主意。Linux rsyslog 服务使此过程变得简单。

包管理器简化了应用程序维护。对于新用户来说，Linux 最令人困惑的方面之一是，各种发行版依赖于不同的包管理器。实际上，并没有一个普遍认可的工具来部署、更新和删除软件。计划学习您选择的发行版使用的任何包管理器。

| 发行版： | 常用包管理器： |
|---|---|
| Red Hat 及相关 | dnf、yum、rpm |
| Debian 及相关 | apt |
| SUSE 及相关 | zypper |
## 配置网络

Linux 可以轻松地集成到基于 IP 的网络中。管理员可以使用 [Nmap](https://nmap.org/) 和 [Wireshark](https://www.wireshark.org/) 等标准工具配置静态或动态 IP 地址并监控网络。使用防火墙允许和拒绝进出系统的正确流量也很重要。几乎所有 Linux 发行版都包含防火墙，尽管其界面各不相同。大多数防火墙默认情况下采用“拒绝所有”配置，期望管理员手动指定允许流量的例外情况。一些防火墙假设一些基本协议，并为这些协议打开端口。远程管理工具 SSH 就是一个很好的例子。

![](https://cdn.thenewstack.io/media/2024/07/ff16665c-firewall-cmd-listall.png)

说到 SSH，请实施基于密钥的身份验证，以简化 SSH 连接。基于密钥的身份验证还可以实现集中式配置管理，使自动化工具能够在没有用户干预的情况下连接到远程系统。此功能对于扩展资源、管理安全性和部署应用程序版本至关重要。

| 步骤： | 描述： |
|---|---|
| ssh-keygen | 生成唯一的公钥-私钥对 |
| ssh-copy-id remotehost | 将公钥复制到远程主机 |
| ssh remoteuser@remotehost | 使用 SSH 启动远程连接 |

## 总结

如果您计划学习 Linux，请做好付出大量努力的准备。然而，回报是巨大的。您将能够组装一个系统，为用户提供服务，提供安全的日常使用，或 [针对编程进行优化](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/)。掌握命令行还可以为您提供更高的速度和自动化机会。

将以上类别作为学习计划的一部分，然后发展每个类别中列出的个人技能，以保持专注而不感到不知所措。当您对这些主题感到满意时，您可以探索其他领域，例如 Web 服务器配置、自动化和更高级的存储选项。

请记住，Linux 也是 [主要的云平台](https://thenewstack.io/microsoft-linux-is-the-top-operating-system-on-azure-today/)。您将在物理 Linux 服务器管理中学习的许多技能也适用于云 VM 和 [容器](https://thenewstack.io/alpine-linux-heart-docker/)。

立即开始您的 Linux 系统管理之旅，并准备好使用这个强大而通用的操作系统。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)