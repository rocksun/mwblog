<!--
title: 通过SSH端口转发创建加密隧道
cover: https://cdn.thenewstack.io/media/2024/01/eabeb80d-hamburg-8290719_1280-1024x682.jpg
-->

如果您想在两个Linux实例之间创建加密隧道，最佳选择是使用SSH端口转发。

> 译自 [Linux: Create Encrypted Tunnels with SSH Port Forwarding](https://thenewstack.io/linux-create-encrypted-tunnels-with-ssh-port-forwarding/)，作者 Jack Wallen 是当X世代的思想与当下的嘲讽相融合时所产生的结果。Jack 是一位追求真理、以量子力学铅笔和不协调的声音与灵魂节奏写作的作家。

Secure Shell（[SSH](https://thenewstack.io/dr-torq-go-remote-with-ssh/)）拥有[几个非常酷的技巧](https://thenewstack.io/create-and-manage-shh-keys-for-third-party-integration/)，每个技巧都提供了[一个方便的功能](https://thenewstack.io/create-a-local-git-repository-on-linux-with-the-help-of-ssh/)（包裹在安全的保护层中），可以[让你的生活变得更轻松一些](https://thenewstack.io/create-and-manage-shh-keys-for-third-party-integration/)。

上周，我们讨论了使用 [SSH 进行密钥身份验证](https://thenewstack.io/secure-remote-linux-server-logins-with-ssh-key-authentication/)；本周我们将讨论端口转发，它可以用于：

- 访问你可能无法直接访问的服务器。
- 以更高的安全性访问远程机器。
- 授予一个临时的、加密的通道，从本地机器到远程机器。

SSH 端口转发有三种不同的类型。它们分别是本地（客户端的连接通过 SSH 转发到远程主机）、远程（远程服务器的连接通过 SSH 转发到另一台机器）和动态（不同应用程序的连接通过 SSH 转发到多个服务器）。

有许多端口转发的示例，其中一些可能变得相当复杂。因此，我们只会在这里处理前两种端口转发（本地和远程）。这也是你最常使用的 SSH 端口转发类型。

SSH 端口转发默认内置在 SSH 中，因此只要安装了 SSH，你应该就拥有使用这个功能所需的一切。

说到这里，让我向你展示 SSH 端口转发的工作原理。

## 安装 OpenSSH 服务器

你的 [Linux 发行版](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)可能已经安装了 SSH。但是，为了进行端口转发，你还需要添加 SSH 服务器。在[基于 Ubuntu 的发行版上](https://thenewstack.io/enable-automatic-updates-for-ubuntu-server/)，安装 SSH 服务器的命令如下：

```bash
sudo apt-get install openssh-server -y
```

在基于 RHEL 的发行版上，该命令为：

```bash
sudo dnf install openssh-server -y
```

安装完成后，在 Ubuntu 发行版上使用以下命令启动并启用 SSH 服务器：

```bash
sudo systemctl enable --now ssh
```

在基于 RHEL 的发行版上，启动/启用命令如下：

```bash
sudo systemctl enable --now sshd
```

## SSH本地端口转发

我们首先要处理的端口转发类型是本地。假设你正在开发一个新站点，并且希望能够通过加密连接访问它。这个新站点可能位于本地网络或远程服务器上。无论如何，你都可以使用本地端口连接到远程SSH服务器，从而实现从本地端口到远程端口的连接。

假设你想使用本地端口8080并通过SSH将连接转发到IP地址192.168.1.11的端口80。为此，命令如下：

```bash
ssh -L 8080:192.168.1.11:80 localhost
```

系统将提示你输入本地SSH用户密码，然后会返回到命令提示符。要验证隧道是否成功，请打开Web浏览器并指向：

```bash
localhost:8080
```

远程站点（在192.168.1.11上）应该出现在Web浏览器中，并且通过SSH加密进行隧道传输。

只要你在终端窗口中保持“登录”状态，就可以继续使用加密隧道。要关闭加密隧道，请返回到终端窗口并键入：

```bash
exit
```

## SSH远程端口转发

这种类型的端口转发可能更实用，因为它可以让你通过加密隧道[为他人提供对远程机器的访问](https://thenewstack.io/10-things-to-consider-when-allowing-access-to-production/)。比如说，你在局域网中有人需要VNC访问带有GUI的服务器，并且你希望确保该连接因安全原因而加密。当然，这需要你在服务器上正确设置VNC，并在客户机器上安装VNC查看器。

在这个例子中，我们将继续使用远程机器的IP地址为192.168.1.11，而客户机器位于192.168.1.21。你必须同时具备对客户机器的SSH访问权限。

但在执行这之前，你必须处理一下简单的SSH配置。使用以下命令打开SSH服务器配置文件：

```bash
sudo nano /etc/ssh/sshd_config
```

在文件底部添加以下行：

```bash
GatewayPorts yes
```

保存并关闭文件。重新启动SSH，可以使用以下命令之一：

```bash
sudo systemctl restart ssh
```

或者

```bash
sudo systemctl restart sshd
```

现在，让我们创建远程隧道。为了为VNC（运行在端口5900上）创建隧道，请在远程服务器上（在我们的例子中是192.168.1.11）运行以下命令：

```bash
ssh -R 5900:localhost:5900 USERNAME@192.168.1.21
```

其中USERNAME是客户机器上你有访问权限的用户名。一旦验证了该用户，SSH远程隧道就已经建立并运行。其他用户随后可以使用VNC客户端连接到服务器，使用localhost和端口5900。

注意，即使远程用户断开了他们的VNC连接，隧道仍然是建立并运行的。要关闭隧道，请返回到远程服务器的终端并键入exit。

如果你想要为各种用途创建加密隧道，SSH是一个不可多得的选择。一旦你掌握了创建这些隧道的方法，你会发现它们在多种不同类型的场景中都非常有用。
