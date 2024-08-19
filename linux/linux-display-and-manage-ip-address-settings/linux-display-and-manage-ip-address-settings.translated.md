# Linux：显示和管理 IP 地址设置

![Featued image for: Linux: Display and Manage IP Address Settings](https://cdn.thenewstack.io/media/2024/08/5b178800-humboldt-penguin-7283765_1280-1024x682.jpg)

[Linux: Companion Lab for Linux Skill Blocks Repository](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)文章。在本系列中，我们还介绍了
[如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/)和
[安装平台](https://thenewstack.io/linux-choose-an-installation-platform/)，Linux 内核如何
[与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)以及如何
[Linux 管理系统服务](https://thenewstack.io/linux-skills-manage-system-services/)，
[存储](https://thenewstack.io/how-to-manage-linux-storage/)，
[文件权限](https://thenewstack.io/linux-how-file-permissions-work/)，
[系统进程](https://thenewstack.io/linux-manage-system-processes/)，以及
[用户和组权限](https://thenewstack.io/linux-user-and-group-management/)。

现代计算机及其用户几乎依赖网络连接来完成所有操作，包括基于云的应用程序、软件访问、数据访问和通信。似乎计算的各个方面都依赖于网络。Linux 工作站和服务器在这方面的必要性与 Windows 或 macOS 系统没有区别。

Linux 系统管理员的主要职责之一是确保网络连接。这需要了解系统在网络上的身份并对其进行配置以参与网络数据交换。

Linux 系统在网络上具有三个身份。各种网络设备以不同的方式使用每个身份。

以下是三个身份及其用途的摘要：

**主机名**: 一个对用户和管理员友好的名称，为他们提供了一种简单的方法来识别节点。**IP 地址**: 路由器和网络配置工具用来识别系统的逻辑地址。**MAC 地址**: 网络接口卡 (NIC) 上的物理地址，用于唯一地识别它与交换机和其他第 2 层设备。
例如，计算机的三个身份可能如下所示：

- 主机名：computer27
- IP 地址：192.168.2.200
- MAC 地址：00:1c:42:73:8d:f2

这三个网络身份的使用和功能是本文的假设知识。如果您需要复习，请务必查看基本网络信息。您可能想[构建一个实验室环境](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)来练习本文中介绍的命令。如果您需要复习基本的 Linux 命令语法，请参考[这篇文章](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)。

避免以 root（管理员）用户身份登录 Linux 系统。大多数系统强制您以普通用户身份登录，然后使用 sudo（超级用户执行）命令和您的密码来提升您的权限。本教程中的一些命令可能需要在您的 Linux 发行版上使用 sudo 命令。您还必须使用 sudo 以提升的权限打开文本编辑器来管理网络配置文件。

```
$ sudo vim /etc/resolv.conf
```

本文通过提供命令示例并提供轻松维护网络设置的方法，来检查三个网络身份的使用和配置。

## 显示系统身份

使用 hostname 命令显示系统的对用户友好的名称。这几乎肯定是用戶识别其计算机的唯一方式。主机名可能是称为完全限定域名 (FQDN) 的更大命名结构的一部分，指示系统在分层命名结构中的位置。

```
$ hostname
```

![](https://cdn.thenewstack.io/media/2024/07/ed3aba05-hostname.png)

单个命令还可以显示 IP 和 MAC 地址，尽管输出不太直观。使用
ip addr 命令显示系统中每个网络接口的信息。请记住，每个接口都有其自己的唯一 IP 和 MAC 地址。服务器通常包含两个或多个 NIC，以实现冗余或连接到多个段。

```
$ sudo ip addr
```

![](https://cdn.thenewstack.io/media/2024/07/1674b903-ipaddr.png)

较旧的 Linux 系统使用 ifconfig 命令来实现此目的。

这些值是如何选择和分配的？管理员在安装操作系统时配置主机名。IP 地址可以由管理员手动配置，也可以由动态主机配置协议 (DHCP) 服务器动态分配。MAC 地址由其制造商硬编码。其中，您可能只更改系统的 hostname 和 IP 地址，这可能很少发生。

即使是简单的网络也会很快变得难以管理，因此许多 IT 部门会记录这些配置，以便在故障排除期间轻松参考。

## 管理系统主机名
## 系统主机名

系统主机名通常在安装 Linux 时设置。较大的组织通常使用特定的命名约定，以指示系统在网络中的角色或用途。较小的公司可能使用简单的名称。无论如何，系统名称在环境中必须是唯一的。

通过键入 `hostname` 命令显示当前主机名。

通过键入以下命令将系统的 hostname 临时更改为 `comp99`：

```bash
$ sudo hostname comp99.mycompany
```

但是，此名称分配将在系统下次重启时丢失。

如果您需要在安装操作系统后永久更改主机名，请使用 `hostnamectl` 命令。假设您需要将新主机名设置为 `comp42` 在 `mycompany` 域中。使用以下命令：

```bash
$ sudo hostnamectl set-hostname comp42.mycompany
```

![](https://cdn.thenewstack.io/media/2024/07/b41b173d-set-hostnamectl.png)

此方法使更改在重启后保持持久。`hostnamectl` 命令修改 `/etc/hostname` 文件，因此您无需直接查找和编辑它。

更改系统的 hostname 意味着任何通过名称引用的脚本、网络映射或用户将不再能够这样做。因此，通常不建议通过主机名引用系统。IP 地址通常是引用网络服务器、打印机和其他设备的更好方法。

## 管理系统 IP 地址

管理员负责分配 IP 地址。他们可以通过在网络中的每个系统上手动输入唯一的 IP 地址（非常繁琐）来完成此操作，或者通过配置一个服务器，该服务器具有工作站可以从中租赁 IP 配置的地址池。大多数管理员通过为服务器和其他基本网络设备分配静态 IP 地址，并让工作站和最终用户设备从服务器租赁配置，来结合使用这两种方法。

### 静态 IP 地址配置

静态 IP 地址对于需要一致且不变的 IP 地址标识符的网络节点很有用。Linux 服务器就是一个很好的例子，打印机、路由器和其他基础设施设备也是如此。手动键入 IP 地址配置非常耗时，并且配置无法容忍打字错误或重复的 IP 地址分配，这使得这种方法在工作站和客户端设备的大规模应用中非常低效。

由于服务器和类似设备往往较少，因此静态分配对这些设备非常有效。您可以设置一个在重启后消失的临时 IP 地址，或者设置一个系统保留的持久设置，除非您更改它。

使用以下命令将临时 IP 地址分配给 `eth0` 网络接口：

```bash
$ sudo ip addr add 192.168.2.200/24 dev eth0
```

![](https://cdn.thenewstack.io/media/2024/07/1ed4ea65-tempip.png)

使用 `del` 子命令删除静态 IP 地址，如下所示：

```bash
$ sudo ip addr del 192.168.2.200/24 dev eth0
```

请注意，上面的命令不会永久设置 IP 地址。它们只适用于当前运行时，并且不会在重启后保留。

您可能会发现 Linux 网络的 [NetworkManager](https://www.networkmanager.dev/) 组件更易于处理网络配置。该工具使用 `nmcli` 命令来管理网络设置，而不是直接编辑网络配置文件并重新启动网络服务。

键入 `nmcli` 命令而不带任何标志以查看是否安装了 NetworkManager：

```bash
$ sudo nmcli
```

![](https://cdn.thenewstack.io/media/2024/07/2b0f735c-nmcli.png)

并非所有发行版都使用 `nmcli`，但大多数与 Red Hat 相关的发行版都使用。如有必要，请使用发行版的包管理器（可能是 APT 或 DNF）安装 NetworkManager。对于 Debian 类系统，输入 `sudo apt install network-manager`。在 Red Hat 相关的系统上，输入 `sudo dnf install NetworkManager`。

查看网络设备以识别您要使用的设备名称：

```bash
$ sudo nmcli device status
```

![](https://cdn.thenewstack.io/media/2024/07/13c6a553-nmcli-dev-status.png)

假设输出显示一个名为 `enp0s5` 的网络接口设备。使用以下 `nmcli` 命令配置 `eth0` 接口，其静态 IP 地址为 `192.168.2.200`，子网掩码为 `/24`，默认网关为 `192.168.2.1`：

```bash
$ sudo nmcli con add con-name "static-connection" ifname eth0 type ethernet ip4 192.168.2.200/24 gw4 192.168.2.1
```

![](https://cdn.thenewstack.io/media/2024/07/b0ae2e99-staticip.png)

使用以下 `nmcli` 命令重新加载接口：

```bash
$ sudo nmcli con down eth0
$ sudo nmcli con up eth0
```

修改网络配置文件是使 IP 地址保持持久的另一种方法。这些文件因发行版而异，但这里有两个常见的示例。

在 Red Hat 和类似的发行版上，使用文本编辑器编辑以下文件：

```bash
/etc/sysconfig/network/etc/sysconfig/network-scripts/ifcfg-eth0
```

编辑
/etc/sysconfig/network 文件包含主机名、默认网关和 IPv6 配置的设置。
修改 /etc/sysconfig/network-scripts/ifcfg-eth0 文件，添加合适的 IP 地址、子网掩码、网关（默认网关）和至少一个 DNS 服务器地址。

您应该使用 sudo systemctl restart network 命令重启网络服务。与其他命令一样，此命令在不同的发行版中可能有所不同。

Debian 及其相关发行版（Ubuntu、Mint 等）使用 [Netplan](https://ubuntu.com/server/docs/about-netplan) 配置来管理网络。您指定的信息与 Red Hat 派生发行版相同。Netplan 是 NetworkManager 的一个接口，它使用 YAML 文件配置网络设置。

编辑 /etc/netplan 目录中的默认文件以添加网络接口的设置。请注意，此文件是 YAML 格式的，对语法（尤其是空格）非常挑剔。请记住使用 sudo 运行文本编辑器以提升您的权限。

以下是一个 enp0s5 接口的示例条目。只需将 IP 设置替换为您的网络的相应值即可。dhcp4: no 参数将其设置为静态 IP 地址。如果系统当前是 DHCP 客户端，则此行将读取 dhcp4: true。

```yaml
ethernets:
  enp0s5:
    dhcp4: no
    addresses: [192.168.2.200/24]
    gateway: 192.168.2.1
    nameservers:
      addresses: [192.168.2.10, 192.168.2.11]
```

保存并关闭文件，然后运行以下命令更新设置：

```bash
$ sudo netplan apply
```

使用 ip addr 命令（或尝试 hostname -I 命令）确认 IP 地址是否正确。
编辑 [YAML 文档](https://yaml.org/spec/1.2.2/#chapter-1-introduction-to-yaml) 时要小心。YAML 对空格非常敏感，因此请确保与模板匹配。

如果您想将系统设置为 DHCP 客户端而不是维护静态 IP 地址配置，请通过删除 addresses 和 nameservers 行来编辑文件，然后将 DHCP 行设置为 dhcp4: true。然后系统将成为 DHCP 客户端。

### 使用图形界面进行静态 IP 配置
网络设置图形用户界面包含一个手动选项，允许管理员配置 IP 地址、子网掩码、网关和 DNS 服务器条目。请务必小心避免在此处出现打字错误。您还必须记住，网络上的任何系统都不能具有相同的 IP 地址，因此需要仔细记录静态分配的 IP 地址。此配置工具在各种发行版中相似，因为始终需要相同的网络设置。

![](https://cdn.thenewstack.io/media/2024/07/468baae5-gui-static-ip.png)
### 动态 IP 地址配置
最终用户工作站很少需要被网络上的其他系统发现。由于业务数据通常存储在 Linux 文件服务器上并从那里共享，因此用户系统上应该很少有其他系统必须引用的内容。因此，没有必要拥有永久的静态 IP 地址。让这些设备从中央服务器获取 IP 地址效率更高。

动态主机配置协议 (DHCP) 服务使管理员能够定义一个服务器，该服务器具有一个可用的 IP 地址池及其所有相关设置（子网掩码、默认网关/路由器等）。在引导过程中，DHCP 客户端设备发送网络广播请求使用 IP 地址。DHCP 将 IP 配置租借给客户端。与管理员进行静态配置相比，此过程更简单、更灵活、更快。它也更不容易出错。

DHCP 租约生成过程包括由客户端系统发起的四个步骤。这些步骤允许客户端请求 IP 设置并让 DHCP 服务器响应。

以下是步骤：

- DHCPDiscover：客户端设备发出的广播，请求 DHCP 服务器。
- DHCPOffer：DHCP 服务器发出的响应，提供 IP 地址配置。
- DHCPRequest：DHCP 客户端发出的正式请求，请求使用提供的 IP 地址配置。
- DHCPAck：DHCP 服务器发出的对分配的配置的确认。
客户端设备定期向 DHCP 服务器进行检查以续订 IP 地址租约。

大多数客户端设备假设它们将是 DHCP 客户端，因此这通常是默认设置。从最终用户的角度来看，这意味着他们的计算机正在自行配置以进行网络连接。无论是在家庭环境还是企业网络中，您都可能将 Linux 系统保留为 DHCP 客户端。例如，当连接到咖啡店的无线网络和您的家庭时，Linux 笔记本电脑将是 DHCP 客户端。您希望笔记本电脑根据其所处的环境自行配置。

要使用 NetworkManager 将主机配置为 DHCP 客户端，请键入以下命令：

```bash
$ sudo nmcli con modify eth0 ipv4.method auto
```

使用以下 nmcli 命令重新加载接口：

```bash
$ sudo nmcli con down eth0
$ sudo nmcli con up eth0
```
如上所述，要将基于 Debian 的发行版设置为 DHCP 客户端，请在 `/etc/netplan` 目录中编辑接口文件，并添加以下条目：

```
dhcp4: true
```

### 使用图形界面配置 DHCP

图形网络配置工具提供了多种选项，包括自动（DHCP）或手动（静态）设置。自动设置将系统配置为 DHCP 客户端，使其能够完成上述租约生成过程。

![](https://cdn.thenewstack.io/media/2024/07/bcdb4c2f-rh-gui-dhcpclient.png)

大多数发行版都有非常类似的 GUI 网络配置工具。这些设置始终是必需的，因此任何图形工具都应该易于理解。

## 默认网关配置

DHCP 服务器提供的首要设置是客户端的 IP 地址和子网掩码。但是，DHCP 服务器可能还会包含默认网关值。此值是子网中路由器的 IP 地址。客户端计算机不需要路由器才能与同一子网上的其他节点通信，但它们确实需要路由器才能与其他子网上的机器通信。如果系统需要将信息发送到与自身网络 ID 不同的节点，则会将消息转发到路由器。默认网关值让计算机知道路由器在此过程中的位置。

网关 IP 地址是 DHCP 服务器提供的 IP 地址设置的一部分。如果管理员手动配置 IP 地址，则必须在该配置中设置网关值。

## 配置名称解析

主机名和 IP 地址之间的关系至关重要。大多数人通过主机名来引用系统，但大多数网络设备识别 IP 地址来管理通信。如果最终用户必须记住 172.16.33.58 是“color-sales-printer”或 192.168.2.10 是“dev-dept-fileserver”，那将非常困难。想象一下，如果您必须通过其特定的 IP 地址来跟踪所有您喜欢的互联网网站！

名称解析是指存储和使用有关哪些主机名与哪些 IP 地址相关的信息。

域名系统 (DNS) 提供名称解析。此服务维护一个主机名和 IP 地址数据库。如果用户输入包含主机名的命令，例如 ping server07，他们的工作站将查询 DNS，询问 server07 的 IP 地址。计算机无法基于主机名进行通信；TCP/IP 通信需要 IP 地址。但是，由于 IP 地址对于人们来说很难记住，因此他们需要能够通过名称来引用系统。DNS 将这两个值关联起来，以便网络节点和用户可以使用正确的数据。

假设您告诉您的计算机 ping server07。由于它不知道如何处理此名称，因此它会询问 DNS 服务器，DNS 服务器会以相应的 IP 地址进行响应。

该过程基本上如下所示：

- 用户输入 ping server07
- 他们的工作站不知道 server07 是什么，并且需要一个 IP 地址
- 工作站向 DNS 服务器发送查询，询问：“server07 的 IP 地址是什么？”
- DNS 服务器检查其资源记录，直到找到显示“server07 = 192.168.2.22”的记录
- 服务器响应工作站，说明：“server07 的 IP 地址是 192.168.2.22”
- 工作站运行 ping 192.168.2.22

工作站必须知道 DNS 服务器的 IP 地址，以便它可以发送查询。此设置对于计算机至关重要。DHCP 服务器通常会提供它，以及计算机的 IP 地址、子网掩码和默认网关。

以上示例假设内部业务网络上的名称解析。访问互联网上的网站使用该过程的更复杂变体。概念相似，但涉及更多 DNS 服务器。

DHCP 服务器通常会将 DNS 服务器 IP 地址作为标准 IP 地址设置的一部分提供给租用给客户端设备。

如果您正在管理服务器上的静态 IP 地址配置，则应设置 DNS 服务器 IP 地址。您可以使用 `nmcli` 命令静态配置客户端查询的 DNS 服务器。以下是一个示例：

```
$ sudo nmcli con mod "static-connection" ipv4.dns "192.168.2.10,192.168.2.11"
```

要手动配置客户端设备以查询 DNS 服务器，请编辑 `/etc/resolv.conf` 文件。您通常会指定两个 DNS 服务器（名称解析非常重要，足以证明使用多个服务器）。

![](https://cdn.thenewstack.io/media/2024/07/6d81ad6b-nameservers.png)

请务必使用 `sudo` 提升您的权限，以便编辑此文件。例如，要使用 Vim 编辑名称解析文件，请键入：

```
$ sudo vim /etc/resolv.conf
```

## 显示系统的 MAC 地址
可以使用 `ip` 命令显示网卡的 MAC 地址。这样做在故障排除或记录系统配置时可能很有用，但这不是您经常更改或自己使用的设置。

有多种命令可以显示系统上安装的每个网卡的 MAC 地址。以下是一些示例：

- `ip addr`：显示大量网卡信息，包括 IP 地址和 MAC 地址。
- `ip link show`：显示每个网卡的 MAC 地址、MTU 大小和状态。
- `ip link show eth0`：显示指定网卡（本例中为 eth0）的 MAC 地址、MTU 大小和状态。
![IP link 命令的屏幕截图。](https://cdn.thenewstack.io/media/2024/08/33675a7c-ip-link-show.png)
图 11：IP link 命令是显示 MAC 地址的几种命令之一。

在使用 [Nmap](https://nmap.org/)、[tcpdump](https://www.tcpdump.org/) 和 [Wireshark](https://thenewstack.io/wireshark-celebrates-25th-anniversary-with-a-new-foundation/) 等工具时，了解系统的 MAC 地址可能会有所帮助。这些故障排除实用程序显示详细的网络信息，包括 MAC 地址。您可能需要确定数据包的来源或哪个网卡正在网络上发送错误数据包。

在发送信息时，计算机会在数据帧中添加自己的 MAC 地址。它们还会添加目标计算机的 MAC 地址。源计算机必须发现同一网络段上任何目标系统的 MAC 地址。它们使用地址解析协议 (ARP) 查找此信息。每台计算机还会缓存（临时保存）它发现的 MAC 地址以提高效率。您可以查看和清除此缓存。

使用以下 `ip` 命令查看 Linux 计算机上的 MAC 地址缓存：

```
$ sudo ip neigh show
```
查看 MAC 地址缓存是了解段网络设备和排查连接失败的好方法。
使用以下命令清除 ARP 缓存：

```
$ sudo ip neigh flush all
```
清除缓存会强制计算机重新发现本地 MAC 地址，有助于确保缓存中的信息是最新的和准确的。
## 总结
识别联网计算机使用的三种身份对于安全审计、故障排除、系统配置等非常有用。每个身份都由网络基础设施的不同方面使用。

- 主机名：通常由人使用。
- IP 地址：通常由计算机和路由器使用。
- MAC 地址：通常由计算机和交换机使用。
MAC 地址几乎没有可用的配置，主机名通常在操作系统安装期间设置。IP 地址设置是大多数配置和故障排除将发生的地方。

管理员可以手动配置 IP 设置（称为“静态 IP 地址”），也可以允许系统从 DHCP 服务器租赁 IP 设置（称为“动态 IP 地址”）。无论哪种方式，常见的设置如下：

- IP 地址：显示计算机位于哪个网络段的逻辑地址。
- 子网掩码：指示 IP 地址的哪一部分是网络 ID，哪一部分是主机 ID。
- 默认网关：路由器的 IP 地址。
- 域名服务器：一个或多个 DNS 域名服务器的 IP 地址。
管理和排查 IP 地址是 Linux 管理员的一项标准技能。在管理 Linux 网络节点时，预计将在命令行和图形界面上工作。从今天开始探索 Linux 实验室计算机上的网络设置。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)