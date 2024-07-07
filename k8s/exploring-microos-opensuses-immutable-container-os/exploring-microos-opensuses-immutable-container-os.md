
<!--
title: 探索MicroOS，OpenSUSE的不可变容器操作系统
cover: https://cdn.thenewstack.io/media/2024/07/a0489be3-opensuse-microos.png
-->

MicroOS 是 OpenSUSE 的以容器为中心的不可变 Linux 发行版。以下是如何设置它并进行测试。

> 译自 [Exploring MicroOS, OpenSUSE's Immutable Container OS](https://thenewstack.io/exploring-microos-opensuses-immutable-container-os/)，作者 Jack Wallen。

[容器化](https://thenewstack.io/containers/) 的关键在于“少即是多”。在部署容器化工作负载时，您需要以与传统桌面或服务器不同的方式考虑您的操作系统。您需要的是专门为这类工作负载设计的操作系统。您需要原子更新、滚动发布以及专门针对容器的安全措施。

这就是 [openSUSE MicroOS](https://microos.opensuse.org/) 的用武之地。这种 [以容器为中心](https://thenewstack.io/canonical-offers-lts-distroless-containerized-apps-for-k8s/) 的 Linux 发行版具有可预测性、不可变性、可扩展性，使用事务性/安全更新，所有应用程序都安装在容器中。

您目前可能正在使用标准发行版（例如 [Ubuntu Server](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/)、[Debian](https://thenewstack.io/install-a-full-lamp-stack-on-a-debian-server/)、[AlmaLinux](https://thenewstack.io/linux-and-cloud-native-security-almalinux/) 或 [Red Hat Enterprise Linux](https://www.openshift.com/try?utm_content=inline+mention)）来部署容器。这些操作系统的弊端在于它们可能会被更改。一些不怀好意的攻击者可能会访问正在运行的容器，跳到操作系统上，并注入恶意代码。

对于不可变操作系统，这将变得更加困难，因为磁盘上无法进行任何更改。

您可能希望拥有这样的操作系统，而 openSUSE MicroOS 就能满足您的需求。

我想向您展示 openSUSE MicroOS 的安装过程是多么简单，甚至可以安装 [Cockpit](https://cockpit-project.org/)，这样您就可以使用基于 Web 的 GUI 来管理平台（因为对于某些人来说，它比 CLI 更容易）。

您准备好了吗？

让我们开始吧。

## 您需要什么

要使此操作正常工作，您需要 openSUSE MicroOS 的 ISO 镜像和一个虚拟机平台。我将使用 VirtualBox 演示此过程，但您可以使用您选择的 VM 技术。

## 获取和安装 openSUSE MicroOS

首先，您需要从 [官方网站](https://get.opensuse.org/microos/) 下载 openSUSE MicroOS 的 ISO 镜像。请确保下载适合您架构的文件（它适用于 Intell/AMD、PowerPC、小端和 aarch64）。

将 ISO 镜像保存到本地驱动器后，按照您选择的 VM 平台的正常步骤创建一个新的虚拟机。在第一个交互式屏幕（图 1）中，使用键盘上的上下键选择“安装”，然后按 Enter 键。

![](https://cdn.thenewstack.io/media/2024/07/f9dedb12-microos1.jpg)

*图 1：这是 MicroOS 安装向导的第一个屏幕。*

然后，您需要在同一页面上选择您的语言和键盘布局，并接受许可协议。默认情况下，语言/键盘配置为英语，因此您可以单击“下一步”继续（图 2）。

![许可协议](https://cdn.thenewstack.io/media/2024/07/65e54e4e-microos2.jpg)

*图 2：许可协议*

然后，您将看到系统角色选择。对于容器部署，请选择“MicroOS 容器主机”，然后单击“下一步”（图 3）。这将安装 MicroOS，使其针对容器化工作负载进行优化，其中包括 [Podman 运行时](https://thenewstack.io/red-hat-podman-lab-gets-developers-started-on-genai/)。

![](https://cdn.thenewstack.io/media/2024/07/c62b667f-microos3.jpg)

*图 3：在安装过程中选择您的系统角色。*

做出您的选择，然后单击“下一步”。

在“NTP 服务器”窗口中，保留默认设置，然后单击“下一步”。

然后，系统会要求您为 root 用户创建密码。输入并确认您的密码，然后单击“下一步”（图 4）。

![](https://cdn.thenewstack.io/media/2024/07/08d1c1eb-microos4.jpg)

*图 4：为 root 用户创建密码。*

您还可以导入公钥 SSH，但该密钥必须从 MicroOS 文件系统中复制。为此，您需要在虚拟机和桌面之间创建一个共享文件夹。我将向您展示如何稍后上传 SSH 密钥。

最后，单击“安装”开始安装过程。安装完成后，重新启动并登录。这是一个无 GUI 的操作系统，因此您会发现自己处于终端提示符下。

## 安装 Cockpit

对于那些希望使用基于 Web 的 GUI 来管理 MicroOS 的用户，以下是如何操作。以 root 用户身份，执行以下命令：

```
transactional-update pkg install patterns-microos-cockpit cockpit-ws cockpit-tukit
```

这将安装 Cockpit。在使用该应用程序之前，您需要使用以下命令重新启动机器：

```
reboot
```

然后，您必须使用以下命令启用它：

```
systemctl enable --now cockpit.socket
```

最后，使用以下命令允许 Cockpit 通过防火墙：

```
firewall-cmd --permanent --zone=public --add-service=cockpit
```

使用以下命令重新加载防火墙：

```
firewall-cmd --reload
```

完成这些操作后，使用以下命令查找 MicroOS 服务器的 IP 地址：

```
ip a
```

您可以通过将浏览器指向 https://SERVER:9090（其中 SERVER 是 MicroOS 服务器的 IP 地址）来访问 Cockpit。在登录屏幕上，使用 root 和您在安装过程中创建的密码。

## 添加新用户

您尝试登录 Cockpit 时会发现的第一件事是 root 用户不允许这样做。要解决此问题，您需要创建一个新用户。回到命令行，执行以下操作：

```
useradd -m USERNAME
``` 

其中 USERNAME 是您要添加的用户。
接下来，使用以下命令为用户提供一个强/唯一的密码：

```
passwd USERNAME
```

其中 USERNAME 是您刚刚添加的新用户。

添加新用户后，您可以使用这些凭据登录 Cockpit。登录后，您需要通过单击窗口顶部的“管理访问权限”来授予该用户管理访问权限。

完成此操作后，您可以进入“帐户”（在 Cockpit 中），然后添加您的 SSH 公钥。以下是操作方法：

在您的桌面（您将从这里 SSH 到 MicroOS）上，发出以下命令（假设您将密钥保存在默认位置）：

```
cat ~/.ssh/id_rsa.pub
``` 

复制该密钥的内容，然后返回到 Cockpit > 帐户 > 授权的公共 SSH 密钥，然后单击添加密钥。将 SSH 密钥粘贴到结果窗口中，然后单击添加。完成此操作后，您应该能够通过该新用户使用 SSH（使用您的 SSH 密钥）登录到 MicroOS。

现在您已经完成了这些操作，您可以使用 Cockpit 或命令行来处理您的 Podman 容器。

这就是让 openSUSE MicroOS 运行起来并准备好进行您的第一个容器化部署的全部内容。
