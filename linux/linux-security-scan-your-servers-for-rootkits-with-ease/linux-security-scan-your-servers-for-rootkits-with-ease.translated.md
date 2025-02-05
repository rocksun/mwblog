# Linux 安全：轻松扫描服务器中的Rootkit

![Linux 安全：轻松扫描服务器中的Rootkit 的特色图片](https://cdn.thenewstack.io/media/2025/01/121fc7d0-getty-images-fayapriipvq-unsplash-1024x683.jpg)

Linux 是地球上最安全的操作系统之一。但是，没有任何事情是绝对有保障的，如果服务器连接到网络，它就容易受到攻击……即使该服务器由 [Linux](https://thenewstack.io/learning-linux-start-here/) 驱动。总有人 [潜伏在暗处](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/)，希望访问这些服务器并利用它们来达到有利可图的目的。

存在恶意软件、勒索软件，以及也许最糟糕的 [rootkit](https://thenewstack.io/rootkits-come-to-containers-and-bring-trouble-with-them/)，它们是攻击者用来接管你的计算机的秘密安装的软件。它们似乎总是准备让你的公司倒闭。

幸运的是，在 Linux 中，你可以使用一些工具来扫描这些服务器中的 rootkit。

## 什么是 Rootkit？

对于那些不熟悉的人来说，rootkit 是一类恶意软件，它可以控制操作系统或设备并操纵其行为，同时隐藏其存在。

rootkit 的主要目标是防止安全软件、杀毒程序和其他监控工具检测到它，以便它可以继续执行其操作（这总是恶意的）。

Rootkit 通常在多个级别工作：

**低级系统操作**: Rootkit 可以更改底层系统文件、注册表项或内核模块以逃避检测。**内核模式操作**: 一些 rootkit 在所谓的内核模式下运行，以便它们可以访问系统资源的低级权限，并使其他软件更难以检测到它们的存在。**文件和进程隐藏**: Rootkit 几乎总是通过修改文件名、图标、进程、网络连接和其他关键服务来隐藏自己。

Rootkit 有两种不同的类型：

**Bootkit**: Bootkit 在启动时感染硬盘上的主引导记录 (MBR)，以防止系统从合法操作系统启动。**内核模式 rootkit**: 这些 rootkit 在内核模式下运行，可以拦截系统调用、操纵内存或创建虚假网络流量。

Rootkit 通常包括其他功能，例如网络活动监控、进程控制和数据加密。

现在你已经对 rootkit 有了基本的了解，让我们找出如何在 Linux 上扫描它们。

## Chkrootkit

Chkrootkit 是一款简单的 rootkit 检测器，它检查类 Unix 文件系统上各种感染迹象。[Chkrootkit](https://www.chkrootkit.org/) 可以使用以下命令从标准存储库安装在 [基于 Ubuntu 的系统](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) 上：

```bash
sudo apt-get install chkrootkit -y
```

在安装过程中，系统会询问你是否要配置 chkrootkit 以发送电子邮件警报。如果你决定这样做，请确保你有使用 SMTP 服务器所需的信息。如果没有，请选择仅限本地。

如果你使用的是基于 Fedora 的发行版，则安装命令为：

```bash
sudo dnf install chkrootkit -y
```

安装软件后，可以使用以下命令运行扫描：

```bash
sudo chkrootkit
```

该应用程序将立即启动并开始检查已知的 rootkit。完成后，你将看到它找到的所有内容（或希望没有找到）的报告。

你可以设置一个 cron 作业，让 chkrootkit 每晚（午夜）运行一次，使用以下命令：

```bash
sudo crontab -e
```

在文件的底部，添加以下内容：

```
0 0 * * * sudo chkrootkit | mail -s "Chkrootkit Report" EMAIL
```

Where EMAIL is your email address.

保存并关闭文件。你的系统现在将在午夜自动扫描 rootkit，并将报告发送到你配置的电子邮件地址。

## LMD

LMD 代表 Linux Malware Detect，是一款功能齐全的开源恶意软件扫描程序。LMD 具有完整的报告系统、电子邮件警报，并使用来自网络入侵检测系统的威胁数据来创建正在积极使用的恶意软件的签名。

LMD 最好的部分是它会定期更新，以跟上不断变化的野外恶意软件环境。

以下是安装 LMD 的步骤：

- 打开终端窗口。
- 使用命令 `wget http://www.rfxn.com/downloads/maldetect-current.tar.gz` 下载源代码。
- 使用 `tar xvzf maldetect-current.tar.gz` 解压缩存档。
- 使用 `cd maldetect` 进入 maldetect 目录。
- 使用命令 `sudo ./install.sh` 运行安装程序。
安装速度很快，一眨眼就完成了。

接下来，你需要配置 LDM。使用以下命令打开配置文件：

```bash
sudo nano /usr/local/maldetect/conf.maldet
```
本文件中包含许多自定义选项。例如，`quarantine_clean` 选项用于指示 LMD 自动清理任何检测到的恶意软件。将该选项设置为 1 以启用它。请仔细阅读整个文件并配置您所需的所有内容。完成后保存文件。

配置好 LMD 后，您可以使用以下命令启动手动扫描：

```bash
sudo maldet -a /
```

您也可以指定要扫描的特定目录。如果您选择扫描根目录（/）下的所有内容，请注意这将需要一些时间才能完成。例如，在我的 Ubuntu Server 24.04 实例上，有超过 62000 个文件需要扫描。

另一个不错的功能是能够监控目录更改。例如，您可以像这样监控 `/etc` 目录：

```bash
sudo maldet --monitor /etc
```

需要注意的是，如果您使用监控选项，则还需要使用以下命令安装 inotify-tools：

```bash
sudo apt-get install inotify-tools -y
```

监控选项运行后，您可以在 `/usr/local/maldetect/logs/inotify_log` 中找到日志。请定期阅读该文件以查看 `/etc` 中是否有任何更改。该日志文件实时更新，因此只要有任何更改，它就会被写入文件。

您还可以使用以下命令列出隔离的文件：

```bash
sudo maldet -l
```

要使用 LMD 安排每日扫描，您将使用 cronjob。如果您希望该扫描每天午夜运行，您可以将必要的行添加到 cron 中。使用 `sudo` 打开 `crontab` 进行编辑：

```bash
sudo crontab -e
```

在该文件的底部，添加以下内容：

您的 Linux 服务器现在正在监控 rootkit。永远不要假设，仅仅因为它是 Linux，这些服务器就能保证不会被黑客入侵。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等等。