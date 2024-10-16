# Linux：使用 Syncthing 在服务器之间同步文件

![Linux：使用 Syncthing 在服务器之间同步文件的功能图像](https://cdn.thenewstack.io/media/2024/09/61d124c1-syncthing-1024x683.png)

您是否想过在 Linux 机器之间保持文件和/或文件夹同步？您可以使用 [Samba](https://thenewstack.io/samba-network-shares-for-rhel-based-linux-distributions/) 或 [NFS](https://thenewstack.io/linux-create-and-connect-to-an-nfs-share/) 来实现，但这些解决方案并非专门针对同步而设计。使用 Syncthing，您不仅可以设置加密同步选项，还可以在计算机、移动设备和服务器之间进行同步。最重要的是，Syncthing 比其他两个选项更容易设置和使用。当您需要保持机器之间的数据处于持续同步状态时，这就是您要走的路。

我将逐步引导您完成在 [AlmaLinux](https://thenewstack.io/almalinux-your-enterprise-linux-ticket-to-freedom/) 和 [Ubuntu Linux](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) 上安装 [Syncthing](https://syncthing.net/) 的过程，以便您可以看到在两者之间同步文件是多么容易。

## 您需要什么

您只需要运行 AlmaLinux 和 Ubuntu Linux 实例以及一个具有 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) 的用户。当然，您可以使用两个 AlmaLinux 实例、两个 Ubuntu 实例或两个完全不同的发行版。

准备好这些东西后，让我们安装 Syncthing。

## 安装 Syncthing

在 AlmaLinux 上安装 Syncthing 需要下载一个文件，解压缩它，然后将一个文件移动到新创建的目录中。以下是实际步骤：

- 登录到您的 AlmaLinux 机器。
- 使用以下命令下载最新版本的 Syncthing：

  ```bash
  curl -s https://api.github.com/repos/syncthing/syncthing/releases/latest | grep browser_download_url | grep linux-amd64 | cut -d '"' -f 4 | wget -qi -
  ```

- 使用以下命令解压缩文件：

  ```bash
  tar xvzf syncthing*tar.gz
  ```

- 使用以下命令移动所需文件：

  ```bash
  sudo mv syncthing-linux*/syncthing /usr/bin
  ```

- 使用以下命令验证安装：

  ```bash
  syncthing --version
  ```

Ubuntu 的安装甚至更容易。只需按照以下步骤操作：

- 打开终端窗口。
- 发出命令：

  ```bash
  sudo apt-get install syncthing -y
  ```

- 等待安装完成。

## 创建 Systemd 文件

要在 [启用 systemd 的发行版](https://thenewstack.io/systemds-lennart-poettering-wants-to-bring-linux-home-directories-into-the-21st-century/) 上将 Syncthing 作为服务运行，您必须使用以下命令创建一个 systemd 文件：

```bash
sudo nano /etc/systemd/system/syncthing@.service
```

注意 `@` 符号？它在那里，因此您可以以用户身份启动 Syncthing。
在该文件中，粘贴以下内容：

```
[Unit]
Description=Syncthing - Open Source Continuous File Synchronization for %I
Documentation=man:syncthing(1)
After=network.target

[Service]
User=%i
ExecStart=/usr/bin/syncthing -no-browser -gui-address=0.0.0.0:8384 -no-restart -logflags=0
Restart=on-failure
SuccessExitStatus=3 4
RestartForceExitStatus=3 4
# Hardening
ProtectSystem=full
PrivateTmp=true
SystemCallArchitectures=native
MemoryDenyWriteExecute=true
NoNewPrivileges=true

[Install]
WantedBy=multi-user.target
```

保存并关闭文件。
使用以下命令重新加载 systemd 守护程序：

```bash
sudo systemctl daemon-reload
```

假设您想以用户“jack”身份运行 Syncthing。启动和启用该服务的命令是：

```bash
sudo systemctl enable --now syncthing@jack
```

在 AlmaLinux 和 Ubuntu 上执行相同的操作。

## 允许 Syncthing 通过防火墙

由于我们使用的是两个不同的发行版，因此您需要使用两种不同的防火墙工具。在 AlmaLinux 上，我们将使用以下命令打开防火墙端口：

```bash
sudo firewall-cmd --zone=public --add-service=syncthing --permanent
sudo firewall-cmd --zone=public --add-service=syncthing-gui --permanent
sudo firewall-cmd --reload
```

对于 Ubuntu，可以使用以下命令打开防火墙：

```bash
sudo ufw allow syncthing
sudo ufw allow syncthing-gui
```

## 配置 Syncthing

使用以下命令打开 Syncthing 配置文件：

```bash
sudo nano ~/.local/state/syncthing/config.xml
```

在该文件中，找到以下部分：
将 `tls="false"` 
更改为 `tls="true"`
并确保地址部分配置为托管机器的 IP 地址。完成后，保存并关闭文件。

使用以下命令重新启动 Syncthing 服务：

```bash
sudo systemctl restart syncthing@jack
```

## 访问 Syncthing Web UI

打开 Web 浏览器并将其指向 `http://SERVER:8384`（其中 SERVER 是托管机器的 IP 地址。在主页面上，您将收到警告，指出您需要设置远程访问密码。单击“设置”（图 1）来执行此操作。在“设置”弹出窗口中，单击“GUI”选项卡，然后设置用户名和密码。

- 图 1：Syncthing 设置按钮（右下角）。
当你完成时点击保存。这将把你带到登录页面，你需要输入你刚刚设置的用户名和密码。

## 连接机器

现在，你已经在两台机器上启动并运行了 Syncthing，现在是时候连接它们了。在一台机器上，进入 Syncthing 仪表盘，点击“操作”，然后点击“显示 ID”。你会看到一个二维码和一长串随机字符串。复制该字符串，然后移动到另一台机器。在第二台机器上，在“远程设备”部分，点击“添加设备”。在“设备 ID”部分，粘贴第一台机器的 ID，给设备起一个名字，然后点击“保存”。

进入“共享”选项卡，在“未共享文件夹”部分，勾选“默认文件夹”选项，然后勾选“自动接受”选项（图 2）。

*图 2：向 Syncthing 添加第二个节点。*

点击“保存”，然后刷新仪表盘。连接的机器现在应该被列为“最新”。

确保你对两台机器都执行了这个过程。

Syncthing 的默认文件夹是 `~/Sync`。你在其中一台机器上添加到该文件夹的任何文件或文件夹都将自动与另一台机器同步。你可以通过在一台机器上发出以下命令来测试：

```
touch ~/Sync/testing
```

如果你检查第二台机器，你会发现 testing 文件已经同步。

这就是在 Syncthing 的帮助下同步机器的全部内容。

---

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)