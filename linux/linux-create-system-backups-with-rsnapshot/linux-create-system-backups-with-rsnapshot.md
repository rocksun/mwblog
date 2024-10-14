
<!--
title: Linux：使用rsnapshot创建系统备份
cover: https://cdn.thenewstack.io/media/2024/10/6e91333c-getty-images-bhjklypz8fy-unsplash.jpg
-->

Rsnapshot 是一个广泛使用的 rsync 工具的包装器，安装和配置非常容易。从这里开始了解更多信息。

> 译自 [Linux: Create System Backups With rsnapshot](https://thenewstack.io/linux-create-system-backups-with-rsnapshot/)，作者 Jack Wallen。

数据可靠性的一个步骤是定期备份数据。您永远不知道服务器或桌面何时会发生故障，导致关键文件或配置丢失。为了避免这种噩梦，您可能需要考虑使用一个工具来处理本地和远程文件系统的增量备份。

rsnapshot 就是这样一个工具，它利用硬链接，因此只有在必要时才会使用磁盘空间。rsnapshot 作为广泛使用的 [rsync 工具](https://thenewstack.io/linux-synchronize-local-and-remote-directories-with-rsync/) 的包装器，安装和配置相当容易。

我将引导您完成在 [Ubuntu Server 22.04](https://thenewstack.io/how-to-safely-upgrade-ubuntu-22-04-to-ubuntu-24-04/) 上安装和配置 rsnapshot 的过程，但您也可以在大多数基于 Debian 的发行版以及基于 Fedora 的发行版上使用此应用程序。

## 您需要什么

您唯一需要的是一个正在运行的 Ubuntu Server 实例和一个具有 [sudo 权限](https://thenewstack.io/linux-understand-sudo-to-rule-your-server/) 的用户。由于 rsnapshot 也可以备份到外部驱动器，因此您也可以考虑连接这样的驱动器以获得更好的备份可靠性。毕竟，如果您的操作系统崩溃并导致机器无法启动，如果您的备份存储在包含操作系统的驱动器上，您也可能会丢失这些备份。

例如，您可以连接一个外部驱动器并将其挂载到一个名为 */backup* 的新目录，这正是我将在本文中演示的内容。为了实现这一点，您可能还想配置该驱动器在启动时自动挂载，这将需要在 */etc/fstab* 文件中添加类似以下内容的行：

```
/dev/disk/by-uuid/13557fad-d203-4448-991b-c8011907dc1d /backup auto rw,nosuid,nodev,nofail,x-gvfs-show 0 0
```

请确保使用您特定的驱动器 UUID 以及您喜欢的任何选项来自动挂载驱动器。

话虽如此，让我们开始安装。

## 安装 rsnapshot

rsnapshot 包可以从标准存储库中使用以下命令安装：

```
sudo apt-get install rsnapshot -y
```

如果您使用的是基于 Fedora 的发行版，则安装命令为：

```
sudo dnf install rsnapshot -y
```

如果您的选择是 Arch Linux，则命令为：

```
sudo pacman -S rsnapshot
```

这应该安装所有依赖项。如果您发现 rsync 未安装，请使用以下命令安装：

- Ubuntu：`sudo apt-get install rsync -y`
- Fedora：`sudo dnf install rsync -y`
- Arch：`sudo pacman -S rsync`

## 配置 rsnapshot

现在 rsnapshot 已安装，是时候配置它了。需要注意的一点（这一点非常重要）是，您不能在配置文件中使用空格；如果您这样做，会导致语法错误。相反，如果需要，[使用制表符](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go/)。

使用以下命令打开配置文件：

```
sudo nano /etc/rsnapshot.conf
```

您要查找的第一行是：

```
snapshot_root /var/cache/rsnapshot/
```

在基于 Fedora 的发行版上，该行可能显示为：

```
snapshot_root /snapshots/
```

上面的行配置了将存放备份的目录。例如，如果您按照我的建议将外部驱动器挂载到 */backup*，则该行将为：

```
snapshot_root /backup
```

您还需要禁用根目录的创建；否则，您最终会得到一个带有 */backup* 的子目录。要禁用此功能，请查找以下行：

```
#no_create_root 1
```

通过删除 # 字符来取消注释该行，使结果看起来像这样：

```
no_create_root 1
```

您需要知道 rsync 可执行文件的路径，可以使用以下命令找到：

```
which rsync
```

结果应该是 */usr/bin/rsync*。如果结果是其他内容，请注意，因为您必须在以下行中配置该路径：

```
cmd_rsync /usr/bin/rsync
```

接下来，我们需要设置保留策略。这在配置文件的 BACKUP LEVELS / INTERVALS 部分中处理，您将在其中看到以下默认选项：

```
retain alpha 6
retain beta 7
retain gamma 4
```

上面的名称是任意的，数字表示将保留该类型的备份数量。您可以根据需要更改名称，但请记住，它们应该按升序排列，并且您选择的名称将用于运行特定的备份。您可以将这些名称从 alpha、beta 和 gamma 更改为 daily、weekly 和 monthly，这样更有意义。

要配置的下一部分是您要备份的内容。此部分列在 #LOCALHOST 下（在配置文件的底部附近），您将在其中找到以下内容：

```
backup  /home/          localhost/
backup  /etc/           localhost/
backup  /usr/local/     localhost/
```

你可以将备份目录更改为您需要的任何内容，但保留 localhost/ 不变；这指示 rsnapshot 我们正在备份到本机。也可以从备份中排除和包含文件。

这在 LOCALHOST 部分的上方进行处理，您将在那里看到以下内容：

```
#include        ???
#include        ???
#exclude        ???
#exclude        ???
````

例如，您可能有一些不想包含在备份中的特定文件。为此，请确保使用要排除文件的直接路径创建一个排除行。

完成上述操作后，使用 Ctrl+X 键盘快捷键保存并关闭文件。

## 测试配置

在启动备份之前，您应该使用以下命令测试配置文件的语法：

```bash
sudo rsnapshot configtest
```

如果命令返回 `Syntax OK`，则可以继续。

让我们对每日备份（我在配置文件中使用 alpha 代替）进行测试。要运行测试，请发出以下命令：

```
sudo rsnapshot -t daily
```

您将看到类似于以下内容的输出：

```
echo 28061 &gt; /var/run/rsnapshot.pid
mkdir -m 0755 -p /backup/daily.0/
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /home/ /backup/daily.0/localhost/
mkdir -m 0755 -p /backup/daily.0/
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded /etc/ \
    /backup/daily.0/localhost/
mkdir -m 0755 -p /backup/daily.0/
/usr/bin/rsync -a --delete --numeric-ids --relative --delete-excluded \
    /usr/local/ /backup/daily.0/localhost/
touch /backup/daily.0/
```

要运行第一次备份，请发出以下命令：

```
sudo rsnapshot daily
```

备份完成后，您将在 */backup* 中找到一个名为 `daily.0` 的子目录，其中包含快照。

## 计划备份

[Rsnapshot](https://rsnapshot.org/) 不包含内置的调度程序，因此您必须使用 cron。我们将创建三个条目 - 每天、每周和每月各一个。发出以下命令：

```
sudo crontab -e
```

在文件底部，添加以下行：

```
0 1 * * * root /usr/bin/rsnapshot daily
0 5 * * 6 root /usr/bin/rsnapshot weekly
0 2 1 * * root /usr/bin/rsnapshot monthly
```

以上行执行以下操作：

- 在凌晨 1 点进行每日快照。
- 每个星期六进行每周快照。
- 每个月的第一天凌晨 2 点进行每月快照。

就是这样。您现在拥有一个备份系统，它将自动对配置的目录进行快照，并将它们保存到您选择的目的地。
