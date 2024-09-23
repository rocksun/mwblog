
<!--
title: Linux：创建和连接NFS共享
cover: https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux.jpg
-->

如果您需要比 Samba 更快的复制和写入速度，NFS 是一个不错的选择。请记住，NFS 不如 Samba 灵活。

> 译自 [Linux: Create and Connect to an NFS Share](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/)，作者 Jack Wallen。

NFS 代表[网络文件系统](https://www.techtarget.com/searchenterprisedesktop/definition/Network-File-System)，是另一种通过网络共享目录的方式。NFS 自 80 年代中期就已经出现，虽然它不像 [Samba 那样易于使用](https://thenewstack.io/create-a-samba-share-and-use-from-in-a-docker-container/)，但它仍然是一种有效的共享文件和文件夹的协议。

但是为什么要选择 NFS 而不是 Samba 呢？最大的原因之一是 NFS 比 Samba 快得多。在共享较大文件时尤其如此。我亲眼目睹过 Samba 共享无缘无故地变得非常缓慢。而使用 NFS，这种情况不太可能发生。

NFS 的两个主要缺点是它不像 Samba 那样易于使用（这就是很多人选择 SMB 路线的原因），而且它不包含任何访问控制方法。因此，只能在您信任的安全机器和网络上使用 NFS。如果您需要更好的基于 LAN 的共享性能，NFS 是一个很好的选择。

让我向您展示如何做到这一点。

## 您需要什么

在本演示中，您需要在同一个 LAN 上有两台 [Linux 机器](https://thenewstack.io/linux-server-operating-systems-red-hat-enterprise-linux-and-beyond/)。您使用什么发行版并不重要（因为必要的 NFS 软件可以从大多数标准存储库中获得）。您还需要一个具有 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)的用户。我将在 [Pop!_OS](https://pop.system76.com/) 和 [AlmaLinux](https://thenewstack.io/almalinux-your-enterprise-linux-ticket-to-freedom/) 服务器上进行演示。

是时候开始了。

## 安装必要的软件包

我们要做的第一件事是登录到将作为我们服务器的机器，并使用以下命令安装所需的软件：

```
sudo dnf install nfs-utils -y
```

接下来，转到客户端，并使用以下命令安装相同的软件包：

```
sudo apt-get install nfs-common -y
```

请注意服务器和客户端的软件包名称不同。确保在正确的操作系统上安装正确的软件。

## 创建 NFS 共享

接下来，我们可以创建 NFS 共享。回到服务器，我们将使用以下命令在根目录下创建一个名为 nfs-share 的目录：

```
sudo mkdir nfs-share
```

使用以下命令更改目录的权限：

```
sudo chmod -R 777 /nfs-share
```

## 定义新的共享

现在，我们必须在 */etc/exports* 文件中定义新的共享。在服务器上，使用以下命令打开该文件进行编辑：

```
sudo nano /etc/exports
```

每个条目的格式为：

*目录 client_IP (权限)*

假设您有以下详细信息：

* 目录 – /nfs-share
* client_IP – 192.168.1.79
* 权限 – 读/写

以上信息的条目将是：

**/nfs_share 192.168.1.79(rw)**

保存并关闭文件。

## 启动 NFS 服务器并打开防火墙

在服务器上，让我们打开防火墙，以便我们的客户端可以访问共享。这可以通过以下两个命令完成：

```
sudo firewall-cmd --permanent --zone=public --add-service=nfs
sudo firewall-cmd --reload
```

现在是时候启动和启用 NFS 服务了，这可以通过一个命令完成：

```
sudo systemctl enable --now nfs-server
```

您可以使用以下命令验证服务器是否正在运行：

```
systemctl status nfs-server
```

## 添加一些测试文件并创建一个客户端目录

回到服务器，让我们使用以下命令添加一些测试文件：

```
touch /nfs-share/{test1,test2,test3}
```

在客户端机器上，创建一个目录，作为共享的挂载点，使用以下命令：

```
mkdir ~/nfs_mount
```

您可以将该目录放在您喜欢的任何位置（只要您的用户有权访问它）。

## 挂载共享

假设我们的 NFS 服务器的 IP 地址是 192.168.1.210。在客户端机器上，使用以下命令挂载共享：

```
sudo mount 192.168.1.210:/nfs-share ~/nfs_mount
```

现在，服务器上的 NFS 共享目录应该已经挂载到客户端上的 NFS 挂载目录。如果您查看客户端上 *nfs_mount* 文件夹的内容，您应该会看到它包含文件 test1、test2 和 test3（您在服务器上创建的）。

如果您想更容易地挂载 NFS 共享，我们可以向 [fstab](https://wiki.archlinux.org/title/Fstab) 添加一个条目。在客户端机器上打开文件进行编辑，使用以下命令：

```
sudo nano /etc/fstab
```

在文件的底部，添加以下内容（修改它以匹配您的配置）：

*192.168.1.210:/nfs-share /home/USER/nfs-mount nfs rw 0 0*

请注意，您不能在 fstab 中使用 ~/ 来指示您的主目录。而是使用挂载目录的完整路径。

使用以下命令测试配置：

```
mount -a
```
如果您没有收到任何错误，那么您就可以开始了。您可以通过重新启动客户端机器来验证它是否有效。NFS 共享应该会自动挂载。

这就是在 Linux 上设置基本 NFS 共享的全部内容。如果您需要比 Samba 更快的复制和写入速度，那么 NFS 是一个不错的选择。请记住，NFS 不如 Samba 灵活，因此您无法与 Active Directory 集成或共享打印机。此外，NFS 也没有文件管理器集成，因此任何时候您想要配置新的共享或连接到现有的共享，都只能使用命令行。
