几十年来，我一直使用 VirtualBox 来满足我的所有[虚拟机](https://thenewstack.io/linux-how-to-run-virtualbox-vms-from-the-command-line/) (VM) 需求。我可以将其用作图形用户界面 (GUI)，也可以从命令行运行它。它易于使用，跨平台，并且很少给我带来任何问题。

直到它不再是这样。

在过去的几年里，我记不清有多少次我遇到 VirtualBox 安装损坏，需要我完全删除软件并重新安装。一般来说，这很麻烦，但解决方案有效。

直到它不再是这样。

几周前，VirtualBox 又坏了。我尝试了惯用的技巧，但无法使其正常工作。我删除了冲突的内核模块（这通常是问题所在），进行了彻底卸载、重启、升级……你能想到的，我都做了。然而，这次修复不起作用了。

问题是，我每天都依赖虚拟机。如果没有启动虚拟机的能力，我就无法评审 Linux 发行版、测试软件和执行其他几项任务。

因此，我永久删除了 VirtualBox，并发誓再也不使用它。

解决方案是通过 [KVM](https://thenewstack.io/amazon-web-services-open-sources-a-kvm-based-fuzzing-framework/) 实现的，它是一个基于 [Linux](https://thenewstack.io/introduction-to-linux-operating-system/) 内核的虚拟机。KVM 是一种开源虚拟化技术，允许 Linux 内核充当管理程序，以提供接近原生性能和可靠性。

自从采用 KVM 以来，我的虚拟机没有出现过任何问题。但是，我不会单独使用 KVM。相反，我将其与 [Virt-Manager](https://virt-manager.org/) 搭配使用，以使虚拟机的使用变得极其简单。

如何安装和使用 KVM/Virt-Manager？

让我来告诉你。

## 你需要什么

你只需要一台正在运行的 Linux 实例、一个具有 sudo 权限的用户以及任何 Linux 发行版的 ISO 镜像。

让我们开始工作吧。

## 安装 Virt-Manager

首先，你无需安装 KVM，因为它已内置于 Linux 内核中。话虽如此，你确实需要安装 GUI 前端 Virt-Manager，方法如下：

*   在基于 Ubuntu/Debian 的机器上： *sudo apt-get install virt-manager -y*
*   在基于 Fedora 的机器上： *sudo dnf install virt-manager -y*
*   在基于 Arch 的机器上： *sudo pacman -S virt-manager*
*   在基于 openSUSE 的机器上： *sudo zypper install virt-manager*

安装 Virt-Manager 后，你就可以创建你的第一个虚拟机了。

## 使用 KVM/Virt-Manager 创建虚拟机

你会在桌面菜单中找到一个名为“Virtual Machine Manager”的新条目。点击它来运行应用程序。当它出现时，你会看到一个小的独立窗口（图 1）。

![](https://cdn.thenewstack.io/media/2026/01/17838a53-virtman1.jpg)

图 1：我的默认泡泡糖粉色主题中的 Virt-Manager 主窗口。

点击最左侧的图标（看起来像一个显示器）来创建一个新的虚拟机。在弹出的窗口中（图 2），确保选中“本地安装介质”并点击“前进”。

![](https://cdn.thenewstack.io/media/2026/01/006d7fc3-virtman2.jpg)

图 2：本地安装介质应默认选中。

在下一个屏幕中（图 3），点击“浏览”，然后使用你的默认文件选择器找到并选择你想要使用的 ISO 镜像。

![](https://cdn.thenewstack.io/media/2026/01/2d4b9868-virtman3.jpg)

图 3：如果你已经创建了一个虚拟机，你发行版的 ISO 镜像将出现在下拉列表中。

Virt-Manager 很可能不会自动检测操作系统，因此输入“gen”，然后选择“Generic Linux 2024”。点击“前进”继续。

你现在可以为操作系统分配所需的任意数量的 RAM 和 CPU 内核（图 4）。

![](https://cdn.thenewstack.io/media/2026/01/ce6fb992-virtman4.jpg)

图 4：除非操作系统需要更多 RAM，我通常保持原样。

下一个窗口（图 5）是事情开始变得有点复杂的地方。别担心，一旦你了解了正在发生的事情，你就会没事的。

![](https://cdn.thenewstack.io/media/2026/01/c97bd37e-virtman5.jpg)

图 5：确保明智地使用你的存储空间。

默认情况下，Virt-Manager 会将你的虚拟机存储在与操作系统相同的驱动器上。因为我创建了大量的虚拟机，所以我更喜欢将它们存储在外部驱动器上，以避免空间不足。如果你不担心这个问题，请勾选“为虚拟机创建磁盘镜像”并分配你想要的存储空间。

选择“选择或创建自定义”，然后点击“管理”。

现在是时候创建一个新的存储池，然后创建一个卷来存放虚拟机了。在“定位或创建存储卷”窗口中（图 6），点击窗口左下角的 +。为新池命名，将“目标路径”更改为外部驱动器上的目录（如果需要），然后点击“完成”。

![](https://cdn.thenewstack.io/media/2026/01/b0273c3d-virtman6.jpg)

图 6：你必须先创建存储池，然后才能创建卷。

创建池后，点击“卷”右侧的 +。在弹出的窗口中（图 7），为新卷命名（可能与发行版同名），分配你想要为虚拟机提供的空间，然后点击“完成”。

![](https://cdn.thenewstack.io/media/2026/01/bcb44692-virtman7.jpg)

图 7：你快完成了。

确保你的新卷被选中（它将以 qcow2 结尾），然后点击“选择卷”。

回到“新建虚拟机”窗口，点击“前进”。在下一个窗口中，为虚拟机命名，然后勾选“安装前自定义配置”。

点击“完成”，自定义配置窗口将打开（图 8）。

![](https://cdn.thenewstack.io/media/2026/01/fc28b8e2-virtman8.jpg)

图 8：这里有很多可以自定义的地方。

对于我的 KDE Neon 安装，我必须从“固件”下拉列表中选择 UEFI。完成此操作后，我点击“应用”，然后点击“开始安装”。

此时，将打开一个新窗口，你可以在其中开始操作系统安装过程。

这就是你如何安装 Virt-Manager 并将其与 KVM 结合使用，以创建可靠、接近原生性能的虚拟机。