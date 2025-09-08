
<!--
title: Linux：部署蜜罐，诱捕服务器攻击者
cover: https://cdn.thenewstack.io/media/2025/09/be214105-cowrie.jpg
summary: 本文介绍了如何在 Ubuntu Server 上安装和配置 Cowrie 蜜罐，用于检测和研究未经授权的 SSH/Telnet 访问尝试。步骤包括安装依赖项、创建用户、克隆存储库、配置虚拟环境、创建配置文件以及重定向端口。
-->

本文介绍了如何在 Ubuntu Server 上安装和配置 Cowrie 蜜罐，用于检测和研究未经授权的 SSH/Telnet 访问尝试。步骤包括安装依赖项、创建用户、克隆存储库、配置虚拟环境、创建配置文件以及重定向端口。

> 译自：[Linux: Deploy a Honeypot to Catch Your Server's Attackers](https://thenewstack.io/linux-deploy-a-honeypot-to-catch-your-servers-attackers/)
> 
> 作者：Jack Wallen

在这一点上，安全性绝对至关重要。任何企业（无论规模大小）都[不能忽视安全性](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/)，并假设[什么都不会发生](https://thenewstack.io/xz-security-incident-the-importance-of-reputation-in-security/)。它迟早会发生，只是时间问题。

而且那还是在你不断关注网络内部发生的事情的前提下。想象一下，如果你不注意会怎样。

问题是，安全方面需要考虑的事情太多了，有时显而易见的事情可能会被忽略。例如，telnet。还记得吗？曾经的远程连接领导者变成了各种邪恶活动的后门。然后出现了 SSH，它[在安全性上呈指数级增长](https://thenewstack.io/linux-ssh-and-key-based-authentication/)……但并非完美。

你必须跟踪这些事情，始终警惕服务器“底层”发生的事情。

你也可以引诱潜在的攻击者进入所谓的蜜罐。

从本质上讲，蜜罐是一种诱饵，可以将攻击者从你的生产服务器上引开，同时保存黑客试图进入的所有详细信息。通过蜜罐保存的信息，你可以采取适当的措施来防止对关键系统的攻击。

蜜罐不是直接的防御手段。相反，蜜罐是一种旨在帮助你检测和研究对你网络未经授权的访问尝试的工具。

听起来很难，不是吗？

多亏了 [Linux](https://thenewstack.io/learning-linux-start-here/)，它并不像你想象的那么具有挑战性。

我将引导你完成在 [Ubuntu Server](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 上安装蜜罐的过程。这里提到的蜜罐是 [Cowrie](https://www.cowrie.org)，这是一个基于 SSH/telnet 的蜜罐，可以帮助你了解攻击者可能试图如何远程访问你的系统。

Cowrie 是开源的，可以免费安装/使用。Cowrie 正在积极开发中，并且已经存在一段时间了，因此它是一个经过验证的工具。

你可以将 Cowrie 部署为 [Docker 容器](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/)，但我将向你展示如何以老式的方式安装它。

令人兴奋。

你准备好了吗？

## 你需要什么

你需要的唯一东西是一个正在运行的 Ubuntu Server 实例（最好是 v 22.04 或更高版本）和一个具有 sudo 权限的用户。当然，你还需要网络连接，但这不用多说。

让我们开始吧。

## 安装依赖项

第一步是安装所需的依赖项。登录到你的 Ubuntu Server 实例并发出以下命令：

```
sudo apt-get install git python3-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind virtualenv python3.12-venv -y
```

安装完成后，你就可以继续了。

## 添加 Cowrie 用户

我们将创建一个名为 cowrie 的新用户，没有密码，使用以下命令完成：

```
sudo adduser --disabled-password cowrie
```

回答必填问题（你可以直接按 Enter 键接受默认答案）。完成此操作后，使用以下命令切换到 cowrie 用户：

```
sudo su - cowrie
```

## 克隆 Cowrie 存储库

我们现在可以使用以下命令克隆 Cowrie 存储库：

```
git clone http://github.com/cowrie/cowrie
```

完成后，使用以下命令更改到新目录：

```
cd cowrie
```

## 创建一个虚拟环境

我们现在需要使用以下命令创建一个 Python 虚拟环境：

```
python3 -m venv cowrie-env
```

创建完成后，让我们运行安装步骤，这可以通过以下命令完成：

```
source cowrie-env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade -r requirements.txt
```

## 创建 Cowrie 配置文件

现在是时候创建一个 Cowrie 配置文件来启用 telnet 了。使用以下命令创建文件（在 cowrie 目录中）：

```
nano etc/cowrie.conf
```

在该文件中，粘贴以下内容：

```
[telnet]
enabled = true
```

使用 Ctrl-x 保存并关闭文件。

使用以下命令启动 Cowrie（从 Cowrie 目录中运行）：

```
bin/cowrie start
```

## 重定向必要的端口

我们现在将重定向 SSH 和 telnet 端口，以便 SSH 端口 22 转到 2222，telnet 端口 23 转到 2223。为此，你需要退出 Cowrie 用户，然后使用以下命令进行更改：

```
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223
```

## 验证它是否正常工作

在蜜罐上，切换回 cowrie 用户 (`sudo su - cowrie`)，然后让我们使用以下命令跟踪 Cowrie 日志：

```
tail -f cowrie/var/log/cowrie/cowrie.log
```

转到你网络上的另一台计算机，并尝试 telnet 或 SSH 进入蜜罐服务器，你将看到出现在你正在跟踪的日志中的条目，这些条目指示连接来自何处（以及其他有用的信息）。你也可以通过测试与蜜罐的 SSH 连接来执行相同的操作。

你需要确保定期检查 Cowrie 日志（就像一天中定期检查一样），以查看是否有人试图访问服务器。如果是这样，你将了解连接来自何处，并可以在发生任何灾难性事件之前减轻它。