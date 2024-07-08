# 如何管理 Linux 存储

![关于如何管理 Linux 存储的特色图片](https://cdn.thenewstack.io/media/2024/07/138ac0f8-getty-images-acyelgjsmjs-unsplash-1024x675.jpg)

[Linux: Linux 技能模块库的配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/) 文章。在本系列中，我们还介绍了
[如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/)，Linux 内核如何
[与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/) 以及如何
[Linux 管理系统服务](https://thenewstack.io/linux-skills-manage-system-services/) 和
[权限](https://thenewstack.io/linux-user-and-group-management/)。

最常见的 [Linux 系统管理员任务](https://www.thenewstack.io/Linux) 之一是管理存储空间。存储驱动器包含各种信息：用户数据、日志文件、临时文件、更新等等。许多最终用户没有意识到存储空间在当今的计算机系统中仍然是一种有限的资源，他们经常用冗余、无用和非业务文件填满容量。

管理员将固态硬盘或硬盘驱动器添加到 Linux 系统以增加容量。但是，存储空间必须在使用之前被组织成分区并使用文件系统进行结构化。

本文演示了如何添加和识别存储空间，包括分区和安装文件系统。它还展示了调查驱动器空间利用率所需的命令。您可以使用这些命令而无需任何额外的设置，但您可能会发现查看 [了解 Linux 命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/) 文章很有用。您需要将存储磁盘添加到您的实验室计算机或虚拟机以练习添加存储。

在包含实际数据的系统上使用以下命令时要非常小心。操作分区和文件系统的工具很容易导致数据丢失，因此始终从备份开始。使用不包含任何真实用户或业务文件的实验室计算机更好。如果您想构建一个实验室环境来练习这些命令，请参考本 [教程](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)。

注意：以 root（管理员）用户身份登录 Linux 系统是一种糟糕的安全做法。大多数系统会强制您以普通用户身份登录，然后使用 [sudo](https://linux.die.net/man/8/sudo)（超级用户执行）命令来提升您的权限。使用 sudo 时，系统可能会提示您输入密码。

## 识别存储设备

假设用户已消耗了其 Linux 系统存储驱动器上的所有空间，或者服务器的存储磁盘已满。虽然教用户有效地管理空间很有帮助，但通常情况下，消耗驱动器的数据是合法且必要的。这意味着您需要添加更多存储空间。

假设您已在计算机中物理安装了额外的固态硬盘或硬盘驱动器。您的下一个任务是识别它，以便您可以添加一个或多个分区。

### 驱动器识别

Linux 通过将存储磁盘表示为 /dev 目录中的文件来简化识别。每个磁盘都由一系列字母标识。

- sd = 存储磁盘
- a 或 b = 第一个或第二个磁盘（它也计算 c、d 等）
- 1 或 2 = 磁盘上的分区（它也计算更高的数字）

结果是 /dev/sdb1 是存储设备 (sd)，第二个设备 (b)，第一个分区 (1)，或者第二个存储设备上的第一个分区。

重要的是要理解，Linux 中的存储磁盘 a、b、c 等与 Windows 中的 C: 或 D: 磁盘没有关系。这两个操作系统不以相同的方式表示其存储容量。

使用 ls 命令显示 /dev/disk 目录的内容。在 Ubuntu 中，您可以按 id、按路径等查看存储设备。您应该至少看到一个名为 sda 的条目。那是系统中的第一个存储磁盘。当您添加第二个磁盘时，它将被标记为 sdb。其他标识符包括磁盘的通用唯一标识符 (UUID)。

![](https://cdn.thenewstack.io/media/2024/06/c72e4173-ls-dev-disks-by-uuid.png)

但是，使用 lsblk 命令显示磁盘更容易。树状输出显示存储设备，包括 sda 和 sdb（假设安装了两个物理磁盘）。它还显示任何现有的分区。

![](https://cdn.thenewstack.io/media/2024/06/962afa3f-lsblk-dev-sda.png)

在您识别出新磁盘（可能是 sdb）后，下一步是在其上创建一个或多个分区以组织数据。管理员创建分区以将各种类型的数据存储在驱动器的不同部分。通常，您只需创建一个消耗整个驱动器的单个分区。
另一个显示分区信息的实用命令是 `cat /proc/partitions`。此输出显示系统当前识别的所有存储磁盘和分区。

![](https://cdn.thenewstack.io/media/2024/06/765fc44e-cat-proc-parts.png)

## 管理分区

Linux 使用两个主要工具来管理分区：`fdisk` 和 `parted`。它们共享许多基本功能（创建、删除和显示分区），但它们的高级用法差异很大。

### 使用 `fdisk` 管理分区

`fdisk` 实用程序多年来一直是系统设置的一部分。它的主要功能包括创建和删除分区。它还显示分区信息，帮助管理员了解和规划存储容量。

![](https://cdn.thenewstack.io/media/2024/06/ebc2e739-fdisk-l-dev-sda.png)

`fdisk` 是一个交互式程序。通过键入 `fdisk /dev/sda` 运行它，然后按 **m** 键显示菜单。以下是需要注意的常见菜单项：

命令：| 描述：|
------- | -------- |
n | 创建一个新分区 |
d | 删除现有分区 |
p | 打印当前分区表 |
w | 将更改写入（保存）分区表并退出 `fdisk` |
q | 退出 `fdisk` 而不将更改保存到分区表 |

![](https://cdn.thenewstack.io/media/2024/06/c92c9036-fdisk-menu.png)

`fdisk` 可以处理更多任务，但这些是主要任务。请注意，删除或更改分区会使现有数据难以或无法恢复。

当您选择创建新分区的选项（菜单中的 **n**）时，`fdisk` 会提示您完成其余的分区配置。您将设置分区大小，可以通过标识扇区或指定容量（例如 mebibyte 或 gibibyte）来显示和输入。

请注意，gibibytes 和 gigabytes 是略有不同的度量。Gibibytes 是 1024 的倍数的精确度量，而 gigabytes 基于十的幂。这些度量导致总计为 1024（gibibytes）与 1000（gigabytes）。

以下是使用 `fdisk` 创建分区的步骤：

- 通过指定要分区的驱动器来打开 `fdisk`。例如，要使用驱动器 `/dev/sdb`，请键入 `fdisk /dev/sdb`。
- 如果需要，将分区表设置为 GUID 分区表 (GPT) 或主引导记录 (MBR)。
- 选择 **n** 创建一个新分区。
- 输入一个分区号（对于 MBR 表为 1-4，对于 GPT 表为 1-128）。请注意，如果您选择创建 MBR 表，则最多可以定义三个主分区或一个扩展分区。这仅在 MBR 表中必要。
- 通过定义第一个可用扇区来设置大小。
- 设置剩余的大小。最简单的方法是从定义的第一个扇区开始添加一定量的空间。例如，要创建一个 50 gibibyte 的分区，将结束大小设置为 **+50G**。
- 输入 **p** 打印或显示分区，包括您的新分区。请注意，`fdisk` 尚未对磁盘进行更改。
- 如果您对新分区的设置感到满意，请使用 **w** 写入（保存）更改。这也会退出 `fdisk`。如果您不想保留更改，请返回并编辑设置或通过按 **q** 退出 `fdisk` 而不保存。

![](https://cdn.thenewstack.io/media/2024/06/3a10c7fc-fdisk-create-a.png)
![](https://cdn.thenewstack.io/media/2024/06/745e39fc-fdisk-create-print-b.png)
![](https://cdn.thenewstack.io/media/2024/06/34f0d351-fdisk-create-write-c.png)

保存分区信息并退出 `fdisk` 后，使用 `lsblk` 命令显示新的磁盘和分区。在某些系统上，您可能需要键入 `partprobe` 命令来更新分区信息。

![](https://cdn.thenewstack.io/media/2024/06/7a6b09ee-lsblk-dev-sdb.png)

### 使用 `parted` 管理分区

GNU `parted`（分区编辑器）实用程序与 `fdisk` 的作用类似，但它更强大，因为它允许管理员扩展或缩小分区。

像 `fdisk` 一样，`parted` 是一个交互式工具。进入程序后，键入 **help** 查看各种配置选项。

常见命令包括：

命令：| 描述：|
------- | -------- |
mklabel | 定义分区表类型，例如 GPT 或 MBR |
mkpart | 在选定的驱动器上创建一个新分区 |
print | 显示当前分区表 |
quit | 退出 `parted`，保存所有更改 |

![](https://cdn.thenewstack.io/media/2024/06/3237b8ac-parted-help.png)

一般分区配置步骤与 `fdisk` 的步骤相同。步骤如下：

- 通过键入 `parted /dev/sdb` 打开 `parted` 来编辑驱动器，例如 `/dev/sdb`。
- 如果需要，使用 **mklabel {type}** 创建一个新的分区表。您可以输入 **msdos** 用于主引导记录表，或输入 **gpt** 用于 GUID 分区表。您可能需要输入 **msdos**。
- 使用
**mkpart** 和所需的类型和大小。类型包括 primary 或 logical，如果您计划使用 ext4 文件系统。- Parted 会提示您输入第一个和最后一个 GiB，这是设置所需大小所必需的。您也可以使用空间百分比来设置大小。
- 使用 **print** 命令显示修改后的（但未保存的）表格。- 使用 **quit** 命令保存更改并退出 parted。
![](https://cdn.thenewstack.io/media/2024/06/4fe2714b-parted-print-parts.png)
请记住使用 lsblk 命令查看最终配置。如果新分区没有显示，请尝试使用 partprobe 命令。

Parted 非常灵活且功能强大。以上步骤只是创建新分区的最小命令。

如果您在 parted 中使用 resize 命令缩小包含数据的分区，请务必小心。您有丢失数据的风险。我强烈建议在调整分区大小之前进行备份。

## 安装文件系统
现在您已经将存储磁盘的容量划分为一个或多个分区，您必须添加一个文件系统来组织数据。Windows 通常依赖于单个文件系统 (NTFS)，但 Linux 支持多种文件系统选项。最常见的两个是 ext4 和 XFS。

使用 **mkfs** 命令在指定分区上安装文件系统。例如，要将 XFS 文件系统添加到 /dev/sdb1，请键入：

1 |
$ sudo mkfs.xfs /dev/sdb1 |
使用 ext4 文件系统的类似示例如下所示：
1 |
$ sudo mkfs.ext4 /dev/sdb1 |
![](https://cdn.thenewstack.io/media/2024/06/618faeee-mkfs-sdb1.png)
mkfs 命令有一些变体或选项，但它们不太常用。

存储空间现在已准备好供用户使用。剩下的唯一步骤是通过将其挂载到用户可以保存数据的目录来使容量可用。

## 创建挂载点
Linux 不会像 Windows 那样用驱动器号标记存储空间。相反，管理员将存储空间附加或“挂载”到目录。也许您正在使用的文件服务器存储空间不足，并且一个团队即将开始一个大型项目。在前面的步骤中，您添加了一个磁盘，对其进行了分区，并安装了一个文件系统。接下来，创建一个名为 projects 的目录并将新的存储空间挂载到那里，使容量可用。

首先，使用以下命令在文件系统的根目录下创建一个名为 projects 的目录：

1 |
$ sudo mkdir /projects |
![](https://cdn.thenewstack.io/media/2024/06/fc5285b6-mkdir-projects.png)
然后，使用 **mount** 命令附加存储空间：

1 |
$ sudo mount /dev/sdb1 /projects |
![](https://cdn.thenewstack.io/media/2024/06/1b351ca3-mount-projects-sdb.png)
mount 的语法是指定物理设备（在上面的示例中为 /dev/sdb1），然后指定应将其挂载到的目录（在上面的示例中为 /projects）。

使用 **df** 命令验证存储空间是否存在。

1 |
$ df -h /projects |
![](https://cdn.thenewstack.io/media/2024/06/a9e87c27-df-h-projects.png)
下面将详细介绍 df 命令。

不要忘记使用 Linux 权限来控制对该存储空间的访问。

### 关于 umount 的说明
可移动介质（如 DVD 和 USB 驱动器）也必须使用 **mount** 命令进行挂载。这些临时存储区域也必须使用 **umount** 命令进行分离。请注意命令的拼写；要卸载，请使用 **umount** 命令（不带 **n** 字符）。

## 检查存储利用率
以上工具提供了有关添加和配置存储空间的信息，但用于管理驱动器的两个最有用的调查工具是 du 和 df。它们的主要作用是显示当前如何使用存储空间。

### 使用 du 命令
[du](https://linux.die.net/man/1/du) 命令显示磁盘使用情况。它显示指定目录占用的存储容量，使您能够识别哪些目录使用最多的空间。例如，这些目录可能包含日志文件或用户数据。

与其他 Linux 命令一样，du 包含各种标志或选项来收集您正在寻找的信息。

标志： |
描述： |
-h | 人类友好的格式，例如 G 或 M（而不是字节） |
-s | 指定位置的总和，不包括每个文件/目录的大小 |
-c | 指定位置的总和以及每个文件/目录的大小 |
-a | 显示所有文件和目录 |
-t | 显示上次修改的时间 |
在这些选项中，我建议您最关注 -h 选项。此标志以人类可读的增量（如兆字节或千兆字节）显示已使用的空间。

![](https://cdn.thenewstack.io/media/2024/06/00b79038-du-withwithout-h.png)
键入以下命令以查看日志文件在系统上占用了多少空间：

1 |
$ du -hc /var/log |
![](https://cdn.thenewstack.io/media/2024/06/5d2a1fc8-du-c-total.png)
### 使用 df 命令
[df](https://linux.die.net/man/1/df) 命令显示可用存储空间，这与
du（已使用空间）。通常将这两个工具一起使用。例如，您可能需要知道特定磁盘分区上剩余的存储容量。df 命令及其相关选项会显示此信息。

标志 | 描述
------- | --------
-h | 人性化的格式，例如 G 或 M（而不是字节）
–total | 显示指定文件的总计
-l | 限制为本地文件系统，而不是远程文件系统

像 du 一样，df 也受益于 -h 选项，使结果更人性化和易读。以下示例假设您的主目录。

```
$ df -h
```

![](https://cdn.thenewstack.io/media/2024/06/6952afd3-df-h.png)

您会很快发现 du 和 df 是日常 Linux 管理的两个基本命令。

## 总结流程

依靠 du、df 和 lsblk 等工具来调查存储空间利用率。使用 -h 选项以人性化的格式显示大小。不要忘记，将 -l 或 -s 标志添加到 ls 命令也会提供文件大小信息。

我将总结向 Linux 系统添加和管理存储空间的过程。

- 物理安装存储介质（固态硬盘或硬盘驱动器）。
- 使用 lsblk 和 cat /proc/partitions 等命令识别它。
- 使用 parted 或 fdisk 对其进行分区。parted 更加强大。
- 使用 mkfs 命令添加文件系统。
- 使用 mkdir 命令创建一个目录作为挂载点。
- 使用 mount 命令将存储空间挂载到目录。
- 使用 df 和 du 命令检查存储空间。
- 设置标准的 Linux 权限（或访问控制列表）来控制对存储空间的访问。

## 总结

存储容量不是无限的，Linux 用户必须能够管理工作站和服务器上的磁盘空间。这种管理从识别新安装的存储驱动器开始，然后创建分区并将文件系统添加到其中以组织数据。管理员还将存储容量挂载到目录，使其可供最终用户使用。标准的 Linux 权限控制对该存储空间的访问。

除了配置之外，Linux 用户还必须分析存储空间的使用方式。du 和 df 命令对于此任务至关重要。这两个命令都依赖于强大的标志来显示您管理系统所需的确切信息。

请记住，在处理包含数据的任何分区时要非常小心。使用 fdisk 和 parted 等工具很容易出错，导致您丢失数据。最佳做法是从备份开始。

从今天开始使用 cat /proc/partitions、lsblk、du 和 df 检查您当前的存储使用情况。然后，如果需要，使用其他工具和命令在您的系统上配置额外的存储磁盘。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)