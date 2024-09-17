
<!--
title: AlmaLinux：为您的内部网络部署DHCP服务器
cover: https://cdn.thenewstack.io/media/2024/07/31ad3212-alma-linux.jpg
-->

通过将 DHCP 服务器部署到单独的 Linux 服务器上以运行您的内部网络，您可以控制更新甚至设备的安全性。

> 译自 [AlmaLinux: Deploy a DHCP Server for Your Internal Network](https://thenewstack.io/almalinux-deploy-a-dhcp-server-for-your-internal-network/)，作者 Jack Wallen。

在你的网络中，你已经有一个 DHCP 服务器的可能性很大。DHCP 代表动态主机配置协议，它是一个利用网络协议桥接你的内部服务器和互联网的网络协议。

但是如果那个 DHCP 服务器恰好也充当你的路由器或调制解调器，你可能会错过在专用服务器上部署 DHCP 服务器所带来的灵活性与强大功能。

同时还有安全问题。

考虑以下情况：在将路由器或调制解调器用作 DHCP 服务器时，你只能用那台设备，并且依赖设备制造商发布安全更新的时间。对于每天都会发现新漏洞的当今网络环境来说，这可能不够快。

如果你非常重视安全性，你也许更喜欢对这样的事情有更多控制的想法。

这就是 Linux 发挥作用的地方。通过传统的 Linux 服务器部署 DHCP 服务器，你可以控制更新甚至设备的安全性。当你采用 AlmaLinux 作为你的 DHCP 服务器时，你还可以获得 SELinux 和其他安全机制的优势，这些机制有助于锁定操作系统。

我想向你展示使用 AlmaLinux 部署 DHCP 服务器有多么容易。

![DHCP Diagram](https://cdn.thenewstack.io/media/2024/09/f102cf55-roadmapsh-dhcp-813x1024.png)

*Source: [Roamap.sh](https://roadmap.sh/guides/dhcp-in-one-picture)*

## 你需要的东西

完成此项操作，你唯一需要的是 AlmaLinux 的一个正在运行的实例和一个拥有 sudo 权限的用户。需要记住的一件事是，你想确保你的网络上不会出现多个 DHCP 服务器。如果有多个 DHCP 服务器在工作，你可能会产生地址冲突，这可能会造成比你想处理的更多的麻烦。

如果你已经通过路由器或调制解调器拥有了一个 DHCP 服务器，在你部署新设备时，请务必关闭该功能。

## 更新 AlmaLinux 

进入正题之前，请确保您的 AlmaLinux 实例是最新的。为此，请登录至服务器并发出命令：

```
sudo dnf update
```

一旦完成，你就可以继续了。但请注意，若内核升级，你需要重启机器以使变更生效。

## 安装DHCP服务器软件

要安装 DHCP 服务器软件，请发出以下命令：

```
sudo dnf install dhcp-server -y
```

DHCP服务目前未运行，在进行一些配置之前，我们先将其保留这样（否则，可能会出现问题）。

## 配置您的新 DHCP 服务器

你需要做的第一件事是找到网络接口的名称。若要执行此操作，请发出以下命令：

```
ip a
```

您应在输出中看到类似以下内容：

```
enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 08:00:27:b6:98:a3 brd ff:ff:ff:ff:ff:ff
```

上面网卡接口的名称为 enp0s3。这些信息是您所需要的。

使用命令打开必要的配置文件：

```
sudo nano /etc/dhcp/dhcpd.conf
```

在那个文件中，你不会发现除了一些被注释掉的行以外的任何内容。幸运的是，DHCP 服务器软件带有一个示例配置文件，可以通过以下命令查看：

```
less /usr/share/doc/dhcp-server/dhcpd.conf.example
```

您可以按原样查看文件与实际配置文件并排显示，或使用该命令在空文件所在位置创建该文件的副本：

```
sudo cp /usr/share/doc/dhcp-server/dhcpd.conf.example /etc/dhcp/dhcpd.conf
```

有几行/部分需要定制。要查找的第一部分是这两行代码块：

```
*default-lease-time 900;*
*max-lease-time 10800;*
```

您需要自定义 DHCP 地址的默认租用时间和最大租用时间，以便服务器可以分配这些地址。

接下来，请确保取消注释（删除开头的 # 字符），以便在该行中：

```
#authoritative;
```

所以那条线看起来像：

```
authoritative;
```

最后，查看以下部分：

```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.51 192.168.200.99;
  option routers 192.168.1.1;
  option subnet-mask 255.255.255.0;
  option domain-name-servers 192.168.1.1;
}
```

- 选项路由器线路为客户端的子网中路由器的 IP 地址清单
- 子网选项为网络定义子网
- 域名服务器选项是希望使用的 DNS 服务器清单

您需要调整以上部分中的地址以匹配您的网络以及您想要服务器给出的地址范围。

例如，您可能在网络上为静态 IP（例如其他服务器）保留了从 192.168.1.10 到 192.168.1.50 的地址。因此，您不希望 DHCP 服务器分配该范围内的地址，否则会发生冲突。

保存并关闭文件。

## 打开防火墙

接下来，您需要打开防火墙，以便服务器可以接受来自网络中机器的 DHCP 请求。DHCP 服务器使用端口 67，因此使用以下命令打开它：

```
sudo firewall-cmd --add-port=67/udp --permanent
```

使用以下命令重新加载防火墙：

```
sudo firewall-cmd --reload
```

## 启动并启用服务

一切就绪后，您需要启动并启用服务。使用以下命令执行此操作：

```
sudo systemctl enable --now dhcpd
```

您的 AlmaLinux 服务器现在正在接受 DHCP 请求，并将根据需要分配地址。此服务器应该为您不懈地工作，但请确保定期检查并应用任何可用的升级。

就是这样，您自己的 DHCP 服务器，它应该比您以前使用的更强大、更灵活。享受！
