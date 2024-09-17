# AlmaLinux: Deploying a DHCP Server for Your Internal Network

![AlmaLinux: Deploying a DHCP Server for Your Internal Network](https://cdn.thenewstack.io/media/2024/07/31ad3212-alma-linux-1024x683.jpg)

Your network likely already has a DHCP server. DHCP stands for [Dynamic Host Configuration Protocol](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top), which is the network protocol that connects your internal servers to the internet.

However, if that DHCP server happens to also be your router or modem, you might be missing out on the flexibility and power that comes with deploying a DHCP server on a dedicated server.

There are also security concerns.

Consider this: When using your router or modem as a DHCP server, you are locked into that device and whatever security updates its manufacturer releases. In today's environment where new [vulnerabilities](https://thenewstack.io/kubernetes-access-vulnerability-found-in-windows-nodes/) are discovered every day, that might not be fast enough.

If you are serious about security, you might prefer to have more control over such things.

That's where Linux comes in. By deploying a DHCP server on a traditional Linux server, you can control updates and even the security of the device. When you adopt [AlmaLinux](https://thenewstack.io/almalinux-makes-in-place-upgradeseasier-for-centos-users/) as your DHCP server, you also get the benefits of SELinux and other security mechanisms that help lock down the operating system.

I want to show you how easy it is to deploy a DHCP server using [AlmaLinux](https://thenewstack.io/almalinux-your-enterprise-linux-ticket-to-freedom/).

![DHCP Diagram](https://cdn.thenewstack.io/media/2024/09/f102cf55-roadmapsh-dhcp-813x1024.png)
Source: [Roamap.sh](https://roadmap.sh/guides/dhcp-in-one-picture)

## What You Need

You only need a running AlmaLinux instance and a user with [sudo privileges](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/). It's important to note that you want to make sure that you don't have multiple DHCP servers running on your network. If you have multiple DHCP servers working, you might run into address conflicts, which can lead to more trouble than you want to deal with.

If you already have a DHCP server running with your router or modem, make sure to disable that functionality when deploying your new machine.

## Update AlmaLinux

Before we dive in, make sure your AlmaLinux instance is up to date. To do this, log in to your server and issue the following command:

```
sudo dnf update
```

Once that's done, you can move on. But be aware that if the kernel is upgraded, you will need to reboot your machine for the changes to take effect.

## Install the DHCP Server Software

To install the DHCP server software, issue the following command:

```
sudo dnf install dhcp-server -y
```

The DHCP service is not currently running, and we will keep it that way until we handle some configuration (otherwise, you might run into problems).

## Configure Your New DHCP Server

The first thing you need to do is find the name of the network interface you will be using. To do this, issue the following command:

```
ip a
```

You should see something like this in the output:

```
enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000 link/ether 08:00:27:b6:98:a3 brd ff:ff:ff:ff:ff:ff
```

The name of the network interface above is enp0s3. This is the information you need.

Open the necessary configuration file using the following command:

```
sudo nano /etc/dhcp/dhcpd.conf
```

In that file, you will only find a few lines of commented-out code. Luckily, the DHCP server software comes with an example configuration file that you can view using the following command:

```
less /usr/share/doc/dhcp-server/dhcpd.conf.example
```

You can view that file side-by-side with your actual configuration file or use the following command to copy a copy of that file to the location of your empty file:

```
sudo cp /usr/share/doc/dhcp-server/dhcpd.conf.example /etc/dhcp/dhcpd.conf
```

You will need to customize a few lines/sections. The first thing to look for is the following two-line block:

```
*default-lease-time 900;*
*max-lease-time 10800;*
```

You need to make sure to customize the default lease time and the maximum lease time for the DHCP addresses that your server will be handing out.

Next, make sure to uncomment (remove the # character at the beginning) the following line:

```
#authoritative;
```

So that the line looks like this:

```
authoritative;
```

Finally, look for the following section:

```
subnet 192.168.1.0 netmask 255.255.255.0 {
  range 192.168.1.51 192.168.200.99;
  option routers 192.168.1.1;
  option subnet-mask 255.255.255.0;
  option domain-name-servers 192.168.1.1;
}
```

- The `option routers` line specifies the list of IP addresses of the routers on the client subnet.
- The `option subnet-mask` defines the subnet of the network.

### EDITOR'S RESPONSE
- 选项 `domain-name-servers` 是您要使用的 DNS 服务器列表。
您需要调整上述部分中的地址以匹配您的网络以及您希望服务器分配的地址范围。

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

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)