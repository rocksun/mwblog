
<!--
title: Linux 技能：管理系统服务
cover: https://cdn.thenewstack.io/media/2024/06/304436eb-derek-oyen-3xd5j9-drda-unsplash.jpg
-->

系统管理员负责 Linux 设备上的服务管理。以下是他们需要了解的有关配置、启动选项、安全等方面的信息。

> 译自 [Linux Skills: Manage System Services](https://thenewstack.io/linux-skills-manage-system-services/)，作者 Damon M Garn。

服务是长期运行的应用程序，为用户、本地系统或远程系统提供功能。服务支持了我们今天认为理所当然的大部分网络功能。服务的示例包括电子邮件、网页、打印作业、文件共享等的传输。

系统管理员负责 Linux 设备上的服务管理。这些任务包括配置、启动选项、安全等。

您需要一个可用的 Linux 发行版才能使用以下服务管理示例。您可以使用物理或虚拟计算机，任何发行版都应该可用。请注意，某些发行版包含与其他发行版不同的工具。此处描述的工具可在大多数 Linux 发行版中找到。

本文关于服务的文章属于一系列涵盖各种系统管理员主题的 Linux 文章，包括硬件识别和管理系统进程。您可以按照 [Linux：Linux 技能模块存储库配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) 文章中的信息构建一个实验室环境。如果您需要复习 Linux 命令语法，请阅读 [了解 Linux 命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)。

在本系列中，我们还介绍了 [如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/) 以及 Linux 内核如何 [与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)。

## 什么是一些常见服务？

在大多数 Linux 系统上，您可能会定期遇到一些服务。您可能会在配置和故障排除任务中操作或检查它们的状态。

以下列表提供了一些示例服务供您熟悉，并总结了它们的功能。

- sshd：安全外壳 (ssh) 是一个重要的 Linux 远程管理工具。
- httpd：Apache Web 服务器是 Linux 系统上的标准 Web 服务器服务。
- firewalld：防火墙使用规则过滤进出系统的网络流量，以确定允许或阻止什么。
- cupsd：通用 Unix 打印系统 (CUPS) 提供了对打印服务器的出色管理。
- rsyslogd：rsyslog 服务管理系统和应用程序日志文件。

我将在这里澄清一个令人困惑的点：守护进程、服务和进程之间的区别。

- Linux 守护进程在后台运行，没有控制终端界面。它响应事件或时间来执行任务。它是一种服务。
- Linux 服务响应来自其他程序的请求。并非所有服务都是守护进程。
- Linux 进程是正在运行的代码的实例。守护进程和服务可能具有进程，但其他软件（例如 Chrome Web 浏览器或 Vim 文本编辑器等最终用户应用程序）也可能具有进程。

## 检查服务状态

现代 Linux 设备上的服务管理命令是 [systemctl](https://www.man7.org/linux/man-pages/man1/systemctl.1.html)。语法是命令、子命令、服务名称。它看起来像这样：

```
systemctl <子命令> <服务名称>
```

此示例通过显示 status 子命令和 sshd 服务演示了语法：

```
$ systemctl status sshd
```

在使用 systemctl 时，您可能需要使用 sudo 命令提升您的权限。

注意：以 root（管理员）用户身份登录 Linux 系统是一种很差的安全做法。大多数系统会强制您以普通用户身份登录，然后使用 [sudo](https://linux.die.net/man/8/sudo)（超级用户执行）命令提升您的权限。在使用 sudo 时，系统可能会提示您输入密码。

状态信息允许您查看服务是否正在运行。如果它没有运行，您需要启动它才能使用其功能。

![](https://cdn.thenewstack.io/media/2024/04/fa868594-systemctl-status-sshd.png)

*图 1：systemctl 状况子命令显示了该服务目前的状况。在本例中，该服务已加载并处于活动状态。*

状态结果分为三类，每类有几种可能的状态。以下列表显示了每种类别的一些可能状态。

- **单元状态**
  - active（正在运行）——服务正在运行（这通常是期望的结果）。
  - inactive——服务未运行（您可能已停止它）。
  - failed——服务失败且未运行。
- **已加载状态**
  - loaded——单元配置文件已加载。
  - error——单元配置文件加载失败。
- **已启用状态**
  - enabled——服务随系统自动启动。
  - disabled——服务不会随系统自动启动。

### 使用 Tab 键显示子命令

像 systemctl 或 ip 有许多子命令，记住所有这些命令可能具有挑战性。显示可用子命令的一个技巧是使用 Linux 选项卡补全功能。键入命令，输入一个空格，然后按两次 Tab 键。可用子命令将显示出来。

```bash
systemctl <tab><tab>
```

确保在 systemctl 后面留一个空格。

## 服务需要哪些管理？

服务需要哪些类型的管理？服务需要安全设置、配置选项、资源访问、网络访问等。Linux 将这些配置存储在文本文件中。每个服务都有一个或多个文本文件。当服务启动（通常在计算机启动时）时，它会读取文本文件并应用设置。

这是一个重要的细节。服务在启动时使用在文本文件中找到的设置。如果管理员更改了这些设置，则必须重新启动服务才能使其重新读取配置文件并应用新设置。

因此，管理服务的第一个系统管理员任务之一是重新启动它们。

## 启动、停止或重新启动服务

使用 systemctl 命令管理服务。该命令识别许多子命令，包括重新启动选项。

语法为：

```
systemctl restart <servicename>
```

例如，要重新启动系统上的 sshd 服务，请键入：

```
$ sudo systemctl restart sshd
```

![](https://cdn.thenewstack.io/media/2024/04/0f0cf374-sudo-systemctl-restart-sshd.png)

*图 2：重新启动服务，可能是因为配置更改。*

SSH 服务关闭然后重新启动。执行此操作时，它会应用在 SSH 配置文件中找到的任何设置（通常位于 /etc/ssh/sshd_config）。

重新启动网络服务（如 sshd 或 httpd）时需要考虑的一点是，它会断开现有连接，可能会中断用户活动。您可以选择重新加载配置，而不是重新启动，这将保持现有连接。

```
$ systemctl reload sshd
```

对于重新启动和重新加载这两种用例，您可能对配置文件进行了更改，并且服务需要实现新设置。

您还可以使用 stop 和 start 子命令手动管理服务：

```
$ sudo systemctl stop sshd

$ sudo systemctl start sshd
```

![](https://cdn.thenewstack.io/media/2024/04/5b7c318c-systemctl-stop-start-sshd.png)

*图 3：手动停止和启动服务，例如在进行故障排除时。*

您可能希望在故障排除、安全审计或其他事件期间暂时停止服务，此时您尝试衡量特定服务对系统的影响。完成后，您可以再次手动启动服务。

请注意，对于其中一些命令，系统通常不会提供反馈。它只是管理服务。

## 将服务配置为自动启动

启动和停止服务仅管理它们在当前系统运行时（系统的当前实例）的状态。管理员通常需要指示服务在系统启动时自动启动或在系统启动时不启动。这些设置的适用子命令是 enable 和 disable。

要使 SSH 服务在系统启动时自动启动，请键入：

```
$ sudo systemctl enable sshd
```

要阻止 SSH 在系统启动时启动，请键入：

```
$ sudo systemctl disable sshd
```

您可能在初始安装后启用服务。

### 服务管理示例

假设您刚刚在 Linux 系统上安装了 Apache Web 服务并希望对其进行管理。编辑配置文件后，您的下一步是启动服务，以便您可以测试它是否按预期工作。满意后，启用它，以便它在系统启动时启动。最后，使用 status 子命令确认服务正在运行。

以下是命令示例：

```
$ sudo systemctl start httpd

$ sudo systemctl enable httpd

$ systemctl status httpd
```

您可以使用 --now 选项一次启动和启用服务：

```
$ sudo systemctl enable --now sshd
```

### 检查服务的启动配置

is-enabled 子命令可用于检查服务的启动状态，而无需进行任何更改。

```
$ systemctl is-enabled ssh
```

该命令返回三个响应之一：

- enabled – 服务自动运行。
- disabled – 服务不会自动运行。
- static – 服务在被其他服务调用时运行。

您还可以使用 is-active 子命令查看服务的当前状态：

```bash
$ systemctl is-active ssh
```

![](https://cdn.thenewstack.io/media/2024/04/e9d09505-systemctl-is-enabled-active-ssh.png)
*图 4：检查服务是否已启用且处于活动状态。请注意，此处服务名为“ssh”。*

请注意，服务名称在此发行版中别名为 ssh。

### 阻止服务启动

使用 mask 和 unmask 子命令阻止或允许服务启动。mask 子命令阻止服务通过 systemctl start 命令手动启动或被其他服务调用。unmask 子命令会反转设置，允许服务在启动时运行。使用上面学到的相同 systemctl 语法与这两个子命令一起使用。

## 总结

服务管理是 Linux 系统管理员的日常工作。幸运的是，`systemctl` 语法相当简单。您主要会使用 `status` 和 `restart` 子命令。不要忘记服务如何发现其配置设置：它们在启动时读取配置文件，并且仅在您重新启动它们时才再次读取它（以查找您的更改）。这意味着重新启动服务是系统和服务配置中的一个基本步骤。

虽然本文没有直接关注安全性，但值得注意的是，服务管理是加固的关键部分。加固系统包括删除其指定角色不需要的所有内容。这意味着使用 `systemctl` 禁用任何不必要或未使用的服务。

使用您的实验室计算机练习 `systemctl` 命令并探索各种子命令。务必练习制表符补全技巧以显示我在文章开头介绍的可用子命令。今天学习此工具将使您的 Linux 管理之旅变得更加轻松。
