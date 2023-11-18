<!--
title:  Kali Linux如何帮助测试网络安全
cover: https://cdn.thenewstack.io/media/2023/11/4b416c71-kali-1024x685.png
-->

如果你想深入了解网络、网站、系统或应用的安全性，就需要学习Kali Linux。

> 译自 [How Kali Linux Can Help Security Test Your Network](https://thenewstack.io/how-kali-linux-can-help-security-test-your-network/)，作者 Jack Wallen。

<secondTrans>

渗透测试(又称“pentesting”)是一种发现网络及其连接系统漏洞的好方法。[渗透测试](https://thenewstack.io/john-deere-harvests-def-con-mockery-for-lax-web-security/)也被称为道德黑客入侵，这有助于解释它的确切含义——使用与恶意入侵者相似的工具，试图发现任何可能允许黑客访问你网络的问题和漏洞。

对于希望确保网络尽可能安全的企业来说，渗透测试是[必不可少的](https://thenewstack.io/use-pen-testing-to-gauge-software-development-life-cycle-health/)。大问题是应该从哪里入手。目前有相当多的渗透测试工具可用，其中许多都是开源和免费使用的。事实上，你可以在任何选择的操作系统上安装这些工具中的任何一个。

然而，感谢 Kali Linux，现在有了一个更好的方法。

如果你不熟悉 Kali Linux，它是一个[专门用于渗透测试的 Linux 发行版](https://thenewstack.io/penetration-testing-with-kali-linux-as-a-docker-container/)，并且包含了许多用于此目的的工具。你很难找到一个拥有这么多预装的渗透测试工具的操作系统。

尽管这些工具中的一些确实有相当陡峭的学习曲线，但好消息是，感谢 Kali Linux，你不必担心它们的正确安装和配置。这些工具已经在那里准备就绪。

Kali Linux 中的渗透测试工具既有图形用户界面(GUI)工具，也有命令行界面(CLI)工具，CLI 工具中的一些实际上比 GUI 更简单。情况并不总是如此，但如果你曾经使用过命令行，你就会知道它通常比 GUI 更高效。

学习曲线问题暂且不论，Kali Linux 无疑是市场上最好的渗透测试平台。如果你想知道你的网络、网站、系统或应用程序的安全性究竟如何，你会想要了解 Kali Linux。

## 如何获取 Kali Linux

我首先想提的一点是如何获取和安装 Kali Linux。由于这是一个 Linux 发行版，你总是可以下载一个 [ISO 安装镜像](https://www.kali.org/get-kali/#kali-platforms)，并将其安装在任何可用的系统上。Kali Linux 是一个相当轻量级的发行版，因此即使在较老的硬件上安装也应该可以。

另一种方法(也是我倾向于首选的方法)是下载一个[虚拟机](https://www.kali.org/get-kali/#kali-virtual-machines)，并在 VMware、VirtualBox、Hyper-V 或 QEMU 上使用它。只要确保下载与你的虚拟机平台相匹配的虚拟机。

我更喜欢虚拟机方法的原因是，我可以从任何支持虚拟机的操作系统运行它，并且可以随意启动、暂停和停止 Kali Linux。

要在 VirtualBox 上运行 Kali Linux 虚拟机，请执行以下步骤:

- 确保下载 [VirtualBox 虚拟机镜像](https://cdimage.kali.org/kali-2023.3/kali-linux-2023.3-virtualbox-amd64.7z)。
- 从命令行或图形文件管理器中提取 .7z 文件。
- 打开 VirtualBox。
- 单击“添加”。
- 导航到新创建的 kali-linux-XXX-virtualbox-amd64 文件夹(其中 XXX 是发布编号)，双击以 .vbox 结尾的文件。
- 导入 VM 后，单击“完成”。

在启动 VM 之前，从左面板中选择它，然后单击“设置”。我们要确保 Kali Linux 附加到你的局域网，因此单击“网络”，然后从“连接到”下拉列表(图1)中选择“桥接适配器”。

![](https://cdn.thenewstack.io/media/2023/11/dd730fe4-kali1.jpg)

*图1:将网络从默认的NAT更改为桥接*

一旦你完成了这一步，关闭“设置”，然后启动虚拟机。当你最终看到 Kali Linux 登录界面时，使用凭据 kali/kali 登录。

## 你的第一个渗透测试体验

在本文中，我们将从一些简单的事情开始。Kali Linux 中包含的众多工具之一称为 [wpscan](https://wpscan.com/)，它可以扫描 WordPress 部署中的问题。

你可以在“Web 应用程序分析”菜单中找到 wpscan，它被标记为 wpscan。当你点击该条目时，将打开一个终端窗口，准备好运行你的第一个扫描(图2)。

![](https://cdn.thenewstack.io/media/2023/11/6644033a-kali2.jpg)

*图2:Kali Linux 终端窗口*

你不必通过桌面菜单。相反，你可以简单地点击顶栏中的终端图标，就会打开 Kali Linux 终端窗口。由于 Linux 安装应用程序的方式，你可以从任何终端和任何目录运行 wpscan 命令。

假设你当前正在测试一个 WordPress 部署，它还未投入生产。我们将使用 IP 地址 192.168.1.229 进行测试。这个测试的命令是:

```bash
wpscan --url=http://192.168.1.229
```

输出会快速滚动，在末尾，你会看到消息“未给定 WPScan API Token，因此未输出漏洞数据”。在下面你会看到一个链接，你可以点击并注册获取 API Token。

将你的 token 复制后，可以像这样将其添加到命令中:

```bash
wpscan --api-token TOKEN --url=http://192.168.1.229
```

如果你想要保存扫描输出到一个文件，可以这样做:

```bash
wpscan --api-token TOKEN FILENAME --url=http://192.168.1.229 &gt; FILENAME
```

其中 TOKEN 是你的 API token，FILENAME 是你希望输出保存到的文件的名称。

当扫描完成后，你可以使用以下命令之一查看文件内容:

```bash
cat FILENAME
less FILENAME
```

我更喜欢使用 less，因为它允许我上下滚动更容易地读取文件。

这就是如何开始用 Kali Linux 运行你的第一个渗透测试。我们会在未来的文章中重新讨论这个主题，并且介绍更具挑战性的测试。在那之前，尽情享受这个道德黑客平台吧。
