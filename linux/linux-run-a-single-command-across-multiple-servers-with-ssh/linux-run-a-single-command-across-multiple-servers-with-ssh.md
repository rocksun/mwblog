
<!--
title: Linux：使用 SSH 在多台服务器上运行单个命令
cover: https://cdn.thenewstack.io/media/2024/03/46226c01-marathon-2366475_1280.jpg
-->

您并不总是需要第三方软件来控制多个 Linux 服务器——当一点脚本魔术可以完成这项工作时，就不需要。

> 译自 [Linux: Run a Single Command across Multiple Servers with SSH](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/)，作者 Jack Wallen。

使用 Linux，总有许多途径可以达到同一目的地。这实际上是此操作系统的优势之一：由你决定如何从 A 点到达 B 点。可以将它视为操作系统的“疯狂填词”。

以在远程计算机上运行命令的能力为例。有很多选项，例如 [Red Hat](https://www.openshift.com/try?utm_content=inline-mention) Ansible、Puppet 和 Chef，它们都是非常棒的平台，[但可能有点过剩](https://thenewstack.io/in-space-you-might-still-need-two-factor-authentication/)。

考虑一下：你有一个工作站和 5 或 10 台需要管理的服务器。你可以使用该工作站并通过安全外壳登录到每台服务器，运行必要的命令，退出服务器，然后冲洗、洗涤和重复，直到处理好所有事情。

这很耗时，并且可能导致问题。想象一下，如果你在错误的计算机上运行了错误的命令。你肯定不希望发生这种情况。

你还希望尽可能简化操作，这就是这个方便的 SSH 技巧可以让你轻松一点的原因。

假设你有多台 Ubuntu 服务器和 Rocky Linux 服务器，你希望确保每台服务器始终是最新的。正如我之前提到的，你可以登录到每台 Ubuntu 服务器并发出以下命令：

```
sudo apt-get update && sudo apt-get upgrade -y
```

然后，你可以登录到每台 Rocky Linux 服务器并发出命令：

```
sudo dnf update -y
```

这可能需要比你可能有的空闲时间更多的时间。那么，我们如何让 [Secure Shell](https://thenewstack.io/ssh-made-easy-with-ssh-agent-and-ssh-config/)（[SSH](https://thenewstack.io/dr-torq-go-remote-with-ssh/)）为我们做繁重的工作？借助 [SSH](https://thenewstack.io/create-a-local-git-repository-on-linux-with-the-help-of-ssh/) 配置文件，这实际上非常容易。

让我告诉你如何操作。

## 创建 SSH 配置文件

我们要做的第一件事是创建一个 SSH 配置文件。我们将坚持我们的 [Ubuntu 和 Rocky Linux 服务器](https://thenewstack.io/ubuntu-server-struggles-with-post-docker-kubernetes-installs/)示例。使用以下命令创建配置文件：

```
nano ~/.ssh/config
```

记住，你将需要以将运行该命令的用户身份创建该文件。我们将在该文件中创建四个条目（你可以根据需要创建任意多个条目）——两个用于 Ubuntu 服务器，两个用于 Rocky Linux 服务器——其中包含以下信息：

- ubuntu-web 在 192.168.1.100
- ubuntu-db 在 192.168.1.101
- rocky-web 在 192.168.1.102
- rocky-db 在 192.168.1.103

这些名称可以随意命名，但重要的是名称必须以 Ubuntu 或 Rocky 开头。配置条目将如下所示：

```
Host ubuntu-web
Hostname 192.168.1.100

Host ubuntu-db
Hostname 192.168.1.101

Host rocky-web
Hostname 192.168.1.102

Host rocky-db
Hostname 192.168.1.103
```

保存并关闭文件。

接下来，我们必须创建两个脚本，它们将接受用户输入以供运行的命令、从配置文件中获取主机、测试要运行的命令是否需要 sudo 权限，然后循环遍历主机以执行命令。使用以下命令创建第一个脚本：

```
nano ~/ubuntu-cmd
```

你可以将该文件命名为任何你喜欢的名称。在该文件中，粘贴以下内容：

```shell
#!/bin/bash
 
# Get the user's input for the command
[[ -z ${@} ]] &amp;&amp; exit || CMD_EXEC="${@}"
 
# Locate the hosts from ~/.ssh/config with Host entries that are prefixed by `ubuntu-`
HOSTS=$(grep -Po 'Host\s\Kubuntu-.*' "$HOME/.ssh/config")
 
# Test for a sudo requirement
if [[ $CMD_EXEC =~ ^sudo ]]
then
 
# Ask for the sudo password
read -sp '[sudo] password for remote_admin: ' password; echo
 
# Rewrite the command as needed
CMD_EXEC=$(sed "s/^sudo/echo '$password' | sudo -S/" &lt;&lt;&lt; "$CMD_EXEC")
fi
 
# Iterate through the hosts and execute the SSH command, remove `-a` to override "&gt;"
while IFS= read -r host
do
echo -e '\n\033[1;33m'"HOST: ${host}"'\033[0m'
ssh -n "$host" "$CMD_EXEC 2&gt;&amp;1" | tee -a "/tmp/$(basename "${0}").${host}."
done &lt;&lt;&lt; "$HOSTS"
```

保存并关闭文件。

接下来，使用以下命令为 Rocky Linux 主机创建脚本：

```
nano ~/rocky-cmd
```

在该文件中，粘贴以下内容：

```
#!/bin/bash
# 获取用户输入的命令
[[ -z ${@} ]] && exit || CMD_EXEC="${@}"
# 从 ~/.ssh/config 中找到以 `rocky-` 为前缀的主机条目
HOSTS=$(grep -Po 'Host\s\Krocky-.*' "$HOME/.ssh/config")
```
## 测试 sudo 需求

```bash
if [[ $CMD_EXEC =~ ^sudo ]]
then
  # 询问 sudo 密码
  read -sp '[sudo] remote_admin 的密码：' password; echo
  # 根据需要重写命令
  CMD_EXEC=$(sed "s/^sudo/echo '$password' | sudo -S/" <<< "$CMD_EXEC")
fi
```

## 遍历主机并执行 SSH 命令，删除 `-a` 以覆盖 “>”

```bash
while IFS= read -r host
do
  echo -e '\n\033[1;33m'"主机：${host}"'\033[0m'
  ssh -n "$host" "$CMD_EXEC 2>&1" | tee -a "/tmp/$(basename "${0}").${host}."
done <<< "$HOSTS"
```

保存并关闭文件。

接下来，我们将脚本移动到 `/usr/local/bin`:

```bash
sudo mv ubuntu-cmd /usr/local/bin
sudo mv rocky-cmd /usr/local/bin
```

接下来，更改脚本的所有权：

```bash
sudo chown $USER /usr/local/bin/ubuntu-cmd
sudo chown $USER /usr/local/bin/rocky-cmd
```

最后，授予文件可执行权限：

```bash
sudo chmod u+x /usr/local/bin/ubuntu-cmd
sudo chmod u+x /usr/local/bin/rocky-cmd
```

## 如何使用脚本

假设你想要向 Ubuntu 服务器发送 `sudo apt-get update && sudo apt-get upgrade -y` 命令。为此，你需要发出以下命令：

```bash
ubuntu-cmd sudo apt-get update && sudo apt-get upgrade -y
```

你将在远程机器上收到 sudo 密码提示，成功验证后，它将运行命令，然后迭代到下一台主机。

然后，你可以对 Rocky 主机执行相同操作，如下所示：

```bash
rocky-cmd sudo dnf update -y
```

同样，它将遍历所有已配置的主机并在每台主机上运行命令。

恭喜！你刚刚让 Linux 服务器管理变得更轻松……而无需依赖更复杂、第三方平台来完成繁重的工作。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。