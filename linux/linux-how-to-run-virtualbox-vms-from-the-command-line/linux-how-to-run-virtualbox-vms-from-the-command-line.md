
<!--
title: Linux：如何从命令行运行VirtualBox虚拟机
cover: https://cdn.thenewstack.io/media/2024/11/74278f41-virtualbox.png
-->

Oracle的开源VirtualBox提供了一个可靠的GUI来管理虚拟机。但有时您可能更倾向于使用命令行。方法如下：

> 译自 [Linux: How to Run VirtualBox VMs from the Command Line](https://thenewstack.io/linux-how-to-run-virtualbox-vms-from-the-command-line/)，作者 Jack Wallen。

如果您开始使用VirtualBox虚拟机，您可能会发现该软件[非常易于使用](https://thenewstack.io/deploy-a-virtual-machine-with-oracles-open-source-virtualbox/)。使用[Oracle](https://developer.oracle.com/?utm_content=inline+mention)的[VirtualBox](https://www.virtualbox.org/)，您可以创建和部署您最喜欢的[Linux发行版](https://thenewstack.io/choosing-a-linux-distribution/)的虚拟机，用于测试或日常使用，包括Windows甚至macOS。

问题是：如果您创建了一个服务器操作系统的虚拟机实例，您可能不想让VirtualBox GUI一直运行，以便可以访问无头服务器。GUI不仅占用系统资源，而且也可能使一些不知情的人很容易走到您的桌面前并停止正在运行的服务器。

如果您遇到这种情况，您需要知道如何从[命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)运行这些虚拟机。

这不仅意味着您可以节省宝贵的CPU周期和RAM，还可以远程管理这些虚拟机。通过[SSH](https://thenewstack.io/linux-ssh-and-key-based-authentication/)连接到主机，启动、暂停、停止甚至删除您的虚拟机。

让我向您展示如何做到这一点。

## 您需要什么

要使此方法有效，您需要在Linux主机上安装并运行VirtualBox实例。您还需要一个具有sudo权限的用户。就是这样——让我们开始工作吧。

## 安装VirtualBox扩展包

您必须首先安装VirtualBox扩展包。使用扩展包，任何从命令行启动的虚拟机都将无法访问网络。如果没有可用的网络，这些虚拟机就没什么用了。

要安装VirtualBox扩展包，请执行以下操作：

- 下载[VirtualBox下载站点上的最新扩展包版本](https://www.virtualbox.org/wiki/Downloads)。
- 打开VirtualBox。
- 点击文件>工具>扩展管理器。
- 点击安装（图1）。
- 导航到您保存下载的扩展包文件的位置，该文件将以.vbox-extpack结尾。
- 点击打开。
- 输入您的[sudo密码](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/)。
- 点击确定。


![](https://cdn.thenewstack.io/media/2024/11/e4bfc2f0-vbcommand1.jpg)

*图1：如果扩展包已经安装，它将在此处列出。*

现在扩展包已安装（它应该列在管理器中），您可以开始从命令行使用您的虚拟机了。

## 列出您的虚拟机

要管理您的虚拟机，您必须知道它们的完整名称，这可以通过以下命令找到：

```bash
VBoxManage list vms
```

输出应该如下所示：

```
"KDE NEON" {02a76c48-cacf-4cfb-8ec2-97a84454d97f}
"Ubuntu Golang" {3384369f-82a5-467a-aaf8-b1f5d806f404}
"Ubuntu Server" {a647b5be-7736-453a-bae5-b30c40a15250}
"Ubuntu 22.04" {bac0764b-ee2d-4476-b5f9-8f315e27f55c}
"AlmaLinux 9.4 beta" {68294206-cdd5-4c2e-b807-f33c11f45751}
"Debian Server" {a20b1fe6-1b9c-4788-b8c2-076662b0869d}
"Ubuntu 24.04" {8e2b3b4d-8544-4c34-920a-4901d2b2362f}
"COSMIC2" {a4e0c8e8-139f-4f73-b0e6-7d82a039083c}
"Gentoo" {221e41f3-1923-4652-be7f-f939d757a54f}
"AlmaLinux Home Auto" {443a6a7f-28ce-4ece-b80b-00140523492a}
"Fedora 41" {90593cbc-58b5-460c-895b-b826bf705472}
"Zorin 17.2" {bdf99643-807f-41e0-9470-1e2f681c758e}
"Manjaro" {076bd311-9f69-4558-8834-38b7d80d7f75}
"Debian" {2ffe5b00-31c3-42f6-8f5f-f4e069af6f67}
"TrueNAS" {f7b591fa-3925-415a-94d1-859abd64e260}
"Ubuntu Desktop" {5c7cf691-7436-400b-b76c-6787643be324}
"Fedora KDE" {6978832e-d7c5-4a7f-8523-812f107a288c}
"CachyOS" {413ede52-a002-48e3-b100-c10ac0c8f65e}
```

这些是我添加到VirtualBox中的所有当前虚拟机。

假设您想启动虚拟机“Ubuntu Server”。为此，命令将是：

```bash
VBoxManage startvm "Ubuntu Server" --type headless
```

输出应该如下所示：

```
Waiting for VM "Ubuntu Server" to power on...
VM "Ubuntu Server" has been successfully started.
```

您可以通过发出以下命令来验证它是否正在运行：

```bash
VBoxManage list runningvms
```

输出应该如下所示：

```
"Ubuntu Server" {a647b5be-7736-453a-bae5-b30c40a15250}
```

然后，您可以像往常一样访问虚拟机（只要您记住服务器的IP地址）。
以下是一些您可以用来管理这些虚拟机的其他命令（我将继续使用Ubuntu Server虚拟机为例）：

- 暂停虚拟机：
`VBoxManage controlvm "Ubuntu Server" pause --type headless`
- 重新启动暂停的虚拟机：
`VBoxManage controlvm "Ubuntu Server" resume --type headless`
- 关闭正在运行的虚拟机：
`VBoxManage controlvm "Ubuntu Server" acpipowerbutton`

`VBoxManage controlvm "Ubuntu Server" poweroff --type headless`

- 删除虚拟机：
`VBoxManage unregistervpm "Ubuntu Server" --delete-all`

## 创建新的虚拟机

您也可以通过命令行创建虚拟机。此过程比管理现有虚拟机稍微复杂一些，您仍然需要使用 GUI（例如 RDP 客户端）来完成操作系统安装。在开始此过程之前，请确保已下载要安装的操作系统的 ISO 镜像。如果您胆子够大，以下是步骤（请根据您的情况修改）：

### 创建虚拟机

首先，使用以下命令创建虚拟机：

```bash
VBoxManage createvm --name Ubuntu_Server --ostype "Ubuntu_64" --register --basefolder "`pwd`"
```

### 配置内存和网卡

接下来，您需要使用以下三个命令配置内存和网卡：

```bash
VBoxManage modifyvm Ubuntu_Server --ioapic on
VBoxManage modifyvm Ubuntu_Server --memory 1024 --vram 128
VBoxManage modifyvm Ubuntu_Server --nic1 bridged
```

### 创建磁盘并连接 ISO 镜像

现在，我们将使用以下命令创建一个 80GB 的 SATA 硬盘和一个带有附加 Ubuntu ISO 的 CDROM（根据需要修改）：

```bash
VBoxManage createhd --filename "`pwd`"/Ubuntu_Server/Ubuntu_Server_DISK.vdi --size 80000 --format VDI
VBoxManage storagectl Ubuntu_Server --name "SATA Controller" --add sata --controller IntelAhci
VBoxManage storageattach Ubuntu_Server --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "`pwd`"/Ubuntu_Server/Ubuntu_Server_DISK.vdi
VBoxManage storagectl Ubuntu_Server --name "IDE Controller" --add ide --controller PIIX4
VBoxManage storageattach Ubuntu_Server --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium "`pwd`"/ISO
VBoxManage modifyvm Ubuntu_Server --boot1 dvd --boot2 disk --boot3 none --boot4 none
```

### 配置 RDP 访问

接下来，使用以下命令配置 RDP 访问，以便可以从网络访问：

```bash
VBoxManage modifyvm Ubuntu_Server --vrde on
VBoxManage modifyvm Ubuntu_Server --vrdemulticon on --vrdeport 10001
VBoxHeadless --startvm Ubuntu_Server
```

然后，您可以使用以下命令启动新的虚拟机：

```bash
VBoxManage startvm Ubuntu_Server --type headless
```

这将启动虚拟机，然后您可以通过 10001 端口上的 RDP 访问它，在那里您可以完成客户机的操作系统安装。

这就是从命令行管理 VirtualBox 虚拟机的所有内容。说实话，我更喜欢从 GUI 创建虚拟机，然后从命令行管理它们。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)