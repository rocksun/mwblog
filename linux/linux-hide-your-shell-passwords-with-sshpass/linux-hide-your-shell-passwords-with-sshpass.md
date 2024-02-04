<!--
title: 通过sshpass隐藏Shell密码
cover: https://cdn.thenewstack.io/media/2024/02/42c43604-sshpass-1024x682.jpg
-->

避免硬编码的陷阱，选择sshpass更为安全可靠。

> 译自 [Linux: Hide Your Shell Passwords with sshpass](https://thenewstack.io/linux-hide-your-shell-passwords-with-sshpass/)，作者 Jack Wallen。

在你[与Linux的交互](https://thenewstack.io/linux-create-encrypted-tunnels-with-ssh-port-forwarding/)中的某个时刻，你将会编写一个 shell 脚本，不管是 [Bash](https://thenewstack.io/microsoft-plants-bash-windows-freaks-everyone/) 还是其他。它可能只是一行代码，也可能是你曾经编写的任何程序一样复杂。无论如何，它们都有助于使Linux成为地球上[最灵活](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)和强大的操作系统。

当你深入研究Linux中的 shell 脚本时，你可能会遇到一种情况，即你需要在脚本中包含一个密码。当这种情况发生时，你肯定不希望将密码硬编码到脚本中。

或者，如果最终需要输入密码，你就无法自动化脚本。任何能够访问你的计算机的人都可以查看该脚本，然后访问与该密码相关联的任何账户。此外，该脚本的 cron 作业将失败。

例如，你可能创建一个备份脚本，该脚本使用 rsync 通过网络传输并需要用户密码以确保安全性。比如，你有一个存储特定信息的 /data 目录，你需要定期备份。你已经设置好了所有必要的权限，剩下的就是创建一个备份，将内容保存到远程机器。

这样的脚本可能如下所示：

```bash
#!/bin/bash
rsync -av /data USER@SERVER:/home/USER/databackup
```

其中 USER 是远程用户名，SERVER 是远程服务器的IP地址或域名。运行脚本时，你将会被提示输入密码。

那么，如何解决这种情况呢？

## 通过sshpass的一点帮助...

应用程序sshpass专为实现密码自动化而创建。这个非交互式工具使得能够自动化shell脚本，即使它们需要密码。

让我演示一下它是如何工作的...

### 安装sshpass

要使用sshpass，你需要一个正在运行的Linux发行版。我将演示在Ubuntu Server 22.04上的操作，但该应用程序也可以安装在基于Fedora的发行版上。你还需要一个具有sudo权限的用户。

要在基于Ubuntu的发行版上安装sshpass，请打开终端窗口并执行以下命令：

```bash
sudo apt-get install sshpass -y
```

对于基于Fedora的发行版，该命令将是：

```bash
sudo dnf install sshpass -y
```

安装工作就完成了。

### 使用sshpass

我们将继续使用我们的备份脚本想法。首先，我们必须创建一个加密文件来保存我们的密码。使用以下命令创建文件：

```bash
nano ~/.password
```

你可以随意命名该文件，但我建议在文件名的开头使用一个点，使其成为隐藏文件。

在文件中添加用于shell脚本中的账户的密码，并使用Ctrl-x键盘快捷键保存。

使用以下命令加密文件：

```bash
gpg -c ~/.password
```

系统将提示你输入和验证加密密码。

以上命令将创建一个新文件，名为.password.gpg，其中包含密码的加密版本。然后你可以删除~/.password文件。

### 创建Shell脚本

记住，我们还是继续使用我们的简单备份脚本。首先，我将演示如何使用[sshpass](https://linux.die.net/man/1/sshpass)命令简单传递密码（以便你了解它的工作原理）。例如，一个需要用户验证的rsync备份命令看起来像这样：

```bash
sshpass -p "PASSWORD" rsync -av /data USER@SERVER:/home/USER/databackup
```

其中PASSWORD是远程用户密码，USER是远程用户名，SERVER是远程服务器的IP地址或域名。sshpass应用程序将把密码传递给rsync命令，一切都应该如预期般工作。

当然，你不想硬编码密码，对吧？为了避免这种情况，你需要在脚本中加入一些创意，下面是它的样子：

```bash
#!/bin/bash
gpg -d -q ~/.password.gpg | sshpass rsync -av /data USER@SERVER:/home/USER/databackups
```

其中USER是远程用户名，SERVER是远程服务器的IP地址或域名。

在这里，我们首先解密.password.gpg文件，并将其输出发送到sshpass，然后由rsync用于连接到远程服务器进行备份。

这有点棘手但是它能够正常工作。

借助sshpass的帮助，你可以创建能够使用加密密码的Shell脚本，将其传递给脚本内的sshpass，而无需硬编码密码或与脚本交互。

通过这样做，你在系统上增加了一层安全性，同时也使得可以创建自动化脚本来执行几乎任何你需要的任务。

