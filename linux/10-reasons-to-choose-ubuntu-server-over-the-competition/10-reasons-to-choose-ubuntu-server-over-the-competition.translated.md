# 选择Ubuntu Server的10大理由

![选择Ubuntu Server的10大理由特色图片](https://cdn.thenewstack.io/media/2023/12/b0026b48-ubuntu-1024x683.png)

说到服务器操作系统（OS），你会想到什么？如果你过去十年一直生活在微软的“岩石”下，那么Windows Server可能是你的首选。

如果我说还有更好的选择呢？

实际上，微软服务器还有几个替代方案，所有这些都属于开源的范畴。例如有[Red Hat Enterprise Linux](https://thenewstack.io/red-hat-enterprise-linux-9-5-arrives-with-enhanced-ai-support-and-automation/), [AlmaLinux](https://thenewstack.io/almalinux-captures-the-soul-of-centos/), [Oracle Linux](https://developer.oracle.com/?utm_content=inline+mention), [Fedora Server](https://thenewstack.io/fedora-41-offers-zippy-performance/), [Debian Server](https://thenewstack.io/debian-retools-apt-for-superior-dependency-management/), 等等。

然而，对我来说，首选是Canonical的[Ubuntu Server](https://thenewstack.io/ubuntu-24-10-refreshes-gnome-permission-prompts/)。十多年前我切换到Ubuntu Server，并且再也没有回头。这并不是说我不使用其他服务器操作系统。在过去几年中，我有很多基于[AlmaLinux](https://thenewstack.io/almalinux-kitten-offers-preview-of-distros-next-release/)的部署，这是一个非常不错的选择。

但是，任何时候如果由我决定，Ubuntu Server都是我的首选。你问为什么？让我列举十个理由，解释为什么我十多年来一直默认选择Ubuntu Server。

## 1. apt

在我使用过的所有包管理器中，我发现高级包工具（[apt](https://ubuntu.com/server/docs/package-management)）不仅最易于使用，而且在解决问题方面也最有效……即使是损坏的包。例如，如果我使用apt安装某些东西并且安装失败，大多数情况下，我可以使用[sudo命令](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)修复问题：`sudo apt-get install -f`。-f是–fix-broken的缩写，它尝试修复具有损坏依赖项的系统。多年来，这个命令帮助我摆脱了无数困境，它已成为一个非常宝贵的选项。很少有包管理器像apt一样易于使用且可靠。

## 2. 没有SELinux

[SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux)是一个非常强大的安全控制框架，存在于大多数基于Fedora的Linux操作系统中。我并非反对SELinux，但它可能会导致问题，例如使新安装的应用程序无法使用。我见过这种情况发生很多次。这个问题非常普遍，以至于许多管理员错误地禁用SELinux以避免这些问题。不幸的是，这会删除一个更重要的安全工具，从而使操作系统容易受到攻击。与其禁用SELinux，不如学习它的来龙去脉，这样你就可以避免禁用它。Ubuntu Server选择使用[AppArmor](https://thenewstack.io/4-ways-to-use-kernel-security-features-for-process-monitoring/)，它提供强大的安全性，而不会阻止应用程序按预期运行。

## 3. 海量的应用程序和工具

由于apt和Snap的结合（稍后会详细介绍），你会发现大量可用于在Ubuntu Server上安装的应用程序和工具。Ubuntu Server拥有任何Linux发行版中最丰富的应用程序选择之一。如果你在默认存储库中找不到应用程序，很有可能存在你可以添加的第三方存储库来安装该应用程序。

## 4. 出色的支持

截至目前，Ubuntu Server 24.04（这是一个长期支持版本）将支持到2029年。如果你添加LTS扩展安全维护，则支持期限将延长至2035年，而传统支持则会额外增加一年。想象一下，部署一个服务器操作系统，知道它将享有12年的支持。这是一段很长的时间。在安全窗口过期之前，你很可能已经升级到新版本，并将享受更多支持。

## 5. 可预测的发布

Ubuntu的发布分为两类：长期发布和短期发布。长期发布版本为.04，短期发布版本为.10。LTS版本总是在每年的第四个月发布，短期版本在每年的第十个月发布。Ubuntu的发布周期像钟表一样精准，与地球上任何软件发布一样可靠和可预测。

## 6. 高效利用资源
多年来，我使用过许多不同的服务器操作系统，但我从未遇到过比Ubuntu Server更有效利用资源的操作系统。操作系统本身的性能几乎就像一个轻量级的Linux发行版，这意味着您添加的应用程序和服务都将表现出色。即使在资源匮乏的服务器上，我也可以始终依靠Ubuntu Server表现出色。如果您在基于云的主机（例如AWS）上部署Ubuntu Server，您可以放心，不必担心操作系统本身会消耗过多的计算或网络资源。

## 7. 用户友好（尤其对于Linux新手）

如果您以前从未使用过Linux，Ubuntu Server 是显而易见的选择。Ubuntu一直被认为是最用户友好的发行版之一，服务器端也是如此。我对此如此坚信的原因之一是，Ubuntu不会设置太多障碍来阻碍您的成功。它非常直观，并且拥有所有服务器专用操作系统中最简单的学习曲线之一。

## 8. 强大的硬件支持

我安装Ubuntu时，硬件不被识别的的情况非常罕见。对于服务器来说尤其如此，因为您不会添加扫描仪、使用无线网络连接或使用利基外围设备。在部署Ubuntu Server时，我从未需要搜索驱动程序来运行任何东西，因为它都能“正常工作”。

## 9. Snap软件包

我知道Snap受到了那些不喜欢Canonical的人的很多批评，但是Snap软件包使部署某些应用程序和服务变得非常容易，任何人都可以做到。例如，如果您想运行Nextcloud云服务器，您可以使用命令`sudo snap install nextcloud`通过Snap安装它。安装命令完成后，打开浏览器，将其指向托管服务器的IP地址，创建一个管理员帐户，您就可以开始了。没有比这更容易的了。

## 10. 在线帮助的可用性

当您遇到Ubuntu Server问题时，Google（或DuckDuckGo——我的首选搜索引擎）是您的朋友。您会发现很多地方可以寻求帮助，例如Ubuntu论坛，在那里您会发现一个庞大的用户社区，他们能够回答您的问题。您还可以在Mastodon上找到许多社区（例如官方的Ubuntu社区）和官方的Ubuntu Discourse频道。

如果您还没有尝试过Ubuntu Server，我强烈建议您下载一个ISO映像并启动虚拟机，看看这个开源、面向服务器的操作系统是多么容易和可靠。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。