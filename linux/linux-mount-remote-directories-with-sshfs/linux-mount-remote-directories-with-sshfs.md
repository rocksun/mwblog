
<!--
title: Linux：使用SSHFS挂载远程目录
cover: https://cdn.thenewstack.io/media/2024/07/62ac5402-island-2482200_1280.jpg
-->

SSHFS 使用安全加密将远程目录挂载到本地机器，连接比标准 FTP 安全得多。

> 译自 [Linux: Mount Remote Directories With SSHFS](https://thenewstack.io/linux-mount-remote-directories-with-sshfs/)，作者 Jack Wallen。

Secure Shell([SSH](https://thenewstack.io/linux-limit-concurrent-users-on-your-server-with-ssh/)) 不仅仅是让你远程登录服务器来处理管理任务。借助这个安全的网络协议，你还可以借助 SSH 文件系统 (SSHF) 挂载远程目录。

SSHFS 使用 SFTP（SSH 文件传输协议）通过安全的加密将远程目录挂载到本地机器，这意味着连接比你的 [标准 FTP](https://thenewstack.io/create-a-secure-ftp-server-with-linux-and-ssh/) 安全得多。此外，一旦远程目录被挂载，它就可以像本地机器上的目录一样使用。

可以将 SSHFS 视为一种更安全的方式来创建网络共享，唯一的区别是，你需要在任何需要连接到共享的机器上安装 SSHFS（而使用 Samba，你只需要在托管共享的机器上安装它）。

让我们一起了解如何设置 SSHFS 并运行它，这样你就可以安全地将远程目录挂载到你的本地机器。

## 你需要什么

要使此方法生效，你需要至少两台 Linux 机器。这些机器可以是 [Ubuntu](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) 或 [基于 Fedora 的](https://thenewstack.io/set-up-python-on-fedora-linux-4-steps/)，因为 SSHFS 在大多数 Linux 发行版的标准存储库中都可以找到。你还需要一个具有 sudo 权限的用户。

## 安装 SSHFS

由于 [SSHFS](https://man7.org/linux/man-pages/man1/sshfs.1.html) 在标准存储库中可以找到，因此安装非常简单。登录到服务器（将托管要共享的目录）并使用以下命令之一安装 SSHFS：

- 基于 Ubuntu 的发行版 - `sudo apt-get install sshfs -y`
- 基于 Fedora 的发行版 - `sudo dnf install fuse-sshfs -y`
- 基于 Arch 的发行版 - `sudo pacman -S sshfs`
- 基于 openSUSE 的发行版 - `sudo zypper -n in sshfs`

接下来，登录到你的本地机器并安装该软件包。

安装完成后，你需要在本地机器上的 SSHFS 配置文件中设置 **user_allow_other**。为此，使用以下命令打开该文件：

```
sudo nano /etc/fuse.conf
```
在该文件中，找到以下行：

```
#user_allow_other
```
将其更改为：

```
user_allow_other
```
保存并关闭该文件。

## 创建用于挂载的目录

回到服务器，我们必须创建一个将在客户端机器上挂载的目录。我们将使用以下命令将新目录放在 /srv 中：

```
sudo mkdir /srv/data
```
创建新目录后，我们需要授予它所有权，以便用户或组可以访问它。如果你只有一个用户需要访问它，你可以使用以下命令更改所有权：

```
sudo chown -R USERNAME:USERNAME /srv/data
```
如果你想允许多个用户访问该目录，你需要先使用以下命令创建一个组：

```
sudo groupadd GROUP
```
其中 **GROUP** 是新组的名称。

接下来，使用以下命令将必要的用户添加到该组（一次添加一个）：

```
sudo usermod -aG GROUP USERNAME
```
其中 GROUP 是组的名称，USERNAME 是要添加的用户的名称。

然后，你需要使用以下命令将新目录的所有权更改为新组：

```
sudo chown -R USERNAME:GROUP /srv/data
```

在本地机器上，你需要创建一个目录来存放挂载的远程目录。我们将使用以下命令在用户的 home 目录中创建它：

```
mkdir ~/data_mount
```

## 挂载目录

现在是时候挂载我们的远程目录了。请记住，我们将远程目录 */srv/data* 挂载到本地目录 *~/data_mount*。这可以通过以下命令完成：

```
sshfs USER@SERVER:/srv/data ~/data_mount
```
其中 USER 是远程用户名，SERVER 是远程服务器的 IP 地址。系统会提示你输入远程用户的密码。身份验证成功后，远程目录将被挂载到本地目录，你可以像访问本地机器上的目录一样访问它。如果你在 *~/data_mount* 中保存或编辑文件，它将在远程机器上的 */srv/data* 中反映出来。

这种挂载方法是临时的。让我们将其永久化。

## 永久挂载远程驱动器

要永久挂载 SSHFS 驱动器，你需要在它生效之前进行一些操作。首先，你需要使用以下命令创建一个 SSH 密钥对（在本地机器上）：

```
ssh-keygen -t rsa
```
确保为密钥设置一个强/唯一的密码。

密钥生成后，使用以下命令将其复制到服务器：

```
ssh-copy-id USER@SERVER
```
其中 USER 是远程用户名，SERVER 是远程服务器的 IP 地址。

让我们测试一下连接，以确保它正常工作。从本地机器上，使用以下命令 SSH 到服务器：

```
ssh USER@SERVER
```
其中 USER 是远程用户名，SERVER 是远程服务器的 IP 地址。您应该会收到 SSH 密钥密码的提示，而不是您的用户密码。成功验证后，使用 exit 命令退出连接。

要使此挂载永久生效，您需要修改本地机器上的 `/etc/fstab` 文件。使用以下命令打开该文件进行编辑：

```
sudo nano /etc/fstab
```

在文件末尾粘贴以下行：

```
USER1@SERVER:/srv/data /home/USER1/data_mount fuse.sshfs x-systemd.automount,_netdev,user,idmap=user,transform_symlinks,identityfile=/home/USER2/.ssh/id_rsa,allow_other,default_permissions,uid=USER_ID_N,gid=USER_GID_N 0 0
```

其中 USER1 是远程用户名，SERVER 是服务器的 IP 地址，USER2 是本地机器上的用户名，USER_ID 和 GROUP_ID 是本地机器独有的。您可以使用以下命令找到 ID：

```
id
```

您应该会看到类似以下内容：

```
uid=1000(jack) gid=1000(jack)
```

在上面的示例中，用户 ID 为 1000，组 ID 也为 1000。

保存文件并使用以下命令测试挂载：

```
mount -a
```

如果您没有收到错误，则一切正常。

这里有一个需要注意的地方。在启动过程中，挂载会失败，因为它会在网络启动之前尝试挂载。因此，在本地机器重启后，您需要打开一个终端窗口并使用以下命令挂载 SSHFS 目录：

```
mount -a
```

完成此操作后，您就可以像使用本地目录一样使用远程目录了。