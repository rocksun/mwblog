
<!--
title: 如何管理Linux防火墙
cover: https://cdn.thenewstack.io/media/2024/08/10729184-rowan-heuvel-yq0hnz6cqyo-unsplash.jpg
-->

防火墙是分层安全方法的重要组成部分。以下是如何定期监控和测试防火墙配置以确保安全。

> 译自 [How to Manage a Linux Firewall](https://thenewstack.io/how-to-manage-a-linux-firewall/)，作者 Damon M Garn。

防火墙控制对网络和（可能）网络设备（包括工作站和服务器）的访问。管理员依靠防火墙根据各种标准（包括源、目标和协议类型）允许或拒绝连接。

防火墙具有以下三个主要功能：

- 过滤网络流量。
- 充当网络和网络段之间的守门员。
- 记录和监控网络连接尝试。

一些防火墙提供额外的功能以允许更多连接类型。这些功能包括：

- 网络地址转换 (NAT) 支持，用于管理内部和外部 IP 地址。
- 虚拟专用网络 (VPN) 端点支持，允许安全连接。

这些功能通过控制连接来帮助避免恶意软件。它们还控制内部和外部客户端对敏感信息的访问。最后，防火墙帮助组织实施可靠、可预测和有效的安全策略，以证明合规性。

一些防火墙（包括 Linux [firewalld](https://firewalld.org/) 服务）使用预定义区域来设置通用规则。受信任网络（例如您家或公司网络）的防火墙区域将允许与公共或不受信任网络的区域不同的入站连接集，后者可能根本不允许任何入站连接。

防火墙配置几乎总是默认使用“拒绝所有”策略，这意味着防火墙拒绝所有入站流量，管理员为合法流量配置例外。例如，如果防火墙保护包含 Web 服务器的网络段，则所有流量都会被阻止，然后管理员显式打开端口 80 (HTTP) 和 443 (HTTPS)。

防火墙通常存在于两个地方：作为网络或段之间的守门员，以及作为控制进出单个设备流量的控制器。

- 基于网络的防火墙：控制网络或网络段之间的访问，以保护每个段中的所有数据和设备。
- 基于主机的防火墙：控制进出设备的连接，帮助保护每个设备上的数据和服务。

管理员可以将 Linux 系统配置为网络路由器和防火墙，尽管为此功能存在更有效的专用硬件设备。但是，基本的 Linux 防火墙可以设置为管理网络控制。您通常会将 Linux 防火墙配置为基于主机的解决方案，以保护该特定设备。

您可以按照“[Linux: Linux 技能模块库配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)”文章中找到的信息构建一个用于练习防火墙设置的实验室环境。如果您需要复习 Linux 命令的语法，请参考“[了解 Linux 命令行”](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 文章。

*注意：以 root（管理员）用户身份登录 Linux 系统是一种糟糕的安全做法。大多数系统会强制您以普通用户身份登录，然后使用 sudo（超级用户执行）命令提升您的权限。使用 sudo 时，您可能会被提示输入密码。本教程中的一些命令可能需要在您的 Linux 发行版上使用 sudo 命令。*

## 了解防火墙如何管理网络流量

基本的防火墙根据三个标准识别网络流量：源、目标和协议。防火墙通过检查 TCP/IP 通信中找到的寻址信息来实现这一点。这些数据显示发送设备的 IP 地址、目标系统的 IP 地址以及正在使用的通信协议。

假设工作站3的IP地址为192.168.2.200，想要建立与IP地址为192.168.2.10的webserver02的HTTP连接。防火墙会检查其规则，以查看是否允许客户端设备向目标服务器发送流量。它还会检查规则，以查看是否允许HTTP（端口80）流量。

人们倾向于通过协议来识别应用程序层服务，例如超文本传输协议（HTTP）、简单邮件传输协议（SMTP）或安全外壳（SSH）。网络设备通常不通过名称识别这些协议，而是通过称为端口号的数值来识别它们。可能有超过65,000个可能的端口号，但只有前1,023个是标准化的。这些被称为“众所周知的”端口号。

以下是一些常见的协议及其众所周知的端口号：

- 超文本传输协议（HTTP）：端口80，Web服务
- 超文本传输协议安全（HTTPS）：端口443，加密的Web服务
- 安全外壳（SSH）：端口22，安全的远程管理
- 文件传输协议（FTP）：端口21，文件传输
- 简单邮件传输协议（SMTP）：端口25，电子邮件传输
- 邮局协议v3（POP3）：端口110，访问电子邮件
- 互联网邮件访问协议（IMAP4）：端口143，访问电子邮件
- 网络时间协议（NTP）：端口123，时间同步
- 远程桌面协议（RDP）：端口3389，远程连接到图形用户界面

一些防火墙通过名称识别这些协议，但您通常需要使用端口号配置防火墙，因此最好记住这些端口号。

## 常见的Linux防火墙接口

Linux的底层防火墙服务是iptables或nftables。这些是Linux内核的可配置部分，能够过滤网络流量。您将使用前端应用程序来管理这些设置。有几个这样的前端程序，但下面列出了两个最常见的：

- **Uncomplicated Firewall (UFW):** 简单直观的配置，但功能相对较少。
- **firewalld**: 更复杂，但具有更多配置选项。

它们之间的主要区别在于易用性和高级配置。此外，大多数源自Debian的Linux发行版使用UFW，而源自Red Hat的发行版通常依赖于firewalld。

## Uncomplicated Firewall (UFW) 设置

基本命令语法是[ufw](https://manpages.org/ufw/8)命令，后跟一个或多个子命令和配置参数。使用UFW时，这些命令通常非常简单。

如果您使用的是基于Debian的系统，并且不确定当前配置，那么重置UFW到其默认值可能是一个好主意。我不建议在生产工作站或服务器上执行此操作，因为它可能会中断通信。

使用以下命令重置入站和出站UFW设置：

```
$ sudo ufw default deny incoming
$ sudo ufw default deny outgoing
```

您应该看到一条消息，表明每个命令都成功执行。

基于网络的应用程序通常会向UFW注册自己。使用以下命令显示已注册的应用程序：

```
$ sudo ufw app list
```

列表将根据已安装的程序而有所不同。假设本教程中安装了OpenSSH。

请注意，UFW允许针对特定接口设置特定规则集。这在具有连接到不同段的多个网络接口卡的服务器上非常有用。

使用以下命令启用SSH服务，以允许流量通过UFW防火墙：

```
$ sudo ufw allow OpenSSH
```

此命令有效是因为OpenSSH已注册。UFW将允许SSH连接在端口22上。

一种可能的安全性设置是更改各种服务的默认端口。虽然端口22是SSH的众所周知的端口，但您可以将其配置为使用其他端口，例如2222。在这种情况下，您需要将UFW设置为识别该端口。

使用此命令在UFW中定义允许的特定端口号：

```
$ sudo ufw allow 2222
```

最后一步是使用更新的规则启用UFW。使用以下两个命令重置UFW：

```
$ sudo ufw disable
$ sudo ufw enable
```

使用
`sudo ufw logging on` 命令管理UFW日志文件设置。

您可以随时使用status子命令查看您的设置：

```
$ sudo ufw status
```

上述配置允许来自任何工作站的入站SSH连接。但是，SSH主要是一个系统管理员工具，因此可能只有有限数量的工作站需要通过SSH连接。假设您只希望允许来自位于 192.168.2.42 的系统管理员工作站的SSH连接。使用以下命令：

```
$ sudo ufw allow from 192.168.2.42 to any port 22
```

连接源是192.168.2.42（管理员计算机），目标是端口22（SSH）。

UFW允许对此想法进行许多变体。例如，它识别子网作为进一步集中规则的一种方式。

那么拒绝设置呢？ UFW 允许管理员指定要阻止通信的特定 IP 地址（或子网）。 当需要明确阻止某个系统访问或 DDoS 攻击来自特定主机时，这可能很有用。 此类规则的一个示例是：

```
$ sudo ufw deny from 192.168.2.200
```

总而言之，在添加或删除规则以控制访问之前，请先检查当前的 UFW 设置。 完成后启用设置。 以下是步骤：

1. 列出当前规则：`sudo ufw status`
2. 添加任何必要的规则：`sudo ufw allow OpenSSH`
3. 查看更新后的规则：`sudo ufw status`
4. 重新加载 UFW 配置：`sudo ufw disable` 然后 `sudo ufw enable`

![](https://cdn.thenewstack.io/media/2024/07/793f8336-openssh-status.png)

*图 1：允许 OpenSSH 应用通过 UFW*

UFW 的主要配置文件是 `/etc/default/ufw`，它允许您定义默认策略等。

## Firewalld 设置

源自 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的 Linux 发行版倾向于依赖 firewalld 接口来管理连接。 此实用程序使用 [firewall-cmd](https://manpages.org/firewall-cmd) 命令以及一系列标志来定义您的设置。 但是，总体功能与 UFW 相同——定义允许哪些连接以及不允许哪些连接。 您可以通过服务名称、协议或端口号来执行此操作。

该 `firewall-cmd` 命令管理 firewalld 设置。 此命令包含许多标志来显示和配置规则。 请注意，这些标志使用两个连字符 (`--option`)，而许多其他 Linux 命令选项只使用一个连字符 (`-option`)。 使用一个 `=` 字符来定义参数或设置。

```
$ sudo firewall-cmd --list-all
```

![](https://cdn.thenewstack.io/media/2024/07/ed38734c-firewallcmd-list-all.png)

*图 2：firewall-cmd 命令展示了默认区域的规则。*

此示例显示当前区域的当前规则。 以下是一些示例，包括一些带有参数设置的示例。

Firewalld 使用区域来定义不同的角色或访问类型。 这些区域具有不同的默认规则，您创建的任何自定义规则也是特定于区域的。 使用区域可以使防火墙配置更容易，特别是对于在网络中更改位置或用途的设备。

一些常见的区域包括：

- 家庭
- 工作
- 内部
- DMZ
- [Docker](https://www.docker.com/?utm_content=inline+mention)
- 公共

公共区域通常是大多数安装的默认区域。 如果您没有指定区域，系统将假定默认区域。 使用 `--set-default-zone=internal` 设置来设置默认区域。

Firewalld 允许您在每个接口的基础上设置区域，这对于连接到多个子网的服务器很有用。 例如，您可能有一个设置为工作或内部区域的部门 Linux 服务器，以及一个为公共区域配置的面向互联网的 Linux 服务器。

使用 `--get-active-zones` 子命令显示系统上的当前区域：

```
$ sudo firewall-cmd --get-active-zones
```

使用 `--get-zones` 选项列出系统上的所有区域：

```
$ sudo firewall-cmd --get-zones
```

![](https://cdn.thenewstack.io/media/2024/07/9641714d-firewallcmd-get-zones.png)

*图 3：--get-zones 子命令显示可用区域。*

这些是系统上所有现有的区域。

使用以下命令显示区域及其规则的详细列表：

```
$ sudo firewall-cmd --list-all-zones
```

您可以将区域分配给 Linux 系统中的每个网络接口卡。 首先使用 `ip addr` 命令显示现有的接口：

```
$ sudo ip addr
```

然后运行以下命令将接口设置为公共区域：

```
$ sudo firewall-cmd --change-interface=enp0s5 --zone=public --permanent
```

![](https://cdn.thenewstack.io/media/2024/07/91ecbee2-changezones.png)

*图 4：将网卡分配到特定的区域。*

Firewalld 通过将潜在的连接类型与特定服务相关联来识别它们。 例如 ssh、http、https 等。 如果这些服务不符合您的需求——也许您有使用非标准端口号的自定义应用程序或服务——您可以创建您需要的任何自定义规则。

以下是一些常见的配置选项：

- `--permanent`
- `--zone=`
- `--add-service=`
- `--add-port=`
- `--remove-service=`
- `--remove-port=`
- `--reload`

我在下面介绍了这些选项的使用。

请特别注意 `--permanent` 选项。 使用它可以使条目在重启后持久存在。 如果您不包含该选项，firewalld 将假定您正在对当前运行时进行临时规则更改。

我在上面的 UFW 示例中使用了 SSH 服务。 我将在 firewalld 中做同样的事情。

```
$ sudo firewall-cmd --zone=public --add-service=ssh --permanent
```

您可以为内部网络应用程序使用自定义端口号。 您也可以尝试通过使用与默认端口不同的网络端口来隐藏网络服务（例如，将 SSH 设置为端口 2222 而不是 22）。 如果您需要通过端口号定义设置，请使用 `--add-port=` 选项。 以下是 SSH 端口 22 的相同示例：

```
$ sudo firewall-cmd --zone=public --add-port=22/tcp --permanent
```

$ sudo firewall-cmd --zone=public --add-port=22/tcp --permanent
请注意，端口号值也显示了
tcp 传输层协议。

![](https://cdn.thenewstack.io/media/2024/07/654b1574-add-ssh-service.png)

*图 5：为已识别的服务配置防火墙。*

![](https://cdn.thenewstack.io/media/2024/07/06780bc5-add-ssh-port.png)

*图 6：针对特定端口号配置防火墙。*

使用以下命令查看您的设置：

```
$ sudo firewall-cmd --list-all
```

请注意，SSH 通常默认情况下是允许的。

使用相同的语法，使用 --remove-service=ssh 或 --remove-port=22/tcp 标志删除条目。例如，要阻止 SSH 服务，请键入以下命令：

```
$ sudo firewall-cmd --zone=public --remove-service=ssh --permanent
```

您指定的 firewalld 设置不会立即生效。Firewalld 假设您需要时间来创建、编辑或删除规则中的各种条目。完成配置微调后，使用
--reload 选项实施更改。

```
$ sudo firewall-cmd --reload
```

![](https://cdn.thenewstack.io/media/2024/07/60c162f5-reload.png)

*图 7：在进行任何更改后重新加载防火墙配置。*

请记住，如果您在规则中不包含 --permanent 标志，它们在下次重启后将不会持久保存。

以下是基本配置的摘要。查看设置，添加或删除规则并重新加载配置。以下步骤作为指南：

1. 列出当前规则：sudo firewall-cmd --zone=public --list-all
2. 永久添加任何必要的规则：sudo firewall-cmd --zone-public --add-service=ssh --permanent
3. 删除不再适用的任何规则：sudo firewall-cmd --zone-public --remove-service=http --permanent
4. 查看新设置：sudo firewall-cmd --zone=public --list all
5. 重新加载防火墙以更新设置：sudo firewall-cmd --reload

## 图形防火墙界面怎么样？

使用图形界面处理系统配置通常更容易。命令行工具速度快且可脚本化，但前提是您记得特定的命令。如果您坐在带有图形用户界面 (GUI) 的 Linux 工作站上，并且只需要快速添加防火墙规则，那么图形工具可能是最好的选择。

UFW 和 firewalld 都提供 GUI 选项。

### GUFW 界面

如果您的 Debian 基于发行版上尚未安装 GUFW，请使用以下步骤。您必须添加 universe 存储库，更新 Apt 配置并安装软件包。以下是命令：

```
$ sudo apt add-apt-repository universe
$ sudo apt update
$ sudo apt install gufw -y
```

安装完成后，通过搜索 GUFW 访问新的 GUI 防火墙界面。

![](https://cdn.thenewstack.io/media/2024/07/8156cb55-search-gufw.png)

*图 8：如果已安装，搜索 GUFW 接口。*

您可以启用和禁用防火墙（在禁用之前请仔细考虑）。您还可以更改配置文件。您的选择是家庭、办公室、公共和自定义。这些类似于 firewalld 区域。最后，添加或删除规则以允许或拒绝指定流量。

![](https://cdn.thenewstack.io/media/2024/07/50dac73c-gufw-profiles.png)

*图 9：选择合适的配置文件。*

![](https://cdn.thenewstack.io/media/2024/07/60b538fd-gufw-open22.png)

*图 10：添加规则，比如允许端口 22 的流量。*

### firewall-config 界面
如果您使用的是与 Red Hat Linux 相关的 Linux 发行版，请添加 firewall-config 实用程序以使用图形界面配置防火墙。

使用此命令安装 firewall-config：

```
$ sudo dnf install -y firewall-config
```

搜索“firewall”一词以查找 GUI 防火墙控制台。

![](https://cdn.thenewstack.io/media/2024/07/c811d840-firewall-gui.png)

*图 11：搜索 GUI 防火墙配置工具。*

该界面显示了可用的区域（与命令行 firewall-cmd 工具中找到的区域相同）。选择一个区域，然后使用每个列出服务的复选框来允许或拒绝访问。

![](https://cdn.thenewstack.io/media/2024/07/05442412-firewall-config-gui.png)

*图 12：选择一个区域，然后选中允许的协议或服务的复选框。*

## 测试防火墙配置

测试防火墙设置也是一个好主意。显然，您可以阅读规则和逻辑，了解它们对入站连接尝试应该产生什么影响。这对于基本审计和确认当然有效。但是，您还应该测试来自远程系统的允许连接，以确保*应该*有访问权限的服务实际上*确实*有访问权限。最后，考虑使用网络扫描应用程序（如 [Nmap](https://nmap.org/)）来验证设置。这种方法比检查来自大量远程设备的连接效率更高。

## 总结

防火墙是分层安全方法的重要组成部分。定期监控和测试防火墙配置，以确保网络服务和系统得到妥善保护。

在大多数情况下，Linux 工作站和服务器应使用基于主机的防火墙配置，以仅允许必要的入站连接。连接将根据设备的角色（例如 Web 服务器或数据库主机）而有所不同。防火墙通常默认为“拒绝所有”配置。

一些管理员使用 Linux 系统作为网络段之间的路由器。防火墙机制也支持此角色。

您必须知道您选择的发行版上提供了哪些防火墙界面。

- UFW：在基于 Debian 的系统上找到，包括 Ubuntu、Linux Mint 和 Debian 本身。
- firewalld：在基于 Red Hat 的系统上找到，包括 Red Hat Enterprise Linux (RHEL)、Fedora、[AlmaLinux](https://thenewstack.io/almalinux-makes-in-place-upgradeseasier-for-centos-users/) 和 [Rocky Linux](https://thenewstack.io/post-centos-rocky-linux-fights-for-community-driven-enterprise-open-source/)。

评估设备所需的连接类型，然后检查现有的防火墙规则以确保它们匹配。如果它们不匹配，请添加或删除规则，直到只允许所需的连接。不要忘记启用设置并使其在重启后保持持久。

当然，通过图形界面管理防火墙设置并没有错，尤其是在最终用户设备（如笔记本电脑）上。您使用的界面将因发行版而异。

- GUFW：对于基于 UFW 的系统，例如那些源自 Debian 的系统。
- firewall-config：对于基于 firewalld 的系统，例如那些源自 Red Hat Linux 的系统。

从今天开始，审查和修改您当前的防火墙配置，以确保与您的 Linux 设备的安全、受控连接。
