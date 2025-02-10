# 什么是 Linux 命名空间以及它们是如何使用的？

![Featued image for: What Are Linux Namespaces and How Are They Used?](https://cdn.thenewstack.io/media/2025/02/3d7503c1-getty-images-bdopvgvwcc0-unsplash-1024x683.jpg)

如果玫瑰在任何其他命名空间中，还会一样香吗？

莎士比亚现在正在敲打他的棺材，恳求我删除这句扭曲的引言，但我要对这位诗人说：“不，不”。

自 2002 年以来，命名空间一直是 [Linux kernel](https://thenewstack.io/linux-kernel-6-13-stands-ready-with-security-performance-driver-updates/) 的一项功能。从那时起，它们已经演变成 Linux 安全的一个非常重要的方面。但直到 [containers](https://thenewstack.io/bytedance-to-network-a-million-containers-with-netkit/) 的出现，命名空间的重要性才变得显而易见。

从本质上讲，[namespaces](https://man7.org/linux/man-pages/man7/namespaces.7.html) 限制了容器化进程可以看到的资源，因此一个进程无法看到另一个进程正在使用的资源。此功能对于容器和 Kubernetes 等编排工具至关重要，因为否则，一个已部署的容器将能够访问或查看另一个容器使用的资源。

我的朋友们，这是一个安全问题。如果一个容器能够以资源级别[与另一个容器交互](https://thenewstack.io/runc-related-leaky-vessels-threaten-container-security/)，那么一段恶意代码可能会对您的系统、网络和数据造成严重破坏。

命名空间的隔离发生在内核级别，以将进程彼此隔离。

Linux 命名空间有不同的类型，包括：

- 用户命名空间 – 添加唯一的用户 ID 和组 ID 以分配给进程，这意味着某些进程可能具有管理员权限，而其他进程则没有。
- 进程 ID 命名空间 – 这会将一组 PID 分配给一个命名空间中的进程，同时能够将不同的 PID 分配给不同命名空间中的相同进程。
- 网络命名空间 – 这是一个独立的网络堆栈（路由表、IP 地址、套接字列表、连接跟踪表、防火墙等），可以分配给特定的命名空间。
- 挂载命名空间 – 一个独立的挂载点列表，对于命名空间内的进程可见。
- 进程间通信 (IPC) 命名空间 – 可以分配它自己的 IPC 资源。
- UNIX 分时命名空间 – 可以为不同的进程分配不同的主机名和域名。

## 如何在 Linux 上创建命名空间

假设您想要创建两个网络命名空间，然后允许它们相互连接。

第一步是创建命名空间。我们将这些命名空间称为 net1 和 net2，并使用以下命令创建它们：

```
sudo ip netns add net1
sudo ip netns add net2
```

接下来，我们必须为两个接口创建一个管道（一个虚拟以太网对），这可以通过以下命令完成：

```
sudo ip link add veth0 type veth peer name veth1
```

现在我们必须将我们的命名空间与管道关联起来，如下所示：

```
sudo ip link set veth0 netns net1
sudo ip link set veth1 netns net2
```

下一步是为每个虚拟接口提供一个 IP 地址。确保您不要设置网络上已在使用的 IP 地址；否则，您最终会遇到冲突。我们将使用以下命令将 192.168.1.100 分配给 veth0，将 192.168.1.101 分配给 veth1：

```
sudo ip -n s1 addr add 192.168.1.100/24 dev veth0
sudo ip -n s1 addr add 192.168.1.101/24 dev veth1
```

太棒了。
您现在可以验证 IP 地址是否已分配并查看 arp 表。要查看 net1 的 IP 地址，命令将是：

```
sudo ip netns exec net1 ip addr
```

输出应如下所示：
如您所见，正确的 IP 地址已分配给 net1。可以使用以下命令对 net2 执行相同的操作：

```
sudo ip netns exec net2 ip addr
```

我们现在可以使用以下命令启动这些接口：

```
sudo ip -n net1 link set veth0 up
sudo ip -n net2 link set veth1 up
```

现在让我们测试一下它们是否可以互相 ping。我们将使用以下命令从 net1 ping net2：

```
sudo ip netns exec net1 ping 192.168.1.101
```

使用以下命令从 net2 ping net1：

```
sudo ip netns exec net2 ping 192.168.1.100
```

在这两种情况下，您都应该看到成功的 ping 结果。
现在，让我们尝试从主机 ping 192.168.1.100 IP 地址。只要您的网络上没有具有该地址的设备，它应该是无法访问的：

```
ping 192.168.1.100
```

您应该无法访问该地址。
您所做的本质上是创建了两个可以相互访问但不能被任何其他资源访问的网络命名空间。这就是命名空间的全部意义。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)