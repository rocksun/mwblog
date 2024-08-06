# 如何管理 Linux 日志服务

![关于如何管理 Linux 日志服务的特色图片](https://cdn.thenewstack.io/media/2024/06/a8082e57-thomas-park-i_dqdjghckw-unsplash-1024x660.png)

[Linux：Linux 技能模块库的配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) 文章。在本系列文章中，我们还介绍了
[如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/) 和
[安装平台](https://thenewstack.io/linux-choose-an-installation-platform/)，Linux 内核如何
[与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/) 以及如何
[管理 Linux 系统服务](https://thenewstack.io/linux-skills-manage-system-services/)，
[存储](https://thenewstack.io/how-to-manage-linux-storage/)，
[文件权限](https://thenewstack.io/linux-how-file-permissions-work/)，
[系统进程](https://thenewstack.io/linux-manage-system-processes/)，以及
[用户和组权限](https://thenewstack.io/linux-user-and-group-management/)。

日志文件是 Linux 用户排查系统问题、审计正常运行时间和管理安全配置的关键工具。与其他操作系统一样，Linux 包含强大的日志记录功能，用于跟踪登录尝试（成功和失败）、软件安装、应用程序错误、系统停止等信息。现代 Linux 系统依赖于两种日志服务：syslog 和 journald。常见的 syslog 实现是 [rsyslog](https://www.rsyslog.com/)。维护和查看系统日志是任何 Linux 管理员工作的重要组成部分。

本文介绍了 rsyslog 日志服务，并将其与较新的 journald 系统进行了比较。它使用实际的命令示例来管理服务和更新配置文件。

关于日志文件的讨论属于更广泛的 Linux 文章系列的一部分，涵盖了各种系统管理员主题，包括硬件识别和管理系统进程。您可以按照 [Linux：Linux 技能模块库的配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) 文章中的信息构建一个实验室环境来自己尝试这些命令。如果您需要复习 Linux 命令语法，请阅读 [了解 Linux 命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)。

本系列文章还介绍了 [如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/) 以及 Linux 内核如何 [与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)。

注意：以 root（管理员）用户身份登录 Linux 系统是一种糟糕的安全做法。大多数系统会强制您以普通用户身份登录，然后使用 [sudo](https://linux.die.net/man/8/sudo)（超级用户执行）命令来提升您的权限。使用
sudo 时，您可能会被提示输入密码。

## 了解和管理 rsyslog 服务

使用
`systemctl` 命令来管理 rsyslog 服务。您可以启动、停止和重启服务。这些选项在更改配置文件时非常有用。必须重启 rsyslog 服务才能读取更新的配置文件设置。

```
$ sudo systemctl restart rsyslogd
```

您可以使用
`systemctl enable` 和
`disable` 命令使服务在系统启动时启动或停止启动。以下是每个命令的示例：

```
$ sudo systemctl disable rsyslogd
$ sudo systemctl enable rsyslogd
```

这些命令和方法与您用于管理其他服务的命令和方法相同。

## 识别 /var/log 中的特定日志

Linux 发行版使用标准存储位置来存放日志文件。该位置是 `/var/log` 目录。该目录中存在其他日志和子目录。这些目录因发行版和已安装的应用程序而异。

使用
`cd` 命令更改到
`/var/log` 目录，然后使用
`ls` 命令 [列出内容](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)。

以下是 Fedora 和 Ubuntu Linux 的常见日志文件。请注意，某些日志在两个发行版之间有所不同。这是 Linux 发行版中常见的现象。

在 Fedora Linux 中找到的日志文件示例：

- `/var/log/messages`：系统日志，如内核、身份验证和服务
- `/var/log/secure` 或 `/var/log/auth.log`：身份验证日志
- `/var/log/boot.log`：启动日志
- `/var/log/kern.log`：Linux 内核日志条目
- `/var/log/dnf.log`：安装和其他包管理器事件
- `/var/log/utmp`：当前系统登录和连接
- `/var/log/btmp`：失败的登录信息
- `/var/log/wtmp`：utmp 条目的历史记录

请注意，上面提到的某些日志存在于较旧的 Linux 版本中。内核、服务、身份验证和其他功能的日志条目已在许多发行版中移至 journald 日志。
![](https://cdn.thenewstack.io/media/2024/06/12360ac3-ls-var-log.png)
Ubuntu Linux 中找到的日志文件示例：

- /var/log/syslog：系统日志，例如内核、身份验证和服务
- /var/log/kern.log：Linux 内核日志条目
- /var/log/auth.log：用户登录和 sudo 凭据使用
- /var/log/fail.log：身份验证失败尝试
- /var/log/lastlog：用户最近的登录
- /var/log/apt：安装和其他包管理事件

某些发行版会在 /var/log 目录中添加或删除日志，因此您可能需要查看特定 Linux 发行版的文档。上面的一些日志现在是 journald 日志机制的一部分，可能不再出现在 /var/log 目录中。

## 应用程序日志文件

许多应用程序与 rsyslog 集成以管理其日志。例如，rsyslog 可以管理和转发常见 Apache Web 服务器程序的日志文件。Apache 的日志通常位于基于 Red Hat 的系统上的 /var/log/httpd 或基于 Debian 的发行版上的 /var/log/apache2。Nginx Web 服务器和 MySQL 数据库等工具使用类似的日志记录方案。

## 读取和搜索日志文件

Syslog 日志文件是简单的文本文档，可以使用 cat 和 less 等应用程序轻松打开和读取。grep 和 tail 等工具还提供强大的过滤和搜索功能，可帮助您找到所需的确切内容。

### 使用 grep 搜索日志

大多数日志文件以纯文本形式存储其信息，使其易于阅读和搜索。例如，您可能希望检查 /var/log/dnf.log 以查看 vim 软件包是否已安装。使用 grep 模式匹配实用程序检查应用程序。

1. ```bash
$ sudo cat /var/log/dnf.log | grep -i vim |
```
![](https://cdn.thenewstack.io/media/2024/06/58d86955-dnf-log-vim.png)
应显示包含 vim 字符串的任何日志文件条目。grep 模式匹配器在这些情况下很有用。上面使用的 -i 选项使其忽略大小写。

### 使用 tail 搜索日志

另一个用于检查日志文件的有用工具是 tail 命令。它显示文件的底部。日志文件在底部存储最新的条目，因此您可以通过检查日志文件的末尾来查看最新的信息。

1. ```bash
$ tail /var/log/dnf.log |
```
您可以调整 tail 显示的行数，方法是使用 -n 开关和要查看的行数。以下示例显示 20 行而不是默认的 10 行。

1. ```bash
$ tail -n 20 /var/log/dnf.log |
```
但是，tail 最有用的标志可能是 -f 。此选项定期刷新 tail 输出，允许您打开一个终端窗口， tail 一个日志文件，并看到窗口定期更新最新的日志条目。

1. ```bash
$ tail -f /var/log/dnf.log |
```

## 什么是 journald？

如今，大多数 Linux 发行版都依赖 systemd 来进行系统初始化和服务管理，因为它提供了比旧的 init 系统更现代的优势。您将使用 systemctl restart sshd 等命令来 [管理服务](https://thenewstack.io/linux-skills-manage-system-services/) 与 systemd。

systemd 的另一个方面是日志文件管理。systemd 需要一种不同且更强大的日志记录机制，而不是 rsyslog 可以提供的。结果是 journald，这是一种在大多数当前发行版上可用的新日志文件机制。它收集来自 Linux 内核的信息。它还记录 systemd 管理的服务和应用程序的信息。

但是，许多关于 Linux 日志的讨论听起来好像您必须选择一个或另一个日志记录引擎。实际上，您可能同时使用 journald 和 rsyslog 来监控系统上发生的事情。

### journald 的优点和缺点

与任何其他实用程序一样，与类似服务相比，journald 也有其优点和缺点。以下是一些注意事项。

优点：

- journald 对条目进行索引，使查找速度更快。
- 轻松过滤和优先排序日志文件条目。
- 权限访问，用户可以查看与其工作相关的日志，而 root 可以查看所有日志条目。
- 内置灵活的日志轮换。

缺点：

- 它不能将日志本地转发到中央服务器以进行聚合。
- 它不使用标准文本文件来记录信息，这使得使用除 journalctl 命令以外的任何其他方法读取日志条目变得更加困难。

## 使用 journalctl 查看日志

journalctl 命令允许管理员配置 journald 设置并显示日志文件条目。它提供了广泛的自定义和灵活性。

需要注意的两个主要 journald 资源是：

- journald 日志的默认持久存储位置是 /var/log/journal 。
- 主要配置文件是 /etc/systemd/journald.conf 。

如果您被授予权限，请务必使用 sudo 命令。journald 会根据用户仔细过滤它显示的内容。
不带参数的 `journalctl` 命令按时间顺序显示最近的日志条目（最旧的条目排在最前面）。它会自动使用 `less` 实用程序将结果分成页面，因此您可以像使用 `less` 一样浏览条目。

使用 **q** 键退出日志。以下是 `journalctl` 命令的部分输出。

![](https://cdn.thenewstack.io/media/2024/06/55ed054a-journalctl.png)

要以相反的顺序显示日志（最新的条目排在最前面），请键入：

```
journalctl -r
```

使用 `-n` 标志并指定一个数字来显示有限数量的条目。例如，要显示五个条目，请键入：

```
journalctl -n 5
```

![](https://cdn.thenewstack.io/media/2024/06/714cb3eb-journalctl-n5.png)

一些 Linux 用户熟悉使用 `tail -f` 命令实时查看日志文件的技巧。`-f` 选项在 `journalctl` 命令中具有相同的功能，会自动刷新命令输出以实时显示最新的日志条目。使用 **Ctrl+C** 退出输出。

```
journalctl -f
```

`-k` 选项显示内核消息。当在内核级别排查问题时，此标志很有用，因为它可以避免服务日志条目的混乱。

![](https://cdn.thenewstack.io/media/2024/06/3d3994ec-journalctl-k-kernel.png)

添加 `| grep {string}` 命令来过滤您的 `journalctl` 输出。例如，您可能正在寻找系统启动序列中的错误或错误配置，这些错误或错误配置可能会减慢系统速度。要搜索的一个术语是“Unknown”。使用 `grep` 和 `-k` 选项来显示内核信息。

```
$ sudo journalctl -k | grep -i unknown
```

![](https://cdn.thenewstack.io/media/2024/06/0b3ceabc-journalctl-grep.png)

一些最重要的和最有趣的结果将来自特定的服务。将服务名称指定为 `journalctl` 命令的参数。例如，要显示与 `firewalld` 相关的日志，请键入：

```
journalctl -u firewalld
```

![](https://cdn.thenewstack.io/media/2024/06/60e7a8c8-journalctl-u-firewalld.png)

`-u` 标志代表单元，并为管理员提供了对显示的输出的进一步控制。

这些只是一些 `journalctl` 选项。它还提供按时间间隔和日志条目严重性进行过滤的功能。不难看出为什么 `journalctl` 受学习它的管理员的欢迎——它为过滤和管理日志数据提供了极大的灵活性。

## 将 journald 与 rsyslog 集成

rsyslog 和 journald 之间可以进行一定程度的集成。虽然 journald 不会将日志文件转发到远程中央服务器进行聚合，但它可以将日志条目转发到 rsyslog，然后 rsyslog 可以将它们转发到远程系统。这种方法允许管理员继续将日志集中起来进行审计和分析，同时仍然可以从 journald 从内核和 systemd 管理的服务中接收的额外信息中受益。

您可能会使用这两种机制来监控您的 Linux 服务器。

## 总结

管理员应定期查看日志文件以查找异常行为、意外操作、可疑登录尝试等。这样做有助于您更好地了解系统并识别潜在的安全或性能问题。您可能还需要在合规性或安全审计中证明日志文件维护。`grep`、`tail` 和 `less` 等命令可以帮助您查看和操作 rsyslog 日志文件条目。您将使用 `journalctl` 命令来查看 journald 管理的日志条目。

如果您管理的 Linux 系统不止几个，请考虑使用 rsyslog 的内置转发机制将日志文件集中到一台服务器上。对于 journald 日志来说，这更难实现，但可以做到。

管理 Linux 日志最令人困惑的部分之一是不同发行版之间的差异。希望您的组织已经标准化了一两个特定的发行版。如果是这样，请查看发行版的文档或维基，并记下它使用的日志文件。如果您的公司使用许多不同的发行版，这个过程会更难。

现在就开始学习哪些日志存在、它们在哪里以及如何过滤或搜索它们以找到您需要的内容。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)