
<!--
title: Linux内核如何与硬件交互
cover: https://cdn.thenewstack.io/media/2024/04/3c893af6-ai-generated-8230770_1280.png
-->

Linux 提供了各种工具，用于报告和检查 CPU、RAM、存储和网络的操作。本文演示了其中许多实用程序的工作原理。

> 译自 [Linux: How the Kernel Interacts with Hardware](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)，作者 Damon M Garn。

这是达蒙·加恩关于了解 Linux 操作环境所著的十部分系列的第三部分。另请参见“[Linux：了解 Linux 命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)”。

在理解计算机系统的结构时，不妨将其视为包含四个主要子系统。这些子系统相互关联并相互影响，但首先将它们视为独立的组件。

这四个子系统是：

- **中央处理器 (CPU)**：处理器负责运行代码。
- **随机存取存储器 (RAM)**：内存临时存储数据并允许快速检索。它与 CPU 密切相关。
- **存储**：固态和硬盘驱动器即使在系统关闭时也能存储数据。存储容量会影响系统性能和功能。
- **网络**：提供网络连接，允许交换文件或其他通信。

[Linux](https://thenewstack.io/Linux/) 提供了用于报告和检查这些组件的各种工具。本文演示了其中许多实用程序。

您需要一个功能齐全的 Linux 发行版才能按照以下命令和示例进行操作。您可以使用物理或虚拟计算机，任何发行版都应该可以工作。请注意，某些发行版包含与其他发行版不同的工具。大多数 Linux 发行版都包含此处描述的工具。

本文是涵盖各种系统管理员主题的更大系列 Linux 文章的一部分。您可以按照 [Linux：Linux 技能模块存储库的配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) 中找到的信息构建一个实验室环境。

## 显示 CPU 和内存信息

CPU 和内存上面描述为独立的子系统，但它们密切相关。本节介绍如何显示有关这两者的信息。

Linux 在引导过程中清点可用硬件。一些硬件信息存储在 [/proc](https://linux.die.net/sag/proc-fs.html) 目录中，该目录在每次系统启动时都会动态填充。此目录包含两个与处理器和内存相关的文件。

- /proc/cpuinfo：提供系统在启动过程中检测到的有关处理器的信息。
- /proc/meminfo：提供系统在启动过程中检测到的有关内存的信息。

使用 [cat](https://linux.die.net/man/1/cat) 命令显示此信息。cat 命令显示文件的内容，使其成为读取文件的便捷工具。/proc 目录还包含 PCI 总线数据、IO 端口等。

```
$ cat /proc/cpuinfo
```
![](https://cdn.thenewstack.io/media/2024/04/4c390696-cat-proc-cpuinfo.png)

*通过 cat /proc/cpuinfo 指令输出。*

输出显示了两个 CPU 内核（0 和 1），以及功能和架构信息。此屏幕截图来自虚拟机，不显示处理器型号或规格。

meminfo 文件显示了总内存以及如何使用该内存。

```
$ cat /proc/meminfo
```

![](https://cdn.thenewstack.io/media/2024/04/7e6c776a-cat-meminfo.png)

*cat /proc/meminfo 命令的部分输出。*

为什么这些信息很重要？也许系统对您来说是新的，您不知道其当前规格是什么。或者您正在考虑升级并希望查看现有硬件。

您还可以使用 [lscpu](https://linux.die.net/man/1/lscpu) 命令显示来自 /proc/cpuinfo 的信息。

一个常见的升级是内存。通过添加 RAM，相对容易提高某些系统的性能。/proc/meminfo 显示已安装内存的数量和类型。

### 内存工具

用于内存利用率的两个标准信息收集工具是 [free](https://linux.die.net/man/1/free) 和 [vmstat](https://linux.die.net/man/8/vmstat)。这些工具提供了有关系统识别了多少内存以及如何使用它的基本信息。

free 命令显示系统上当前未使用的 RAM，因此可用于其他应用程序或服务。

![](https://cdn.thenewstack.io/media/2024/04/6711ac89-free.png)

*free 命令显示内存总计和利用信息。*

使用 -h 选项以更用户友好的格式显示结果。

vmstat 命令指示虚拟内存利用率。回想一下，RAM 和存储设备都存储信息。如果系统没有足够的 RAM 来存储所需数据，它可以从磁盘借用存储空间。磁盘提供了额外的“虚拟内存”。但是，此解决方案可能会极大地减慢系统速度，如果可能，应避免使用。最好添加更多内存或减少系统工作负载。使用虚拟内存也称为交换。

![](https://cdn.thenewstack.io/media/2024/04/b5dc1bf3-vmstat-megs.png)

*vmstat 命令显示的是虚拟内存使用情况。
*
使用 -S M 以兆字节显示结果。

### 使用 uname 命令

显示基本 CPU 信息的快速命令是 [uname](https://linux.die.net/man/1/uname)。它有几个选项可以修改其输出。使用 `-a` 选项显示所有处理器和操作系统详细信息。

![](https://cdn.thenewstack.io/media/2024/04/5da22413-uname.png)

uname 命令提供的信息不多，但它显示的信息很有用。信息包括 Linux 内核版本、硬件架构、处理器类型和操作系统名称。

## 显示存储信息

硬盘驱动器 (HDD) 或固态驱动器 (SSD) 通常提供计算机存储。这些设备支持长期文件存储。查看系统上的存储信息可以让你预测容量问题并可能提高性能。

大多数人认为容量是存储的主要属性。如今的存储磁盘往往非常大，通常大于最终用户需要。在大多数业务环境中，数据应存储在网络服务器上。但是，值得检查存储容量以确保系统有足够的空间使用，尤其是对于服务器而言。

存储磁盘会影响系统性能。系统、服务和用户文件存储在驱动器上。读取和写入这些文件所需的时间越长，系统就会变得越慢。

### 了解分区

存储磁盘被划分为分区。分区是通常分配给特定类型数据的逻辑存储单元。

使用与上面用于 CPU 和内存数据的相同 `cat` 命令显示分区信息。参数是 `/proc/partitions`。

```
$ cat /proc/partitions
```

![](https://cdn.thenewstack.io/media/2024/04/c47a04fb-cat-proc-partitions.png)

*请注意屏幕截图中的 sda 详细信息。*

第一个存储磁盘通常命名为 `sda`，第二个命名为 `sdb`，依此类推。磁盘上的每个分区都按从 1 开始的顺序进行编号。因此，第二个存储磁盘上的第三个分区是 `sdb3`。

`/proc` 目录还包含有关 SCSI 磁盘 (`/proc/scsi/scsi`) 和块设备 (`/proc/diskstats`) 的信息。

你可以使用 [lsblk](https://linux.die.net/man/8/lsblk) 命令显示类似的信息。你可以将该命令指向特定存储磁盘，例如 `/dev/sda`。

```
$ lsblk /dev/sda
```

![](https://cdn.thenewstack.io/media/2024/04/a8059866-lsblk-sda.png)

*lsblk命令报告了存储磁盘sda的信息，显示了两个分区。*

lsblk 命令使用分层树结构显示磁盘、分区和逻辑卷，以便于解释。

### 显示容量信息

`/proc/partitions` 文件和 lsblk 输出显示存储结构，但你通常使用 [df](https://linux.die.net/man/1/df) 和 [du](https://linux.die.net/man/1/du) 命令来了解有关容量和利用率的更多信息。

磁盘利用率 (`du`) 命令对于了解特定目录或文件占用多少空间非常有用。例如，如果你有一个装满图片的文件夹，你可以使用 du 命令来确定文件夹使用了多少存储驱动器。du 命令通过添加所有选定目录和文件的大小来估算此消耗。

你几乎总是使用 `-h` 选项以人类可读的格式（例如 KB、MB、GB 等）显示大小。

尝试使用 du 检查日志文件在 Linux 设备上消耗了多少容量。Linux 将日志文件存储在 `/var/log` 目录中。

```
$ du -h /var/log
```

![](https://cdn.thenewstack.io/media/2024/04/eab18749-du-h-var-log.png)

*du 命令显示每个目录和每个文件的磁盘使用情况。*

`-s` 选项提供利用率摘要，而不列出所有文件。这对于内容较多的目录很有用。

![](https://cdn.thenewstack.io/media/2024/04/2d15283f-du-hs-var-log-summary.png)

*搭配 du 命令使用 -s 选项可以显示存储信息摘要。*

df 实用程序通过显示可用和已用空间的总量来显示整体驱动器容量消耗。例如，如果你的系统有一个带有分区的硬盘驱动器，df 将显示该驱动器有多少可用空间用于更多文件和程序，以及有多少空间已被占用。

df 命令还受益于 `-h` 选项，使其输出更易于用户使用。

```
$ df -h /dev/sda
```

![](https://cdn.thenewstack.io/media/2024/04/130149eb-df-h-sda.png)

## 显示网络信息

网络连接对于大多数 Linux 设备至关重要。有线和无线网络接口卡 (NIC) 将系统连接到其他网络节点，从而实现电子邮件、网络浏览、打印、文件共享等功能。

最常见的网络信息收集和故障排除工具之一是 [ip](https://linux.die.net/man/8/ip) 命令。此命令包含许多修改其功能的子命令。例如，使用 `ip addr` 命令显示基本网络设置：

```
$ ip addr show enp0s5
```

![](https://cdn.thenewstack.io/media/2024/04/fca39281-ipaddr-show-eth.png)

*ip addr 命令的部分输出，显示 enp0s5 接口的信息。*

上面显示的 `ip addr` 命令显示接口名称 (`enp0s5`)、基本传输信息 (`mtu 1500`) 和状态 (`UP`)。它还显示接口的媒体访问控制 (MAC) 硬件地址 (`00:1c:42:c2:62:1c`) 和 IPv4 逻辑地址 (`10.211.55.4/24`)。状态和 IP 地址对于故障排除尤为重要。

ip 命令的较旧版本是 [ifconfig](https://linux.die.net/man/8/ifconfig)。某些 Linux 发行版可能仍识别该命令，但您应该学习 ip 命令。

### 使用 ethtool 实用程序

基本 [ethtool](https://linux.die.net/man/8/ethtool) 命令显示指定网卡（enp0s5）的当前硬件设置。

```
$ ethtool enp0s5
```

![](https://cdn.thenewstack.io/media/2024/04/894d8324-ethtool.png)

*ethtool命令显示网络接口卡信息。*

添加 `-i` 选项以显示设备驱动程序信息。

```
$ ethtool -i enp0s5
```

![](https://cdn.thenewstack.io/media/2024/04/9473fab8-ethtool-i.png)

*ethtool -i 命令显示网卡设备驱动程序的详细信息。*

通常最好使用最新的驱动程序。

ethtool 的一个实用用途是让物理网卡的指示灯闪烁一段时间。此功能有助于识别具有多个接口的 Linux 设备上的网卡。

```
$ ethtool --identify enp0s5 5
```

上述示例使指示灯闪烁五秒钟。

## 使用监控工具

上述工具显示有关各个系统组件的特定信息。但是，top、htop 和 Glances 等工具提供了更广泛的硬件视图。本部分中的实用程序以实时方式显示性能信息，并帮助您分析硬件的使用情况。

### 使用 top 工具

标准的 Linux 硬件监控工具是 [top](https://linux.die.net/man/1/top)。它在上方框中显示基本的硬件信息，在下方部分中显示系统进程及其 CPU 和内存消耗的动态表。

![](https://cdn.thenewstack.io/media/2024/04/08f4d1f8-top-hwinfo.png)

*top 命令的上半部分显示了硬件详细信息和使用情况，例如空闲内存和处理器时间。*

![](https://cdn.thenewstack.io/media/2024/04/853b3ac8-top-monitor.png)

*硬件摘要下方部分显示了运行中的进程及其 CPU 和内存消耗（部分屏幕截图）。*

使用 **P** 和 **M** 键对主要的 CPU 和内存消耗者进行排序。当您检查完 top 的结果后，按 **q** 键退出。

### 使用 htop 工具

更动态的利用率工具是 [htop](https://linux.die.net/man/1/htop)。并非所有 Linux 发行版都默认安装它，因此您可能需要将其添加到您的系统中。htop 工具是一个实时监控器，具有更强大的仪表板，包括颜色编码和动态元素。这更像是一个监控工具，而不是一种收集系统硬件信息的方式，但它提供了有关硬件行为方式以及系统是否有足够资源来处理其工作负载的见解。

### 使用 Glances 工具

[Glances](https://nicolargo.github.io/glances/) 硬件监控器并未默认安装在所有 Linux 发行版上，但将其添加到系统中非常容易。Glances 使用易于阅读的仪表板提供系统资源的实时监控。对于拥有多个系统的 Linux 用户来说，Glances 非常棒，因为它包括一个网络模式，允许远程连接以监控多个设备。

Glances 是开源的，并用 Python 编写，因此可以在 Linux、macOS 和 Windows 系统上运行，这使其成为更令人信服的信息收集工具。

## 总结

回想一下，计算机系统由多个子系统组成。其中包括处理能力、存储和网络。系统管理包括显示硬件信息并使用它来管理服务、进程、应用程序等。

Linux 用户将希望看到硬件信息，以帮助选择系统升级、监控性能和解决问题。许多资源（如 /proc/cpuinfo 和 /proc/meminfo）提供静态信息。其他资源（如 top 和 Glances）提供实时处理器、内存、存储和网络硬件资源的动态视图。您经常会发现自己使用多个工具来确保您了解系统规范。
